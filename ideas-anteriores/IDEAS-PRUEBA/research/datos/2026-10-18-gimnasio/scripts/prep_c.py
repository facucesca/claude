# -*- coding: utf-8 -*-
"""Insumos locales de la etapa C y armado de la matriz (sin agentes).
Uso:
  python -I -X utf8 prep_c.py insumos <salidas> <insumos> <repo>     -> lentes-compactas.json, lentes_maestras.json, bitacora-formato.md
  python -I -X utf8 prep_c.py etiquetar <salidas>                    -> para-etiquetar.json (ideas vivas + empresas)
  python -I -X utf8 prep_c.py matriz <salidas> <tags.json>           -> matriz.json
  python -I -X utf8 prep_c.py fusionar <salidas>                     -> fusiona duplicadas en ideas_final.json
"""
import sys, json, re, pathlib, collections
modo = sys.argv[1]; D = pathlib.Path(sys.argv[2])
SECTORES = ["Hogar y oficios", "Salud y cuidado", "Autos y movilidad", "Logística y comercio exterior", "PyMEs y comercio", "Inmuebles y construcción",
            "Energía y agua", "Agro y alimentos", "Educación y trabajo", "Finanzas, seguros y trámites", "Ocio, turismo y eventos", "Comunidad y vida cotidiana"]
K = ("innovacion", "factibilidad_facu", "brecha_argentina", "por_que_ahora", "potencial")
def V(i): return i.get("verificacion") or {}
def tot(i):
    v = V(i).get("score_ajustado") or i.get("score") or {}
    return round(sum(float(v.get(k, 0) or 0) for k in K) / 5, 1)
def viva(i): return i.get("estado_registro") != "repetida" and V(i).get("veredicto") != "descartar"
def patrones_nombres():
    P = json.load(open(D / "patrones.json", encoding="utf-8"))
    return [re.sub(r"^\d+\.\s*", "", x["nombre"]).split(" (")[0].strip() for p in P["patrones"] for x in p["patrones"]]

if modo == "insumos":
    I = pathlib.Path(sys.argv[3]); R = pathlib.Path(sys.argv[4])
    L = json.load(open(D / "lentes.json", encoding="utf-8"))
    comp = [{"libro": b["libro"].split(",")[0].split(" — ")[0][:60], "lente": l["nombre"], "que_mirar": l["que_mirar"][:400], "pregunta": l["pregunta_generadora"], "referencia": l["referencia"][:120]}
            for b in L["libros"] for l in b["lentes"]]
    json.dump(comp, open(D / "lentes-compactas.json", "w", encoding="utf-8"), ensure_ascii=False, indent=0)
    t = (D / "sintesis-parte1.md").read_text(encoding="utf-8")
    sec = t[t.index("### Las 12 lentes maestras"):t.index("### Lo que los libros te dicen a vos")]
    out = []
    for row in sec.splitlines():
        m = re.match(r"^\|\s*(\d+)\s*\|\s*\*\*(.+?)\*\*\s*(.*?)\|\s*(.*?)\s*\|\s*(.*?)\s*\|\s*$", row)
        if m: out.append({"lente": m.group(2).strip().rstrip("."), "que_mirar": m.group(3).strip(), "pregunta": m.group(4).strip(), "libros": m.group(5).strip()})
    json.dump(out, open(D / "lentes_maestras.json", "w", encoding="utf-8"), ensure_ascii=False, indent=1)
    b = (R / "ideas" / "BITACORA-DE-PROBLEMAS.md").read_text(encoding="utf-8")
    (I / "bitacora-formato.md").write_text(b[:b.index("## Nichos para recorrer")], encoding="utf-8")
    print(f"lentes compactas: {len(comp)} · maestras: {len(out)} · bitácora: ok")

elif modo == "etiquetar":
    ideas = json.load(open(D / "ideas_final.json", encoding="utf-8")); P = json.load(open(D / "patrones.json", encoding="utf-8"))
    el = [{"id": i["id_tmp"], "titulo": i["titulo"], "una_linea": i.get("una_linea", "")[:300]} for i in ideas if viva(i)]
    el += [{"id": f"E:{s['sector']}||{e['empresa']}", "titulo": e["empresa"], "una_linea": e["que_hace"][:300]} for s in P["contraste"] for e in s["empresas"]]
    json.dump({"patrones": patrones_nombres(), "sectores": SECTORES, "elementos": el}, open(D / "para-etiquetar.json", "w", encoding="utf-8"), ensure_ascii=False, indent=0)
    print(f"para etiquetar: {len(el)} elementos")

elif modo == "matriz":
    tags = json.load(open(sys.argv[3], encoding="utf-8")); tags = tags.get("result", tags); tags = (tags.get("tags") or tags).get("etiquetas", [])
    ideas = {i["id_tmp"]: i for i in json.load(open(D / "ideas_final.json", encoding="utf-8")) if viva(i)}
    pats = patrones_nombres(); cell = collections.defaultdict(lambda: {"ideas": [], "emp": []})
    malos = 0
    for t in tags:
        sec = t["sector"] if t["sector"] in SECTORES else None
        for p in t["patrones"]:
            if p not in pats or not sec: malos += 1; continue
            if t["id"].startswith("E:"): cell[(p, sec)]["emp"].append(t["id"].split("||", 1)[1])
            elif t["id"] in ideas: cell[(p, sec)]["ideas"].append(ideas[t["id"]])
    filas = []
    for p in pats:
        celdas = {}; total = 0
        for s in SECTORES:
            c = cell.get((p, s));
            if not c: continue
            ni, ne = len(c["ideas"]), len(c["emp"]); total += ni + ne
            if ne and not ni: celdas[s] = f"HUECO: {ne} empresa(s) afuera ({', '.join(c['emp'][:3])}) y 0 ideas acá"
            elif ni:
                top = sorted(c["ideas"], key=lambda i: -tot(i))[:2]
                celdas[s] = f"{ni} idea(s): " + " · ".join(f"{i['titulo'][:45]} ({tot(i)})" for i in top) + (f" | {ne} empresa(s) afuera" if ne else "")
        filas.append({"patron": p, "celdas": celdas, "total": total})
    huecos = sorted([(len(c["emp"]), p, s, c["emp"]) for (p, s), c in cell.items() if c["emp"] and not c["ideas"]], reverse=True)
    llenos = sorted([(len(c["ideas"]), p, s) for (p, s), c in cell.items() if c["ideas"]], reverse=True)
    sin_uso = [p for p in pats if not any(cell.get((p, s), {}).get("ideas") for s in SECTORES)]
    por_sector = collections.Counter(t["sector"] for t in tags if not t["id"].startswith("E:") and t["id"] in ideas and t["sector"] in SECTORES)
    lectura = ["Huecos más grandes (el patrón funciona afuera en ese sector y no generamos ninguna idea acá): " + "; ".join(f"{p} en {s} ({n}: {', '.join(e[:3])})" for n, p, s, e in huecos[:6]),
               "Celdas más llenas (donde se amontonaron las ideas): " + "; ".join(f"{p} en {s} ({n})" for n, p, s in llenos[:6]),
               "Patrones que ninguna idea usa: " + (", ".join(sin_uso) if sin_uso else "ninguno"),
               "Ideas vivas por sector (cada idea cuenta una vez): " + ", ".join(f"{s}: {por_sector.get(s, 0)}" for s in SECTORES),
               f"Etiquetas descartadas por no coincidir con las listas: {malos}"]
    json.dump({"columnas": SECTORES, "filas": filas, "lectura": lectura}, open(D / "matriz.json", "w", encoding="utf-8"), ensure_ascii=False, indent=1)
    print("matriz ok:", len(filas), "patrones;"); [print(" -", x[:400]) for x in lectura]

elif modo == "fusionar":
    ideas = json.load(open(D / "ideas_final.json", encoding="utf-8")); by = {i["id_tmp"]: i for i in ideas}
    def raiz(i, seen=()):
        d = (i.get("duplicada_de") or "").strip()
        if not d or d == i["id_tmp"] or d not in by or d in seen: return i
        return raiz(by[d], seen + (i["id_tmp"],))
    n = 0
    for i in ideas:
        if not i.get("duplicada_de") or i.get("estado_registro") == "repetida": continue
        r = raiz(i)
        if r is i or not viva(r): continue
        i["fusionada_en"] = r["id_tmp"]
        fus = r.setdefault("fusionadas", [])
        if not any(f["id_tmp"] == i["id_tmp"] for f in fus):
            fus.append({"id_tmp": i["id_tmp"], "angulo": i.get("angulo"), "titulo": i["titulo"], "vuelta_de_tuerca": i.get("vuelta_de_tuerca", ""),
                        "palancas": i.get("palancas_para_retorcerla", []), "existe_afuera": i.get("existe_afuera", [])})
            known = {(e.get("empresa") or "").lower() for e in r.get("existe_afuera") or []}
            for e in i.get("existe_afuera") or []:
                if (e.get("empresa") or "").lower() not in known: r.setdefault("existe_afuera", []).append({**e, "dato": e.get("dato", "") + f" (aportado por {i['id_tmp']})"})
            n += 1
    json.dump(ideas, open(D / "ideas_final.json", "w", encoding="utf-8"), ensure_ascii=False, indent=1)
    print(f"fusionadas {n} duplicadas en {sum(1 for i in ideas if i.get('fusionadas'))} ideas vivas")
