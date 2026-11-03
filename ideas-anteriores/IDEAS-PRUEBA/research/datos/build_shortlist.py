# Genera SHORTLIST-ETAPA-1.xlsx: 39 ideas elegidas del Excel general para la etapa 1
# (negocios intermedios). Datos de cada idea: 2026-10-02-todas-las-ideas.json.
# "Familia", "por qué" y "qué enseña" son OPINIÓN de Claude (2026-10-06), no datos.
import json, math, os
from openpyxl import Workbook
from openpyxl.styles import Font, Alignment, PatternFill, Border, Side
from openpyxl.worksheet.datavalidation import DataValidation
from openpyxl.utils import get_column_letter

SCR = os.path.dirname(os.path.abspath(__file__))
OUT = r"C:\FACU\IDEAS-PRUEBA\SHORTLIST-ETAPA-1.xlsx"
src = {d["id"]: d for d in json.load(open(os.path.join(SCR, "2026-10-02-todas-las-ideas.json"), encoding="utf-8"))}

F1 = "1. Orden operativo (tu especialidad)"
F2 = "2. IA para PyMEs y profesionales"
F3 = "3. Capacitación"
F4 = "4. Contenido y catálogos con IA (sin cara)"
F5 = "5. Herramientas para comercios y distribuidoras"
F6 = "6. Comercio y producto físico"

# (id, familia, por qué está en la lista, qué te enseña para la etapa 2)  -> opinión de Claude
PICKS = [
    ("X1", F1, "Es donde más pesa tu diferencial (método de ingeniería industrial + experiencia en Sporting). Capital casi cero.", "Ver por dentro muchas empresas y sus problemas: la mejor fuente de ideas de startup que tenés a mano."),
    ("C2", F1, "Versión remota y de precio fijo de la consultora: alcanza con que el cliente te mande un export.", "Vender un entregable estandarizado (productizar) y ver patrones de stock en muchos rubros."),
    ("K8", F1, "Primer cobro en días, capital cero; cada planilla rota muestra un proceso roto.", "Vender rápido a desconocidos y detectar qué problema se repite."),
    ("K9", F1, "Entregable chico, remoto, que abre la puerta a la auditoría de stock (C2).", "Qué datos tienen (y cuáles no) las PyMEs."),
    ("H18", F1, "Vende plata recuperada, no imagen; buen momento antes de fin de año.", "Diagnosticar en el lugar y hablar con dueños cara a cara."),
    ("H17", F1, "Demanda con fecha (inventario de cierre al 31/12) y cobro con seña.", "Coordinar una cuadrilla: tu primera experiencia manejando gente y una operación."),
    ("C10", F1, "Dolor fuerte y documentado en gastronomía (ver fuente en el estudio).", "Un rubro entero por dentro y vender abonos mensuales."),
    ("C7", F1, "Es lo que Claude en Excel hace bien sin programar; mantenimiento mensual.", "Compras y demanda: el corazón de una distribuidora."),
    ("D4", F1, "La parte más recurrente de la línea de servicios (según el estudio, ~1 h por cliente por mes).", "Ingresos recurrentes y retención: por qué un cliente se queda o se va."),
    ("D1", F1, "Tu método + una herramienta no-code que queda instalada: paso de servicio a producto.", "Productizar: el puente natural hacia un software propio (posible startup)."),
    ("F30", F1, "Logística/transporte, sector que te interesa y donde tenés experiencia (Sporting).", "Problemas de reparto y última milla de primera mano. Ojo: el estudio dice que es Orden Operativo con otro nombre."),
    ("C21", F1, "Ahorro medible en plata, se puede cobrar por éxito; contexto de aumentos de tarifas en 2026.", "La energía como costo de las PyMEs, un territorio grande. Ojo: las mediciones reales pueden requerir matrícula."),
    ("F4", F2, "Ola nueva (Claude for Small Business, 2026-05-13, según el estudio) y no programar no es desventaja.", "Vender IA a empresas y ver qué tareas se repiten: materia prima de startup."),
    ("F17", F2, "Mercado grande y cercano; los contadores se recomiendan entre colegas.", "Un rubro regulado (impuestos) por dentro, donde hay lugar para startups."),
    ("B17", F2, "Capital cero; además de la implementación, comisión recurrente del programa de partners (35-50% según el estudio).", "Ventas consultivas y CRM: cómo venden las PyMEs. Riesgo: dependés de Kommo."),
    ("B12", F2, "El resultado se mide en pesos recuperados: fácil de explicar y de vender.", "Cobranzas y flujo de caja, un dolor enorme de las PyMEs argentinas."),
    ("B28", F2, "Productiza la consultora; según el estudio, tu mejor diferencial en ese frente.", "Documentos y datos caóticos de distribuidoras: terreno típico de startups de IA."),
    ("F26", F2, "Importadores chicos y reglas nuevas (RG 5857/2026, según el estudio; volumen de importadores no verificado).", "Comercio exterior, un sector entero. Ojo: requiere despachante aliado y un error trae multas."),
    ("B10", F2, "Salud, sector que te interesa, con un dolor universal (pacientes que faltan).", "Cómo funciona un consultorio por dentro. Ojo: datos de salud (Ley 25.326)."),
    ("F22", F2, "Salud otra vez: según el estudio, afuera hay startups financiadas haciendo esto.", "Es casi una startup en miniatura. Ojo: la demanda local no está relevada."),
    ("A1", F3, "Cobro relativamente rápido con ticket decente, y es embudo hacia la consultora.", "Hablar en público y vender a equipos. Ojo: se vuelve commodity rápido."),
    ("A10", F3, "Producto digital que se vende muchas veces; foco en operaciones para diferenciarse.", "Crear y vender algo escalable. Ojo: el caso de éxito citado en el estudio es survivorship."),
    ("K24", F3, "Cobro en días, capital cero, y es tu diferencial real.", "Descubrir qué hacen las PyMEs con sus planillas y qué les duele."),
    ("R26", F4, "Según el estudio, ~90% automatizable; el cliente (vendedor de Mercado Libre) tiene plata.", "Operar un servicio automatizado en volumen. Ojo: ML podría hacerlo gratis."),
    ("R20", F4, "Une video + ingeniería + seguridad; baja saturación en español según el estudio.", "Plantas industriales por dentro. Ojo: industria en baja."),
    ("T5", F4, "Margen muy alto según el estudio y la muestra es fácil de hacer.", "Vender contenido B2B. Ojo: apps de clips saturadas."),
    ("R31", F4, "Recurrente mientras dura la obra (12-30 meses según el estudio); es planificación y control puro.", "Construcción e inversores, un sector grande. Ojo: pocas obras nuevas."),
    ("R1", F4, "Según el estudio, las distribuidoras argentinas no tercerizan esto hoy; abre la puerta a R8.", "Procesar en volumen con IA. Ojo: el precio por foto tiende a cero."),
    ("R8", F5, "La inflación convierte un entregable de una vez en abono mensual.", "Software liviano para un dolor argentino: candidato a producto propio."),
    ("H22", F5, "Cobro en días y abono natural.", "Precios y márgenes de comercios. Ojo: un error de precio le cuesta plata al cliente."),
    ("D37", F5, "Riesgo técnico bajo; resuelve el caos de pedidos por chat.", "Tu primer producto web propio. Ojo: hay competencia gratuita."),
    ("F19", F5, "El Estado compra siempre y la IA hace lo pesado (leer pliegos).", "Un negocio de datos con potencial de producto. Ojo: competidores establecidos."),
    ("E6", F5, "Mismo cliente que la consultora (vendedores de ML); arranque en semanas.", "Cómo vende un vendedor de ML por dentro. Ojo: precio bajo."),
    ("H1", F5, "El cobro más rápido y simple de la lista.", "Vender cara a cara a comercios: entrenamiento de ventas."),
    ("J23", F6, "Producto físico con seña (capital casi cero) y temporada justa (diciembre).", "Comprar, armar y entregar en fecha: logística real. Y una cartera de empresas."),
    ("J20", F6, "Comercio puro con capital casi cero (comprás con las señas).", "Comprar, vender y cobrar: la base de cualquier negocio. Ojo: monotributo y marcas falsificadas."),
    ("J14", F6, "Tu cancha (inventario y rotación) aplicada al comercio; comisión sin capital.", "Liquidación de stock: podría crecer a 'liquidador de stock para PyMEs'."),
    ("J37", F6, "Según el estudio, la que más construye: procesos, stock y despacho.", "Operar un depósito propio (fulfillment es un sector con startups). Ojo: espacio y responsabilidad por mercadería ajena."),
    ("J25", F6, "Producto muy argentino, personalizable, con seña.", "Trabajar con un proveedor (taller). El estudio sugiere fusionarla con las canastas (J23)."),
]

COLS = [
    ("Nº", 5), ("Código", 7), ("Familia", 22), ("Nombre", 34), ("Me gusta\n(Sí / Tal vez / No)", 12),
    ("Qué es (del estudio)", 60), ("Capital inicial", 18), ("Tiempo al primer cobro", 18), ("Precio / ticket", 24),
    ("Por qué está en la lista\n(OPINIÓN de Claude)", 38), ("Qué te enseña para la startup\n(OPINIÓN de Claude)", 38),
    ("Riesgos (del estudio)", 38), ("Mis notas", 30),
]

FONT = "Arial"
thin = Side(style="thin", color="BFBFBF")
border = Border(left=thin, right=thin, top=thin, bottom=thin)
hdr_fill = PatternFill("solid", fgColor="1F3864")
fam_fill = {F1: "DDEBF7", F2: "E2EFDA", F3: "FCE4D6", F4: "EDE2F6", F5: "DEEAF1", F6: "F2F2F2"}
body = Font(name=FONT, size=10)
bold = Font(name=FONT, size=10, bold=True)
wrap = Alignment(wrap_text=True, vertical="top")
center = Alignment(wrap_text=True, vertical="top", horizontal="center")

def lines(text, width):
    s = str(text or "")
    return sum(max(1, math.ceil(len(p) / max(4, int(width * 1.15)))) for p in s.split("\n"))

wb = Workbook()
ws = wb.active
ws.title = "Shortlist"
for ci, (h, w) in enumerate(COLS, 1):
    c = ws.cell(row=1, column=ci, value=h)
    c.font = Font(name=FONT, bold=True, color="FFFFFF", size=10); c.fill = hdr_fill; c.border = border
    c.alignment = Alignment(wrap_text=True, vertical="center", horizontal="center")
    ws.column_dimensions[get_column_letter(ci)].width = w
ws.row_dimensions[1].height = 48

for n, (iid, fam, why, learn) in enumerate(PICKS, 1):
    d = src[iid]
    vals = [n, iid, fam, d["nombre"], None, d.get("explicacion"), d.get("capital_inicial"),
            d.get("tiempo_primer_dolar"), d.get("precio"), why, learn, d.get("riesgos"), None]
    r = n + 1
    maxl = 1
    for ci, v in enumerate(vals, 1):
        c = ws.cell(row=r, column=ci, value=v)
        c.font = bold if ci == 4 else body
        c.border = border
        c.alignment = center if ci in (1, 2, 5) else wrap
        if ci == 3:
            c.fill = PatternFill("solid", fgColor=fam_fill[fam])
        maxl = max(maxl, lines(v, COLS[ci - 1][1]))
    ws.row_dimensions[r].height = min(409, max(30, maxl * 12.6 + 4))

last = len(PICKS) + 1
ws.freeze_panes = "E2"
ws.auto_filter.ref = f"A1:{get_column_letter(len(COLS))}{last}"
dv = DataValidation(type="list", formula1='"Sí,Tal vez,No"', allow_blank=True)
ws.add_data_validation(dv)
dv.add(f"E2:E{last}")

# ---- Hoja "Cómo usar" ----
g = wb.create_sheet("Cómo usar", 0)
g.column_dimensions["A"].width = 30
g.column_dimensions["B"].width = 100
r = 1
g.cell(row=r, column=1, value="SHORTLIST ETAPA 1 — negocios intermedios").font = Font(name=FONT, bold=True, size=14, color="1F3864"); r += 1
g.cell(row=r, column=1, value="Generada el 2026-10-06 a partir de TODAS-LAS-IDEAS.xlsx (633 ideas).").font = body; r += 2

def kv(k, v):
    global r
    a = g.cell(row=r, column=1, value=k); a.font = bold; a.alignment = wrap
    b = g.cell(row=r, column=2, value=v); b.font = body; b.alignment = wrap
    g.row_dimensions[r].height = max(15, lines(v, 100) * 12.6 + 2)
    r += 1

kv("Qué tenés que hacer", "1) Leé solo «Nombre», «Qué es» y «Por qué está en la lista». 2) En «Me gusta» elegí Sí / Tal vez / No y pintá de AMARILLO las que te entusiasman. 3) No analices: marcá por instinto. 4) En «Mis notas» escribí UNA línea de por qué te gusta o no. Eso es lo más valioso: con tus notas busco patrones (qué tipo de problema, cliente y trabajo te tira).")
kv("Tiempo estimado", "Estimación propia: 1 a 2 horas para las 39 ideas.")
kv("Familias", "Las ideas están agrupadas en 6 familias (columna con color). Si una familia entera te aburre, es un dato útil: anotalo.")
r += 1
g.cell(row=r, column=1, value="Cómo se eligieron").font = Font(name=FONT, bold=True, size=12, color="1F3864"); r += 1
kv("Paso 1: filtros automáticos", "De 633 ideas se sacaron: descartadas por la investigación (67), trabajo por hora / empleo (39), ideas para el exterior que necesitan inglés fluido (169), capital mayor a ~USD 800 o costos mayores a USD 150/mes (35), y las que exigen poner la cara en cámara (35). Una idea puede caer en más de un filtro. Quedaron 387.")
kv("Paso 2: elección a mano", "De esas 387, Claude eligió 39 con estos criterios: empresa propia; capital que entra en tus ~USD 1.300 dejando reserva; mercado en español; sin cara en redes; la IA como ventaja; posibilidad de crecer más allá de tus horas; y que te enseñe algo útil para la startup. Se evitaron las ideas repetidas. Se dejaron afuera las del Día de la Madre (2026-10-18) porque quedan muy pocos días.")
kv("Ideas que quedaron afuera", "No están muertas. Si algo del Excel general te gusta y no está acá, se agrega.")
r += 1
g.cell(row=r, column=1, value="Honestidad sobre los datos").font = Font(name=FONT, bold=True, size=12, color="1F3864"); r += 1
kv("De dónde salen", "«Qué es», capital, tiempo, precio y riesgos vienen de los estudios del 2026-10-01 y 2026-10-02 (detalle y fuentes en research/). NO se volvieron a verificar el 2026-10-06. Donde el texto dice «Estimación», «estimado del informe» o «sin verificar», es eso: no es un dato medido.")
kv("Opinión", "Las columnas «Familia», «Por qué está en la lista» y «Qué te enseña para la startup» son OPINIÓN de Claude, no datos.")
kv("Antes de ejecutar", "Cualquier idea que elijas pasa por una ficha en ideas/ donde se re-verifican precios, demanda y riesgos con fuentes actuales antes de invertir un peso.")

wb.active = 0
wb.save(OUT)
print("ideas:", len(PICKS), "->", OUT)
