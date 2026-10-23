"""Genera la plantilla del auto clásico (v2) y su dibujo de armado.

Uso:  python3 generar.py            (MDF / terciado de 3 mm)
      python3 generar.py 2.8        (si las ranuras quedan flojas, probar otro valor)

Todas las medidas en mm. ROJO = cortar, AZUL = grabar.
"""
import math
import sys

T = float(sys.argv[1]) if len(sys.argv) > 1 else 3.0  # ancho de ranura = espesor real
HOJA_W, HOJA_H = 400, 300

# --- medidas del auto -------------------------------------------------------
LARGO, ALTO = 180, 72          # costado
ANCHO_IN = 64                  # ancho interior entre costados
EJES = [(38, 14), (142, 14)]   # (x, z) de los ejes en el costado
R_EJE = 1.75                   # agujero del eje en el costado (palito de 3 mm gira libre)
R_AJUSTE = 1.4                 # agujero en ruedas y polea (ajusta a presion)

PERFIL = [  # contorno del costado, (x, z) con z hacia arriba
    ("M", (6, 0)), ("L", (174, 0)), ("Q", (180, 0), (180, 6)), ("L", (180, 36)),
    ("Q", (180, 42), (174, 42)), ("L", (150, 42)),
    ("C", (138, 42), (130, 72), (118, 72)), ("L", (76, 72)),
    ("C", (64, 72), (58, 42), (46, 42)), ("L", (6, 42)),
    ("Q", (0, 42), (0, 36)), ("L", (0, 6)), ("Q", (0, 0), (6, 0)), ("Z",),
]
VENTANA_DEL = [("M", (70, 48)), ("L", (96, 48)), ("L", (96, 66)), ("L", (81, 66)),
               ("Q", (75, 66), (72, 60)), ("Z",)]
VENTANA_TRAS = [("M", (102, 48)), ("L", (128, 48)), ("L", (121, 60)),
                ("Q", (118, 66), (112, 66)), ("L", (102, 66)), ("Z",)]
PUERTAS = [("M", (60, 44)), ("L", (60, 12)), ("Q", (60, 8), (64, 8)), ("L", (128, 8)),
           ("Q", (132, 8), (132, 12)), ("L", (132, 40)), ("M", (99, 46)), ("L", (99, 8))]

PISO_TABS = [(20, 36), (82, 98), (148, 164)]   # en x del costado
CAPO_X, CAPO_TABS = (8, 48), [(18, 38)]
BAUL_X, BAUL_TABS = (148, 172), [(152, 168)]
PISO_X = (10, 170)
FRENTE_X, COLA_X = 4, 173                      # ranuras verticales
PLACA_TABS_Z = (14, 28)


def f(v):
    return f"{v:.2f}".rstrip("0").rstrip(".")


def path_d(cmds, tr):
    out = []
    for c in cmds:
        if c[0] == "Z":
            out.append("Z")
        else:
            out.append(c[0] + " ".join(f"{f(tr(*p)[0])},{f(tr(*p)[1])}" for p in c[1:]))
    return " ".join(out)


def tabbed(L, W, tabs):
    """Rectangulo L x W con pestañas de largo T en los dos lados largos."""
    pts = [(0, 0)]
    for a, b in tabs:
        pts += [(a, 0), (a, -T), (b, -T), (b, 0)]
    pts += [(L, 0), (L, W)]
    for a, b in reversed(tabs):
        pts += [(b, W), (b, W + T), (a, W + T), (a, W)]
    pts.append((0, W))
    return pts


class SVG:
    def __init__(self, w, h, unidades=True):
        size = f'width="{w}mm" height="{h}mm"' if unidades else f'width="{w*3}" height="{h*3}"'
        self.head = f'<svg xmlns="http://www.w3.org/2000/svg" {size} viewBox="0 0 {w} {h}">'
        self.cut, self.eng, self.extra = [], [], []

    def poly(self, pts, tr, cut=True):
        d = "M" + " L".join(f"{f(tr(*p)[0])},{f(tr(*p)[1])}" for p in pts) + " Z"
        (self.cut if cut else self.eng).append(f'<path d="{d}"/>')

    def path(self, cmds, tr, cut=True):
        (self.cut if cut else self.eng).append(f'<path d="{path_d(cmds, tr)}"/>')

    def circle(self, x, y, r, cut=True):
        (self.cut if cut else self.eng).append(f'<circle cx="{f(x)}" cy="{f(y)}" r="{f(r)}"/>')

    def rect(self, x, y, w, h, cut=True, rx=0):
        (self.cut if cut else self.eng).append(
            f'<rect x="{f(x)}" y="{f(y)}" width="{f(w)}" height="{f(h)}" rx="{f(rx)}"/>')

    def text(self, x, y, s, size=3.5):
        self.extra.append(f'<text x="{f(x)}" y="{f(y)}" font-size="{size}">{s}</text>')

    def write(self, name, fondo=True):
        parts = [self.head]
        if fondo:
            parts.append(f'<rect width="{HOJA_W}" height="{HOJA_H}" fill="#fff"/>')
            parts.append(f'<rect x="0.5" y="0.5" width="{HOJA_W-1}" height="{HOJA_H-1}" fill="none" '
                         'stroke="#999" stroke-width="0.3" stroke-dasharray="3 2"/>')
        parts.append('<g id="cortar" fill="none" stroke="#ff0000" stroke-width="0.1">')
        parts += self.cut
        parts.append('</g><g id="grabar" fill="none" stroke="#0000ff" stroke-width="0.3">')
        parts += self.eng
        parts.append('</g><g id="etiquetas" fill="#0000ff" font-family="Arial, sans-serif">')
        parts += self.extra
        parts.append("</g></svg>\n")
        open(name, "w").write("\n".join(parts))


def costado(s, ox, oy, espejo):
    def tr(x, z):
        return (ox + (LARGO - x if espejo else x), oy + ALTO - z)
    s.path(PERFIL, tr)
    s.path(VENTANA_DEL, tr)
    s.path(VENTANA_TRAS, tr)
    for x, z in EJES:
        s.circle(*tr(x, z), R_EJE)
    ranuras = [(a, b, 3, 3 + T) for a, b in PISO_TABS]
    ranuras += [(a, b, 39 - T, 39) for a, b in CAPO_TABS + BAUL_TABS]
    ranuras += [(x, x + T, *PLACA_TABS_Z) for x in (FRENTE_X, COLA_X)]
    for x1, x2, z1, z2 in ranuras:
        s.poly([(x1, z1), (x2, z1), (x2, z2), (x1, z2)], tr)
    s.path(PUERTAS, tr, cut=False)
    for hx in (88, 121):  # manijas
        s.poly([(hx, 38), (hx + 7, 38), (hx + 7, 40), (hx, 40)], tr, cut=False)


def plancha(s, ox, oy, x_rango, tabs):
    """Pieza horizontal (piso, capó, baúl) entre los costados."""
    L = x_rango[1] - x_rango[0]
    local = [(a - x_rango[0], b - x_rango[0]) for a, b in tabs]
    tr = lambda u, v: (ox + u, oy + T + v)
    s.poly(tabbed(L, ANCHO_IN, local), tr)
    return tr


def placa_vertical(s, ox, oy):
    """Frente o cola: 64 de ancho x 30 de alto, pestañas a los costados."""
    alto = 36 - 6
    a, b = 36 - PLACA_TABS_Z[1], 36 - PLACA_TABS_Z[0]
    tr = lambda u, v: (ox + T + v, oy + u)
    s.poly(tabbed(alto, ANCHO_IN, [(a, b)]), tr)
    return lambda a_, h_: (ox + T + a_, oy + h_)


def rueda_tapa(s, cx, cy):
    s.circle(cx, cy, 25)
    s.circle(cx, cy, R_AJUSTE)
    s.circle(cx, cy, 19, cut=False)
    s.circle(cx, cy, 8, cut=False)
    for i in range(6):
        ang = math.radians(i * 60)
        s.circle(cx + 13 * math.cos(ang), cy + 13 * math.sin(ang), 1.8, cut=False)


def plantilla():
    s = SVG(HOJA_W, HOJA_H)
    # fila 1: costados
    costado(s, 8, 8, espejo=False)
    costado(s, 196, 8, espejo=True)
    s.text(8, 88, "COSTADO IZQ.")
    s.text(196, 88, "COSTADO DER. (grabado hacia afuera)")

    # fila 2: piso, capó, baúl, techo, soporte motor
    y2 = 94
    tr = plancha(s, 8, y2, PISO_X, PISO_TABS)
    u0 = lambda x: x - PISO_X[0]
    s.poly([(u0(122), 33), (u0(162), 33), (u0(162), 46), (u0(122), 46)], tr)  # ventana polea
    for a in (104.9, 131.1):                                                     # soporte motor
        s.poly([(u0(a), 20 - T / 2), (u0(a + 4), 20 - T / 2),
                (u0(a + 4), 20 + T / 2), (u0(a), 20 + T / 2)], tr)
    s.poly([(34, 16), (92, 16), (92, 48), (34, 48)], tr, cut=False)              # pilas
    s.poly([(u0(109.8), 8), (u0(130.2), 8), (u0(130.2), 33), (u0(109.8), 33)], tr, cut=False)
    s.text(tr(44, 34)[0], tr(44, 34)[1], "PILAS 2xAA")
    s.text(tr(100, 25)[0], tr(100, 25)[1], "MOTOR", 3)
    s.text(8, y2 + 76, "PISO")

    tr = plancha(s, 176, y2, CAPO_X, CAPO_TABS)
    s.circle(*tr(20, 32), 6.25)                       # pulsador 12 mm
    for v in (24, 40):
        s.poly([(2, v), (38, v)], tr, cut=False)
    s.text(176, y2 + 76, "CAPÓ")

    tr = plancha(s, 224, y2, BAUL_X, BAUL_TABS)
    s.text(222, y2 + 76, "BAÚL")

    s.rect(256, y2, 46, 70, rx=3)                     # techo (se saca para cambiar pilas)
    s.rect(260, y2 + 4, 38, 62, cut=False, rx=2)
    s.text(258, y2 + 76, "TECHO")
    for i in range(2):                                # guías del techo
        s.rect(310, y2 + 31 + i * 8, 40, 5, rx=1)
    s.text(310, y2 + 52, "GUÍAS TECHO x2", 3)

    m = [(0, 0), (32, 0), (32, 22), (31.1, 22), (31.1, 22 + T), (27.1, 22 + T), (27.1, 22),
         (26.2, 22), (26.2, 6.6), (5.8, 6.6), (5.8, 22), (4.9, 22), (4.9, 22 + T),
         (0.9, 22 + T), (0.9, 22), (0, 22)]
    s.poly(m, lambda x, y: (310 + x, y2 + y))
    s.text(310, y2 + 29, "SOPORTE MOTOR", 3)
    s.circle(375, 110, 14)
    s.circle(375, 110, R_AJUSTE)
    for i in range(4):                                # arandelas
        s.circle(315 + i * 12, 155, 5)
        s.circle(315 + i * 12, 155, R_EJE)
    s.text(310, 164, "ARANDELAS x4", 3)

    # fila 3: frente, cola, poleas, ruedas
    p = placa_vertical(s, 8, 176)
    for a in (10, 54):
        s.circle(*p(a, 12), 2.6)                      # luces (LED 5 mm, opcional)
        s.circle(*p(a, 12), 6, cut=False)
    s.rect(*p(22, 6), 20, 14, cut=False, rx=3)
    for h in (9.5, 13, 16.5):
        s.poly([(24, h), (40, h)], lambda a_, h_: p(a_, h_), cut=False)
    s.poly([(2, 25), (62, 25)], lambda a_, h_: p(a_, h_), cut=False)
    s.text(8, 211, "FRENTE", 3)

    p = placa_vertical(s, 8, 214 + 2)
    for a in (4, 50):
        s.rect(*p(a, 8), 10, 8, cut=False, rx=2)
    s.rect(*p(20, 17), 24, 9, cut=False, rx=1)
    s.text(p(23.5, 23)[0], p(23.5, 23)[1], "TUC 001", 4.2)
    s.text(8, 251, "COLA", 3)

    for cx in (26, 66):
        s.circle(cx, 270, 18)
        s.circle(cx, 270, R_AJUSTE)
    s.text(8, 293, "POLEA: 36 + 28 + 36", 3)

    fila1 = [(115 + 52 * i, 199) for i in range(5)]
    fila2 = [(115 + 52 * i, 253) for i in range(5)]
    for cx, cy in fila1[:4]:
        rueda_tapa(s, cx, cy)
    for cx, cy in fila1[4:] + fila2[:3]:              # interiores, sin grabar
        s.circle(cx, cy, 25)
        s.circle(cx, cy, R_AJUSTE)
    for cx, cy in fila2[3:] + [(372, 199), (372, 253)]:  # discos del medio (canaleta)
        s.circle(cx, cy, 22)
        s.circle(cx, cy, R_AJUSTE)
    s.text(90, 293, "RUEDAS: 4 tapas (grabadas) + 4 interiores + 4 discos chicos (canaleta de la goma)", 3)
    s.text(300, 293, f"ROJO=cortar AZUL=grabar | material {f(T)} mm", 3)
    s.write("auto-clasico.svg")


def dibujo():
    """Dibujo del auto armado, visto de costado y de frente (no se corta)."""
    W, H, K = 330, 130, 1.0
    piso = 11  # altura del costado sobre el suelo
    suelo = 115
    out = [f'<svg xmlns="http://www.w3.org/2000/svg" width="{W*3}" height="{H*3}" viewBox="0 0 {W} {H}" '
           'font-family="Arial, sans-serif">', f'<rect width="{W}" height="{H}" fill="#fff"/>',
           '<text x="10" y="12" font-size="7" font-weight="bold" fill="#333">Auto clásico (v2)</text>',
           f'<line x1="5" y1="{suelo}" x2="{W-5}" y2="{suelo}" stroke="#bbb" stroke-width="0.8"/>']
    ox = 15
    tr = lambda x, z: (ox + x, suelo - piso - z)
    madera, borde = "#e8cfa4", "#9b7546"
    out.append(f'<path d="{path_d(PERFIL, tr)}" fill="{madera}" stroke="{borde}" stroke-width="0.6"/>')
    for v in (VENTANA_DEL, VENTANA_TRAS):
        out.append(f'<path d="{path_d(v, tr)}" fill="#5b6770" stroke="{borde}" stroke-width="0.5"/>')
    out.append(f'<path d="{path_d(PUERTAS, tr)}" fill="none" stroke="#a07a4a" stroke-width="0.5"/>')
    for hx in (88, 121):
        x, y = tr(hx, 40)
        out.append(f'<rect x="{x}" y="{y}" width="7" height="2" fill="#a07a4a"/>')
    x, y = tr(74, 75)
    out.append(f'<rect x="{x}" y="{y}" width="46" height="3" rx="1" fill="#d9b98a" stroke="{borde}" stroke-width="0.5"/>')
    x, y = tr(25.5, 46)
    out.append(f'<rect x="{x}" y="{y}" width="5" height="4" rx="1.5" fill="#d33"/>')
    for ex, ez in EJES:
        cx, cy = tr(ex, ez)
        out.append(f'<circle cx="{cx}" cy="{cy}" r="25" fill="#2f2f2f"/>'
                   f'<circle cx="{cx}" cy="{cy}" r="22.5" fill="#dcbf91" stroke="{borde}" stroke-width="0.5"/>'
                   f'<circle cx="{cx}" cy="{cy}" r="19" fill="none" stroke="#a07a4a" stroke-width="0.5"/>'
                   f'<circle cx="{cx}" cy="{cy}" r="8" fill="none" stroke="#a07a4a" stroke-width="0.5"/>')
        for i in range(6):
            a = math.radians(i * 60)
            out.append(f'<circle cx="{cx+13*math.cos(a):.2f}" cy="{cy+13*math.sin(a):.2f}" r="1.8" '
                       'fill="none" stroke="#a07a4a" stroke-width="0.5"/>')
        out.append(f'<circle cx="{cx}" cy="{cy}" r="1.5" fill="#6b4c22"/>')
    out.append(f'<text x="{ox+40}" y="{suelo+10}" font-size="5" fill="#555">Costado: 18 cm de largo, '
               '8,6 cm de alto, 10 cm de ancho con ruedas</text>')

    # vista de frente
    fx = 240
    trf = lambda y, z: (fx + y, suelo - piso - z)
    out.append(f'<text x="{fx-8}" y="12" font-size="5" fill="#555">De frente</text>')
    for y0 in (-3, ANCHO_IN):
        x, yy = trf(y0, 72)
        out.append(f'<rect x="{x}" y="{yy}" width="3" height="72" fill="{madera}" stroke="{borde}" stroke-width="0.5"/>')
    x, yy = trf(0, 72)
    out.append(f'<rect x="{x}" y="{yy}" width="{ANCHO_IN}" height="33" fill="#5b6770"/>')
    x, yy = trf(-3, 75)
    out.append(f'<rect x="{x}" y="{yy}" width="70" height="3" rx="1" fill="#d9b98a" stroke="{borde}" stroke-width="0.5"/>')
    x, yy = trf(0, 39)
    out.append(f'<rect x="{x}" y="{yy}" width="{ANCHO_IN}" height="3" fill="#d9b98a" stroke="{borde}" stroke-width="0.5"/>')
    x, yy = trf(0, 36)
    out.append(f'<rect x="{x}" y="{yy}" width="{ANCHO_IN}" height="30" fill="{madera}" stroke="{borde}" stroke-width="0.5"/>')
    for a in (10, 54):
        cx, cy = trf(a, 36 - 12)
        out.append(f'<circle cx="{cx}" cy="{cy}" r="6" fill="none" stroke="#a07a4a" stroke-width="0.5"/>'
                   f'<circle cx="{cx}" cy="{cy}" r="2.6" fill="#ffe066" stroke="#a07a4a" stroke-width="0.4"/>')
    x, yy = trf(22, 36 - 6)
    out.append(f'<rect x="{x}" y="{yy}" width="20" height="14" rx="3" fill="none" stroke="#a07a4a" stroke-width="0.5"/>')
    for h in (9.5, 13, 16.5):
        x, yy = trf(24, 36 - h)
        out.append(f'<line x1="{x}" y1="{yy}" x2="{x+16}" y2="{yy}" stroke="#a07a4a" stroke-width="0.5"/>')
    for y0 in (-15, ANCHO_IN + 6):
        x, yy = trf(y0, 25 - piso + 25)
        out.append(f'<rect x="{x}" y="{yy}" width="9" height="50" rx="2" fill="#2f2f2f"/>')
    x, yy = trf(-15, 14)
    out.append(f'<line x1="{x}" y1="{yy}" x2="{x+100}" y2="{yy}" stroke="#6b4c22" stroke-width="1"/>')
    out.append("</svg>\n")
    open("como-se-ve.svg", "w").write("\n".join(out))


if __name__ == "__main__":
    plantilla()
    dibujo()
    print("Listo: auto-clasico.svg y como-se-ve.svg")
