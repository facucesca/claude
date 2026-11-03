# Crea la hoja "Fase 2" en TODAS-LAS-IDEAS.xlsx (pedido de Facu, 2026-10-09):
#   Bloque A = ideas propias de Facu (L1-L10 + A3), copiadas de la hoja "Ideas de Facu" (análisis del 2026-10-08).
#   Bloque B = las 33 ideas que Facu marcó (amarillo/celeste) en la hoja "Ideas".
# Después borra la hoja "Ideas de Facu" porque queda contenida entera en "Fase 2".
# No toca la hoja "Ideas" (preserva las marcas de Facu).
import math, sys
from openpyxl import load_workbook
from openpyxl.styles import Font, Alignment, PatternFill, Border, Side
from openpyxl.utils import get_column_letter
from openpyxl.worksheet.datavalidation import DataValidation

P = r"C:\FACU\IDEAS-PRUEBA\TODAS-LAS-IDEAS.xlsx"
try:
    open(P, "r+b").close()
except PermissionError:
    sys.exit("LOCKED: cerrá el Excel y volvé a correr")

wb = load_workbook(P)
src_a = wb["Ideas de Facu"]
src_b = wb["Ideas"]

thin = Side(style="thin", color="BFBFBF")
border = Border(left=thin, right=thin, top=thin, bottom=thin)
HDR = PatternFill("solid", fgColor="1F3864")
YELLOW = PatternFill("solid", fgColor="FFFF00")
CELESTE = PatternFill("solid", fgColor="00B0F0")
F = "Arial"


def nlines(v, w):
    return sum(max(1, math.ceil(len(p) / max(4, int(w * 1.15)))) for p in str(v or "").split("\n"))


def header(ws, row, cols):
    for ci, (h, w) in enumerate(cols, 1):
        c = ws.cell(row=row, column=ci, value=h)
        c.font = Font(name=F, bold=True, color="FFFFFF", size=10)
        c.fill = HDR
        c.border = border
        c.alignment = Alignment(wrap_text=True, vertical="center", horizontal="center")
    ws.row_dimensions[row].height = 48


def title(ws, row, text, sub):
    ws.cell(row=row, column=1, value=text).font = Font(name=F, bold=True, size=13, color="1F3864")
    ws.cell(row=row + 1, column=1, value=sub).font = Font(name=F, size=10, italic=True)


if "Fase 2" in wb.sheetnames:
    del wb["Fase 2"]
ws = wb.create_sheet("Fase 2", 1)

# Anchos: el bloque A manda (19 columnas); el bloque B usa las mismas columnas con otros anchos razonables
WIDTHS = [10, 40, 46, 11, 9, 8, 11, 10, 11, 11, 10, 46, 46, 32, 42, 38, 22, 12, 30]
for ci, w in enumerate(WIDTHS, 1):
    ws.column_dimensions[get_column_letter(ci)].width = w

r = 1
ws.cell(row=r, column=1, value="FASE 2 — Ideas guardadas para más adelante").font = Font(name=F, bold=True, size=15, color="1F3864")
r += 1
ws.cell(row=r, column=1, value="Hoja creada el 2026-10-09 a pedido de Facu: acá quedan sus ideas propias y las que marcó en el Excel, en pausa por el momento.").font = Font(name=F, size=10)
r += 2

# ---------- Bloque A: ideas propias (copiadas de "Ideas de Facu") ----------
title(ws, r, "A. Ideas propias de Facu (libreta y notas)", "Analizadas a fondo el 2026-10-08. Puntajes = OPINIÓN de Claude fundada en datos (detalle en research/2026-10-08-ideas-de-facu-analisis.md).")
r += 2
a_cols = [(src_a.cell(row=1, column=ci).value, WIDTHS[ci - 1]) for ci in range(1, src_a.max_column + 1)]
header(ws, r, a_cols)
a_first = r + 1
r += 1
for sr in range(2, src_a.max_row + 1):
    code = src_a.cell(row=sr, column=1).value
    if not code or str(code).startswith("Notas") or str(code).startswith("Hoja") or str(code).startswith("Puntajes") or str(code).startswith("Las columnas"):
        continue
    mx = 1
    for ci in range(1, src_a.max_column + 1):
        v = src_a.cell(row=sr, column=ci).value
        c = ws.cell(row=r, column=ci, value=v)
        c.font = Font(name=F, size=10, bold=(ci in (1, 4)))
        c.border = border
        centered = 4 <= ci <= 11 or ci in (1, 18)
        c.alignment = Alignment(wrap_text=True, vertical="top", horizontal="center" if centered else None)
        if ci == 4:
            c.number_format = "0.0"
        mx = max(mx, nlines(v, WIDTHS[ci - 1]))
    ws.row_dimensions[r].height = min(409, max(30, mx * 12.6 + 4))
    r += 1
a_last = r - 1
dva = DataValidation(type="list", formula1='"Sí,Tal vez,No"', allow_blank=True)
ws.add_data_validation(dva)
dva.add(f"R{a_first}:R{a_last}")
r += 2

# ---------- Bloque B: marcadas en la hoja "Ideas" ----------
hdr_b = [src_b.cell(row=1, column=ci).value for ci in range(1, src_b.max_column + 1)]
idx = {h: i for i, h in enumerate(hdr_b)}


def col(name_start):
    for h, i in idx.items():
        if h and str(h).startswith(name_start):
            return i
    raise KeyError(name_start)


ix = {
    "codigo": col("Código"), "gusta": col("Me gusta"), "nombre": col("Nombre"), "cat": col("Categoría"),
    "tipo": col("Tipo de negocio"), "mod": col("Modalidad"), "merc": col("Mercado"), "exp": col("Qué es"),
    "t1": col("Tiempo al primer"), "precio": col("Precio"), "cap": col("Capital"), "riesgo": col("Riesgos"),
    "score": col("Score"), "estado": col("Estado"), "fuente": col("Informe fuente"), "notas": col("Mis notas"),
}
b_cols = [("Código", 0), ("Nombre", 0), ("Qué es (explicación del estudio)", 0), ("Score del informe (1-10)", 0),
          ("Marca de Facu", 0), ("Nota de Facu", 0), ("Categoría", 0), ("Tipo de negocio", 0), ("Modalidad", 0),
          ("Mercado", 0), ("Tiempo al primer dólar", 0), ("Precio / ticket", 0), ("Capital inicial", 0),
          ("Riesgos principales", 0), ("Estado en la investigación", 0), ("Informe fuente", 0),
          ("Mis notas", 0)]
b_cols = [(h, WIDTHS[i]) for i, (h, _) in enumerate(b_cols)]

title(ws, r, "B. Ideas del Excel que Facu marcó (33)", "Copiadas de la hoja «Ideas» (marcas amarillas y celeste de Facu). Datos de los estudios 2026-09-02 a 2026-10-02, no re-verificados.")
r += 2
header(ws, r, b_cols)
r += 1
count = 0
for row in src_b.iter_rows(min_row=2):
    color = None
    for c in row:
        if c.fill and c.fill.fill_type and c.fill.fgColor.type == "rgb":
            if c.fill.fgColor.rgb == "FF00B0F0":
                color = "Celeste"
            elif c.fill.fgColor.rgb == "FFFFFF00" and color is None:
                color = "Amarillo"
    if not color:
        continue
    g = lambda k: row[ix[k]].value
    nota = g("gusta")
    nota = None if nota in (None, "Sí", "Tal vez", "No") else nota
    vals = [g("codigo"), g("nombre"), g("exp"), g("score"), color, nota, g("cat"), g("tipo"), g("mod"),
            g("merc"), g("t1"), g("precio"), g("cap"), g("riesgo"), g("estado"), g("fuente"), g("notas")]
    mx = 1
    for ci, v in enumerate(vals, 1):
        c = ws.cell(row=r, column=ci, value=v)
        c.font = Font(name=F, size=10, bold=(ci in (1, 2)))
        c.border = border
        c.alignment = Alignment(wrap_text=True, vertical="top", horizontal="center" if ci in (1, 4, 5) else None)
        if ci == 5:
            c.fill = CELESTE if color == "Celeste" else YELLOW
        mx = max(mx, nlines(v, WIDTHS[ci - 1]))
    ws.row_dimensions[r].height = min(409, max(30, mx * 12.6 + 4))
    r += 1
    count += 1

ws.freeze_panes = "B1"

# La hoja "Ideas de Facu" queda contenida entera en el bloque A
del wb["Ideas de Facu"]
wb.save(P)

wb2 = load_workbook(P)
w2 = wb2["Ideas"]
marcadas = sum(1 for row in w2.iter_rows(min_row=2)
               if any(c.fill and c.fill.fill_type and c.fill.fgColor.type == "rgb"
                      and c.fill.fgColor.rgb in ("FFFFFF00", "FF00B0F0") for c in row))
print("hojas:", wb2.sheetnames, "| bloque A:", a_last - a_first + 1, "| bloque B:", count,
      "| marcas intactas en 'Ideas':", marcadas)
