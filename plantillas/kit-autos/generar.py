"""Genera todo el kit: hojas de corte (SVG + DXF), vistas 3D, imágenes de los pasos,
instructivo para imprimir (HTML + PDF) y la planilla para pedir presupuesto.

Uso:  pip install shapely ezdxf pillow
      python3 generar.py            (material de 3 mm)
      python3 generar.py 2.8        (si el material mide otra cosa)
Necesita Chromium para pasar las imágenes a PNG y el instructivo a PDF.
"""
import os
import shutil
import subprocess
import sys

from PIL import Image
from shapely import affinity
from shapely.geometry import Point

import kit

if len(sys.argv) > 1:
    kit.configurar(sys.argv[1])

import modelos  # noqa: E402  (las siluetas dependen del espesor)

AQUI = os.path.dirname(os.path.abspath(__file__))
CHROME = shutil.which("chromium") or shutil.which("google-chrome") or \
    "/opt/pw-browsers/chromium-1194/chrome-linux/chrome"
HOJA = (600, 400)


# --- utilidades -----------------------------------------------------------------
def a_png(svg_path, png_path, w, h, ancho_final=None):
    subprocess.run([CHROME, "--headless", "--no-sandbox", "--disable-gpu", "--hide-scrollbars",
                    f"--screenshot={png_path}", f"--window-size={w},{h + 140}",
                    f"file://{svg_path}"], capture_output=True, check=False)
    im = Image.open(png_path).crop((0, 0, w, h))
    if ancho_final and ancho_final < w:
        im = im.resize((ancho_final, round(h * ancho_final / w)), Image.LANCZOS)
    im.save(png_path, optimize=True)


def guardar_escena(escena, ruta, w=900, h=560, titulo=None, fondo="#ffffff"):
    with open(ruta + ".svg", "w") as f:
        f.write(escena.svg(w, h, fondo, titulo))
    a_png(ruta + ".svg", ruta + ".png", w, h)
    os.remove(ruta + ".svg")
    return ruta + ".png"


def tono(pz):
    return "#e6c391" if (pz.capa or 0) % 2 else "#dfba86"


# --- escenas ----------------------------------------------------------------------
def escena_chasis(H, partes, nuevas=(), elec=(), elec_nueva=(), ejes=(), cubiertas=(),
                  levantar=8.0, cam=None):
    """Chasis con algunas partes; las nuevas van resaltadas y un poco levantadas."""
    e = kit.Escena(cam or kit.Camara(-118, 52))
    for pz in kit.chasis(H):
        clave = grupo(pz)
        if clave not in partes and clave not in nuevas:
            continue
        nueva = clave in nuevas
        d = (0, 0, levantar) if nueva and clave in ("largueros", "travesanos", "soporte", "torre") \
            else (0, 0, 0)
        if nueva:
            e.pieza(pz, fill=kit.NUEVO, stroke=kit.BORDE_NUEVO, desplazar=d)
        else:
            e.pieza(pz)
    for x in ejes:
        kit.eje(e, x)
    if cubiertas:
        kit.cubiertas(e, ejes=cubiertas)
    if elec:
        kit.electronica(e, H, que=elec)
    if elec_nueva:
        kit.electronica(e, H, que=elec_nueva)
    return e


def grupo(pz):
    n = pz.nombre
    if n == "PISO":
        return "piso"
    if n.startswith("LARGUERO"):
        return "largueros"
    if n.startswith("TRAVESA"):
        return "travesanos"
    if n == "SOPORTE MOTOR":
        return "soporte"
    if n.startswith("TORRE") or n == "TAPA TORRE":
        return "torre"
    if n == "POLEA":
        return "polea"
    if n.startswith("RUEDA") or n == "ARANDELA":
        x = pz.g3d.centroid.x if pz.g3d is not None else 0
        return "ruedas_tras" if x > 100 else "ruedas_del"
    return n


def escena_auto(modelo, H, con_chasis=False, cam=None):
    e = kit.Escena(cam or kit.Camara(-125, 22), por_capas=True)
    body, _ = kit.carroceria(modelo)
    for pz in body:
        e.pieza(pz, fill=tono(pz))
    for pz in kit.ruedas_y_polea():
        e.pieza(pz)
    kit.cubiertas(e)
    if con_chasis:
        for pz in kit.chasis(H):
            if pz.tipo in ("chasis", "torre"):
                e.pieza(pz)
        kit.electronica(e, H, que=("motor", "goma", "pilas", "bornes"))
        for x in (kit.EJE_DEL, kit.EJE_TRAS):
            kit.eje(e, x)
    else:
        torre = [p for p in kit.chasis(H) if p.nombre == "TAPA TORRE"][0]
        e.pieza(torre, prof=e.cam.c[1] * kit.CANAL_Y)
    e.prisma(Point(*kit.BOTON).buffer(5, 24), "xy", H, 7, fill="#e03131", stroke="#8a1c1c",
             prof=e.cam.c[1] * -6)
    return e


def escena_capas(modelo, separar=6.0):
    """Carrocería abierta en abanico, para mostrar el orden de las capas."""
    e = kit.Escena(kit.Camara(-145, 32), por_capas=True)
    body, _ = kit.carroceria(modelo)
    for pz in body:
        if pz.capa is None:
            d = (0, 0, 18)
            e.pieza(pz, fill=kit.NUEVO, stroke=kit.BORDE_NUEVO, desplazar=d)
            continue
        d = (0, (pz.capa - kit.N / 2 + 0.5) * separar, 0)
        e.pieza(pz, fill=tono(pz), desplazar=d)
    marcas = sorted({0, 4, 5, kit.N // 2, kit.N - 6, kit.N - 5, kit.N - 1})
    for k in marcas:
        partes = [p for p in body if p.capa == k]
        if not partes:
            continue
        top = max(p.geom.bounds[3] for p in partes)
        y = kit.tramo(k)[0] + kit.T / 2 + (k - kit.N / 2 + 0.5) * separar
        e.texto((100, y, top + 6), str(k + 1), 17, "#b03a00")
    return e


def escena_rueda():
    """Discos de la rueda y de la polea en fila, de frente, con nombres."""
    e = kit.Escena(kit.Camara(-96, 14))
    piezas = {p.nombre: p for p in kit.ruedas_y_polea() if p.pos < 0 or p.nombre == "POLEA"}
    fila = [("RUEDA llanta", "1. llanta"), ("RUEDA disco", "2. disco chico"),
            ("RUEDA interior", "3. disco liso")]
    for i, (n, txt) in enumerate(fila):
        pz = piezas[n]
        x = i * 42
        e.prisma(affinity.translate(pz.geom, x, 0), "xz", 0, kit.T,
                 fill=pz.color or kit.MADERA, grab=pz.grab and [affinity.translate(g, x, 0)
                                                               for g in pz.grab])
        e.texto((x, 0, -24), txt, 15, "#8a4b12")
    x = 3 * 42
    g = Point(0, 0).buffer(kit.R_CUBIERTA, 48).difference(Point(0, 0).buffer(kit.R_CANAL, 48))
    e.prisma(affinity.translate(g, x, 0), "xz", 0, kit.T, fill="#222", stroke="#000")
    e.texto((x, 0, -24), "4. o-ring", 15, "#8a4b12")
    for i, r in enumerate((10.5, 9.0, 10.5)):
        e.prisma(affinity.translate(kit.disco(r), 190 + i * 26, 0), "xz", 0, kit.T)
    e.texto((216, 0, -24), "polea: grande + chico + grande", 15, "#8a4b12")
    return e


def escena_colocar(modelo, H):
    e = kit.Escena(kit.Camara(-125, 30))
    for pz in kit.chasis(H):
        e.pieza(pz)
    kit.electronica(e, H)
    for x in (kit.EJE_DEL, kit.EJE_TRAS):
        kit.eje(e, x)
    kit.cubiertas(e)
    body, _ = kit.carroceria(modelo)
    for pz in body:
        e.pieza(pz, fill=tono(pz), desplazar=(0, 0, 75), prioridad=1)
    return e


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


def pernos_svg(modelo, pernos, ruta):
    """Perfil de costado con la posición de cada perno."""
    body, _ = kit.carroceria(modelo)
    perfil = kit.unary_union([p.geom for p in body if p.plano == "xz"]).buffer(0)
    E, W, H = 4.0, 900, 300
    ox, oz = 50, 260

    def f(ring):
        return " ".join(f"{ox + E * a:.1f},{oz - E * b:.1f}" for a, b in ring)

    out = [f'<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}" '
           'font-family="Arial, sans-serif">', f'<rect width="{W}" height="{H}" fill="#fff"/>']
    for q in kit.poligonos(perfil):
        d = "M" + f(q.exterior.coords) + " Z" + "".join(" M" + f(r.coords) + " Z" for r in q.interiors)
        out.append(f'<path d="{d}" fill="#f1dcb8" fill-rule="evenodd" stroke="#a07a4a" stroke-width="1.5"/>')
    vistos = {}
    for i, p in enumerate(pernos):
        letra = chr(65 + i)
        clave = (p["x"], p["z"])
        vistos.setdefault(clave, []).append(letra)
    for (x, z), letras in vistos.items():
        cx, cy = ox + E * x, oz - E * z
        out.append(f'<circle cx="{cx}" cy="{cy}" r="7" fill="#e8590c" stroke="#fff" stroke-width="2"/>')
        out.append(f'<text x="{cx}" y="{cy - 12}" font-size="17" font-weight="bold" fill="#c2410c" '
                   f'text-anchor="middle">{" y ".join(letras)}</text>')
    out.append(f'<text x="20" y="26" font-size="16" fill="#333">Vista de costado: cada punto naranja '
               'es un perno (letras de la tabla). FRENTE a la izquierda.</text></svg>')
    with open(ruta + ".svg", "w") as fh:
        fh.write("\n".join(out))
    a_png(ruta + ".svg", ruta + ".png", W, H)
    os.remove(ruta + ".svg")


# --- hojas de corte -------------------------------------------------------------
def hojas_de_corte(modelo, carpeta, H):
    piezas = kit.chasis(H) + kit.carroceria(modelo)[0]
    hojas = kit.acomodar(piezas, HOJA)
    largo, relleno, lineas, tamanos = 0.0, 0.0, 0.0, []
    for i, h in enumerate(hojas, 1):
        base = os.path.join(carpeta, "hoja")
        # la hoja se recorta a lo que se usa (redondeado a 1 cm)
        usado = max(it["geom"].bounds[3] for it in h) + 12
        alto = min(HOJA[1], int(-(-usado // 10) * 10))
        l, r = kit.guardar_hoja(base, i, h, (HOJA[0], alto), f"Kit {modelo.titulo}")
        tamanos.append((HOJA[0], alto))
        largo += l
        relleno += r
        lineas += sum(e.length for it in h for e in it["grab"] if e.geom_type == "LineString")
        a_png(f"{base}-{i}.svg", f"{base}-{i}.png", 2268, round(alto * 3.78), 1600)
    area = sum(p.geom.area for p in piezas if p.cortar)
    return dict(hojas=len(hojas), tamanos=tamanos, piezas=sum(1 for p in piezas if p.cortar),
                corte_m=largo / 1000, relleno_cm2=relleno / 100, lineas_m=lineas / 1000,
                area_m2=area / 1e6, peso_g=area * kit.T / 1000 * 0.75)


def minutos(st):
    """Estimación de minutos de láser (60-80 W): corte a 12-18 mm/s, grabado lleno a
    ~25-40 mm²/s y grabado de línea a ~60 mm/s."""
    lento = st["corte_m"] * 1000 / 12 + st["relleno_cm2"] * 100 / 25 + st["lineas_m"] * 1000 / 60
    rapido = st["corte_m"] * 1000 / 18 + st["relleno_cm2"] * 100 / 40 + st["lineas_m"] * 1000 / 90
    return round(rapido / 60), round(lento / 60)


def hojas_txt(st):
    partes = [f"{w // 10} x {h // 10} cm" for w, h in st["tamanos"]]
    return ("1 hoja de " if len(partes) == 1 else f"{len(partes)} hojas: ") + " + ".join(partes)


# --- instructivo -------------------------------------------------------------------
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


def instructivo(modelo, carpeta, H, st, pernos):
    img = os.path.join(carpeta, "pasos")
    os.makedirs(img, exist_ok=True)
    rutas = {}
    rutas["tapa"] = guardar_escena(escena_auto(modelo, H, con_chasis=False), os.path.join(img, "00-auto"),
                                   1100, 560, None, "#f6f1ea")
    pasos_chasis = [
        ("01", dict(partes=("piso",), nuevas=("largueros",))),
        ("02", dict(partes=("piso", "largueros"), nuevas=("travesanos",))),
        ("04", dict(partes=("piso", "largueros", "travesanos"), nuevas=("ruedas_tras", "polea"),
                    ejes=(kit.EJE_TRAS,), cubiertas=(kit.EJE_TRAS,))),
        ("05", dict(partes=("piso", "largueros", "travesanos", "ruedas_tras", "polea"),
                    nuevas=("ruedas_del",), ejes=(kit.EJE_DEL, kit.EJE_TRAS))),
        ("06", dict(partes=("piso", "largueros", "travesanos", "ruedas_tras", "ruedas_del", "polea"),
                    nuevas=("soporte",), ejes=(kit.EJE_DEL, kit.EJE_TRAS), elec_nueva=("motor", "goma"))),
        ("07", dict(partes=("piso", "largueros", "travesanos", "ruedas_tras", "ruedas_del", "polea",
                            "soporte"), nuevas=("torre",), ejes=(kit.EJE_DEL, kit.EJE_TRAS),
                    elec=("motor", "goma"), elec_nueva=("boton",))),
        ("08", dict(partes=("piso", "largueros", "travesanos", "ruedas_tras", "ruedas_del", "polea",
                            "soporte", "torre"), ejes=(kit.EJE_DEL, kit.EJE_TRAS),
                    elec=("motor", "goma", "boton"), elec_nueva=("pilas", "bornes", "cables"))),
    ]
    for n, kw in pasos_chasis:
        cub = kw.get("cubiertas", ())
        if n in ("05", "06", "07", "08"):
            kw["cubiertas"] = (kit.EJE_DEL, kit.EJE_TRAS)
        elif not cub:
            kw["cubiertas"] = ()
        rutas[n] = guardar_escena(escena_chasis(H, **kw), os.path.join(img, f"{n}-chasis"), 900, 520)
    rutas["03"] = guardar_escena(escena_rueda(), os.path.join(img, "03-ruedas"), 900, 420)
    circuito_svg(os.path.join(img, "08b-circuito"))
    rutas["08b"] = os.path.join(img, "08b-circuito.png")
    rutas["10"] = guardar_escena(escena_capas(modelo), os.path.join(img, "10-capas"), 1000, 600)
    rutas["12"] = guardar_escena(escena_colocar(modelo, H), os.path.join(img, "12-colocar"), 900, 600)
    pernos_svg(modelo, pernos, os.path.join(img, "10b-pernos"))
    rutas["10b"] = os.path.join(img, "10b-pernos.png")

    rel = lambda r: os.path.relpath(r, carpeta)
    filas_pernos = "".join(
        f"<tr><td>{chr(65 + i)}</td><td>{p['largo']:g} mm</td><td>capas {p['desde']} a {p['hasta']}</td></tr>"
        for i, p in enumerate(pernos))
    n_capas = len({p.capa for p in kit.carroceria(modelo)[0] if p.capa is not None})
    extras = [p.nombre for p in kit.carroceria(modelo)[0] if p.capa is None]
    t_min, t_max = minutos(st)
    html = f"""<!doctype html><html lang="es"><head><meta charset="utf-8">
<title>Instructivo {modelo.titulo}</title><style>{CSS}</style></head><body>
<div class="tapa">
<h1>Auto {modelo.titulo}</h1>
<div class="sub">{modelo.subtitulo} · escala 1:24 · madera cortada con láser + motor eléctrico</div>
<img src="{rel(rutas['tapa'])}">
</div>
<h2>Qué trae el kit</h2>
<table>
<tr><th>Madera (MDF o terciado de {kit.T:g} mm)</th><th>Electrónica y otros</th></tr>
<tr><td><ul>
<li>Chasis: piso, 2 largueros, 2 travesaños, soporte del motor y torre del botón (3 piezas).</li>
<li>Carrocería: {n_capas} capas numeradas de 1 a {kit.N}{(' + ' + ', '.join(extras).lower()) if extras else ''}.</li>
<li>4 ruedas de 3 discos cada una, 8 arandelas y la polea (3 discos).</li>
<li>Total: {st['piezas']} piezas en {hojas_txt(st)}.</li>
</ul></td><td><ul>
<li>1 motor DC 3 V tipo 130 (mejor con cables).</li>
<li>1 portapilas para 2 pilas AA con cables (mejor con tapa a tornillo) + 2 pilas AA.</li>
<li>1 pulsador de 12 mm con traba (mejor con cables).</li>
<li>3 bornes de empalme sin soldar (tipo Wago 221).</li>
<li>4 o-rings de goma 31 x 3 mm (o 30 x 3) para las cubiertas.</li>
<li>1 gomita de silicona chica (la transmisión).</li>
<li>Palitos de brochette de 3 mm: 2 ejes de 80 mm + los pernos (ver paso 9).</li>
<li>Cola vinílica, cinta doble faz, lija fina (220).</li>
</ul></td></tr></table>
<div class="ojo"><b>Seguridad:</b> armar con un adulto. Tiene piezas chicas: no apto para menores de
3 años. No usar pilas de botón. Lijar los bordes antes de jugar.</div>

<h2 class="salto">Parte 1: el chasis (la base con el motor)</h2>
<p>El chasis es igual para todos los modelos. Las piezas encastran: las pestañas entran en las ranuras.
Si entran muy justas, lijá un poquito la pestaña. Si quedan flojas, poné una gota de cola.</p>

<div class="paso"><h3><span class="num">1</span>Piso y largueros</h3>
<img src="{rel(rutas['01'])}">
<p>Poné el <b>PISO</b> con los dibujos grabados hacia arriba (la palabra FRENTE va adelante). Encastrá los
dos <b>LARGUEROS</b> (los que tienen 2 agujeros para los ejes) en las ranuras de los costados.</p></div>

<div class="paso"><h3><span class="num">2</span>Travesaños</h3>
<img src="{rel(rutas['02'])}">
<p>Encastrá el <b>TRAVESAÑO DELANTERO</b> (TD, el más bajo) adelante y el <b>TRASERO</b> (TT) atrás. Sus
pestañas entran en el piso y en los largueros. Ahora es buen momento para poner cola en las uniones.</p></div>

<div class="paso"><h3><span class="num">3</span>Armar las ruedas y la polea</h3>
<img src="{rel(rutas['03'])}">
<p>Cada rueda son 3 discos: la <b>llanta</b> (con rayos) afuera, el <b>disco chico</b> en el medio y el
<b>disco liso</b> adentro. Pegalos con cola, alineando los agujeros con un palito. Cuando sequen, poné el
<b>o-ring</b> en la canaleta: es la cubierta. La <b>polea</b> se arma igual: disco grande + chico + grande.</p></div>

<div class="paso"><h3><span class="num">4</span>Eje trasero con la polea</h3>
<img src="{rel(rutas['04'])}">
<p>Pasá un palito de 80 mm por el agujero de atrás de un larguero, metele la <b>polea</b> por adentro del
chasis y seguí hasta el otro larguero. Afuera, en cada punta: <b>2 arandelas</b> y una <b>rueda</b> a
presión. El eje tiene que girar libre en los largueros; las ruedas y la polea, en cambio, quedan firmes en
el eje (si bailan, una gota de cola).</p></div>

<div class="paso"><h3><span class="num">5</span>Eje delantero</h3>
<img src="{rel(rutas['05'])}">
<p>Igual que el trasero, pero sin polea: palito, 2 arandelas y una rueda en cada punta.</p></div>

<div class="paso"><h3><span class="num">6</span>Motor y goma</h3>
<img src="{rel(rutas['06'])}">
<p>Apoyá el <b>motor</b> en el piso, sobre el dibujo que dice MOTOR, con el eje hacia la polea. Calzá el
<b>SOPORTE MOTOR</b> encima (sus patitas entran en el piso). Pasá la <b>gomita</b> por el eje del motor y
por la canaleta de la polea. Mové la polea sobre el eje hasta que quede justo enfrente del eje del motor.</p></div>

<div class="paso"><h3><span class="num">7</span>Torre del botón</h3>
<img src="{rel(rutas['07'])}">
<p>Encastrá los 2 laterales de la <b>TORRE</b> en el piso y poné la tapa arriba. Atornillá el
<b>pulsador</b> en el agujero de la tapa (la tuerca va por abajo). Los cables del botón bajan por adentro
de la torre.</p></div>

<div class="paso"><h3><span class="num">8</span>Pilas y conexiones (sin soldar)</h3>
<img src="{rel(rutas['08'])}">
<p>Pegá el <b>portapilas</b> con cinta doble faz sobre el dibujo PILAS. Los <b>bornes</b> van en los
lugares marcados B1, B2 y B3. Para conectar: levantá la palanquita del borne, meté el cable pelado
(1 cm sin plástico) y bajá la palanquita. Seguí este dibujo:</p>
<img src="{rel(rutas['08b'])}">
<table><tr><th>Borne</th><th>Cables que van juntos</th></tr>
<tr><td>B1</td><td>Rojo (+) de las pilas y un cable del botón</td></tr>
<tr><td>B2</td><td>El otro cable del botón y un cable del motor</td></tr>
<tr><td>B3</td><td>El otro cable del motor y el negro (−) de las pilas</td></tr></table>
<p>Pasá los cables pegados al piso, lejos de la polea y la goma.</p></div>

<div class="paso"><h3><span class="num">9</span>¡Prueba!</h3>
<p>Poné 2 pilas AA y apretá el botón: las ruedas de atrás tienen que girar. Volvé a apretar: se apaga.</p>
<ul><li>Si gira para atrás: cambiá entre sí los cables del motor en B2 y B3.</li>
<li>Si el motor gira pero las ruedas no: la goma patina. Probá una gomita más chica (más tensa).</li>
<li>Si no hace nada: revisá que cada cable esté bien apretado en su borne y que las pilas estén bien puestas.</li></ul></div>

<h2 class="salto">Parte 2: la carrocería del {modelo.titulo}</h2>
<div class="paso"><h3><span class="num">10</span>Apilar las capas en orden</h3>
<img src="{rel(rutas['10'])}">
<p>Las capas tienen el número grabado (en la parte que queda tapada). Se apilan de la <b>1</b>
(costado izquierdo, la que tiene los detalles grabados) a la <b>{kit.N}</b> (costado derecho).
Las piezas que dicen <b>(espejo)</b> en la hoja ya vienen dadas vuelta: el lado grabado va hacia afuera.
Algunas capas vienen en 2 partes (a y b): van una detrás de la otra, en la misma capa.</p>
<p><b>Pernos:</b> usá palitos de brochette como pernos para que las capas queden alineadas. Cortalos a
estas medidas:</p>
<table><tr><th>Perno</th><th>Largo</th><th>Pasa por</th></tr>{filas_pernos}</table>
<img src="{rel(rutas['10b'])}">
<p>Andá poniendo cola entre capa y capa (poca, con un pincel) y apretá. Dejá secar 2 horas con peso
encima.</p></div>

<div class="paso"><h3><span class="num">11</span>Lijar y terminar</h3>
<p>Lijá los cantos con lija 220 hasta que queden suaves y sin hollín. Terminá con barniz al agua o
cera de abejas. Si lo pintás, usá acrílico al agua (no tóxico). <b>No pintes ni barnices adentro</b>,
donde apoya en el chasis, así no se pega.</p></div>

<div class="paso"><h3><span class="num">12</span>Poner la carrocería</h3>
<img src="{rel(rutas['12'])}">
<p>Bajá la carrocería sobre el chasis: apoya sobre los largueros y el botón asoma por el agujero de
atrás. <b>Para cambiar las pilas o ver el motor, levantala.</b> Para llevar el auto, agarralo de abajo
(del chasis).</p></div>

<h2 class="salto">Datos técnicos</h2>
<table>
<tr><td>Medidas</td><td>20 cm de largo, 8,4 cm de ancho · escala 1:24</td></tr>
<tr><td>Material</td><td>{hojas_txt(st)} de MDF o terciado de {kit.T:g} mm</td></tr>
<tr><td>Piezas</td><td>{st['piezas']}</td></tr>
<tr><td>Corte láser</td><td>{st['corte_m']:.1f} m de corte, {st['relleno_cm2']:.0f} cm² de grabado lleno,
{st['lineas_m']:.1f} m de grabado de línea · unos {t_min} a {t_max} minutos (estimado)</td></tr>
<tr><td>Peso de la madera</td><td>unos {st['peso_g']:.0f} g en MDF (el terciado es más liviano)</td></tr>
<tr><td>Circuito</td><td>2 pilas AA (3 V) → pulsador con traba → motor 130</td></tr>
</table>
<p class="chico">Diseño propio, genérico. No usar nombres ni logos de marcas de autos.</p>
</body></html>"""
    ruta = os.path.join(carpeta, "instructivo.html")
    with open(ruta, "w") as f:
        f.write(html)
    subprocess.run([CHROME, "--headless", "--no-sandbox", "--disable-gpu", "--no-pdf-header-footer",
                    f"--print-to-pdf={os.path.join(carpeta, 'instructivo.pdf')}", f"file://{ruta}"],
                   capture_output=True, check=False)


# --- principal -----------------------------------------------------------------------
def main():
    resumen = []
    for m in modelos.MODELOS:
        carpeta = os.path.join(AQUI, m.clave)
        if os.path.isdir(carpeta):
            shutil.rmtree(carpeta)
        os.makedirs(carpeta)
        H = kit.altura_torre(m)
        body, pernos = kit.carroceria(m)
        avisos = kit.verificar(m, body)
        if H < 31:
            avisos.append(f"la torre del botón queda baja ({H} mm)")
        st = hojas_de_corte(m, carpeta, H)
        guardar_escena(escena_auto(m, H, con_chasis=(m.clave == "formula")),
                       os.path.join(carpeta, "vista-3d"), 1200, 620, None, "#f6f1ea")
        instructivo(m, carpeta, H, st, pernos)
        st.update(modelo=m.titulo, clave=m.clave, avisos=avisos, minutos=minutos(st), torre=H)
        resumen.append(st)
        print(f"{m.titulo}: {st['piezas']} piezas, {st['hojas']} hojas, {st['corte_m']:.1f} m de corte, "
              f"{st['relleno_cm2']:.0f} cm2 relleno, ~{st['minutos'][0]}-{st['minutos'][1]} min, "
              f"{st['peso_g']:.0f} g, torre {H} mm, avisos: {avisos or 'ninguno'}")
    pedido(resumen)


def pedido(resumen):
    """Planilla para pedir presupuesto a los que cortan con láser."""
    filas = []
    for st in resumen:
        archivos = ", ".join(f"`{st['clave']}/hoja-{i}.svg`" for i in range(1, st["hojas"] + 1))
        filas.append(f"| **{st['modelo']}** | {hojas_txt(st)} | {st['piezas']} | {st['corte_m']:.1f} m | "
                     f"{st['relleno_cm2']:.0f} cm² + {st['lineas_m']:.1f} m de línea | "
                     f"{st['minutos'][0]} a {st['minutos'][1]} min | {archivos} |")
    txt = f"""# Pedido de presupuesto: corte láser del kit de autos

Archivo generado por `generar.py`. Si cambia el diseño o el espesor, se vuelve a generar.

## Qué mandar al taller
- Los archivos de la carpeta de cada modelo: `hoja-N.svg` o `hoja-N.dxf` (el mismo dibujo, en los
  dos formatos; mandar el que pida el taller).
- **Material:** MDF / fibrofácil **crudo de {kit.T:g} mm**. Versión premium: terciado de {kit.T:g} mm
  "para láser" (abedul o álamo; el fenólico no sirve).
- **Colores / capas del archivo:**
  - **Rojo / CORTAR:** corte pasante.
  - **Azul / GRABAR:** grabado de línea y textos (números de las piezas, puertas, dibujos del piso).
  - **Azul relleno / GRABAR_RELLENO:** grabado lleno, no muy profundo (vidrios y discos de las ruedas).
  - **Gris / NOTAS:** son notas, **no se cortan ni se graban**.
- **Medidas:** las ranuras y pestañas están hechas para material de {kit.T:g} mm justos. Pedirle al
  taller que **mida el espesor real de la placa**: si no es {kit.T:g} mm, se regenera el archivo con la
  medida correcta (`python3 generar.py 2.8`, por ejemplo). No hace falta compensar el ancho del corte.
- **Primero 1 auto de prueba** de cada modelo, para revisar los encastres antes de cortar la tanda.

## Datos por modelo (1 auto)

| Modelo | Material | Piezas | Corte | Grabado | Tiempo estimado* | Archivos |
|---|---|---|---|---|---|---|
""" + "\n".join(filas) + f"""

\* Estimación propia para un láser CO2 de 60 a 80 W. Cada taller tiene su velocidad: pedirles el
precio por minuto o por hoja.

## Mensaje para mandar por WhatsApp
> Hola, quiero cotizar corte y grabado láser en MDF crudo de {kit.T:g} mm (yo puedo llevar la placa o
> la ponen ustedes). Son kits de autitos de madera. Te mando los archivos (SVG y DXF):
> - Fórmula: {hojas_txt(resumen[2])}, unos {resumen[2]['corte_m']:.0f} m de corte.
> - Superauto: {hojas_txt(resumen[0])}, unos {resumen[0]['corte_m']:.0f} m de corte.
> - Clásico: {hojas_txt(resumen[1])}, unos {resumen[1]['corte_m']:.0f} m de corte.
>
> Rojo es corte, azul es grabado (el azul relleno es grabado lleno) y lo gris no se hace.
> Quiero primero 1 de cada uno de prueba, y después cotizar 10, 20 y 50 de cada modelo.
> ¿Cuánto me sale cada uno y en cuánto tiempo lo tienen? ¿Pueden medir el espesor real de la placa?
"""
    with open(os.path.join(AQUI, "PEDIDO-DE-PRESUPUESTO.md"), "w") as f:
        f.write(txt)


if __name__ == "__main__":
    main()
