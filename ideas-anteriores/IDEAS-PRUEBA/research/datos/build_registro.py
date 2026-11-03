# Registro único de TODO lo que ya se investigó en el proyecto (Regla N.º 2 del CLAUDE.md: no repetir).
# Genera research/datos/registro-de-ideas.csv. Correrlo después de cada investigación nueva.
# Incluye TODO: lo que Facu eligió y lo que no eligió o descartó (columna decision_facu). Nada de esto se vuelve a proponer.
# Incluye las 2 búsquedas de nichos (2026-10-13 y 2026-10-14).
# Uso: python research/datos/build_registro.py
import csv
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
D = ROOT / "research" / "datos"
OUT = D / "registro-de-ideas.csv"

# Ideas propias de Facu (ideas/LISTA-DE-IDEAS.md, hoja "Fase 2")
PROPIAS = [
    ("A1", "Intermediario de pagos seguros con el exterior (escrow)"),
    ("A2", "Calculadora web de índices de ingeniería industrial + consultoría paga"),
    ("A3", "Visualizador de indumentaria y merchandising personalizado"),
    ("A4", "Traer a Argentina lo que funciona en EE.UU. (método)"),
    ("L1", "App intermediaria para compradores / cierre seguro de autos usados"),
    ("L2", "App para sacar fotos a los precios del súper y saber cuánto llevás"),
    ("L3", "Automatización absoluta de clips para apps que pagan por vistas"),
    ("L4", "Revivir con IA a seres queridos / homenaje"),
    ("L5", "IA analista de negocios (rentabilidad con fórmulas)"),
    ("L6", "Uber de la logística empresarial (unir cargas con transportistas)"),
    ("L7", "App de huella de carbono para personas o empresas"),
    ("L8", "Edición de video automática para inmobiliarias y concesionarias"),
    ("L9", "Página de cálculos de ingeniería (stock, ABC, Pareto) + 1:1"),
    ("L10", "Stock con IA y cámara para súper / auditoría de góndola por foto"),
    ("L11", "Plataforma de aprendizaje confiable (contra info dispersa y cursos truchos)"),
    ("L12", "Cámaras de seguridad con IA en Argentina (une L10 + COM-2-4 + COM-4-4)"),
    ("L13", "RFID para otras cosas / stickers, algo distinto"),
    ("L14", "Stock de piezas chicas (mercerías, bulonerías, ferreterías, multimarcas), adaptable y anti-robo; ¿por peso?"),
    ("L15", "Intercambiar efectivo por transferencia en puntos físicos, con la app custodiando la plata"),
]


def decisiones():
    """Qué decidió Facu con cada código, separado por origen (los códigos L y A se repiten entre las 633 y sus ideas propias).
    Devuelve {"633": {...}, "propias": {...}, "nichos": {...}} con (decisión, nivel en 'Orden de Claude')."""
    dec = {"633": {}, "propias": {}, "nichos": {}}
    orden = D / "2026-10-14-orden-fase2.json"
    if not orden.exists():
        return dec
    destino = {"A": "propias", "D": "propias", "B": "633", "C": "nichos"}
    for f in json.loads(orden.read_text(encoding="utf-8"))["filas"]:
        for cod in [c.strip() for c in f["codigo"].split("+")]:
            dec[destino[f["bloque"]]][cod] = ("elegida (está en Fase 2)", f["nivel"])
    dec["propias"]["L15"] = ("DESCARTADA por Facu (2026-10-14)", "")
    dec["propias"]["A2"] = ("elegida (variante de C34, en Fase 2)", dec["633"].get("C34", ("", ""))[1])
    dec["propias"]["A4"] = ("método (= F36), no es una idea", "")
    dec["propias"]["A1"] = ("propia, con ficha en ideas/ (no está en Fase 2)", "")
    return dec


def main():
    dec = decisiones()
    no_elegida = ("NO elegida por Facu (no la marcó o la rechazó)", "")
    filas = []
    for i in json.loads((D / "2026-10-02-todas-las-ideas.json").read_text(encoding="utf-8")):
        d = dec["633"].get(i["id"], no_elegida)
        filas.append([i["id"], i["nombre"], i.get("categoria", ""), "TODAS-LAS-IDEAS.xlsx (2026-10-02)", "idea", "", d[0], d[1]])
    for k, n in PROPIAS:
        d = dec["propias"].get(k, ("propia de Facu", ""))
        filas.append([f"{k} (propia)", n, "Idea propia de Facu", "ideas/LISTA-DE-IDEAS.md + hoja Fase 2", "idea", "", d[0], d[1]])
    dedup = json.loads((D / "2026-10-13-deduplicacion.json").read_text(encoding="utf-8"))
    fusion_de = {x: f["canonica"] for f in dedup["fusiones"] for x in f["miembros"] if x != f["canonica"]}
    for f in sorted((D / "2026-10-13-nichos").glob("*.json")):
        for r in json.loads(f.read_text(encoding="utf-8")):
            c = dedup["cruce"].get(r["id"], {})
            est = {"N": "nueva", "P": "parecida", "C": "repetida"}.get(c.get("estado"), "")
            ref = c.get("repite_o_se_parece_a", "")
            if r["id"] in fusion_de:
                est, ref = "fusionada", f"fusionada en {fusion_de[r['id']]}"
            if r["id"] in dec["nichos"]:
                d = dec["nichos"][r["id"]]
            elif est == "repetida":
                d = ("repetía una idea anterior (ver referencia)", "")
            elif est == "fusionada":
                d = dec["nichos"].get(fusion_de[r["id"]], no_elegida)
            else:
                d = no_elegida
            filas.append([r["id"], r["problema"], f"{r.get('nicho')} / {r.get('especialidad')}",
                          "NICHOS-Y-PROBLEMAS.xlsx (2026-10-13)", est, ref, d[0], d[1]])
    # Búsqueda 2 (2026-10-14, 20 nichos nuevos). Estados: N nueva, P parecida a ganador, C repite, R parecida a algo no elegido.
    d2 = D / "2026-10-14-deduplicacion-2.json"
    if d2.exists():
        dedup2 = json.loads(d2.read_text(encoding="utf-8"))
        fusion2 = {x: f["canonica"] for f in dedup2["fusiones"] for x in f["miembros"] if x != f["canonica"]}
        pendiente = ("pendiente: Facu todavía no marcó NICHOS-Y-PROBLEMAS-2", "")
        MARCADAS2 = {"PET-1-3", "SEG-3-4", "HOG-3-2", "ALQ-2-3", "TEL-5-5", "EVE-4-5", "SEG-2-5", "MOV-2-5"}  # marcadas por Facu el 2026-10-20
        elegida2 = ("elegida (marcada en NICHOS-Y-PROBLEMAS-2, 2026-10-20)", "")
        for f in sorted((D / "2026-10-14-nichos-2").glob("*.json")):
            for r in json.loads(f.read_text(encoding="utf-8")):
                if str(r.get("id", "")).startswith("_"):
                    continue
                c = dedup2["cruce"].get(r["id"], {})
                est = {"N": "nueva", "P": "parecida a ganador", "C": "repetida",
                       "R": "parecida a no elegida"}.get(c.get("estado"), "")
                ref = c.get("repite_o_se_parece_a", "")
                if est == "repetida":
                    d = ("repetía una idea anterior (ver referencia)", "")
                elif est == "parecida a no elegida":
                    d = ("salió: parecida a algo que Facu no eligió (ver referencia)", "")
                elif r["id"] in fusion2:
                    est, ref, d = "fusionada", f"fusionada en {fusion2[r['id']]}", pendiente
                else:
                    d = pendiente
                if r["id"] in MARCADAS2:
                    d = elegida2
                filas.append([r["id"], r["problema"], f"{r.get('nicho')} / {r.get('especialidad')}",
                              "NICHOS-Y-PROBLEMAS-2.xlsx (2026-10-14)", est, ref, d[0], d[1]])
    # Gimnasio de ideas (2026-10-18): lentes de libros + patrones + contraste EE.UU.-AR + ideas web. Decisión de Facu pendiente.
    g = D / "2026-10-18-gimnasio-ideas.json"
    if g.exists():
        for r in json.loads(g.read_text(encoding="utf-8")):
            filas.append([r["id"], r["nombre"], r.get("categoria", ""), "GIMNASIO-DE-IDEAS.xlsx (2026-10-18)",
                          r.get("estado", "nueva"), r.get("referencia", ""),
                          r.get("decision", "pendiente: Facu todavía no marcó GIMNASIO-DE-IDEAS"), ""])
    with OUT.open("w", encoding="utf-8-sig", newline="") as fh:
        w = csv.writer(fh)
        w.writerow(["id", "nombre_o_problema", "categoria_o_nicho", "origen", "estado", "repite_o_referencia",
                    "decision_facu", "nivel_orden_claude"])
        w.writerows(filas)
    from collections import Counter
    print(f"ok: {OUT} | {len(filas)} entradas | decisiones: {dict(Counter(f[6].split(' (')[0] for f in filas))}")


if __name__ == "__main__":
    main()
