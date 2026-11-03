# -*- coding: utf-8 -*-
"""Elige las ideas para las fichas a fondo y escribe ficha-<id>.json con la ficha completa.
Regla: ranking por puntaje final, con tope de 3 por ángulo, hasta N-3; después hasta 3 comodines con factibilidad >= 7 (las más lanzables para Facu).
Excluye las que tienen competencia directa en Argentina ("existe y compite").
Uso: python -I -X utf8 select_b.py <carpeta_salidas> <N>"""
import sys, json, pathlib, collections
D = pathlib.Path(sys.argv[1]); N = int(sys.argv[2])
K = ("innovacion", "factibilidad_facu", "brecha_argentina", "por_que_ahora", "potencial")
ideas = json.load(open(D / "ideas_final.json", encoding="utf-8"))
def V(i): return i.get("verificacion") or {}
def s(i, k): return float((V(i).get("score_ajustado") or i.get("score") or {}).get(k, 0) or 0)
def tot(i): return round(sum(s(i, k) for k in K) / 5, 2)
viv = [i for i in ideas if i.get("estado_registro") != "repetida" and V(i).get("veredicto") not in ("descartar", "sin juzgar") and V(i).get("existe_en_argentina") != "existe y compite"]
viv.sort(key=lambda i: (-tot(i), -s(i, "factibilidad_facu"), i["id_tmp"]))
sel = []; por = collections.Counter()
for i in viv:
    if len(sel) >= N - 3: break
    if por[i["angulo"]] >= 3: continue
    sel.append(i); por[i["angulo"]] += 1
for i in sorted([x for x in viv if x not in sel], key=lambda i: (-s(i, "factibilidad_facu"), -tot(i))):
    if len(sel) >= N: break
    if s(i, "factibilidad_facu") >= 7 and por[i["angulo"]] < 4: sel.append(i); por[i["angulo"]] += 1; i["_comodin"] = True
for i in sel:
    d = {k: v for k, v in i.items() if not k.startswith("_") and k not in ("sospechas_registro", "sospechas_internas")}
    json.dump(d, open(D / f"ficha-{i['id_tmp']}.json", "w", encoding="utf-8"), ensure_ascii=False, indent=1)
print(json.dumps([i["id_tmp"] for i in sel]))
for n, i in enumerate(sel, 1): print(f"{n:2d}. {i['id_tmp']} [{tot(i)}] {'(comodín) ' if i.get('_comodin') else ''}{i['titulo'][:70]} · {i['angulo']} · AR: {V(i).get('existe_en_argentina')}", file=sys.stderr)
