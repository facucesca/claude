# -*- coding: utf-8 -*-
"""Aplica el resultado de la etapa A: verificación de ideas, del contraste e ideas nuevas de la 2.ª pasada.
Uso: python -I -X utf8 merge_etapa_a.py <carpeta_salidas> <etapa-a.json>"""
import sys, json, pathlib, subprocess, collections
D = pathlib.Path(sys.argv[1]); R = json.load(open(sys.argv[2], encoding="utf-8")); R = R.get("result", R)
HERE = pathlib.Path(__file__).parent
print("motivo:", R.get("motivo"), "| pendientes:", R.get("pendientes"), "| fallidos:", R.get("fallidos")); print("usos:", R.get("usos"))
# 1) verificación de ideas
vf = D / "verif-etapa-a.json"; json.dump({"lotes": R.get("verif", [])}, open(vf, "w", encoding="utf-8"), ensure_ascii=False)
print(subprocess.run([sys.executable, "-I", "-X", "utf8", str(HERE / "merge_verif.py"), str(D / "ideas_final.json"), str(vf)], capture_output=True, text=True, encoding="utf-8").stdout)
# 2) contraste
cv = {}
for lote in R.get("contraste", []):
    for e in lote.get("empresas", []):
        comp = "; ".join(f"{c['nombre']} ({c['parecido']}): {c['que_hace'][:160]} — {c['url']}" for c in e.get("competidores_argentina", []))
        cv[e["clave"]] = {"existe_en_argentina": e["existe_en_argentina"], "detalle": (f"Competidores: {comp}\n" if comp else "") + e["detalle"],
                          "importabilidad_ajustada": e["importabilidad_ajustada"], "nota": e["nota"], "busquedas_hechas": e.get("busquedas_hechas")}
old = json.load(open(D / "contraste_verif.json", encoding="utf-8")) if (D / "contraste_verif.json").exists() else {}
old.update(cv); json.dump(old, open(D / "contraste_verif.json", "w", encoding="utf-8"), ensure_ascii=False, indent=1)
print(f"contraste: {len(cv)} empresas re-verificadas · " + str(dict(collections.Counter(x['existe_en_argentina'] for x in cv.values()))))
# 3) ideas nuevas de la 2.ª pasada
ideas = json.load(open(D / "ideas_final.json", encoding="utf-8")); ids = {i["id_tmp"] for i in ideas}
nxt = max(int(i["id_tmp"][1:]) for i in ideas if i["id_tmp"].startswith("N")) + 1
J = {j["id_tmp"]: j for j in ((R.get("juicios") or {}).get("juicios") or [])}
pmap = {}; nuevas = []
for gi, g in enumerate(R.get("gen", [])):
    for k, i in enumerate(g.get("ideas", [])):
        pid = f"P{gi + 1}-{k + 1}"; nid = f"N{nxt:03d}"; nxt += 1; pmap[pid] = nid
        d = dict(i); d["id_tmp"] = nid; d["angulo"] = g.get("key") or "segunda-pasada"; d["angulo_descripcion"] = (g.get("angulo") or "")[:300]; d["segunda_pasada"] = True
        nuevas.append((pid, d))
for pid, d in nuevas:
    j = J.get(pid)
    v = {"existe_en_argentina": d.get("existe_en_argentina"), "competidores_argentina": d.get("competidores_argentina", []), "evidencia_argentina": d.get("detalle_argentina", ""),
         "verificada_web": True, "verificada_en": "generación (2.ª pasada)", "fecha_verificacion": "2026-10-19"}
    if j:
        dup = (j.get("duplicada_de") or "").strip(); dup = pmap.get(dup, dup)
        d["estado_registro"] = j["estado_registro"]; d["parecidas_confirmadas"] = j.get("parecidas_confirmadas", [])
        d["duplicada_de"] = dup if dup in ids or dup in pmap.values() else ""
        v.update({"veredicto": "descartar" if d["duplicada_de"] else j["veredicto"], "score_ajustado": j["score_ajustado"], "nota_para_facu": j["nota_para_facu"], "nota_juez": j["nota_para_facu"]})
    else:
        d["estado_registro"] = "nueva"; v.update({"veredicto": "sin juzgar", "score_ajustado": d.get("score"), "nota_para_facu": "Sin juez: la etapa se frenó antes de juzgar."})
    d["verificacion"] = v; ideas.append(d)
json.dump(ideas, open(D / "ideas_final.json", "w", encoding="utf-8"), ensure_ascii=False, indent=1)
with open(D / "indice-titulos.txt", "w", encoding="utf-8") as f:
    for i in ideas: f.write(f"{i['id_tmp']} [{i.get('angulo','')}] {i['titulo']} — {i.get('una_linea','')[:160]}\n")
viv = [d for _, d in nuevas if d["estado_registro"] != "repetida" and d["verificacion"].get("veredicto") != "descartar"]
print(f"2.ª pasada: {len(nuevas)} ideas nuevas · vivas {len(viv)} · " + str(dict(collections.Counter((d['angulo'], d['estado_registro'], d['verificacion'].get('veredicto')) for _, d in nuevas))))
for d in viv: print(f"  {d['id_tmp']} [{d['angulo']}] {d['titulo'][:70]} · AR: {d['verificacion'].get('existe_en_argentina')}")
