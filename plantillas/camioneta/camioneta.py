"""Camioneta clásica para chicos (v5): pocas piezas, todo encastrado a presión, SIN COLA.

Inspirada en las camionetas clásicas (tipo F-100) y en kits que encastran sin cola
(FBRKN Laser Cut Car, camión solar de madera, Ugears).

Construcción: 2 costados con la silueta + piezas que los unen con pestañas y ranuras.
La caja de carga queda abierta: ahí van las pilas, los bornes y el botón, a la vista.
Por una ventanita en la caja se ven la goma y la polea girando.

Uso:  python3 camioneta.py [espesor] [ajuste]
      espesor = espesor real de la placa (3 por defecto)
      ajuste  = cuánto más angostas que el espesor se cortan las ranuras para que
                encastren firme (0.1 por defecto; si quedan flojas, subirlo)
"""
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
sys.path.insert(0, os.path.join(AQUI, "..", "kit-autos"))
import kit  # noqa: E402  (motor común: hojas, dibujos 3D)

T = float(sys.argv[1]) if len(sys.argv) > 1 and __name__ == "__main__" else 3.0
AJ = float(sys.argv[2]) if len(sys.argv) > 2 and __name__ == "__main__" else 0.1
kit.configurar(T)
CHROME = shutil.which("chromium") or "/opt/pw-browsers/chromium-1194/chrome-linux/chrome"

# --- medidas (mm) ------------------------------------------------------------------
YI = 29.0                         # mitad del ancho interior (entre costados)
EJES = (42.0, 152.0)
ZE = 18.5                         # altura de los ejes
R_RUEDA, R_CANAL, R_CUB = 18.0, 15.5, 18.5
Z_PISO = 8.0                      # piso: z 8 a 11
Z_CAJA = 28.0                     # piso de la caja: z 28 a 31
Z_CAPO = 35.0
Z_TECHO = 58.0
X_FRENTE, X_CABINA, X_PORTON = 4.0, 100.0, 193.0
MOTOR_X = (116.0, 136.4)          # cuna del motor (el motor apoya en z 13)
MOTOR_Y = (-6.0, 19.0)
SOPORTES_Y = (-2.0, 12.0)
POLEA_Y = (-17.0, -8.0)
PILAS = (107.0, -3.0, 165.0, 29.0)
BORNES = [(166, -27, 179, -9), (166, -8, 179, 10), (166, 11, 179, 29)]
BOTON = (185.5, 0.0)
VENTANA = (120.0, -24.0, 166.0, -6.0)


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


# --- costados -------------------------------------------------------------------
TABS_PISO = [(20, 34), (60, 90), (118, 133), (168, 184)]
TABS_CAJA = [(112, 126), (168, 182)]
TABS_CAPO = [(14, 26), (36, 48)]
TABS_TECHO = [(74, 96)]
TABS_FRENTE_Z = [(16, 30)]
TABS_CABINA_Z = [(15, 25), (36, 52)]
TABS_PORTON_Z = [(15, 25), (32, 42)]
TABS_ABAJO_Y = [(-20, -8), (8, 20)]


def silueta():
    p = Polygon([(0, 7), (0, 39), (2, 41.5), (53, 41.5), (64, 64), (106, 64), (106, 47),
                 (200, 47), (200, 7), (197, 5), (3, 5)])
    p = redondo(p, 2.5)
    return p.buffer(1.2, 8).buffer(-1.2, 8)   # suaviza también las esquinas hacia adentro


def costado():
    p = silueta()
    ventana = Polygon([(69, 45), (97, 45), (97, 55.5), (74.1, 55.5)])
    p = p.difference(redondo(ventana, 1.5))
    hue = []
    hue += [ranura(a, Z_PISO, b, Z_PISO + T) for a, b in TABS_PISO]
    hue += [ranura(a, Z_CAJA, b, Z_CAJA + T) for a, b in TABS_CAJA]
    hue += [ranura(a, Z_CAPO, b, Z_CAPO + T) for a, b in TABS_CAPO]
    hue += [ranura(a, Z_TECHO, b, Z_TECHO + T) for a, b in TABS_TECHO]
    hue += [ranura(X_FRENTE, a, X_FRENTE + T, b) for a, b in TABS_FRENTE_Z]
    hue += [ranura(X_CABINA, a, X_CABINA + T, b) for a, b in TABS_CABINA_Z]
    hue += [ranura(X_PORTON, a, X_PORTON + T, b) for a, b in TABS_PORTON_Z]
    hue += [Point(x, ZE).buffer(kit.R_EJE, 24) for x in EJES]
    p = p.difference(unary_union(hue))
    grab = [LineString([(57, 41.5), (57, 15), (100, 15), (100, 41.5)]),       # puerta
            box(88, 37, 95, 39.2).exterior,                                       # manija
            LineString([(108, 43), (196, 43)])]                                  # borde de la caja
    for x in EJES:                                                                # guardabarros
        arco = [(x + 22 * math.cos(math.radians(a)), ZE + 22 * math.sin(math.radians(a)))
                for a in range(10, 171, 4)]
        grab.append(LineString(arco))
    return p, grab


# --- piezas que unen los costados ------------------------------------------------
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


def piezas():
    P = kit.Pieza
    out = []
    c, grab = costado()
    out.append(P(c, "COSTADO IZQ", "xz", -YI - T, grab, etiqueta="", tipo="carroceria"))
    cd = P(c, "COSTADO DER", "xz", YI, grab, etiqueta="", tipo="carroceria", espejo=True)
    out.append(cd)

    # piso
    piso = con_pestanas_x(box(1, -YI, 199, YI), TABS_PISO)
    hue = []
    for x in (X_FRENTE, X_CABINA, X_PORTON):
        hue += [ranura(x, a, x + T, b) for a, b in TABS_ABAJO_Y]
    for y in SOPORTES_Y:
        hue += [ranura(112.5, y, 115.5, y + T), ranura(136.9, y, 139.9, y + T)]
    hue.append(box(140, POLEA_Y[0] - 1.5, 164, POLEA_Y[1] + 1.5))
    piso = piso.difference(unary_union(hue))
    pz = P(piso, "PISO", "xy", Z_PISO, [box(MOTOR_X[0], MOTOR_Y[0], MOTOR_X[1], MOTOR_Y[1]).exterior],
           etiqueta="", tipo="chasis")
    pz.textos = [("PISO", 60, 0, 5), ("FRENTE", 20, 0, 4), ("MOTOR", 126, 6, 3.5)]
    out.append(pz)

    # piso de la caja (las pilas, los bornes y el botón van arriba, a la vista)
    caja = con_pestanas_x(box(X_CABINA + T, -YI, X_PORTON, YI), TABS_CAJA)
    caja = caja.difference(redondo(box(*VENTANA), 2))
    caja = caja.difference(Point(*BOTON).buffer(6.25, 32)).difference(Point(185.5, -14).buffer(2.5, 16))
    grab = [box(*PILAS).exterior] + [box(*b).exterior for b in BORNES]
    pz = P(caja, "CAJA", "xy", Z_CAJA, grab, etiqueta="", tipo="chasis")
    pz.textos = [("PILAS 2xAA", 136, 10, 5), ("+", 111, 22, 5), ("-", 111, 1, 5),
                 ("B1", 172.5, -19, 4), ("B2", 172.5, 0, 4), ("B3", 172.5, 19, 4),
                 ("POLEA", 143, -16.5, 3.5)]
    out.append(pz)

    # capó y techo
    capo = con_pestanas_x(box(X_FRENTE + T, -YI, 53, YI), TABS_CAPO)
    out.append(P(capo, "CAPÓ", "xy", Z_CAPO, [LineString([(12, 0), (50, 0)])], etiqueta="CAPÓ",
                 tipo="carroceria"))
    techo = con_pestanas_x(box(66, -YI, 105.5, YI), TABS_TECHO)
    techo = techo.difference(unary_union([ranura(X_CABINA, a, X_CABINA + T, b)
                                          for a, b in TABS_ABAJO_Y]))
    out.append(P(redondo(techo, 0.8), "TECHO", "xy", Z_TECHO, etiqueta="TECHO", tipo="carroceria"))

    # frente (parrilla y faros)
    fr = con_pestanas_y(box(-YI, Z_PISO + T, YI, Z_CAPO), TABS_FRENTE_Z)
    for y in (-21, 21):
        fr = fr.difference(Point(y, 25).buffer(2.6, 16))
    grab = [Point(y, 25).buffer(6, 32).exterior for y in (-21, 21)]
    grab += [box(-13, 16, 13, 31).exterior] + [LineString([(-11, z), (11, z)]) for z in (19.5, 23.5, 27.5)]
    grab.append(LineString([(-YI + 1, 14), (YI - 1, 14)]))
    out.append(P(fr, "FRENTE", "yz", X_FRENTE, grab, etiqueta="", tipo="carroceria"))

    # pared de atrás de la cabina (con pestañas arriba para el techo)
    cab = con_pestanas_y(box(-YI, Z_PISO + T, YI, Z_TECHO), TABS_CABINA_Z)
    for a, b in TABS_ABAJO_Y:
        cab = unir(cab, box(a, Z_TECHO, b, Z_TECHO + T))
    out.append(P(cab, "CABINA", "yz", X_CABINA, [redondo(box(-18, 44, 18, 54), 3).exterior],
                 etiqueta="CABINA", tipo="carroceria"))

    # portón trasero
    po = con_pestanas_y(box(-YI, Z_PISO + T, YI, 45), TABS_PORTON_Z)
    grab = [box(-27, 33, -22, 41).exterior, box(22, 33, 27, 41).exterior,
            redondo(box(-15, 17, 15, 38), 2).exterior]
    out.append(P(po, "PORTÓN", "yz", X_PORTON, grab, etiqueta="", tipo="carroceria"))

    # 2 soportes del motor (cuna: el motor se apoya y la caja lo aprieta desde arriba)
    so = box(112, Z_PISO + T, 140, 24).difference(box(MOTOR_X[0], 13, MOTOR_X[1], 40))
    so = unir(so, box(112.5, Z_PISO, 115.5, Z_PISO + T), box(136.9, Z_PISO, 139.9, Z_PISO + T))
    for y in SOPORTES_Y:
        out.append(P(so, "SOPORTE MOTOR", "xz", y, etiqueta="M", tipo="chasis"))

    out += ruedas()
    return out


def llanta():
    p = Point(0, 0).buffer(R_RUEDA, 64)
    anillo = Point(0, 0).buffer(13.5, 64).difference(Point(0, 0).buffer(5, 48))
    rayos = unary_union([affinity.rotate(box(-1.8, 0, 1.8, 16), a * 72, origin=(0, 0))
                         for a in range(5)])
    return p.difference(anillo.difference(rayos)).difference(Point(0, 0).buffer(kit.R_AJUSTE, 16))


def disco(r, agujero=kit.R_AJUSTE):
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
def electronica(e, que=("motor", "goma", "pilas", "bornes", "boton", "cables"), d=(0, 0, 0)):
    zc = Z_CAJA + T
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
        e.prisma(Point(*BOTON).buffer(6, 24), "xy", zc - 18, 18, fill="#555", stroke="#222", desplazar=d)
        e.prisma(Point(*BOTON).buffer(5, 24), "xy", zc, 7, fill="#e03131", stroke="#8a1c1c", desplazar=d)
    if "cables" in que:
        z = zc + 1
        rojo, negro, azul = "#e03131", "#222", "#1c7ed6"
        for pts, col in [
            ([(108, 22, z + 6), (112, 26, z), (160, 27, z), (168, 21, z + 5)], rojo),      # + a B1? (B3)
            ([(108, 2, z + 6), (104, 2, z), (104, -26, z), (168, -21, z + 5)], negro),
            ([(185.5, -6, z), (180, -15, z + 2), (175, -18, z + 5)], azul),
            ([(185.5, 6, z), (180, 3, z + 2), (175, 1, z + 5)], azul),
            ([(126, -6, 26), (126, -10, z + 2), (160, -5, z + 4), (175, -1, z + 5)], rojo),
            ([(130, 19, 26), (126, -18, z + 1), (162, -26, z + 4), (172, 20, z + 5)], negro),
        ]:
            e.linea([(x + d[0], y + d[1], zz + d[2]) for x, y, zz in pts], col, 1.8)


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


def escena(grupos, nuevos=(), elec=(), elec_nueva=(), con_ejes=(), con_cubiertas=(),
           transparente=False, cam=(-125, 30), levantar=0.0):
    """Dibuja las piezas de los grupos pedidos; los nuevos van resaltados."""
    e = kit.Escena(kit.Camara(*cam), por_capas=True)
    for pz in piezas():
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
        electronica(e, elec)
    if elec_nueva:
        electronica(e, elec_nueva)
    return e


def grupo(pz):
    n = pz.nombre
    if n.startswith("RUEDA") or n == "ARANDELA":
        return "ruedas_del" if pz.g3d.centroid.x < 100 else "ruedas_tras"
    return {"COSTADO IZQ": "costado_izq", "COSTADO DER": "costado_der", "SOPORTE MOTOR": "soportes",
            "POLEA": "polea"}.get(n, n.lower())


def hoja(salida):
    hojas = kit.acomodar(piezas(), (600, 400))
    assert len(hojas) == 1, "no entra en una hoja"
    h = hojas[0]
    alto = min(400, int(-(-(max(it["geom"].bounds[3] for it in h) + 12) // 10) * 10))
    largo, relleno = kit.guardar_hoja(os.path.join(salida, "hoja"), 1, h, (600, alto),
                                      "Camioneta clásica (sin cola)")
    a_png(os.path.join(salida, "hoja-1.svg"), os.path.join(salida, "hoja-1.png"), 2268,
          round(alto * 3.78))
    return dict(alto=alto, corte=largo / 1000, piezas=len(h))


CSS = open(os.path.join(AQUI, "..", "kit-autos", "generar.py")).read().split('CSS = """')[1].split('"""')[0]


def instructivo(salida, datos):
    img = os.path.join(salida, "pasos")
    os.makedirs(img, exist_ok=True)
    R = {}
    todo = ["piso", "soportes", "costado_izq", "costado_der", "frente", "cabina", "portón", "caja",
            "capó", "techo", "polea", "ruedas_del", "ruedas_tras"]
    R["tapa"] = foto(escena(todo, elec=("pilas", "bornes", "boton", "goma"),
                            con_ejes=EJES, con_cubiertas=EJES, cam=(-128, 26)),
                     os.path.join(img, "00-camioneta"), 1100, 600, "#f6f1ea")
    R["atras"] = foto(escena(todo, elec=("pilas", "bornes", "boton", "goma", "motor"),
                             con_ejes=EJES, con_cubiertas=EJES, cam=(-35, 40)),
                      os.path.join(img, "00b-caja"), 900, 520, "#f6f1ea")
    # paso 1: ruedas
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
    R["1"] = foto(e, os.path.join(img, "01-ruedas"), 900, 300)
    pasos = [
        ("2", dict(grupos=("piso",), nuevos=("soportes",), levantar=10)),
        ("3", dict(grupos=("piso", "soportes"), nuevos=("costado_izq",), levantar=0)),
        ("4", dict(grupos=("piso", "soportes", "costado_izq"), nuevos=("frente", "cabina", "portón"),
                   levantar=10)),
        ("5", dict(grupos=("piso", "soportes", "costado_izq", "frente", "cabina", "portón"),
                   nuevos=("polea",), elec_nueva=("motor", "goma"), con_ejes=EJES, transparente=True)),
        ("6", dict(grupos=("piso", "soportes", "costado_izq", "frente", "cabina", "portón", "polea"),
                   nuevos=("caja", "capó", "techo"), elec=("motor", "goma"), con_ejes=EJES, levantar=12,
                   transparente=True)),
        ("7", dict(grupos=("piso", "soportes", "costado_izq", "frente", "cabina", "portón", "polea",
                           "caja", "capó", "techo"), nuevos=("costado_der",), elec=("motor", "goma"),
                   con_ejes=EJES, cam=(-55, 30))),
        ("8", dict(grupos=("piso", "soportes", "costado_izq", "costado_der", "frente", "cabina", "portón",
                           "polea", "caja", "capó", "techo"), nuevos=("ruedas_del", "ruedas_tras"),
                   elec=("motor", "goma"), con_ejes=EJES, con_cubiertas=EJES)),
        ("9", dict(grupos=todo, elec=("motor", "goma"), elec_nueva=("pilas", "bornes", "boton", "cables"),
                   con_ejes=EJES, con_cubiertas=EJES, cam=(-35, 48))),
    ]
    for n, kw in pasos:
        R[n] = foto(escena(**kw), os.path.join(img, f"{n.zfill(2)}-paso"), 900, 520)
    sys.path.insert(0, os.path.join(AQUI, "..", "kit-autos"))
    import generar
    generar.circuito_svg(os.path.join(img, "09b-circuito"))
    R["9b"] = os.path.join(img, "09b-circuito.png")
    rel = lambda r: os.path.relpath(r, salida)
    html = f"""<!doctype html><html lang="es"><head><meta charset="utf-8"><title>Camioneta clásica</title>
<style>{CSS}</style></head><body>
<h1>Camioneta clásica</h1>
<div class="sub">Juguete de madera con motor eléctrico · <b>se arma sin cola</b> · {datos['piezas']} piezas</div>
<img src="{rel(R['tapa'])}" style="width:100%">
<h2>Qué trae el kit</h2>
<table><tr><th>Madera (MDF de {T:g} mm)</th><th>Electrónica y otros</th></tr><tr><td><ul>
<li>2 costados, piso, piso de la caja, capó, techo, frente, pared de la cabina y portón.</li>
<li>2 soportes del motor.</li>
<li>4 ruedas (3 discos cada una), 4 arandelas y la polea (3 discos).</li>
</ul></td><td><ul>
<li>1 motor 3 V tipo 130 con cables.</li>
<li>1 portapilas 2 x AA con cables + 2 pilas AA.</li>
<li>1 pulsador de 12 mm con traba, con cables.</li>
<li>3 bornes sin soldar (tipo Wago 221).</li>
<li>4 o-rings 31 x 3 mm (cubiertas) y 1 gomita de silicona (transmisión).</li>
<li>2 palitos de brochette de 3 mm (ejes de {2 * (YI + 5 * T) + 2:.0f} mm).</li>
<li>Cinta doble faz.</li>
</ul></td></tr></table>
<div class="ojo"><b>No lleva cola.</b> Todas las piezas encastran a presión: si una pestaña no entra, no la
fuerces; pedile a un adulto que la lije un poquito. Armar con un adulto. Piezas chicas: no apto para menores
de 3 años.</div>

<div class="paso salto"><h2>¿Cómo funciona?</h2>
<img src="{rel(R['atras'])}" style="width:100%">
<ul>
<li><b>Las pilas</b> guardan la energía. Cuando apretás el <b>botón</b>, se cierra el camino (el
<b>circuito</b>) y la corriente viaja de la pila al motor y vuelve a la pila.</li>
<li><b>El motor</b> gira muy rápido pero con poca fuerza.</li>
<li><b>La goma</b> pasa por el eje finito del motor y por la <b>polea</b> grande del eje de atrás. Como la
polea es mucho más grande, gira más despacio pero con más fuerza: así puede mover la camioneta. Es lo mismo
que hacen los cambios de una bicicleta.</li>
<li>Mirá por la ventanita de la caja: vas a ver la goma y la polea girando.</li>
</ul></div>

<h2 class="salto">Armado</h2>
<div class="paso"><h3><span class="num">1</span>Ruedas y polea</h3><img src="{rel(R['1'])}">
<p>Todavía no se arman: los discos se meten en el eje en el paso 8. Separá para cada rueda: <b>llanta</b>,
<b>disco del medio</b> y <b>disco liso</b>, y un <b>o-ring</b>. La polea son 3 discos: grande, chico y grande.</p></div>
<div class="paso"><h3><span class="num">2</span>Soportes del motor</h3><img src="{rel(R['2'])}">
<p>Encastrá los 2 <b>SOPORTES</b> (los que tienen forma de U) en el <b>PISO</b>, en las ranuras del medio.</p></div>
<div class="paso"><h3><span class="num">3</span>Primer costado</h3><img src="{rel(R['3'])}">
<p>Apoyá un <b>COSTADO</b> acostado en la mesa, con el dibujo de la puerta hacia abajo. Encastrá el piso en las
ranuras de abajo del costado.</p></div>
<div class="paso"><h3><span class="num">4</span>Frente, cabina y portón</h3><img src="{rel(R['4'])}">
<p>Encastrá el <b>FRENTE</b> (con los faros) adelante, la pared de la <b>CABINA</b> en el medio y el
<b>PORTÓN</b> atrás. Cada uno entra en el piso y en el costado.</p></div>
<div class="paso"><h3><span class="num">5</span>Motor, eje trasero y goma</h3><img src="{rel(R['5'])}">
<p>Apoyá el <b>motor</b> en la U de los soportes, con el eje hacia el lado de la ventanita. Pasá el
<b>eje trasero</b> por el agujero de atrás del costado y metele la <b>polea</b> (grande + chico + grande).
Poné la <b>gomita</b> en el eje del motor y en la canaleta de la polea. Pasá también el eje delantero.</p></div>
<div class="paso"><h3><span class="num">6</span>Caja, capó y techo</h3><img src="{rel(R['6'])}">
<p>Encastrá el piso de la <b>CAJA</b> arriba del motor (lo deja apretado en su lugar), el <b>CAPÓ</b> y el
<b>TECHO</b>.</p></div>
<div class="paso"><h3><span class="num">7</span>Cerrar con el otro costado</h3><img src="{rel(R['7'])}">
<p>Poné el otro <b>COSTADO</b> encima, haciendo coincidir todas las pestañas con sus ranuras, y los ejes con
sus agujeros. Apretá de a poco, parejo, hasta que entre todo.</p></div>
<div class="paso"><h3><span class="num">8</span>Ruedas</h3><img src="{rel(R['8'])}">
<p>En cada punta de eje: una <b>arandela</b>, el <b>disco liso</b>, el <b>disco del medio</b> y la
<b>llanta</b>, bien apretados. Después estirá el <b>o-ring</b> y ponelo en la canaleta. Las ruedas aprietan los
costados y dejan todo firme.</p></div>
<div class="paso"><h3><span class="num">9</span>Pilas, botón y cables (sin soldar)</h3><img src="{rel(R['9'])}">
<p>En la caja está todo dibujado. Pegá el <b>portapilas</b> con doble faz donde dice PILAS. Atornillá el
<b>botón</b> en el agujero redondo. Poné los <b>bornes</b> en B1, B2 y B3. Para conectar: levantá la palanquita,
meté el cable pelado y bajala. Los cables del motor suben por la ventanita y los del botón, por el agujerito.</p>
<img src="{rel(R['9b'])}">
<table><tr><th>Borne</th><th>Cables</th></tr>
<tr><td>B1</td><td>Rojo (+) de las pilas y un cable del botón</td></tr>
<tr><td>B2</td><td>El otro cable del botón y un cable del motor</td></tr>
<tr><td>B3</td><td>El otro cable del motor y el negro (−) de las pilas</td></tr></table></div>
<div class="paso"><h3><span class="num">10</span>¡Prueba!</h3>
<p>Poné las pilas y apretá el botón. Si va para atrás, cambiá entre sí los cables del motor (B2 y B3). Si el
motor gira pero las ruedas no, la gomita patina: probá una más chica.</p></div>
<p class="chico">Diseño propio. Material: 1 hoja de 60 x {datos['alto'] // 10} cm de MDF de {T:g} mm · ~{datos['corte']:.0f} m de corte láser.</p>
</body></html>"""
    ruta = os.path.join(salida, "instructivo.html")
    with open(ruta, "w") as f:
        f.write(html)
    subprocess.run([CHROME, "--headless", "--no-sandbox", "--disable-gpu", "--no-pdf-header-footer",
                    f"--print-to-pdf={os.path.join(salida, 'instructivo.pdf')}", f"file://{ruta}"],
                   capture_output=True, check=False)


def main():
    salida = AQUI
    datos = hoja(salida)
    instructivo(salida, datos)
    with zipfile.ZipFile(os.path.join(salida, "camioneta-para-cortar.zip"), "w", zipfile.ZIP_DEFLATED) as z:
        for f in ("hoja-1.svg", "hoja-1.dxf", "hoja-1.png", "instructivo.pdf"):
            z.write(os.path.join(salida, f), "camioneta-" + f)
    print(datos)


if __name__ == "__main__":
    main()
