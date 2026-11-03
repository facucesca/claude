# -*- coding: utf-8 -*-
"""Junta las ideas de los journals de los workflows generadores en un solo JSON plano.
Uso: python -I consolidate.py <salida.json> <journal1> <journal2> ...
"""
import sys, json, re
out = sys.argv[1]; ideas = []; vistos = set(); resumen = []
for jp in sys.argv[2:]:
    labels = {}
    lines = [l for l in open(jp, encoding="utf-8")]
    for line in lines:
        try: e = json.loads(line)
        except Exception: continue
        if e.get("type") == "started": labels[e.get("agentId")] = e.get("label", "")
    for line in lines:
        try: e = json.loads(line)
        except Exception: continue
        if e.get("type") != "result": continue
        key = labels.get(e.get("agentId"), "") or e.get("key", "") or ""
        m = re.search(r"gen:([a-z0-9\-]+)", key)
        angulo = m.group(1) if m else key[:40]
        if angulo in vistos: continue
        vistos.add(angulo)
        r = e.get("result") or {}
        n = 0
        for idea in r.get("ideas", []):
            idea = dict(idea); idea["angulo"] = angulo
            idea["angulo_descripcion"] = (r.get("angulo") or "")[:300]
            ideas.append(idea); n += 1
        resumen.append((angulo, n, len(r.get("descartadas_por_repetidas", []))))
for k, i in enumerate(ideas, 1): i["id_tmp"] = f"N{k:03d}"
json.dump(ideas, open(out, "w", encoding="utf-8"), ensure_ascii=False, indent=1)
for a, n, d in resumen: print(f"  {a:34s} ideas={n:2d} descartadas_por_el_agente={d}")
print(f"TOTAL {len(ideas)} ideas de {len(resumen)} ángulos")
