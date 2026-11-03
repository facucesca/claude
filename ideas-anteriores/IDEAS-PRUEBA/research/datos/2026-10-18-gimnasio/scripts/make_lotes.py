# -*- coding: utf-8 -*-
"""Parte ideas_dedup.json en N lotes (lote-01.json ...) y escribe indice-titulos.txt con todas las ideas.
Uso: python -I -X utf8 make_lotes.py <ideas_dedup.json> <carpeta_salidas> <n_lotes>
Si se pasa un 4.º argumento 'top:K', arma lotes solo con las K mejores por puntaje (para verificación web)."""
import sys, json, math, pathlib
ideas = json.load(open(sys.argv[1], encoding="utf-8")); out = pathlib.Path(sys.argv[2]); n = int(sys.argv[3])
pref = "lote"
if len(sys.argv) > 4 and sys.argv[4].startswith("top:"):
    k = int(sys.argv[4][4:]); pref = "vlote"
    def tot(i):
        v = (i.get("verificacion") or {}).get("score_ajustado") or i.get("score") or {}
        return sum(float(v.get(x, 0) or 0) for x in ("innovacion","factibilidad_facu","brecha_argentina","por_que_ahora","potencial"))
    ideas = sorted([i for i in ideas if i.get("estado_registro") != "repetida" and (i.get("verificacion") or {}).get("veredicto") != "descartar"], key=tot, reverse=True)[:k]
with open(out / "indice-titulos.txt", "w", encoding="utf-8") as f:
    for i in ideas: f.write(f"{i['id_tmp']} [{i.get('angulo','')}] {i['titulo']} — {i.get('una_linea','')[:160]}\n")
size = math.ceil(len(ideas) / n); names = []
for k in range(n):
    chunk = ideas[k*size:(k+1)*size]
    if not chunk: continue
    name = f"{pref}-{k+1:02d}.json"; names.append(name)
    json.dump(chunk, open(out / name, "w", encoding="utf-8"), ensure_ascii=False, indent=1)
print(json.dumps(names)); print(f"{len(ideas)} ideas en {len(names)} lotes de ~{size}", file=sys.stderr)
