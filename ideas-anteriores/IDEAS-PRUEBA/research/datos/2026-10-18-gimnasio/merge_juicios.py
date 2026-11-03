# -*- coding: utf-8 -*-
"""Aplica los juicios al JSON de ideas. Uso: python -I -X utf8 merge_juicios.py <ideas_dedup.json> <ideas_final.json> <juicios1.json> [<juicios2.json> ...]
Cada juicios*.json es el 'result' del workflow juez: {lotes:[{lote, juicios:[...]}]}"""
import sys, json, collections
ideas = json.load(open(sys.argv[1], encoding="utf-8")); out = sys.argv[2]
J = {}
for p in sys.argv[3:]:
    r = json.load(open(p, encoding="utf-8"))
    r = r.get("result", r)
    for lote in r.get("lotes", []):
        for j in lote.get("juicios", []): J[j["id_tmp"]] = j
by_id = {i["id_tmp"]: i for i in ideas}
for i in ideas:
    j = J.get(i["id_tmp"])
    if not j:
        i["estado_registro"] = i.get("estado_registro", "nueva"); i["verificacion"] = i.get("verificacion") or {}; continue
    i["estado_registro"] = j["estado_registro"]
    i["parecidas_confirmadas"] = j.get("parecidas_confirmadas", [])
    i["duplicada_de"] = j.get("duplicada_de", "") or ""
    ver = {"veredicto": j["veredicto"], "score_ajustado": j["score_ajustado"], "nota_para_facu": j["nota_para_facu"]}
    if i["duplicada_de"] and i["duplicada_de"] != i["id_tmp"] and i["duplicada_de"] in by_id:
        ver["veredicto"] = "descartar"
        ver["nota_para_facu"] = f"Duplicada de {i['duplicada_de']} ({by_id[i['duplicada_de']]['titulo']}). " + ver["nota_para_facu"]
    i["verificacion"] = ver
json.dump(ideas, open(out, "w", encoding="utf-8"), ensure_ascii=False, indent=1)
c = collections.Counter((i["estado_registro"], (i.get("verificacion") or {}).get("veredicto", "sin juzgar")) for i in ideas)
vivas = [i for i in ideas if i["estado_registro"] != "repetida" and (i.get("verificacion") or {}).get("veredicto") != "descartar"]
print(f"{len(ideas)} ideas · juzgadas {len(J)} · vivas {len(vivas)}"); 
for k, v in sorted(c.items()): print("  ", k, v)
