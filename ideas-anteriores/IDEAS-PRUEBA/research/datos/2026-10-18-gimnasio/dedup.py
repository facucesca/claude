# -*- coding: utf-8 -*-
"""Cruce automático de ideas nuevas contra el registro y entre sí.
Uso: python -I dedup.py <ideas_consolidadas.json> <exclusion-registro.tsv> <salida.json>
Entrada: lista de ideas (dicts con titulo, una_linea, problema, cliente_que_paga, angulo).
Salida: misma lista con campos: id_tmp, sospechas_registro [(id, nombre, decision, score)], sospechas_internas [(id_tmp, titulo, score)].
No decide: marca candidatos para que un agente juez los mire.
"""
import sys, json, re, csv, unicodedata, math
from collections import Counter

STOP = set("""de la el los las un una unos unas y o u a en para por con sin que se su sus del al lo es son como mas más pero
sobre entre hacia desde hasta donde cuando cual cuales quien quienes este esta estos estas ese esa esos esas aquel aquella
app plataforma web pagina página sistema servicio servicios ideas idea negocio negocios argentina argentino argentinos
via vía ia inteligencia artificial claude automatizacion automatización online digital nuevo nueva nuevos nuevas
marketplace mercado cliente clientes persona personas empresa empresas pyme pymes gente cosa cosas hacer tener
con sin mediante través traves usando usar uso solo sólo cada todo toda todos todas otro otra otros otras
""".split())

def norm(s):
    s = unicodedata.normalize("NFKD", s or "").encode("ascii", "ignore").decode().lower()
    toks = re.findall(r"[a-z0-9]{3,}", s)
    out = []
    for t in toks:
        if t in STOP: continue
        # stem muy básico español
        for suf in ("ciones", "cion", "mente", "idades", "idad", "ados", "adas", "ado", "ada", "ares", "eros", "eras", "ero", "era", "es", "as", "os", "s"):
            if len(t) > 5 and t.endswith(suf):
                t = t[: -len(suf)]; break
        out.append(t)
    return out

def tfidf_vecs(docs):
    df = Counter()
    toks = [set(norm(d)) for d in docs]
    for t in toks: df.update(t)
    N = len(docs)
    vecs = []
    for t in toks:
        v = {w: math.log(1 + N / df[w]) for w in t}
        n = math.sqrt(sum(x * x for x in v.values())) or 1
        vecs.append({w: x / n for w, x in v.items()})
    return vecs

def cos(a, b):
    if len(a) > len(b): a, b = b, a
    return sum(x * b.get(w, 0) for w, x in a.items())

def main():
    ideas = json.load(open(sys.argv[1], encoding="utf-8"))
    reg = list(csv.DictReader(open(sys.argv[2], encoding="utf-8"), delimiter="\t"))
    out_path = sys.argv[3]
    idea_docs = [f"{i.get('titulo','')} {i.get('una_linea','')} {i.get('problema','')} {i.get('cliente_que_paga','')}" for i in ideas]
    reg_docs = [f"{r['nombre_o_problema']} {r['categoria_o_nicho']}" for r in reg]
    vecs = tfidf_vecs(idea_docs + reg_docs)
    iv, rv = vecs[: len(ideas)], vecs[len(ideas):]
    for k, idea in enumerate(ideas):
        idea["id_tmp"] = idea.get("id_tmp") or f"N{k+1:03d}"
        sims = sorted(((cos(iv[k], rv[j]), j) for j in range(len(reg))), reverse=True)[:5]
        idea["sospechas_registro"] = [
            {"id": reg[j]["id"], "nombre": reg[j]["nombre_o_problema"][:120], "decision": reg[j]["decision_facu"], "score": round(s, 3)}
            for s, j in sims if s >= 0.22
        ]
        sims_i = sorted(((cos(iv[k], iv[m]), m) for m in range(len(ideas)) if m != k), reverse=True)[:3]
        idea["sospechas_internas"] = [
            {"id_tmp": ideas[m].get("id_tmp") or f"N{m+1:03d}", "titulo": ideas[m].get("titulo", "")[:100], "score": round(s, 3)}
            for s, m in sims_i if s >= 0.35
        ]
    json.dump(ideas, open(out_path, "w", encoding="utf-8"), ensure_ascii=False, indent=1)
    n_reg = sum(1 for i in ideas if i["sospechas_registro"])
    n_int = sum(1 for i in ideas if i["sospechas_internas"])
    print(f"{len(ideas)} ideas · {n_reg} con sospecha de registro · {n_int} con sospecha interna")

if __name__ == "__main__":
    main()
