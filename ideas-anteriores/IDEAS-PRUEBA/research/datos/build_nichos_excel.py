# Arma NICHOS-Y-PROBLEMAS.xlsx a partir de los JSON de research/datos/2026-10-13-nichos/.
# Cada JSON lo escribió un investigador (un nicho, 25 problemas, 2 soluciones de afuera por problema).
# parches/*.json = 2.ª pasada (presencia en Argentina) y revisión de coherencia.
# 2026-10-13-familias.json = familias transversales.
# 2026-10-13-deduplicacion.json = qué filas repiten investigaciones anteriores y qué filas se fusionan (Regla N.º 2).
# Uso: python research/datos/build_nichos_excel.py [ruta_salida.xlsx]
import json
import sys
from pathlib import Path

from openpyxl import Workbook
from openpyxl.formatting.rule import ColorScaleRule
from openpyxl.styles import Alignment, Border, Font, PatternFill, Side
from openpyxl.utils import get_column_letter
from openpyxl.worksheet.datavalidation import DataValidation

ROOT = Path(__file__).resolve().parents[2]
SRC = ROOT / "research" / "datos" / "2026-10-13-nichos"
FAMILIAS = ROOT / "research" / "datos" / "2026-10-13-familias.json"
DEDUP = ROOT / "research" / "datos" / "2026-10-13-deduplicacion.json"
IDEAS_633 = ROOT / "research" / "datos" / "2026-10-02-todas-las-ideas.json"
OUT = Path(sys.argv[1]) if len(sys.argv) > 1 else ROOT / "NICHOS-Y-PROBLEMAS.xlsx"
FECHA = "2026-10-13"
# Ideas propias de Facu (hoja "Fase 2" de TODAS-LAS-IDEAS.xlsx) que pueden aparecer como referencia
IDEAS_FASE2 = {
    "L1": "Intermediario de compras / cierre seguro de autos usados",
    "L6": "Uber de la logística empresarial",
    "L10": "Stock con IA y cámara / auditoría de góndola por foto",
}

CRITERIOS = ["mercado", "hueco_ar", "fit_app_ia", "fit_facu", "regulacion_facilidad"]

HEADER_FILL = PatternFill("solid", fgColor="1F3864")
HEADER_FONT = Font(bold=True, color="FFFFFF")
NICHO_FILLS = ["DDEBF7", "FCE4D6", "E2EFDA", "FFF2CC", "EDEDED",
               "D9E1F2", "F8CBAD", "C6E0B4", "FFE699", "DBDBDB"]
THIN = Side(style="thin", color="BFBFBF")
BORDER = Border(left=THIN, right=THIN, top=THIN, bottom=THIN)
WRAP = Alignment(wrap_text=True, vertical="top")
CENTER = Alignment(horizontal="center", vertical="top", wrap_text=True)
LINK_FONT = Font(color="0563C1", underline="single")
NUEVA_FILL = PatternFill("solid", fgColor="E2EFDA")
TOTAL_SCALE = dict(start_type="min", start_color="F8696B", mid_type="percentile", mid_value=50,
                   mid_color="FFEB84", end_type="max", end_color="63BE7B")


def norm_si_no(v):
    s = str(v or "").strip().lower()
    if s in ("sí", "si", "yes", "true", "verificado"):
        return "sí"
    if s in ("no", "false"):
        return "no"
    return s or "no"


def num(v):
    try:
        n = float(v)
    except (TypeError, ValueError):
        return None
    return int(n) if n == int(n) else n


def total_of(r):
    p = r.get("puntajes") or {}
    scores = [num(p.get(c)) for c in CRITERIOS]
    return sum(scores) if all(isinstance(s, (int, float)) for s in scores) else None


def sol_cols(s):
    s = s or {}
    nombre = s.get("nombre", "")
    pais = s.get("pais", "")
    titulo = f"{nombre} ({pais})" if pais else nombre
    return [titulo, s.get("que_hace", ""), s.get("traccion", "") or "sin dato", s.get("url", ""),
            norm_si_no(s.get("verificado")), s.get("como_verifique", ""), s.get("fuente_traccion", "")]


def apply_patches(rows, avisos):
    """Segunda pasada: parches/*.json completan la presencia en Argentina sin tocar los JSON originales.
    Cada parche es una lista de {id, presencia_ar, presencia_ar_detalle, hueco_ar, nota}."""
    by_id = {r.get("id"): r for r in rows}
    n = 0
    for f in sorted((SRC / "parches").glob("*.json")):
        try:
            data = json.loads(f.read_text(encoding="utf-8"))
        except Exception as e:  # noqa: BLE001
            avisos.append(f"parche {f.name}: JSON inválido ({e})")
            continue
        for p in data:
            r = by_id.get(p.get("id"))
            if r is None:
                avisos.append(f"parche {f.name}: id desconocido {p.get('id')}")
                continue
            etiqueta = p.get("etiqueta", f"2.ª pasada {FECHA}")
            previa = "anterior" if r.get("_parcheada") else "1.ª pasada"
            r["presencia_ar"] = p.get("presencia_ar", r.get("presencia_ar"))
            r["presencia_ar_detalle"] = (f"[{etiqueta}] {p.get('presencia_ar_detalle', '')}"
                                         f" || [{previa}] {r.get('presencia_ar_detalle', '')}")
            if p.get("hueco_ar") is not None:
                r.setdefault("puntajes", {})["hueco_ar"] = p["hueco_ar"]
            if p.get("nota"):
                r["notas_puntaje"] = f"{r.get('notas_puntaje', '')} | {etiqueta}: {p['nota']}"
            r["_parcheada"] = True
            n += 1
    return n


def ref_text(refs, nombres):
    out = []
    for x in [x.strip() for x in refs.split(",") if x.strip()]:
        key = x.split(" ")[0]
        nombre = nombres.get(key, "")
        out.append(f"{x}: {nombre[:70]}" if nombre else x)
    return " | ".join(out)


def apply_dedup(rows, avisos):
    """Regla N.º 2: separa las filas que repiten investigaciones anteriores y fusiona las repetidas entre nichos."""
    if not DEDUP.exists():
        for r in rows:
            r["_estado"], r["_nueva"] = "N", "nueva"
        return rows, [], 0
    d = json.loads(DEDUP.read_text(encoding="utf-8"))
    nombres = {i["id"]: i["nombre"] for i in json.loads(IDEAS_633.read_text(encoding="utf-8"))}
    nombres.update(IDEAS_FASE2)
    by_id = {r["id"]: r for r in rows}
    for r in rows:
        c = d["cruce"].get(r["id"])
        if c is None:
            avisos.append(f"sin dato de deduplicación: {r['id']}")
            c = {"estado": "N", "repite_o_se_parece_a": ""}
        r["_estado"] = c["estado"]
        r["_ref"] = ref_text(c.get("repite_o_se_parece_a", ""), nombres)
        r["_ref_nota"] = c.get("nota", "")
        r["_nueva"] = {"N": "nueva", "P": f"parecida a {r['_ref']}", "C": f"repite {r['_ref']}"}[c["estado"]]
    quitar = set()
    for f in d.get("fusiones", []):
        canon = by_id[f["canonica"]]
        otros = [by_id[x] for x in f["miembros"] if x != f["canonica"]]
        huecos = [num((m.get("puntajes") or {}).get("hueco_ar")) for m in [canon] + otros]
        huecos = [h for h in huecos if isinstance(h, (int, float))]
        if huecos and min(huecos) < num(canon["puntajes"]["hueco_ar"]):
            canon["notas_puntaje"] = (f"{canon.get('notas_puntaje', '')} | Fusión: hueco en AR = el menor del grupo "
                                      f"({canon['puntajes']['hueco_ar']} → {min(huecos)}).")
            canon["puntajes"]["hueco_ar"] = min(huecos)
        canon["_tambien"] = "\n".join(
            f"{m['id']} · {m.get('nicho')} / {m.get('especialidad')}: {m.get('problema')} — afuera: "
            f"{(m.get('solucion_1') or {}).get('nombre', '')}, {(m.get('solucion_2') or {}).get('nombre', '')} — "
            f"en AR: {m.get('presencia_ar', '')} (hueco {(m.get('puntajes') or {}).get('hueco_ar')})"
            for m in otros)
        canon["_nichos_fusion"] = [canon.get("nicho")] + [m.get("nicho") for m in otros]
        quitar.update(m["id"] for m in otros)
    repetidas = [r for r in rows if r["_estado"] == "C"]
    unicas = [r for r in rows if r["_estado"] != "C" and r["id"] not in quitar]
    return unicas, repetidas, len(quitar)


def load_rows():
    rows, avisos = [], []
    files = sorted(SRC.glob("*.json"))
    for f in files:
        try:
            data = json.loads(f.read_text(encoding="utf-8"))
        except Exception as e:  # noqa: BLE001
            avisos.append(f"{f.name}: JSON inválido ({e})")
            continue
        if isinstance(data, dict):
            data = data.get("problemas") or data.get("filas") or []
        if len(data) != 25:
            avisos.append(f"{f.name}: tiene {len(data)} filas (se esperaban 25)")
        rows.extend(data)
    parcheadas = apply_patches(rows, avisos)
    fam = {"familias": {}, "asignacion": {}, "comentarios": {}}
    if FAMILIAS.exists():
        fam.update(json.loads(FAMILIAS.read_text(encoding="utf-8")))
    for r in rows:
        code = fam["asignacion"].get(r.get("id"), "")
        r["_familia_cod"] = code
        r["_familia"] = fam["familias"].get(code, "")
        if not code:
            avisos.append(f"sin familia: {r.get('id')}")
    unicas, repetidas, fusionadas = apply_dedup(rows, avisos)
    return files, rows, unicas, repetidas, fusionadas, avisos, parcheadas, fam


COLUMNS = [
    # (encabezado, ancho)
    ("ID", 10), ("Nicho", 16), ("Especialidad", 22), ("Problema", 40), ("Familia transversal", 26),
    ("¿Es nueva? (vs. investigaciones anteriores)", 26), ("Me gusta (Facu)", 12), ("Total /25", 9),
    ("Mercado", 9), ("Hueco en AR", 9), ("Fit app/IA", 9), ("Fit Facu", 9), ("Regulación (5 = fácil)", 11),
    ("Detalle del problema", 55), ("Quién paga", 22), ("Cómo se resuelve hoy", 40),
    ("Solución 1 (afuera)", 24), ("Qué hace 1", 40), ("Tracción 1", 35), ("Web 1", 28), ("Verificada 1", 10), ("Cómo se verificó 1", 24), ("Fuente tracción 1", 28),
    ("Solución 2 (afuera)", 24), ("Qué hace 2", 40), ("Tracción 2", 35), ("Web 2", 28), ("Verificada 2", 10), ("Cómo se verificó 2", 24), ("Fuente tracción 2", 28),
    ("Presencia en Argentina", 12), ("Qué hay en Argentina", 45),
    ("Tipo de solución", 16), ("Cómo usa IA", 40), ("Patrón CEMEVA", 10), ("Conocimiento de Facu", 18), ("Regulación (detalle)", 30),
    ("Por qué ese puntaje (opinión)", 50), ("También aparece en (filas fusionadas)", 55),
]
# Índices (base 0) dentro de row_values()
I_FAM, I_NUEVA, I_TOTAL, I_HUECO, I_SOL1, I_SOL2, I_PRES, I_CEMEVA = 4, 5, 7, 9, 16, 23, 30, 34


def row_values(r):
    p = r.get("puntajes") or {}
    scores = [num(p.get(c)) for c in CRITERIOS]
    return ([r.get("id", ""), r.get("nicho", ""), r.get("especialidad", ""), r.get("problema", ""),
             r.get("_familia", ""), r.get("_nueva", ""), "", total_of(r)] + scores +
            [r.get("detalle", ""), r.get("quien_paga", ""), r.get("parche_actual", "")] +
            sol_cols(r.get("solucion_1")) + sol_cols(r.get("solucion_2")) +
            [r.get("presencia_ar", ""), r.get("presencia_ar_detalle", ""),
             r.get("tipo_solucion", ""), r.get("como_usa_ia", ""), norm_si_no(r.get("patron_cemeva")),
             r.get("conocimiento_facu", ""), r.get("regulacion", ""), r.get("notas_puntaje", ""),
             r.get("_tambien", "")])


def style_header(ws, cols):
    ws.append([c[0] for c in cols])
    for i, (_, w) in enumerate(cols, start=1):
        cell = ws.cell(row=1, column=i)
        cell.fill, cell.font, cell.alignment, cell.border = HEADER_FILL, HEADER_FONT, CENTER, BORDER
        ws.column_dimensions[get_column_letter(i)].width = w
    ws.row_dimensions[1].height = 42


def style_row(ws, ncols, centered, height=None):
    rr = ws.max_row
    for c in range(1, ncols + 1):
        cell = ws.cell(row=rr, column=c)
        cell.alignment = CENTER if c in centered else WRAP
        cell.border = BORDER
    if height:
        ws.row_dimensions[rr].height = height
    return rr


def sort_key(t):
    return (-t[0], -t[1], t[2].get("id", ""))


def build():
    files, todas, rows, repetidas, fusionadas, avisos, parcheadas, fam = load_rows()
    if not rows:
        sys.exit("No hay filas: ¿están los JSON en " + str(SRC) + "?")

    nichos = []
    for r in todas:
        if r.get("nicho") not in nichos:
            nichos.append(r.get("nicho"))
    fill_by_nicho = {n: PatternFill("solid", fgColor=NICHO_FILLS[i % len(NICHO_FILLS)]) for i, n in enumerate(nichos)}

    scored = []
    for r in rows:
        v = row_values(r)
        scored.append((v[I_TOTAL] if isinstance(v[I_TOTAL], (int, float)) else -1, v[I_HUECO] or 0, r, v))
    scored.sort(key=sort_key)
    n_nuevas = sum(1 for r in rows if r["_estado"] == "N")
    n_parecidas = sum(1 for r in rows if r["_estado"] == "P")

    wb = Workbook()

    # ---------- Hoja Problemas (solo únicas: sin repetidas y con fusiones) ----------
    ws = wb.active
    ws.title = "Problemas"
    style_header(ws, COLUMNS)
    centered = {7, 8, 9, 10, 11, 12, 13, 21, 28, 31, 35}
    url_cols = {20, 23, 27, 30}
    for r in rows:
        ws.append(row_values(r))
        rr = style_row(ws, len(COLUMNS), centered, 75)
        for c in url_cols:
            cell = ws.cell(row=rr, column=c)
            if isinstance(cell.value, str) and cell.value.startswith("http"):
                cell.hyperlink, cell.font = cell.value, LINK_FONT
        ws.cell(row=rr, column=2).fill = fill_by_nicho.get(r.get("nicho"), PatternFill())
        if r["_estado"] == "N":
            ws.cell(row=rr, column=6).fill = NUEVA_FILL
        ws.cell(row=rr, column=8).font = Font(bold=True)
    last = ws.max_row
    ws.freeze_panes = "E2"
    ws.auto_filter.ref = f"A1:{get_column_letter(len(COLUMNS))}{last}"
    ws.conditional_formatting.add(f"H2:H{last}", ColorScaleRule(**TOTAL_SCALE))
    for col in "IJKLM":
        ws.conditional_formatting.add(f"{col}2:{col}{last}", ColorScaleRule(
            start_type="num", start_value=1, start_color="F8CBAD",
            end_type="num", end_value=5, end_color="C6EFCE"))
    dv = DataValidation(type="list", formula1='"sí,tal vez,no"', allow_blank=True)
    ws.add_data_validation(dv)
    dv.add(f"G2:G{last}")

    # ---------- Hoja Ranking ----------
    rk = wb.create_sheet("Ranking")
    rk_cols = [("Puesto", 7), ("ID", 10), ("Nicho", 18), ("Especialidad", 22), ("Problema", 45),
               ("Familia transversal", 26), ("¿Es nueva?", 22), ("Total /25", 9), ("Hueco en AR", 9),
               ("Patrón CEMEVA", 10), ("Solución 1", 26), ("Solución 2", 26), ("Presencia en Argentina", 12)]
    style_header(rk, rk_cols)
    for pos, (total, hueco, r, v) in enumerate(scored, start=1):
        rk.append([pos, v[0], v[1], v[2], v[3], v[I_FAM], v[I_NUEVA], v[I_TOTAL], v[I_HUECO], v[I_CEMEVA],
                   v[I_SOL1], v[I_SOL2], v[I_PRES]])
        rr = style_row(rk, len(rk_cols), {1, 2, 8, 9, 10, 13})
        rk.cell(row=rr, column=3).fill = fill_by_nicho.get(r.get("nicho"), PatternFill())
        if r["_estado"] == "N":
            rk.cell(row=rr, column=7).fill = NUEVA_FILL
    rk.freeze_panes = "F2"
    rk.auto_filter.ref = f"A1:{get_column_letter(len(rk_cols))}{rk.max_row}"
    rk.conditional_formatting.add(f"H2:H{rk.max_row}", ColorScaleRule(**TOTAL_SCALE))

    # ---------- Hoja Familias ----------
    fm = wb.create_sheet("Familias")
    fm_cols = [("Familia transversal", 34), ("Problemas", 10), ("Nichos donde aparece", 10),
               ("Total promedio /25", 11), ("Mejor total", 9), ("Hueco AR promedio", 10),
               ("Patrón CEMEVA", 10), ("Nichos", 40), ("Problemas de la familia (ID, total)", 70),
               ("Comentario (opinión de Claude)", 60)]
    style_header(fm, fm_cols)
    grupos = {}
    for t in scored:
        grupos.setdefault(t[2].get("_familia_cod", ""), []).append(t)

    def nichos_de(ts):
        ns = []
        for t in ts:
            for n in t[2].get("_nichos_fusion") or [t[2].get("nicho")]:
                if n not in ns:
                    ns.append(n)
        return ns

    orden = sorted((c for c in grupos if c and c != "Q"),
                   key=lambda c: (-len(nichos_de(grupos[c])), -sum(t[0] for t in grupos[c]) / len(grupos[c])))
    orden += [c for c in ("Q", "") if c in grupos]
    for code in orden:
        ts = grupos[code]
        ns = nichos_de(ts)
        totals = [t[0] for t in ts if t[0] >= 0]
        huecos = [t[1] for t in ts if t[1]]
        fm.append([fam["familias"].get(code, "(sin familia)"), len(ts), len(ns),
                   round(sum(totals) / len(totals), 1) if totals else None, max(totals) if totals else None,
                   round(sum(huecos) / len(huecos), 1) if huecos else None,
                   sum(1 for t in ts if norm_si_no(t[2].get("patron_cemeva")) == "sí"),
                   ", ".join(ns),
                   "\n".join(f"{t[2].get('id')} ({t[0]}): {t[2].get('problema')}" for t in ts),
                   fam.get("comentarios", {}).get(code, "")])
        style_row(fm, len(fm_cols), {2, 3, 4, 5, 6, 7}, min(15 * len(ts) + 10, 400))
    fm.freeze_panes = "B2"
    fm.conditional_formatting.add(f"D2:D{fm.max_row}", ColorScaleRule(**TOTAL_SCALE))

    # ---------- Hoja Por nicho ----------
    pn = wb.create_sheet("Por nicho")
    pn_cols = [("Nicho", 26), ("Investigadas", 11), ("Repetidas (salieron)", 11), ("Fusionadas en otra fila", 11),
               ("Quedan", 9), ("Nuevas", 9), ("Parecidas", 10), ("Total promedio /25", 11), ("Mejor total", 9),
               ("Con hueco en AR (4-5)", 11), ("Los 3 mejores (ID: problema)", 80)]
    style_header(pn, pn_cols)
    ids_quedan = {r["id"] for r in rows}
    for n in nichos:
        todas_n = [r for r in todas if r.get("nicho") == n]
        rep_n = [r for r in todas_n if r["_estado"] == "C"]
        fus_n = [r for r in todas_n if r["_estado"] != "C" and r["id"] not in ids_quedan]
        rs = [t for t in scored if t[2].get("nicho") == n]
        totals = [t[0] for t in rs if t[0] >= 0]
        pn.append([n, len(todas_n), len(rep_n), len(fus_n), len(rs),
                   sum(1 for t in rs if t[2]["_estado"] == "N"), sum(1 for t in rs if t[2]["_estado"] == "P"),
                   round(sum(totals) / len(totals), 1) if totals else None, max(totals) if totals else None,
                   sum(1 for t in rs if (t[1] or 0) >= 4),
                   "\n".join(f"{t[2].get('id')}: {t[2].get('problema')} ({t[0]})" for t in rs[:3])])
        rr = style_row(pn, len(pn_cols), {2, 3, 4, 5, 6, 7, 8, 9, 10}, 50)
        pn.cell(row=rr, column=1).fill = fill_by_nicho.get(n, PatternFill())
    pn.freeze_panes = "B2"

    # ---------- Hoja Ya estaban antes (repetidas) ----------
    ya = wb.create_sheet("Ya estaban antes")
    ya_cols = [("ID", 10), ("Nicho", 18), ("Especialidad", 22), ("Problema", 45),
               ("Repite a (idea anterior)", 45), ("Nota de la limpieza", 40), ("Total /25", 9),
               ("Solución 1 (afuera)", 26), ("Solución 2 (afuera)", 26), ("Presencia en Argentina", 12),
               ("Qué hay en Argentina", 60)]
    style_header(ya, ya_cols)
    for r in sorted(repetidas, key=lambda r: (-(total_of(r) or 0), r["id"])):
        ya.append([r["id"], r.get("nicho"), r.get("especialidad"), r.get("problema"), r.get("_ref"),
                   r.get("_ref_nota", ""), total_of(r), sol_cols(r.get("solucion_1"))[0],
                   sol_cols(r.get("solucion_2"))[0], r.get("presencia_ar", ""), r.get("presencia_ar_detalle", "")])
        rr = style_row(ya, len(ya_cols), {1, 7, 10}, 60)
        ya.cell(row=rr, column=2).fill = fill_by_nicho.get(r.get("nicho"), PatternFill())
    ya.freeze_panes = "E2"
    ya.auto_filter.ref = f"A1:{get_column_letter(len(ya_cols))}{ya.max_row}"

    # ---------- Hoja Cómo leer ----------
    cl = wb.create_sheet("Cómo leer", 0)
    cl.column_dimensions["A"].width = 120
    tot_ver = sum(1 for r in todas for k in ("solucion_1", "solucion_2")
                  if norm_si_no((r.get(k) or {}).get("verificado")) == "sí")
    tot_nover = 2 * len(todas) - tot_ver
    sin_buscar = sum(1 for r in todas if "sin verificar" in str(r.get("presencia_ar", "")).lower()
                     or ("no pude buscar" in str(r.get("presencia_ar_detalle", "")).lower() and not r.get("_parcheada")))
    lines = [
        ("NICHOS Y PROBLEMAS — embudo de oportunidades", True),
        (f"Armado el {FECHA} por Claude con 10 investigadores en paralelo (uno por nicho), una 2.ª pasada para la presencia en Argentina "
         "y una limpieza de repetidas. Datos crudos: research/datos/2026-10-13-nichos/ (un JSON por nicho + parches/). "
         "Script: research/datos/build_nichos_excel.py.", False),
        ("", False),
        ("Para qué sirve", True),
        (f"Es el embudo que pidió Facu el {FECHA}: muchas opciones buenas (nicho → especialidad → problema), cada una con 2 soluciones que ya funcionan afuera. "
         "Se filtra junto con la hoja \"Fase 2\" de TODAS-LAS-IDEAS.xlsx hasta quedar en 5-10, y de ahí se elige UNA para arrancar; las demás quedan de respaldo. "
         "Se espera descartar entre el 70% y el 90%.", False),
        ("", False),
        ("Cuántas quedaron (limpieza de repetidas, Regla N.º 2 del CLAUDE.md)", True),
        (f"Se investigaron {len(todas)} problemas ({len(nichos)} nichos × 5 especialidades × 5). "
         f"{len(repetidas)} repetían ideas de investigaciones anteriores (las 633 de TODAS-LAS-IDEAS.xlsx o las ideas propias de Facu en \"Fase 2\") "
         f"y salieron de la hoja principal: están en la hoja \"Ya estaban antes\", con la idea que repiten, porque traen datos nuevos (empresas de afuera y competencia local). "
         f"Otras {fusionadas} eran el mismo problema en dos nichos y se fusionaron en una sola fila (columna \"También aparece en\"). "
         f"QUEDAN {len(rows)} PROBLEMAS ÚNICOS: {n_nuevas} nuevos (verde en \"¿Es nueva?\") y {n_parecidas} parecidos a una idea anterior (con la referencia).", False),
        ("Repetida = mismo problema y mismo tipo de cliente que una idea anterior, aunque antes estuviera planteada como servicio. "
         "Parecida = comparte cliente o un problema vecino, pero no es la misma. Es criterio de Claude, revisado fila por fila "
         "(datos: research/datos/2026-10-13-deduplicacion.json).", False),
        ("En las filas fusionadas, el \"Hueco en AR\" es el menor del grupo (si en un nicho apareció competencia, vale para todos).", False),
        ("", False),
        ("Estructura", True),
        ("Nichos: " + ", ".join(nichos) + ". "
         "Las especialidades las eligió Claude por tamaño estimado de clientela (es estimación, no un ranking verificado de cantidad de empresas). "
         "Agro está como 1 nicho de 10 porque Facu lo conoce (CEMEVA) pero no quiere ir 100% por ahí.", False),
        ("", False),
        ("Hojas", True),
        ("Problemas: los únicos, con todo el detalle. Columna \"Me gusta (Facu)\" para marcar sí / tal vez / no (o pintar la fila, como en el otro Excel). Filtros en todas las columnas.", False),
        ("Ranking: las mismas filas ordenadas por el total. Es una vista para empezar, NO el filtro final.", False),
        ("Familias: agrupa los problemas que se repiten entre rubros. Un producto de una familia que toca muchos nichos se puede vender en varios rubros: "
         "es el \"nicho transversal\". La clasificación es opinión de Claude.", False),
        ("Por nicho: cuántas se investigaron, cuántas salieron por repetidas y cuántas quedan en cada nicho.", False),
        ("Ya estaban antes: las repetidas, con la idea anterior que repiten. No se borran: sirven para enriquecer esa idea vieja.", False),
        ("", False),
        ("Puntajes (1 a 5 cada uno; total sobre 25) — son OPINIÓN del investigador, no datos", True),
        ("Mercado: tamaño del problema en Argentina y Latinoamérica (5 = cientos de miles de clientes o mucha plata por cliente).", False),
        ("Hueco en AR: 5 = no se encontró nada local conocido; 1 = ya está resuelto y es famoso acá. En la 2.ª pasada: con 1 sola búsqueda sin resultados, máximo 4.", False),
        ("Fit app/IA: 5 = se resuelve mayormente con software o IA que se puede construir con Claude; 1 = requiere hardware pesado, red física o mucho capital.", False),
        ("Fit Facu: 5 = usa lo que sabe (transporte, stock y depósito, procesos, back-office de PyME) y lo puede vender él.", False),
        ("Regulación: 5 = casi sin regulación (fácil); 1 = muy regulado.", False),
        ("Ojo: los investigadores fueron 10 personas distintas; un 20 en un nicho no es exactamente comparable con un 20 en otro.", False),
        ("", False),
        ("Qué es dato y qué no (Regla N.º 1)", True),
        ("Soluciones de afuera: \"Verificada = sí\" significa que el investigador vio el sitio o una fuente en esta sesión (columna \"Cómo se verificó\"). "
         "\"no\" = NO se pudo comprobar: tratarla como dudosa.", False),
        ("Tracción (inversión, clientes, año): casi siempre es lo que la empresa dice de sí misma en su sitio (no auditado). \"sin dato\" = no se encontró.", False),
        ("Presencia en Argentina: sale de búsquedas rápidas. \"No encontrada\" NO prueba que no exista nada; antes de avanzar con una idea hay que buscar a fondo. "
         "Las filas de la 2.ª pasada empiezan con [2.ª pasada].", False),
        ("\"Cómo se resuelve hoy\" y los números del detalle son estimación salvo que digan la fuente. Leyes y normas citadas: verificar en el Boletín Oficial antes de usarlas.", False),
        ("Patrón CEMEVA: trabajo administrativo con documentos hecho a mano (Excel, mail, PDF, WhatsApp) que se puede automatizar con IA, como lo que Facu ya hizo en CEMEVA.", False),
        ("", False),
        ("Resumen de verificación", True),
        (f"Investigadas: {len(todas)}. Soluciones de afuera verificadas: {tot_ver}. Sin verificar: {tot_nover}. "
         f"Filas actualizadas en la 2.ª pasada y en la revisión de coherencia: {parcheadas}. Filas que siguen sin búsqueda en Argentina: {sin_buscar}.", False),
    ]
    if avisos:
        lines.append(("Avisos al armar: " + " | ".join(avisos), False))
    for text, bold in lines:
        cl.append([text])
        cell = cl.cell(row=cl.max_row, column=1)
        cell.alignment = Alignment(wrap_text=True, vertical="top")
        if bold:
            cell.font = Font(bold=True, size=14 if cl.max_row == 1 else 12)

    wb.save(OUT)
    print(f"ok: {OUT} | investigadas={len(todas)} | repetidas={len(repetidas)} | fusionadas={fusionadas} "
          f"| quedan={len(rows)} (nuevas={n_nuevas}, parecidas={n_parecidas}) | verificadas={tot_ver} | sin búsqueda AR={sin_buscar}")
    for a in avisos:
        print("aviso:", a)


if __name__ == "__main__":
    build()
