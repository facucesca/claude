# -*- coding: utf-8 -*-
"""Arma lotes temáticos de ideas con su contexto previo para que agentes las investiguen una por una.
Uso: python -I -X utf8 build_lotes.py <carpeta_salida>
Entrada: marcas-todas.json (116 filas) + Excel/JSON de origen. Salida: lote-XX.json e indice-lotes.json"""
import sys, json, re, pathlib
from openpyxl import load_workbook
R = pathlib.Path(__file__).resolve().parents[3]; OUT = pathlib.Path(sys.argv[1]); OUT.mkdir(parents=True, exist_ok=True)
marc = json.load(open(pathlib.Path(__file__).parent / "marcas-todas.json", encoding="utf-8"))
def cut(x, n=420):
    x = re.sub(r"\s+", " ", str(x or "")).strip(); return x if len(x) <= n else x[:n].rsplit(" ", 1)[0] + "…"
# Fase 2 y Orden
wb = load_workbook(R / "TODAS-LAS-IDEAS.xlsx", read_only=True)
orows = list(wb["Orden de Claude"].iter_rows(values_only=True)); oh = next(k for k, r in enumerate(orows) if r[0] == "Puesto")
OH = [str(x or "") for x in orows[oh]]; orden = {str(dict(zip(OH, r))["Código"]).strip(): dict(zip(OH, r)) for r in orows[oh + 1:] if r[0]}
blk = None; hdrs = {}; f2 = {}
for r in wb["Fase 2"].iter_rows(values_only=True):
    f = r[0]
    if isinstance(f, str) and f.startswith(("A. ", "B. ", "C. ", "D. ")): blk = f[0]; continue
    if isinstance(f, str) and f.startswith("Código"): hdrs[blk] = [str(x or "").replace("\n", " ") for x in r]; continue
    if f and blk and not (isinstance(f, str) and len(f) > 40): f2[str(f).strip()] = dict(zip(hdrs[blk], r))
def col(d, pref):
    for k, v in d.items():
        if k.startswith(pref) and v not in (None, ""): return v
    return ""
# gimnasio
gim = {i["id_tmp"]: i for i in json.load(open(R / "research/datos/2026-10-18-gimnasio/ideas_final.json", encoding="utf-8"))}
# nichos 2
wb2 = load_workbook(R / "NICHOS-Y-PROBLEMAS-2.xlsx", read_only=True); pr = list(wb2["Problemas"].iter_rows(values_only=True)); ph = [str(x or "") for x in pr[0]]
n2 = {r[0]: dict(zip(ph, r)) for r in pr[1:] if r[0]}
def contexto(d):
    cod = d["codigo"]; partes = []
    if cod.startswith("GIM-N"):
        i = gim[cod[4:]]; v = i["verificacion"]
        comp = "; ".join(f"{c['nombre']} ({c['parecido']}): {c['que_hace'][:130]}" for c in (v.get("competidores_argentina") or [])[:3])
        partes += [f"Qué es: {cut(i.get('una_linea'), 300)}", f"Vuelta de tuerca: {cut(i.get('vuelta_de_tuerca'), 300)}", f"Existe en Argentina (verificado 2026-10-19): {v.get('existe_en_argentina')}. {comp}",
                   f"Nota del verificador: {cut(v.get('nota_para_facu'), 400)}", f"Primer experimento propuesto: {cut(i.get('primer_experimento_barato'), 200)}", f"Fichas: ver research/2026-10-19-gimnasio-top-a-fondo.md si figura ahí (id {i['id_tmp']})"]
    elif cod in n2:
        x = n2[cod]
        partes += [f"Problema: {cut(x.get('Problema'), 300)}", f"Quién paga: {cut(x.get('Quién paga'), 150)}", f"Solución afuera 1: {cut(x.get('Solución 1 (afuera)'), 80)} — {cut(x.get('Qué hace 1'), 160)}",
                   f"Solución afuera 2: {cut(x.get('Solución 2 (afuera)'), 80)} — {cut(x.get('Qué hace 2'), 120)}", f"Argentina (según el Excel): {x.get('Presencia en Argentina')}. {cut(x.get('Qué hay en Argentina'), 380)}",
                   f"Regulación: {cut(x.get('Regulación (detalle)'), 200)}", f"Puntajes del Excel: total {x.get('Total /25')}/25, mercado {x.get('Mercado')}, hueco AR {x.get('Hueco en AR')}, fit Facu {x.get('Fit Facu')}"]
    else:
        fr = f2.get(cod, {}); o = orden.get(cod, {})
        for lab, pref, n in (("Qué es", "Qué es (", 380), ("Versión que tiene sentido", "Versión que tiene", 300), ("Veredicto", "Veredicto", 250), ("Argentina", "Argentina (", 300), ("Qué hay en Argentina", "Qué hay en Argentina", 300),
                             ("Qué existe", "Qué existe", 300), ("Comentario de Claude", "Comentario de Claude", 320), ("Estado en la investigación", "Estado en la investigación", 160), ("Riesgos", "Riesgos principales", 200)):
            v = col(fr, pref)
            if v: partes.append(f"{lab}: {cut(v, n)}")
        if o: partes += [f"Por qué ese puesto: {cut(o.get('Por qué este lugar (opinión)'), 300)}", f"Qué averiguar primero: {cut(o.get('Qué averiguar primero'), 200)}", f"Territorio: {o.get('Territorio')}"]
    return " | ".join(p for p in partes if p and not p.endswith(": "))
TEMAS = [("stock", r"stock|inventario|\bABC\b|pieza|bulon|FIFO|pick|calculadora|dep[oó]sito|operarios|estudio de tiempos|kaizen|vencimientos|ferreter"),
         ("logistica_accesos", r"flete|log[ií]stic|repuesto|paquete|port[oó]n|locker|transporte|volquete|env[ií]o|carga|portal(es)? de proveedores|factura|orden de compra"),
         ("camaras_sensores", r"c[aá]mara|rfid|sensor|collar|alambrado|hacienda|fruta|visi[oó]n|robos hormiga|conversi[oó]n|gente entra|cu[aá]nta gente|botón|brazalete|rastread"),
         ("educacion", r"profesor|alumno|universi|aprendizaje|equivalencia|academia|escuel|colegio|docente|capacit"),
         ("salud_comida", r"salud|enfermer|cuidador|certificado m[eé]dico|prepaga|nutricional|rotulad|higiene|bromatolog|cervecer|excedente|comida|mayores|remedio|chequeo|geri"),
         ("video_contenido", r"video|remotion|youtube|m[uú]sica|clipping|clips|render|ropa|indumentaria|papá noel|plantilla|spotify"),
         ("software_ia_pymes", r"claude|skills|mcp|apify|scraper|alertas|x402|\bapp\b.*(shopify|chatgpt)|shopify|chatgpt|bpmn|ai-ready|datos de pymes|kit ia|inmobiliaria|contable|coaching|micro-saas|constructor|apps hechas|calculadoras y mini"),
         ("marketplaces_usados", r"marketplace|usado|celular|reventa|intermediari|escrow|compradores y vendedores|garant[ií]a de|sello de confianza|trusted|cierre seguro|proveedores"),
         ("tramites_finanzas", r"jubil|seguro|siniestro|reclam|deuda|fiado|referencias|apel|factura|trámite|tramite|pasaporte|hipotec|impuesto|arba|ciudadan|perito"),
         ("hogar_obra_barrio", r"hogar|obra|barrio|edificio|limpieza|mantenimiento|solar|casa|construc|techo|pintura|empleadas|alquiler|cuadra|consorcio"),
         ("agro_industria", r"agro|campo|pastoreo|forraj|rollo|maquinaria|fas[oó]n|capacidad ociosa|export|planta|cosecha|ganader|silo|junta|pasanaku")]
def tema(d):
    t = (d["idea"] + " " + d["anot"][:200]).lower()
    for nombre, rx in TEMAS:
        if re.search(rx, t, re.I): return nombre
    return "otros"
filas = []
for k, d in enumerate(marc, 1):
    filas.append(dict(n=f"M{k:03d}", origen=d["origen"], codigo=d["codigo"], idea=d["idea"], anotaciones_de_facu=d["anot"], puntuacion_previa=d["score"], contexto_previo=contexto(d), tema_auto=tema(d)))
from collections import defaultdict
por = defaultdict(list)
for f in filas: por[f["tema_auto"]].append(f)
lotes = []
for t, lst in por.items():
    for k in range(0, len(lst), 10):
        chunk = lst[k:k + 10]
        if lotes and len(chunk) < 4 and len(lotes[-1]) + len(chunk) <= 13: lotes[-1].extend(chunk)
        else: lotes.append(chunk)
idx = []
for k, ch in enumerate(lotes, 1):
    name = f"lote-{k:02d}.json"; json.dump(ch, open(OUT / name, "w", encoding="utf-8"), ensure_ascii=False, indent=1); idx.append((name, len(ch), sorted({c['tema_auto'] for c in ch})))
json.dump(filas, open(OUT / "todas-las-filas.json", "w", encoding="utf-8"), ensure_ascii=False, indent=1)
print({t: len(v) for t, v in por.items()}); [print(i) for i in idx]; print("contexto vacío:", sum(1 for f in filas if not f["contexto_previo"]), "| largo medio:", sum(len(f["contexto_previo"]) for f in filas) // len(filas))
