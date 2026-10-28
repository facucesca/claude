"""Base común de la línea "para chicos": autos que se arman SIN COLA, todo a presión.

Todos los modelos (camioneta, jeep, colectivo) comparten:
- 2 costados con la silueta + piezas que los unen con pestañas y ranuras;
- el piso, el piso de la caja (pilas, bornes y botón), los 2 soportes del motor;
- las ruedas (3 discos + o-ring), la polea, los ejes y la electrónica.
Cada modelo cambia la silueta y las piezas de arriba (capó, techo, paredes).

Coordenadas (mm): x a lo largo (0 = trompa, 200 = cola), y a lo ancho (0 = centro),
z hacia arriba (0 = suelo).
"""
import glob
import math
import os
import shutil
import subprocess
import sys
import zipfile

from shapely import affinity
from shapely.geometry import LineString, Point, Polygon, box
from shapely.ops import unary_union

AQUI = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, AQUI)
import kit  # noqa: E402  (motor de dibujo: hojas de corte, vistas 3D)

T = 3.0       # espesor de la placa
AJ = 0.1      # cuánto más angostas que el espesor se cortan las ranuras


def configurar(argv):
    """Lee [espesor] [ajuste] de la línea de comandos."""
    global T, AJ
    if len(argv) > 1:
        T = float(argv[1])
    if len(argv) > 2:
        AJ = float(argv[2])
    kit.configurar(T)


kit.configurar(T)
CHROME = (shutil.which("chromium") or shutil.which("google-chrome")
          or next(iter(sorted(glob.glob("/opt/pw-browsers/chromium-*/chrome-linux*/chrome"))), "chromium"))

# --- medidas comunes (mm) -------------------------------------------------------------
YI = 29.0                         # mitad del ancho interior (entre costados)
EJES = (42.0, 152.0)
ZE = 18.5                         # altura de los ejes
R_RUEDA, R_CANAL, R_CUB = 18.0, 15.5, 18.5
Z_PISO = 8.0                      # piso: z 8 a 11
Z_CAJA = 28.0                     # piso de la caja: z 28 a 31
X_FRENTE, X_CABINA, X_PORTON = 4.0, 100.0, 193.0
MOTOR_X = (116.0, 136.4)          # cuna del motor (el motor apoya en z 13)
MOTOR_Y = (-6.0, 19.0)
SOPORTES_Y = (-2.0, 12.0)
POLEA_Y = (-17.0, -8.0)
PILAS = (107.0, -3.0, 165.0, 29.0)
BORNES = [(166, -27, 179, -9), (166, -8, 179, 10), (166, 11, 179, 29)]
BOTON = (185.5, 0.0)
VENTANA = (120.0, -24.0, 166.0, -6.0)

TABS_PISO = [(20, 34), (60, 90), (118, 133), (168, 184)]
TABS_CAJA = [(112, 126), (168, 182)]
TABS_ABAJO_Y = [(-20, -8), (8, 20)]


def ranura(x0, z0, x1, z1):
    """Ranura un poco más angosta que el espesor, para que encastre firme."""
    if abs((x1 - x0) - T) < 1e-6:
        c = (x0 + x1) / 2
        x0, x1 = c - (T - AJ) / 2, c + (T - AJ) / 2
    if abs((z1 - z0) - T) < 1e-6:
        c = (z0 + z1) / 2
        z0, z1 = c - (T - AJ) / 2, c + (T - AJ) / 2
    return box(x0, z0, x1, z1)


def unir(*gs):
    return unary_union(list(gs))


def redondo(p, r):
    return p.buffer(-r, 12).buffer(r, 12)


def suavizar(p, r=1.2):
    """Redondea también las esquinas hacia adentro."""
    return p.buffer(r, 8).buffer(-r, 8)


# --- piezas comunes -------------------------------------------------------------------
def costado(silueta, placas, paredes, ventanas=(), grab=()):
    """Costado: silueta con las ranuras de las piezas que lo unen al otro costado.
    placas  = [(z, tabs_x)]  piezas acostadas (piso, caja, capó...)
    paredes = [(x, tabs_z)]  piezas paradas (frente, cabina, portón...)"""
    p = silueta
    for v in ventanas:
        p = p.difference(v)
    hue = []
    for z, tabs in placas:
        hue += [ranura(a, z, b, z + T) for a, b in tabs]
    for x, tabs in paredes:
        hue += [ranura(x, a, x + T, b) for a, b in tabs]
    hue += [Point(x, ZE).buffer(kit.R_EJE, 24) for x in EJES]
    p = p.difference(unary_union(hue))
    grab = list(grab)
    for x in EJES:                                                                # guardabarros
        arco = [(x + 22 * math.cos(math.radians(a)), ZE + 22 * math.sin(math.radians(a)))
                for a in range(10, 171, 4)]
        grab.append(LineString(arco))
    return p, grab


def con_pestanas_y(base, tabs_z):
    """Pieza en el plano yz: pestañas a los costados (en z) y abajo (en y)."""
    g = base
    for a, b in tabs_z:
        g = unir(g, box(-YI - T, a, -YI, b), box(YI, a, YI + T, b))
    for a, b in TABS_ABAJO_Y:
        g = unir(g, box(a, Z_PISO, b, Z_PISO + T))
    return g


def con_pestanas_x(base, tabs_x):
    """Pieza en el plano xy: pestañas hacia los dos costados."""
    g = base
    for a, b in tabs_x:
        g = unir(g, box(a, -YI - T, b, -YI), box(a, YI, b, YI + T))
    return g


def pared(z_arriba, tabs_z, forma=None):
    """Pieza parada entre los costados, desde el piso hasta z_arriba."""
    return con_pestanas_y(forma if forma is not None else box(-YI, Z_PISO + T, YI, z_arriba), tabs_z)


def costados(c, grab):
    P = kit.Pieza
    return [P(c, "COSTADO IZQ", "xz", -YI - T, grab, etiqueta="", tipo="carroceria"),
            P(c, "COSTADO DER", "xz", YI, grab, etiqueta="", tipo="carroceria", espejo=True)]


def piso(x_paredes):
    piso = con_pestanas_x(box(1, -YI, 199, YI), TABS_PISO)
    hue = []
    for x in x_paredes:
        hue += [ranura(x, a, x + T, b) for a, b in TABS_ABAJO_Y]
    for y in SOPORTES_Y:
        hue += [ranura(112.5, y, 115.5, y + T), ranura(136.9, y, 139.9, y + T)]
    hue.append(box(140, POLEA_Y[0] - 1.5, 164, POLEA_Y[1] + 1.5))
    piso = piso.difference(unary_union(hue))
    pz = kit.Pieza(piso, "PISO", "xy", Z_PISO, [box(MOTOR_X[0], MOTOR_Y[0], MOTOR_X[1], MOTOR_Y[1]).exterior],
                   etiqueta="", tipo="chasis")
    pz.textos = [("PISO", 60, 0, 5), ("FRENTE", 20, 0, 4), ("MOTOR", 126, 6, 3.5)]
    return pz


def caja(boton=True):
    """Piso de la caja: las pilas, los bornes y (si va acá) el botón, arriba y a la vista."""
    c = con_pestanas_x(box(X_CABINA + T, -YI, X_PORTON, YI), TABS_CAJA)
    c = c.difference(redondo(box(*VENTANA), 2))
    if boton:
        c = c.difference(Point(*BOTON).buffer(6.25, 32)).difference(Point(185.5, -14).buffer(2.5, 16))
    grab = [box(*PILAS).exterior] + [box(*b).exterior for b in BORNES]
    pz = kit.Pieza(c, "CAJA", "xy", Z_CAJA, grab, etiqueta="", tipo="chasis")
    pz.textos = [("PILAS 2xAA", 136, 10, 5), ("+", 111, 22, 5), ("-", 111, 1, 5),
                 ("B1", 172.5, -19, 4), ("B2", 172.5, 0, 4), ("B3", 172.5, 19, 4),
                 ("POLEA", 143, -16.5, 3.5)]
    return pz


def soportes():
    """2 soportes del motor (cuna: el motor se apoya y la caja lo aprieta desde arriba)."""
    so = box(112, Z_PISO + T, 140, 24).difference(box(MOTOR_X[0], 13, MOTOR_X[1], 40))
    so = unir(so, box(112.5, Z_PISO, 115.5, Z_PISO + T), box(136.9, Z_PISO, 139.9, Z_PISO + T))
    return [kit.Pieza(so, "SOPORTE MOTOR", "xz", y, etiqueta="M", tipo="chasis") for y in SOPORTES_Y]


def llanta():
    p = Point(0, 0).buffer(R_RUEDA, 64)
    anillo = Point(0, 0).buffer(13.5, 64).difference(Point(0, 0).buffer(5, 48))
    rayos = unary_union([affinity.rotate(box(-1.8, 0, 1.8, 16), a * 72, origin=(0, 0))
                         for a in range(5)])
    return p.difference(anillo.difference(rayos)).difference(Point(0, 0).buffer(kit.R_AJUSTE, 16))


def disco(r, agujero=None):
    agujero = kit.R_AJUSTE if agujero is None else agujero
    return Point(0, 0).buffer(r, 64).difference(Point(0, 0).buffer(agujero, 16))


def ruedas():
    P = kit.Pieza
    out = []
    y_lar = YI + T                     # cara de afuera del costado
    for lado in (-1, 1):
        for x in EJES:
            capas = [("RUEDA llanta", llanta(), "#cfd3d6"), ("RUEDA medio", disco(R_CANAL), None),
                     ("RUEDA interior", disco(R_RUEDA), None)]
            for i, (n, g, col) in enumerate(capas):
                d = y_lar + T + (2 - i) * T          # arandela (3) + interior + medio + llanta
                y0 = d if lado > 0 else -d - T
                out.append(P(g, n, "xz", y0, tipo="rueda", g3d=affinity.translate(g, x, ZE), color=col))
            g = disco(4.5, kit.R_EJE)
            y0 = y_lar if lado > 0 else -y_lar - T
            out.append(P(g, "ARANDELA", "xz", y0, tipo="arandela", g3d=affinity.translate(g, x, ZE)))
    for i, r in enumerate((10.5, 9.0, 10.5)):
        g = disco(r)
        out.append(P(g, "POLEA", "xz", POLEA_Y[0] + i * T, tipo="polea",
                     g3d=affinity.translate(g, EJES[1], ZE)))
    return out


# --- electrónica y extras para los dibujos ----------------------------------------
CABLES_CAJA = [   # botón en la caja (camioneta, jeep)
    ([(108, 22, 6), (112, 26, 0), (160, 27, 0), (168, 21, 5)], "rojo"),
    ([(108, 2, 6), (104, 2, 0), (104, -26, 0), (168, -21, 5)], "negro"),
    ([(185.5, -6, 0), (180, -15, 2), (175, -18, 5)], "azul"),
    ([(185.5, 6, 0), (180, 3, 2), (175, 1, 5)], "azul"),
    ([(126, -6, -6), (126, -10, 2), (160, -5, 4), (175, -1, 5)], "rojo"),
    ([(130, 19, -6), (126, -18, 1), (162, -26, 4), (172, 20, 5)], "negro"),
]
COLORES = {"rojo": "#e03131", "negro": "#222", "azul": "#1c7ed6"}


def electronica(e, que=("motor", "goma", "pilas", "bornes", "boton", "cables"), d=(0, 0, 0),
                boton=None, cables=None):
    """boton = (x, y, z de la cara de arriba de la placa donde va); cables = [(puntos, color)]
    con z medida desde la cara de arriba de la caja + 1."""
    zc = Z_CAJA + T
    boton = boton or (BOTON[0], BOTON[1], zc)
    if "motor" in que:
        g = kit.redondear(box(MOTOR_X[0] + 0.2, 13, MOTOR_X[1] - 0.2, 28), 3)
        e.prisma(g, "xz", MOTOR_Y[0], MOTOR_Y[1] - MOTOR_Y[0], fill="#a7b0ba", stroke="#4a525a",
                 desplazar=d)
        e.prisma(Point(126.2, 20.5).buffer(1, 12), "xz", MOTOR_Y[0] - 8, 8, fill="#ddd",
                 stroke="#555", desplazar=d)
    if "goma" in que:
        pts = []
        for i in range(25):
            a = math.pi / 2 + i * math.pi / 24
            pts.append((126.2 + 1.2 * math.cos(a), -12.5, 20.5 + 1.2 * math.sin(a)))
        for i in range(25):
            a = -math.pi / 2 + i * math.pi / 24
            pts.append((EJES[1] + 9.2 * math.cos(a), -12.5, ZE + 9.2 * math.sin(a)))
        pts.append(pts[0])
        e.linea([(x + d[0], y + d[1], z + d[2]) for x, y, z in pts], "#e8590c", 2.4)
    if "pilas" in que:
        x0, y0, x1, y1 = PILAS
        e.caja(x0, y0, zc, x1, y1, zc + 15, "#2b2b2b", "#111", desplazar=d)
        for yy in (y0 + 2.5, (y0 + y1) / 2 + 0.5):
            e.caja(x0 + 4, yy, zc + 15, x1 - 4, yy + 13, zc + 15.5, "#e9a23b", "#8a5a10", desplazar=d)
    if "bornes" in que:
        for x0, y0, x1, y1 in BORNES:
            e.caja(x0, y0, zc, x1, y1, zc + 8, "#f4f4f4", "#888", desplazar=d)
            e.caja(x0 + 1, y0 + 1, zc + 8, x0 + 5, y1 - 1, zc + 9.5, "#f08c00", "#a35f00", desplazar=d)
    if "boton" in que:
        bx, by, bz = boton
        pri = 1 if bz > zc else 0          # en el techo: el capuchón se dibuja encima
        e.prisma(Point(bx, by).buffer(6, 24), "xy", bz - 18, 18, fill="#555", stroke="#222", desplazar=d)
        e.prisma(Point(bx, by).buffer(5, 24), "xy", bz, 7, fill="#e03131", stroke="#8a1c1c", desplazar=d,
                 prioridad=pri)
    if "cables" in que:
        z = zc + 1
        for pts, col in (cables or CABLES_CAJA):
            e.linea([(x + d[0], y + d[1], zz + z + d[2]) for x, y, zz in pts], COLORES[col], 1.8)


def ejes(e, que=EJES, d=(0, 0, 0)):
    largo = 2 * (YI + 5 * T) + 2
    for x in que:
        e.prisma(Point(x, ZE).buffer(1.5, 12), "xz", -largo / 2, largo, desplazar=d)


def cubiertas(e, que=EJES, d=(0, 0, 0)):
    for x in que:
        for lado in (-1, 1):
            dd = YI + 3 * T
            y0 = dd if lado > 0 else -dd - T
            g = Point(x, ZE).buffer(R_CUB, 48).difference(Point(x, ZE).buffer(R_CANAL, 48))
            e.prisma(g, "xz", y0 - 0.2, T + 0.4, fill="#222", stroke="#000", desplazar=d)


# --- salida ---------------------------------------------------------------------------
def a_png(svg, png, w, h):
    subprocess.run([CHROME, "--headless", "--no-sandbox", "--disable-gpu", "--hide-scrollbars",
                    f"--screenshot={png}", f"--window-size={w},{h + 140}", f"file://{svg}"],
                   capture_output=True, check=False)
    from PIL import Image
    Image.open(png).crop((0, 0, w, h)).save(png, optimize=True)


def foto(e, ruta, w=900, h=560, fondo="#ffffff"):
    with open(ruta + ".svg", "w") as f:
        f.write(e.svg(w, h, fondo))
    a_png(ruta + ".svg", ruta + ".png", w, h)
    os.remove(ruta + ".svg")
    return ruta + ".png"


def grupo(pz):
    n = pz.nombre
    if n.startswith("RUEDA") or n == "ARANDELA":
        return "ruedas_del" if pz.g3d.centroid.x < 100 else "ruedas_tras"
    return {"COSTADO IZQ": "costado_izq", "COSTADO DER": "costado_der", "SOPORTE MOTOR": "soportes",
            "POLEA": "polea"}.get(n, n.lower())


class Modelo:
    """Lo que cambia de un modelo a otro. Cada modelo define piezas() y el instructivo."""
    nombre = ""          # nombre de archivo (camioneta, jeep...)
    titulo = ""
    boton = None         # (x, y, z) del botón si no va en la caja
    cables = None        # cables para los dibujos si el botón no va en la caja

    def piezas(self):
        raise NotImplementedError

    def electronica(self, e, que, d=(0, 0, 0)):
        electronica(e, que, d, boton=self.boton, cables=self.cables)

    def escena(self, grupos, nuevos=(), elec=(), elec_nueva=(), con_ejes=(), con_cubiertas=(),
               transparente=False, cam=(-125, 30), levantar=0.0):
        """Dibuja las piezas de los grupos pedidos; los nuevos van resaltados."""
        e = kit.Escena(kit.Camara(*cam), por_capas=True)
        for pz in self.piezas():
            g = grupo(pz)
            if g not in grupos and g not in nuevos:
                continue
            nuevo = g in nuevos
            kw = {}
            if nuevo:
                kw.update(fill=kit.NUEVO, stroke=kit.BORDE_NUEVO)
                if levantar and pz.tipo != "rueda":
                    kw["desplazar"] = (0, 0, levantar)
            if transparente and pz.nombre == "COSTADO IZQ":
                kw["op"] = 0.35
            if pz.nombre == "PISO":
                kw["prioridad"] = -1
            e.pieza(pz, **kw)
        ejes(e, con_ejes)
        cubiertas(e, con_cubiertas)
        if elec:
            self.electronica(e, elec)
        if elec_nueva:
            self.electronica(e, elec_nueva)
        return e

    def hoja(self, salida):
        hojas = kit.acomodar(self.piezas(), (600, 400))
        assert len(hojas) == 1, "no entra en una hoja"
        h = hojas[0]
        alto = min(400, int(-(-(max(it["geom"].bounds[3] for it in h) + 12) // 10) * 10))
        largo, relleno = kit.guardar_hoja(os.path.join(salida, "hoja"), 1, h, (600, alto),
                                          f"{self.titulo} (sin cola)")
        a_png(os.path.join(salida, "hoja-1.svg"), os.path.join(salida, "hoja-1.png"), 2268,
              round(alto * 3.78))
        return dict(alto=alto, corte=largo / 1000, piezas=len(h))

    def instructivo(self, salida, datos):
        raise NotImplementedError

    def generar(self, salida):
        datos = self.hoja(salida)
        self.instructivo(salida, datos)
        with zipfile.ZipFile(os.path.join(salida, f"{self.nombre}-para-cortar.zip"), "w",
                             zipfile.ZIP_DEFLATED) as z:
            for f in ("hoja-1.svg", "hoja-1.dxf", "hoja-1.png", "instructivo.pdf"):
                z.write(os.path.join(salida, f), f"{self.nombre}-" + f)
        print(self.nombre, datos)
        return datos


# --- instructivo ------------------------------------------------------------------------
CSS = """
@page { size: A4; margin: 14mm 14mm 16mm 14mm; }
body { font-family: Arial, Helvetica, sans-serif; color: #2b2118; font-size: 11.5pt; line-height: 1.4; }
h1 { font-size: 26pt; margin: 0 0 4px; color: #3b2a1a; }
h2 { font-size: 16pt; margin: 18px 0 6px; color: #8a4b12; border-bottom: 2px solid #e8c9a0; padding-bottom: 3px; }
h3 { font-size: 13pt; margin: 10px 0 4px; }
.sub { color: #6b5640; font-size: 13pt; margin-bottom: 10px; }
.paso { page-break-inside: avoid; margin-bottom: 16px; }
.paso img { width: 100%; border: 1px solid #eadcc8; border-radius: 6px; }
.num { display: inline-block; background: #8a4b12; color: #fff; border-radius: 50%; width: 30px;
       height: 30px; text-align: center; line-height: 30px; font-weight: bold; margin-right: 8px; }
table { border-collapse: collapse; width: 100%; font-size: 10.5pt; margin: 6px 0; }
td, th { border: 1px solid #d9c3a3; padding: 4px 6px; text-align: left; vertical-align: top; }
th { background: #f6ead8; }
.ojo { background: #fff4e0; border-left: 4px solid #e8590c; padding: 6px 10px; margin: 8px 0; }
.salto { page-break-before: always; }
.tapa img { width: 100%; }
ul { margin: 4px 0 4px 18px; padding: 0; }
.chico { font-size: 9.5pt; color: #6b5640; }
"""


def foto_ruedas(ruta):
    """Paso 1: discos de una rueda y de la polea."""
    e = kit.Escena(kit.Camara(-96, 14))
    for i, (g, n, col) in enumerate([(llanta(), "1. llanta", "#cfd3d6"), (disco(R_CANAL), "2. disco del medio", None),
                                     (disco(R_RUEDA), "3. disco liso", None)]):
        e.prisma(affinity.translate(g, i * 46, 0), "xz", 0, T, fill=col or kit.MADERA)
        e.texto((i * 46, 0, -27), n, 15, "#8a4b12")
        anillo = Point(0, 0).buffer(R_CUB, 48).difference(Point(0, 0).buffer(R_CANAL, 48))
    e.prisma(affinity.translate(anillo, 3 * 46, 0), "xz", 0, T, fill="#222", stroke="#000")
    e.texto((3 * 46, 0, -27), "4. o-ring", 15, "#8a4b12")
    for i, r in enumerate((10.5, 9.0, 10.5)):
        e.prisma(affinity.translate(disco(r), 205 + i * 26, 0), "xz", 0, T)
    e.texto((231, 0, -27), "polea: grande + chico + grande", 15, "#8a4b12")
    return foto(e, ruta, 900, 300)


def circuito_svg(ruta):
    """Esquema del circuito: una sola vuelta, con los 3 bornes."""
    W, H = 900, 400
    rojo, negro, azul = "#e03131", "#222", "#1c7ed6"

    def caja(x, y, w, h, fill, stroke, txt, col="#222", tam=17):
        return (f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="8" fill="{fill}" '
                f'stroke="{stroke}" stroke-width="2.5"/><text x="{x + w / 2}" y="{y + h / 2 + 6}" '
                f'font-size="{tam}" font-weight="bold" fill="{col}" text-anchor="middle">{txt}</text>')

    def cable(pts, col):
        return (f'<polyline points="{" ".join(f"{a},{b}" for a, b in pts)}" fill="none" '
                f'stroke="{col}" stroke-width="6" stroke-linejoin="round" stroke-linecap="round"/>')

    def nota(x, y, s, col="#555", anchor="middle"):
        return (f'<text x="{x}" y="{y}" font-size="14" fill="{col}" text-anchor="{anchor}">{s}</text>')

    out = [f'<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}" '
           'font-family="Arial, sans-serif">', f'<rect width="{W}" height="{H}" fill="#fff"/>',
           '<text x="450" y="34" font-size="20" font-weight="bold" fill="#222" text-anchor="middle">'
           'PILA (+) → B1 → BOTÓN → B2 → MOTOR → B3 → PILA (−)</text>']
    out += [cable([(230, 150), (330, 110), (390, 110)], rojo),
            cable([(470, 110), (560, 110), (600, 140)], azul),
            cable([(660, 140), (720, 180), (720, 215)], azul),
            cable([(720, 275), (720, 300), (640, 320)], rojo),
            cable([(520, 320), (470, 330)], negro),
            cable([(390, 330), (300, 330), (230, 245)], negro)]
    out += [caja(70, 130, 170, 130, "#2b2b2b", "#111", "PILAS 2xAA", "#fff"),
            '<text x="225" y="160" font-size="26" fill="#ff8787" font-weight="bold">+</text>',
            '<text x="225" y="252" font-size="26" fill="#fff" font-weight="bold">−</text>',
            caja(390, 85, 80, 50, "#fff4e6", "#e8590c", "B1", "#c2410c"),
            caja(680, 215, 80, 60, "#fff4e6", "#e8590c", "B2", "#c2410c"),
            caja(390, 305, 80, 50, "#fff4e6", "#e8590c", "B3", "#c2410c"),
            caja(520, 290, 120, 60, "#a7b0ba", "#4a525a", "MOTOR"),
            '<circle cx="630" cy="125" r="34" fill="#e03131" stroke="#8a1c1c" stroke-width="3"/>',
            '<text x="630" y="131" font-size="15" font-weight="bold" fill="#fff" '
            'text-anchor="middle">BOTÓN</text>']
    out += [nota(300, 95, "cable rojo de las pilas", rojo),
            nota(515, 92, "cable del botón", azul),
            nota(790, 165, "otro cable del botón", azul, "middle"),
            nota(800, 315, "cable del motor", "#555"),
            nota(300, 368, "cable negro de las pilas", "#333"),
            nota(490, 378, "otro cable del motor", "#555")]
    out.append(nota(450, 392, "", "#555"))
    out.append("</svg>")
    with open(ruta + ".svg", "w") as f:
        f.write("\n".join(out))
    a_png(ruta + ".svg", ruta + ".png", W, H)
    os.remove(ruta + ".svg")


def circuito(img):
    circuito_svg(os.path.join(img, "09b-circuito"))
    return os.path.join(img, "09b-circuito.png")


ELECTRONICA_KIT = f"""<li>1 motor 3 V tipo 130 con cables.</li>
<li>1 portapilas 2 x AA con cables + 2 pilas AA.</li>
<li>1 pulsador de 12 mm con traba, con cables.</li>
<li>3 bornes sin soldar (tipo Wago 221).</li>
<li>4 o-rings 31 x 3 mm (cubiertas) y 1 gomita de silicona (transmisión).</li>
<li>2 palitos de brochette de 3 mm (ejes de {{largo_eje:.0f}} mm).</li>
<li>Cinta doble faz.</li>"""

SIN_COLA = """<div class="ojo"><b>No lleva cola.</b> Todas las piezas encastran a presión: si una pestaña no entra, no la
fuerces; pedile a un adulto que la lije un poquito. Armar con un adulto. Piezas chicas: no apto para menores
de 3 años.</div>"""

TABLA_BORNES = """<table><tr><th>Borne</th><th>Cables</th></tr>
<tr><td>B1</td><td>Rojo (+) de las pilas y un cable del botón</td></tr>
<tr><td>B2</td><td>El otro cable del botón y un cable del motor</td></tr>
<tr><td>B3</td><td>El otro cable del motor y el negro (−) de las pilas</td></tr></table>"""


def largo_eje():
    return 2 * (YI + 5 * T) + 2


def html_instructivo(salida, titulo, sub, tapa, como_funciona, madera, pasos, pie):
    """pasos = [(título, imagen o None, html)]; el número se pone solo."""
    rel = lambda r: os.path.relpath(r, salida)
    partes = []
    for i, (tit, img, txt) in enumerate(pasos, 1):
        im = f'<img src="{rel(img)}">' if img else ""
        partes.append(f'<div class="paso"><h3><span class="num">{i}</span>{tit}</h3>{im}\n{txt}</div>')
    html = f"""<!doctype html><html lang="es"><head><meta charset="utf-8"><title>{titulo}</title>
<style>{CSS}</style></head><body>
<h1>{titulo}</h1>
<div class="sub">{sub}</div>
<img src="{rel(tapa)}" style="width:100%">
<h2>Qué trae el kit</h2>
<table><tr><th>Madera (MDF de {T:g} mm)</th><th>Electrónica y otros</th></tr><tr><td><ul>
{madera}
</ul></td><td><ul>
{ELECTRONICA_KIT.format(largo_eje=largo_eje())}
</ul></td></tr></table>
{SIN_COLA}

<div class="paso salto"><h2>¿Cómo funciona?</h2>
{como_funciona(rel)}</div>

<h2 class="salto">Armado</h2>
{chr(10).join(partes)}
<p class="chico">{pie}</p>
</body></html>"""
    ruta = os.path.join(salida, "instructivo.html")
    with open(ruta, "w") as f:
        f.write(html)
    subprocess.run([CHROME, "--headless", "--no-sandbox", "--disable-gpu", "--no-pdf-header-footer",
                    f"--print-to-pdf={os.path.join(salida, 'instructivo.pdf')}", f"file://{ruta}"],
                   capture_output=True, check=False)


def como_funciona(img_atras, extra=""):
    def f(rel):
        return f"""<img src="{rel(img_atras)}" style="width:100%">
<ul>
<li><b>Las pilas</b> guardan la energía. Cuando apretás el <b>botón</b>, se cierra el camino (el
<b>circuito</b>) y la corriente viaja de la pila al motor y vuelve a la pila.</li>
<li><b>El motor</b> gira muy rápido pero con poca fuerza.</li>
<li><b>La goma</b> pasa por el eje finito del motor y por la <b>polea</b> grande del eje de atrás. Como la
polea es mucho más grande, gira más despacio pero con más fuerza: así puede mover {extra or 'el auto'}. Es lo mismo
que hacen los cambios de una bicicleta.</li>
<li>Mirá por la ventanita de la caja: vas a ver la goma y la polea girando.</li>
</ul>"""
    return f


# textos de los pasos que se repiten en todos los modelos
P_RUEDAS = ("Ruedas y polea", """<p>Todavía no se arman: los discos se meten en el eje más adelante. Separá para cada rueda: <b>llanta</b>,
<b>disco del medio</b> y <b>disco liso</b>, y un <b>o-ring</b>. La polea son 3 discos: grande, chico y grande.</p>""")
P_SOPORTES = ("Soportes del motor", """<p>Encastrá los 2 <b>SOPORTES</b> (los que tienen forma de U) en el <b>PISO</b>, en las ranuras del medio.</p>""")
P_COSTADO = ("Primer costado", """<p>Apoyá un <b>COSTADO</b> acostado en la mesa, con el dibujo de la puerta hacia abajo. Encastrá el piso en las
ranuras de abajo del costado.</p>""")
P_MOTOR = ("Motor, eje trasero y goma", """<p>Apoyá el <b>motor</b> en la U de los soportes, con el eje hacia el lado de la ventanita. Pasá el
<b>eje trasero</b> por el agujero de atrás del costado y metele la <b>polea</b> (grande + chico + grande).
Poné la <b>gomita</b> en el eje del motor y en la canaleta de la polea. Pasá también el eje delantero.</p>""")
P_CERRAR = ("Cerrar con el otro costado", """<p>Poné el otro <b>COSTADO</b> encima, haciendo coincidir todas las pestañas con sus ranuras, y los ejes con
sus agujeros. Apretá de a poco, parejo, hasta que entre todo.</p>""")
P_MONTAR = ("Ruedas", """<p>En cada punta de eje: una <b>arandela</b>, el <b>disco liso</b>, el <b>disco del medio</b> y la
<b>llanta</b>, bien apretados. Después estirá el <b>o-ring</b> y ponelo en la canaleta. Las ruedas aprietan los
costados y dejan todo firme.</p>""")
P_PRUEBA = ("¡Prueba!", """<p>Poné las pilas y apretá el botón. Si va para atrás, cambiá entre sí los cables del motor (B2 y B3). Si el
motor gira pero las ruedas no, la gomita patina: probá una más chica.</p>""")


def pie(datos):
    return (f"Diseño propio. Material: 1 hoja de 60 x {datos['alto'] // 10} cm de MDF de {T:g} mm · "
            f"~{datos['corte']:.0f} m de corte láser.")
