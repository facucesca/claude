# -*- coding: utf-8 -*-
"""Lotes del contraste a re-verificar: todas las 'no verificado' + las de importabilidad >= 7.
Uso: python -I -X utf8 make_clotes.py <patrones.json> <carpeta_salidas> <por_lote>"""
import sys, json, math, pathlib
P = json.load(open(sys.argv[1], encoding="utf-8")); out = pathlib.Path(sys.argv[2]); n = int(sys.argv[3])
sel = []
for s in P["contraste"]:
    for e in s["empresas"]:
        if e.get("existe_en_argentina") == "no verificado" or float(e.get("importabilidad_1_10", 0) or 0) >= 7:
            sel.append({"clave": f"{s['sector']}||{e['empresa']}", "sector": s["sector"], "empresa": e["empresa"], "pais": e["pais"], "que_hace": e["que_hace"],
                        "existe_en_argentina": e["existe_en_argentina"], "detalle_argentina": e["detalle_argentina"], "importabilidad_1_10": e["importabilidad_1_10"],
                        "version_argentina_con_vuelta": e["version_argentina_con_vuelta"]})
names = []
for k in range(math.ceil(len(sel) / n)):
    name = f"clote-{k + 1:02d}.json"; names.append(name)
    json.dump(sel[k * n:(k + 1) * n], open(out / name, "w", encoding="utf-8"), ensure_ascii=False, indent=1)
print(json.dumps(names)); print(f"{len(sel)} empresas en {len(names)} lotes", file=sys.stderr)
