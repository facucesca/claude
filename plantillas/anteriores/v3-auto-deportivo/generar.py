"""Auto deportivo en capas (v3), estilo superauto en cuña, escala 1:24.

La carrocería son capas de 3 mm con el perfil del auto, apiladas a lo ancho.
Cada capa tiene una forma un poco distinta (guardabarros, cabina, tomas de aire),
así el auto queda en 3D. Adentro hay huecos para pilas, motor, goma y botón.

Uso:  pip install shapely ezdxf
      python3 generar.py          (material de 3 mm)
      python3 generar.py 2.8      (si el material mide otra cosa)

Salida: hoja-1.svg/.dxf, hoja-2.svg/.dxf ... (para el láser), vista-3d.png
y vista-lateral.svg (para mirar). ROJO = cortar, AZUL = grabar, GRIS = notas.
"""
import math
import sys

from shapely import affinity
from shapely.geometry import LineString, MultiPolygon, Point, Polygon, box
from shapely.ops import unary_union

T = float(sys.argv[1]) if len(sys.argv) > 1 else 3.0
ANCHO = 84.0                       # ancho total del auto (1:24 de ~2 m)
N = round(ANCHO / T)               # cantidad de capas
MEDIO = 27.0                       # |y| donde empieza la zona de guardabarros
HOJA = (600, 400)

EJE_DEL, EJE_TRAS, Z_EJE = 46.0, 156.0, 16.0
R_ARCO = 17.8                      # hueco del guardabarros
R_EJE, R_AJUSTE, R_PERNO = 1.75, 1.4, 1.6
SEP_TAPA = 26.0                    # altura donde se separa la tapa (techo + motor)
TAPA_X = (64.0, 176.0)
MEDIO_CAPAS = round(MEDIO / T)     # capas de cabina a cada lado del centro


# --- curvas -----------------------------------------------------------------
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


COLA = [(200, 36), (200.4, 30), (199.5, 18), (197.5, 9), (193, 5)]
NARIZ = [(10, 5), (4, 6.6), (1, 9.2), (0, 13)]


def silueta(techo):
    pts = suave(techo) + suave(COLA)[1:] + suave(NARIZ)[:-1]
    return Polygon(pts).buffer(0)


# línea de techo de la cabina (capas del centro) y de los guardabarros (capas de afuera)
CABINA = silueta([(0, 13), (10, 20.5), (30, 28), (46, 31.5), (63, 34.5), (78, 40),
                  (93, 45.3), (104, 47), (117, 46.4), (140, 41.6), (165, 37.6),
                  (186, 35.6), (196, 36.6), (200, 36)])
CUERPO = silueta([(0, 13), (8, 21), (24, 30.8), (46, 37.4), (63, 35.2), (82, 33.8),
                  (104, 34), (128, 36), (150, 39.8), (163, 40.2), (181, 38.4),
                  (196, 37.3), (200, 36)])


def arriba(p, z):
    return p.intersection(box(-10, z, 250, 100))


def abajo(p, z):
    return p.intersection(box(-10, -10, 250, z))


# --- capas --------------------------------------------------------------------
def tramo(k):
    """Rango en y (mm) que ocupa la capa k; y=0 es el centro del auto."""
    return (-ANCHO / 2 + k * T, -ANCHO / 2 + (k + 1) * T)


def toca(k, y0, y1):
    a, b = tramo(k)
    return a < y1 - 1e-6 and b > y0 + 1e-6


def de_afuera(k):
    a, b = tramo(k)
    return min(abs(a), abs(b)) >= MEDIO - 1e-6


def orden_desde_afuera(k):
    return min(k, N - 1 - k)


HUECOS = [  # (forma, datos, y0, y1)
    ("caja", (66, 10, 126.4, SEP_TAPA + 0.01), -27, 18),      # pilas 2xAA + bornes
    ("caja", (126, 10, 146.4, SEP_TAPA + 0.01), -23.5, 1.5),  # motor 130
    ("caja", (136, 10, 156, SEP_TAPA + 0.01), 1.5, 15),       # goma
    ("circulo", (EJE_TRAS, Z_EJE, 12.5), 1.5, 15),         # polea
    ("caja", (146, 22, 177, SEP_TAPA + 0.01), -6, 0),      # cables al botón (bajo la tapa)
    ("caja", (176, 12, 193.5, SEP_TAPA + 0.01), -9, 9),    # cuerpo del botón
    ("caja", (176, 25, 188.5, 60), -6, 6),                 # agujero del botón
]


def hueco(forma, d):
    return box(*d) if forma == "caja" else Point(d[0], d[1]).buffer(d[2], 48)


def capa(k):
    """Devuelve (perfil completo de la capa k, grabados)."""
    o = orden_desde_afuera(k)
    grabados = []
    if de_afuera(k):
        p = CUERPO.buffer(-1.0, 32) if o == 0 else CUERPO
        for x in (EJE_DEL, EJE_TRAS):
            p = p.difference(Point(x, Z_EJE).buffer(R_ARCO, 64))
        if o <= 1:  # toma de aire lateral
            p = p.difference(Polygon([(102, 11), (132, 11), (135.5, 28), (121, 29)]))
        if 1 <= o <= 4:  # ranura de faro
            p = p.difference(box(-1, 16.5, 13, 19.5))
        if o == 0:  # líneas de la puerta
            grabados.append(LineString([(63.5, 31.5), (66, 9), (99, 9)]))
    else:
        orden_c = o - sum(1 for j in range(N) if de_afuera(j) and j < N / 2)
        if orden_c in (0, 1):  # bordes redondeados de la cabina
            p = CABINA.buffer(-2.5 if orden_c == 0 else -1.2, 32).union(abajo(CABINA, 28))
        else:
            p = CABINA
        if orden_c == 0:  # ventanilla grabada (relleno = vidrio oscuro)
            v = arriba(p, 34.8).intersection(box(64, 0, 150, 100)).buffer(-1.6, 16)
            if not v.is_empty:
                grabados.append(v)
        for x in (EJE_DEL, EJE_TRAS):
            p = p.difference(Point(x, Z_EJE).buffer(R_EJE, 24))
        for forma, d, y0, y1 in HUECOS:
            if toca(k, y0, y1):
                p = p.difference(hueco(forma, d))
        if k % 2 == 0 and not toca(k, -9, 9):  # aletas del difusor y la trompa
            p = p.difference(box(186, 4, 201, 10)).difference(box(-1, 4, 9, 8.5))
    if 1 <= o <= 6:
        p = p.difference(box(193, 27.5, 201, 30))  # ranura de luz trasera
    # pernos de alineación
    pernos = [(20, 11)] if o > 0 else []  # no atraviesan el costado de afuera
    if o > 0 and not toca(k, -27, 18):
        pernos.append((88, 20))
    if o > 0 and not toca(k, -9, 9):
        pernos.append((186, 24))
    for x, z in pernos:
        p = p.difference(Point(x, z).buffer(R_PERNO, 24))
    return p, grabados


def separar_tapa(k, p):
    """Las capas del centro se cortan en dos: base y tapa (se levanta)."""
    if de_afuera(k):
        return p, None
    zona = box(TAPA_X[0], SEP_TAPA, TAPA_X[1], 100)
    tapa = p.intersection(zona)
    cabina_afuera = k in (N // 2 - MEDIO_CAPAS, N - 1 - (N // 2 - MEDIO_CAPAS))
    for x, z in [] if cabina_afuera else [(100, 38), (150, 33)]:
        tapa = tapa.difference(Point(x, z).buffer(R_PERNO, 24))
    return p.difference(zona), tapa


def partes(g):
    if g is None or g.is_empty:
        return []
    if isinstance(g, Polygon):
        return [g]
    return [q for q in getattr(g, "geoms", []) if isinstance(q, Polygon) and q.area > 4]


# --- ruedas -------------------------------------------------------------------
R_RUEDA, R_CANAL = 15.5, 13.0


def llanta():
    p = Point(0, 0).buffer(R_RUEDA, 64)
    anillo = Point(0, 0).buffer(11.5, 64).difference(Point(0, 0).buffer(4.5, 48))
    rayos = unary_union([affinity.rotate(box(-1.6, 0, 1.6, 14), a * 72, origin=(0, 0))
                         for a in range(5)])
    p = p.difference(anillo.difference(rayos))
    return p.difference(Point(0, 0).buffer(R_AJUSTE, 16))


def disco(r):
    return Point(0, 0).buffer(r, 64).difference(Point(0, 0).buffer(R_AJUSTE, 16))


def arandela():
    return Point(0, 0).buffer(4, 32).difference(Point(0, 0).buffer(R_EJE, 16))


# --- piezas -------------------------------------------------------------------
def piezas():
    """Lista de piezas: dict(geom, grabados, nombre, espejo)."""
    out = []
    for k in range(N):
        p, grab = capa(k)
        base, tapa = separar_tapa(k, p)
        derecha = k >= N / 2  # las de la derecha con grabado se cortan en espejo
        nb = partes(base)
        for i, q in enumerate(nb):
            nombre = f"{k+1}" + ("abc"[i] if len(nb) > 1 else "")
            g = grab if i == 0 and not tapa else []
            out.append(dict(geom=q, grab=g, nombre=nombre, espejo=derecha and bool(g), capa=k,
                            tipo="base"))
        for q in partes(tapa):
            out.append(dict(geom=q, grab=grab, nombre=f"T{k+1}", espejo=derecha and bool(grab),
                            capa=k, tipo="tapa"))
    for i in range(4):
        out.append(dict(geom=llanta(), grab=[Point(0, 0).buffer(2.6, 16).exterior],
                        nombre="", espejo=False, tipo="rueda"))
        out.append(dict(geom=disco(R_CANAL), grab=[Point(0, 0).buffer(11.8, 48)], nombre="",
                        espejo=False, tipo="rueda"))
        out.append(dict(geom=disco(R_RUEDA), grab=[], nombre="", espejo=False, tipo="rueda"))
        out.append(dict(geom=arandela(), grab=[], nombre="", espejo=False, tipo="arandela"))
    for r in (10.5, 9.0, 10.5):
        out.append(dict(geom=disco(r), grab=[], nombre="", espejo=False, tipo="polea"))
    return out


# --- acomodar en hojas --------------------------------------------------------
def acomodar(lista, margen=6, sep=3):
    hojas, hoja, x, y, alto_fila = [], [], margen, margen, 0
    for pz in sorted(lista, key=lambda d: -(d["geom"].bounds[3] - d["geom"].bounds[1])):
        g, grab = pz["geom"], pz["grab"]
        if pz["espejo"]:
            g = affinity.scale(g, -1, 1, origin=(100, 0))
            grab = [affinity.scale(e, -1, 1, origin=(100, 0)) for e in grab]
        x0, y0, x1, y1 = g.bounds
        w, h = x1 - x0, y1 - y0
        if x + w > HOJA[0] - margen:
            x, y, alto_fila = margen, y + alto_fila + sep, 0
        if y + h > HOJA[1] - margen:
            hojas.append(hoja)
            hoja, x, y, alto_fila = [], margen, margen, 0
        # en la hoja el eje y va hacia abajo: damos vuelta z
        tr = lambda gg, dx=x - x0, dy=y + y1: affinity.translate(
            affinity.scale(gg, 1, -1, origin=(0, 0)), dx, dy)
        hoja.append(dict(pz, geom=tr(g), grab=[tr(e) for e in grab]))
        x += w + sep
        alto_fila = max(alto_fila, h)
    if hoja:
        hojas.append(hoja)
    return hojas



def anillos(g):
    if isinstance(g, Polygon):
        return [list(g.exterior.coords)] + [list(i.coords) for i in g.interiors]
    if isinstance(g, MultiPolygon):
        return [r for q in g.geoms for r in anillos(q)]
    if isinstance(g, LineString):
        return [list(g.coords)]
    if hasattr(g, "coords"):
        return [list(g.coords)]
    return []


def d_de(ring, cerrar=True):
    s = "M" + " L".join(f"{a:.2f},{b:.2f}" for a, b in ring)
    return s + (" Z" if cerrar else "")


def guardar_hoja(n, hoja):
    import ezdxf
    svg = [f'<svg xmlns="http://www.w3.org/2000/svg" width="{HOJA[0]}mm" height="{HOJA[1]}mm" '
           f'viewBox="0 0 {HOJA[0]} {HOJA[1]}">',
           f'<rect width="{HOJA[0]}" height="{HOJA[1]}" fill="#fff"/>',
           f'<rect x="0.5" y="0.5" width="{HOJA[0]-1}" height="{HOJA[1]-1}" fill="none" '
           'stroke="#999" stroke-width="0.3" stroke-dasharray="3 2"/>']
    corte, grab, rel, notas = [], [], [], []
    doc = ezdxf.new()
    for nombre, color in (("CORTAR", 1), ("GRABAR", 5), ("GRABAR_RELLENO", 5)):
        doc.layers.add(nombre, color=color)
    msp = doc.modelspace()
    for pz in hoja:
        for r in anillos(pz["geom"]):
            corte.append(f'<path d="{d_de(r)}"/>')
            msp.add_lwpolyline([(a, HOJA[1] - b) for a, b in r], close=True,
                               dxfattribs={"layer": "CORTAR"})
        for e in pz["grab"]:
            relleno = isinstance(e, Polygon) and e.area > 30
            for r in anillos(e):
                cerr = isinstance(e, Polygon)
                (rel if relleno else grab).append(f'<path d="{d_de(r, cerr)}"/>')
                msp.add_lwpolyline([(a, HOJA[1] - b) for a, b in r], close=cerr,
                                   dxfattribs={"layer": "GRABAR_RELLENO" if relleno else "GRABAR"})
        if pz["nombre"]:
            c = pz["geom"].representative_point() if pz["tipo"] == "tapa" else None
            x0, y0, x1, y1 = pz["geom"].bounds
            if c is None:  # número en el piso de la capa (queda escondido al pegar)
                c = Point((x0 + x1) / 2 - 15 if not pz["espejo"] else (x0 + x1) / 2 + 15, y1 - 3)
                if not pz["geom"].buffer(-0.5).contains(Point(c.x + 3, c.y - 1)):
                    c = pz["geom"].representative_point()
            if orden_desde_afuera(pz["capa"]) > 0:
                grab.append(f'<text x="{c.x:.1f}" y="{c.y:.1f}" font-size="3.2" fill="#0000ff" '
                            f'stroke="none" font-family="Arial">{pz["nombre"]}</text>')
                msp.add_text(pz["nombre"], height=2.6, dxfattribs={"layer": "GRABAR"}
                             ).set_placement((c.x, HOJA[1] - c.y))
            notas.append(f'<text x="{x0:.1f}" y="{y0 - 0.6:.1f}" font-size="2.6">'
                         f'{pz["nombre"]}{" (espejo)" if pz["espejo"] else ""}</text>')
    svg.append('<g id="CORTAR" fill="none" stroke="#ff0000" stroke-width="0.1">')
    svg += corte
    svg.append('</g><g id="GRABAR_RELLENO" fill="#0000ff" fill-opacity="0.35" stroke="#0000ff" '
               'stroke-width="0.1">')
    svg += rel
    svg.append('</g><g id="GRABAR" fill="none" stroke="#0000ff" stroke-width="0.25">')
    svg += grab
    svg.append('</g><g id="NOTAS_no_grabar" fill="#888" font-family="Arial">')
    svg += notas
    svg.append(f'<text x="8" y="{HOJA[1]-4}" font-size="4">Hoja {n} - ROJO=cortar  '
               f'AZUL=grabar (relleno = grabado lleno)  GRIS=notas, no grabar - material {T:g} mm'
               '</text></g></svg>')
    open(f"hoja-{n}.svg", "w").write("\n".join(svg))
    doc.saveas(f"hoja-{n}.dxf")


# --- vistas para mirar --------------------------------------------------------
def vista_3d():
    """Dibujo en perspectiva caballera: capa por capa, de atrás para adelante."""
    E, DX, DZ = 3.6, -0.42, 0.30           # escala px/mm y desplazamiento por mm de ancho
    W, H = 1000, 520
    ox, oz = 150, 450
    svg = [f'<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" '
           f'viewBox="0 0 {W} {H}">', f'<rect width="{W}" height="{H}" fill="#f6f1ea"/>',
           f'<ellipse cx="{ox+E*100+E*42*DX}" cy="{oz+6}" rx="{E*118}" ry="22" fill="#000" '
           'opacity="0.12"/>']

    def pts(ring, y):
        prof = (y + ANCHO / 2)
        return " ".join(f"{ox + E * (a + prof * DX):.1f},{oz - E * (b + prof * DZ):.1f}"
                        for a, b in ring)

    def dib(g, y, fill, stroke="#7a5530", sw=0.7, op=1):
        for q in partes(g) if not isinstance(g, Polygon) else [g]:
            d = "M" + pts(q.exterior.coords, y) + " Z"
            for i in q.interiors:
                d += " M" + pts(i.coords, y) + " Z"
            svg.append(f'<path d="{d}" fill="{fill}" fill-rule="evenodd" stroke="{stroke}" '
                       f'stroke-width="{sw}" opacity="{op}"/>')

    madera = ["#e6c391", "#dfba86"]
    for k in range(N - 1, -1, -1):
        y = tramo(k)[1]
        p, grab = capa(k)
        dib(p, y, madera[k % 2])
        for e in grab:
            if isinstance(e, Polygon):
                dib(e, y, "#3c4650", "#2a3138", 0.6, 0.92)
            else:
                d = "M" + pts(e.coords, y)
                svg.append(f'<path d="{d}" fill="none" stroke="#9c7243" stroke-width="1"/>')
        o = orden_desde_afuera(k)
        if o in (1, 2, 3):  # ruedas
            for x in (EJE_DEL, EJE_TRAS):
                cub = Point(x, Z_EJE).buffer(R_RUEDA + 0.6, 64)
                if o == 2:
                    dib(cub, y, "#1f1f1f", "#000", 0.6)
                    dib(Point(x, Z_EJE).buffer(R_CANAL, 64), y, "#2b2b2b", "#000", 0.4)
                else:
                    g = affinity.translate(llanta() if (o == 1) else disco(R_RUEDA), x, Z_EJE)
                    dib(Point(x, Z_EJE).buffer(R_RUEDA + 0.6, 64), y, "#1f1f1f", "#000", 0.6)
                    dib(g, y, "#cfd3d6" if o == 1 else "#2b2b2b", "#555", 0.6)
    svg.append(f'<text x="30" y="40" font-family="Arial" font-size="22" font-weight="bold" '
               'fill="#3b2a1a">Auto deportivo en capas (v3)</text>')
    svg.append(f'<text x="30" y="66" font-family="Arial" font-size="15" fill="#6b5640">'
               f'Escala 1:24 - 20 cm de largo, 8,4 cm de ancho, 4,7 cm de alto - '
               f'{N} capas de {T:g} mm</text>')
    svg.append("</svg>")
    open("vista-3d.svg", "w").write("\n".join(svg))


def vista_lateral():
    E = 4
    W, H = 920, 260
    svg = [f'<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}">',
           f'<rect width="{W}" height="{H}" fill="#fff"/>']
    ox, oz = 50, 230
    f = lambda ring: " ".join(f"{ox+E*a:.1f},{oz-E*b:.1f}" for a, b in ring)
    for g, col in ((CABINA, "#e6c391"), (capa(0)[0], "#d9b07a")):
        for q in partes(g) if not isinstance(g, Polygon) else [g]:
            d = "M" + f(q.exterior.coords) + " Z" + "".join(" M" + f(i.coords) + " Z"
                                                           for i in q.interiors)
            svg.append(f'<path d="{d}" fill="{col}" fill-rule="evenodd" stroke="#7a5530"/>')
    for forma, d, *_ in HUECOS:
        q = hueco(forma, d).intersection(CABINA)
        for r in partes(q) if not isinstance(q, Polygon) else [q]:
            svg.append(f'<path d="M{f(r.exterior.coords)} Z" fill="none" stroke="#c0392b" '
                       'stroke-dasharray="4 3"/>')
    for x in (EJE_DEL, EJE_TRAS):
        svg.append(f'<circle cx="{ox+E*x}" cy="{oz-E*Z_EJE}" r="{E*(R_RUEDA+0.6)}" fill="#222" '
                   'opacity="0.85"/>')
    svg.append(f'<line x1="{ox+E*TAPA_X[0]}" y1="{oz-E*SEP_TAPA}" x2="{ox+E*TAPA_X[1]}" '
               f'y2="{oz-E*SEP_TAPA}" stroke="#2b6cb0" stroke-width="2" stroke-dasharray="6 4"/>')
    svg.append('<text x="20" y="24" font-family="Arial" font-size="15" fill="#333">Corte lateral: '
               'rojo = huecos internos (pilas, motor, goma, polea, botón). Azul = donde se separa la tapa.'
               '</text></svg>')
    open("vista-lateral.svg", "w").write("\n".join(svg))


if __name__ == "__main__":
    lista = piezas()
    hojas = acomodar(lista)
    for i, h in enumerate(hojas, 1):
        guardar_hoja(i, h)
    vista_3d()
    vista_lateral()
    print(f"{N} capas, {len(lista)} piezas, {len(hojas)} hojas de {HOJA[0]}x{HOJA[1]} mm")
