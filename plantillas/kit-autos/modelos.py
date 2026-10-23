"""Las 3 carrocerías del kit. Todas se apoyan en el mismo chasis.

Cada modelo define el perfil de cada capa (vista de costado). El motor (kit.py) le
saca el hueco del chasis, los huecos de las ruedas, el canal del botón y los pernos.
"""
from shapely.geometry import LineString, Polygon, box
from shapely.ops import unary_union

import kit
from kit import (Pieza, abajo, arriba, desde_afuera, silueta, suave, y_centro)


class Superauto:
    """Superauto en cuña, estilo deportivo italiano (diseño propio, sin marcas)."""
    clave = "superauto"
    titulo = "Superauto"
    subtitulo = "Deportivo en cuña, estilo superauto italiano"
    pernos = [(14, 12), (110, 16), (180, 25), (100, 38), (150, 33)]

    COLA = [(200, 36), (200.4, 30), (199.5, 18), (197.5, 9), (193, 5)]
    NARIZ = [(10, 5), (4, 6.6), (1, 9.2), (0, 13)]
    CABINA = silueta([(0, 13), (10, 20.5), (30, 28), (46, 31.5), (63, 34.5), (78, 40),
                      (93, 45.3), (104, 47), (117, 46.4), (140, 41.6), (165, 37.6),
                      (186, 35.6), (196, 36.6), (200, 36)], COLA, NARIZ)
    CUERPO = silueta([(0, 13), (8, 21), (24, 30.8), (46, 37.4), (63, 35.2), (82, 33.8),
                      (104, 34), (128, 36), (150, 39.8), (163, 40.2), (181, 38.4),
                      (196, 37.3), (200, 36)], COLA, NARIZ)

    def perfil(self, k):
        o = desde_afuera(k)
        grab = []
        if not kit.con_cavidad(k):                         # capas de afuera: guardabarros
            p = self.CUERPO.buffer(-1.0, 32) if o == 0 else self.CUERPO
            if o <= 1:                                      # toma de aire
                p = p.difference(Polygon([(102, 11), (132, 11), (135.5, 28), (121, 29)]))
            if 1 <= o <= 4:                                 # faro
                p = p.difference(box(-1, 16.5, 13, 19.5))
            if o == 0:                                      # puerta
                grab.append(LineString([(63.5, 31.5), (66, 9), (99, 9)]))
        else:
            c = o - 5                                       # 0 = capa de cabina de afuera
            if c in (0, 1):
                p = self.CABINA.buffer(-2.5 if c == 0 else -1.2, 32).union(abajo(self.CABINA, 28))
            else:
                p = self.CABINA
            if c == 0:                                      # vidrio grabado
                v = arriba(p, 34.8).intersection(box(64, 0, 150, 100)).buffer(-1.6, 16)
                grab.append(v)
            if k % 2 == 0 and c >= 2:                       # aletas de trompa y difusor
                p = p.difference(box(194.5, 4, 201, 10)).difference(box(-1, 4, 9, 8.5))
        if 1 <= o <= 6:                                     # luz trasera
            p = p.difference(box(193, 27.5, 201, 30))
        return p, grab


class Clasico:
    """Coupé clásico argentino de los 70 (inspirado en los fastback de la época)."""
    clave = "clasico"
    titulo = "Clásico"
    subtitulo = "Coupé fastback de los años 70"
    pernos = [(12, 12), (110, 16), (180, 25), (100, 46), (150, 36), (40, 30)]

    COLA = [(200, 37.5), (200.4, 30), (200.2, 16), (198.8, 9), (194.5, 5.5)]
    NARIZ = [(8, 5), (2.5, 6.5), (0.4, 10), (0, 15), (0, 30)]
    CUERPO = silueta([(0, 30), (4, 35.2), (18, 37.4), (46, 38.3), (80, 38.5), (120, 38.9),
                      (156, 39.7), (184, 39.5), (196, 38.9), (200, 37.5)], COLA, NARIZ)
    CABINA = silueta([(0, 30), (4, 35), (18, 36.8), (46, 37.5), (62, 38), (67, 38.8),
                      (84, 51.5), (96, 55.4), (110, 56.3), (124, 55.7), (140, 51),
                      (158, 43.6), (172, 40.5), (186, 39.7), (196, 38.9), (200, 37.5)],
                     COLA, NARIZ)

    def perfil(self, k):
        o = desde_afuera(k)
        grab = []
        if not kit.con_cavidad(k):
            p = self.CUERPO.buffer(-1.0, 32) if o == 0 else self.CUERPO
            if 1 <= o <= 4:                                 # luces traseras
                p = p.difference(box(197, 27, 201, 33))
            if o == 0:
                grab.append(LineString([(6, 31.5), (194, 32.5)]))          # moldura
                grab.append(LineString([(70, 9), (70, 36.5)]))              # puerta
                grab.append(LineString([(70, 9), (124, 9), (124, 36.8)]))
                grab.append(box(112, 30, 120, 31.6).exterior)               # manija
        else:
            c = o - 5
            if c in (0, 1):
                p = self.CABINA.buffer(-2.5 if c == 0 else -1.2, 32).union(abajo(self.CABINA, 38))
            else:
                p = self.CABINA
            if c == 0:                                      # ventanillas grabadas
                v = arriba(p, 40.6).intersection(box(70, 0, 156, 100)).buffer(-1.8, 16)
                v = v.difference(box(108.5, 0, 111.5, 100))
                grab.append(v)
            if c in (0, 1):                                 # faros
                p = p.difference(box(-1, 18, 4, 25))
            elif k % 2 == 1:                                # parrilla de barras
                p = p.difference(box(-1, 16, 3, 27))
        return p, grab


class Formula:
    """Auto de carrera con ruedas a la vista. El más fácil y el que menos madera usa."""
    clave = "formula"
    titulo = "Fórmula"
    subtitulo = "Auto de carrera con ruedas a la vista"
    pernos = [(44, 25.3), (192, 30.2), (100, 29.8)]
    NUMERO = "24"

    COLA = [(200, 33), (200.3, 24), (199, 12), (196, 6), (193, 5)]
    PISO = [(20, 33)]  # no se usa

    def __init__(self):
        cola = self.COLA
        # cubierta baja que tapa el chasis (pontones)
        self.cubierta = silueta([(62, 26), (63, 29), (67, 32.6), (100, 33), (140, 33),
                                 (147, 34), (168, 34), (175, 34.6), (196, 34.2), (200, 33)],
                                cola, [(62, 5), (62, 26)])
        # trompa angosta (capas del centro)
        trompa_arriba = suave([(1, 9.5), (6, 12), (20, 17), (34, 22.5), (48, 27.5), (66, 31)])
        trompa_abajo = suave([(66, 10), (40, 9), (20, 8), (4, 7.2), (1, 9.5)])
        self.trompa = Polygon(trompa_arriba + trompa_abajo).buffer(0).union(box(18, 5, 66, 12))
        self.frente = silueta([(18, 9), (22, 20), (28, 27.5), (46, 28.6), (62, 29.6), (66, 31.5),
                               (100, 31.5)], [(100, 31.5), (100, 5)], [(22, 5), (19, 6), (18, 9)])
        # cockpit, casco y toma de aire
        self.cockpit = silueta([(70, 31), (76, 34.5), (100, 35.5), (112, 35), (120, 37),
                                (150, 36), (172, 35.2)], [(172, 35.2), (172, 20)],
                               [(70, 20), (70, 31)])
        self.toma = silueta([(108, 36), (113, 41.5), (122, 44), (134, 43), (156, 38.5),
                             (172, 35.6)], [(172, 35.6), (172, 25)], [(108, 25), (108, 36)])
        self.casco = Polygon(suave([(92, 34), (94, 39.5), (100, 42.5), (106, 41.5), (109, 37),
                                    (108, 33)])).buffer(0)
        self.pilar = box(186, 30, 196, 38).union(box(188, 38, 196, 38 + kit.T))

    def perfil(self, k):
        o = desde_afuera(k)
        yc = y_centro(k)
        grab = []
        if not kit.con_cavidad(k):
            if o == 4:                                      # costado del pontón
                p = silueta([(64, 25), (66, 29), (100, 30.2), (136, 30.2), (138, 28)],
                            [(138, 28), (138, 6)], [(66, 5), (64, 7), (64, 25)])
                return p, grab
            return None, grab
        p = self.cubierta
        if yc >= 9:  # pontones: terminan antes del eje trasero (se ve la polea)
            p = p.intersection(box(-1, -1, 148, 100)).buffer(-1.5, 8).buffer(1.5, 8)
        if yc < 9:
            p = p.union(self.frente).union(self.trompa if yc < 7.5 else self.frente)
            p = p.difference(box(0, 4, 21.5, 5 + kit.T))       # hueco del alerón delantero
        if yc < 10.5:
            p = p.union(self.cockpit)
        if yc < 7.5:
            p = p.union(self.toma)
        if yc < 3:
            p = p.union(self.casco).union(self.pilar)
        if o == 5:                                          # borde redondeado
            p = p.buffer(-1.0, 16).union(abajo(p, 29))
        return p, grab

    def extras(self):
        T = kit.T
        out = []
        # alerón trasero: plancha horizontal con pestañas a las derivas
        ala = box(184, -39, 199, 39).union(box(186, -42, 198, -39)).union(box(186, 39, 198, 42))
        ala = ala.difference(box(188, -kit.ANCHO / 2 + 13 * T, 196, -kit.ANCHO / 2 + 15 * T))
        out.append(Pieza(ala, "ALERÓN TRASERO", "xy", 38, tipo="carroceria", etiqueta="AT", pri=1))
        # alerón delantero
        ala_d = box(0.5, -39, 21, 39).union(box(2, -42, 19, -39)).union(box(2, 39, 19, 42))
        out.append(Pieza(ala_d, "ALERÓN DELANTERO", "xy", 5, tipo="carroceria", etiqueta="AD", pri=-1))
        # derivas (placas de los costados de los alerones)
        der_t = Polygon(suave([(180, 20), (182, 44), (200, 46), (200, 22)], 4)).buffer(0)
        der_t = box(180, 20, 200, 46).difference(box(186, 38, 198, 38 + T))
        der_d = box(0, 5, 24, 15).difference(box(2, 4, 19, 5 + T))
        der_d = kit.redondear(der_d, 1.2)
        for lado, y0 in (("IZQ", -kit.ANCHO / 2), ("DER", kit.ANCHO / 2 - T)):
            cerca = y0 < 0
            out.append(Pieza(kit.redondear(der_t, 1.5), f"DERIVA TRAS {lado}", "xz", y0,
                             tipo="carroceria", etiqueta="DT", pri=2 if cerca else 0))
            out.append(Pieza(der_d, f"DERIVA DEL {lado}", "xz", y0, tipo="carroceria",
                             etiqueta="DD", pri=2 if cerca else -2))
        return out

    def textos_capa(self, k):
        """Número de carrera grabado en los pontones."""
        if desde_afuera(k) == 4:
            return [(self.NUMERO, 101, 13, 12)]
        return []


MODELOS = [Superauto(), Clasico(), Formula()]
