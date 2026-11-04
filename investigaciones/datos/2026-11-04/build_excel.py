"""Junta las ideas de los 6 ángulos C (2026-11-04), marca parecidos y arma el Excel.

Uso (desde la raíz del proyecto):
    python3 investigaciones/datos/2026-11-04/build_excel.py

Entradas: c?-*.json (ideas), c?-lecciones.json, exclusion.txt, descartes.json (opcional:
{"<id>": "motivo"} para sacar ideas a mano después de revisar los parecidos).
Salidas: investigaciones/2026-11-04-IDEAS-NICHOS-Y-APPS.xlsx, ideas.json, parecidos.json
"""
import json, re, sys
from pathlib import Path
from openpyxl import Workbook
from openpyxl.styles import Alignment, Font, PatternFill
from openpyxl.utils import get_column_letter

AQUI = Path(__file__).parent
RAIZ = AQUI.parents[2]
sys.path.insert(0, str(AQUI.parent / "2026-11-03"))
from build_excel import norm, texto, ancho, encabezado  # noqa: E402

SALIDA = RAIZ / "investigaciones" / "2026-11-04-IDEAS-NICHOS-Y-APPS.xlsx"
ANGULOS = {
    "c1": "Nichos de salud",
    "c2": "Ingeniería industrial en una app",
    "c3": "Mundo real + IA + web",
    "c4": "Formas nuevas de pagar y cobrar",
    "c5": "Agregar valor a lo que ya existe",
    "c6": "Personas afectadas y nichos raros",
}
PESOS = ["facil_de_lanzar", "dolor_real", "escala", "hueco", "construible_con_claude", "riesgo_bajo", "impacto_en_personas"]


def verif(d):
    if not d.get("fuentes"):
        return "SIN VERIFICAR"
    t = json.dumps(d, ensure_ascii=False).lower()
    return "Parcial" if ("no verific" in t or "sin verific" in t or "no pude verificar" in t) else "Sí"


def cargar():
    ideas = []
    for f in sorted(AQUI.glob("c[0-9]-*.json")):
        if "lecciones" in f.name:
            continue
        clave = f.name[:2]
        for i, d in enumerate(json.loads(f.read_text(encoding="utf-8")), 1):
            d["id"] = f"{clave.upper()}-{i:02d}"
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


def main():
    ideas = cargar()
    (AQUI / "parecidos.json").write_text(json.dumps(parecidos(ideas), ensure_ascii=False, indent=1), encoding="utf-8")
    (AQUI / "ideas.json").write_text(json.dumps(ideas, ensure_ascii=False, indent=1), encoding="utf-8")
    df = AQUI / "descartes.json"
    descartes = json.loads(df.read_text(encoding="utf-8")) if df.exists() else {}
    vivas = sorted([d for d in ideas if d["id"] not in descartes], key=lambda d: -d["total"])
    fuera = [d for d in ideas if d["id"] in descartes]

    wb = Workbook()
    ws = wb.active
    ws.title = "LEÉME"
    for fila in [
        ["IDEAS EN NICHOS Y APPS — investigación del 2026-11-04"],
        [""],
        [f"{len(vivas)} ideas nuevas, chicas, en nichos, fáciles de lanzar con app/web/WhatsApp + IA."],
        [f"Salieron {len(fuera)} por repetidas o parecidas a algo anterior (hoja SALIERON). No repiten nada de ideas-anteriores/ ni del 2026-11-03."],
        [""],
        ["Cómo leerlo:"],
        ["• Hoja IDEAS: ordenadas por puntaje total (máx. 35). Amarillo = me interesa, verde = explicame mejor, azul = buenísima."],
        ["• 'Inspiración' = empresa real que ya existe y qué le cambiamos. 'Jugada mental' = cómo se llegó a la idea (para entrenar la cabeza)."],
        ["• Hoja LECCIONES: patrones para encontrar problemas, con ejemplos reales."],
        ["• Puntajes 1 a 5 = OPINIÓN de Claude. Precios y mercados sin fuente = ESTIMACIÓN."],
        ["• '¿Verificada?': Sí = con fuentes; Parcial = algún dato sin chequear; SIN VERIFICAR = confirmar antes de usar."],
        ["• Escribí en 'Mis comentarios'."],
    ]:
        ws.append(fila)
    ws["A1"].font = Font(bold=True, size=14)
    ws.column_dimensions["A"].width = 140

    cols = ["#", "Idea", "Mis comentarios", "Total /35", "¿Verificada?", "En una línea", "Ángulo", "Nicho",
            "Cuello de botella", "Solución", "Mundo real + IA + web", "Inspiración (empresa real)", "La vuelta",
            "Quién paga", "Cómo gana plata", "Por qué escala", "Competencia en Argentina", "Mercado",
            "Lanzar en 2 semanas", "Qué hace Claude", "Riesgos", "Jugada mental", "Opinión de Claude"] + \
           [f"P: {k.replace('_', ' ')}" for k in PESOS] + ["Se parece a (revisado)", "Fuentes"]
    ws = wb.create_sheet("IDEAS")
    encabezado(ws, cols)
    for d in vivas:
        p = d.get("puntajes") or {}
        ws.append([d["id"], d.get("titulo"), "", d["total"], verif(d)] +
                  [texto(d.get(k)) for k in ["en_una_linea"]] + [d["angulo"]] +
                  [texto(d.get(k)) for k in ["nicho", "cuello_de_botella", "solucion", "mundo_real_ia_web", "inspiracion",
                                             "la_vuelta", "cliente_que_paga", "como_gana_plata", "por_que_escala",
                                             "competencia_argentina", "mercado", "mvp_2_semanas", "como_ayuda_claude",
                                             "riesgos", "leccion", "opinion"]] +
                  [p.get(k) for k in PESOS] + [texto(d.get("parecido_a")), texto(d.get("fuentes"))])
    for fila in ws.iter_rows(min_row=2):
        for c in fila:
            c.alignment = Alignment(wrap_text=True, vertical="top")
    ancho(ws, [7, 32, 30, 8, 12, 45, 22, 25] + [45] * 15 + [6] * 7 + [40, 50])
    ws.auto_filter.ref = ws.dimensions

    ws = wb.create_sheet("LECCIONES")
    encabezado(ws, ["Ángulo", "Lección", "Cómo aplicarla", "Ejemplo real", "Fuente"])
    for f in sorted(AQUI.glob("c[0-9]-lecciones.json")):
        for l in json.loads(f.read_text(encoding="utf-8")):
            ws.append([ANGULOS.get(f.name[:2]), texto(l.get("leccion")), texto(l.get("como_aplicarla")),
                       texto(l.get("ejemplo_real")), texto(l.get("fuente"))])
    for fila in ws.iter_rows(min_row=2):
        for c in fila:
            c.alignment = Alignment(wrap_text=True, vertical="top")
    ancho(ws, [26, 45, 55, 55, 40])

    ws = wb.create_sheet("POR ÁNGULO")
    encabezado(ws, ["Ángulo", "Ideas", "Puntaje promedio", "Mejor idea", "Puntaje de la mejor"])
    for a in ANGULOS.values():
        g = [d for d in vivas if d["angulo"] == a]
        if g:
            m = max(g, key=lambda d: d["total"])
            ws.append([a, len(g), round(sum(d["total"] for d in g) / len(g), 1), m["titulo"], m["total"]])
    ancho(ws, [36, 8, 14, 50, 12])

    ws = wb.create_sheet("SALIERON")
    encabezado(ws, ["#", "Idea", "Por qué salió", "En una línea", "Ángulo"])
    for d in fuera:
        ws.append([d["id"], d.get("titulo"), descartes[d["id"]], d.get("en_una_linea"), d["angulo"]])
    ancho(ws, [7, 35, 60, 60, 25])

    wb.save(SALIDA)
    print(f"{len(ideas)} ideas, {len(vivas)} vivas, {len(fuera)} fuera -> {SALIDA}")


if __name__ == "__main__":
    main()
