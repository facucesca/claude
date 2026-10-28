"""Camioneta clásica para chicos (v5): pocas piezas, todo encastrado a presión, SIN COLA.

Inspirada en las camionetas clásicas (tipo F-100) y en kits que encastran sin cola
(FBRKN Laser Cut Car, camión solar de madera, Ugears).

Construcción: 2 costados con la silueta + piezas que los unen con pestañas y ranuras.
La caja de carga queda abierta: ahí van las pilas, los bornes y el botón, a la vista.
Por una ventanita en la caja se ven la goma y la polea girando.
La base común (piso, caja, motor, ruedas, electrónica) está en ../encastre.py.

Uso:  python3 camioneta.py [espesor] [ajuste]
      espesor = espesor real de la placa (3 por defecto)
      ajuste  = cuánto más angostas que el espesor se cortan las ranuras para que
                encastren firme (0.1 por defecto; si quedan flojas, subirlo)
"""
import os
import sys

from shapely.geometry import LineString, Point, Polygon, box
from shapely.ops import unary_union

AQUI = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(AQUI, ".."))
import encastre as E  # noqa: E402
from encastre import (EJES, X_CABINA, X_FRENTE, X_PORTON, YI, Z_PISO, con_pestanas_x,  # noqa: E402
                      con_pestanas_y, pared, ranura, redondo, unir)

kit = E.kit

# --- medidas propias (mm) ----------------------------------------------------------
Z_CAPO = 35.0
Z_TECHO = 58.0
TABS_CAPO = [(14, 26), (36, 48)]
TABS_TECHO = [(74, 96)]
TABS_FRENTE_Z = [(16, 30)]
TABS_CABINA_Z = [(15, 25), (36, 52)]
TABS_PORTON_Z = [(15, 25), (32, 42)]


def silueta():
    p = Polygon([(0, 7), (0, 39), (2, 41.5), (53, 41.5), (64, 64), (106, 64), (106, 47),
                 (200, 47), (200, 7), (197, 5), (3, 5)])
    return E.suavizar(redondo(p, 2.5))


class Camioneta(E.Modelo):
    nombre = "camioneta"
    titulo = "Camioneta clásica"

    def costado(self):
        ventana = Polygon([(69, 45), (97, 45), (97, 55.5), (74.1, 55.5)])
        grab = [LineString([(57, 41.5), (57, 15), (100, 15), (100, 41.5)]),       # puerta
                box(88, 37, 95, 39.2).exterior,                                       # manija
                LineString([(108, 43), (196, 43)])]                                  # borde de la caja
        return E.costado(silueta(),
                         [(Z_PISO, E.TABS_PISO), (E.Z_CAJA, E.TABS_CAJA), (Z_CAPO, TABS_CAPO),
                          (Z_TECHO, TABS_TECHO)],
                         [(X_FRENTE, TABS_FRENTE_Z), (X_CABINA, TABS_CABINA_Z), (X_PORTON, TABS_PORTON_Z)],
                         [redondo(ventana, 1.5)], grab)

    def piezas(self):
        P = kit.Pieza
        T = E.T
        out = E.costados(*self.costado())
        out.append(E.piso((X_FRENTE, X_CABINA, X_PORTON)))
        out.append(E.caja())

        # capó y techo
        capo = con_pestanas_x(box(X_FRENTE + T, -YI, 53, YI), TABS_CAPO)
        out.append(P(capo, "CAPÓ", "xy", Z_CAPO, [LineString([(12, 0), (50, 0)])], etiqueta="CAPÓ",
                     tipo="carroceria"))
        techo = con_pestanas_x(box(66, -YI, 105.5, YI), TABS_TECHO)
        techo = techo.difference(unary_union([ranura(X_CABINA, a, X_CABINA + T, b)
                                              for a, b in E.TABS_ABAJO_Y]))
        out.append(P(redondo(techo, 0.8), "TECHO", "xy", Z_TECHO, etiqueta="TECHO", tipo="carroceria"))

        # frente (parrilla y faros)
        fr = pared(Z_CAPO, TABS_FRENTE_Z)
        for y in (-21, 21):
            fr = fr.difference(Point(y, 25).buffer(2.6, 16))
        grab = [Point(y, 25).buffer(6, 32).exterior for y in (-21, 21)]
        grab += [box(-13, 16, 13, 31).exterior] + [LineString([(-11, z), (11, z)]) for z in (19.5, 23.5, 27.5)]
        grab.append(LineString([(-YI + 1, 14), (YI - 1, 14)]))
        out.append(P(fr, "FRENTE", "yz", X_FRENTE, grab, etiqueta="", tipo="carroceria"))

        # pared de atrás de la cabina (con pestañas arriba para el techo)
        cab = pared(Z_TECHO, TABS_CABINA_Z)
        for a, b in E.TABS_ABAJO_Y:
            cab = unir(cab, box(a, Z_TECHO, b, Z_TECHO + T))
        out.append(P(cab, "CABINA", "yz", X_CABINA, [redondo(box(-18, 44, 18, 54), 3).exterior],
                     etiqueta="CABINA", tipo="carroceria"))

        # portón trasero
        po = pared(45, TABS_PORTON_Z)
        grab = [box(-27, 33, -22, 41).exterior, box(22, 33, 27, 41).exterior,
                redondo(box(-15, 17, 15, 38), 2).exterior]
        out.append(P(po, "PORTÓN", "yz", X_PORTON, grab, etiqueta="", tipo="carroceria"))

        out += E.soportes()
        out += E.ruedas()
        return out

    def instructivo(self, salida, datos):
        img = os.path.join(salida, "pasos")
        os.makedirs(img, exist_ok=True)
        f = lambda e, n, w=900, h=520, fondo="#ffffff": E.foto(e, os.path.join(img, n), w, h, fondo)
        esc = self.escena
        todo = ["piso", "soportes", "costado_izq", "costado_der", "frente", "cabina", "portón", "caja",
                "capó", "techo", "polea", "ruedas_del", "ruedas_tras"]
        tapa = f(esc(todo, elec=("pilas", "bornes", "boton", "goma"), con_ejes=EJES, con_cubiertas=EJES,
                     cam=(-128, 26)), "00-camioneta", 1100, 600, "#f6f1ea")
        atras = f(esc(todo, elec=("pilas", "bornes", "boton", "goma", "motor"), con_ejes=EJES,
                      con_cubiertas=EJES, cam=(-35, 40)), "00b-caja", 900, 520, "#f6f1ea")
        base = ("piso", "soportes", "costado_izq", "frente", "cabina", "portón")
        arriba = base + ("polea", "caja", "capó", "techo")
        con = lambda p, imagen: (p[0], imagen, p[1])
        pasos = [
            con(E.P_RUEDAS, E.foto_ruedas(os.path.join(img, "01-ruedas"))),
            con(E.P_SOPORTES, f(esc(("piso",), nuevos=("soportes",), levantar=10), "02-paso")),
            con(E.P_COSTADO, f(esc(("piso", "soportes"), nuevos=("costado_izq",)), "03-paso")),
            ("Frente, cabina y portón",
             f(esc(("piso", "soportes", "costado_izq"), nuevos=("frente", "cabina", "portón"), levantar=10),
               "04-paso"),
             """<p>Encastrá el <b>FRENTE</b> (con los faros) adelante, la pared de la <b>CABINA</b> en el medio y el
<b>PORTÓN</b> atrás. Cada uno entra en el piso y en el costado.</p>"""),
            con(E.P_MOTOR, f(esc(base, nuevos=("polea",), elec_nueva=("motor", "goma"), con_ejes=EJES,
                                 transparente=True), "05-paso")),
            ("Caja, capó y techo",
             f(esc(base + ("polea",), nuevos=("caja", "capó", "techo"), elec=("motor", "goma"), con_ejes=EJES,
                   levantar=12, transparente=True), "06-paso"),
             """<p>Encastrá el piso de la <b>CAJA</b> arriba del motor (lo deja apretado en su lugar), el <b>CAPÓ</b> y el
<b>TECHO</b>.</p>"""),
            con(E.P_CERRAR, f(esc(arriba, nuevos=("costado_der",), elec=("motor", "goma"), con_ejes=EJES,
                                  cam=(-55, 30)), "07-paso")),
            con(E.P_MONTAR, f(esc(arriba + ("costado_der",), nuevos=("ruedas_del", "ruedas_tras"),
                                  elec=("motor", "goma"), con_ejes=EJES, con_cubiertas=EJES), "08-paso")),
            ("Pilas, botón y cables (sin soldar)",
             f(esc(todo, elec=("motor", "goma"), elec_nueva=("pilas", "bornes", "boton", "cables"),
                   con_ejes=EJES, con_cubiertas=EJES, cam=(-35, 48)), "09-paso"),
             f"""<p>En la caja está todo dibujado. Pegá el <b>portapilas</b> con doble faz donde dice PILAS. Atornillá el
<b>botón</b> en el agujero redondo. Poné los <b>bornes</b> en B1, B2 y B3. Para conectar: levantá la palanquita,
meté el cable pelado y bajala. Los cables del motor suben por la ventanita y los del botón, por el agujerito.</p>
<img src="pasos/09b-circuito.png">
{E.TABLA_BORNES}"""),
            con(E.P_PRUEBA, None),
        ]
        E.circuito(img)
        madera = """<li>2 costados, piso, piso de la caja, capó, techo, frente, pared de la cabina y portón.</li>
<li>2 soportes del motor.</li>
<li>4 ruedas (3 discos cada una), 4 arandelas y la polea (3 discos).</li>"""
        E.html_instructivo(salida, self.titulo,
                           f"Juguete de madera con motor eléctrico · <b>se arma sin cola</b> · {datos['piezas']} piezas",
                           tapa, E.como_funciona(atras, "la camioneta"), madera, pasos, E.pie(datos))


if __name__ == "__main__":
    E.configurar(sys.argv)
    Camioneta().generar(AQUI)
