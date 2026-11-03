# -*- coding: utf-8 -*-
"""Une la investigación de los agentes con las marcas de Facu y arma MARCAS-DE-FACU.xlsx (versión 2: ordenado, filtrable, con opinión y variantes).
Uso: python -I -X utf8 build_excel_final.py <carpeta_scratch_marcas> <salida.xlsx>
Entrada: todas-las-filas.json (lotes) + res-XX.json (agentes) + marcas-todas.json (puntajes de la v1)"""
import sys, json, glob, re, pathlib, statistics, collections
from openpyxl import Workbook
from openpyxl.styles import Alignment, Font, PatternFill, Border, Side
from openpyxl.formatting.rule import ColorScaleRule
from openpyxl.worksheet.datavalidation import DataValidation
from openpyxl.utils import get_column_letter

SC = pathlib.Path(sys.argv[1]); OUT = sys.argv[2]; HERE = pathlib.Path(__file__).parent
filas = json.load(open(SC / "todas-las-filas.json", encoding="utf-8"))
res = {}
for f in sorted(glob.glob(str(SC / "res-*.json"))):
    try:
        for x in json.load(open(f, encoding="utf-8")): res[x["n"]] = x
    except Exception as e: print("ERROR leyendo", f, e)
res2 = {}
for f in sorted(glob.glob(str(SC / "p2-res-*.json"))):
    try:
        for x in json.load(open(f, encoding="utf-8")): res2[x["n"]] = x
    except Exception as e: print("ERROR leyendo", f, e)
por_n = {f["n"]: f for f in filas}
TEMAS = ["Stock y depósito", "Logística y reparto", "Cámaras, sensores y hardware", "Software e IA para PyMEs", "Marketplace o intermediario", "Educación y trabajo", "Salud y cuidado", "Comida y alimentos", "Hogar, obra y barrio", "Agro e industria", "Trámites, seguros y finanzas", "Video y contenido con IA", "Otro"]
TIPOS = ["Producto web o app", "Marketplace o intermediario", "Hardware más software", "Servicio con personas", "Contenido o infoproducto", "Datos o información"]
ETAPAS = ["Empezar ya", "Probar barato", "Reserva para etapa 2", "Combinar con otra", "Pausar por ahora"]
# sesgo por lote: si un investigador puntúa mucho más alto o bajo que el resto, se corrige la mitad de la diferencia
lote_de = {}
for f in sorted(glob.glob(str(SC / "lote-*.json"))):
    for x in json.load(open(f, encoding="utf-8")): lote_de[x["n"]] = pathlib.Path(f).stem
dif_lote = collections.defaultdict(list)
for n, x in res.items():
    try: dif_lote[lote_de[n]].append(float(x["puntuacion"]) - float(por_n[n]["puntuacion_previa"]))
    except Exception: pass
media_global = statistics.mean(d for l in dif_lote.values() for d in l) if dif_lote else 0
sesgo = {l: statistics.mean(d) - media_global for l, d in dif_lote.items()}
rows = []
for f in filas:
    x = res.get(f["n"]); prev = float(f["puntuacion_previa"])
    if x:
        inv = float(x["puntuacion"]); inv_corr = inv - 0.5 * sesgo.get(lote_de.get(f["n"]), 0)
        base = 0.5 * inv_corr + 0.5 * prev
        y = res2.get(f["n"])
        final = round(max(1.0, min(10.0, (0.5 * float(y["puntuacion_revisada"]) + 0.5 * base) if y else base)), 1)
    else:
        inv = None; final = prev
    rows.append(dict(f=f, x=x, y=res2.get(f["n"]), inv=inv, final=final, prev=prev))
rows.sort(key=lambda r: (-r["final"], -(r["inv"] or 0), r["f"]["codigo"]))
cod = {f["n"]: f["codigo"] for f in filas}
def agr(x):
    if not x: return ""
    return ", ".join(cod.get(a, a) for a in (x.get("agrupar_con") or []))
def T(v):
    if isinstance(v, list): return chr(10).join("• " + str(i) for i in v)
    if isinstance(v, dict): return chr(10).join(f"{k}: {T(x)}" for k, x in v.items())
    return "" if v is None else v
def lista(v): return "\n".join(f"• {s}" for s in (v or []))
def ty(r, k): return T((r["y"] or {}).get(k, "")) if r.get("y") else ""
def tx(r, k): return T((r["x"] or {}).get(k, "")) if r["x"] else ""

HDR_FILL = PatternFill("solid", fgColor="1F3A5F"); HDR_FONT = Font(bold=True, color="FFFFFF", size=11)
WRAP = Alignment(wrap_text=True, vertical="top"); CEN = Alignment(horizontal="center", vertical="top", wrap_text=True)
THIN = Side(style="thin", color="D9D9D9"); BORDER = Border(left=THIN, right=THIN, top=THIN, bottom=THIN)
FACU = PatternFill("solid", fgColor="FFF2CC")
wb = Workbook(); ws = wb.active; ws.title = "Mis ideas"
COLS = [("Ideas", 70, lambda r: f"[{r['f']['origen']}] {r['f']['idea']}"), ("Anotaciones de Facu", 70, lambda r: r["f"]["anotaciones_de_facu"]),
        ("Puntuación (1 a 10)", 14, lambda r: r["final"]), ("Mi opinión", 70, lambda r: tx(r, "opinion") or "(sin investigar)"), ("Veredicto tras investigar a fondo", 46, lambda r: ty(r, "veredicto")),
        ("Variantes posibles", 62, lambda r: lista(tx(r, "variantes"))), ("Lo que averigüé", 62, lambda r: tx(r, "hallazgos")),
        ("Tema", 22, lambda r: tx(r, "tema")), ("Tipo", 22, lambda r: tx(r, "tipo")), ("Etapa sugerida", 20, lambda r: tx(r, "etapa")), ("Dificultad", 11, lambda r: tx(r, "dificultad")),
        ("Plata para probar (estimación)", 20, lambda r: tx(r, "plata_para_probar")), ("Primer paso", 46, lambda r: tx(r, "primer_paso")), ("Riesgo principal", 40, lambda r: tx(r, "riesgo_principal")),
        ("Se agrupa con", 26, lambda r: agr(r["x"])), ("Por qué ese puntaje", 46, lambda r: tx(r, "por_que_puntuacion")),
        ("Puntaje a fondo", 11, lambda r: round(float(r["y"]["puntuacion_revisada"]), 1) if r.get("y") else ""), ("Puntaje del investigador", 13, lambda r: round(r["inv"], 1) if r["inv"] is not None else ""), ("Puntaje anterior (2026-10-21)", 13, lambda r: r["prev"]),
        ("Tu clasificación", 16, lambda r: ""), ("Tu comentario nuevo", 40, lambda r: "")]
ws.append([c[0] for c in COLS])
for c in range(1, len(COLS) + 1):
    cell = ws.cell(1, c); cell.fill = HDR_FILL; cell.font = HDR_FONT; cell.alignment = CEN; cell.border = BORDER
    ws.column_dimensions[get_column_letter(c)].width = COLS[c - 1][1]
ws.row_dimensions[1].height = 44
for r in rows: ws.append([c[2](r) for c in COLS])
IDX = {c[0]: k + 1 for k, c in enumerate(COLS)}
for ri in range(2, ws.max_row + 1):
    for ci in range(1, len(COLS) + 1):
        cell = ws.cell(ri, ci); cell.border = BORDER; cell.alignment = CEN if ci in (3, 8, 9, 10, 11, 12, 17, 18, 19) else WRAP
        if ci in (IDX["Tu clasificación"], IDX["Tu comentario nuevo"]): cell.fill = FACU
    ws.cell(ri, 3).number_format = "0.0"; ws.cell(ri, 3).font = Font(bold=True, size=12)
ws.freeze_panes = "B2"; ws.auto_filter.ref = ws.dimensions
col = get_column_letter(3)
ws.conditional_formatting.add(f"{col}2:{col}{ws.max_row}", ColorScaleRule(start_type="num", start_value=3, start_color="F8696B", mid_type="num", mid_value=6, mid_color="FFEB84", end_type="num", end_value=9, end_color="63BE7B"))
def dv(lista_, col_name):
    d = DataValidation(type="list", formula1='"' + ",".join(lista_) + '"', allow_blank=True); ws.add_data_validation(d); L = get_column_letter(IDX[col_name]); d.add(f"{L}2:{L}{ws.max_row}")
dv(["⭐ Empezar", "🤔 Evaluar", "🔁 Variar", "⏸ Reserva", "❌ Descartar"], "Tu clasificación")
ws.page_setup.orientation = "landscape"; ws.page_setup.fitToWidth = 1; ws.page_setup.fitToHeight = 0; ws.sheet_properties.pageSetUpPr.fitToPage = True; ws.print_title_rows = "1:1"

# ---------- A fondo ----------
if res2:
    wa = wb.create_sheet("A fondo"); AH = ["Idea", "Puntuación", "Veredicto", "Quién lo intentó", "Competencia en Argentina", "Regulación", "Números de unidad", "Mercado", "Variante que recomiendo probar", "A quién entrevistar", "Preguntas de entrevista", "Experimento de dos semanas", "Por qué cambió el puntaje", "Fuentes", "Tu clasificación", "Tu comentario nuevo"]
    wa.append(AH)
    for c in range(1, len(AH) + 1):
        cell = wa.cell(1, c); cell.fill = HDR_FILL; cell.font = HDR_FONT; cell.alignment = CEN; cell.border = BORDER
    for r in rows:
        y = r.get("y")
        if not y: continue
        e = y.get("experimento") or {}
        exp = chr(10).join(filter(None, [f"Hipótesis: {e.get('hipotesis','')}", f"Predicción: {e.get('prediccion','')}", f"Pérdida máxima: {e.get('perdida_maxima','')}", f"Duración: {e.get('duracion','')}", "Pasos: " + " · ".join(e.get("pasos") or []), f"Sigue si: {e.get('sigue_si','')}", f"Se corta si: {e.get('se_corta_si','')}"]))
        wa.append([f"[{r['f']['origen']}] {r['f']['idea']}", r["final"], T(y.get("veredicto")), T(y.get("quien_lo_intento")), T(y.get("competencia")), T(y.get("regulacion")), T(y.get("numeros")), T(y.get("mercado")), T(y.get("variante_recomendada")), T(y.get("entrevistar_a")), lista(y.get("preguntas_entrevista")), exp, T(y.get("por_que_revisada")), chr(10).join(str(u) for u in (y.get("fuentes") or [])), "", ""])
    for k, w in enumerate((56, 12, 40, 46, 46, 40, 42, 36, 46, 38, 52, 56, 40, 50, 16, 36), 1): wa.column_dimensions[get_column_letter(k)].width = w
    for ri in range(2, wa.max_row + 1):
        for ci in range(1, len(AH) + 1):
            cell = wa.cell(ri, ci); cell.border = BORDER; cell.alignment = CEN if ci == 2 else WRAP
            if ci >= 15: cell.fill = FACU
        wa.cell(ri, 2).number_format = "0.0"; wa.cell(ri, 2).font = Font(bold=True, size=12)
    wa.freeze_panes = "B2"; wa.auto_filter.ref = wa.dimensions
    wa.conditional_formatting.add(f"B2:B{wa.max_row}", ColorScaleRule(start_type="num", start_value=3, start_color="F8696B", mid_type="num", mid_value=6, mid_color="FFEB84", end_type="num", end_value=9, end_color="63BE7B"))
    d2 = DataValidation(type="list", formula1='"⭐ Empezar,🤔 Evaluar,🔁 Variar,⏸ Reserva,❌ Descartar"', allow_blank=True); wa.add_data_validation(d2); d2.add(f"O2:O{wa.max_row}")

# ---------- Resumen por tema ----------
w2 = wb.create_sheet("Resumen por tema")
w2.append(["Tema", "Ideas", "Puntuación promedio", "Mejor idea del tema", "Puntuación de la mejor", "Empezar ya o probar barato"])
for c in range(1, 7):
    cell = w2.cell(1, c); cell.fill = HDR_FILL; cell.font = HDR_FONT; cell.alignment = CEN
por_tema = collections.defaultdict(list)
for r in rows: por_tema[tx(r, "tema") or "Sin investigar"].append(r)
for t, lst in sorted(por_tema.items(), key=lambda kv: -statistics.mean(r["final"] for r in kv[1])):
    mejor = max(lst, key=lambda r: r["final"])
    w2.append([t, len(lst), round(statistics.mean(r["final"] for r in lst), 1), mejor["f"]["idea"][:110], mejor["final"], sum(1 for r in lst if tx(r, "etapa") in ("Empezar ya", "Probar barato"))])
for k, w in enumerate((30, 8, 14, 90, 14, 18), 1): w2.column_dimensions[get_column_letter(k)].width = w
for ri in range(2, w2.max_row + 1):
    for ci in range(1, 7): w2.cell(ri, ci).alignment = WRAP if ci in (1, 4) else CEN; w2.cell(ri, ci).border = BORDER
w2.freeze_panes = "A2"

# ---------- Cómo puntué ----------
w3 = wb.create_sheet("Cómo puntué")
tex = [("CÓMO SE PUNTUÓ (opinión de Claude y de los investigadores, 2026-10-23; no es dato)", True),
       ("Puntuación = mitad lo que opina el investigador que revisó la idea hoy y mitad la puntuación anterior (2026-10-21). En las 60 mejores hubo una segunda investigación más profunda: ahí la mitad del número es la nota de esa segunda pasada y la otra mitad el promedio de las dos anteriores. La hoja «A fondo» las trae completas.", False),
       ("El investigador puntuó de 1 a 10 con estos factores: demanda probable, hueco verificado en Argentina, si se puede construir sin programar y con poca plata, si es producto global o trabajo a medida, regulación y riesgo, ventaja tuya (ingeniería industrial, CEMEVA, agro) y la evidencia que hay. Un 8 o más es excepcional.", False),
       ("La puntuación anterior mezclaba 7 criterios de encaje con lo estudiado antes (indagación del 2026-10-15, estudios de nichos, verificación del gimnasio). Está en la columna «Puntaje anterior».", False),
       ("Como cada investigador revisó un lote distinto, corregí la mitad de la diferencia si un lote puntuó mucho más alto o más bajo que el resto.", False),
       ("", False), ("COSAS QUE TENÉS QUE SABER", True),
       ("Ninguna idea fue validada con clientes. Lo que más puede cambiar un puntaje es hablar con 5 o 10 personas que tengan el problema.", False),
       ("Los hallazgos de hoy tienen fuente y fecha entre corchetes. Lo que dice «no verificado» no se pudo confirmar. Que una búsqueda no encuentre algo no prueba que no exista.", False),
       ("Una diferencia de menos de 0,5 entre dos ideas no significa nada. Sirve para ordenar la lectura, no para decidir.", False),
       ("Las columnas Tema, Tipo, Etapa sugerida y Dificultad son para que filtres. Las dos últimas columnas amarillas son tuyas.", False),
       ("No se borró ninguna idea. Las que figuran como «Pausar por ahora» siguen en la lista.", False)]
w3.column_dimensions["A"].width = 140
for k, (t, b) in enumerate(tex, 1):
    c = w3.cell(k, 1, t); c.alignment = WRAP; c.font = Font(bold=b, size=12 if b else 11, color="1F3A5F" if b else "000000")
wb.save(OUT)
json.dump([dict(n=r["f"]["n"], codigo=r["f"]["codigo"], final=r["final"], previo=r["prev"], investigador=r["inv"], **{k: (r["x"] or {}).get(k) for k in ("tema", "tipo", "etapa", "dificultad", "plata_para_probar", "primer_paso", "riesgo_principal")}) for r in rows],
          open(HERE / "marcas-v2-resumen.json", "w", encoding="utf-8"), ensure_ascii=False, indent=1)
sin = [r["f"]["n"] for r in rows if not r["x"]]
print(f"A fondo: {len(res2)} ideas")
print(f"OK {OUT}: {len(rows)} filas · investigadas {len(rows) - len(sin)} · sin investigar {sin}")
print("sesgo por lote:", {l: round(v, 2) for l, v in sorted(sesgo.items())})
print("etapas:", dict(collections.Counter(tx(r, 'etapa') for r in rows))); print("temas:", dict(collections.Counter(tx(r, 'tema') for r in rows)))
