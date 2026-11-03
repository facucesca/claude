"""Jeep para chicos: todoterreno abierto, todo encastrado a presión, SIN COLA.

Inspirado en el Jeep clásico (Willys / IKA): costados bajos con el recorte de la puerta,
parrilla de 7 ranuras, parabrisas, asiento y arco antivuelco.
Comparte con la camioneta el piso, la caja (pilas, bornes y botón a la vista), el motor,
las ruedas y la electrónica (ver ../encastre.py).

Uso:  python3 jeep.py [espesor] [ajuste]
"""
import math
import os
import sys

from shapely.geometry import LineString, Point, Polygon, box

AQUI = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(AQUI, ".."))
import encastre as E  # noqa: E402
from encastre import (EJES, X_CABINA, X_FRENTE, X_PORTON, YI, Z_PISO, con_pestanas_x,  # noqa: E402
                      pared, redondo, unir)

kit = E.kit

# --- medidas propias (mm) ----------------------------------------------------------
Z_BORDE = 46.0                   # borde de arriba de los costados
Z_CAPO = 40.0                    # capó: z 40 a 43 (queda 3 mm hundido)
X_PARABRISAS = 56.0
X_ASIENTO = 84.0
PUERTA = (62.0, 96.0, 31.0)      # recorte de la puerta: x desde, x hasta, z de abajo
Z_PARABRISAS, Z_ARCO = 76.0, 74.0
TABS_CAPO = [(16, 28), (38, 50)]
TABS_FRENTE_Z = [(16, 30)]
TABS_PARABRISAS_Z = [(16, 26), (32, 40)]
TABS_ASIENTO_Z = [(14, 24)]
TABS_ARCO_Z = [(15, 25), (34, 42)]
TABS_PORTON_Z = [(15, 25), (32, 42)]


def silueta():
    p = Polygon([(0, 7), (0, Z_BORDE - 2), (2, Z_BORDE), (198, Z_BORDE), (200, Z_BORDE - 2),
                 (200, 7), (197, 5), (3, 5)])
    x0, x1, zb = PUERTA
    r = (x1 - x0) / 2
    # recorte redondeado de la puerta (como el Jeep: abierto, sin puertas)
    arco = [(x0 + r + r * math.cos(math.radians(a)), Z_BORDE + (Z_BORDE - zb) * math.sin(math.radians(a)))
            for a in range(180, 361, 6)]
    recorte = Polygon([(x0, Z_BORDE + 5)] + arco + [(x1, Z_BORDE + 5)])
    p = p.difference(recorte)
    return E.suavizar(redondo(p, 2.5), 2.5)


class Jeep(E.Modelo):
    nombre = "jeep"
    titulo = "Jeep todoterreno"

    def costado(self):
        grab = [LineString([(4, 41), (58, 41)]),                                  # borde del capó
                box(28, 30, 50, 32.5).exterior,                                     # rejilla del capó
                LineString([(104, 41), (196, 41)]),                                 # borde de la caja
                Point(186, 30).buffer(3.5, 24).exterior]                            # tapa del tanque
        return E.costado(silueta(),
                         [(Z_PISO, E.TABS_PISO), (E.Z_CAJA, E.TABS_CAJA), (Z_CAPO, TABS_CAPO)],
                         [(X_FRENTE, TABS_FRENTE_Z), (X_PARABRISAS, TABS_PARABRISAS_Z),
                          (X_ASIENTO, TABS_ASIENTO_Z), (X_CABINA, TABS_ARCO_Z), (X_PORTON, TABS_PORTON_Z)],
                         grab=grab)

    def piezas(self):
        P = kit.Pieza
        T = E.T
        out = E.costados(*self.costado())
        out.append(E.piso((X_FRENTE, X_PARABRISAS, X_ASIENTO, X_CABINA, X_PORTON)))
        out.append(E.caja())

        # capó
        capo = con_pestanas_x(box(X_FRENTE + T, -YI, X_PARABRISAS, YI), TABS_CAPO)
        grab = [LineString([(12, y), (50, y)]) for y in (-10, 10)]
        out.append(P(capo, "CAPÓ", "xy", Z_CAPO, grab, etiqueta="CAPÓ", tipo="carroceria"))

        # frente: la parrilla de 7 ranuras y los faros redondos, caladas
        fr = pared(Z_CAPO, TABS_FRENTE_Z)
        for i in range(7):
            y = (i - 3) * 4.6
            fr = fr.difference(redondo(box(y - 1.3, 17, y + 1.3, 35), 1.2))
        for y in (-22, 22):
            fr = fr.difference(Point(y, 30).buffer(4.2, 24))
        grab = [Point(y, 30).buffer(6, 32).exterior for y in (-22, 22)]
        grab.append(LineString([(-YI + 1, 14), (YI - 1, 14)]))                   # paragolpes
        out.append(P(fr, "FRENTE", "yz", X_FRENTE, grab, etiqueta="", tipo="carroceria"))

        # parabrisas: abajo va entre los costados, arriba es un marco del ancho del jeep
        marco = redondo(box(-YI - T, Z_BORDE, YI + T, Z_PARABRISAS), 2.5)
        marco = marco.difference(redondo(box(-YI + 3, Z_BORDE + 3, YI - 3, Z_PARABRISAS - 4), 2))
        pb = unir(pared(Z_BORDE, TABS_PARABRISAS_Z), marco)
        out.append(P(pb, "PARABRISAS", "yz", X_PARABRISAS, [LineString([(-YI, 44), (YI, 44)])],
                     etiqueta="", tipo="carroceria"))

        # asiento: banco con 2 respaldos
        base = box(-YI, Z_PISO + T, YI, 28)
        resp = [redondo(box(a, 20, b, 44), 4) for a, b in ((-26, -3), (3, 26))]
        asiento = pared(28, TABS_ASIENTO_Z, unir(base, *resp))
        grab = [redondo(box(a + 3, 31, b - 3, 41), 2).exterior for a, b in ((-26, -3), (3, 26))]
        out.append(P(asiento, "ASIENTO", "yz", X_ASIENTO, grab, etiqueta="", tipo="carroceria"))

        # arco antivuelco: abajo cierra la caja, arriba es una U dada vuelta
        u = redondo(box(-YI, Z_BORDE - 2, YI, Z_ARCO), 5)
        u = u.difference(redondo(box(-YI + 5, Z_BORDE - 3, YI - 5, Z_ARCO - 5), 3))
        arco = pared(Z_BORDE, TABS_ARCO_Z, unir(box(-YI, Z_PISO + T, YI, Z_BORDE), u))
        out.append(P(arco, "ARCO", "yz", X_CABINA, etiqueta="ARCO", tipo="carroceria"))

        # portón trasero con la rueda de auxilio grabada
        po = pared(Z_BORDE, TABS_PORTON_Z)
        grab = [Point(0, 29).buffer(r, 48).exterior for r in (14, 9)]
        grab += [box(-27, 34, -22, 42).exterior, box(22, 34, 27, 42).exterior]
        out.append(P(po, "PORTÓN", "yz", X_PORTON, grab, etiqueta="", tipo="carroceria"))

        out += E.soportes()
        out += E.ruedas()
        return out

    def instructivo(self, salida, datos):
        img = os.path.join(salida, "pasos")
        os.makedirs(img, exist_ok=True)
        f = lambda e, n, w=900, h=520, fondo="#ffffff": E.foto(e, os.path.join(img, n), w, h, fondo)
        esc = self.escena
        paredes = ("frente", "parabrisas", "asiento", "arco", "portón")
        todo = ("piso", "soportes", "costado_izq", "costado_der", "caja", "capó", "polea",
                "ruedas_del", "ruedas_tras") + paredes
        tapa = f(esc(todo, elec=("pilas", "bornes", "boton", "goma"), con_ejes=EJES, con_cubiertas=EJES,
                     cam=(-128, 26)), "00-jeep", 1100, 600, "#f6f1ea")
        atras = f(esc(todo, elec=("pilas", "bornes", "boton", "goma", "motor"), con_ejes=EJES,
                      con_cubiertas=EJES, cam=(-35, 40)), "00b-caja", 900, 520, "#f6f1ea")
        base = ("piso", "soportes", "costado_izq") + paredes
        arriba = base + ("polea", "caja", "capó")
        con = lambda p, imagen: (p[0], imagen, p[1])
        pasos = [
            con(E.P_RUEDAS, E.foto_ruedas(os.path.join(img, "01-ruedas"))),
            con(E.P_SOPORTES, f(esc(("piso",), nuevos=("soportes",), levantar=10), "02-paso")),
            con(E.P_COSTADO, f(esc(("piso", "soportes"), nuevos=("costado_izq",)), "03-paso")),
            ("Frente, parabrisas, asiento, arco y portón",
             f(esc(("piso", "soportes", "costado_izq"), nuevos=paredes, levantar=10), "04-paso"),
             """<p>Encastrá de adelante para atrás: el <b>FRENTE</b> (la parrilla con ranuras), el <b>PARABRISAS</b>,
el <b>ASIENTO</b>, el <b>ARCO</b> y el <b>PORTÓN</b> (el de la rueda de auxilio dibujada). Cada uno entra en el
piso y en el costado.</p>"""),
            con(E.P_MOTOR, f(esc(base, nuevos=("polea",), elec_nueva=("motor", "goma"), con_ejes=EJES,
                                 transparente=True), "05-paso")),
            ("Caja y capó",
             f(esc(base + ("polea",), nuevos=("caja", "capó"), elec=("motor", "goma"), con_ejes=EJES,
                   levantar=12, transparente=True), "06-paso"),
             """<p>Encastrá el piso de la <b>CAJA</b> arriba del motor (lo deja apretado en su lugar) y el
<b>CAPÓ</b> adelante, entre el frente y el parabrisas.</p>"""),
            con(E.P_CERRAR, f(esc(arriba, nuevos=("costado_der",), elec=("motor", "goma"), con_ejes=EJES,
                                  cam=(-55, 30)), "07-paso")),
            con(E.P_MONTAR, f(esc(arriba + ("costado_der",), nuevos=("ruedas_del", "ruedas_tras"),
                                  elec=("motor", "goma"), con_ejes=EJES, con_cubiertas=EJES), "08-paso")),
            ("Pilas, botón y cables (sin soldar)",
             f(esc(todo, elec=("motor", "goma"), elec_nueva=("pilas", "bornes", "boton", "cables"),
                   con_ejes=EJES, con_cubiertas=EJES, cam=(-35, 48)), "09-paso"),
             f"""<p>Atrás del arco está todo dibujado. Pegá el <b>portapilas</b> con doble faz donde dice PILAS. Atornillá
el <b>botón</b> en el agujero redondo. Poné los <b>bornes</b> en B1, B2 y B3. Para conectar: levantá la palanquita,
meté el cable pelado y bajala. Los cables del motor suben por la ventanita y los del botón, por el agujerito.</p>
<img src="pasos/09b-circuito.png">
{E.TABLA_BORNES}"""),
            con(E.P_PRUEBA, None),
        ]
        E.circuito(img)
        madera = """<li>2 costados, piso, piso de la caja, capó, frente, parabrisas, asiento, arco y portón.</li>
<li>2 soportes del motor.</li>
<li>4 ruedas (3 discos cada una), 4 arandelas y la polea (3 discos).</li>"""
        E.html_instructivo(salida, self.titulo,
                           f"Juguete de madera con motor eléctrico · <b>se arma sin cola</b> · {datos['piezas']} piezas",
                           tapa, E.como_funciona(atras, "el jeep"), madera, pasos, E.pie(datos))


if __name__ == "__main__":
    E.configurar(sys.argv)
    Jeep().generar(AQUI)
