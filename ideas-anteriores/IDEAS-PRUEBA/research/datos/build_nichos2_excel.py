# Arma NICHOS-Y-PROBLEMAS-2.xlsx (búsqueda nueva del 2026-10-14, 20 nichos) a partir de research/datos/2026-10-14-nichos-2/.
# Copia adaptada de build_nichos_excel.py (que arma el primer Excel y NO se toca).
# Cada JSON lo escribió un investigador (un nicho, 25 problemas, 2 soluciones de afuera por problema); el objeto "_extras" se ignora.
# parches/*.json = 2.ª pasada (presencia en Argentina) y revisión de coherencia.
# 2026-10-14-familias-2.json = familias transversales.
# 2026-10-14-deduplicacion-2.json = cruce contra TODO el registro (Regla N.º 2). Estados:
#   N = nueva · P = parecida a un GANADOR de Facu (queda, con referencia)
#   C = repite algo anterior (sale) · R = parecida a algo que Facu NO eligió, rechazó o descartó (sale)
# Uso: python research/datos/build_nichos2_excel.py [ruta_salida.xlsx]
import csv
import json
import sys
from pathlib import Path

from openpyxl import Workbook
from openpyxl.formatting.rule import ColorScaleRule
from openpyxl.styles import Alignment, Border, Font, PatternFill, Side
from openpyxl.utils import get_column_letter
from openpyxl.worksheet.datavalidation import DataValidation

ROOT = Path(__file__).resolve().parents[2]
SRC = ROOT / "research" / "datos" / "2026-10-14-nichos-2"
FAMILIAS = ROOT / "research" / "datos" / "2026-10-14-familias-2.json"
DEDUP = ROOT / "research" / "datos" / "2026-10-14-deduplicacion-2.json"
REGISTRO = ROOT / "research" / "datos" / "registro-de-ideas.csv"
OUT = Path(sys.argv[1]) if len(sys.argv) > 1 else ROOT / "NICHOS-Y-PROBLEMAS-2.xlsx"
FECHA = "2026-10-14"

CRITERIOS = ["mercado", "hueco_ar", "fit_app_ia", "fit_facu", "regulacion_facilidad"]

HEADER_FILL = PatternFill("solid", fgColor="1F3864")
HEADER_FONT = Font(bold=True, color="FFFFFF")
NICHO_FILLS = ["DDEBF7", "FCE4D6", "E2EFDA", "FFF2CC", "EDEDED",
               "D9E1F2", "F8CBAD", "C6E0B4", "FFE699", "DBDBDB",
               "BDD7EE", "F4B084", "A9D08E", "FFD966", "D0CECE",
               "B4C6E7", "F2DCDB", "D8E4BC", "FDE9D9", "E4DFEC"]
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
            if p.get("presencia_ar_detalle"):
                r["presencia_ar"] = p.get("presencia_ar", r.get("presencia_ar"))
                r["presencia_ar_detalle"] = (f"[{etiqueta}] {p.get('presencia_ar_detalle', '')}"
                                             f" || [{previa}] {r.get('presencia_ar_detalle', '')}")
            if p.get("hueco_ar") is not None:
                r.setdefault("puntajes", {})["hueco_ar"] = p["hueco_ar"]
            for k in ("solucion_1", "solucion_2"):
                if isinstance(p.get(k), dict):
                    r[k] = p[k]
            if p.get("nota"):
                r["notas_puntaje"] = f"{r.get('notas_puntaje', '')} | {etiqueta}: {p['nota']}"
            r["_parcheada"] = True
            n += 1
    return n


def ref_text(refs, nombres):
    out = []
    for x in [x.strip() for x in refs.split(",") if x.strip()]:
        key = x.split(" ")[0]
        # "L14 (propia)" es la idea propia de Facu; "L14" a secas puede ser la de las 633: se busca primero el texto completo
        nombre = nombres.get(x) or nombres.get(x.split(":")[0].strip()) or nombres.get(key, "")
        out.append(f"{x}: {nombre[:70]}" if nombre else x)
    return " | ".join(out)


def apply_dedup(rows, avisos):
    """Regla N.º 2: separa las filas que repiten investigaciones anteriores y fusiona las repetidas entre nichos."""
    if not DEDUP.exists():
        for r in rows:
            r["_estado"], r["_nueva"] = "N", "nueva"
        return rows, [], 0
    d = json.loads(DEDUP.read_text(encoding="utf-8"))
    nombres = {}
    with REGISTRO.open(encoding="utf-8-sig") as fh:
        for x in csv.DictReader(fh):
            nombres[x["id"]] = f"{x['nombre_o_problema']} [{x['decision_facu'].split(' (')[0]}]"
            nombres.setdefault(x["id"].split(" ")[0], nombres[x["id"]])
    by_id = {r["id"]: r for r in rows}
    for r in rows:
        c = d["cruce"].get(r["id"])
        if c is None:
            avisos.append(f"sin dato de deduplicación: {r['id']}")
            c = {"estado": "N", "repite_o_se_parece_a": ""}
        r["_estado"] = c["estado"]
        r["_ref"] = ref_text(c.get("repite_o_se_parece_a", ""), nombres)
        r["_ref_nota"] = c.get("nota", "")
        r["_nueva"] = {"N": "nueva", "P": f"parecida a un ganador: {r['_ref']}", "C": f"repite {r['_ref']}",
                       "R": f"parecida a algo NO elegido: {r['_ref']}"}[c["estado"]]
    quitar = set()
    for f in d.get("fusiones", []):
        canon = by_id[f["canonica"]]
        otros = [by_id[x] for x in f["miembros"] if x != f["canonica"]]
        # los "sin buscar" tienen hueco provisorio: no cuentan para el mínimo
        buscadas = [m for m in [canon] + otros if str(m.get("presencia_ar", "")).strip().lower() != "sin buscar"]
        huecos = [num((m.get("puntajes") or {}).get("hueco_ar")) for m in buscadas]
        huecos = [h for h in huecos if isinstance(h, (int, float))]
        if buscadas and buscadas[0] is not canon and str(canon.get("presencia_ar", "")).strip().lower() == "sin buscar":
            canon["presencia_ar"] = buscadas[0].get("presencia_ar")
            canon["presencia_ar_detalle"] = (f"[de la fila fusionada {buscadas[0]['id']}] {buscadas[0].get('presencia_ar_detalle', '')}"
                                             f" || [{canon['id']}] {canon.get('presencia_ar_detalle', '')}")
        if huecos and (min(huecos) < num(canon["puntajes"]["hueco_ar"]) or buscadas[0] is not canon):
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
    repetidas = [r for r in rows if r["_estado"] in ("C", "R")]
    unicas = [r for r in rows if r["_estado"] not in ("C", "R") and r["id"] not in quitar]
    return unicas, repetidas, len(quitar - {r["id"] for r in repetidas})


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
        data = [r for r in data if not str(r.get("id", "")).startswith("_")]
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
    ("Tipo de solución", 16), ("Cómo usa IA", 40), ("Patrón CEMEVA", 10), ("Conocimiento de Facu", 18), ("Producto global o a medida", 24), ("Regulación (detalle)", 30),
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
             r.get("conocimiento_facu", ""), r.get("producto_global", ""), r.get("regulacion", ""), r.get("notas_puntaje", ""),
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
    pn_cols = [("Nicho", 26), ("Investigadas", 11), ("Salieron (repetidas o parecidas a no elegidas)", 13), ("Fusionadas en otra fila", 11),
               ("Quedan", 9), ("Nuevas", 9), ("Parecidas a ganadores", 10), ("Total promedio /25", 11), ("Mejor total", 9),
               ("Con hueco en AR (4-5)", 11), ("Los 3 mejores (ID: problema)", 80)]
    style_header(pn, pn_cols)
    ids_quedan = {r["id"] for r in rows}
    for n in nichos:
        todas_n = [r for r in todas if r.get("nicho") == n]
        rep_n = [r for r in todas_n if r["_estado"] in ("C", "R")]
        fus_n = [r for r in todas_n if r["_estado"] not in ("C", "R") and r["id"] not in ids_quedan]
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
               ("Motivo", 22), ("Repite o se parece a (idea anterior y decisión de Facu)", 50), ("Nota de la limpieza", 40), ("Total /25", 9),
               ("Solución 1 (afuera)", 26), ("Solución 2 (afuera)", 26), ("Presencia en Argentina", 12),
               ("Qué hay en Argentina", 60)]
    style_header(ya, ya_cols)
    for r in sorted(repetidas, key=lambda r: (-(total_of(r) or 0), r["id"])):
        motivo = "repite algo anterior" if r["_estado"] == "C" else "parecida a algo que Facu no eligió"
        ya.append([r["id"], r.get("nicho"), r.get("especialidad"), r.get("problema"), motivo, r.get("_ref"),
                   r.get("_ref_nota", ""), total_of(r), sol_cols(r.get("solucion_1"))[0],
                   sol_cols(r.get("solucion_2"))[0], r.get("presencia_ar", ""), r.get("presencia_ar_detalle", "")])
        rr = style_row(ya, len(ya_cols), {1, 8, 11}, 60)
        ya.cell(row=rr, column=2).fill = fill_by_nicho.get(r.get("nicho"), PatternFill())
    ya.freeze_panes = "E2"
    ya.auto_filter.ref = f"A1:{get_column_letter(len(ya_cols))}{ya.max_row}"

    # ---------- Hoja Cómo leer ----------
    cl = wb.create_sheet("Cómo leer", 0)
    cl.column_dimensions["A"].width = 120
    tot_ver = sum(1 for r in todas for k in ("solucion_1", "solucion_2")
                  if norm_si_no((r.get(k) or {}).get("verificado")) == "sí")
    tot_nover = 2 * len(todas) - tot_ver
    sin_buscar = sum(1 for r in rows if str(r.get("presencia_ar", "")).strip().lower() == "sin buscar")
    n_rech = sum(1 for r in repetidas if r["_estado"] == "R")
    lines = [
        ("NICHOS Y PROBLEMAS 2 — búsqueda nueva, sin repetir nada", True),
        (f"Armado el {FECHA} por Claude con 20 investigadores en paralelo (uno por nicho), una 2.ª pasada para la presencia en Argentina "
         "y una limpieza contra TODO lo investigado antes. Datos crudos: research/datos/2026-10-14-nichos-2/ (un JSON por nicho + parches/). "
         "Script: research/datos/build_nichos2_excel.py. Mismo formato que NICHOS-Y-PROBLEMAS.xlsx (que no se tocó).", False),
        ("", False),
        ("Para qué sirve", True),
        ("Es una búsqueda \"por las dudas\", pedida por Facu el 2026-10-14, con 20 nichos que NO se habían investigado. "
         "Se filtra junto con la hoja \"Fase 2\" de TODAS-LAS-IDEAS.xlsx (los 74 ganadores ordenados en \"Orden de Claude\").", False),
        ("", False),
        ("Cuántas quedaron (Regla N.º 2: no repetir nada)", True),
        (f"Se investigaron {len(todas)} problemas ({len(nichos)} nichos × 5 especialidades × 5). Cada fila se cruzó contra el registro completo "
         "(research/datos/registro-de-ideas.csv: las 633 ideas, las ideas propias de Facu y los 250 problemas de la búsqueda anterior; ganadores Y rechazados). "
         f"Salieron {len(repetidas)}: {len(repetidas) - n_rech} por repetir algo anterior y {n_rech} por parecerse a algo que Facu NO eligió, rechazó o descartó "
         "(para no volver a rechazarlas). Están en la hoja \"Ya estaban antes\", con la referencia y los datos nuevos. "
         f"Otras {fusionadas} eran el mismo problema en dos nichos nuevos y se fusionaron (columna \"También aparece en\"). "
         f"QUEDAN {len(rows)}: {n_nuevas} nuevas (verde en \"¿Es nueva?\") y {n_parecidas} parecidas a un GANADOR de Facu (sirven como variante; con la referencia).", False),
        ("Repetida = mismo problema y mismo tipo de cliente que algo anterior, aunque estuviera planteado distinto. "
         "Parecida = comparte cliente o un problema vecino. Es criterio de Claude, revisado fila por fila "
         "(datos: research/datos/2026-10-14-deduplicacion-2.json).", False),
        ("En las filas fusionadas, el \"Hueco en AR\" es el menor del grupo.", False),
        ("", False),
        ("Estructura", True),
        ("Nichos: " + ", ".join(nichos) + ". Las especialidades las eligió Claude y las aprobó Facu (2026-10-14); son estimación de tamaño, no un ranking verificado.", False),
        ("", False),
        ("Hojas", True),
        ("Problemas: las que quedan, con todo el detalle. Columna \"Me gusta (Facu)\" para marcar sí / tal vez / no (o pintar la fila).", False),
        ("Ranking: las mismas filas ordenadas por el total. Es una vista para empezar, NO el filtro final.", False),
        ("Familias: agrupa los problemas que se repiten entre rubros (opinión de Claude).", False),
        ("Por nicho: cuántas se investigaron, cuántas salieron y cuántas quedan en cada nicho.", False),
        ("Ya estaban antes: las que salieron, con el motivo y la idea anterior. No se borran: sus datos enriquecen esa idea vieja.", False),
        ("", False),
        ("Puntajes (1 a 5 cada uno; total sobre 25) — son OPINIÓN del investigador, no datos", True),
        ("Mercado: tamaño del problema en Argentina y Latinoamérica.", False),
        ("Hueco en AR: 5 = no se encontró nada local en 2 búsquedas; 4 = nada en 1 búsqueda; 1 = ya está resuelto y es conocido acá.", False),
        ("Fit app/IA: 5 = se resuelve con software o IA construible con Claude; 1 = hardware pesado, red física o mucho capital.", False),
        ("Fit Facu: 5 = usa lo que sabe (stock y depósito, logística y fleteros, procesos, back-office de PyME).", False),
        ("Regulación: 5 = casi sin regulación (fácil); 1 = muy regulado.", False),
        ("Columna \"Producto global o a medida\": si serviría igual para muchos clientes (criterio de Facu) — opinión del investigador.", False),
        ("Ojo: fueron 20 investigadores distintos; los puntajes no son exactamente comparables entre nichos.", False),
        ("", False),
        ("Qué es dato y qué no (Regla N.º 1)", True),
        ("Soluciones de afuera: \"Verificada = sí\" = el investigador vio el sitio oficial o una fuente en esta sesión. \"no\" = tratarla como dudosa.", False),
        ("Tracción: casi siempre es lo que la empresa dice de sí misma (no auditado). \"sin dato\" = no se encontró.", False),
        ("Presencia en Argentina: sale de 1-2 búsquedas rápidas. \"No encontrada\" NO prueba que no exista; antes de avanzar, buscar a fondo. "
         "\"sin buscar\" = quedó sin búsqueda por la cuota.", False),
        ("Números del detalle y \"Cómo se resuelve hoy\": estimación salvo que digan la fuente. Leyes y normas: verificar en el Boletín Oficial.", False),
        ("", False),
        ("Resumen de verificación", True),
        (f"Investigadas: {len(todas)}. Soluciones de afuera verificadas: {tot_ver}. Sin verificar: {tot_nover}. "
         f"Filas actualizadas en la 2.ª pasada: {parcheadas}. Filas que quedan (de las {len(rows)}) sin búsqueda en Argentina: {sin_buscar}.", False),
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
          f"| parecidas a no elegidas={n_rech} | quedan={len(rows)} (nuevas={n_nuevas}, parecidas a ganadores={n_parecidas}) | verificadas={tot_ver} | sin búsqueda AR={sin_buscar}")
    for a in avisos:
        print("aviso:", a)


if __name__ == "__main__":
    build()
