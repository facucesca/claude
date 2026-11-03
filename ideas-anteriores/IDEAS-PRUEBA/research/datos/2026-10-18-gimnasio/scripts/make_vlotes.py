# -*- coding: utf-8 -*-
"""Arma lotes livianos para verificación web a partir de ideas_final.json.
Uso: python -I -X utf8 make_vlotes.py <ideas_final.json> <carpeta_salidas> <desde> <hasta> <ideas_por_lote> <prefijo>
Toma las ideas vivas ordenadas por puntaje (juez), posiciones [desde, hasta) (base 0), y escribe <prefijo>-NN.json.
Imprime la lista de nombres de lote en JSON (para pasar como args.lotes)."""
import sys, json, math, pathlib
ideas = json.load(open(sys.argv[1], encoding="utf-8")); out = pathlib.Path(sys.argv[2])
a, b, n, pref = int(sys.argv[3]), int(sys.argv[4]), int(sys.argv[5]), sys.argv[6]
K = ("innovacion", "factibilidad_facu", "brecha_argentina", "por_que_ahora", "potencial")
def tot(i):
    v = (i.get("verificacion") or {}).get("score_ajustado") or i.get("score") or {}
    return round(sum(float(v.get(x, 0) or 0) for x in K) / 5, 2)
vivas = [i for i in ideas if i.get("estado_registro") != "repetida" and (i.get("verificacion") or {}).get("veredicto") != "descartar"]
vivas.sort(key=lambda i: (-tot(i), i["id_tmp"]))
sel = [i for i in vivas[a:b] if not (i.get("verificacion") or {}).get("verificada_web")]
CAMPOS = ("id_tmp", "titulo", "una_linea", "problema", "cliente_que_paga", "modelo_de_cobro", "vuelta_de_tuerca",
          "por_que_ahora", "existe_afuera", "existe_en_argentina", "detalle_argentina", "angulo", "parecidas_confirmadas")
names = []
for k in range(math.ceil(len(sel) / n)):
    chunk = []
    for i in sel[k * n:(k + 1) * n]:
        d = {c: i.get(c) for c in CAMPOS}
        v = i.get("verificacion") or {}
        d["juez"] = {"score_ajustado": v.get("score_ajustado"), "nota": v.get("nota_para_facu"), "puntaje_total": tot(i)}
        chunk.append(d)
    name = f"{pref}-{k + 1:02d}.json"; names.append(name)
    json.dump(chunk, open(out / name, "w", encoding="utf-8"), ensure_ascii=False, indent=1)
print(json.dumps(names))
print(f"{len(sel)} ideas (posiciones {a}-{b - 1}) en {len(names)} lotes", file=sys.stderr)
