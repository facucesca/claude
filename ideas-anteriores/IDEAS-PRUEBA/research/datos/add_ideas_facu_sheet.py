# NOTA 2026-10-09: superado por build_fase2_sheet.py (la hoja "Ideas de Facu" se consolidó en "Fase 2"). No correr: recrearía la hoja vieja.
# Agrega (o reemplaza) la hoja "Ideas de Facu" en TODAS-LAS-IDEAS.xlsx sin tocar la hoja "Ideas"
# (preserva las marcas amarillas de Facu). Datos: síntesis research/2026-10-08-ideas-de-facu-analisis.md.
# Puntajes = OPINIÓN de Claude fundada en los informes de research/fuentes/2026-10-08-*.md.
import math, sys
from openpyxl import load_workbook
from openpyxl.styles import Font, Alignment, PatternFill, Border, Side
from openpyxl.utils import get_column_letter
from openpyxl.worksheet.datavalidation import DataValidation

P = r"C:\FACU\IDEAS-PRUEBA\TODAS-LAS-IDEAS.xlsx"
try:
    open(P, "r+b").close()
except PermissionError:
    sys.exit("LOCKED: cerrá el Excel y volvé a correr")

R = "research/fuentes/"
ROWS = [
    ("L9 + L5",
     "Página de cálculos de ingeniería (stock, ABC, Pareto) con IA que sugiere mejoras y deriva a un 1:1 con Facu · IA analista de negocios que dice si algo será rentable",
     "«Diagnóstico de stock en 5 minutos»: subís tu Excel → ABC, plata parada, quiebres y punto de pedido explicados por IA (números con fórmulas fijas) → consultoría paga. L5 como módulo de «qué productos te dejan plata»",
     6.0, (6, 4, 6, 6, 8, 5, 7),
     "Calculadoras sueltas gratis (miniwebtool, The Retail Exec); software de inventario que cobra por conectarse a los datos (Prediko desde USD 49/mes, Netstock desde USD 900/mes); validadores de ideas gratis (ValidatorAI, ~288.000 ideas)",
     "1,77 M de certificados MiPyME (2023). No se encontró herramienta en español «subí tu Excel → diagnóstico». Sin dato de disposición a pagar",
     "Mejor vehículo de etapa 1. L5 sola: 3/10",
     "Diagnóstico gratis a 30 negocios de 2 segmentos; si ≥10 mandan archivo y ≥2-3 pagan → construir la web. < USD 200, 2-4 semanas",
     R + "2026-10-08-L5-L9-herramientas-analisis.md", "Propuesta: negocio principal de etapa 1"),
    ("L4",
     "Revivir con IA a seres queridos: nuevas fotos y videos, réplica de voz",
     "«Homenaje»: restaurar fotos + video homenaje + animación sin voz, con línea roja pública; piloto B2B con cocherías",
     5.6, (5, 5, 5, 5, 8, 4, 7),
     "StoryFile en concurso (2024), Eternos pivoteó (2025), 2wai con rechazo masivo (2025); Vivo Recuerdo (España, 150+ funerarias); crematorios del Reino Unido £50-110 por video",
     "353.428 muertes (2024); no se encontró cochería con video homenaje (búsqueda limitada). Art. 53 CCyC: imagen y voz requieren consentimiento de los herederos",
     "«Revivir» (voz o chatbot): 3,9/10, no recomendado. Homenaje: servicio chico y ético",
     "Pack homenaje B2C + 3-5 cocherías; < USD 200, 4 semanas",
     R + "2026-10-08-L4-recuerdos-ia.md", "En reserva"),
    ("L8",
     "Edición de video automática para empresas con videos parecidos (inmobiliarias, concesionarias)",
     "Video automático por unidad (fotos + ficha → video) para inmobiliarias y agencias de usados; servicio con motor propio → producto «cero intervención»",
     5.5, (5, 4, 5, 4, 7, 6, 4),
     "AutoReel, Reeltors, Reel-E (EE.UU., USD 25-300/mes); render a menos de USD 0,30 por video",
     "Zonaprop tiene 11.000+ clientes y planea IA para avisos (riesgo principal); no se encontró producto local",
     "Mejor opción de «producto» en etapa 1; no es startup grande",
     "30 inmobiliarias + 30 agencias de usados; ≥5 pagan y ≥3 renuevan. USD 10-60, 3-4 semanas",
     R + "2026-10-08-L3-L8-A3-video-y-visualizacion.md", "En reserva (1.ª)"),
    ("L10",
     "Sistema de stock con IA y cámara para supermercados y almacenes que descuenta lo que se lleva el cliente",
     "Auditoría de góndola y faltantes por FOTO DE CELULAR para distribuidoras y marcas medianas del canal tradicional (variante: pedido sugerido para preventistas)",
     5.4, (7, 5, 4, 4, 6, 7, 5),
     "Amazon anunció el cierre de sus tiendas Go y Fresh (TechCrunch, 2026-01-27); Grabango cerró (2024); crecen Trax, Ailet, Involves, Teamcore, Simbe, Focal y Caper",
     "Ya se intentó: Go2Future/MiniGo (2022) y Carrefour Flash Pilar (2023); Sensify (cámaras en heladeras, inversión de Kamay y Arca). Canal tradicional ≈35% del consumo masivo, 194.700+ puntos de venta (NielsenIQ, 2026)",
     "«Amazon Go argentino»: 2,0/10. Versión por foto de celular: mejor candidata a startup",
     "Entrevistas + prueba técnica con 100 fotos (≥90% de acierto) + piloto con 1-2 distribuidoras (≥3 de 10 aceptan piloto pago). < USD 200, 4 semanas",
     R + "2026-10-08-L10-stock-ia-camara.md", "Propuesta: experimento en paralelo / candidata de etapa 2"),
    ("L6",
     "«Uber de la logística empresarial»: une en todo el país a quien necesita transporte (por ejemplo, frutas y verduras) con transportistas",
     "Broker manual por WhatsApp en UN corredor frutihortícola, centrado en el viaje de vuelta vacío, SIN poner capital de trabajo. Etapa 2 (hipótesis): servicios al camionero chico",
     4.7, (8, 5, 4, 3, 4, 6, 3),
     "Convoy cerró (2023, USD 900 M+); Kobo360 se fundió por capital de trabajo; Transfix y BlackBuck vendieron su negocio de fletes; Uber Freight pierde plata (2026); ganan Porter (urbano) y los servicios al camionero",
     "91% de la carga va en camión (BCR, 2018); Avancargo (desde ~2017, pasó a software); apps de granos; Fletalo; grupos de WhatsApp. Mercado Central ≈1,4 M t/año",
     "Uber nacional: no. Experimento para aprender el sector: sí",
     "15-20 entrevistas en el Mercado Central + 3-5 viajes reales; ≥3 viajes y ≥1 cliente que repite a través de Facu. Máx. USD 200, 4 semanas",
     R + "2026-10-08-L6-logistica.md", "En reserva"),
    ("L1",
     "App intermediaria para transacciones donde se desconfía (Argentina o exterior); pago retenido hasta que se cumpla lo acordado",
     "«Cierre seguro» de autos usados entre particulares: verificar + coordinar que pago y firma pasen juntos, SIN custodiar plata",
     4.6, (7, 4, 6, 3, 4, 5, 3),
     "Escrow.com: A$12,3 M en 2025, con volumen en caída 4 años seguidos; Payoneer Escrow cerró (2018); Caramel (autos) comprada por eBay (2025)",
     "≈12.170 reportes de estafas en compraventas online (UFECI 2024, estimación); 1.887.024 transferencias de usados (2025). Custodiar fondos = PSP regulado (BCRA)",
     "Escrow genérico: chico. Candidata de etapa 2 en el nicho autos",
     "15-20 entrevistas + página con precio + 1-3 operaciones; consulta legal antes. Máx. USD 200, 4 semanas",
     R + "2026-10-08-L1-intermediario.md", "En reserva (candidata de etapa 2)"),
    ("A3",
     "Visualizador de cómo quedarían remeras, indumentaria personalizada, banners (app o página)",
     "«Cotizador visual» para talleres: mockup + precio por técnica y cantidad + plazo al instante",
     4.5, (4, 3, 4, 5, 7, 4, 6),
     "Printful (gratis), Placeit (USD 7,47/mes), Zakeke y Customily (USD 49-300/mes + comisión)",
     "Sin datos de cantidad de talleres ni de demanda",
     "Solo como cotizador, después de las entrevistas",
     "15-20 entrevistas a talleres + piloto a mano con 2-3. < USD 30",
     R + "2026-10-08-L3-L8-A3-video-y-visualizacion.md", "En reserva"),
    ("L7",
     "App de huella de carbono para personas o empresas, con suscripción y seguimiento",
     "Personas: descartar. Empresas obligadas (EUDR, Mendoza): servicio, mejor como módulo de la consultora",
     4.0, (5, 5, 3, 4, 5, 4, 4),
     "Klima cerró (2025); Commons es gratis; software B2B en consolidación (Greenly compró Normative, 2026)",
     "EUDR desde el 2026-12-30 (soja, carne, cueros), pero VISEC es gratis; Mendoza obliga a reportar emisiones",
     "App para personas: 2/10. Empresas: 4/10, validar con entrevistas",
     "20 entrevistas a empresas obligadas; ≥5 con un pedido real y ≥1 que paga",
     R + "2026-10-08-L2-L7-apps-consumo-y-carbono.md", "Personas: descartada · Empresas: en reserva"),
    ("L2",
     "App para sacar fotos a los precios del súper y saber cuánto llevás",
     "—", 3.0, (4, 2, 3, 2, 7, 4, 6),
     "Al menos 5 apps gratis en Google Play («Calculadora de compras», «SuperJusto»); app de Carrefour Argentina",
     "Ratoneando, Mirá Precios (~15.000 usuarios, no cobra), Precios Claros",
     "No como negocio", "Solo si se quiere aprender a lanzar una app (máx. USD 200)",
     R + "2026-10-08-L2-L7-apps-consumo-y-carbono.md", "Descartada por ahora"),
    ("L3",
     "Automatización absoluta de clips en distintos canales (apps que pagan por vistas)",
     "—", 3.0, (5, 3, 2, 2, 6, 2, 2),
     "Pago efectivo ~USD 0,39 cada 1.000 vistas; Instagram y YouTube bajan el alcance de lo re-subido (2026); el scanner de campañas ya existe en Apify (83 usuarios)",
     "—", "No", "—",
     R + "2026-10-08-L3-L8-A3-video-y-visualizacion.md", "Descartada"),
]

COLS = [("Código", 9), ("Tu idea (palabras de Facu)", 40), ("Versión que tiene sentido (OPINIÓN de Claude)", 48),
        ("Puntaje (promedio simple)", 11), ("Problema", 9), ("Pago", 8), ("Competencia", 11), ("Ventaja de Facu", 10),
        ("Factibilidad", 11), ("Escalabilidad", 11), ("Riesgo (10 = bajo)", 10),
        ("Parecidos en el mundo (DATOS)", 48), ("Argentina (DATOS)", 48), ("Veredicto", 34), ("Cómo validar", 44),
        ("Informe completo", 40), ("Estado", 22), ("Me gusta\n(Sí / Tal vez / No)", 12), ("Mis notas", 34)]

wb = load_workbook(P)
if "Ideas de Facu" in wb.sheetnames:
    del wb["Ideas de Facu"]
ws = wb.create_sheet("Ideas de Facu", 1)
thin = Side(style="thin", color="BFBFBF")
border = Border(left=thin, right=thin, top=thin, bottom=thin)
hdr = PatternFill("solid", fgColor="1F3864")
for ci, (h, w) in enumerate(COLS, 1):
    c = ws.cell(row=1, column=ci, value=h)
    c.font = Font(name="Arial", bold=True, color="FFFFFF", size=10)
    c.fill = hdr
    c.border = border
    c.alignment = Alignment(wrap_text=True, vertical="center", horizontal="center")
    ws.column_dimensions[get_column_letter(ci)].width = w
ws.row_dimensions[1].height = 48

for ri, (code, idea, ver, sc, crit, par, arg, verd, val, inf, est) in enumerate(ROWS, 2):
    vals = [code, idea, ver, sc, *crit, par, arg, verd, val, inf, est, None, None]
    mx = 1
    for ci, v in enumerate(vals, 1):
        c = ws.cell(row=ri, column=ci, value=v)
        c.font = Font(name="Arial", size=10, bold=(ci in (1, 4)))
        c.border = border
        centered = 4 <= ci <= 11 or ci in (1, 18)
        c.alignment = Alignment(wrap_text=True, vertical="top", horizontal="center" if centered else None)
        if ci == 4:
            c.number_format = "0.0"
        w = COLS[ci - 1][1]
        mx = max(mx, sum(max(1, math.ceil(len(p) / max(4, int(w * 1.15)))) for p in str(v or "").split("\n")))
    ws.row_dimensions[ri].height = min(409, max(30, mx * 12.6 + 4))

last = len(ROWS) + 1
ws.freeze_panes = "C2"
ws.auto_filter.ref = f"A1:{get_column_letter(len(COLS))}{last}"
dv = DataValidation(type="list", formula1='"Sí,Tal vez,No"', allow_blank=True)
ws.add_data_validation(dv)
dv.add(f"R2:R{last}")

n = last + 2
ws.cell(row=n, column=1, value="Notas").font = Font(name="Arial", bold=True, size=11, color="1F3864")
for i, t in enumerate([
    "Hoja agregada el 2026-10-08. Síntesis completa: research/2026-10-08-ideas-de-facu-analisis.md.",
    "Puntajes 1-10 = OPINIÓN de Claude fundada en datos; el promedio es simple (los criterios no pesan igual). Ninguna idea tiene todavía evidencia de que alguien en Argentina pague: eso se valida con entrevistas.",
    "Las columnas «Parecidos» y «Argentina» son datos con fuente en el informe de cada idea. «Versión que tiene sentido» y «Veredicto» son opinión.",
], 1):
    c = ws.cell(row=n + i, column=1, value=t)
    c.font = Font(name="Arial", size=10)
    ws.merge_cells(start_row=n + i, start_column=1, end_row=n + i, end_column=8)

wb.save(P)

# Verificación: las marcas de Facu en la hoja "Ideas" siguen intactas
wb2 = load_workbook(P)
w2 = wb2["Ideas"]
marcadas = sum(1 for row in w2.iter_rows(min_row=2)
               if any(c.fill and c.fill.fill_type and c.fill.fgColor.type == "rgb"
                      and c.fill.fgColor.rgb in ("FFFFFF00", "FF00B0F0") for c in row))
print("hojas:", wb2.sheetnames, "| filas marcadas preservadas:", marcadas)
