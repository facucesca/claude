"""Motor del kit de autos: chasis común, carrocerías en capas, hojas de corte e imágenes 3D.

Coordenadas del auto (mm): x a lo largo (0 = trompa, 200 = cola), y a lo ancho
(0 = centro, negativo = lado izquierdo), z hacia arriba (0 = piso).
Todas las carrocerías se apoyan sobre el mismo chasis.
"""
import math
from dataclasses import dataclass, field

from shapely import affinity
from shapely.geometry import (GeometryCollection, LineString, MultiLineString, MultiPolygon,
                              Point, Polygon, box)
from shapely.ops import unary_union
from shapely.strtree import STRtree

# --- medidas generales ------------------------------------------------------
T = 3.0                    # espesor del material (se cambia con configurar)
ANCHO = 84.0               # ancho de la carrocería
N = 28                     # capas de carrocería
LARGO = 200.0

EJE_DEL, EJE_TRAS, Z_EJE = 46.0, 156.0, 16.0
R_RUEDA, R_CANAL, R_CUBIERTA = 15.5, 13.0, 16.1
R_ARCO, R_EJE, R_AJUSTE, R_PERNO = 17.8, 1.75, 1.4, 1.6
Y_RUEDA = (29.5, 38.5)     # |y| que ocupa cada rueda (3 discos)
Y_CAVIDAD = 27.0           # las capas con |y| < 27 tienen el hueco del chasis

# chasis
X0, X1 = 26.0, 194.0
Z_PISO = 5.0
Y_PISO = 26.5
Y_LARG = (20.5, 23.5)
TECHO = [(25.5, 62.0, 22.0), (62.0, 142.0, 26.5), (142.0, 170.0, 28.0), (170.0, 194.5, 26.5)]
TABS_LARG = [(34, 44), (86, 100), (162, 176)]
X_TRAV = (29.0, 188.0)
TABS_TRAV_Y = [(-14, -6), (6, 14)]
CANAL_X, CANAL_Y = (171.5, 188.5), 15.0
BOTON = (180.0, 0.0)
TORRE_Y = (9.0, 12.0)
MOTOR = dict(x=(125.8, 146.2), y=(-20.0, 5.0), alto=15.4)   # motor 130 acostado
SOPORTE_Y = -9.0
POLEA_Y = (7.0, 16.0)
PILAS = (63.0, -20.0, 121.0, 12.0)                         # portapilas 2xAA (x0, y0, x1, y1)
BORNES = [(48, -19, 61, -1), (48, 1, 61, 19), (100, 12.5, 118, 20.5)]


def configurar(t):
    global T, N
    T = float(t)
    N = round(ANCHO / T)


def zp():
    return Z_PISO + T            # cara de arriba del piso


def techo(x):
    for a, b, h in TECHO:
        if a <= x < b:
            return h
    return TECHO[-1][2]


def zona_techo(x0=X0, x1=X1, z0=None):
    z0 = zp() if z0 is None else z0
    return unary_union([box(max(a, x0), z0, min(b, x1), h) for a, b, h in TECHO
                        if min(b, x1) > max(a, x0)])


def cavidad():
    return unary_union([box(a, -10, b, h) for a, b, h in TECHO])


# --- curvas -------------------------------------------------------------------
def suave(pts, n=10):
    """Curva Catmull-Rom que pasa por los puntos."""
    out = []
    for i in range(len(pts) - 1):
        p0, p1 = pts[max(i - 1, 0)], pts[i]
        p2, p3 = pts[i + 1], pts[min(i + 2, len(pts) - 1)]
        for j in range(n):
            t = j / n
            t2, t3 = t * t, t * t * t
            out.append(tuple(0.5 * ((2 * p1[k]) + (-p0[k] + p2[k]) * t
                                    + (2 * p0[k] - 5 * p1[k] + 4 * p2[k] - p3[k]) * t2
                                    + (-p0[k] + 3 * p1[k] - 3 * p2[k] + p3[k]) * t3)
                             for k in (0, 1)))
    out.append(pts[-1])
    return out


def silueta(techo_pts, cola, nariz):
    """Perfil cerrado: línea de arriba (trompa a cola), cola hacia abajo, piso, trompa."""
    pts = suave(techo_pts) + suave(cola)[1:] + suave(nariz)[:-1]
    return Polygon(pts).buffer(0)


def arriba(p, z):
    return p.intersection(box(-50, z, 300, 300))


def abajo(p, z):
    return p.intersection(box(-50, -50, 300, z))


def poligonos(g):
    if g is None or g.is_empty:
        return []
    if isinstance(g, Polygon):
        return [g]
    return [q for q in getattr(g, "geoms", []) if isinstance(q, Polygon) and q.area > 3]


# --- capas ------------------------------------------------------------------------
def tramo(k):
    return (-ANCHO / 2 + k * T, -ANCHO / 2 + (k + 1) * T)


def toca(k, y0, y1):
    a, b = tramo(k)
    return a < y1 - 1e-6 and b > y0 + 1e-6


def con_cavidad(k):
    return toca(k, -Y_CAVIDAD, Y_CAVIDAD)


def desde_afuera(k):
    return min(k, N - 1 - k)


def y_centro(k):
    a, b = tramo(k)
    return abs((a + b) / 2)


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


def tabs_a_caja(lista):
    return unary_union([box(*b) for b in lista])


def redondear(p, r=1.2):
    return p.buffer(-r, 8).buffer(r, 8) if r else p


def chasis(H):
    """Piezas del chasis. H = altura de la tapa de la torre del botón (depende del modelo)."""
    Z1 = zp()
    yl0, yl1 = Y_LARG
    out = []

    # piso
    piso = box(X0, -Y_PISO, X1, Y_PISO)
    ranuras = []
    for a, b in TABS_LARG:
        ranuras += [(a, yl0, b, yl1), (a, -yl1, b, -yl0)]
    for x in X_TRAV:
        ranuras += [(x, y0, x + T, y1) for y0, y1 in TABS_TRAV_Y]
    ranuras += [(175, TORRE_Y[0], 185, TORRE_Y[1]), (175, -TORRE_Y[1], 185, -TORRE_Y[0])]
    ranuras += [(122.4, SOPORTE_Y, 125.4, SOPORTE_Y + T), (146.6, SOPORTE_Y, 149.6, SOPORTE_Y + T)]
    ranuras += [(144, POLEA_Y[0] - 1.5, 168, POLEA_Y[1] + 1.5)]   # paso de la polea
    piso = redondear(piso, 2).difference(tabs_a_caja(ranuras))
    grab = [box(*PILAS).exterior, box(MOTOR["x"][0], MOTOR["y"][0], MOTOR["x"][1],
                                      MOTOR["y"][1]).exterior]
    grab += [box(*b).exterior for b in BORNES]
    cables = [  # recorridos sugeridos de los cables
        [(63, -12), (61.5, -12)],                                  # pila + a borne 1
        [(66, 8), (66, 16.5), (100, 16.5)],                        # pila - a borne 3
        [(176, -15.5), (70, -15.5), (61.5, -15.5)],                # botón a borne 1
        [(176, -17.5), (64, -17.5), (64, 10), (61.5, 10)],         # botón a borne 2
        [(128, -19), (124, -19), (124, -19.6)],                    # motor
        [(128, 2), (124, 2), (124, 14.5), (118.5, 14.5)],          # motor a borne 3
    ]
    grab += [LineString(c) for c in cables]
    textos = [("PILAS 2xAA", 76, -6, 4), ("MOTOR", 129, -9, 3), ("B1", 51.5, -12, 3.2),
              ("B2", 51.5, 8, 3.2), ("B3", 105, 15, 3), ("+", 64.5, -14, 3.5),
              ("-", 67.5, 9, 3.5), ("BOTÓN", 172, -2, 3), ("FRENTE", 31, 18, 3)]
    out.append(Pieza(piso, "PISO", "xy", Z_PISO, grab, etiqueta="", tipo="chasis"))
    out[-1].textos = textos

    # largueros (los dos iguales)
    larg = zona_techo().union(tabs_a_caja([(a, Z_PISO, b, Z1) for a, b in TABS_LARG]))
    larg = larg.difference(tabs_a_caja([(x, 12, x + T, 18) for x in X_TRAV]))
    for x in (EJE_DEL, EJE_TRAS):
        larg = larg.difference(Point(x, Z_EJE).buffer(R_EJE, 24))
    for pos, n in ((-yl1, "LARGUERO IZQ"), (yl0, "LARGUERO DER")):
        out.append(Pieza(larg, n, "xz", pos, etiqueta="L", tipo="chasis"))

    # travesaños
    for x, n in ((X_TRAV[0], "TRAVESAÑO DEL"), (X_TRAV[1], "TRAVESAÑO TRAS")):
        h = techo(x + T / 2)
        g = box(-yl0, Z1, yl0, h)
        g = g.union(tabs_a_caja([(-yl1, 12, -yl0, 18), (yl0, 12, yl1, 18)]))
        g = g.union(tabs_a_caja([(a, Z_PISO, b, Z1) for a, b in TABS_TRAV_Y]))
        out.append(Pieza(g, n, "yz", x, etiqueta="TD" if x < 100 else "TT", tipo="chasis"))

    # soporte del motor (abraza al motor desde arriba)
    mx0, mx1 = MOTOR["x"]
    g = box(122, Z1, 150, 26).difference(box(mx0, Z1 - 1, mx1, Z1 + MOTOR["alto"]))
    g = g.union(tabs_a_caja([(122.4, Z_PISO, 125.4, Z1), (146.6, Z_PISO, 149.6, Z1)]))
    out.append(Pieza(g, "SOPORTE MOTOR", "xz", SOPORTE_Y, etiqueta="SM", tipo="chasis"))

    # torre del botón: 2 laterales + tapa con el agujero del pulsador
    lat = box(172, Z1, 188, H - T).union(box(175, Z_PISO, 185, Z1)).union(box(176, H - T, 184, H))
    for pos, n in ((-TORRE_Y[1], "TORRE IZQ"), (TORRE_Y[0], "TORRE DER")):
        out.append(Pieza(lat, n, "xz", pos, etiqueta="TB", tipo="torre"))
    tapa = redondear(box(CANAL_X[0] + 0.3, -CANAL_Y + 0.5, CANAL_X[1] - 0.3, CANAL_Y - 0.5), 2)
    tapa = tapa.difference(Point(*BOTON).buffer(6.25, 32))
    tapa = tapa.difference(tabs_a_caja([(176, TORRE_Y[0], 184, TORRE_Y[1]),
                                        (176, -TORRE_Y[1], 184, -TORRE_Y[0])]))
    out.append(Pieza(tapa, "TAPA TORRE", "xy", H - T, etiqueta="", tipo="torre"))
    out += ruedas_y_polea()
    return out


def llanta():
    p = Point(0, 0).buffer(R_RUEDA, 64)
    anillo = Point(0, 0).buffer(11.5, 64).difference(Point(0, 0).buffer(4.5, 48))
    rayos = unary_union([affinity.rotate(box(-1.6, 0, 1.6, 14), a * 72, origin=(0, 0))
                         for a in range(5)])
    return p.difference(anillo.difference(rayos)).difference(Point(0, 0).buffer(R_AJUSTE, 16))


def disco(r, agujero=R_AJUSTE):
    return Point(0, 0).buffer(r, 64).difference(Point(0, 0).buffer(agujero, 16))


def ruedas_y_polea():
    out = []
    for lado in (-1, 1):
        for x in (EJE_DEL, EJE_TRAS):
            y_ext = Y_RUEDA[1] if lado > 0 else -Y_RUEDA[1]
            capas = [("llanta", llanta(), [Point(0, 0).buffer(2.6, 16).exterior]),
                     ("disco", disco(R_CANAL), [Point(0, 0).buffer(11.8, 48)]),
                     ("interior", disco(R_RUEDA), [])]
            for i, (n, g, gr) in enumerate(capas):
                y0 = (Y_RUEDA[1] - (i + 1) * T) if lado > 0 else (-Y_RUEDA[1] + i * T)
                out.append(Pieza(g, f"RUEDA {n}", "xz", y0, gr, tipo="rueda",
                                 g3d=affinity.translate(g, x, Z_EJE),
                                 color="#cfd3d6" if n == "llanta" else None))
            for j in range(2):  # 2 arandelas entre larguero y rueda
                y0 = (Y_LARG[1] + j * T) if lado > 0 else (-Y_LARG[1] - (j + 1) * T)
                g = disco(4, R_EJE)
                out.append(Pieza(g, "ARANDELA", "xz", y0, tipo="arandela",
                                 g3d=affinity.translate(g, x, Z_EJE)))
    for i, r in enumerate((10.5, 9.0, 10.5)):
        g = disco(r)
        out.append(Pieza(g, "POLEA", "xz", POLEA_Y[0] + i * T, tipo="polea",
                         g3d=affinity.translate(g, EJE_TRAS, Z_EJE)))
    return out


# --- carrocería ---------------------------------------------------------------------
def altura_torre(modelo):
    """Altura de la tapa de la torre: 1,5 mm debajo de la carrocería en el canal del botón."""
    minimo = 999
    for k in range(N):
        if not toca(k, -CANAL_Y, CANAL_Y):
            continue
        p, _ = modelo.perfil(k)
        if p is None or p.is_empty:
            continue
        for i in range(18):
            x = CANAL_X[0] + i * (CANAL_X[1] - CANAL_X[0]) / 17
            corte = p.intersection(LineString([(x, 0), (x, 200)]))
            if not corte.is_empty:
                minimo = min(minimo, corte.bounds[3])
    return math.floor((minimo - 1.5) * 2) / 2


def carroceria(modelo):
    """Arma las capas de la carrocería y devuelve (piezas, pernos)."""
    piezas, agujeros = [], {}
    arcos = unary_union([Point(x, Z_EJE).buffer(R_ARCO, 64) for x in (EJE_DEL, EJE_TRAS)])
    canal = box(CANAL_X[0], -10, CANAL_X[1], 300)
    for k in range(N):
        p, grab = modelo.perfil(k)
        if p is None or p.is_empty:
            continue
        if con_cavidad(k):
            p = p.difference(cavidad())
        else:
            p = p.difference(arcos)
        if toca(k, -CANAL_Y, CANAL_Y):
            p = p.difference(canal)
        o = desde_afuera(k)
        for i, (x, z) in enumerate(modelo.pernos):
            c = Point(x, z).buffer(R_PERNO, 24)
            if o > 0 and k not in getattr(modelo, "sin_pernos", ()) and \
                    p.buffer(-0.05).contains(Point(x, z).buffer(R_PERNO + 1.3)):
                p = p.difference(c)
                agujeros.setdefault(i, []).append(k)
        grab = [g.intersection(p.buffer(-0.3)) for g in grab]
        grab = [g for g in grab if not g.is_empty]
        partes = sorted(poligonos(p), key=lambda q: q.bounds[0])
        for j, q in enumerate(partes):
            g = [e for e in grab if e.intersects(q)]
            n = f"{k + 1}" + ("abcd"[j] if len(partes) > 1 else "")
            tx = [t for t in (modelo.textos_capa(k) if hasattr(modelo, "textos_capa") else [])
                  if q.contains(Point(t[1], t[2]))]
            pz = Pieza(q, n, "xz", tramo(k)[0], g, tipo="carroceria",
                       espejo=k >= N / 2 and bool(g or tx),
                       etiqueta="" if (o == 0 or tx) else n, capa=k)
            pz.textos = tx
            piezas.append(pz)
    piezas += modelo.extras() if hasattr(modelo, "extras") else []
    # pernos: tramos seguidos de capas con agujero
    pernos = []
    for i, ks in agujeros.items():
        ks = sorted(ks)
        ini = ks[0]
        for a, b in zip(ks, ks[1:] + [None]):
            if b != a + 1:
                pernos.append(dict(x=modelo.pernos[i][0], z=modelo.pernos[i][1],
                                   desde=ini + 1, hasta=a + 1, largo=(a - ini + 1) * T))
                ini = b
    return piezas, pernos


def verificar(modelo, piezas):
    """Controles: la carrocería no toca las ruedas ni el chasis."""
    avisos = []
    ruedas = unary_union([Point(x, Z_EJE).buffer(R_CUBIERTA + 0.4, 48) for x in (EJE_DEL, EJE_TRAS)])
    for pz in piezas:
        if pz.tipo != "carroceria" or pz.plano != "xz" or pz.capa is None:
            continue
        k = pz.capa
        if toca(k, Y_RUEDA[0], Y_RUEDA[1]) or toca(k, -Y_RUEDA[1], -Y_RUEDA[0]):
            if pz.geom.intersection(ruedas).area > 0.5:
                avisos.append(f"capa {pz.nombre} toca una rueda")
        if con_cavidad(k) and pz.geom.intersection(cavidad()).area > 0.5:
            avisos.append(f"capa {pz.nombre} invade el chasis")
    return avisos


# --- acomodar piezas en hojas ---------------------------------------------------
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
MADERA, BORDE = "#e6c391", "#8a6239"
NUEVO, BORDE_NUEVO = "#ffc96b", "#b36b00"


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


NORMAL = {"xz": (0, 1, 0), "xy": (0, 0, 1), "yz": (1, 0, 0)}


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


# --- electrónica para los dibujos ---------------------------------------------------
def electronica(escena, H, que=("pilas", "motor", "goma", "bornes", "boton", "cables"),
                nuevo=(), d=(0, 0, 0)):
    Z1 = zp()
    if "pilas" in que:
        x0, y0, x1, y1 = PILAS
        escena.caja(x0, y0, Z1, x1, y1, Z1 + 15, "#2b2b2b", "#111", desplazar=d)
        for yy in (y0 + 3, (y0 + y1) / 2 + 1):
            escena.caja(x0 + 4, yy, Z1 + 15, x1 - 4, yy + 13, Z1 + 15.5, "#e9a23b", "#8a5a10",
                        desplazar=d)
    if "motor" in que:
        mx0, mx1 = MOTOR["x"]
        g = redondear(box(mx0, Z1, mx1, Z1 + 15), 3)
        escena.prisma(g, "xz", MOTOR["y"][0], MOTOR["y"][1] - MOTOR["y"][0], fill="#a7b0ba",
                      stroke="#4a525a", desplazar=d)
        eje = Point(136, Z1 + 7.5).buffer(1, 12)
        escena.prisma(eje, "xz", MOTOR["y"][1], 8, fill="#ddd", stroke="#555", desplazar=d)
    if "goma" in que:
        z = Z1 + 7.5
        pts = []
        for i in range(25):
            a = math.pi / 2 + i * math.pi / 24
            pts.append((136 + 1.2 * math.cos(a), 11.5, z + 1.2 * math.sin(a)))
        for i in range(25):
            a = -math.pi / 2 + i * math.pi / 24
            pts.append((EJE_TRAS + 9.2 * math.cos(a), 11.5, Z_EJE + 9.2 * math.sin(a)))
        pts.append(pts[0])
        escena.linea([(x + d[0], y + d[1], z_ + d[2]) for x, y, z_ in pts], "#e8590c", 2.2)
    if "bornes" in que:
        for x0, y0, x1, y1 in BORNES:
            escena.caja(x0, y0, Z1, x1, y1, Z1 + 8, "#f4f4f4", "#888", desplazar=d)
            escena.caja(x0 + 1, y0 + 1, Z1 + 8, x0 + 5, y1 - 1, Z1 + 9.5, "#f08c00", "#a35f00",
                        desplazar=d)
    if "boton" in que:
        escena.prisma(Point(*BOTON).buffer(6, 24), "xy", H - 20, 20, fill="#555", stroke="#222",
                      desplazar=d)
        escena.prisma(Point(*BOTON).buffer(5, 24), "xy", H, 7, fill="#e03131", stroke="#8a1c1c",
                      desplazar=d)
    if "cables" in que:
        z = Z1 + 0.8
        rojo, negro, azul = "#e03131", "#222", "#1c7ed6"
        cables = [
            ([(63, -12, z + 3), (55, -12, z + 4)], rojo),
            ([(64, 8, z + 3), (66, 16.5, z), (108, 16.5, z + 4)], negro),
            ([(180, -6, H - 20), (176, -15.5, z), (60, -15.5, z), (55, -12, z + 4)], azul),
            ([(180, -4, H - 20), (176, -17.5, z), (64, -17.5, z), (64, 10, z), (55, 10, z + 4)], azul),
            ([(130, -20, z + 7), (124, -19, z), (64, -19, z), (64, 12, z), (55, 12, z + 4)], negro),
            ([(130, 4, z + 10), (124, 6, z), (124, 14.5, z), (108, 15.5, z + 4)], rojo),
        ]
        for pts, col in cables:
            escena.linea([(x + d[0], y + d[1], zz + d[2]) for x, y, zz in pts], col, 1.8)


def eje(escena, x, d=(0, 0, 0), fill=MADERA):
    g = Point(x, Z_EJE).buffer(1.5, 12)
    largo = 2 * Y_RUEDA[1] + 2
    escena.prisma(g, "xz", -largo / 2, largo, fill=fill, desplazar=d)


def cubiertas(escena, d=(0, 0, 0), ejes=(EJE_DEL, EJE_TRAS)):
    for x in ejes:
        for lado in (-1, 1):
            y0 = (Y_RUEDA[1] - 2 * T) if lado > 0 else (-Y_RUEDA[1] + T)
            g = Point(x, Z_EJE).buffer(R_CUBIERTA, 48).difference(Point(x, Z_EJE).buffer(R_CANAL, 48))
            escena.prisma(g, "xz", y0 - 0.2, T + 0.4, fill="#222", stroke="#000", desplazar=d)
