# -*- coding: utf-8 -*-
"""Arma GIMNASIO-DE-IDEAS.xlsx (versión 2: con verificación web, fichas a fondo, programa, matriz).
Uso: python -I -X utf8 build_excel2.py <carpeta_salidas> <salida.xlsx>
Lee (todos opcionales): lentes.json, patrones.json, ideas_final.json, fichas.json, programa30.json, matriz.json, lentes_maestras.json, contraste_verif.json"""
import sys, json, re, pathlib, collections
from openpyxl import Workbook
from openpyxl.styles import Alignment, Font, PatternFill, Border, Side
from openpyxl.utils import get_column_letter
from openpyxl.formatting.rule import ColorScaleRule
from openpyxl.worksheet.datavalidation import DataValidation

D = pathlib.Path(sys.argv[1]); OUT = sys.argv[2]
def load(name, default):
    p = D / name
    return json.load(open(p, encoding="utf-8")) if p.exists() else default
lentes = load("lentes.json", {"libros": []}); patr = load("patrones.json", {"patrones": [], "contraste": []})
ideas = load("ideas_final.json", []); fichas = load("fichas.json", []); prog = load("programa30.json", {"dias": []})
matriz = load("matriz.json", {}); maestras = load("lentes_maestras.json", []); cverif = load("contraste_verif.json", {})

HDR_FILL = PatternFill("solid", fgColor="1F3A5F"); HDR_FONT = Font(bold=True, color="FFFFFF", size=11)
WRAP = Alignment(wrap_text=True, vertical="top"); CENTER = Alignment(horizontal="center", vertical="top", wrap_text=True)
THIN = Side(style="thin", color="D9D9D9"); BORDER = Border(left=THIN, right=THIN, top=THIN, bottom=THIN)
FACU_FILL = PatternFill("solid", fgColor="FFF2CC"); VER_FILL = PatternFill("solid", fgColor="E2EFDA")
URL_RE = re.compile(r"https?://[^\s\)\]\>\"'，,;]+")
K = ("innovacion", "factibilidad_facu", "brecha_argentina", "por_que_ahora", "potencial")
wb = Workbook(); fuentes = []

def sheet(title, headers, rows, widths, freeze="B2", facu_cols=(), score_cols=(), center_cols=(), fill_cols=None, landscape=True):
    ws = wb.create_sheet(title[:31]); ws.append(headers)
    for c in range(1, len(headers) + 1):
        cell = ws.cell(row=1, column=c); cell.fill = HDR_FILL; cell.font = HDR_FONT; cell.alignment = CENTER; cell.border = BORDER
        ws.column_dimensions[get_column_letter(c)].width = widths[c - 1] if c - 1 < len(widths) else 18
    ws.row_dimensions[1].height = 42
    for r in rows: ws.append(["" if v is None else v for v in r])
    for ri in range(2, ws.max_row + 1):
        for c in range(1, len(headers) + 1):
            cell = ws.cell(row=ri, column=c); cell.alignment = CENTER if c in center_cols else WRAP; cell.border = BORDER
            if c in facu_cols: cell.fill = FACU_FILL
            elif fill_cols and c in fill_cols: cell.fill = fill_cols[c]
            if isinstance(cell.value, str):
                for u in URL_RE.findall(cell.value): fuentes.append((ws.title, ri, u.rstrip(".")))
    ws.freeze_panes = freeze; ws.auto_filter.ref = ws.dimensions
    for c in score_cols:
        col = get_column_letter(c)
        ws.conditional_formatting.add(f"{col}2:{col}{max(ws.max_row, 2)}", ColorScaleRule(start_type="num", start_value=1, start_color="F8696B", mid_type="num", mid_value=5.5, mid_color="FFEB84", end_type="num", end_value=10, end_color="63BE7B"))
    ws.page_setup.orientation = "landscape" if landscape else "portrait"; ws.page_setup.fitToWidth = 1; ws.page_setup.fitToHeight = 0
    ws.sheet_properties.pageSetUpPr.fitToPage = True; ws.print_title_rows = "1:1"
    return ws

def marca(ws, col_idx, n):
    dv = DataValidation(type="list", formula1='"⭐ me gusta,🤔 tal vez,❌ no,🔁 variar"', allow_blank=True)
    ws.add_data_validation(dv); col = get_column_letter(col_idx); dv.add(f"{col}2:{col}{max(n + 1, 2)}")

def j(lst, sep="\n"): return sep.join(str(x) for x in (lst or []) if x)
def V(i): return i.get("verificacion") or {}
def sc(i, k):
    v = V(i).get("score_ajustado") or i.get("score") or {}
    return float(v.get(k, 0) or 0)
def total(i): return round(sum(sc(i, k) for k in K) / 5, 1)
def viva(i): return i.get("estado_registro") != "repetida" and V(i).get("veredicto") != "descartar"

leeme = wb.active; leeme.title = "LEÉME"
fichas_by = {f.get("id_tmp"): f for f in fichas}
vivas = sorted([i for i in ideas if viva(i)], key=lambda i: (-total(i), i.get("titulo", "")))
muertas = [i for i in ideas if not viva(i)]

# ---------- IDEAS ----------
def comp(i): return j([f"{c.get('nombre')} ({c.get('parecido')}): {c.get('que_hace')} — {c.get('url')}" for c in V(i).get("competidores_argentina") or []])
def fus(i): return j([f"{f.get('id_tmp')} [{f.get('angulo')}]: {f.get('titulo')}. Vuelta: {f.get('vuelta_de_tuerca','')[:400]}" for f in i.get("fusionadas") or []])
COLS = [
    ("#", 5, lambda i, n: n), ("Puntaje /10", 9, lambda i, n: total(i)),
    ("Verificada en web", 12, lambda i, n: "sí (2026-10-19)" if V(i).get("verificada_web") else "no (solo juez)"),
    ("Veredicto", 11, lambda i, n: V(i).get("veredicto", "sin juzgar")),
    ("Título", 30, lambda i, n: i.get("titulo")), ("En una línea", 42, lambda i, n: i.get("una_linea")),
    ("¿Existe en Argentina?", 16, lambda i, n: V(i).get("existe_en_argentina") or i.get("existe_en_argentina")),
    ("Competidores en Argentina", 44, lambda i, n: comp(i)),
    ("Intentos previos (quién lo probó)", 36, lambda i, n: V(i).get("intentos_previos", "")),
    ("Nota del verificador web", 44, lambda i, n: V(i).get("nota_para_facu", "") if V(i).get("verificada_web") else ""),
    ("Ficha a fondo", 14, lambda i, n: "sí: hoja TOP A FONDO" if i.get("id_tmp") in fichas_by else ""),
    ("Ángulo", 18, lambda i, n: i.get("angulo")), ("Patrón", 20, lambda i, n: i.get("patron")), ("Lente", 20, lambda i, n: i.get("lente")),
    ("Problema", 40, lambda i, n: i.get("problema")), ("Cliente que paga", 24, lambda i, n: i.get("cliente_que_paga")),
    ("Modelo de cobro", 24, lambda i, n: i.get("modelo_de_cobro")), ("Vuelta de tuerca", 46, lambda i, n: i.get("vuelta_de_tuerca")),
    ("Qué combina", 30, lambda i, n: j(i.get("componentes_que_combina"), " + ")), ("Por qué ahora", 34, lambda i, n: i.get("por_que_ahora")),
    ("Qué hace la IA", 34, lambda i, n: i.get("que_hace_la_ia")),
    ("Existe afuera", 44, lambda i, n: j([f"{e.get('empresa','')} ({e.get('pais','')}): {e.get('dato','')} — {e.get('fuente','')}" for e in (i.get("existe_afuera") or [])])),
    ("Búsquedas en Argentina (detalle)", 44, lambda i, n: (V(i).get("evidencia_argentina") or "") + ("\n— generador: " + i.get("detalle_argentina", "") if i.get("detalle_argentina") else "")),
    ("Huevo y gallina", 36, lambda i, n: i.get("huevo_gallina")),
    ("Palanca 1 para retorcerla", 30, lambda i, n: (i.get("palancas_para_retorcerla") or [""])[0]),
    ("Palanca 2", 30, lambda i, n: ((i.get("palancas_para_retorcerla") or []) + ["", ""])[1]),
    ("Palanca 3", 30, lambda i, n: ((i.get("palancas_para_retorcerla") or []) + ["", "", ""])[2]),
    ("Primer experimento barato", 36, lambda i, n: i.get("primer_experimento_barato")), ("Riesgos", 34, lambda i, n: i.get("riesgos")),
    ("Innovación", 9, lambda i, n: sc(i, "innovacion")), ("Factibilidad Facu", 9, lambda i, n: sc(i, "factibilidad_facu")),
    ("Brecha Argentina", 9, lambda i, n: sc(i, "brecha_argentina")), ("Por qué ahora (nota)", 9, lambda i, n: sc(i, "por_que_ahora")),
    ("Potencial", 9, lambda i, n: sc(i, "potencial")),
    ("Nota del juez (sin web)", 40, lambda i, n: V(i).get("nota_juez") if V(i).get("verificada_web") else V(i).get("nota_para_facu", "")),
    ("También apareció como (fusionadas)", 40, lambda i, n: fus(i)),
    ("Parecida a (registro)", 34, lambda i, n: j([f"{s.get('id')}: {s.get('nombre')} [{s.get('decision')}]" for s in (i.get("parecidas_confirmadas") or [])]) or i.get("referencia_registro", "")),
    ("Estado vs registro", 12, lambda i, n: i.get("estado_registro", "nueva")),
    ("Marca de Facu", 14, lambda i, n: ""), ("Comentario de Facu", 30, lambda i, n: ""),
]
H = [c[0] for c in COLS]; W = [c[1] for c in COLS]; idx = {h: k + 1 for k, h in enumerate(H)}
rows = [[c[2](i, n) for c in COLS] for n, i in enumerate(vivas, 1)]
ws = sheet("IDEAS", H, rows, W, freeze="F2", facu_cols=(idx["Marca de Facu"], idx["Comentario de Facu"]),
           score_cols=(idx["Puntaje /10"], idx["Innovación"], idx["Factibilidad Facu"], idx["Brecha Argentina"], idx["Por qué ahora (nota)"], idx["Potencial"]),
           center_cols=tuple(idx[h] for h in ("#", "Puntaje /10", "Verificada en web", "Veredicto", "¿Existe en Argentina?", "Ficha a fondo", "Innovación", "Factibilidad Facu", "Brecha Argentina", "Por qué ahora (nota)", "Potencial", "Estado vs registro")),
           fill_cols={idx["Competidores en Argentina"]: VER_FILL, idx["Intentos previos (quién lo probó)"]: VER_FILL, idx["Nota del verificador web"]: VER_FILL})
marca(ws, idx["Marca de Facu"], len(rows))

# ---------- TOP A FONDO ----------
if fichas:
    order = {i["id_tmp"]: n for n, i in enumerate(vivas, 1)}
    FH = ["Puesto general", "Título", "Resumen en 5 líneas", "Quién lo intentó y qué le pasó", "Competencia en Argentina (a fondo)", "Regulación (leída en la fuente)",
          "Números de unidad (estimación marcada)", "Tamaño del mercado (con fuente)", "A quién entrevistar y dónde encontrarlo", "Guion de entrevista (Mom Test)",
          "Experimento de 2 semanas", "Predicción, pérdida máxima y criterio de corte", "Variantes para retorcerla", "Riesgos principales", "Veredicto del investigador", "Fuentes", "Marca de Facu", "Comentario de Facu"]
    frows = []
    for f in sorted(fichas, key=lambda f: order.get(f.get("id_tmp"), 999)):
        e = f.get("experimento") or {}
        frows.append([order.get(f.get("id_tmp"), ""), f.get("titulo"), f.get("resumen"), f.get("quien_lo_intento"), f.get("competencia_argentina"), f.get("regulacion"),
                      f.get("numeros_unidad"), f.get("tamano_mercado"), f.get("a_quien_entrevistar"), j(f.get("guion_entrevista")),
                      j([e.get("hipotesis", ""), "Pasos: " + j(e.get("pasos"), " · ")]), j([f"Predicción: {e.get('prediccion','')}", f"Pérdida máxima: {e.get('perdida_maxima','')}", f"Sigue si: {e.get('criterio_sigue','')}", f"Se corta si: {e.get('criterio_corta','')}"]),
                      j(f.get("variantes")), j(f.get("riesgos")), f.get("veredicto"), j(f.get("fuentes")), "", ""])
    wf = sheet("TOP A FONDO", FH, frows, [8, 28, 46, 46, 44, 40, 40, 36, 36, 50, 46, 40, 40, 36, 36, 60, 14, 30], freeze="C2", facu_cols=(17, 18), center_cols=(1,))
    marca(wf, 17, len(frows))

# ---------- SALIERON ----------
def motivo(i):
    v = V(i)
    if i.get("estado_registro") == "repetida": return "repetida (Regla N.º 2)"
    if i.get("fusionada_en"): return f"duplicada: fusionada en {i['fusionada_en']} (sus palancas y fuentes pasaron a esa ficha)"
    if i.get("duplicada_de"): return f"duplicada de {i['duplicada_de']}"
    if v.get("verificada_web"): return f"descartada por la verificación web: {v.get('nota_para_facu','')}"
    return f"descartada por el juez: {v.get('nota_para_facu','')}"
rows2 = [[i.get("id_tmp"), i.get("titulo"), i.get("una_linea"), i.get("angulo"), motivo(i), comp(i),
          j([f"{s.get('id')}: {s.get('nombre')} [{s.get('decision')}]" for s in (i.get("parecidas_confirmadas") or [])]) or i.get("referencia_registro", "")] for i in muertas]
sheet("SALIERON (repetidas-refutadas)", ["id", "Título", "En una línea", "Ángulo", "Por qué salió", "Competidores encontrados", "Repite o se parece a (registro)"], rows2, [8, 30, 44, 18, 50, 40, 40])

# ---------- CONTRASTE ----------
H3 = ["Sector", "Empresa", "País", "Qué hace", "Modelo de cobro", "Tracción (dato verificable)", "Fuente", "Fecha consulta", "¿Existe en Argentina?", "Verificada en web", "Detalle Argentina", "Barreras en Argentina", "Por qué ahora", "Importabilidad /10", "Versión argentina con vuelta de tuerca", "Chequeo registro", "Marca de Facu", "Comentario de Facu"]
rows3 = []
for s in patr.get("contraste", []):
    for e in s.get("empresas", []):
        cv = cverif.get(f"{s.get('sector')}||{e.get('empresa')}") or {}
        det = (cv.get("detalle") + "\n— antes: " + (e.get("detalle_argentina") or "")) if cv else e.get("detalle_argentina")
        imp = float(cv.get("importabilidad_ajustada", e.get("importabilidad_1_10", 0)) or 0)
        rows3.append([s.get("sector"), e.get("empresa"), e.get("pais"), e.get("que_hace"), e.get("modelo_de_cobro"), e.get("traccion"), e.get("fuente"), e.get("fecha_consulta", "2026-10-18"),
                      cv.get("existe_en_argentina") or e.get("existe_en_argentina"), "sí (2026-10-19)" if cv and cv.get("existe_en_argentina") != "no verificado" else ("intentada, sin cupo de búsqueda" if cv else "no"), det, e.get("barreras_argentina"), e.get("por_que_ahora"), imp,
                      e.get("version_argentina_con_vuelta") + (("\n— nota de verificación: " + cv.get("nota", "")) if cv.get("nota") else ""), e.get("chequeo_registro"), "", ""])
rows3.sort(key=lambda r: -r[13])
ws3 = sheet("CONTRASTE EE.UU.-AR", H3, rows3, [22, 20, 10, 40, 24, 36, 36, 11, 16, 12, 44, 36, 30, 10, 48, 28, 14, 30], freeze="C2", facu_cols=(17, 18), score_cols=(14,), center_cols=(3, 8, 9, 10, 14))
marca(ws3, 17, len(rows3))
sheet("LECTURA POR SECTOR", ["Sector", "Lectura del sector (qué se repite afuera y qué falta en Argentina)"], [[s.get("sector"), s.get("lectura_del_sector")] for s in patr.get("contraste", [])], [26, 120])

# ---------- PATRONES ----------
H4 = ["Tipo", "Patrón", "Cómo funciona", "Cuándo funciona", "Casos reales (empresa, país: dato — fuente)", "Cómo muere", "Truco para el huevo y la gallina / arrancar sin plata", "Ejemplo argentino", "Preguntas generadoras", "¿Encaja con Facu?"]
rows4 = []; combos = []
for k, p in enumerate(patr.get("patrones", [])):
    tipo = "Intermediación" if k == 0 else "Paquete / servicio integrado"
    for x in p.get("patrones", []):
        rows4.append([tipo, x.get("nombre"), x.get("como_funciona"), x.get("cuando_funciona"), j([f"{c.get('empresa')} ({c.get('pais')}): {c.get('dato_de_traccion')} — {c.get('fuente')}" for c in x.get("casos_reales", [])]),
                      x.get("como_muere"), x.get("truco_huevo_gallina"), x.get("ejemplo_argentino"), j(x.get("preguntas_generadoras")), x.get("encaja_con_facu")])
    combos += [[tipo, c] for c in p.get("como_combinar_patrones", [])]
sheet("PATRONES", H4, rows4, [16, 24, 40, 36, 50, 36, 40, 30, 44, 36], freeze="C2")
sheet("COMBINAR PATRONES", ["Tipo", "Combinación que genera un modelo nuevo"], combos, [22, 120])

# ---------- MATRIZ ----------
if matriz.get("filas"):
    cols = matriz["columnas"]; MH = ["Patrón"] + cols + ["Total"]
    mrows = [[f["patron"]] + [f["celdas"].get(c, "") for c in cols] + [f.get("total", "")] for f in matriz["filas"]]
    wm = sheet("MATRIZ PATRÓN×SECTOR", MH, mrows, [30] + [22] * len(cols) + [8], freeze="B2")
    GAP = PatternFill("solid", fgColor="FCE4D6"); HIT = PatternFill("solid", fgColor="DDEBF7")
    for ri in range(2, wm.max_row + 1):
        for ci in range(2, len(cols) + 2):
            v = str(wm.cell(row=ri, column=ci).value or "")
            if v.startswith("HUECO"): wm.cell(row=ri, column=ci).fill = GAP
            elif v: wm.cell(row=ri, column=ci).fill = HIT
    if matriz.get("lectura"):
        sheet("LECTURA DE LA MATRIZ", ["Hallazgo"], [[x] for x in matriz["lectura"]], [140])

# ---------- LENTES ----------
if maestras:
    sheet("LENTES MAESTRAS", ["#", "Lente", "Qué mirar", "Pregunta que te hacés", "De qué libros sale"], [[n, m.get("lente"), m.get("que_mirar"), m.get("pregunta"), m.get("libros")] for n, m in enumerate(maestras, 1)], [5, 28, 60, 50, 40], freeze="C2", center_cols=(1,))
if prog.get("dias"):
    wp = sheet("PROGRAMA 30 DÍAS", ["Día", "Lente", "Libro", "Dónde mirarla (tu vida real)", "Ejercicio (15-20 min)", "Qué anotar en la bitácora", "Pregunta del día", "Hecho", "Lo que vi"],
               [[d.get("dia"), d.get("lente"), d.get("libro"), d.get("donde_mirar"), d.get("ejercicio"), d.get("que_anotar"), d.get("pregunta"), "", ""] for d in prog["dias"]], [6, 26, 22, 40, 46, 40, 40, 8, 40], freeze="C2", facu_cols=(8, 9), center_cols=(1, 8))
    dvh = DataValidation(type="list", formula1='"✔"', allow_blank=True); wp.add_data_validation(dvh); dvh.add(f"H2:H{len(prog['dias']) + 1}")
H5 = ["Libro", "Lente", "Qué mirar", "Pregunta generadora", "Ejemplo Argentina 2026", "Referencia en el libro", "Tipo de idea que produce"]
rows5 = []; sem = []; adv = []
for b in lentes.get("libros", []):
    for l in b.get("lentes", []): rows5.append([b.get("libro"), l.get("nombre"), l.get("que_mirar"), l.get("pregunta_generadora"), l.get("ejemplo_argentina_2026"), l.get("referencia"), l.get("tipo_de_idea_que_produce")])
    for s in b.get("ideas_semilla", []): sem.append([b.get("libro"), s.get("titulo"), s.get("problema"), s.get("cliente_que_paga"), s.get("vuelta_de_tuerca"), s.get("lente_usada"), s.get("lanzable_como_web"), s.get("chequeo_registro"), "", ""])
    for a in b.get("advertencias_para_facu", []): adv.append([b.get("libro"), b.get("tesis_en_una_linea"), a, b.get("cita_corta", "")])
sheet("LENTES (libros)", H5, rows5, [26, 24, 44, 40, 44, 22, 18], freeze="C2")
ws6 = sheet("SEMILLAS (libros)", ["Libro", "Idea semilla", "Problema", "Cliente que paga", "Vuelta de tuerca", "Lente usada", "Lanzable como web / qué hace la IA", "Chequeo registro", "Marca de Facu", "Comentario de Facu"], sem, [26, 28, 40, 24, 40, 22, 40, 30, 14, 30], freeze="C2", facu_cols=(9, 10))
marca(ws6, 9, len(sem))
sheet("ADVERTENCIAS (libros)", ["Libro", "Tesis del libro en una línea", "Advertencia para Facu", "Cita corta"], adv, [26, 44, 70, 40])

# ---------- FUENTES ----------
seen = set(); frows = []
for h, r, u in fuentes:
    if (h, u) in seen: continue
    seen.add((h, u)); frows.append([h, r, u])
sheet("FUENTES", ["Hoja", "Fila", "URL"], frows, [26, 8, 110], freeze="A2")

# ---------- LEÉME ----------
ver = [i for i in vivas if V(i).get("verificada_web")]
ex = collections.Counter(V(i).get("existe_en_argentina") or i.get("existe_en_argentina") for i in vivas)
cver = sum(1 for r in rows3 if r[9].startswith("sí"))
leeme.column_dimensions["A"].width = 120
hojas = [ws.title for ws in wb.worksheets]
texto = [
    ("GIMNASIO DE IDEAS — versión 2 (2026-10-19)", True),
    ("Pedido de Facu: material para aprender a VER negocios. Lentes de sus libros de startup, patrones de intermediación y de paquete, contraste de empresas que funcionan afuera y no existen en Argentina, y fichas de ideas lanzables como web para retorcer. No es una lista para elegir una idea hoy: es para entrenar el ojo.", False),
    ("", False), ("QUÉ CAMBIÓ EN LA VERSIÓN 2", True),
    (f"Verificación web en Argentina de {len(ver)} de {len(vivas)} ideas vivas (columnas verdes de la hoja IDEAS: competidores, intentos previos y nota del verificador). Contraste: {cver} de {len(rows3)} empresas re-verificadas. " + ("Fichas a fondo de las mejores en la hoja TOP A FONDO. " if fichas else "") + ("Programa de 30 días de lentes, matriz patrón×sector y lentes maestras imprimibles. " if prog.get("dias") else "") + "Las duplicadas se fusionaron en su mejor versión (columna 'También apareció como').", False),
    ("", False), ("CÓMO USARLO", True),
    ("1) LENTES MAESTRAS (12 formas de mirar que aparecen en 3 o más libros; imprimible) y PROGRAMA 30 DÍAS (una lente por día, dónde mirarla en tu vida real y qué anotar). 2) PATRONES, COMBINAR PATRONES y MATRIZ PATRÓN×SECTOR: los moldes y dónde hay huecos. 3) CONTRASTE EE.UU.-AR y LECTURA POR SECTOR. 4) IDEAS ordenadas por puntaje y TOP A FONDO. 5) Marcá en las columnas amarillas (⭐ me gusta, 🤔 tal vez, ❌ no, 🔁 variar) y anotá tu vuelta de tuerca en 'Comentario de Facu'.", False),
    ("", False), ("PUNTAJES (1-10, opinión, no dato)", True),
    ("Innovación, Factibilidad Facu (lanzable sin programar, con Claude, no-code y ~USD 1.300), Brecha Argentina (10 = no hay nada acá), Por qué ahora (qué lo hace posible recién en 2025-2026) y Potencial. Puntaje /10 = promedio simple. Primero los puso el generador, después un juez sin web, y en las verificadas los ajustó un verificador con búsquedas reales en Argentina.", False),
    ("", False), ("REGLAS QUE SE RESPETARON", True),
    ("Regla N.º 1 (nada inventado): cada empresa o cifra lleva fuente y fecha; 'no verificado' significa exactamente eso. Regla N.º 2 (no repetir): cada idea se cruzó contra el registro (automático + juez); las repetidas y duplicadas están en SALIERON con su referencia.", False),
    ("", False), ("CONTEOS", True),
    (f"Ideas vivas: {len(vivas)} · salieron: {len(muertas)} · verificadas en web: {len(ver)} · ¿existe en Argentina?: " + ", ".join(f"{k}: {v}" for k, v in ex.most_common()), False),
    (f"Empresas en el contraste: {len(rows3)} · patrones: {len(rows4)} · lentes: {len(rows5)} · semillas: {len(sem)} · fichas a fondo: {len(fichas)} · URLs de fuentes: {len(frows)}", False),
    ("", False), ("HOJAS", True), (" · ".join(hojas), False),
]
for k, (t, bold) in enumerate(texto, 1):
    c = leeme.cell(row=k, column=1, value=t); c.alignment = WRAP; c.font = Font(bold=bold, size=12 if bold else 11, color="1F3A5F" if bold else "000000")
# ---------- copiar marcas de Facu de la versión anterior ----------
CLAVES = {"IDEAS": ("Título",), "TOP A FONDO": ("Título",), "CONTRASTE EE.UU.-AR": ("Sector", "Empresa"), "SEMILLAS (libros)": ("Libro", "Idea semilla")}
copiadas = 0
if len(sys.argv) > 3 and pathlib.Path(sys.argv[3]).exists():
    from openpyxl import load_workbook
    prev = load_workbook(sys.argv[3], read_only=True)
    for name, keys in CLAVES.items():
        if name not in prev.sheetnames or name not in wb.sheetnames: continue
        rows_p = list(prev[name].iter_rows(values_only=True))
        if not rows_p: continue
        hp = list(rows_p[0]); ki = [hp.index(k) for k in keys if k in hp]
        mi = [hp.index(h) for h in ("Marca de Facu", "Comentario de Facu") if h in hp]
        if len(ki) != len(keys) or len(mi) != 2: continue
        marcas = {tuple(r[k] for k in ki): (r[mi[0]], r[mi[1]]) for r in rows_p[1:] if any(r[m] not in (None, "") for m in mi)}
        if not marcas: continue
        wsn = wb[name]; hn = [c.value for c in wsn[1]]; kn = [hn.index(k) + 1 for k in keys]; mn = [hn.index("Marca de Facu") + 1, hn.index("Comentario de Facu") + 1]
        for ri in range(2, wsn.max_row + 1):
            m = marcas.get(tuple(wsn.cell(row=ri, column=c).value for c in kn))
            if m:
                wsn.cell(row=ri, column=mn[0]).value = m[0]; wsn.cell(row=ri, column=mn[1]).value = m[1]; copiadas += 1
print(f"marcas de Facu copiadas de la versión anterior: {copiadas}")
wb.save(OUT)
print(f"OK {OUT}: {len(vivas)} vivas ({len(ver)} verificadas), {len(muertas)} salieron, {len(rows3)} empresas ({cver} re-verificadas), {len(fichas)} fichas, {len(frows)} fuentes; hojas: {len(hojas)}")
