# Regla N.º 2, paso automático: para cada fila de 2026-10-14-nichos-2/*.json busca en el registro
# (registro-de-ideas.csv, SOLO las entradas anteriores a esta búsqueda) las 5 entradas con más palabras en común.
# También compara las filas nuevas entre sí (mismo problema en dos nichos).
# Es un primer filtro por palabras; la decisión final (N/P/C/R) se toma a mano y se guarda en 2026-10-14-deduplicacion-2.json.
# Uso: python research/datos/cruce_registro_nichos2.py > salida.txt
import csv
import json
import re
import unicodedata
from pathlib import Path

D = Path(__file__).resolve().parent
SRC = D / "2026-10-14-nichos-2"
STOP = set("""de la el los las un una y o a en con por para que del al se su sus sin no es lo como mas más muy hoy
cada entre sobre desde hasta cuando donde quien quién qué cual cuál le les ya pero tambien también otro otra otros
otras mano manual manuales hacen hace tienen tiene saben sabe ni nadie todo toda todos todas""".split())


def toks(s):
    s = unicodedata.normalize("NFKD", s.lower())
    s = "".join(c for c in s if not unicodedata.combining(c))
    return {w[:6] for w in re.findall(r"[a-z0-9]+", s) if len(w) > 3 and w not in STOP}


def main():
    reg = []
    with (D / "registro-de-ideas.csv").open(encoding="utf-8-sig") as fh:
        for x in csv.DictReader(fh):
            if "2026-10-14" in x["origen"] and "NICHOS-Y-PROBLEMAS-2" in x["origen"]:
                continue
            reg.append((x["id"], x["nombre_o_problema"], x["categoria_o_nicho"], x["decision_facu"][:22], toks(x["nombre_o_problema"])))
    filas = []
    for f in sorted(SRC.glob("*.json")):
        for r in json.loads(f.read_text(encoding="utf-8")):
            if str(r.get("id", "")).startswith("_"):
                continue
            filas.append(r)
    for r in filas:
        t = toks(r["problema"] + " " + r.get("especialidad", ""))
        cands = sorted(((len(t & e[4]) / (len(e[4]) ** 0.5 + 1), e) for e in reg), key=lambda z: -z[0])[:5]
        print(f"\n## {r['id']} | {r['problema']}  (dice parecido_a: {r.get('parecido_a', '')})")
        for sc, e in cands:
            if sc > 0.3:
                print(f"   {sc:.2f} {e[0]} [{e[3]}] {e[1][:90]}")
        tr = toks(r["problema"])
        for o in filas:
            if o["id"] != r["id"] and o["id"][:3] != r["id"][:3] and len(tr & toks(o["problema"])) >= 3:
                print(f"   ~ otra fila nueva: {o['id']} {o['problema'][:80]}")


if __name__ == "__main__":
    main()
