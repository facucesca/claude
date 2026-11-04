"""Arma el Excel de empresas de afuera (ronda 1 + ronda 2) con la lista corta marcada.

Uso (desde la raíz del proyecto): python3 investigaciones/datos/2026-11-04-afuera/build_excel.py
Entradas: f1-*.json, r2-*.json (empresas), lista_corta.json ({"<empresa contiene>": "motivo"}).
Salida: investigaciones/2026-11-04-EMPRESAS-DE-AFUERA.xlsx
"""
import json, re, sys
from pathlib import Path
from openpyxl import Workbook
from openpyxl.styles import Alignment, Font, PatternFill

AQUI = Path(__file__).parent
RAIZ = AQUI.parents[2]
sys.path.insert(0, str(AQUI.parent / "2026-11-03"))
from build_excel import texto, ancho, encabezado  # noqa: E402

REG = {"f1-china": "China", "f1-india": "India", "f1-asia-sudeste-japon-corea": "Sudeste Asiático, Japón y Corea",
       "f1-latam": "Latinoamérica", "f1-turquia-europa": "Turquía y Europa del sur/este",
       "f1-africa-medio-oriente": "África y Medio Oriente", "r2-eeuu-canada-australia": "EE.UU., Canadá y Australia",
       "r2-europa-norte": "Europa del norte", "r2-rusia-asia-central": "Rusia, Asia Central, Pakistán",
       "r2-china-india-2": "China e India (2.ª pasada)", "r2-agro-alimentos": "Agro y alimentos (mundo)",
       "r2-industria-construccion": "Industria y construcción (mundo)",
       "r3-salud-cuidado": "R3 Salud y cuidado", "r3-educacion-empleo": "R3 Educación y empleo",
       "r3-finanzas-seguros": "R3 Finanzas y seguros", "r3-retail-franquicias": "R3 Locales y franquicias",
       "r3-movilidad-logistica": "R3 Movilidad y logística", "r3-vivienda-inmobiliario": "R3 Vivienda e inmobiliario",
       "r3-agregadores": "R3 Agregadores (juntar chicos)", "r3-leyes-nuevas": "R3 Negocios por leyes nuevas"}
CAMPOS = ["que_hace", "problema_que_resuelve", "como_gana_plata", "traccion", "por_que_funciono_alla",
          "existe_esa_condicion_en_argentina", "argentina_hoy", "la_vuelta_para_argentina", "por_que_nos_necesitarian",
          "riesgos", "veredicto"]
TIT = ["Qué hace", "Problema que resuelve", "Cómo gana plata", "Tracción (verificada)", "Por qué funcionó allá",
       "¿Se da esa condición en Argentina?", "Qué hay en Argentina hoy", "La vuelta para Argentina",
       "Por qué nos necesitarían", "Riesgos", "Veredicto (opinión)"]


def puntaje(v):
    m = re.search(r"(\d+(?:[.,]\d)?)\s*/\s*10", texto(v))
    return float(m.group(1).replace(",", ".")) if m else None


def main():
    corta = json.loads((AQUI / "lista_corta.json").read_text(encoding="utf-8"))
    filas = []
    vistos = set()
    for f in sorted(list(AQUI.glob("f1-*.json")) + list(AQUI.glob("r2-*.json")) + list(AQUI.glob("r3-*.json"))):
        if "descart" in f.name:
            continue
        d = json.loads(f.read_text(encoding="utf-8"))
        items = d.get("empresas", []) if isinstance(d, dict) else d
        for x in items:
            emp = texto(x.get("empresa"))
            motivo = next((m for k, m in corta.items() if k.lower() in emp.lower()), "")
            corto = re.split(r" \(| —| -", emp)[0].strip().lower()
            if motivo and not motivo.startswith("FUERA") and corto in vistos:
                motivo = "FUERA: repetida (aparece en otra fila)"
            vistos.add(corto)
            filas.append((f.stem, emp, x, motivo))
    filas.sort(key=lambda t: (t[3] == "", t[3].startswith("FUERA"), -(puntaje(t[2].get("veredicto")) or 0)))

    wb = Workbook()
    ws = wb.active
    ws.title = "LEÉME"
    vivas = [t for t in filas if t[3] and not t[3].startswith("FUERA")]
    for fila in [["EMPRESAS DE AFUERA QUE NO EXISTEN EN ARGENTINA — 2026-11-04"], [""],
                 [f"{len(filas)} empresas reales con tracción comprobada (ronda 1: 74, ronda 2: 61, ronda 3: {len(filas) - 135})."],
                 [f"{len(vivas)} en la LISTA CORTA (columna 'Lista corta'), elegidas por Claude con el filtro duro (Regla N.º 3)."],
                 ["Filtro: tracción real, no existe en Argentina, la condición que la hizo funcionar se da acá, la plata pasa por el negocio, hay barrera, no repite nada anterior."],
                 ["Puntaje = opinión del explorador (1-10). Tracción con links; lo no verificado dice 'no verificado'."],
                 ["Marcá: amarillo = me interesa, verde = explicame mejor, azul = buenísima. Comentá en 'Mis comentarios'."],
                 ["Las descartadas de cada explorador (con motivo) están en investigaciones/datos/2026-11-04-afuera/*descart*."]]:
        ws.append(fila)
    ws["A1"].font = Font(bold=True, size=14)
    ws.column_dimensions["A"].width = 140

    ws = wb.create_sheet("EMPRESAS")
    encabezado(ws, ["Empresa", "Mis comentarios", "Lista corta", "Puntaje", "País", "Región / ángulo", "Año", "Web"] + TIT +
               ["Se parece a", "Fuentes"])
    amarillo = PatternFill("solid", fgColor="FFF2CC")
    for stem, emp, x, motivo in filas:
        ws.append([emp, "", motivo, puntaje(x.get("veredicto")), texto(x.get("pais")), REG.get(stem, stem),
                   texto(x.get("anio_fundacion")), texto(x.get("web"))] + [texto(x.get(c)) for c in CAMPOS] +
                  [texto(x.get("parecido_a")), texto(x.get("fuentes"))])
        if motivo and not motivo.startswith("FUERA"):
            ws.cell(ws.max_row, 3).fill = amarillo
    for fila in ws.iter_rows(min_row=2):
        for c in fila:
            c.alignment = Alignment(wrap_text=True, vertical="top")
    ancho(ws, [30, 30, 30, 8, 18, 24, 7, 25] + [45] * 11 + [35, 50])
    ws.auto_filter.ref = ws.dimensions
    ws.freeze_panes = "B2"
    out = RAIZ / "investigaciones" / "2026-11-04-EMPRESAS-DE-AFUERA.xlsx"
    wb.save(out)
    print(len(filas), "empresas,", len(vivas), "en lista corta ->", out)


if __name__ == "__main__":
    main()
