import json, glob, math, os, re, sys
from openpyxl import Workbook
from openpyxl.styles import Font, Alignment, PatternFill, Border, Side
from openpyxl.worksheet.datavalidation import DataValidation
from openpyxl.utils import get_column_letter

SCR = os.path.dirname(os.path.abspath(__file__))
OUT = r"C:\FACU\IDEAS-PRUEBA\TODAS-LAS-IDEAS.xlsx"

rows = []
# Fuente única: JSON consolidado al lado de este script (editar ahí y volver a correr).
with open(os.path.join(SCR, "2026-10-02-todas-las-ideas.json"), encoding="utf-8") as fh:
    for i, d in enumerate(json.load(fh)):
        d["_file"] = f"{i:05d}"  # conserva el orden del JSON
        rows.append(d)

# orden: archivo (cronológico) y luego código natural
def natkey(code):
    m = re.match(r"([A-Za-z]+)(\d*)([a-z]*)", str(code))
    if not m:
        return (str(code), 0, "")
    return (m.group(1), int(m.group(2) or 0), m.group(3))
rows.sort(key=lambda d: d["_file"])

def g(d, k, default="sin dato"):
    v = d.get(k)
    if v is None or (isinstance(v, str) and not v.strip()):
        return default
    return v

COLS = [
    # (header, key/func, width, kind)
    ("Nº", None, 6, "n"),
    ("Código", "id", 9, "t"),
    ("Me gusta\n(Sí / Tal vez / No)", None, 12, "t"),
    ("Nombre", "nombre", 32, "t"),
    ("Categoría", "categoria", 20, "t"),
    ("Tipo de negocio\n(servicio, producto…)", "tipo_negocio", 22, "t"),
    ("Modalidad", "modalidad", 12, "t"),
    ("A quién se le vende", "cliente", 28, "t"),
    ("Mercado", "mercado", 13, "t"),
    ("Qué es y por qué (explicación)", "explicacion", 62, "t"),
    ("Cómo se llevaría a cabo", "como_se_hace", 62, "t"),
    ("Tiempo al primer dólar", "tiempo_primer_dolar", 18, "t"),
    ("Días aprox. al 1er dólar\n(para ordenar)", "dias_primer_dolar", 13, "int"),
    ("Precio / ticket", "precio", 22, "t"),
    ("Capital inicial", "capital_inicial", 16, "t"),
    ("Horas por semana", "horas_semana", 16, "t"),
    ("% del público en Argentina que lo necesitaría y pagaría\n(estimación)", "pct_argentina", 16, "pct"),
    ("Base del % (universo y razonamiento)", "pct_argentina_base", 40, "t"),
    ("Cómo se cobra desde Argentina", "cobro_desde_ar", 24, "t"),
    ("Riesgos principales", "riesgos", 40, "t"),
    ("Score del informe\n(1-10)", "score", 10, "num"),
    ("Estado", "estado", 16, "t"),
    ("Estudio", "estudio", 30, "t"),
    ("Informe fuente (en la carpeta del proyecto)", "fuente", 36, "t"),
    ("Mis notas", None, 30, "t"),
]

FONT = "Arial"
thin = Side(style="thin", color="BFBFBF")
border = Border(left=thin, right=thin, top=thin, bottom=thin)
hdr_fill = PatternFill("solid", fgColor="1F3864")
hdr_font = Font(name=FONT, bold=True, color="FFFFFF", size=10)
body_font = Font(name=FONT, size=10)
grey_font = Font(name=FONT, size=10, color="808080")
wrap_top = Alignment(wrap_text=True, vertical="top")
center_top = Alignment(wrap_text=True, vertical="top", horizontal="center")

wb = Workbook()

# ---------------- Hoja Ideas ----------------
ws = wb.active
ws.title = "Ideas"
for ci, (h, _, w, _) in enumerate(COLS, 1):
    c = ws.cell(row=1, column=ci, value=h)
    c.font = hdr_font; c.fill = hdr_fill; c.border = border
    c.alignment = Alignment(wrap_text=True, vertical="center", horizontal="center")
    ws.column_dimensions[get_column_letter(ci)].width = w
ws.row_dimensions[1].height = 54

def est_lines(text, width):
    if text is None:
        return 1
    s = str(text)
    cpl = max(4, int(width * 1.15))
    return sum(max(1, math.ceil(len(part) / cpl)) for part in s.split("\n"))

for ri, d in enumerate(rows, 2):
    descartada = str(g(d, "estado", "")).lower().startswith("descartada")
    max_lines = 1
    for ci, (h, key, w, kind) in enumerate(COLS, 1):
        if ci == 1:
            val = ri - 1
        elif key is None:
            val = None
        else:
            val = g(d, key, None if kind in ("int", "num", "pct") else "sin dato")
        if kind == "int" and val is not None:
            try: val = int(val)
            except Exception: val = None
        if kind == "num" and val is not None:
            try: val = float(str(val).replace(",", "."))
            except Exception: val = None
        if kind == "pct" and val is not None:
            try: val = float(str(val).replace("%", "").replace(",", ".")) / 100.0
            except Exception: val = None
        c = ws.cell(row=ri, column=ci, value=val)
        c.font = grey_font if descartada else body_font
        c.border = border
        c.alignment = center_top if kind in ("n", "int", "num", "pct") or ci in (2, 3) else wrap_top
        if kind == "pct": c.number_format = "0%"
        if kind == "num": c.number_format = "0.0"
        if kind == "t":
            max_lines = max(max_lines, est_lines(val, w))
    ws.row_dimensions[ri].height = min(409, max(30, max_lines * 12.6 + 4))

last = len(rows) + 1
ws.freeze_panes = "E2"
ws.auto_filter.ref = f"A1:{get_column_letter(len(COLS))}{last}"
dv = DataValidation(type="list", formula1='"Sí,Tal vez,No"', allow_blank=True)
ws.add_data_validation(dv)
dv.add(f"C2:C{last}")

# ---------------- Hoja Cómo leer ----------------
gl = wb.create_sheet("Cómo leer", 0)
gl.column_dimensions["A"].width = 34
gl.column_dimensions["B"].width = 100
title = Font(name=FONT, bold=True, size=14, color="1F3864")
bold = Font(name=FONT, bold=True, size=10)
r = 1
gl.cell(row=r, column=1, value="TODAS LAS IDEAS DEL PROYECTO IDEAS-PRUEBA").font = title; r += 1
gl.cell(row=r, column=1, value="Generado el 2026-10-02 a partir de todos los estudios del proyecto (2026-09-02 a 2026-10-02).").font = body_font; r += 2

def kv(k, v):
    global r
    a = gl.cell(row=r, column=1, value=k); a.font = bold; a.alignment = wrap_top
    b = gl.cell(row=r, column=2, value=v); b.font = body_font; b.alignment = wrap_top
    gl.row_dimensions[r].height = max(15, est_lines(v, 100) * 12.6 + 2)
    r += 1

gl.cell(row=r, column=1, value="Cómo usar esta planilla").font = Font(name=FONT, bold=True, size=12, color="1F3864"); r += 1
kv("1. Leé la hoja «Ideas»", "Una fila por idea. Las columnas Código y Nombre quedan fijas al desplazarte. Cada fila se entiende sola: qué es, cómo se haría, cuánto tarda el primer dólar, cuánta demanda habría en Argentina, riesgos y estado.")
kv("2. Marcá las que te gustan", "Pintá la fila (o la celda del nombre) de AMARILLO. Ninguna celda trae color de fondo, así que tu amarillo se va a ver claro. Opcional: en la columna «Me gusta» elegí Sí / Tal vez / No del desplegable y usá «Mis notas» para comentarios. Con el filtro de la columna podés ver solo las marcadas.")
kv("3. Filtrá y ordená", "Todas las columnas tienen filtro (flechita del encabezado). Ejemplos: Tipo de negocio = Servicio; Mercado = Argentina; ordenar por «Días aprox. al 1er dólar» de menor a mayor; ordenar por «% Argentina» de mayor a menor; Estado = Recomendada / Top.")
kv("Filas en gris", "Ideas descartadas o marcadas como trampa por la investigación. Se dejan para que veas por qué se descartaron.")
r += 1
gl.cell(row=r, column=1, value="Qué significa cada columna").font = Font(name=FONT, bold=True, size=12, color="1F3864"); r += 1
kv("Tipo de negocio", "Servicio (hacés un trabajo para un cliente) · Servicio productizado (precio y alcance fijos, como un paquete) · Abono / suscripción de servicio (pago mensual recurrente) · Producto digital (plantilla, kit, archivo que se vende muchas veces) · Infoproducto / curso · Software / SaaS (programa que se usa por suscripción) · Contenido / medios (canal, newsletter que se monetiza) · Comercio / reventa · Producto físico · Afiliación / comisión · Trabajo por hora / empleo · Híbrido.")
kv("Modalidad", "Activo = requiere tu tiempo continuo. Semi-pasivo = mucho trabajo al principio y después camina casi solo. Pasivo = la compu/IA hace casi todo en régimen.")
kv("Tiempo al primer dólar", "Cuánto tarda en entrar la primera plata COBRADA (no solo ganada). Ojo: plataformas como Fiverr, Mercado Libre o Workana retienen el dinero días o semanas.")
kv("Días aprox. al 1er dólar", "Número para ordenar de la más rápida a la más lenta. 999 = no aplica (idea descartada sin ingreso posible, o un método y no un negocio). Cuando el informe no traía el dato, el texto de «Tiempo al primer dólar» (y también precio, capital u horas) empieza con «Estimación:».")
kv("% del público en Argentina", "ESTIMACIÓN PROPIA (no es un dato medido): de cada 100 potenciales clientes del universo indicado en «Base del %», cuántos hoy necesitan esto Y estarían dispuestos/podrían pagarlo, considerando la cultura y la economía argentina 2026 (sensibilidad al precio, desconfianza a pagar intangibles, informalidad, WhatsApp y trato cara a cara, Mercado Libre/Mercado Pago dominantes, inflación, industria en contracción, dificultad para pagar en USD). Sirve para comparar ideas entre sí, no como pronóstico. Para ideas pensadas para clientes del exterior, el % de Argentina suele ser bajo a propósito.")
kv("Score del informe", "Puntaje 1-10 que le dio cada investigación PARA VOS (no para el mercado en general). Los criterios cambian un poco entre estudios: en las «Rápidas 1 semana» pesa la velocidad de cobro; en los de largo plazo, la rentabilidad y durabilidad. Usalo como orientación, no como verdad.")
kv("Estado", "Recomendada / Top = estuvo en el top de su estudio · Evaluada · Descartada / trampa · En cartera (proyecto) = proyectos ya planificados.")
kv("Informe fuente", "Archivo con el detalle completo y las fuentes (links y fechas) dentro de C:\\FACU\\IDEAS-PRUEBA.")
r += 1
gl.cell(row=r, column=1, value="Advertencias").font = Font(name=FONT, bold=True, size=12, color="1F3864"); r += 1
kv("Ideas repetidas", "Algunas ideas aparecen en más de un estudio con otro ángulo (ej. Claude Skills, estudios contables, avance de obra, white-label para agencias). Se dejaron todas: cada una tiene un enfoque distinto.")
kv("Precios", "Muchos precios del rubro vienen de blogs de las propias agencias/herramientas: tomarlos como techo, no como mediana. Un recién llegado suele cobrar 30-50% de eso al principio.")
kv("No programar", "Desde el 2026-10-01 sabemos que no programás: las ideas de software tienen más riesgo para vos (ver columna Riesgos).")
r += 1
gl.cell(row=r, column=1, value="Resumen (se calcula solo)").font = Font(name=FONT, bold=True, size=12, color="1F3864"); r += 1
rng = lambda col: f"Ideas!${col}$2:${col}${last}"
gl.cell(row=r, column=1, value="Total de ideas").font = bold
gl.cell(row=r, column=2, value=f"=COUNTA({rng('B')})").font = body_font; r += 1
for est in ["Recomendada / Top", "Evaluada", "Descartada / trampa", "En cartera (proyecto)"]:
    gl.cell(row=r, column=1, value=f"Estado: {est}").font = body_font
    gl.cell(row=r, column=2, value=f'=COUNTIF({rng("V")},"{est}")').font = body_font; r += 1
gl.cell(row=r, column=1, value="Marcadas «Sí» en Me gusta").font = body_font
gl.cell(row=r, column=2, value=f'=COUNTIF({rng("C")},"Sí")').font = body_font; r += 1
r += 1
gl.cell(row=r, column=1, value="Por tipo de negocio").font = bold; r += 1
for t in sorted({str(g(d, "tipo_negocio")) for d in rows}):
    gl.cell(row=r, column=1, value=t).font = body_font
    gl.cell(row=r, column=2, value=f'=COUNTIF({rng("F")},"{t}")').font = body_font; r += 1
r += 1
gl.cell(row=r, column=1, value="Por categoría").font = bold; r += 1
for t in sorted({str(g(d, "categoria")) for d in rows}):
    gl.cell(row=r, column=1, value=t).font = body_font
    gl.cell(row=r, column=2, value=f'=COUNTIF({rng("E")},"{t}")').font = body_font; r += 1
for row in gl.iter_rows(min_row=1, max_row=r):
    for c in row:
        if c.column == 2 and isinstance(c.value, str) and c.value.startswith("="):
            c.alignment = Alignment(horizontal="left")

wb.active = 0
from openpyxl.workbook.properties import CalcProperties
wb.calculation = CalcProperties(fullCalcOnLoad=True)
wb.save(OUT)
print("filas:", len(rows), "->", OUT)
