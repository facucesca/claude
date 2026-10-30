"""Pasa un archivo Markdown a PDF (A4) para imprimir.

Uso:  pip install markdown
      python3 herramientas/md_a_pdf.py proveedores/proveedores.md
Necesita Chromium.
"""
import glob
import os
import shutil
import subprocess
import sys

import markdown

CHROME = (shutil.which("chromium") or shutil.which("google-chrome") or shutil.which("chromium-browser")
          or shutil.which("chrome")
          or next((p for p in ["/Applications/Google Chrome.app/Contents/MacOS/Google Chrome",
                               r"C:\Program Files\Google\Chrome\Application\chrome.exe",
                               r"C:\Program Files (x86)\Google\Chrome\Application\chrome.exe"]
                   if os.path.exists(p)), None)
          or next(iter(sorted(glob.glob("/opt/pw-browsers/chromium-*/chrome-linux*/chrome"))), "chromium"))

CSS = """
@page { size: A4; margin: 12mm; }
body { font-family: Arial, Helvetica, sans-serif; color: #2b2118; font-size: 10pt; line-height: 1.35; }
h1 { font-size: 20pt; color: #3b2a1a; margin: 0 0 6px; }
h2 { font-size: 14pt; color: #8a4b12; border-bottom: 2px solid #e8c9a0; margin: 16px 0 6px; }
h3 { font-size: 11.5pt; margin: 10px 0 4px; }
table { border-collapse: collapse; width: 100%; margin: 6px 0; font-size: 9pt; page-break-inside: auto; }
tr { page-break-inside: avoid; }
td, th { border: 1px solid #d9c3a3; padding: 3px 5px; text-align: left; vertical-align: top; }
th { background: #f6ead8; }
blockquote { background: #fff4e0; border-left: 4px solid #e8590c; margin: 6px 0; padding: 4px 10px; }
code { background: #f3ede4; padding: 0 3px; }
hr { border: none; border-top: 1px dashed #d9c3a3; margin: 12px 0; }
"""


def convertir(ruta_md):
    texto = open(ruta_md, encoding="utf-8").read()
    cuerpo = markdown.markdown(texto, extensions=["tables"])
    base = os.path.splitext(ruta_md)[0]
    html = f'<!doctype html><html lang="es"><head><meta charset="utf-8"><style>{CSS}</style></head>' \
           f'<body>{cuerpo}</body></html>'
    with open(base + ".html", "w", encoding="utf-8") as f:
        f.write(html)
    subprocess.run([CHROME, "--headless", "--no-sandbox", "--disable-gpu", "--no-pdf-header-footer",
                    f"--print-to-pdf={base}.pdf", f"file://{os.path.abspath(base)}.html"],
                   capture_output=True, check=False)
    os.remove(base + ".html")
    return base + ".pdf"


if __name__ == "__main__":
    for r in sys.argv[1:]:
        print(convertir(r))
