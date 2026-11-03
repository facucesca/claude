# -*- coding: utf-8 -*-
"""Arma el Excel GIMNASIO-DE-IDEAS.xlsx a partir de los JSON de los agentes.
Uso: python -I build_excel.py <carpeta_salidas> <salida.xlsx>
Espera en carpeta_salidas: lentes.json, patrones.json, ideas_final.json (todos opcionales; arma con lo que haya).
"""
import sys, json, re, pathlib
from openpyxl import Workbook
from openpyxl.styles import Alignment, Font, PatternFill, Border, Side
from openpyxl.utils import get_column_letter
from openpyxl.formatting.rule import ColorScaleRule
from openpyxl.worksheet.datavalidation import DataValidation

D = pathlib.Path(sys.argv[1]); OUT = sys.argv[2]
def load(name, default):
    p = D / name
    return json.load(open(p, encoding="utf-8")) if p.exists() else default
lentes = load("lentes.json", {"libros": []})
patr = load("patrones.json", {"patrones": [], "contraste": []})
ideas = load("ideas_final.json", [])

HDR_FILL = PatternFill("solid", fgColor="1F3A5F"); HDR_FONT = Font(bold=True, color="FFFFFF", size=11)
WRAP = Alignment(wrap_text=True, vertical="top"); CENTER = Alignment(horizontal="center", vertical="top", wrap_text=True)
THIN = Side(style="thin", color="D9D9D9"); BORDER = Border(left=THIN, right=THIN, top=THIN, bottom=THIN)
FACU_FILL = PatternFill("solid", fgColor="FFF2CC")
URL_RE = re.compile(r"https?://[^\s\)\]\>\"']+")

wb = Workbook()
fuentes = []  # (hoja, fila, url)

def sheet(title, headers, rows, widths, freeze="B2", facu_cols=(), score_cols=(), center_cols=()):
    ws = wb.create_sheet(title)
    ws.append(headers)
    for c in range(1, len(headers) + 1):
        cell = ws.cell(row=1, column=c); cell.fill = HDR_FILL; cell.font = HDR_FONT; cell.alignment = CENTER; cell.border = BORDER
        ws.column_dimensions[get_column_letter(c)].width = widths[c - 1] if c - 1 < len(widths) else 18
    ws.row_dimensions[1].height = 42
    for r in rows:
        ws.append(["" if v is None else v for v in r])
    for ri in range(2, ws.max_row + 1):
        for c in range(1, len(headers) + 1):
            cell = ws.cell(row=ri, column=c); cell.alignment = CENTER if c in center_cols else WRAP; cell.border = BORDER
            if c in facu_cols: cell.fill = FACU_FILL
            if isinstance(cell.value, str):
                for u in URL_RE.findall(cell.value): fuentes.append((title, ri, u))
    ws.freeze_panes = freeze
    ws.auto_filter.ref = ws.dimensions
    for c in score_cols:
        col = get_column_letter(c)
        ws.conditional_formatting.add(f"{col}2:{col}{max(ws.max_row, 2)}", ColorScaleRule(start_type="num", start_value=1, start_color="F8696B", mid_type="num", mid_value=5.5, mid_color="FFEB84", end_type="num", end_value=10, end_color="63BE7B"))
    return ws

def marca_validation(ws, col_letter, n):
    dv = DataValidation(type="list", formula1='"⭐ me gusta,🤔 tal vez,❌ no,🔁 variar"', allow_blank=True)
    ws.add_data_validation(dv); dv.add(f"{col_letter}2:{col_letter}{max(n + 1, 2)}")

def j(lst, sep="\n"):
    return sep.join(str(x) for x in (lst or []) if x)

# ---------- LEÉME (se completa al final con conteos) ----------
leeme = wb.active; leeme.title = "LEÉME"

# ---------- IDEAS ----------
def sc(idea, k):
    v = (idea.get("verificacion") or {}).get("score_ajustado") or {}
    if isinstance(v.get(k), (int, float)): return float(v[k])
    s = idea.get("score") or {}
    return float(s.get(k, 0) or 0)
def total(idea):
    return round(sum(sc(idea, k) for k in ("innovacion", "factibilidad_facu", "brecha_argentina", "por_que_ahora", "potencial")) / 5, 1)

vivas = [i for i in ideas if i.get("estado_registro") != "repetida" and (i.get("verificacion") or {}).get("veredicto") != "descartar"]
muertas = [i for i in ideas if i not in vivas]
vivas.sort(key=lambda i: (-total(i), i.get("titulo", "")))
H = ["#", "Puntaje /10", "Veredicto verificación", "Título", "En una línea", "Ángulo", "Patrón", "Lente", "Problema", "Cliente que paga", "Modelo de cobro", "Vuelta de tuerca", "Qué combina", "Por qué ahora", "Qué hace la IA", "Existe afuera (verificado)", "¿Existe en Argentina?", "Detalle Argentina", "Huevo y gallina", "Palanca 1 para retorcerla", "Palanca 2", "Palanca 3", "Primer experimento barato", "Riesgos", "Innovación", "Factibilidad Facu", "Brecha Argentina", "Por qué ahora (nota)", "Potencial", "Nota del verificador", "Parecida a (registro)", "Estado vs registro", "Marca de Facu", "Comentario de Facu"]
rows = []
for n, i in enumerate(vivas, 1):
    v = i.get("verificacion") or {}
    ea = j([f"{e.get('empresa','')} ({e.get('pais','')}): {e.get('dato','')} — {e.get('fuente','')}" for e in (i.get("existe_afuera") or [])])
    pal = (i.get("palancas_para_retorcerla") or []) + ["", "", ""]
    rows.append([n, total(i), v.get("veredicto", "sin verificar"), i.get("titulo"), i.get("una_linea"), i.get("angulo"), i.get("patron"), i.get("lente"), i.get("problema"), i.get("cliente_que_paga"), i.get("modelo_de_cobro"), i.get("vuelta_de_tuerca"), j(i.get("componentes_que_combina"), " + "), i.get("por_que_ahora"), i.get("que_hace_la_ia"), ea, v.get("existe_en_argentina") or i.get("existe_en_argentina"), (v.get("evidencia_argentina") or "") + ("\n— generador: " + i.get("detalle_argentina", "") if i.get("detalle_argentina") else ""), i.get("huevo_gallina"), pal[0], pal[1], pal[2], i.get("primer_experimento_barato"), i.get("riesgos"), sc(i, "innovacion"), sc(i, "factibilidad_facu"), sc(i, "brecha_argentina"), sc(i, "por_que_ahora"), sc(i, "potencial"), v.get("nota_para_facu", ""), j([f"{s.get('id')}: {s.get('nombre')} [{s.get('decision')}]" for s in (i.get("parecidas_confirmadas") or [])]) or i.get("referencia_registro", ""), i.get("estado_registro", "nueva"), "", ""])
W = [5, 9, 14, 28, 40, 18, 18, 18, 40, 24, 22, 44, 30, 34, 34, 44, 16, 44, 36, 30, 30, 30, 36, 34, 9, 9, 9, 9, 9, 40, 34, 12, 14, 30]
ws = sheet("IDEAS", H, rows, W, freeze="E2", facu_cols=(33, 34), score_cols=(2, 25, 26, 27, 28, 29), center_cols=(1, 2, 3, 17, 25, 26, 27, 28, 29, 32))
marca_validation(ws, "AG", len(rows))

# ---------- REPETIDAS / DESCARTADAS ----------
H2 = ["Título", "En una línea", "Ángulo", "Por qué salió", "Repite o se parece a (registro)", "Dato nuevo que aporta"]
rows2 = []
for i in muertas:
    v = i.get("verificacion") or {}
    rows2.append([i.get("titulo"), i.get("una_linea"), i.get("angulo"), "repetida (Regla N.º 2)" if i.get("estado_registro") == "repetida" else f"descartada en verificación: {v.get('nota_para_facu','')}", j([f"{s.get('id')}: {s.get('nombre')} [{s.get('decision')}]" for s in (i.get("parecidas_confirmadas") or [])]) or i.get("referencia_registro", ""), v.get("evidencia_argentina") or v.get("evidencia_afuera") or ""])
sheet("SALIERON (repetidas-refutadas)", H2, rows2, [30, 44, 18, 40, 40, 44])

# ---------- CONTRASTE ----------
H3 = ["Sector", "Empresa", "País", "Qué hace", "Modelo de cobro", "Tracción (dato verificable)", "Fuente", "Fecha consulta", "¿Existe en Argentina?", "Detalle Argentina", "Barreras en Argentina", "Por qué ahora", "Importabilidad /10", "Versión argentina con vuelta de tuerca", "Chequeo registro", "Marca de Facu", "Comentario de Facu"]
rows3 = []
for s in patr.get("contraste", []):
    for e in sorted(s.get("empresas", []), key=lambda x: -float(x.get("importabilidad_1_10", 0) or 0)):
        rows3.append([s.get("sector"), e.get("empresa"), e.get("pais"), e.get("que_hace"), e.get("modelo_de_cobro"), e.get("traccion"), e.get("fuente"), e.get("fecha_consulta", "2026-10-18"), e.get("existe_en_argentina"), e.get("detalle_argentina"), e.get("barreras_argentina"), e.get("por_que_ahora"), float(e.get("importabilidad_1_10", 0) or 0), e.get("version_argentina_con_vuelta"), e.get("chequeo_registro"), "", ""])
rows3.sort(key=lambda r: -r[12])
ws3 = sheet("CONTRASTE EE.UU.-AR", H3, rows3, [22, 20, 10, 40, 24, 36, 36, 11, 16, 40, 36, 30, 10, 48, 28, 14, 30], freeze="C2", facu_cols=(16, 17), score_cols=(13,), center_cols=(3, 8, 9, 13))
marca_validation(ws3, "P", len(rows3))
H3b = ["Sector", "Lectura del sector (qué se repite afuera y qué falta en Argentina)"]
sheet("LECTURA POR SECTOR", H3b, [[s.get("sector"), s.get("lectura_del_sector")] for s in patr.get("contraste", [])], [26, 120])

# ---------- PATRONES ----------
H4 = ["Tipo", "Patrón", "Cómo funciona", "Cuándo funciona", "Casos reales (empresa, país: dato — fuente)", "Cómo muere", "Truco para el huevo y la gallina / arrancar sin plata", "Ejemplo argentino", "Preguntas generadoras", "¿Encaja con Facu?"]
rows4 = []; combos = []
for k, p in enumerate(patr.get("patrones", [])):
    tipo = "Intermediación" if k == 0 else "Paquete / servicio integrado"
    for x in p.get("patrones", []):
        casos = j([f"{c.get('empresa')} ({c.get('pais')}): {c.get('dato_de_traccion')} — {c.get('fuente')}" for c in x.get("casos_reales", [])])
        rows4.append([tipo, x.get("nombre"), x.get("como_funciona"), x.get("cuando_funciona"), casos, x.get("como_muere"), x.get("truco_huevo_gallina"), x.get("ejemplo_argentino"), j(x.get("preguntas_generadoras")), x.get("encaja_con_facu")])
    combos += [[tipo, c] for c in p.get("como_combinar_patrones", [])]
sheet("PATRONES", H4, rows4, [16, 24, 40, 36, 50, 36, 40, 30, 44, 36], freeze="C2")
sheet("COMBINAR PATRONES", ["Tipo", "Combinación que genera un modelo nuevo"], combos, [22, 120])

# ---------- LENTES ----------
H5 = ["Libro", "Lente", "Qué mirar", "Pregunta generadora", "Ejemplo Argentina 2026", "Referencia en el libro", "Tipo de idea que produce"]
rows5 = []; sem = []; adv = []
for b in lentes.get("libros", []):
    for l in b.get("lentes", []):
        rows5.append([b.get("libro"), l.get("nombre"), l.get("que_mirar"), l.get("pregunta_generadora"), l.get("ejemplo_argentina_2026"), l.get("referencia"), l.get("tipo_de_idea_que_produce")])
    for s in b.get("ideas_semilla", []):
        sem.append([b.get("libro"), s.get("titulo"), s.get("problema"), s.get("cliente_que_paga"), s.get("vuelta_de_tuerca"), s.get("lente_usada"), s.get("lanzable_como_web"), s.get("chequeo_registro"), "", ""])
    for a in b.get("advertencias_para_facu", []):
        adv.append([b.get("libro"), b.get("tesis_en_una_linea"), a, b.get("cita_corta", "")])
sheet("LENTES (libros)", H5, rows5, [26, 24, 44, 40, 44, 22, 18], freeze="C2")
ws6 = sheet("SEMILLAS (libros)", ["Libro", "Idea semilla", "Problema", "Cliente que paga", "Vuelta de tuerca", "Lente usada", "Lanzable como web / qué hace la IA", "Chequeo registro", "Marca de Facu", "Comentario de Facu"], sem, [26, 28, 40, 24, 40, 22, 40, 30, 14, 30], freeze="C2", facu_cols=(9, 10))
marca_validation(ws6, "I", len(sem))
sheet("ADVERTENCIAS (libros)", ["Libro", "Tesis del libro en una línea", "Advertencia para Facu", "Cita corta"], adv, [26, 44, 70, 40])

# ---------- FUENTES ----------
seen = set(); frows = []
for h, r, u in fuentes:
    if (h, u) in seen: continue
    seen.add((h, u)); frows.append([h, r, u])
sheet("FUENTES", ["Hoja", "Fila", "URL"], frows, [26, 8, 110], freeze="A2")

# ---------- LEÉME ----------
leeme.column_dimensions["A"].width = 120
texto = [
    ("GIMNASIO DE IDEAS — 2026-10-18", True),
    ("Pedido de Facu: material para aprender a VER negocios: lentes de los libros de startup, patrones de intermediación y de paquete, contraste de empresas que funcionan afuera y no existen en Argentina, y fichas de ideas lanzables como web para retorcer. No es una lista para elegir una idea hoy: es para entrenar el ojo.", False),
    ("", False),
    ("CÓMO USARLO", True),
    ("1) Empezá por LENTES (libros): cada fila es una forma de mirar + una pregunta para hacerte frente a cualquier negocio. 2) Seguí con PATRONES y COMBINAR PATRONES: son los moldes de Uber, Airbnb, Faire, Sunrun, etc. 3) CONTRASTE EE.UU.-AR: empresas con tracción verificada afuera y qué pasa en Argentina. 4) IDEAS: las fichas, ordenadas por puntaje; filtrá por Ángulo, Patrón o ¿Existe en Argentina?. 5) Marcá en las columnas amarillas (Marca de Facu: ⭐ me gusta, 🤔 tal vez, ❌ no, 🔁 variar) y anotá tu vuelta de tuerca en Comentario de Facu.", False),
    ("", False),
    ("QUÉ SIGNIFICAN LOS PUNTAJES (1-10, opinión de los agentes, ajustada por un verificador independiente cuando dice 'mantener' o 'bajar')", True),
    ("Innovación: cuánto se aparta de lo que ya existe. Factibilidad Facu: qué tan lanzable es sin programar, con Claude, no-code y ~USD 1.300. Brecha Argentina: cuánto falta acá (10 = no encontramos nada). Por qué ahora: qué tan fuerte es la razón de que sea posible recién en 2025-2026. Potencial: tamaño si funciona. Puntaje /10 = promedio simple de los cinco.", False),
    ("", False),
    ("REGLAS QUE SE RESPETARON", True),
    ("Regla N.º 1 (nada inventado): cada empresa o cifra lleva fuente y fecha; donde dice 'no verificado' es porque no se pudo confirmar. Los puntajes son opinión, no dato. Regla N.º 2 (no repetir): cada idea se cruzó contra el registro de 1.402 ideas anteriores (automático por palabras + juez). Las que repetían salieron a la hoja SALIERON; las parecidas a una idea que Facu ya eligió quedaron marcadas en 'Parecida a (registro)'.", False),
    ("", False),
    ("CONTEOS", True),
    (f"Ideas vivas: {len(vivas)} · salieron (repetidas o refutadas): {len(muertas)} · nuevas: {sum(1 for i in vivas if i.get('estado_registro','nueva')=='nueva')} · parecidas a una elegida: {sum(1 for i in vivas if i.get('estado_registro')=='parecida')} · verificadas: {sum(1 for i in vivas if (i.get('verificacion') or {}).get('veredicto'))}", False),
    (f"Empresas en el contraste: {len(rows3)} · patrones: {len(rows4)} · lentes: {len(rows5)} · ideas semilla de libros: {len(sem)} · URLs de fuentes: {len(frows)}", False),
    ("", False),
    ("ADVERTENCIA HONESTA", True),
    ("Los marketplaces genéricos son de los negocios más difíciles (el huevo y la gallina): por eso cada ficha dice cómo arrancaría con un solo lado o con una herramienta de un solo jugador. Que algo 'no exista en Argentina' puede significar oportunidad o que ya se intentó y murió: antes de enamorarte, buscá quién lo intentó.", False),
]
for k, (t, bold) in enumerate(texto, 1):
    c = leeme.cell(row=k, column=1, value=t); c.alignment = WRAP; c.font = Font(bold=bold, size=12 if bold else 11, color="1F3A5F" if bold else "000000")

wb.save(OUT)
print(f"OK {OUT}: {len(vivas)} ideas vivas, {len(muertas)} salieron, {len(rows3)} empresas, {len(rows4)} patrones, {len(rows5)} lentes, {len(sem)} semillas, {len(frows)} fuentes")
