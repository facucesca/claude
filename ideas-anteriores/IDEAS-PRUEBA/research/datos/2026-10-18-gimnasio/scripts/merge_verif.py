# -*- coding: utf-8 -*-
"""Aplica la verificación web a ideas_final.json (in place).
Uso: python -I -X utf8 merge_verif.py <ideas_final.json> <verif1.json> [<verif2.json> ...]
Cada verif*.json es el 'result' del workflow verificar-ideas-argentina: {lotes:[{verificaciones:[...]}], usos:[...]}"""
import sys, json, collections
P = sys.argv[1]; ideas = json.load(open(P, encoding="utf-8")); by = {i["id_tmp"]: i for i in ideas}
K = ("innovacion", "factibilidad_facu", "brecha_argentina", "por_que_ahora", "potencial")
def tot(s): return round(sum(float((s or {}).get(k, 0) or 0) for k in K) / 5, 2)
n = 0; cambios = []; antes = collections.Counter(); despues = collections.Counter(); deltas = []
for f in sys.argv[2:]:
    r = json.load(open(f, encoding="utf-8")); r = r.get("result", r)
    for lote in r.get("lotes", []):
        for x in lote.get("verificaciones", []):
            i = by.get(x["id_tmp"])
            if not i: print("id desconocido:", x["id_tmp"]); continue
            v = i.setdefault("verificacion", {})
            if "nota_juez" not in v:
                v["nota_juez"] = v.get("nota_para_facu", ""); v["score_juez"] = v.get("score_ajustado"); v["veredicto_juez"] = v.get("veredicto")
            gen = i.get("existe_en_argentina_generador") or i.get("existe_en_argentina")
            i["existe_en_argentina_generador"] = gen
            antes[gen] += 1; despues[x["existe_en_argentina"]] += 1
            deltas.append(tot(x["score_ajustado"]) - tot(v.get("score_juez")))
            v.update({"veredicto": x["veredicto"], "score_ajustado": x["score_ajustado"], "existe_en_argentina": x["existe_en_argentina"],
                      "evidencia_argentina": x["evidencia_argentina"], "evidencia_afuera": x["evidencia_afuera"],
                      "competidores_argentina": x["competidores_argentina"], "intentos_previos": x["intentos_previos"],
                      "nota_para_facu": x["nota_para_facu"], "fuentes_verificacion": x["fuentes"],
                      "busquedas_hechas": x["busquedas_hechas"], "verificada_web": True, "fecha_verificacion": "2026-10-19"})
            i["existe_en_argentina"] = x["existe_en_argentina"]
            if gen in ("no encontré nada", "no verificado") and x["existe_en_argentina"] in ("existe y compite", "existe parcial"):
                cambios.append(f'{i["id_tmp"]} {i["titulo"][:60]}: {gen} -> {x["existe_en_argentina"]} ({", ".join(c["nombre"] for c in x["competidores_argentina"][:3])})')
            n += 1
json.dump(ideas, open(P, "w", encoding="utf-8"), ensure_ascii=False, indent=1)
ver = [i for i in ideas if (i.get("verificacion") or {}).get("verificada_web")]
print(f"aplicadas {n} verificaciones · verificadas en total: {len(ver)}")
print("existe (generador) en este lote:", dict(antes)); print("existe (web) en este lote:", dict(despues))
print("veredictos web (total):", dict(collections.Counter(i["verificacion"]["veredicto"] for i in ver)))
if deltas: print(f"cambio de puntaje promedio vs juez: {sum(deltas)/len(deltas):+.2f} (min {min(deltas):+.2f}, max {max(deltas):+.2f})")
print("búsquedas promedio por idea:", round(sum(float(i["verificacion"].get("busquedas_hechas", 0) or 0) for i in ver) / max(len(ver), 1), 1))
print("de 'no existe' a 'existe':"); [print("  " + c) for c in cambios]
