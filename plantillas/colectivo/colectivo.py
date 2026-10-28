"""Colectivo para chicos: todo encastrado a presión, SIN COLA.

Un "bondi" alto con ventanillas. El techo se apoya arriba, en unas pestañitas de los
costados, y se saca con la mano para cambiar las pilas. El botón va en el techo, como el
timbre del colectivo. Comparte con la camioneta el piso, la caja (pilas y bornes), el motor,
las ruedas y la electrónica (ver ../encastre.py).

Uso:  python3 colectivo.py [espesor] [ajuste]
"""
import os
import sys

from shapely.geometry import LineString, Point, Polygon, box
from shapely.ops import unary_union

AQUI = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(AQUI, ".."))
import encastre as E  # noqa: E402
from encastre import EJES, X_CABINA, X_FRENTE, X_PORTON, YI, Z_PISO, pared, redondo, unir  # noqa: E402

kit = E.kit

# --- medidas propias (mm) ----------------------------------------------------------
Z_ALTO = 80.0                    # borde de arriba de los costados; el techo va de 80 a 83
X_ASIENTOS = (52.0, X_CABINA)    # 2 filas de asientos (la de atrás cierra la caja)
TABS_TECHO = [(20, 36), (92, 108), (164, 180)]   # pestañas de los costados que entran en el techo
FLOJO = 0.3                      # el techo tiene que salir fácil: ranuras más anchas
TABS_FRENTE_Z = [(16, 30), (36, 44)]
TABS_ASIENTOS_Z = [(15, 25), (32, 40)]
TABS_FONDO_Z = [(15, 25), (32, 42)]
Z_VENT = (48.0, 71.0)            # ventanillas
VENTANILLAS = [(10, 30)] + [(36 + i * 31, 63 + i * 31) for i in range(5)]
BOTON_TECHO = (180.0, 0.0)
VUELO = 2.0                      # cuánto sobresale el techo de los costados


def silueta():
    p = Polygon([(0, 7), (0, Z_ALTO - 10), (10, Z_ALTO), (200, Z_ALTO), (200, 7), (197, 5), (3, 5)])
    p = E.suavizar(redondo(p, 2.5), 2.5)
    T = E.T
    return unir(p, *[box(a, Z_ALTO - 1, b, Z_ALTO + T) for a, b in TABS_TECHO])


class Colectivo(E.Modelo):
    nombre = "colectivo"
    titulo = "Colectivo"
    boton = BOTON_TECHO + (Z_ALTO + 3.0,)
    cables = [   # z desde la caja: el botón cuelga del techo
        ([(180, -6, 50), (178, -10, 30), (174, -16, 10), (172, -18, 5)], "azul"),
        ([(180, 6, 50), (178, 4, 30), (174, 1, 10), (172, 1, 5)], "azul"),
        ([(108, 22, 6), (112, 26, 0), (160, 27, 0), (168, 21, 5)], "rojo"),
        ([(108, 2, 6), (104, 2, 0), (104, -26, 0), (168, -21, 5)], "negro"),
        ([(126, -6, -6), (126, -10, 2), (160, -5, 4), (175, -1, 5)], "rojo"),
        ([(130, 19, -6), (126, -18, 1), (162, -26, 4), (172, 20, 5)], "negro"),
    ]

    def costado(self):
        vent = [redondo(box(a, Z_VENT[0], b, Z_VENT[1]), 2.5) for a, b in VENTANILLAS]
        grab = [box(10, 14, 30, Z_VENT[0] - 3).exterior,                             # puerta
                LineString([(3, 40), (197, 40)]),                                    # franja
                LineString([(3, 44), (197, 44)]),
                box(188, 30, 195, 37).exterior]                                      # luz de giro
        return E.costado(silueta(),
                         [(Z_PISO, E.TABS_PISO), (E.Z_CAJA, E.TABS_CAJA)],
                         [(X_FRENTE, TABS_FRENTE_Z), (X_ASIENTOS[0], TABS_ASIENTOS_Z),
                          (X_ASIENTOS[1], TABS_ASIENTOS_Z), (X_PORTON, TABS_FONDO_Z)],
                         vent, grab)

    def piezas(self):
        P = kit.Pieza
        T = E.T
        out = E.costados(*self.costado())
        out.append(E.piso((X_FRENTE,) + X_ASIENTOS + (X_PORTON,)))
        out.append(E.caja(boton=False))

        # techo: se apoya arriba y se saca con la mano (las ranuras van flojas)
        ancho = YI + T + VUELO
        techo = redondo(box(1, -ancho, 199, ancho), 5)
        hue = [box(a - FLOJO, y0 - FLOJO, b + FLOJO, y0 + T + FLOJO)
               for a, b in TABS_TECHO for y0 in (-YI - T, YI)]
        hue.append(Point(*BOTON_TECHO).buffer(6.25, 32))
        techo = techo.difference(unary_union(hue))
        grab = [redondo(box(60, -12, 84, 12), 3).exterior, redondo(box(120, -12, 144, 12), 3).exterior,
                Point(*BOTON_TECHO).buffer(10, 32).exterior]
        pz = P(techo, "TECHO", "xy", Z_ALTO, grab, etiqueta="", tipo="carroceria")
        pz.textos = [("TIMBRE", 180, -15, 4), ("TECHO", 30, 0, 5)]
        out.append(pz)

        # frente: parabrisas calado, cartel de la línea, faros y paragolpes grabados
        fr = pared(Z_ALTO, TABS_FRENTE_Z)
        fr = fr.difference(redondo(box(-24, 44, 24, 68), 3))
        grab = [box(-22, 70.5, 22, 77.5).exterior, LineString([(-YI + 1, 14), (YI - 1, 14)]),
                box(-12, 20, 12, 30).exterior]
        grab += [Point(y, 25).buffer(4.5, 24).exterior for y in (-21, 21)]
        pz = P(fr, "FRENTE", "yz", X_FRENTE, grab, etiqueta="", tipo="carroceria")
        pz.textos = [("LÍNEA 10", 0, 72, 5)]
        out.append(pz)

        # 2 filas de asientos (cada una con 2 asientos de cada lado y el pasillo)
        base = box(-YI, Z_PISO + T, YI, 30)
        resp = [redondo(box(a, 22, b, 46), 3) for a, b in ((-28, -16), (-14, -3), (3, 14), (16, 28))]
        asientos = pared(30, TABS_ASIENTOS_Z, unir(base, *resp))
        for x in X_ASIENTOS:
            out.append(P(asientos, "ASIENTOS", "yz", x, etiqueta="", tipo="carroceria"))

        # fondo con la luneta y las luces
        fo = pared(Z_ALTO, TABS_FONDO_Z)
        fo = fo.difference(redondo(box(-20, 52, 20, 70), 3))
        grab = [box(-26, 22, -19, 34).exterior, box(19, 22, 26, 34).exterior, box(-12, 24, 12, 32).exterior,
                LineString([(-YI + 1, 14), (YI - 1, 14)])]
        pz = P(fo, "FONDO", "yz", X_PORTON, grab, etiqueta="", tipo="carroceria")
        out.append(pz)

        out += E.soportes()
        out += E.ruedas()
        return out

    def instructivo(self, salida, datos):
        img = os.path.join(salida, "pasos")
        os.makedirs(img, exist_ok=True)
        f = lambda e, n, w=900, h=520, fondo="#ffffff": E.foto(e, os.path.join(img, n), w, h, fondo)
        esc = self.escena
        paredes = ("frente", "asientos", "fondo")
        sin_techo = ("piso", "soportes", "costado_izq", "costado_der", "caja", "polea",
                     "ruedas_del", "ruedas_tras") + paredes
        todo = sin_techo + ("techo",)
        tapa = f(esc(todo, elec=("boton",), con_ejes=EJES, con_cubiertas=EJES, cam=(-128, 22)),
                 "00-colectivo", 1100, 600, "#f6f1ea")
        atras = f(esc(sin_techo, elec=("pilas", "bornes", "goma", "motor"), con_ejes=EJES,
                      con_cubiertas=EJES, cam=(-35, 50)), "00b-caja", 900, 520, "#f6f1ea")
        base = ("piso", "soportes", "costado_izq") + paredes
        arriba = base + ("polea", "caja")
        con = lambda p, imagen: (p[0], imagen, p[1])
        pasos = [
            con(E.P_RUEDAS, E.foto_ruedas(os.path.join(img, "01-ruedas"))),
            con(E.P_SOPORTES, f(esc(("piso",), nuevos=("soportes",), levantar=10), "02-paso")),
            con(E.P_COSTADO, f(esc(("piso", "soportes"), nuevos=("costado_izq",)), "03-paso")),
            ("Frente, asientos y fondo",
             f(esc(("piso", "soportes", "costado_izq"), nuevos=paredes, levantar=10), "04-paso"),
             """<p>Encastrá el <b>FRENTE</b> (el del parabrisas) adelante, las 2 filas de <b>ASIENTOS</b> en el medio
y el <b>FONDO</b> atrás. Cada uno entra en el piso y en el costado.</p>"""),
            con(E.P_MOTOR, f(esc(base, nuevos=("polea",), elec_nueva=("motor", "goma"), con_ejes=EJES,
                                 transparente=True), "05-paso")),
            ("Caja de las pilas",
             f(esc(base + ("polea",), nuevos=("caja",), elec=("motor", "goma"), con_ejes=EJES,
                   levantar=12, transparente=True), "06-paso"),
             """<p>Encastrá el piso de la <b>CAJA</b> arriba del motor, entre los asientos de atrás y el fondo. Deja
el motor apretado en su lugar.</p>"""),
            con(E.P_CERRAR, f(esc(arriba, nuevos=("costado_der",), elec=("motor", "goma"), con_ejes=EJES,
                                  cam=(-55, 30)), "07-paso")),
            con(E.P_MONTAR, f(esc(arriba + ("costado_der",), nuevos=("ruedas_del", "ruedas_tras"),
                                  elec=("motor", "goma"), con_ejes=EJES, con_cubiertas=EJES), "08-paso")),
            ("Pilas, bornes y cables (sin soldar)",
             f(esc(sin_techo, elec=("motor", "goma"), elec_nueva=("pilas", "bornes"),
                   con_ejes=EJES, con_cubiertas=EJES, cam=(-35, 55)), "09-paso"),
             f"""<p>En la caja está todo dibujado. Pegá el <b>portapilas</b> con doble faz donde dice PILAS y poné los
<b>bornes</b> en B1, B2 y B3. Para conectar: levantá la palanquita, meté el cable pelado y bajala. Los cables del
motor suben por la ventanita.</p>
<img src="pasos/09b-circuito.png">
{E.TABLA_BORNES}"""),
            ("Techo y timbre",
             f(esc(sin_techo, nuevos=("techo",), elec=("motor", "goma", "pilas", "bornes"),
                   elec_nueva=("boton", "cables"), con_ejes=EJES, con_cubiertas=EJES, levantar=25,
                   cam=(-40, 40)), "10-paso"),
             """<p>Atornillá el <b>botón</b> en el agujero del <b>TECHO</b> (donde dice TIMBRE) y conectá sus 2 cables en
B1 y B2. Apoyá el techo arriba: las pestañitas de los costados entran en sus ranuras. <b>No hace falta
apretar</b>: el techo se saca con la mano cada vez que hay que cambiar las pilas.</p>"""),
            con(E.P_PRUEBA, None),
        ]
        E.circuito(img)
        madera = """<li>2 costados, piso, piso de la caja, techo, frente y fondo.</li>
<li>2 filas de asientos y 2 soportes del motor.</li>
<li>4 ruedas (3 discos cada una), 4 arandelas y la polea (3 discos).</li>"""
        E.html_instructivo(salida, self.titulo,
                           f"Juguete de madera con motor eléctrico · <b>se arma sin cola</b> · {datos['piezas']} piezas",
                           tapa, E.como_funciona(atras, "el colectivo"), madera, pasos, E.pie(datos))


if __name__ == "__main__":
    E.configurar(sys.argv)
    Colectivo().generar(AQUI)
