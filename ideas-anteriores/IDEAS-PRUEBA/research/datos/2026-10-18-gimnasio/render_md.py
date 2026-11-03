# -*- coding: utf-8 -*-
"""Convierte los JSON de los agentes a markdown legible (crudos para research/fuentes/).
Uso: python -I -X utf8 render_md.py <carpeta_salidas> <carpeta_destino>"""
import sys, json, pathlib
D = pathlib.Path(sys.argv[1]); O = pathlib.Path(sys.argv[2]); O.mkdir(parents=True, exist_ok=True)
def load(n):
    p = D / n
    return json.load(open(p, encoding="utf-8")) if p.exists() else None
HEAD = "> Crudo generado por agentes el 2026-10-18 para el pedido \"gimnasio de ideas\" (síntesis en `research/2026-10-18-gimnasio-de-ideas.md`). Regla N.º 1: lo que no tiene fuente es opinión o estimación de los agentes; \"no verificado\" significa exactamente eso.\n\n"

L = load("lentes.json")
if L:
    out = ["# Lentes de los libros de startup — crudo 2026-10-18\n", HEAD]
    for b in L["libros"]:
        out.append(f"## {b['libro']}\n\n**Tesis en una línea:** {b['tesis_en_una_linea']}\n")
        if b.get("cita_corta"): out.append(f"\n*Cita corta:* {b['cita_corta']}\n")
        out.append("\n### Lentes\n")
        for k, l in enumerate(b["lentes"], 1):
            out.append(f"\n**{k}. {l['nombre']}** · produce: {l['tipo_de_idea_que_produce']} · ref.: {l['referencia']}\n\n- Qué mirar: {l['que_mirar']}\n- Pregunta: {l['pregunta_generadora']}\n- Argentina 2026: {l['ejemplo_argentina_2026']}\n")
        out.append("\n### Ideas semilla\n")
        for s in b["ideas_semilla"]:
            out.append(f"\n- **{s['titulo']}** — {s['problema']} · Paga: {s['cliente_que_paga']} · Vuelta: {s['vuelta_de_tuerca']} · Lente: {s['lente_usada']} · Web/IA: {s['lanzable_como_web']} · Registro: {s['chequeo_registro']}\n")
        out.append("\n### Advertencias para Facu\n")
        out += [f"\n- {a}\n" for a in b["advertencias_para_facu"]]
        out.append("\n---\n")
    (O / "2026-10-18-gimnasio-lentes-libros.md").write_text("".join(out), encoding="utf-8")

P = load("patrones.json")
if P:
    out = ["# Patrones de intermediación y de paquete — crudo 2026-10-18\n", HEAD]
    for k, p in enumerate(P["patrones"]):
        out.append(f"## {'A. Patrones de intermediación' if k == 0 else 'B. Patrones de paquete y servicio integrado'}\n")
        for x in p["patrones"]:
            out.append(f"\n### {x['nombre']}\n\n- **Cómo funciona:** {x['como_funciona']}\n- **Cuándo funciona:** {x['cuando_funciona']}\n- **Casos reales:**\n")
            out += [f"  - {c['empresa']} ({c['pais']}): {c['dato_de_traccion']} — {c['fuente']} (consultado {c.get('fecha_consulta','2026-10-18')})\n" for c in x["casos_reales"]]
            out.append(f"- **Cómo muere:** {x['como_muere']}\n- **Huevo y gallina / arrancar sin plata:** {x['truco_huevo_gallina']}\n- **Ejemplo argentino:** {x['ejemplo_argentino']}\n- **Preguntas generadoras:**\n")
            out += [f"  - {q}\n" for q in x["preguntas_generadoras"]]
            out.append(f"- **¿Encaja con Facu?** {x['encaja_con_facu']}\n")
        out.append("\n**Combinaciones que generan modelos nuevos:**\n")
        out += [f"\n- {c}\n" for c in p["como_combinar_patrones"]]
        out.append("\n---\n")
    (O / "2026-10-18-gimnasio-patrones.md").write_text("".join(out), encoding="utf-8")
    out = ["# Contraste EE.UU. (y otros) vs Argentina — crudo 2026-10-18\n", HEAD]
    for s in P["contraste"]:
        out.append(f"## {s['sector']}\n\n**Lectura del sector:** {s['lectura_del_sector']}\n")
        for e in sorted(s["empresas"], key=lambda x: -float(x.get("importabilidad_1_10", 0) or 0)):
            out.append(f"\n### {e['empresa']} ({e['pais']}) — importabilidad {e['importabilidad_1_10']}/10\n\n- **Qué hace:** {e['que_hace']}\n- **Cobro:** {e['modelo_de_cobro']}\n- **Tracción:** {e['traccion']} — {e['fuente']} (consultado {e.get('fecha_consulta','2026-10-18')})\n- **¿Existe en Argentina?** {e['existe_en_argentina']}. {e['detalle_argentina']}\n- **Barreras:** {e['barreras_argentina']}\n- **Por qué ahora:** {e['por_que_ahora']}\n- **Versión argentina con vuelta:** {e['version_argentina_con_vuelta']}\n- **Registro:** {e['chequeo_registro']}\n")
        out.append("\n---\n")
    (O / "2026-10-18-gimnasio-contraste.md").write_text("".join(out), encoding="utf-8")

I = load("ideas_final.json")
if I:
    out = ["# Fichas de ideas — crudo 2026-10-18\n", HEAD]
    vivas = [i for i in I if i.get("estado_registro") != "repetida" and (i.get("verificacion") or {}).get("veredicto") != "descartar"]
    def tot(i):
        v = (i.get("verificacion") or {}).get("score_ajustado") or i.get("score") or {}
        return round(sum(float(v.get(x, 0) or 0) for x in ("innovacion","factibilidad_facu","brecha_argentina","por_que_ahora","potencial")) / 5, 1)
    vivas.sort(key=tot, reverse=True)
    for n, i in enumerate(vivas, 1):
        v = i.get("verificacion") or {}
        out.append(f"\n## {n}. {i['titulo']} — {tot(i)}/10 · {i['angulo']}\n\n{i['una_linea']}\n\n- **Problema:** {i['problema']}\n- **Paga:** {i['cliente_que_paga']} · **Cobro:** {i['modelo_de_cobro']}\n- **Vuelta de tuerca:** {i['vuelta_de_tuerca']}\n- **Combina:** {' + '.join(i.get('componentes_que_combina') or [])}\n- **Por qué ahora:** {i['por_que_ahora']}\n- **Qué hace la IA:** {i['que_hace_la_ia']}\n- **Existe afuera:** " + "; ".join(f"{e['empresa']} ({e['pais']}): {e['dato']} — {e['fuente']}" for e in i.get("existe_afuera") or []) + f"\n- **Argentina:** {v.get('existe_en_argentina') or i['existe_en_argentina']}. {i['detalle_argentina']}\n- **Huevo y gallina:** {i['huevo_gallina']}\n- **Palancas:** " + " · ".join(i.get("palancas_para_retorcerla") or []) + f"\n- **Primer experimento:** {i['primer_experimento_barato']}\n- **Riesgos:** {i['riesgos']}\n- **Patrón / lente:** {i['patron']} / {i['lente']}\n- **Puntajes:** " + ", ".join(f"{k} {int(sc)}" for k, sc in ((v.get('score_ajustado') or i['score']).items())) + f"\n- **Juez:** {v.get('veredicto','sin juzgar')}. {v.get('nota_para_facu','')}\n- **Registro:** {i.get('estado_registro','nueva')} {i.get('referencia_registro','')}\n")
    (O / "2026-10-18-gimnasio-ideas.md").write_text("".join(out), encoding="utf-8")
print("render ok:", [p.name for p in O.glob('2026-10-18-gimnasio-*.md')])
