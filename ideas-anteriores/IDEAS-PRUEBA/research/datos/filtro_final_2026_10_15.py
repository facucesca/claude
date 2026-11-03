# Filtro final del 2026-10-15 en TODAS-LAS-IDEAS.xlsx (pedido de Facu: "primeras" y "pendientes").
#   1. Revierte los cambios accidentales de la hoja "Ideas" (hojas agrupadas en Excel), solo si siguen igual.
#   2. "Orden de Claude": título para la columna de comentarios de Facu y columna nueva "Filtro final (2026-10-15)".
#   3. Hoja nueva "Primeras y pendientes" con el resultado de la indagación (research/2026-10-15-indagacion-ganadores.md).
# Hace respaldo antes y verifica después. Uso: python research/datos/filtro_final_2026_10_15.py
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
ARCH = ROOT / "research" / "datos" / "archivo"
BACKUP = ARCH / "2026-10-15-TODAS-LAS-IDEAS-antes-del-filtro-final.xlsx"
ORIGINAL_IDEAS = ARCH / "2026-10-14-TODAS-LAS-IDEAS-antes-de-ordenar.xlsx"  # hoja "Ideas" tal como estaba
COMENTARIOS = ROOT / "research" / "datos" / "2026-10-15-comentarios-facu-orden.json"
HOJA = "Primeras y pendientes"

VERDE, GRIS, SALMON = "C6EFCE", "EDEDED", "F8CBAD"
RESULTADO = {
    "COM-3-5": ("PRIMERA 1 · idea integral 'Orden de stock para piezas chicas' (M2: buscador por foto y por nombre)", VERDE),
    "L9 + L5": ("PRIMERA 1 · idea integral (M0: diagnóstico de stock gratis, la puerta de entrada)", VERDE),
    "L14": ("PRIMERA 1 · idea integral (M1: catálogo vivo con ubicaciones)", VERDE),
    "C34": ("PRIMERA 1 · apoyo: calculadoras como material para atraer clientes, no como negocio", VERDE),
    "EDU-5-3": ("PRIMERA 2 · candidata a principal: 'Profes de finales con pago protegido'", VERDE),
    "I29": ("PRIMERA 3 · experimento de caja en paralelo (2026-11-02 a 2026-12-24)", VERDE),
    "K11": ("PENDIENTE · módulo M5 de la idea integral (vencimientos y FIFO)", GRIS),
    "X1d": ("PENDIENTE · módulo M4 de la idea integral (pick-to-light)", GRIS),
    "C14": ("PENDIENTE · módulo futuro de la idea integral (riesgo laboral e imágenes)", GRIS),
    "LOG-3-4": ("PENDIENTE · módulo futuro de la idea integral (riesgo laboral e imágenes)", GRIS),
    "ALI-4-4": ("PENDIENTE con fecha · revisar el 2026-12-01 para la cosecha de enero a abril de 2027", GRIS),
    "F17": ("PENDIENTE · entrevistas opcionales del 2026-11-02 al 11-20", GRIS),
    "SER-4-4": ("PENDIENTE · riesgo legal alto (datos de salud)", GRIS),
    "T19": ("PENDIENTE · la mediana de ventas es cero; el motor de plantillas pasa a L8", GRIS),
    "L6": ("PENDIENTE · primero hablarlo con el papá (CEMEVA); experimento chico después del 2026-12-24", GRIS),
    "L11": ("PENDIENTE · semilla para la etapa 2", GRIS),
    "LOG-1-4": ("No pasa ('/' de Facu, a confirmar)", SALMON),
}

# Grupo, idea, códigos, F1..F5, total, investigador, resultado, experimento y fechas, seguir si, cortar si, pérdida máxima, qué la haría subir, informe
FILAS = [
    ("PRIMERA 1 · principal", "Orden de stock para comercios de piezas chicas (idea integral)", "L14 + COM-3-5 + L9/L5 + C34 (+ K11, X1d como módulos)",
     "2", "2-3", "4", "4", "4", "16-17", "PRIMERA (las dos partes)",
     "Del 2026-10-20 al 2026-11-19: 30 ferreterías, bulonerías y casas de repuestos; 15 entrevistas; diagnóstico gratis en 48 h; piloto de 200 piezas de tornillería con buscador por foto y por nombre; prueba a ciegas de 50 piezas; oferta paga",
     "8 o más de 15 con un caso concreto de los últimos 30 días; acierto entre los 3 primeros del 80% o más; 2 o más comercios pagan (plan o anticipo)",
     "Menos de 4 de 15 con casos; ningún pago después de 8 diagnósticos; menos del 60% de acierto tras 2 rondas",
     "USD 300 y unas 80 h", "—",
     "research/fuentes/2026-10-15-indagacion-stock-piezas.md + 2026-10-15-indagacion-ing-industrial-productizada.md"),
    ("PRIMERA 2 · candidata a principal", "Profesores particulares con pago protegido (comisionista)", "EDU-5-3",
     "3", "4", "4", "3", "4", "18", "PRIMERA (acotada)",
     "30 días, a mano y sin app: 'Profes de finales con pago protegido'. Solo alumnos adultos; la plata nunca pasa por Facu (link de Mercado Pago del profe); comisión del 15% o abono fijo, se prueban los dos. Las entrevistas se pueden hacer en noviembre",
     "30 o más clases pagadas; 6 o más profes activos; 50% o más de las segundas clases por el sistema; 70% o más de los profes pagan sin pelear",
     "Menos de 10 clases; menos del 30% de segundas clases por el sistema; más de la mitad de los profes se niega a pagar",
     "USD 250 y 60 h", "—", "research/fuentes/2026-10-15-indagacion-profesores-comisionista.md"),
    ("PRIMERA 3 · experimento en paralelo", "Video personalizado de Papá Noel (caja de temporada)", "I29",
     "2", "3", "5", "3", "4", "17", "PRIMERA (caja de temporada)",
     "Preparación del 2026-11-02 al 11-14 (gate 0 el 11-14 con 5 padres); lanzamiento el 2026-11-15 a ARS 9.900; gate 1 el 11-29; gate 2 el 12-13; cierre de pedidos el 12-22; todo entregado el 12-24; post-mortem y datos borrados antes del 12-31",
     "10 o más pedidos pagados (5 o más de fuera del círculo cercano) y 25 minutos o menos por video, al 2026-11-29",
     "Menos de 3 pedidos, más de 40 minutos por video o cualquier incidente con datos de un chico",
     "USD 160; tope de 10 h por semana", "—", "research/fuentes/2026-10-15-indagacion-aprendizaje-y-papa-noel.md (tema 2)"),
    ("PENDIENTE con fecha", "Calidad de fruta por foto", "ALI-4-4", "3", "4", "3", "4", "4", "18", "PRIMERA (experimento chico)",
     "—", "—", "—", "—", "15 entrevistas a empacadores y prueba 'foto contra inspector'. Revisar el 2026-12-01 para la cosecha de pera y manzana (enero a abril de 2027)",
     "research/fuentes/2026-10-15-indagacion-fruta-por-foto.md"),
    ("PENDIENTE", "IA para estudios contables (declaración anual de personas humanas)", "F17", "3", "3", "4", "3", "4", "17", "PENDIENTE",
     "—", "—", "—", "—", "10 entrevistas del 2026-11-02 al 11-20, empezando por el contador de CEMEVA; si dan 'seguir', sube",
     "research/fuentes/2026-10-15-indagacion-contadores.md"),
    ("PENDIENTE", "Validar certificados médicos con IA", "SER-4-4", "3", "3", "4", "2", "4", "16", "PENDIENTE",
     "—", "—", "—", "—", "12 entrevistas a RR.HH.: 6 o más casos concretos y 3 dispuestos a pagar, con asesoría legal desde el día 1",
     "research/fuentes/2026-10-15-indagacion-certificados-medicos.md"),
    ("PENDIENTE", "Plantillas y edición automatizada", "T19", "2", "4", "4", "4", "2", "16", "PENDIENTE",
     "—", "—", "—", "—", "Sumar el motor de plantillas a L8; o prueba de 30 días a USD 19 por video con USD 150 de anuncios",
     "research/fuentes/2026-10-15-indagacion-plantillas-edicion.md"),
    ("PENDIENTE", "Uber de la logística como comisionista", "L6", "3", "2", "4", "3", "3", "15", "PENDIENTE",
     "—", "—", "—", "—", "OK del papá (posible conflicto con CEMEVA); después, corredor puro sin tocar la plata con fleteros de CEMEVA",
     "research/fuentes/2026-10-15-indagacion-logistica-comisionista.md"),
    ("PENDIENTE", "Plataforma de aprendizaje confiable", "L11", "2", "2", "3", "3", "2", "12", "PENDIENTE",
     "—", "—", "—", "—", "'Semáforo de 30 cursos' en un solo rubro; semilla para la etapa 2",
     "research/fuentes/2026-10-15-indagacion-aprendizaje-y-papa-noel.md (tema 1)"),
    ("PENDIENTE", "Estudio de tiempos por video y productividad en depósito", "C14, LOG-3-4", "—", "—", "—", "—", "—", "(dentro de 17)", "PENDIENTE",
     "—", "—", "—", "—", "Que funcione la Primera 1; resolver el riesgo laboral (arts. 70 a 72 de la Ley de Contrato de Trabajo) y el de las imágenes",
     "research/fuentes/2026-10-15-indagacion-ing-industrial-productizada.md"),
    ("A CONFIRMAR", "Pedidos y cotizaciones de fletes por WhatsApp", "LOG-1-4", "—", "—", "—", "—", "—", "—", "—",
     "—", "—", "—", "—", "Facu escribió '/' sin pintarla: se toma como que no pasa", "—"),
]


def marcas_ideas(wb):
    return sum(1 for row in wb["Ideas"].iter_rows(min_row=2)
               if any(c.fill.fill_type and c.fill.fgColor.rgb in ("FFFFFF00", "FF00B0F0") for c in row))


def main():
    try:
        open(XLSX, "r+b").close()
    except OSError:
        sys.exit("TODAS-LAS-IDEAS.xlsx está abierto en Excel: cerralo y volvé a correr.")
    shutil.copy2(XLSX, BACKUP)
    wb = openpyxl.load_workbook(XLSX)
    orig = openpyxl.load_workbook(ORIGINAL_IDEAS)["Ideas"]
    datos = json.loads(COMENTARIOS.read_text(encoding="utf-8"))

    # 1. Revertir cambios accidentales en "Ideas" (solo si la celda sigue como quedó por accidente)
    ws_i = wb["Ideas"]
    revertidas, distintas = 0, []
    for a in datos["hoja_ideas_cambios_accidentales"]:
        c = ws_i.cell(a["fila"], a["col"])
        if str(c.value) == str(a["quedo"]):
            o = orig.cell(a["fila"], a["col"])
            c.value = o.value
            c._style = copy(o._style)
            revertidas += 1
        else:
            distintas.append((a["fila"], a["col"]))
    # Las filas que solo cambiaron de color (sin texto) se comparan por color
    for a in datos["hoja_ideas_cambios_accidentales"]:
        if (a["fila"], a["col"]) in distintas and str(a["quedo"]) == str(a["valor_original"]):
            c = ws_i.cell(a["fila"], a["col"])
            o = orig.cell(a["fila"], a["col"])
            c._style = copy(o._style)
            distintas.remove((a["fila"], a["col"]))
            revertidas += 1

    # 2. "Orden de Claude": títulos y columna de resultado
    o_ws = wb["Orden de Claude"]
    hr = 6
    assert o_ws.cell(hr, 3).value == "Código", "La hoja 'Orden de Claude' cambió de forma: revisar a mano."
    plantilla = o_ws.cell(hr, 16)
    for col, titulo, ancho in ((17, "Comentario de Facu (2026-10-15)", 60), (18, "Filtro final (2026-10-15)", 45)):
        h = o_ws.cell(hr, col, titulo)
        h._style = copy(plantilla._style)
        o_ws.column_dimensions[get_column_letter(col)].width = ancho
    thin = Side(style="thin", color="BFBFBF")
    borde = Border(left=thin, right=thin, top=thin, bottom=thin)
    marcados = 0
    for r in range(hr + 1, o_ws.max_row + 1):
        cod = o_ws.cell(r, 3).value
        if cod in RESULTADO:
            texto, color = RESULTADO[cod]
            c = o_ws.cell(r, 18, texto)
            c.fill = PatternFill("solid", fgColor=color)
            c.alignment = Alignment(wrap_text=True, vertical="top")
            c.border = borde
            marcados += 1
        nota = o_ws.cell(r, 17)
        nota.alignment = Alignment(wrap_text=True, vertical="top")
        nota.border = borde
    o_ws.auto_filter.ref = f"A{hr}:{get_column_letter(18)}{o_ws.max_row}"

    # 3. Hoja "Primeras y pendientes"
    if HOJA in wb.sheetnames:
        del wb[HOJA]
    p = wb.create_sheet(HOJA, 1)
    lineas = [
        ("PRIMERAS Y PENDIENTES — resultado de la indagación a fondo (2026-10-15)", Font(bold=True, size=15, color="1F3864")),
        ("Facu pasó 15 ideas (amarillo en 'Orden de Claude'). 9 investigadores las indagaron a fondo con el mismo filtro (F1 demanda comprobable en Argentina; "
         "F2 producto automatizable y global; F3 validable en 30 días con menos de USD 300; F4 riesgo legal manejable; F5 encaje con Facu; total /25).", Font(size=10)),
        ("Filtro de más (Claude, opinión): es PRIMERA si tiene 16 o más, el investigador la recomienda, se puede empezar en noviembre o diciembre de 2026, F4 es 3 o más "
         "y entra en la regla de la etapa 1 (un principal y un experimento chico en paralelo).", Font(size=10)),
        ("Ninguna tiene la demanda comprobada en Argentina: las primeras son los PRIMEROS EXPERIMENTOS, con números de corte fijados antes. "
         "Síntesis: research/2026-10-15-indagacion-ganadores.md.", Font(size=10, bold=True)),
    ]
    for i, (t, f) in enumerate(lineas, start=1):
        c = p.cell(i, 1, t)
        c.font = f
    cols = [("Grupo", 20), ("Idea", 34), ("Códigos", 22), ("F1", 5), ("F2", 5), ("F3", 5), ("F4", 5), ("F5", 5), ("Total /25", 8),
            ("Investigador", 16), ("Primer experimento y fechas", 60), ("SEGUIR si", 40), ("CORTAR si", 40), ("Pérdida máxima", 14),
            ("Qué la haría subir / cuándo revisarla", 45), ("Informe", 40)]
    h = len(lineas) + 2
    hdr_fill, hdr_font = PatternFill("solid", fgColor="1F3864"), Font(bold=True, color="FFFFFF")
    centro = Alignment(horizontal="center", vertical="top", wrap_text=True)
    for j, (t, w) in enumerate(cols, start=1):
        c = p.cell(h, j, t)
        c.fill, c.font, c.alignment, c.border = hdr_fill, hdr_font, centro, borde
        p.column_dimensions[get_column_letter(j)].width = w
    p.row_dimensions[h].height = 32
    for fila in FILAS:
        r = p.max_row + 1
        for j, v in enumerate(fila, start=1):
            c = p.cell(r, j, v)
            c.alignment = centro if 4 <= j <= 9 else Alignment(wrap_text=True, vertical="top")
            c.border = borde
        color = VERDE if fila[0].startswith("PRIMERA") else (SALMON if fila[0].startswith("A CONFIRMAR") else GRIS)
        p.cell(r, 1).fill = PatternFill("solid", fgColor=color)
        p.cell(r, 1).font = Font(bold=True)
        p.row_dimensions[r].height = 110 if fila[0].startswith("PRIMERA") else 60
    p.freeze_panes = p.cell(h + 1, 3)

    cl = wb["Cómo leer"]
    if not any(HOJA in str(c.value) for row in cl.iter_rows() for c in row):
        cl.cell(cl.max_row + 2, 1, f"2026-10-15: hoja '{HOJA}' = resultado de la indagación a fondo de las 15 ideas que pasó Facu "
                                   "(3 primeras y el resto pendientes). En 'Orden de Claude', la columna 'Filtro final (2026-10-15)' dice qué pasó con cada una.")

    wb.save(XLSX)

    # Verificación
    wb2 = openpyxl.load_workbook(XLSX)
    m = marcas_ideas(wb2)
    print(f"'Ideas': {revertidas} celdas revertidas, {len(distintas)} no tocadas (cambiaron desde el 2026-10-15) | marcas en 'Ideas': {m}")
    print(f"'Orden de Claude': {marcados} filas con resultado | hoja '{HOJA}': {len(FILAS)} filas | hojas: {wb2.sheetnames}")
    if m != 33:
        print(f"AVISO: las marcas en 'Ideas' no son 33. Revisar. Respaldo en {BACKUP}")


if __name__ == "__main__":
    main()
