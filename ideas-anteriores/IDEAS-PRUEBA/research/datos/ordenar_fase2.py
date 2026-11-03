# Ordena los ganadores de la hoja "Fase 2" de TODAS-LAS-IDEAS.xlsx (pedido de Facu, 2026-10-14):
#   1. Crea la hoja "Orden de Claude": los 74 en una sola tabla, de mayor a menor, con 7 criterios (opinión de Claude).
#   2. Ordena las filas DENTRO de cada bloque de "Fase 2" con ese mismo orden y agrega la columna "Puesto".
# No elimina nada. Hace respaldo y verifica que estén los 74, que ninguna fila cambie de contenido y que las 33
# marcas de la hoja "Ideas" sigan intactas. Guarda los puntajes en research/datos/2026-10-14-orden-fase2.json.
# Uso: python research/datos/ordenar_fase2.py
import json
import shutil
import sys
from copy import copy
from pathlib import Path

import openpyxl
from openpyxl.styles import Alignment, Border, Font, PatternFill, Side
from openpyxl.utils import get_column_letter

ROOT = Path(__file__).resolve().parents[2]
XLSX = ROOT / "TODAS-LAS-IDEAS.xlsx"
BACKUP = ROOT / "research" / "datos" / "archivo" / "2026-10-14-TODAS-LAS-IDEAS-antes-de-ordenar.xlsx"
OUT_JSON = ROOT / "research" / "datos" / "2026-10-14-orden-fase2.json"
HOJA = "Orden de Claude"

CRIT = ["G", "P", "M", "H", "C", "R", "V"]
CRIT_NOMBRE = {
    "G": "Gusto de Facu (marca y nota; 5 = celeste, favorita o nota entusiasta; 1 = la descartó)",
    "P": "Producto global (5 = el mismo producto para miles de clientes; 1 = trabajo a medida u horas)",
    "M": "Mercado (tamaño y ganas de pagar en Argentina y Latinoamérica)",
    "H": "Hueco en Argentina (5 = no se encontró nada local; 1 = ya resuelto y conocido)",
    "C": "Construible con Claude y poco capital (5 = software puro; 1 = hardware pesado o mucho capital)",
    "R": "Regulación y riesgo (5 = bajo; 1 = muy regulado o trampa conocida)",
    "V": "Ventaja de Facu (stock y depósito, logística, procesos, CEMEVA, Sporting)",
}
TERR = {
    "S": "Stock y piezas (ing. industrial)", "O": "Cámaras e imágenes con IA", "B": "Presencia y sensores (RFID, GPS)",
    "X": "Conectar dos partes", "D": "Papeles y procesos como producto", "V": "Contenido y video con IA",
    "W": "Software y datos (otros)",
}

# código: (bloque, nombre corto, territorio, G, P, M, H, C, R, V, por qué (opinión), qué averiguar primero)
I = {
    # ---- Bloque A: ideas propias de Facu (libreta) ----
    "L9 + L5": ("A", "Diagnóstico de stock en 5 minutos (subís el Excel → ABC, plata parada, quiebres, punto de pedido) + 1:1", "S", 5, 4, 4, 4, 5, 5, 5,
                "Tu favorita y la mejor de tus ideas en el análisis del 2026-10-08. Producto igual para cualquier negocio con stock, usa lo de Sporting y casi no necesita capital.",
                "¿Los comercios pagan por un diagnóstico o solo si viene con la solución? ¿Qué herramientas de stock con IA ya usan?"),
    "L4": ("A", "Homenaje con IA (fotos restauradas + video, sin voz)", "V", 3, 3, 3, 3, 4, 3, 1,
           "Servicio chico y delicado (ética del duelo); no usa tu ventaja.", ""),
    "L8": ("A", "Video automático por unidad para inmobiliarias y agencias de usados", "V", 3, 4, 3, 2, 5, 5, 1,
           "Producto posible, pero ya hay herramientas de video y staging desde fotos; no usa tu ventaja.", ""),
    "L10": ("A", "Auditoría de góndola y faltantes por foto de celular", "O", 5, 5, 4, 3, 4, 4, 4,
            "Tu favorita: une cámaras con stock. Afuera Trax y ParallelDots; acá había jugadores (2026-10-08). Mismo territorio que L12 y COM-2-4.",
            "¿Las distribuidoras pagan por saber qué falta en la góndola? ¿Cuánto les cuesta hoy relevarlo?"),
    "L6": ("A", "Uber de la logística empresarial (broker en un corredor)", "X", 5, 3, 5, 2, 3, 3, 5,
           "Tu favorita y conocés el rubro, pero acá ya están Avancargo y otras bolsas de cargas, y la versión grande fracasó afuera (Convoy cerró).",
           "¿Hay un corredor sin cubrir? ¿Hay margen para un broker sin capital?"),
    "L1": ("A", "Cierre seguro de autos usados entre particulares", "X", 5, 3, 4, 3, 3, 2, 2,
           "Favorita, pero toca plata de terceros y riesgo legal: mejor para la etapa 2.", ""),
    "A3": ("A", "Cotizador visual para talleres de estampado y merchandising", "V", 4, 4, 3, 2, 5, 5, 2,
           "Los mockups ya son gratis (Printful, Placeit); el valor estaría en cotizar al instante.", ""),
    "L7": ("A", "Huella de carbono para personas o empresas", "W", 3, 3, 2, 3, 4, 3, 2,
           "Las personas no pagan; para empresas obligadas es un servicio chico.", ""),
    "L2": ("A", "App para sacar fotos a los precios del súper", "W", 2, 5, 2, 1, 5, 5, 1,
           "Ya existe gratis en varias apps.", ""),
    "L3": ("A", "Automatización absoluta de clips", "V", 2, 3, 3, 2, 4, 1, 1,
           "Las plataformas castigan lo 100% automático desde 2026.", ""),
    # ---- Bloque B: las 33 marcadas entre las 633 ----
    "P1": ("B", "Scrapers vendidos en Apify (nichos LATAM)", "W", 3, 5, 3, 3, 5, 3, 2,
           "Global y construible con Claude, pero mercado exterior, riesgo legal del scraping y lejos de tus gustos.", ""),
    "P2": ("B", "Calculadoras y mini-herramientas web gratis (SEO) + MCP", "W", 3, 5, 2, 3, 5, 5, 3,
           "Barato y global, pero tarda meses en cobrar; sirve como imán de clientes para L9 y C34.",
           "¿Qué cálculos busca la gente en Google y cuánto volumen tienen?"),
    "P3": ("B", "Micro-SaaS de alertas B2B de nicho (licitaciones, precios)", "W", 3, 5, 3, 3, 5, 5, 2,
           "Producto global y simple; falta un nicho con dolor real.",
           "¿Qué nicho pierde plata por enterarse tarde de algo (licitaciones, precios)?"),
    "P4": ("B", "Clipping pagado por vistas + scanner de campañas", "V", 3, 3, 3, 2, 4, 2, 1,
           "Dependés de plataformas que cambian las reglas.", ""),
    "P8": ("B", "Canal de YouTube largo hecho con IA", "V", 3, 4, 3, 2, 4, 2, 1,
           "El canal típico gana USD 0 y hubo purgas de canales 'inauténticos' (enero 2026, según el estudio).", ""),
    "PD5": ("B", "Música generada con IA en Spotify", "V", 3, 4, 1, 1, 5, 1, 1,
            "Trampa: Spotify borró 75 millones de canciones spam (según el estudio).", ""),
    "X1d": ("B", "Pick-to-light casero para depósitos", "S", 4, 4, 3, 4, 2, 5, 5,
            "Hardware que conecta con L14; mejor como módulo de un sistema de stock que solo.",
            "¿Cuánto cuesta armarlo por estante y cuánto tiempo ahorra al buscar?"),
    "C14": ("B", "Estudio de tiempos remoto (el cliente filma, vos analizás)", "S", 3, 2, 3, 4, 4, 5, 5,
            "Tu oficio puro, pero es servicio (horas), no producto.",
            "¿Se puede automatizar el análisis del video para que sea producto?"),
    "C20": ("B", "Coaching de mejora continua / Kaizen mensual", "S", 3, 1, 3, 3, 3, 5, 5,
            "Servicio a medida: justo lo que querés evitar.", ""),
    "C34": ("B", "Calculadoras web de ingeniería industrial como imán de clientes", "S", 5, 4, 2, 3, 5, 5, 5,
            "Celeste y tu oficio; casi gratis de hacer. Sola gana poco: funciona como puerta de entrada de L9 (diagnóstico + 1:1).",
            "¿Qué cálculos busca la gente? ¿Cuántos pasarían a pagar un diagnóstico?"),
    "D3": ("B", "Setup de Claude para equipos de PyME (Skills + capacitación)", "D", 3, 2, 4, 3, 5, 5, 4,
           "Demanda real y tu experiencia con Claude, pero cada empresa es un caso (a medida).",
           "¿Se puede empaquetar para un rubro, siempre igual?"),
    "D9": ("B", "MCP servers a medida para PyMEs", "W", 3, 1, 2, 3, 4, 5, 3,
           "A medida y técnico.", ""),
    "D27": ("B", "App para la tienda de Shopify", "W", 3, 5, 3, 2, 3, 4, 1,
            "Mercado exterior muy competido; la investigación la descartó por dificultad.", ""),
    "D29": ("B", "App en el directorio de ChatGPT", "W", 3, 5, 2, 3, 4, 4, 1,
            "Sin cobro dentro de ChatGPT, según el estudio.", ""),
    "D35": ("B", "Construir y vender apps hechas con IA", "W", 3, 4, 2, 3, 5, 5, 1,
            "Las apps sin ingresos se venden barato (USD 100-5.000 según el estudio).", ""),
    "D36": ("B", "Generador de informes de relevamiento con IA (fotos + checklist → PDF)", "D", 3, 4, 3, 3, 5, 5, 4,
            "Producto útil para técnicos e inspectores; cercano a tu perfil.",
            "¿Qué oficio hace más relevamientos y odia escribir el informe?"),
    "D38": ("B", "Calculadoras logísticas gratis (EOQ, punto de pedido)", "S", 3, 4, 2, 3, 5, 5, 5,
            "Igual que C34: imán de clientes, no negocio solo.",
            "Mismo que C34: volumen de búsquedas y conversión a pago."),
    "E13": ("B", "Edición de videos largos de YouTube con IA", "V", 3, 2, 3, 2, 4, 4, 1,
            "Editar es commodity (USD 5,5-8,5 por hora según el estudio).", ""),
    "F5": ("B", "Constructor de Claude Skills a medida", "D", 3, 2, 3, 3, 5, 5, 4,
           "A medida por empresa.", ""),
    "F9": ("B", "Conectores MCP entre Claude y software argentino (Tango, Colppy)", "W", 3, 5, 3, 4, 4, 4, 3,
           "Producto global (el mismo conector para todos los que usan ese sistema); depende de que esas empresas no lo hagan ellas.",
           "¿Tango, Colppy o Xubio ya tienen conector o API abierta?"),
    "F11": ("B", "Endpoints x402 (vender datos a agentes de IA)", "W", 3, 5, 1, 3, 4, 4, 1,
            "Volumen mundial muy chico hoy.", ""),
    "F16": ("B", "Ordenar datos de PyMEs para que la IA sirva", "D", 3, 1, 3, 3, 4, 5, 4,
            "Servicio a medida.", ""),
    "F17": ("B", "IA para estudios contables argentinos", "D", 3, 3, 4, 3, 5, 4, 3,
            "Mercado grande y con prescriptores, pero la implementación es por estudio.", ""),
    "F21": ("B", "Kit IA para inmobiliarias", "D", 3, 3, 3, 3, 5, 5, 1,
            "Muchas herramientas parecidas; no usa tu ventaja.", ""),
    "F36": ("B", "Método: traer al español lo que en EE.UU. ya tiene inversión", "W", 3, 3, 3, 3, 4, 4, 3,
            "No es una idea: es el método que ya aplicamos en NICHOS-Y-PROBLEMAS.", ""),
    "I29": ("B", "Video personalizado de Papá Noel", "V", 4, 4, 3, 3, 5, 3, 1,
            "Caja rápida de temporada (ventana 2026-11-15 a 2026-12-22 según el estudio), no negocio de largo plazo. Si se prueba, decidir antes de noviembre.", ""),
    "K9": ("B", "Reporte ABC 'qué productos te dan plata'", "S", 3, 3, 3, 3, 5, 5, 5,
           "Es parte de L9; serviría como primer producto pago del diagnóstico.",
           "Se averigua junto con L9."),
    "K11": ("B", "Control de vencimientos y FIFO para almacén o dietética", "S", 3, 3, 3, 3, 5, 5, 5,
            "Módulo natural de un sistema de stock (L9, L14).",
            "Se averigua junto con L9 y L14."),
    "K18": ("B", "Diagramas de procesos (BPMN) para PyME", "S", 3, 2, 2, 3, 5, 5, 5,
            "Tu oficio, pero es servicio y paga poco.", ""),
    "T7": ("B", "Videos de propiedades desde las fotos", "V", 3, 4, 3, 2, 5, 5, 1,
           "Igual que L8.", ""),
    "T19": ("B", "Plantillas Remotion vendibles", "V", 3, 5, 2, 3, 5, 5, 1,
            "Producto digital chico, mercado exterior.", ""),
    "R2": ("B", "Ropa 'puesta' en modelo IA para marcas", "V", 4, 4, 3, 2, 5, 4, 1,
           "Hay muchas herramientas; el valor estaría en la versión para talleres (A3).", ""),
    "R28": ("B", "Pantallas de precios que se actualizan solas", "W", 3, 4, 3, 3, 4, 5, 3,
            "Útil con inflación; las etiquetas electrónicas ya existen (VusionGroup, Pricer) pero son caras.", ""),
    # ---- Bloque C: ganadores de NICHOS-Y-PROBLEMAS ----
    "EDU-1-4": ("C", "RFID para saber si falta un chico en jardines y colegios", "B", 5, 5, 3, 4, 2, 2, 2,
                "Celeste y lo más original, pero necesita hardware instalado y toca datos de menores y responsabilidad si falla.",
                "¿Una directora de jardín pagaría? ¿Qué pasó la última vez que no encontraron a un chico?"),
    "EDU-5-3": ("C", "App de profesores particulares ('Instagram de profesores', pago retenido hasta puntuar la clase)", "X", 5, 5, 3, 3, 5, 3, 1,
                "Te gusta mucho, es global y se construye rápido. Bajan: Superprof ya está, cada profe paga poco, retener pagos está regulado y no usa tu ventaja.",
                "¿Cuántas clases se pierden por cancelaciones? ¿Profes y alumnos pagarían por la garantía?"),
    "SER-4-4": ("C", "Ausentismo: fichar con RFID y validar certificados médicos con IA", "B", 5, 4, 4, 2, 4, 3, 2,
                "Celeste, pero fichar con tarjeta ya es común; el hueco posible es validar certificados (decreto 2026 a verificar).",
                "¿Las empresas tienen un problema real con certificados truchos?"),
    "SAL-4-2": ("C", "App para pedir enfermeros y cuidadores por hora", "X", 4, 5, 4, 3, 4, 2, 1,
                "Hueco de intermediario, pero es salud: matrículas y responsabilidad.", ""),
    "SAL-5-2": ("C", "Mercado B2B de compradores y proveedores (con vuelta de tuerca)", "X", 4, 5, 4, 2, 4, 3, 3,
                "Un B2B general compite con Mercado Libre Negocios; solo tendría sentido en un rubro puntual.", ""),
    "ALI-2-2": ("C", "Excedentes de panaderías y comercios (todo lo desechable)", "X", 2, 5, 3, 1, 5, 4, 1,
                "Cheaf ya tiene más de 700 comercios en Argentina.", ""),
    "ALI-2-4": ("C", "Cálculo nutricional y etiquetado para comida casera", "D", 5, 5, 3, 2, 5, 2, 2,
                "Te encantó, pero ANMAT ya da una calculadora gratis y la ley puede derogarse.", ""),
    "ALI-2-5": ("C", "Registros de higiene y temperatura en papel", "D", 3, 5, 3, 3, 5, 3, 3,
                "Orden sanitario para productores chicos; el control municipal es desparejo.", ""),
    "ALI-3-2": ("C", "Cervecerías artesanales sin control de barriles y lotes", "D", 3, 5, 2, 3, 5, 4, 3,
                "Nicho chico.", ""),
    "ALI-4-4": ("C", "Calidad de fruta por foto", "O", 4, 5, 3, 3, 3, 5, 3,
                "Foto + IA para empacadores; necesita miles de fotos etiquetadas.",
                "¿Cuánto pierde un empacador por discusiones de calidad?"),
    "LOG-1-4": ("C", "Pedidos y cotizaciones de fletes por WhatsApp y mail cargados a mano", "D", 2, 5, 4, 5, 5, 5, 5,
                "Mejor puntaje objetivo: producto global, CEMEVA, nada local. Pero a vos no te entusiasma ('medio flojo').",
                "Charlar con 3 transportistas: ¿cuántos pedidos por WhatsApp cargan por día y cuánto les cuesta?"),
    "LOG-3-4": ("C", "Productividad de operarios de depósito sin medir", "S", 3, 5, 3, 4, 4, 4, 5,
                "Tu experiencia de depósito; producto global para depósitos y operadores logísticos.",
                "¿Cómo miden hoy la productividad? ¿Paga el dueño o el operador logístico?"),
    "COM-2-3": ("C", "Fiado anotado en libreta", "D", 3, 5, 4, 3, 5, 4, 2,
                "Mercado enorme de almacenes; Treinta ya opera acá.", ""),
    "COM-2-4": ("C", "Robos hormiga en autoservicios (IA sobre las cámaras que ya tienen)", "O", 5, 5, 4, 4, 4, 3, 3,
                "Une tu L10 y L12: software sobre cámaras existentes. Riesgos: privacidad y falsas alarmas.",
                "¿Cuánto pierde un autoservicio por mes en robos? ¿Pagaría un porcentaje de eso?"),
    "COM-3-5": ("C", "Identificar una pieza por foto (sobre una regla) en ferreterías y bulonerías", "S", 5, 5, 4, 5, 4, 5, 5,
                "Tu idea de la regla más tu oficio de stock; no se encontró nada local; arranca como software puro y crece hacia L14.",
                "¿Cuánto tarda un mostrador en encontrar una pieza? ¿Cuántas ventas se pierden por no encontrarla?"),
    "COM-4-4": ("C", "Contar cuánta gente entra al local", "O", 3, 5, 3, 2, 4, 3, 2,
                "Sumato ID ya lo hace acá.", ""),
    "CON-2-3": ("C", "Presupuestar pintura o techos sin ir a medir (foto, dron)", "O", 4, 5, 3, 5, 3, 4, 1,
                "Hueco claro, pero medir en 3D con fotos es técnicamente difícil y no usa tu ventaja.", ""),
    "IND-4-4": ("C", "Cajas impresas a medida para marcas chicas", "X", 3, 4, 3, 4, 2, 5, 2,
                "Es fábrica o e-commerce de packaging, no software.", ""),
    "SER-4-5": ("C", "Base de datos de antecedentes de choferes y operarios", "W", 3, 5, 3, 1, 4, 2, 1,
                "Ya existe (HireRight compró la argentina Inquiro Vitae).", ""),
    "EDU-1-5": ("C", "Combi escolar con seguimiento (GPS del celular)", "B", 3, 5, 2, 4, 5, 3, 3,
                "Simple con el GPS del celular del chofer; ticket chico.", ""),
    "EDU-2-1": ("C", "Academias: alumnos, cuotas y asistencia (variante RFID para gimnasios)", "B", 3, 5, 3, 3, 4, 4, 1,
                "Gestión de academias; la variante RFID para gimnasios no está verificada.", ""),
    "EDU-3-1": ("C", "Predecir qué alumnos van a abandonar la universidad", "W", 2, 4, 2, 3, 3, 3, 1,
                "Vos dudaste; venderle a universidades es lento.", ""),
    "EDU-3-2": ("C", "Equivalencias de materias con IA", "D", 2, 4, 2, 4, 5, 4, 1,
                "Existe afuera; venderle a universidades es lento.", ""),
    "AUT-1-2": ("C", "Encontrar repuestos y stock en negocios cercanos", "S", 4, 5, 4, 4, 3, 5, 4,
                "Tu tema de stock; el desafío es conectar el stock de cada casa de repuestos (vuelve a L14).",
                "¿Cuántas llamadas hace un taller por día buscando repuestos? ¿Las casas compartirían su stock?"),
    "AGR-4-2": ("C", "Alambrado virtual con collares (como Halter)", "B", 4, 4, 3, 3, 1, 3, 2,
                "Es lo que hace Halter: hardware pesado y mucho capital.", ""),
    "AGR-4-4": ("C", "Pesar hacienda sin encierre", "B", 2, 4, 3, 3, 2, 5, 2,
                "Hardware de campo; vos pusiste 'tal vez'.", ""),
    # ---- Bloque D: ideas nuevas de Facu ----
    "L11": ("D", "Plataforma de aprendizaje confiable", "W", 4, 5, 3, 3, 4, 4, 1,
            "La confianza tarda años en construirse y las comisiones son chicas.", ""),
    "L12": ("D", "Cámaras de seguridad con IA en Argentina", "O", 5, 5, 4, 3, 4, 3, 3,
            "Tu territorio de cámaras; ya hay jugadores (Sumato ID, Veesion). Se averigua junto con COM-2-4.",
            "Se averigua junto con COM-2-4."),
    "L13": ("D", "RFID para otras cosas / stickers", "B", 4, 3, 2, 3, 2, 4, 2,
            "Tecnología buscando problema; se suma a los casos concretos con RFID.", ""),
    "L14": ("D", "Stock de piezas chicas (mercerías, bulonerías, ferreterías, multimarcas), adaptable y anti-robo", "S", 5, 5, 4, 4, 3, 5, 5,
            "Tu interés más constante; producto global; une stock, ingeniería y tecnología física. Falta saber cuántos comercios hay y qué usan.",
            "¿Cuántas ferreterías, bulonerías y mercerías hay? ¿Qué sistema usan? ¿Cuánto pierden por desorden y robo?"),
    "L15": ("D", "Intercambiar efectivo por transferencia", "X", 1, 4, 4, 1, 3, 1, 1,
            "Descartada por Facu el 2026-10-14: ya lo cubren Mercado Pago, Extracash y otros; custodia regulada.", ""),
}

NIVELES = [
    (29, "1 · Indagar ya", "C6EFCE"),
    (26, "2 · Ahondar después", "E2EFDA"),
    (22, "3 · En reserva", "F2F2F2"),
    (0, "4 · Baja prioridad o descartada", "F8CBAD"),
]
ESPECIAL = {"F36": ("Método (no es una idea)", "F2F2F2"), "L15": ("4 · Baja prioridad o descartada", "F8CBAD")}


def nivel(cod, total):
    if cod in ESPECIAL:
        return ESPECIAL[cod]
    for minimo, nombre, color in NIVELES:
        if total >= minimo:
            return nombre, color


def ranking():
    filas = []
    for cod, (blq, nom, ter, *rest) in I.items():
        sc, porque, averiguar = rest[:7], rest[7], rest[8]
        total = sum(sc)
        niv, color = nivel(cod, total)
        filas.append(dict(codigo=cod, bloque=blq, nombre=nom, territorio=TERR[ter], puntajes=dict(zip(CRIT, sc)),
                          total=total, nivel=niv, color=color, por_que=porque, averiguar=averiguar))
    # Orden: total, después gusto, después ventaja; los especiales (método) al final de su nivel
    filas.sort(key=lambda f: (f["codigo"] in ESPECIAL and f["codigo"] != "L15", -f["total"], -f["puntajes"]["G"],
                              -f["puntajes"]["V"], f["codigo"]))
    for i, f in enumerate(filas, start=1):
        f["puesto"] = i
    return filas


def marcas_ideas(wb):
    return sum(1 for row in wb["Ideas"].iter_rows(min_row=2)
               if any(c.fill.fill_type and c.fill.fgColor.rgb in ("FFFFFF00", "FF00B0F0") for c in row))


def bloques(ws):
    """Devuelve [(fila_header, primera, ultima, ultima_col)] de cada bloque de Fase 2 (header = fila con 'Código')."""
    out = []
    r = 1
    while r <= ws.max_row:
        if ws.cell(r, 1).value == "Código":
            ncol = max(c for c in range(1, ws.max_column + 1) if ws.cell(r, c).value not in (None, ""))
            primera = r + 1
            ultima = primera
            while ultima + 1 <= ws.max_row and ws.cell(ultima + 1, 1).value not in (None, ""):
                ultima += 1
            out.append((r, primera, ultima, ncol))
            r = ultima + 1
        else:
            r += 1
    return out


def main():
    try:
        open(XLSX, "r+b").close()
    except OSError:
        sys.exit("TODAS-LAS-IDEAS.xlsx está abierto en Excel: cerralo y volvé a correr.")
    shutil.copy2(XLSX, BACKUP)
    filas = ranking()
    puesto = {f["codigo"]: f["puesto"] for f in filas}
    OUT_JSON.write_text(json.dumps({"_nota": "Orden de Claude de los ganadores de Fase 2 (2026-10-14). Puntajes 1-5 = opinión.",
                                    "criterios": CRIT_NOMBRE, "filas": filas}, ensure_ascii=False, indent=1), encoding="utf-8")

    wb = openpyxl.load_workbook(XLSX)
    antes_marcas = marcas_ideas(wb)
    ws = wb["Fase 2"]
    bl = bloques(ws)
    codigos_fase2 = [ws.cell(r, 1).value for (_, a, b, _) in bl for r in range(a, b + 1)]
    faltan = set(codigos_fase2) ^ set(I)
    if faltan:
        sys.exit(f"Los códigos de Fase 2 y los puntajes no coinciden: {sorted(faltan)}")
    contenido_antes = sorted(tuple(ws.cell(r, c).value for c in range(1, ncol + 1))
                             for (_, a, b, ncol) in bl for r in range(a, b + 1))

    # --- Ordenar filas dentro de cada bloque y agregar la columna "Puesto" ---
    for (h, a, b, ncol) in bl:
        filas_bloque = []
        for r in range(a, b + 1):
            celdas = [(ws.cell(r, c).value, copy(ws.cell(r, c)._style)) for c in range(1, ncol + 1)]
            filas_bloque.append((puesto[ws.cell(r, 1).value], celdas, ws.row_dimensions[r].height))
        filas_bloque.sort(key=lambda t: t[0])
        pc = ncol + 1
        hc = ws.cell(h, pc, "Puesto (orden de Claude)")
        hc._style = copy(ws.cell(h, ncol)._style)
        for i, (p, celdas, alto) in enumerate(filas_bloque):
            r = a + i
            for c, (v, st) in enumerate(celdas, start=1):
                ws.cell(r, c).value = v
                ws.cell(r, c)._style = st
            ws.row_dimensions[r].height = alto
            pcell = ws.cell(r, pc, p)
            pcell._style = copy(celdas[0][1])
            pcell.alignment = Alignment(horizontal="center", vertical="top")
        if (ws.column_dimensions[get_column_letter(pc)].width or 0) < 11:
            ws.column_dimensions[get_column_letter(pc)].width = 11
    c2 = ws.cell(2, 1)
    if "ordenad" not in str(c2.value):
        c2.value = f"{c2.value} Ordenada el 2026-10-14: dentro de cada bloque, de mayor a menor según la hoja 'Orden de Claude' (columna 'Puesto')."

    # --- Hoja "Orden de Claude" ---
    if HOJA in wb.sheetnames:
        del wb[HOJA]
    o = wb.create_sheet(HOJA, 1)
    hdr_fill, hdr_font = PatternFill("solid", fgColor="1F3864"), Font(bold=True, color="FFFFFF")
    thin = Side(style="thin", color="BFBFBF")
    borde = Border(left=thin, right=thin, top=thin, bottom=thin)
    wrap, centro = Alignment(wrap_text=True, vertical="top"), Alignment(horizontal="center", vertical="top", wrap_text=True)
    lineas = [
        ("ORDEN DE CLAUDE — los ganadores de Fase 2, de mayor a menor (2026-10-14)", Font(bold=True, size=15, color="1F3864")),
        ("Pedido de Facu: ordenar con criterio, sin eliminar nada, cuáles pueden funcionar, en cuáles indagar ya y en cuáles ahondar después. "
         "Los puntajes son OPINIÓN de Claude, apoyada en los datos de cada investigación (fuentes en la columna 'Origen' y en research/). "
         "Puntajes guardados en research/datos/2026-10-14-orden-fase2.json; script: research/datos/ordenar_fase2.py.", Font(size=10)),
        ("Criterios (1 a 5 cada uno; total sobre 35): " + " · ".join(f"{k} = {v}" for k, v in CRIT_NOMBRE.items()), Font(size=10)),
        ("Niveles: 1 · Indagar ya (29 o más) · 2 · Ahondar después (26-28) · 3 · En reserva (22-25) · 4 · Baja prioridad o descartada (21 o menos). "
         "Empates: primero tu gusto, después tu ventaja.", Font(size=10)),
    ]
    for i, (t, f) in enumerate(lineas, start=1):
        c = o.cell(i, 1, t)
        c.font, c.alignment = f, Alignment(wrap_text=False, vertical="top")
    cols = [("Puesto", 7), ("Nivel", 18), ("Código", 10), ("Idea o problema", 48), ("Territorio", 22), ("Origen (bloque de Fase 2)", 14),
            ("G · Gusto", 7), ("P · Producto global", 8), ("M · Mercado", 7), ("H · Hueco AR", 7), ("C · Construible", 8),
            ("R · Regulación/riesgo", 9), ("V · Ventaja de Facu", 8), ("Total /35", 8),
            ("Por qué este lugar (opinión)", 60), ("Qué averiguar primero", 50)]
    hr = len(lineas) + 2
    for j, (t, w) in enumerate(cols, start=1):
        c = o.cell(hr, j, t)
        c.fill, c.font, c.alignment, c.border = hdr_fill, hdr_font, centro, borde
        o.column_dimensions[get_column_letter(j)].width = w
    o.row_dimensions[hr].height = 45
    origen = {"A": "A · Ideas propias", "B": "B · Marcadas de las 633", "C": "C · Ganadores de nichos", "D": "D · Ideas nuevas"}
    for f in filas:
        r = o.max_row + 1
        vals = [f["puesto"], f["nivel"], f["codigo"], f["nombre"], f["territorio"], origen[f["bloque"]]] + \
               [f["puntajes"][k] for k in CRIT] + [f["total"], f["por_que"], f["averiguar"]]
        for j, v in enumerate(vals, start=1):
            c = o.cell(r, j, v)
            c.alignment = centro if j in (1, 3, 7, 8, 9, 10, 11, 12, 13, 14) else wrap
            c.border = borde
        o.cell(r, 2).fill = PatternFill("solid", fgColor=f["color"])
        o.cell(r, 14).font = Font(bold=True)
        o.row_dimensions[r].height = 48
    o.freeze_panes = o.cell(hr + 1, 5)
    o.auto_filter.ref = f"A{hr}:{get_column_letter(len(cols))}{o.max_row}"

    cl = wb["Cómo leer"]
    if not any("Orden de Claude" in str(c.value) for row in cl.iter_rows() for c in row):
        cl.cell(cl.max_row + 2, 1, "2026-10-14: hoja 'Orden de Claude' = los ganadores de Fase 2 ordenados de mayor a menor con 7 criterios "
                                   "(opinión de Claude). En 'Fase 2', cada bloque quedó ordenado igual (columna 'Puesto').")

    wb.save(XLSX)

    # --- Verificación ---
    wb2 = openpyxl.load_workbook(XLSX)
    ws2 = wb2["Fase 2"]
    bl2 = bloques(ws2)
    ncols_orig = [ncol for (_, _, _, ncol) in bl]  # sin la columna "Puesto" agregada
    contenido_despues = sorted(tuple(ws2.cell(r, c).value for c in range(1, ncol + 1))
                               for (_, a, b, _), ncol in zip(bl2, ncols_orig) for r in range(a, b + 1))
    ok_contenido = contenido_antes == contenido_despues
    n_orden = wb2[HOJA].max_row - hr
    despues_marcas = marcas_ideas(wb2)
    print(f"Fase 2: {len(codigos_fase2)} filas | contenido intacto: {ok_contenido} | hoja '{HOJA}': {n_orden} filas | "
          f"marcas en 'Ideas': {antes_marcas} -> {despues_marcas}")
    from collections import Counter
    print("por nivel:", dict(Counter(f["nivel"] for f in filas)))
    if not ok_contenido or n_orden != len(I) or despues_marcas != antes_marcas:
        sys.exit(f"ERROR en la verificación: restaurar desde {BACKUP}")


if __name__ == "__main__":
    main()
