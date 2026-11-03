# -*- coding: utf-8 -*-
"""Renderiza los crudos legibles de la versión 2.
Uso: python -I -X utf8 render_md2.py <carpeta_salidas> <carpeta_md>
Escribe (si hay datos): 2026-10-18-gimnasio-ideas.md, 2026-10-18-gimnasio-contraste.md (con verificación), 2026-10-19-gimnasio-top-a-fondo.md,
2026-10-19-gimnasio-programa-30-dias.md, LENTES-MAESTRAS.html"""
import sys, json, pathlib, html
D = pathlib.Path(sys.argv[1]); O = pathlib.Path(sys.argv[2]); O.mkdir(parents=True, exist_ok=True)
def load(n, d):
    p = D / n
    return json.load(open(p, encoding="utf-8")) if p.exists() else d
K = ("innovacion", "factibilidad_facu", "brecha_argentina", "por_que_ahora", "potencial")
def V(i): return i.get("verificacion") or {}
def tot(i):
    v = V(i).get("score_ajustado") or i.get("score") or {}
    return round(sum(float(v.get(k, 0) or 0) for k in K) / 5, 1)
def viva(i): return i.get("estado_registro") != "repetida" and V(i).get("veredicto") != "descartar"
HEAD = "> Crudo generado por agentes el 2026-10-18 y verificado en la web el 2026-10-19, para el pedido \"gimnasio de ideas\" (síntesis en `research/2026-10-18-gimnasio-de-ideas.md`). Regla N.º 1: lo que no tiene fuente es opinión o estimación; \"no verificado\" significa exactamente eso.\n\n"
ideas = load("ideas_final.json", []); fichas = load("fichas.json", []); prog = load("programa30.json", {}); maestras = load("lentes_maestras.json", [])
P = load("patrones.json", {}); cverif = load("contraste_verif.json", {})
orden = {}
if ideas:
    vivas = sorted([i for i in ideas if viva(i)], key=lambda i: -tot(i)); orden = {i["id_tmp"]: n for n, i in enumerate(vivas, 1)}
    out = ["# Fichas de ideas — crudo 2026-10-18, verificado 2026-10-19\n", HEAD]
    for n, i in enumerate(vivas, 1):
        v = V(i); comp = "; ".join(f"{c['nombre']} ({c['parecido']}): {c['que_hace'][:200]} — {c['url']}" for c in v.get("competidores_argentina") or [])
        out.append(f"\n## {n}. {i['titulo']} — {tot(i)}/10 · {i['angulo']}\n\n{i.get('una_linea','')}\n\n"
                   f"- **¿Existe en Argentina?** {v.get('existe_en_argentina') or i.get('existe_en_argentina')}" + (f" (verificado en la web el {v.get('fecha_verificacion')}, en {v.get('verificada_en','la verificación')})" if v.get("verificada_web") else " (sin verificar en la web)") + "\n"
                   + (f"- **Competidores en Argentina:** {comp}\n" if comp else "") + (f"- **Intentos previos:** {v.get('intentos_previos')}\n" if v.get("intentos_previos") else "")
                   + f"- **Nota del verificador:** {v.get('nota_para_facu','')}\n" + (f"- **Nota del juez (sin web):** {v.get('nota_juez')}\n" if v.get("nota_juez") and v.get("nota_juez") != v.get("nota_para_facu") else "")
                   + f"- **Problema:** {i.get('problema','')}\n- **Paga:** {i.get('cliente_que_paga','')} · **Cobro:** {i.get('modelo_de_cobro','')}\n- **Vuelta de tuerca:** {i.get('vuelta_de_tuerca','')}\n"
                   f"- **Combina:** {' + '.join(i.get('componentes_que_combina') or [])}\n- **Por qué ahora:** {i.get('por_que_ahora','')}\n- **Qué hace la IA:** {i.get('que_hace_la_ia','')}\n"
                   "- **Existe afuera:** " + "; ".join(f"{e.get('empresa')} ({e.get('pais')}): {e.get('dato')} — {e.get('fuente')}" for e in i.get("existe_afuera") or []) + "\n"
                   f"- **Huevo y gallina:** {i.get('huevo_gallina','')}\n- **Palancas:** " + " · ".join(i.get("palancas_para_retorcerla") or []) + "\n"
                   f"- **Primer experimento:** {i.get('primer_experimento_barato','')}\n- **Riesgos:** {i.get('riesgos','')}\n- **Patrón / lente:** {i.get('patron','')} / {i.get('lente','')}\n"
                   "- **Puntajes:** " + ", ".join(f"{k} {int(float(x))}" for k, x in (v.get("score_ajustado") or i.get("score") or {}).items()) + "\n"
                   + ("- **También apareció como:** " + "; ".join(f"{f['id_tmp']} [{f['angulo']}] {f['titulo']}" for f in i["fusionadas"]) + "\n" if i.get("fusionadas") else "")
                   + f"- **Registro:** {i.get('estado_registro','nueva')} " + "; ".join(f"{s.get('id')} ({s.get('decision')})" for s in i.get("parecidas_confirmadas") or []) + "\n")
    (O / "2026-10-18-gimnasio-ideas.md").write_text("".join(out), encoding="utf-8")
if P.get("contraste"):
    out = ["# Contraste EE.UU. (y otros) vs Argentina — crudo 2026-10-18, re-verificado 2026-10-19\n", HEAD]
    for s in P["contraste"]:
        out.append(f"## {s['sector']}\n\n**Lectura del sector:** {s['lectura_del_sector']}\n")
        for e in sorted(s["empresas"], key=lambda x: -float(x.get("importabilidad_1_10", 0) or 0)):
            c = cverif.get(f"{s['sector']}||{e['empresa']}")
            c = c if c and c.get('existe_en_argentina') != 'no verificado' else None
            out.append(f"\n### {e['empresa']} ({e['pais']}) — importabilidad {c['importabilidad_ajustada'] if c else e['importabilidad_1_10']}/10\n\n- **Qué hace:** {e['que_hace']}\n- **Cobro:** {e['modelo_de_cobro']}\n- **Tracción:** {e['traccion']} — {e['fuente']} (consultado {e.get('fecha_consulta','2026-10-18')})\n- **¿Existe en Argentina?** "
                       + (f"{c['existe_en_argentina']} (re-verificado 2026-10-19). {c['detalle']}\n- **Nota de verificación:** {c['nota']}\n- **Lo que se había dicho antes:** {e['existe_en_argentina']}. {e['detalle_argentina']}\n" if c else f"{e['existe_en_argentina']}. {e['detalle_argentina']}\n")
                       + f"- **Barreras:** {e['barreras_argentina']}\n- **Por qué ahora:** {e['por_que_ahora']}\n- **Versión argentina con vuelta:** {e['version_argentina_con_vuelta']}\n- **Registro:** {e['chequeo_registro']}\n")
        out.append("\n---\n")
    (O / "2026-10-18-gimnasio-contraste.md").write_text("".join(out), encoding="utf-8")
if fichas:
    out = ["# Top a fondo — las mejores ideas del gimnasio, investigadas para decidir si probarlas\n\n",
           "**Fecha:** 2026-10-19. Cada ficha la armó un agente investigador con búsquedas reales (hasta 8 búsquedas y 5 lecturas por idea). Lo que es estimación propia está marcado como tal. El experimento de cada ficha cuesta menos de USD 200 y dura unas dos semanas. Índice general en `research/2026-10-18-gimnasio-de-ideas.md`; la hoja `TOP A FONDO` de `GIMNASIO-DE-IDEAS.xlsx` tiene lo mismo para marcar.\n\n"]
    fs = sorted(fichas, key=lambda f: orden.get(f.get("id_tmp"), 999))
    out.append("| Puesto | Idea | Veredicto del investigador |\n|---|---|---|\n" + "".join(f"| {orden.get(f['id_tmp'],'')} | {f['titulo']} | {f['veredicto'][:160].replace('|','/')} |\n" for f in fs) + "\n")
    for f in fs:
        e = f.get("experimento") or {}
        out.append(f"\n## {orden.get(f['id_tmp'],'')}. {f['titulo']}\n\n{f['resumen']}\n\n**Veredicto:** {f['veredicto']}\n\n### Quién lo intentó y qué le pasó\n\n{f['quien_lo_intento']}\n\n### Competencia en Argentina\n\n{f['competencia_argentina']}\n\n"
                   f"### Regulación\n\n{f['regulacion']}\n\n### Números de unidad\n\n{f['numeros_unidad']}\n\n### Tamaño del mercado\n\n{f['tamano_mercado']}\n\n### A quién entrevistar\n\n{f['a_quien_entrevistar']}\n\n"
                   "### Guion de entrevista (estilo Mom Test)\n\n" + "".join(f"{k}. {q}\n" for k, q in enumerate(f.get("guion_entrevista") or [], 1))
                   + f"\n### Experimento de dos semanas\n\n- **Hipótesis:** {e.get('hipotesis','')}\n- **Predicción (antes de empezar):** {e.get('prediccion','')}\n- **Pérdida máxima:** {e.get('perdida_maxima','')}\n- **Duración:** {e.get('duracion','')}\n- **Pasos:**\n" + "".join(f"  {k}. {p}\n" for k, p in enumerate(e.get("pasos") or [], 1))
                   + f"- **Sigue si:** {e.get('criterio_sigue','')}\n- **Se corta si:** {e.get('criterio_corta','')}\n\n### Cinco formas de retorcerla\n\n" + "".join(f"- {v}\n" for v in f.get("variantes") or [])
                   + "\n### Riesgos\n\n" + "".join(f"- {r}\n" for r in f.get("riesgos") or []) + "\n### Fuentes\n\n" + "".join(f"- {u}\n" for u in f.get("fuentes") or []) + "\n---\n")
    (O / "2026-10-19-gimnasio-top-a-fondo.md").write_text("".join(out), encoding="utf-8")
if prog.get("dias"):
    out = ["# Programa de 30 días para entrenar el ojo de negocios\n\n", f"**Fecha:** 2026-10-19. {prog.get('introduccion','')}\n\n",
           "Se usa junto con `ideas/BITACORA-DE-PROBLEMAS.md` (formato de 5 líneas) y la hoja `PROGRAMA 30 DÍAS` del Excel, que tiene una columna para tildar cada día.\n\n",
           "| Día | Lente | Dónde mirarla | Ejercicio | Qué anotar |\n|---|---|---|---|---|\n"]
    out += [f"| {d['dia']} | **{d['lente']}** ({d['libro']}) | {d['donde_mirar']} | {d['ejercicio']} | {d['que_anotar']} |\n".replace("\n", " ").rstrip() + "\n" for d in prog["dias"]]
    out.append("\n## Pregunta de cada día\n\n" + "".join(f"{d['dia']}. {d['pregunta']}\n" for d in prog["dias"]))
    (O / "2026-10-19-gimnasio-programa-30-dias.md").write_text("".join(out), encoding="utf-8")
if maestras:
    rows = "".join(f"<tr><td class=n>{k}</td><td><b>{html.escape(m['lente'])}</b><br><span>{html.escape(m['que_mirar'])}</span></td><td>{html.escape(m['pregunta'])}</td></tr>" for k, m in enumerate(maestras, 1))
    doc = f"""<!doctype html><html lang="es"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>Lentes maestras</title>
<style>@page{{size:A4 landscape;margin:10mm}}body{{font-family:Georgia,serif;color:#1b1b1b;background:#fff;margin:0;padding:16px}}h1{{font-size:20px;margin:0 0 4px}}p.sub{{margin:0 0 10px;color:#555;font-size:12px}}
table{{border-collapse:collapse;width:100%;font-size:12px}}td{{border-top:1px solid #ccc;padding:6px 8px;vertical-align:top}}td.n{{font-size:18px;color:#1f3a5f;width:24px}}td span{{color:#444}}td:last-child{{width:38%;font-style:italic}}
@media print{{body{{padding:0}}}}</style></head><body><h1>Las 12 lentes maestras</h1><p class=sub>Formas de mirar que aparecen en 3 o más de tus libros de startup. Para llevar en el bolsillo o pegar al lado de la compu. Gimnasio de ideas, 2026-10-19.</p>
<table>{rows}</table></body></html>"""
    (O / "LENTES-MAESTRAS.html").write_text(doc, encoding="utf-8")
print("render2 ok:", sorted(p.name for p in O.iterdir() if p.suffix in (".md", ".html")))
