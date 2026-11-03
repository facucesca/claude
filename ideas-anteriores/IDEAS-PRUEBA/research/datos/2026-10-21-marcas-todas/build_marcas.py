# -*- coding: utf-8 -*-
"""Junta TODO lo que Facu marcó en los Excel del proyecto (más sus ideas propias) y lo puntúa.
Salida: MARCAS-DE-FACU.xlsx (raíz del proyecto) + marcas-todas.json (datos).
Uso: python -I -X utf8 research/datos/2026-10-21-marcas-todas/build_marcas.py
Fuentes: TODAS-LAS-IDEAS.xlsx (Fase 2 y Orden de Claude), research/datos/2026-10-15-comentarios-facu-orden.json,
NICHOS-Y-PROBLEMAS-2.xlsx (hoja Problemas), GIMNASIO-DE-IDEAS.xlsx (hoja IDEAS, colores), ideas/LISTA-DE-IDEAS.md (ideas propias)."""
import json, re, pathlib
from openpyxl import load_workbook, Workbook
from openpyxl.styles import Alignment, Font, PatternFill, Border, Side
from openpyxl.formatting.rule import ColorScaleRule
from openpyxl.utils import get_column_letter

R = pathlib.Path(__file__).resolve().parents[3]
CRIT = ("G", "P", "M", "H", "C", "R", "V")
filas = []

def add(origen, codigo, idea, anot, g, p, m, h, c, r, v, fuente_pts, ajuste=0.0, motivo_ajuste="", E=5.0, E_fuente="sin estudio: valor neutro 5,0"):
    tot = g + p + m + h + c + r + v
    s7 = tot / 35 * 10
    score = round(max(1.0, min(10.0, 0.5 * s7 + 0.5 * E + ajuste)), 1)
    filas.append(dict(origen=origen, codigo=codigo, idea=idea.strip(), anot=anot.strip(), G=g, P=p, M=m, H=h, C=c, R=r, V=v,
                      total35=tot, puntaje_7_criterios=round(s7, 2), evidencia=round(E, 2), evidencia_fuente=E_fuente, ajuste=ajuste, motivo_ajuste=motivo_ajuste, puntos_de=fuente_pts, score=score))

def clamp(x, lo=1, hi=5): return max(lo, min(hi, int(round(x))))

# ---------- 1) Fase 2 (74) con puntajes de "Orden de Claude" ----------
wb = load_workbook(R / "TODAS-LAS-IDEAS.xlsx", read_only=True)
orden = {}
rows = list(wb["Orden de Claude"].iter_rows(values_only=True))
hdr = next(k for k, r in enumerate(rows) if r[0] == "Puesto")
H = [str(x or "") for x in rows[hdr]]
for r in rows[hdr + 1:]:
    if not r[0]: continue
    d = dict(zip(H, r)); orden[str(d["Código"]).strip()] = dict(d, extra=r[16] if len(r) > 16 else None)
f2 = list(wb["Fase 2"].iter_rows(values_only=True))
blk = None; hdrs = {}; f2rows = {}
for r in f2:
    f = r[0]
    if isinstance(f, str) and f.startswith(("A. ", "B. ", "C. ", "D. ")): blk = f[0]; continue
    if isinstance(f, str) and f.startswith("Código"): hdrs[blk] = [str(x or "").replace("\n", " ") for x in r]; continue
    if f and blk and not (isinstance(f, str) and len(f) > 40): f2rows[str(f).strip()] = dict(zip(hdrs[blk], r), _b=blk)
jn = json.load(open(R / "research/datos/2026-10-15-comentarios-facu-orden.json", encoding="utf-8"))
notas_orden = {x["codigo"]: x.get("nota_facu") for x in jn["orden_de_claude"] if x.get("nota_facu") and x["nota_facu"].strip() not in ("", "/")}
BLK = {"A": "Ideas propias (libreta)", "B": "Excel de 633 ideas", "C": "Excel de nichos 1", "D": "Ideas nuevas (chat y nichos 1)"}
AJ = {"EDU-5-3": (-0.4, "Preply y Classgap ya operan en Argentina cobrando en pesos (verificado por agentes 2026-10-19): baja el hueco"),
      "L1": (0.3, "El contraste re-verificado (2026-10-19) no encontró ningún cierre seguro de autos entre particulares en Argentina"),
      "LOG-1-4": (-0.6, "Facu escribió «/» el 2026-10-15 y no la pintó (no pasó); sin estudio a fondo"), "L15": (-1.5, "Facu la descartó el 2026-10-14"), "L3": (-0.8, "Plataformas castigan lo 100% automático (estudio 2026-10-08)"), "L2": (-0.6, "Ya existe gratis en al menos 5 apps (estudio 2026-10-08)")}
EXTRA_NOTA = {"LOG-1-4": "En «Orden de Claude» (2026-10-15) escribió «/» y no la pintó: se tomó como que no pasa, a confirmar con Facu.", "L15": "Facu (chat, 2026-10-14): \"medio rebuscado, no creo que funcione\". La descartó él.",
              "L2": "Sin comentario. Estado del estudio 2026-10-08: descartada por ahora.", "L3": "Sin comentario. Estado del estudio 2026-10-08: descartada."}
DEEP = {"EDU-5-3": 18, "I29": 17, "ALI-4-4": 18, "F17": 17, "SER-4-4": 16, "T19": 16, "L6": 15, "L11": 12, "COM-3-5": 16.5, "L14": 16.5, "L9 + L5": 16.5, "C34": 16.5, "K11": 16.5, "X1d": 16.5, "C14": 17, "LOG-3-4": 17}
def evidencia(cod, fr):
    if cod in DEEP: return DEEP[cod] / 25 * 10, "Indagación a fondo del 2026-10-15 (5 filtros, sobre 25)"
    if fr.get("Total /25 (investigadores)"): return float(fr["Total /25 (investigadores)"]) / 25 * 10, "Total /25 de los investigadores (nichos 1)"
    if fr.get("Score del informe (1-10)"): return float(fr["Score del informe (1-10)"]), "Score del informe (estudios de septiembre y octubre)"
    if fr.get("Puntaje (promedio simple)"): return float(fr["Puntaje (promedio simple)"]), "Puntaje del análisis a fondo de ideas propias (2026-10-08)"
    if cod == "L12": return 5.4, "Tomado de L10, de la que es variante"
    if cod == "L15": return 3.0, "Descartada por Facu"
    return 5.0, "sin estudio: valor neutro 5,0"
for cod, d in orden.items():
    fr = f2rows.get(cod, {}); b = fr.get("_b", "?")
    nota = fr.get("Nota de Facu") or notas_orden.get(cod) or ""
    if fr.get("Nota de Facu") and notas_orden.get(cod) and notas_orden[cod] != fr["Nota de Facu"]:
        nota = fr["Nota de Facu"] + "\n— Comentario del 2026-10-15: " + notas_orden[cod]
    partes = []
    if nota: partes.append(nota.strip())
    marca = fr.get("Marca de Facu")
    if marca: partes.append(f"[Marca: {marca}]" if not str(marca).startswith("Sin color") else "[Sin color, con nota]")
    if cod in EXTRA_NOTA: partes.append(EXTRA_NOTA[cod])
    if b == "A" and fr.get("Tu idea (palabras de Facu)"): idea = f"{cod} · " + str(fr["Tu idea (palabras de Facu)"])
    elif b == "D" and fr.get("Idea (palabras de Facu)"): idea = f"{cod} · " + str(fr["Idea (palabras de Facu)"])
    else: idea = f"{cod} · " + str(d["Idea o problema"])
    aj, mot = AJ.get(cod, (0.0, ""))
    add(BLK.get(b, "?"), cod, idea, "\n".join(partes) if partes else "(marcada, sin comentario)",
        int(d["G · Gusto"]), int(d["P · Producto global"]), int(d["M · Mercado"]), int(d["H · Hueco AR"]), int(d["C · Construible"]),
        int(d["R · Regulación/riesgo"]), int(d["V · Ventaja de Facu"]), "Orden de Claude (2026-10-14)", aj, mot, *evidencia(cod, fr))

# ---------- 2) Ideas propias que no están en Fase 2 ----------
add("Ideas propias (libreta)", "A1", "A1 · Intermediario de pagos seguros con el exterior (escrow). Candidata de etapa 2.",
    "Idea de Facu del 2026-10-07. Comentario suyo: traer a Argentina lo que funciona en EE.UU. (Escrow.com existe en forma genérica). Ficha en ideas/2026-10-07-intermediario-pagos-seguros.md.",
    5, 5, 4, 3, 2, 2, 3, "Estimación de Claude 2026-10-21 (custodia de fondos regulada; hueco solo en un nicho)")

# ---------- 3) NICHOS-Y-PROBLEMAS-2: 8 marcas ----------
wb2 = load_workbook(R / "NICHOS-Y-PROBLEMAS-2.xlsx", read_only=True)
pr = list(wb2["Problemas"].iter_rows(values_only=True)); ph = [str(x or "") for x in pr[0]]
ix = {h: k for k, h in enumerate(ph)}
G2 = {"PET-1-3": 5, "SEG-2-5": 4, "SEG-3-4": 4, "HOG-3-2": 4, "ALQ-2-3": 4, "TEL-5-5": 4, "EVE-4-5": 3, "MOV-2-5": 3}
for r in pr[1:]:
    cod = r[0]; nota = r[ix["Me gusta (Facu)"]]
    if not nota: continue
    glob = str(r[ix["Producto global o a medida"]]).lower()
    P = 5 if glob.startswith("sí") else (3 if glob.startswith("parcial") else 1)
    g = lambda h: int(r[ix[h]])
    C = clamp((g("Fit app/IA") + g("Fit Facu")) / 2)
    idea = f"{cod} · {r[ix['Problema']]}"
    anot = str(nota).strip()
    if cod == "HOG-3-2":
        anot = "(Marcó el problema de las empresas de limpieza; ver su idea propia más abajo.) " + anot
        anot = "Marcó este problema; su comentario propone otra idea y está cargado como fila aparte. Ver «Empresa de empleadas domésticas en blanco»."
    add("Excel de nichos 2", cod, idea, anot, G2[cod], P, g("Mercado"), g("Hueco en AR"), C, g("Regulación (5 = fácil)"), g("Fit Facu"),
        "Puntajes del propio Excel (nichos 2) traducidos a la escala de 7 criterios",
        (-0.5 if cod == "PET-1-3" else 0.0), ("Una sola búsqueda en Argentina y riesgo de términos de uso de los portales de terceros" if cod == "PET-1-3" else ""),
        float(r[ix["Total /25"]]) / 25 * 10, "Total /25 del Excel de nichos 2")
add("Ideas propias (nichos 2)", "HOG-3-2b", "Empresa de empleadas domésticas con sueldo digno, en blanco y con trabajo estable",
    "Facu: \"en argentina la empleada doméstica cobra muy poco, la idea sería hacer una empresa de empleadas domésticas y pagarles un salario digno, ponerlas en blanco y que tengan trabajo estable; muchas veces están en negro, pagadas sobre la ley y los trabajos son físicos y muy duros\". Cargada aparte de HOG-3-2. Es un negocio de servicio con personas, no un producto global.",
    4, 1, 4, 3, 3, 2, 1, "Estimación de Claude 2026-10-21 (Zolvers ya opera con personal verificado; régimen laboral no verificado)")

# ---------- 4) Gimnasio: colores de la hoja IDEAS ----------
ideas = {i["titulo"]: i for i in json.load(open(R / "research/datos/2026-10-18-gimnasio/ideas_final.json", encoding="utf-8"))}
wg = load_workbook(R / "GIMNASIO-DE-IDEAS.xlsx"); ws = wg["IDEAS"]
gh = [c.value for c in ws[1]]
def rgb(c):
    try: return c.fill.fgColor.rgb if c.fill.fill_type else None
    except Exception: return None
VERDE, AMAR, AZUL = "FF00B050", "FFFFFF00", "FF00B0F0"
LEG = {AMAR: "Interesante", VERDE: "Explicar mejor", AZUL: "Buenísima"}
H_AGRO = re.compile(r"agro|campo|forraj|rollo|maquinaria|planta|fas[oó]n|capacidad ociosa|stock|log[ií]stic|proceso|ingenier|dep[oó]sito|obra|arrend|cosecha|acopio|silo|granos", re.I)
H_MED = re.compile(r"edificio|inmueb|alquil|cuadra|barrio|consorcio|reparaci|mantenimiento|oficio", re.I)
R_ALTO = re.compile(r"salud|prepaga|obra social|abogad|jubil|seguro|siniestro|deuda|fondos|escrow|cl[ií]nic|m[eé]dic|remedio|cobertura|reclamo", re.I)
R_BAJO = re.compile(r"puntaje|tasador|balance|ficha|cobertura real|calculadora|diagn[oó]stico satelital|datos", re.I)
for row in ws.iter_rows(min_row=2, max_row=126):
    cols = {rgb(c) for c in row} & {VERDE, AMAR, AZUL}
    if not cols: continue
    t = row[4].value; i = ideas.get(t)
    if not i: continue
    marca = LEG[VERDE] if VERDE in cols else (LEG[AZUL] if AZUL in cols else LEG[AMAR])
    v = i["verificacion"]; s = v["score_ajustado"]; texto = f"{t} {i.get('una_linea','')}"
    Gm = {"Interesante": 4, "Explicar mejor": 3, "Buenísima": 5}[marca]
    Rr = 2 if R_ALTO.search(texto) else (4 if R_BAJO.search(texto) else 3)
    Vv = 4 if H_AGRO.search(texto) else (3 if H_MED.search(texto) else 2)
    comp = ", ".join(c["nombre"].split(" (")[0] for c in (v.get("competidores_argentina") or [])[:3])
    anot = f"[Marca: {marca}]" + (" Quiere que se la expliquen mejor." if marca == "Explicar mejor" else "") + f" Verificación web 2026-10-19: {v.get('existe_en_argentina')}" + (f" (competidores: {comp})" if comp else "") + "."
    ajuste, mot = 0.0, ""
    if t.startswith("Bolsa de capacidad ociosa de plantas"): ajuste, mot = -0.3, "Se parece a IND-3-5, D24 y C5, que Facu rechazó: falta confirmar si fue por el modelo"
    add("Excel del gimnasio", f"GIM-{i['id_tmp']}", t + " — " + i.get("una_linea", ""), anot,
        Gm, clamp(float(s["potencial"]) / 2), clamp((float(s["potencial"]) + float(s["por_que_ahora"])) / 4), clamp(float(s["brecha_argentina"]) / 2),
        clamp(float(s["factibilidad_facu"]) / 2), Rr, Vv, "Puntajes ajustados del gimnasio (juez + verificación web) traducidos a 7 criterios", ajuste, mot,
        sum(float(s[k]) for k in ("innovacion", "factibilidad_facu", "brecha_argentina", "por_que_ahora", "potencial")) / 5, "Puntaje final del gimnasio (juez y verificación web)")
# ideas escritas por Facu al pie de la hoja
propias = [
    (127, "App para el manejo de la obra por el jefe de obra", "Facu: \"se me ocurre una app para el manejo de la obra por el jefe de obra, muchas veces es un albañil más experimentado y hace falta orden y tecnología sencilla; debería ser barata y contratada por el que quiere hacer la obra\". [Amarillo: interesante]", (5, 4, 4, 2, 4, 4, 3), "Estimación de Claude 2026-10-21 (competencia en apps de obra no verificada)"),
    (128, "Programa para arquitectos: mandás una foto y te arma un render con IA, automático y con un solo pago", "Facu: \"nada que ver con este pero el render me gustó; un programa para arquitectos que le mandás una foto y te arma directo con IA, automático y con un solo pago\". [Amarillo: interesante] Relacionada con Yardzen y Hover del contraste.", (5, 3, 3, 1, 4, 5, 2), "Estimación de Claude 2026-10-21 (hay muchas herramientas de render con IA; no verificado en Argentina)"),
    (129, "Membresía mensual de mantenimiento de la casa que cubra todo (se rompe una pared o un caño y se lo arreglan gratis)", "Facu: \"puede ser una membresía mensual por el mantenimiento de la casa, que cubra todo\". Nota suya: «revisar, dudoso». Marca verde: «EXPLICAR MEJOR». El gimnasio verificó algo parecido: abonos de mantenimiento ya existen en parte (IKÉ con bancos y tarjetas, Zolvers y Servidos sueltos) y el riesgo es que funciona como seguro.", (4, 4, 4, 2, 3, 3, 3), "Estimación de Claude 2026-10-21 con lo verificado en el gimnasio (N145, N149, Frontdoor, Honey Homes)"),
]
for _, nombre, anot, (g, p, m, h, c, r, v), pts in propias:
    add("Ideas propias (gimnasio)", "PROPIA-GIM", nombre, anot, g, p, m, h, c, r, v, pts)

filas.sort(key=lambda d: (-d["score"], -d["G"], d["codigo"]))
json.dump(filas, open(pathlib.Path(__file__).parent / "marcas-todas.json", "w", encoding="utf-8"), ensure_ascii=False, indent=1)

# ---------- Excel ----------
HDR_FILL = PatternFill("solid", fgColor="1F3A5F"); HDR_FONT = Font(bold=True, color="FFFFFF", size=12)
WRAP = Alignment(wrap_text=True, vertical="top"); CEN = Alignment(horizontal="center", vertical="top")
THIN = Side(style="thin", color="D9D9D9"); BORDER = Border(left=THIN, right=THIN, top=THIN, bottom=THIN)
wb_out = Workbook(); w1 = wb_out.active; w1.title = "Mis ideas"
w1.append(["Ideas", "Anotaciones de Facu", "Puntuación (1 a 10, opinión de Claude)"])
for c in range(1, 4):
    cell = w1.cell(1, c); cell.fill = HDR_FILL; cell.font = HDR_FONT; cell.alignment = Alignment(wrap_text=True, vertical="center", horizontal="center"); cell.border = BORDER
w1.row_dimensions[1].height = 36
for d in filas:
    w1.append([f"[{d['origen']}] {d['idea']}", d["anot"], d["score"]])
for r in range(2, w1.max_row + 1):
    for c in range(1, 4):
        cell = w1.cell(r, c); cell.border = BORDER; cell.alignment = CEN if c == 3 else WRAP
    w1.cell(r, 3).number_format = "0.0"; w1.cell(r, 3).font = Font(bold=True, size=12)
w1.column_dimensions["A"].width = 78; w1.column_dimensions["B"].width = 95; w1.column_dimensions["C"].width = 18
w1.freeze_panes = "A2"; w1.auto_filter.ref = w1.dimensions
w1.conditional_formatting.add(f"C2:C{w1.max_row}", ColorScaleRule(start_type="num", start_value=3, start_color="F8696B", mid_type="num", mid_value=6, mid_color="FFEB84", end_type="num", end_value=9, end_color="63BE7B"))
w1.page_setup.orientation = "landscape"; w1.page_setup.fitToWidth = 1; w1.page_setup.fitToHeight = 0; w1.sheet_properties.pageSetUpPr.fitToPage = True; w1.print_title_rows = "1:1"

w2 = wb_out.create_sheet("Cómo puntué")
texto = [
    ("CÓMO SE PUNTUÓ (opinión de Claude, 2026-10-21; no es dato)", True),
    ("Puntuación = mitad ENCAJE y mitad EVIDENCIA, en escala de 10. ENCAJE: 7 criterios de 1 a 5 (los de abajo), sumados sobre 35 y llevados a 10; es la misma escala de «Orden de Claude» (2026-10-14). EVIDENCIA: el mejor puntaje que dejó lo que estudiamos de esa idea. Si nunca se estudió, vale 5,0 (neutro). Por eso las ideas que se estudiaron a fondo y salieron flojas bajan, y las que solo se ven lindas no suben solas.", False),
    ("Evidencia usada: indagación a fondo del 2026-10-15 (stock y piezas, profesores, Papá Noel, fruta por foto, contadores, certificados médicos, plantillas, logística, aprendizaje); total de los investigadores en los Excel de nichos; score de los informes en el Excel de 633; puntaje de las ideas propias del 2026-10-08; y el puntaje final del gimnasio. Cada fila guarda su evidencia y su fuente en marcas-todas.json.", False),
    ("", False),
    ("G · Gusto de Facu: cuánto la marcó y cómo habló de ella. Propia o con nota larga y entusiasta = 5. Celeste, azul o idea escrita por él = 4-5. Amarillo o «interesante» = 4. Verde («explicar mejor») = 3. Marcada sin comentario = 3.", False),
    ("P · Producto global: qué tan lejos de un trabajo a medida está. Tu criterio (2026-10-14): producto global, no trabajo a medida por empresa. Un servicio con personas puntúa 1.", False),
    ("M · Mercado: tamaño de quién paga y cuánta gente tiene el problema.", False),
    ("H · Hueco en Argentina: 5 = no hay nada acá; 1 = ya existe casi igual. En las ideas del gimnasio sale de la verificación web del 2026-10-19; en las viejas, de los estudios de la época.", False),
    ("C · Construible: qué tan lanzable es sin programar, con Claude, no-code y poca plata.", False),
    ("R · Regulación y riesgo: 5 = fácil. Bajo cuando hay salud, seguros, juicios, custodia de fondos o datos sensibles.", False),
    ("V · Ventaja de Facu: ingeniería industrial, CEMEVA (granos), agro, stock, logística y procesos puntúan alto; lo que no conocés por dentro puntúa bajo.", False),
    ("", False),
    ("DE DÓNDE SALE CADA PUNTAJE", True),
    ("Las 74 de la Fase 2 (Excel de 633 ideas, nichos 1, ideas propias): los 7 criterios de «Orden de Claude» (2026-10-14), con ajustes chicos por lo que se verificó después. Las ajustadas llevan el motivo en motivo_ajuste dentro de research/datos/2026-10-21-marcas-todas/marcas-todas.json.", False),
    ("Nichos 2 (8): los puntajes del propio Excel (mercado, hueco, fit app e IA, fit Facu, regulación y producto global o a medida) traducidos a estos 7 criterios.", False),
    ("Gimnasio (29 marcadas): los puntajes finales del juez y de la verificación web, traducidos. Regulación y ventaja de Facu las puse yo con reglas simples de palabras clave: son las menos fiables.", False),
    ("Tus ideas escritas en el gimnasio y la de las empleadas domésticas: estimación mía, marcada como tal en el JSON. Ninguna se verificó en la web.", False),
    ("", False),
    ("COSAS QUE TENÉS QUE SABER", True),
    ("Los colores del gimnasio los interpreté con la leyenda que dejaste al pie de la hoja IDEAS: amarillo = INTERESANTE, verde = EXPLICAR MEJOR, azul = BUENISIMA. Ninguna idea tiene azul; la única vez que aparece es en la leyenda.", False),
    ("La puntuación es relativa: sirve para ordenar la lectura, no para decidir. Una diferencia de menos de 0,5 entre dos ideas no significa nada.", False),
    ("El puntaje mezcla cosas distintas: ideas que ya se estudiaron a fondo (stock y piezas, profesores, Papá Noel) con otras que solo pasaron por un juez. Las estudiadas tienen menos incertidumbre, no más puntos.", False),
    ("Ninguna idea fue validada con clientes. Lo que más puede cambiar un puntaje es hablar con 5 o 10 personas que tengan el problema.", False),
]
w2.column_dimensions["A"].width = 150
for k, (t, b) in enumerate(texto, 1):
    c = w2.cell(k, 1, t); c.alignment = WRAP; c.font = Font(bold=b, size=12 if b else 11, color="1F3A5F" if b else "000000")
wb_out.save(R / "MARCAS-DE-FACU.xlsx")
print(f"OK: {len(filas)} filas · origen:", {o: sum(1 for d in filas if d['origen'] == o) for o in sorted({d['origen'] for d in filas})})
print("top 15:"); [print(f"  {d['score']:.1f} G{d['G']} P{d['P']} M{d['M']} H{d['H']} C{d['C']} R{d['R']} V{d['V']} | {d['idea'][:80]}") for d in filas[:15]]
print("últimas 8:"); [print(f"  {d['score']:.1f} | {d['idea'][:80]}") for d in filas[-8:]]
