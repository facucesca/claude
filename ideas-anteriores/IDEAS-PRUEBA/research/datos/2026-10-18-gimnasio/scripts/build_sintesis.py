# -*- coding: utf-8 -*-
"""Completa la síntesis v2 con los datos finales.
Uso: python -I -X utf8 build_sintesis.py <salidas> <plantilla.md> <salida.md> <uso_final> <n_registro> <n_agentes_v2>"""
import sys, json, re, pathlib, collections
D = pathlib.Path(sys.argv[1]); T = pathlib.Path(sys.argv[2]).read_text(encoding="utf-8"); OUT = pathlib.Path(sys.argv[3])
USO_FINAL, N_REG, N_AG = int(sys.argv[4]), sys.argv[5], sys.argv[6]
N_DESC_GEN = sys.argv[7] if len(sys.argv) > 7 else "más de 250"
K = ("innovacion", "factibilidad_facu", "brecha_argentina", "por_que_ahora", "potencial")
I = json.load(open(D / "ideas_final.json", encoding="utf-8")); F = json.load(open(D / "fichas.json", encoding="utf-8")); Fby = {f["id_tmp"]: f for f in F}
M = json.load(open(D / "matriz.json", encoding="utf-8")); PR = json.load(open(D / "programa30.json", encoding="utf-8"))
CV = json.load(open(D / "contraste_verif.json", encoding="utf-8")); P = json.load(open(D / "patrones.json", encoding="utf-8"))
TAGS = json.load(open(D / "tags.json", encoding="utf-8"))["etiquetas"]
def V(i): return i.get("verificacion") or {}
def tot(i): v = V(i).get("score_ajustado") or i.get("score") or {}; return round(sum(float(v.get(k, 0) or 0) for k in K) / 5, 1)
def viva(i): return i.get("estado_registro") != "repetida" and V(i).get("veredicto") != "descartar"
def corto(t, n=230):
    t = re.sub(r"\s+", " ", t or "").strip(); s = re.split(r"(?<=[.!?])\s", t)[0]
    if len(s) > n: s = s[:n].rsplit(" ", 1)[0] + "…"
    return s.replace("|", "/")
def tit(i): return i["titulo"].split(":")[0].strip()
def largo(t, n=300):
    t = re.sub(r"\s+", " ", t or "").strip(); out = ""
    for x in re.split(r"(?<=[.!?])\s", t):
        if len(out) >= 170 or len(out) + len(x) > n: break
        out = (out + " " + x).strip()
    if not out: out = t[:n].rsplit(" ", 1)[0] + "…"
    return out.replace("|", "/")
def c1(x): return f"{x:.1f}".replace(".", ",")
viv = sorted([i for i in I if viva(i)], key=lambda i: (-tot(i), i["id_tmp"])); pos = {i["id_tmp"]: n for n, i in enumerate(viv, 1)}
ex = collections.Counter(V(i).get("existe_en_argentina") or i.get("existe_en_argentina") for i in viv)
ver = [i for i in viv if V(i).get("verificada_web")]
muertas = [i for i in I if not viva(i)]
rep = sum(1 for i in muertas if i.get("estado_registro") == "repetida")
dup = sum(1 for i in muertas if i.get("estado_registro") != "repetida" and (i.get("fusionada_en") or i.get("duplicada_de")))
dweb = [i for i in muertas if i.get("estado_registro") != "repetida" and not (i.get("fusionada_en") or i.get("duplicada_de")) and V(i).get("verificada_web")]
djuez = len(muertas) - rep - dup - len(dweb)
deltas = [tot(i) - round(sum(float((V(i).get("score_juez") or {}).get(k, 0) or 0) for k in K) / 5, 1) for i in ver if V(i).get("score_juez")]
agro = sum(1 for t in TAGS if not t["id"].startswith("E:") and t["sector"] == "Agro y alimentos" and t["id"] in pos)
# parte 1 (lentes, patrones, contraste) con inserciones
p1 = (D / "sintesis-parte1.md").read_text(encoding="utf-8"); p1 = p1[p1.index("## 2. Las lentes"):]
s3, s4 = p1.index("## 3. Los patrones"), p1.index("## 4. El contraste")
mat = "\n### La matriz patrón por sector (2026-10-19)\n\nCada idea viva y cada empresa del contraste se etiquetó con su patrón de negocio y su sector. La hoja `MATRIZ PATRÓN×SECTOR` cruza los 30 patrones con 12 sectores. Las celdas naranjas son huecos: el patrón funciona afuera en ese sector y no generamos ninguna idea acá. Las azules tienen ideas, con las dos mejores y su puntaje. Lo que se lee:\n\n" + "".join(f"- {x}\n" for x in M.get("lectura", [])[:4]) + "\n"
orig = {f"{s['sector']}||{e['empresa']}": e for s in P["contraste"] for e in s["empresas"]}
camb = []
for k, c in CV.items():
    if c["existe_en_argentina"] == "no verificado": continue
    o = orig.get(k);
    if not o: continue
    if o["existe_en_argentina"] != c["existe_en_argentina"] or abs(float(o["importabilidad_1_10"]) - float(c["importabilidad_ajustada"])) >= 1:
        camb.append((float(o["importabilidad_1_10"]), f"- **{o['empresa'].split(' (')[0]}** ({o['existe_en_argentina']} → {c['existe_en_argentina']}; importabilidad {o['importabilidad_1_10']} → {c['importabilidad_ajustada']}): {corto(c['nota'], 260)}\n"))
nver_c = sum(1 for c in CV.values() if c["existe_en_argentina"] != "no verificado")
cont = f"\n### Qué cambió al re-verificar el contraste (2026-10-19)\n\nSe re-verificaron con búsquedas reales {nver_c} empresas (todas las que decían \"no verificado\" y las de importabilidad alta); {len(CV) - nver_c} quedaron pendientes por el cupo de búsqueda. Los cambios más importantes, ordenados por la importabilidad que tenían:\n\n" + "".join(x for _, x in sorted(camb, key=lambda t: -t[0])[:14]) + "\n"
p1 = p1[:s4].rstrip() + chr(10) + mat + p1[s4:].rstrip() + chr(10) + cont
# tablas
filas = ["| # | Idea | /10 | ¿Existe en Argentina? | Lo que encontró la verificación | Ficha a fondo |", "|---|---|---|---|---|---|"]
for i in viv[:25]:
    v = V(i); comp = ", ".join(c["nombre"].split(" (")[0] for c in (v.get("competidores_argentina") or [])[:2])
    filas.append(f"| {pos[i['id_tmp']]} | {tit(i)} | {c1(tot(i))} | {v.get('existe_en_argentina')}" + (f" ({comp})" if comp else "") + f" | {corto(v.get('nota_para_facu',''))} | {'sí' if i['id_tmp'] in Fby else ''} |")
ft = ["| Puesto | Idea | Condición para probarla | Pérdida máxima |", "|---|---|---|---|"]
for f in sorted(F, key=lambda f: pos.get(f["id_tmp"], 999)):
    ft.append(f"| {pos.get(f['id_tmp'], '')} | {f['titulo'].split(':')[0].replace('|','/')} | {largo(f['veredicto'], 320)} | {corto((f.get('experimento') or {}).get('perdida_maxima', ''), 80)} |")
nada = [i for i in viv if V(i).get("existe_en_argentina") == "no encontré nada"]
comp = [i for i in viv if V(i).get("existe_en_argentina") == "existe y compite"]
fichas_nada = [tit(i) for i in nada if i["id_tmp"] in Fby]
res = [tit(i) for i in viv if V(i).get("existe_en_argentina") in ("no encontré nada", "existe parcial") and V(i).get("verificada_web")][:6]
conteos = f"""| Qué | Cuántas |
|---|---|
| Ideas generadas (191 el 2026-10-18 + {sum(1 for i in I if i.get('segunda_pasada'))} en la segunda pasada del 2026-10-19) | {len(I)} |
| Descartadas por los propios generadores antes de proponerlas (ya estaban en el registro) | {N_DESC_GEN} |
| **Vivas** | **{len(viv)}** |
| · nuevas (nada igual en el registro) | {sum(1 for i in viv if i.get('estado_registro') == 'nueva')} |
| · parecidas a una idea que ya elegiste (marcadas con el id) | {sum(1 for i in viv if i.get('estado_registro') == 'parecida')} |
| **Salieron** (hoja `SALIERON`) | **{len(muertas)}** |
| · repetidas: mismo problema y cliente que algo del registro, o parecidas a algo que rechazaste | {rep} |
| · duplicadas: la misma idea desde dos ángulos (fusionada en su mejor versión, con sus palancas y fuentes) | {dup} |
| · descartadas por la verificación web (ya existen casi igual en Argentina) | {len(dweb)} |
| · descartadas por el juez (inviables) | {djuez} |
| Registro de ideas antes → después | 1.402 → {N_REG} filas |
"""
tabla_ex = "| ¿Existe en Argentina? | Ideas vivas |\n|---|---|\n" + "".join(f"| {k} | {v} |\n" for k, v in ex.most_common())
rep_ = {"{{N_VIVAS}}": len(viv), "{{N_GEN}}": len(I), "{{N_SALIERON}}": len(muertas), "{{N_VERIF}}": len(ver), "{{N_SINVERIF}}": len(viv) - len(ver),
        "{{N_NADA}}": ex.get("no encontré nada", 0), "{{N_PARCIAL}}": ex.get("existe parcial", 0), "{{N_COMPITE}}": ex.get("existe y compite", 0), "{{N_DESC_WEB}}": len(dweb),
        "{{N_AGRO}}": agro, "{{N_HOJAS}}": "16", "{{N_AGENTES_V2}}": N_AG, "{{USO_V2}}": USO_FINAL - 3, "{{USO_FINAL}}": USO_FINAL, "{{N_REGISTRO}}": N_REG,
        "{{RESISTIERON}}": "; ".join(res[:-1]) + " y " + res[-1] if len(res) > 1 else (res[0] if res else ""),
        "{{PARTE1}}": p1, "{{EXISTE_TABLA}}": tabla_ex, "{{PROM}}": c1(sum(tot(i) for i in viv) / len(viv)), "{{TOPE}}": c1(tot(viv[0])),
        "{{DELTA}}": f"{sum(deltas) / len(deltas):+.1f}".replace(".", ",") if deltas else "0", "{{TOP25}}": "\n".join(filas),
        "{{NADA_LISTA}}": "".join(f"- **{tit(i)}** ({c1(tot(i))}/10){' — tiene ficha a fondo' if i['id_tmp'] in Fby else ''}: {corto(V(i).get('nota_para_facu',''), 220)}\n" for i in nada),
        "{{COMPITE_LISTA}}": "".join(f"- **{tit(i)}**: compite con " + ", ".join(c["nombre"].split(" (")[0] for c in (V(i).get("competidores_argentina") or [])[:3]) + ".\n" for i in comp),
        "{{FICHAS_TABLA}}": "\n".join(ft), "{{PROGRAMA_INTRO}}": PR.get("introduccion", ""), "{{CONTEOS}}": conteos}
for k, v in rep_.items(): T = T.replace(k, str(v))
assert "{{" not in T, re.findall(r"\{\{[A-Z_0-9]+\}\}", T)
OUT.write_text(T, encoding="utf-8")
print(f"síntesis v2: {len(T):,} caracteres · vivas {len(viv)} · verificadas {len(ver)} · nada {ex.get('no encontré nada',0)} · compite {ex.get('existe y compite',0)} · salieron {len(muertas)} (rep {rep}, dup {dup}, web {len(dweb)}, juez {djuez}) · agro {agro}")
