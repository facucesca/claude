"""Junta las ideas de los 6 ángulos, marca parecidos con lo anterior y arma el Excel.

Uso (desde la raíz del proyecto):
    python3 investigaciones/datos/2026-11-03/build_excel.py

Entradas: a*.json (ideas), exclusion.txt (todo lo anterior), descartes.json (opcional:
{"<titulo>": "motivo"} para sacar ideas a mano después de revisar los parecidos).
Salidas: investigaciones/2026-11-03-IDEAS-A-GRAN-ESCALA.xlsx, parecidos.json, ideas.json
"""
import json, re, unicodedata
from pathlib import Path
from openpyxl import Workbook
from openpyxl.styles import Alignment, Font, PatternFill
from openpyxl.utils import get_column_letter

AQUI = Path(__file__).parent
RAIZ = AQUI.parents[2]
SALIDA = RAIZ / "investigaciones" / "2026-11-03-IDEAS-A-GRAN-ESCALA.xlsx"

ANGULOS = {
    "a1": "Megatendencias 2030-2045",
    "a2": "Ventajas de Argentina hacia el mundo",
    "a3": "Deeptech y ciencia a producto",
    "a4": "Industria pesada y B2B",
    "a5": "Picos y palas de las nuevas olas",
    "a6": "Modelos grandes que no son una app",
}
PESOS = ["escala", "mercado", "por_que_ahora", "hueco", "construible", "riesgo_bajo", "ventaja_propia"]

VACIAS = set("""de la el los las un una unos unas y o en para por con sin a al del que se su sus
es como mas más muy entre sobre hacia desde ya no si lo le les mi tu e u x vs etc tipo hace
hacen todo toda todos cada otro otra otros""".split())


def norm(t):
    t = unicodedata.normalize("NFKD", str(t).lower())
    t = "".join(c for c in t if not unicodedata.combining(c))
    return [w[:6] for w in re.findall(r"[a-z0-9]{3,}", t) if w not in VACIAS]


def texto(v):
    if isinstance(v, list):
        return "\n".join(texto(x) for x in v)
    if isinstance(v, dict):
        return "; ".join(f"{k}: {texto(x)}" for k, x in v.items())
    return "" if v is None else str(v)


def cargar():
    ideas = []
    for f in sorted(AQUI.glob("a[0-9]-*.json")):
        clave = f.name[:2]
        for i, d in enumerate(json.loads(f.read_text(encoding="utf-8")), 1):
            d["id"] = f"N{clave[1]}-{i:02d}"
            d["angulo"] = ANGULOS.get(clave, clave)
            p = d.get("puntajes") or {}
            d["total"] = sum(int(p.get(k, 0) or 0) for k in PESOS)
            ideas.append(d)
    return ideas


def parecidos(ideas):
    viejas = []
    for linea in (AQUI / "exclusion.txt").read_text(encoding="utf-8").splitlines():
        partes = linea.split(" | ")
        viejas.append((partes[0], linea, set(norm(" ".join(partes[1:])))))
    todas = viejas + [(d["id"], d["titulo"], set(norm(d["titulo"] + " " + d.get("en_una_linea", "")))) for d in ideas]
    res = {}
    for d in ideas:
        mio = set(norm(d["titulo"] + " " + d.get("en_una_linea", "")))
        cand = []
        for vid, txt, ws in todas:
            if vid == d["id"] or not ws:
                continue
            comun = mio & ws
            s = len(comun) / max(1, min(len(mio), len(ws)))
            if len(comun) >= 2 and s >= 0.34:
                cand.append((round(s, 2), vid, txt[:160]))
        res[d["id"]] = sorted(cand, reverse=True)[:5]
    return res


def ancho(ws, anchos):
    for i, w in enumerate(anchos, 1):
        ws.column_dimensions[get_column_letter(i)].width = w


def encabezado(ws, cols):
    ws.append(cols)
    for c in ws[1]:
        c.font = Font(bold=True, color="FFFFFF")
        c.fill = PatternFill("solid", fgColor="1F4E78")
        c.alignment = Alignment(wrap_text=True, vertical="top")
    ws.freeze_panes = "C2"


def main():
    ideas = cargar()
    par = parecidos(ideas)
    (AQUI / "parecidos.json").write_text(json.dumps(par, ensure_ascii=False, indent=1), encoding="utf-8")
    desc_f = AQUI / "descartes.json"
    descartes = json.loads(desc_f.read_text(encoding="utf-8")) if desc_f.exists() else {}
    vivas = [d for d in ideas if d["id"] not in descartes]
    fuera = [d for d in ideas if d["id"] in descartes]
    vivas.sort(key=lambda d: -d["total"])
    (AQUI / "ideas.json").write_text(json.dumps(ideas, ensure_ascii=False, indent=1), encoding="utf-8")

    wb = Workbook()
    ws = wb.active
    ws.title = "LEÉME"
    for fila in [
        ["IDEAS A GRAN ESCALA — investigación del 2026-11-03"],
        [""],
        [f"{len(vivas)} ideas nuevas, de 6 ángulos distintos. Ninguna repite lo de ideas-anteriores/ ni los juguetes."],
        [f"Salieron {len(fuera)} por parecerse a algo anterior o entre sí (hoja SALIERON)."],
        [""],
        ["Cómo leerlo:"],
        ["• Hoja IDEAS: ordenadas por puntaje total (máx. 35). Pintá de amarillo las que te interesan, verde las que querés que explique mejor, azul las buenísimas."],
        ["• Escribí lo que pienses en la columna 'Mis comentarios'."],
        ["• Puntajes 1 a 5 = OPINIÓN de Claude (5 = mejor). 'Riesgo bajo' 5 = poco riesgo."],
        ["• 'Plata para arrancar' es ESTIMACIÓN. Mercado, competencia y 'por qué ahora' llevan fuente; si dice 'no verificado' o 'estimación propia', es eso."],
        ["• Columna 'Se parece a': lo más cercano de lo anterior que revisamos, para que veas que no es lo mismo."],
        [""],
        ["Ángulos:"],
    ] + [[f"• {v}"] for v in ANGULOS.values()]:
        ws.append(fila)
    ws["A1"].font = Font(bold=True, size=14)
    ws.column_dimensions["A"].width = 140

    cols = ["#", "Idea", "Mis comentarios", "Total /35", "En una línea", "Ángulo", "Problema", "Quién paga",
            "Cómo gana plata", "Por qué escala", "Por qué ahora", "Mercado", "Competencia en el mundo",
            "Competencia en Argentina/LATAM", "Plata para arrancar (estimación)", "Horizonte", "Primer paso (30-90 días)",
            "Riesgos", "Ventaja de Facu", "Opinión de Claude"] + [f"P: {k.replace('_', ' ')}" for k in PESOS] + \
           ["Se parece a (revisado)", "Fuentes"]
    ws = wb.create_sheet("IDEAS")
    encabezado(ws, cols)
    for d in vivas:
        p = d.get("puntajes") or {}
        ws.append([d["id"], d.get("titulo"), "", d["total"], d.get("en_una_linea"), d["angulo"], d.get("problema"),
                   d.get("cliente_que_paga"), d.get("como_gana_plata"), d.get("por_que_escala"), texto(d.get("por_que_ahora")),
                   texto(d.get("mercado")), texto(d.get("competencia_mundo")), texto(d.get("competencia_argentina")),
                   texto(d.get("plata_para_arrancar")), d.get("horizonte"), texto(d.get("primer_paso")), texto(d.get("riesgos")),
                   texto(d.get("ventaja_facu")), d.get("opinion")] + [p.get(k) for k in PESOS] +
                  [texto(d.get("parecido_a")), texto(d.get("fuentes"))])
    for fila in ws.iter_rows(min_row=2):
        for c in fila:
            c.alignment = Alignment(wrap_text=True, vertical="top")
    ancho(ws, [7, 32, 30, 8, 45, 20] + [45] * 14 + [6] * 7 + [40, 50])
    ws.auto_filter.ref = ws.dimensions

    ws = wb.create_sheet("POR ÁNGULO")
    encabezado(ws, ["Ángulo", "Ideas", "Puntaje promedio", "Mejor idea", "Puntaje de la mejor"])
    for a in ANGULOS.values():
        g = [d for d in vivas if d["angulo"] == a]
        if g:
            m = max(g, key=lambda d: d["total"])
            ws.append([a, len(g), round(sum(d["total"] for d in g) / len(g), 1), m["titulo"], m["total"]])
    ancho(ws, [38, 8, 14, 50, 12])

    ws = wb.create_sheet("SALIERON")
    encabezado(ws, ["#", "Idea", "Por qué salió", "En una línea", "Ángulo"])
    for d in fuera:
        ws.append([d["id"], d.get("titulo"), descartes[d["id"]], d.get("en_una_linea"), d["angulo"]])
    ancho(ws, [7, 35, 60, 60, 25])

    SALIDA.parent.mkdir(parents=True, exist_ok=True)
    wb.save(SALIDA)
    print(f"{len(ideas)} ideas, {len(vivas)} vivas, {len(fuera)} fuera -> {SALIDA}")


if __name__ == "__main__":
    main()
