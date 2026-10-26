"""Arma el paquete para el taller de corte láser (correr después de generar.py):
- para-el-cortador/kit-autos-para-el-cortador.pdf: los autos armados, las hojas y cómo cortar.
- para-el-cortador/kit-autos-para-cortar.zip: el PDF + todos los SVG y DXF con nombres claros.
"""
import glob
import math
import os
import subprocess
import zipfile

import ezdxf

from generar import CHROME

AQUI = os.path.dirname(os.path.abspath(__file__))
SALIDA = os.path.join(AQUI, "para-el-cortador")
MODELOS = [("formula", "Fórmula", "Auto de carrera con ruedas a la vista. El más chico y económico."),
           ("superauto", "Superauto", "Deportivo en cuña, estilo superauto italiano."),
           ("clasico", "Clásico", "Coupé fastback de los años 70.")]


def datos(clave):
    hojas = sorted(glob.glob(os.path.join(AQUI, clave, "hoja-*.dxf")))
    corte, medidas = 0.0, []
    for h in hojas:
        doc = ezdxf.readfile(h)
        for e in doc.modelspace().query('LWPOLYLINE[layer=="CORTAR"]'):
            pts = list(e.get_points("xy"))
            corte += sum(math.dist(a, b) for a, b in zip(pts, pts[1:] + pts[:1]))
        svg = open(h.replace(".dxf", ".svg")).read()
        ancho = svg.split('width="')[1].split("mm")[0]
        alto = svg.split('height="')[1].split("mm")[0]
        medidas.append(f"{float(ancho) / 10:g} x {float(alto) / 10:g} cm")
    return hojas, corte / 1000, medidas


def main():
    os.makedirs(SALIDA, exist_ok=True)
    tarjetas, paginas = [], []
    for clave, nombre, desc in MODELOS:
        hojas, corte, medidas = datos(clave)
        img3d = os.path.join(AQUI, clave, "vista-3d.png")
        tarjetas.append(f'<div class="card"><img src="file://{img3d}"><b>{nombre}</b><br>'
                        f'<span>{" + ".join(medidas)} · ~{corte:.0f} m de corte</span></div>')
        filas = "".join(f"<tr><td><code>{clave}-hoja-{i}.svg</code> / <code>.dxf</code></td>"
                        f"<td>{m}</td></tr>" for i, m in enumerate(medidas, 1))
        imgs = "".join(f'<img class="hoja" src="file://{h.replace(".dxf", ".png")}">' for h in hojas)
        paginas.append(f"""<section class="salto"><h2>{nombre}</h2><p>{desc}</p>
<img class="auto" src="file://{img3d}">
<table><tr><th>Archivo</th><th>Medida de la hoja</th></tr>{filas}
<tr><td>Corte total</td><td>~{corte:.1f} m</td></tr></table>
{imgs}</section>""")
    html = f"""<!doctype html><html lang="es"><head><meta charset="utf-8"><style>
@page {{ size: A4; margin: 12mm; }}
body {{ font-family: Arial, sans-serif; color: #2b2118; font-size: 11pt; }}
h1 {{ font-size: 22pt; margin: 0 0 4px; color: #3b2a1a; }}
h2 {{ font-size: 17pt; color: #8a4b12; border-bottom: 2px solid #e8c9a0; margin: 0 0 6px; }}
.cards {{ display: flex; gap: 8px; margin: 10px 0; }}
.card {{ flex: 1; border: 1px solid #e3d2b8; border-radius: 6px; padding: 6px; font-size: 10pt; }}
.card img {{ width: 100%; }} .card span {{ color: #6b5640; }}
table {{ border-collapse: collapse; width: 100%; margin: 8px 0; font-size: 10pt; }}
td, th {{ border: 1px solid #d9c3a3; padding: 4px 6px; text-align: left; }} th {{ background: #f6ead8; }}
.auto {{ width: 100%; }} .hoja {{ width: 100%; border: 1px solid #ccc; margin-top: 6px; }}
.salto {{ page-break-before: always; }}
.rojo {{ color: #e00; font-weight: bold; }} .azul {{ color: #00f; font-weight: bold; }}
</style></head><body>
<h1>Kit de autos de madera: archivos para corte láser</h1>
<p>3 autos para armar, escala 1:24 (20 cm de largo). Cada archivo trae <b>un auto completo</b>
(chasis, carrocería y ruedas).</p>
<div class="cards">{"".join(tarjetas)}</div>
<h2>Cómo cortar</h2>
<table>
<tr><th>Material</th><td>MDF / fibrofácil <b>crudo de 3 mm</b>. Versión premium: terciado de 3 mm para láser
(abedul o álamo). El fenólico no sirve.</td></tr>
<tr><th>Archivos</th><td>Cada hoja viene en <b>SVG</b> y en <b>DXF</b> (el mismo dibujo). Escala 1:1, en milímetros.</td></tr>
<tr><th><span class="rojo">Rojo</span> / capa CORTAR</th><td>Corte pasante.</td></tr>
<tr><th><span class="azul">Azul</span> / capa GRABAR</th><td>Grabado de línea y textos (números de pieza, dibujos del piso).</td></tr>
<tr><th><span class="azul">Azul relleno</span> / GRABAR_RELLENO</th><td>Grabado lleno, poco profundo (vidrios y discos de las ruedas).</td></tr>
<tr><th>Gris / NOTAS</th><td><b>No se corta ni se graba</b>: son nombres de referencia.</td></tr>
<tr><th>Espesor</th><td>Las ranuras están hechas para <b>3,0 mm justos</b>. Si la placa mide otra cosa
(por ejemplo 2,8 mm), avisar y se mandan los archivos ajustados. No hace falta compensar el ancho del corte.</td></tr>
<tr><th>Pedido</th><td>Primero <b>1 de cada modelo de prueba</b>. Después cotizar 10, 20 y 50 de cada uno.</td></tr>
</table>
{"".join(paginas)}
</body></html>"""
    ruta_html = os.path.join(SALIDA, "tmp.html")
    with open(ruta_html, "w") as f:
        f.write(html)
    pdf = os.path.join(SALIDA, "kit-autos-para-el-cortador.pdf")
    subprocess.run([CHROME, "--headless", "--no-sandbox", "--disable-gpu", "--no-pdf-header-footer",
                    "--allow-file-access-from-files", f"--print-to-pdf={pdf}", f"file://{ruta_html}"],
                   capture_output=True, check=False)
    os.remove(ruta_html)
    with zipfile.ZipFile(os.path.join(SALIDA, "kit-autos-para-cortar.zip"), "w",
                         zipfile.ZIP_DEFLATED) as z:
        z.write(pdf, os.path.basename(pdf))
        for clave, _, _ in MODELOS:
            for f in sorted(glob.glob(os.path.join(AQUI, clave, "hoja-*.svg")) +
                            glob.glob(os.path.join(AQUI, clave, "hoja-*.dxf"))):
                z.write(f, f"{clave}-{os.path.basename(f)}")
    print(pdf)


if __name__ == "__main__":
    main()
