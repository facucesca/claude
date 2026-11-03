"""Motor de dibujo de los kits: piezas, acomodo en la hoja de corte (SVG/DXF) y vistas 3D.

Coordenadas del auto (mm): x a lo largo (0 = trompa, 200 = cola), y a lo ancho
(0 = centro, negativo = lado izquierdo), z hacia arriba (0 = suelo).
"""
import math
from dataclasses import dataclass, field

from shapely import affinity
from shapely.geometry import (GeometryCollection, LineString, MultiLineString, MultiPolygon,
                              Point, Polygon, box)
from shapely.ops import unary_union
from shapely.strtree import STRtree

T = 3.0                    # espesor del material (se cambia con configurar)
R_EJE, R_AJUSTE = 1.75, 1.4   # agujero del eje en los costados (gira) y en ruedas/polea (a presión)
MADERA, BORDE = "#e6c391", "#8a6239"
NUEVO, BORDE_NUEVO = "#ffc96b", "#b36b00"
NORMAL = {"xz": (0, 1, 0), "xy": (0, 0, 1), "yz": (1, 0, 0)}


def configurar(t):
    global T
    T = float(t)


def poligonos(g):
    if g is None or g.is_empty:
        return []
    if isinstance(g, Polygon):
        return [g]
    return [q for q in getattr(g, "geoms", []) if isinstance(q, Polygon) and q.area > 3]


# --- piezas -------------------------------------------------------------------------
@dataclass
class Pieza:
    geom: Polygon                 # forma para cortar (coordenadas locales)
    nombre: str
    plano: str = "xz"             # plano de la pieza en el auto: xz, xy o yz
    pos: float = 0.0              # dónde empieza a lo largo de la normal
    grab: list = field(default_factory=list)
    tipo: str = "chasis"
    espejo: bool = False
    etiqueta: str = ""            # texto grabado en la pieza ("" = sin texto)
    g3d: Polygon = None           # forma ubicada en el auto (si difiere de geom)
    t: float = None               # espesor (None = material)
    color: str = None
    cortar: bool = True           # False = solo para los dibujos (electrónica)
    capa: int = None
    pri: int = None               # orden de dibujo forzado (solo para las vistas)

    def espesor(self):
        return T if self.t is None else self.t


def redondear(p, r=1.2):
    return p.buffer(-r, 8).buffer(r, 8) if r else p


def para_hoja(pz):
    """Forma y grabados listos para la hoja (y hacia abajo, espejo si hace falta)."""
    g, grab = pz.geom, list(pz.grab)
    textos = list(getattr(pz, "textos", []))
    if pz.espejo:
        cx = (g.bounds[0] + g.bounds[2]) / 2
        g = affinity.scale(g, -1, 1, origin=(cx, 0))
        grab = [affinity.scale(e, -1, 1, origin=(cx, 0)) for e in grab]
        textos = [(s, 2 * cx - x, y, h) for s, x, y, h in textos]
    g = affinity.scale(g, 1, -1, origin=(0, 0))
    grab = [affinity.scale(e, 1, -1, origin=(0, 0)) for e in grab]
    textos = [(s, x, -y, h) for s, x, y, h in textos]
    return g, grab, textos


def acomodar(piezas, hoja=(600, 400), margen=6, sep=2.5, paso=4.0):
    """Acomoda las piezas en hojas, buscando el lugar más arriba y a la izquierda.
    Prueba girar 180° (y 90° las piezas chicas) para que encastren mejor."""
    W, H = hoja
    hojas = []
    pendientes = [p for p in piezas if p.cortar]
    pendientes.sort(key=lambda p: -p.geom.area)
    actuales, formas = [], []
    tree = None

    def libre(c):
        if tree is None:
            return True
        for i in tree.query(c):
            if formas[i].intersects(c):
                return False
        return True

    for pz in pendientes:
        g0, grab0, textos0 = para_hoja(pz)
        b = g0.bounds
        chica = max(b[2] - b[0], b[3] - b[1]) < 120
        angulos = (0, 180, 90, 270) if chica else (0, 180)
        mejor = None
        for intento in range(2):
            for ang in angulos:
                g = affinity.rotate(g0, ang, origin=(0, 0))
                gb = g.bounds
                g = affinity.translate(g, -gb[0], -gb[1])
                w, h = gb[2] - gb[0], gb[3] - gb[1]
                if w > W - 2 * margen or h > H - 2 * margen:
                    continue
                gc = g.simplify(0.15).buffer(sep / 2, 4)
                x = margen
                while x + w <= W - margen + 1e-6:
                    y = margen
                    while y + h <= H - margen + 1e-6:
                        if mejor and (y, x) >= mejor[0]:
                            break
                        c = affinity.translate(gc, x, y)
                        if libre(c):
                            # subir de a poco para quedar bien pegado
                            while y - 0.5 >= margen and libre(affinity.translate(gc, x, y - 0.5)):
                                y -= 0.5
                            if not mejor or (y, x) < mejor[0]:
                                mejor = ((y, x), ang, gb, x, y, gc)
                            break
                        y += paso
                    x += paso
            if mejor or not actuales:
                break
            hojas.append(actuales)  # no entra: hoja nueva
            actuales, formas, tree = [], [], None
        if not mejor:
            raise RuntimeError(f"la pieza {pz.nombre} no entra en la hoja")
        _, ang, gb, x, y, gc = mejor

        def ubicar(e, ang=ang, gb=gb, x=x, y=y):
            e = affinity.rotate(e, ang, origin=(0, 0))
            return affinity.translate(e, x - gb[0], y - gb[1])

        textos = []
        for s, tx, ty, th in textos0:
            pt = ubicar(Point(tx, ty))
            textos.append((s, pt.x, pt.y, th, ang))
        actuales.append(dict(pz=pz, geom=ubicar(g0), grab=[ubicar(e) for e in grab0],
                             textos=textos, ang=ang))
        formas.append(affinity.translate(gc, x, y))
        tree = STRtree(formas)
    if actuales:
        hojas.append(actuales)
    return hojas


# --- salida SVG / DXF -----------------------------------------------------------
def anillos(g):
    if isinstance(g, Polygon):
        return [(list(g.exterior.coords), True)] + [(list(i.coords), True) for i in g.interiors]
    if isinstance(g, (MultiPolygon, GeometryCollection, MultiLineString)):
        return [r for q in g.geoms for r in anillos(q)]
    if isinstance(g, LineString):
        c = list(g.coords)
        return [(c, len(c) > 2 and c[0] == c[-1])]
    return []


def d_svg(ring, cerrado):
    s = "M" + " L".join(f"{a:.2f},{b:.2f}" for a, b in ring)
    return s + (" Z" if cerrado else "")


def lugar_texto(pz, geom, alto):
    """Punto adentro de la pieza para grabar el número (en la parte baja, que queda tapada)."""
    pt = geom.buffer(-alto).representative_point() if not geom.buffer(-alto).is_empty \
        else geom.representative_point()
    return pt


def guardar_hoja(base, n, hoja, tam=(600, 400), titulo=""):
    import ezdxf
    W, H = tam
    svg = [f'<svg xmlns="http://www.w3.org/2000/svg" width="{W}mm" height="{H}mm" '
           f'viewBox="0 0 {W} {H}">', f'<rect width="{W}" height="{H}" fill="#fff"/>',
           f'<rect x="0.5" y="0.5" width="{W-1}" height="{H-1}" fill="none" stroke="#999" '
           'stroke-width="0.3" stroke-dasharray="3 2"/>']
    corte, linea, relleno, textos, notas = [], [], [], [], []
    doc = ezdxf.new()
    for nombre, color in (("CORTAR", 1), ("GRABAR", 5), ("GRABAR_RELLENO", 4)):
        doc.layers.add(nombre, color=color)
    msp = doc.modelspace()
    largo_corte, area_relleno = 0.0, 0.0
    for it in hoja:
        pz, g = it["pz"], it["geom"]
        for r, c in anillos(g):
            corte.append(f'<path d="{d_svg(r, True)}"/>')
            msp.add_lwpolyline([(a, H - b) for a, b in r], close=True, dxfattribs={"layer": "CORTAR"})
        largo_corte += g.length
        for e in it["grab"]:
            lleno = isinstance(e, (Polygon, MultiPolygon)) and e.area > 20
            if lleno:
                area_relleno += e.area
            for r, c in anillos(e):
                (relleno if lleno else linea).append(f'<path d="{d_svg(r, c or lleno)}"/>')
                msp.add_lwpolyline([(a, H - b) for a, b in r], close=c or lleno,
                                   dxfattribs={"layer": "GRABAR_RELLENO" if lleno else "GRABAR"})
        for s, x, y, h, ang in it["textos"]:
            textos.append(f'<text x="{x:.1f}" y="{y:.1f}" font-size="{h}" text-anchor="middle" '
                          f'transform="rotate({ang} {x:.1f} {y:.1f})">{s}</text>')
            msp.add_text(s, height=h * 0.8, rotation=-ang, dxfattribs={"layer": "GRABAR"}
                         ).set_placement((x, H - y), align=ezdxf.enums.TextEntityAlignment.BOTTOM_CENTER)
        if pz.etiqueta:
            pt = lugar_texto(pz, g, 2.2)
            textos.append(f'<text x="{pt.x:.1f}" y="{pt.y + 1.1:.1f}" font-size="3" '
                          f'text-anchor="middle">{pz.etiqueta}</text>')
            msp.add_text(pz.etiqueta, height=2.4, dxfattribs={"layer": "GRABAR"}).set_placement(
                (pt.x, H - pt.y - 1.1), align=ezdxf.enums.TextEntityAlignment.BOTTOM_CENTER)
        x0, y0 = g.bounds[0], g.bounds[1]
        nota = pz.nombre + (" (espejo)" if pz.espejo else "")
        notas.append(f'<text x="{x0:.1f}" y="{max(y0 - 0.5, 2.5):.1f}" font-size="2.4">{nota}</text>')
    svg.append('<g id="CORTAR" fill="none" stroke="#ff0000" stroke-width="0.1">')
    svg += corte
    svg.append('</g><g id="GRABAR_RELLENO" fill="#0000ff" fill-opacity="0.35" stroke="#0000ff" '
               'stroke-width="0.1">')
    svg += relleno
    svg.append('</g><g id="GRABAR" fill="none" stroke="#0000ff" stroke-width="0.25">')
    svg += linea
    svg.append('</g><g id="GRABAR_TEXTOS" fill="#0000ff" stroke="none" font-family="Arial">')
    svg += textos
    svg.append('</g><g id="NOTAS_no_grabar" fill="#999" font-family="Arial">')
    svg += notas
    svg.append(f'<text x="8" y="{H-3}" font-size="4">{titulo} - hoja {n} - ROJO=cortar  '
               f'AZUL=grabar (relleno = grabado lleno)  GRIS=notas, no grabar - material {T:g} mm'
               '</text></g></svg>')
    open(f"{base}-{n}.svg", "w").write("\n".join(svg))
    doc.saveas(f"{base}-{n}.dxf")
    return largo_corte, area_relleno


# --- dibujo 3D ----------------------------------------------------------------------

class Camara:
    def __init__(self, az=-125, el=28):
        a, e = math.radians(az), math.radians(el)
        self.c = (math.cos(e) * math.cos(a), math.cos(e) * math.sin(a), math.sin(e))
        cx, cy, cz = self.c
        n = math.hypot(cx, cy)
        self.r = (-cy / n, cx / n, 0.0)
        rx, ry, rz = self.r
        self.u = (cy * rz - cz * ry, cz * rx - cx * rz, cx * ry - cy * rx)

    def p(self, x, y, z):
        return (x * self.r[0] + y * self.r[1] + z * self.r[2],
                x * self.u[0] + y * self.u[1] + z * self.u[2])

    def prof(self, x, y, z):
        return x * self.c[0] + y * self.c[1] + z * self.c[2]


def a_3d(plano, pos, u, v):
    if plano == "xz":
        return (u, pos, v)
    if plano == "xy":
        return (u, v, pos)
    return (pos, u, v)


class Escena:
    def __init__(self, cam=None, por_capas=False):
        self.cam = cam or Camara()
        self.por_capas = por_capas   # ordenar por posición a lo ancho (capas paralelas)
        self.objs = []   # (prioridad, profundidad, lista de (puntos 2D, fill, stroke, sw, op))

    def prisma(self, geom, plano, pos, t, fill=MADERA, stroke=BORDE, sw=0.6, op=1.0,
               prioridad=0, grab=(), desplazar=(0, 0, 0), prof=None):
        cam = self.cam
        dx, dy, dz = desplazar
        n = NORMAL[plano]
        frente = sum(a * b for a, b in zip(n, cam.c)) > 0
        cara = pos + t if frente else pos
        caras = []

        def P(u, v, w):
            x, y, z = a_3d(plano, w, u, v)
            return (x + dx, y + dy, z + dz)

        geom = geom.simplify(0.3)
        for q in poligonos(geom) if not isinstance(geom, Polygon) else [geom]:
            # costados que miran a la cámara
            for ring in [q.exterior] + list(q.interiors):
                c = list(ring.coords)
                for (u1, v1), (u2, v2) in zip(c, c[1:]):
                    a, b = P(u1, v1, pos), P(u2, v2, pos)
                    a2, b2 = P(u1, v1, pos + t), P(u2, v2, pos + t)
                    e = (b[0] - a[0], b[1] - a[1], b[2] - a[2])
                    m = (a2[0] - a[0], a2[1] - a[1], a2[2] - a[2])
                    nn = (e[1] * m[2] - e[2] * m[1], e[2] * m[0] - e[0] * m[2], e[0] * m[1] - e[1] * m[0])
                    caras.append(([cam.p(*a), cam.p(*b), cam.p(*b2), cam.p(*a2)], nn))
            sides = []
            for pts, nn in caras:
                sides.append((pts, nn))
            caras = []
            # la cara de adelante (con agujeros)
            ext = [cam.p(*P(u, v, cara)) for u, v in q.exterior.coords]
            hol = [[cam.p(*P(u, v, cara)) for u, v in i.coords] for i in q.interiors]
            if prof is not None:
                pr = prof
            elif self.por_capas:
                cy = (pos + t / 2) if plano == "xz" else (q.centroid.y if plano == "xy" else
                                                        q.centroid.x)
                pr = cam.c[1] * (cy + dy) + 1e-4 * self._prof(q, plano, pos + t / 2, desplazar)
            else:
                pr = self._prof(q, plano, pos + t / 2, desplazar)
            self.objs.append(dict(pri=prioridad, prof=pr,
                                  sides=sides, ext=ext, hol=hol, fill=fill, stroke=stroke, sw=sw,
                                  op=op, grab=[[cam.p(*P(u, v, cara)) for u, v in r]
                                               for e in grab for r, _ in anillos(e)],
                                  grab_lleno=[isinstance(e, Polygon) and e.area > 20 for e in grab
                                              for _ in anillos(e)]))

    def _prof(self, q, plano, w, d):
        c = q.centroid
        x, y, z = a_3d(plano, w, c.x, c.y)
        return self.cam.prof(x + d[0], y + d[1], z + d[2])

    def pieza(self, pz, **kw):
        g = pz.g3d if pz.g3d is not None else pz.geom
        grab = pz.grab
        if pz.g3d is not None:  # misma traslación para los grabados
            dx = pz.g3d.bounds[0] - pz.geom.bounds[0]
            dz = pz.g3d.bounds[1] - pz.geom.bounds[1]
            grab = [affinity.translate(e, dx, dz) for e in grab]
        kw.setdefault("fill", pz.color or MADERA)
        if pz.nombre == "PISO":
            kw.setdefault("prioridad", -1)
        if pz.pri is not None:
            kw.setdefault("prioridad", pz.pri)
        self.prisma(g, pz.plano, pz.pos, pz.espesor(), grab=grab, **kw)

    def caja(self, x0, y0, z0, x1, y1, z1, fill, stroke="#333", **kw):
        self.prisma(box(x0, y0, x1, y1), "xy", z0, z1 - z0, fill=fill, stroke=stroke, **kw)

    def linea(self, pts3d, color, ancho=1.6, prioridad=0):
        cam = self.cam
        if self.por_capas:
            pr = cam.c[1] * sum(p[1] for p in pts3d) / len(pts3d)
        else:
            pr = sum(cam.prof(*p) for p in pts3d) / len(pts3d)
        self.objs.append(dict(pri=prioridad, prof=pr, linea=[cam.p(*p) for p in pts3d],
                              color=color, ancho=ancho))

    def texto(self, p3d, s, tam=14, color="#222"):
        self.objs.append(dict(pri=99, prof=0, texto=(self.cam.p(*p3d), s, tam, color)))

    def svg(self, ancho=900, alto=560, fondo="#ffffff", titulo=None, margen=30):
        xs, ys = [], []
        for o in self.objs:
            pts = list(o.get("ext") or o.get("linea") or [])
            for lado, _ in o.get("sides", []):
                pts += lado
            xs += [p[0] for p in pts]
            ys += [p[1] for p in pts]
        if not xs:
            return ""
        top = 60 if titulo else 0
        esc = min((ancho - 2 * margen) / (max(xs) - min(xs)),
                  (alto - 2 * margen - top) / (max(ys) - min(ys)))
        ox = (ancho - esc * (max(xs) + min(xs))) / 2
        oy = top + (alto - top + esc * (max(ys) + min(ys))) / 2

        def f(pts):
            return " ".join(f"{ox + esc * a:.1f},{oy - esc * b:.1f}" for a, b in pts)

        out = [f'<svg xmlns="http://www.w3.org/2000/svg" width="{ancho}" height="{alto}" '
               f'viewBox="0 0 {ancho} {alto}" font-family="Arial, sans-serif">',
               f'<rect width="{ancho}" height="{alto}" fill="{fondo}"/>']
        if titulo:
            out.append(f'<text x="24" y="40" font-size="26" font-weight="bold" fill="#3b2a1a">'
                       f'{titulo}</text>')
        for o in sorted(self.objs, key=lambda o: (o["pri"], o["prof"])):
            if "texto" in o:
                (a, b), s, tam, col = o["texto"]
                out.append(f'<text x="{ox + esc * a:.1f}" y="{oy - esc * b:.1f}" font-size="{tam}" '
                           f'fill="{col}" font-weight="bold" text-anchor="middle">{s}</text>')
                continue
            if "linea" in o:
                out.append(f'<polyline points="{f(o["linea"])}" fill="none" stroke="{o["color"]}" '
                           f'stroke-width="{o["ancho"]}" stroke-linejoin="round" stroke-linecap="round"/>')
                continue
            op = f' opacity="{o["op"]}"' if o["op"] < 1 else ""
            g = [f"<g{op}>"]
            for pts, _ in o["sides"]:
                g.append(f'<polygon points="{f(pts)}" fill="{o["fill"]}" stroke="{o["stroke"]}" '
                         f'stroke-width="{o["sw"] * 0.6}" stroke-linejoin="round"/>')
            d = "M" + f(o["ext"]) + " Z" + "".join(" M" + f(h) + " Z" for h in o["hol"])
            g.append(f'<path d="{d}" fill="{o["fill"]}" fill-rule="evenodd" stroke="{o["stroke"]}" '
                     f'stroke-width="{o["sw"]}" stroke-linejoin="round"/>')
            for pts, lleno in zip(o["grab"], o["grab_lleno"]):
                if lleno:
                    g.append(f'<polygon points="{f(pts)}" fill="#3c4650" stroke="#2a3138" '
                             'stroke-width="0.5" opacity="0.9"/>')
                else:
                    g.append(f'<polyline points="{f(pts)}" fill="none" stroke="#9c7243" '
                             'stroke-width="0.9"/>')
            g.append("</g>")
            out += g
        out.append("</svg>")
        return "\n".join(out)
