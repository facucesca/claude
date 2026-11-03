# Agrega a la hoja "Fase 2" de TODAS-LAS-IDEAS.xlsx (el Excel de ganadores) dos bloques nuevos, sin tocar los anteriores:
#   C. Ganadores de NICHOS-Y-PROBLEMAS.xlsx (lo que Facu marcó el 2026-10-14)
#   D. Ideas nuevas de Facu escritas al fondo de ese Excel (L11-L13)
# Hace respaldo antes de escribir y verifica que las 33 marcas de la hoja "Ideas" y los bloques A y B queden intactos.
# Uso: python research/datos/add_fase2_nichos.py
import json
import shutil
import sys
from copy import copy
from pathlib import Path

import openpyxl

ROOT = Path(__file__).resolve().parents[2]
XLSX = ROOT / "TODAS-LAS-IDEAS.xlsx"
BACKUP = ROOT / "research" / "datos" / "archivo" / "2026-10-14-TODAS-LAS-IDEAS-respaldo.xlsx"
MARCAS = ROOT / "research" / "datos" / "2026-10-14-marcas-facu-nichos.json"
NICHOS = ROOT / "research" / "datos" / "2026-10-13-nichos"

TERRITORIO = {
    "COM-2-4": "A · Ojos", "COM-4-4": "A · Ojos", "COM-3-5": "A · Ojos", "ALI-4-4": "A · Ojos", "CON-2-3": "A · Ojos",
    "SER-4-4": "B · Presencia", "EDU-1-4": "B · Presencia", "EDU-1-5": "B · Presencia", "EDU-2-1": "B · Presencia",
    "AGR-4-2": "B · Presencia", "AGR-4-4": "B · Presencia",
    "EDU-5-3": "C · Conectar", "SAL-4-2": "C · Conectar", "SAL-5-2": "C · Conectar", "AUT-1-2": "C · Conectar",
    "ALI-2-2": "C · Conectar", "IND-4-4": "C · Conectar",
    "LOG-1-4": "D · Procesos y papeles", "LOG-3-4": "D · Procesos y papeles", "COM-2-3": "D · Procesos y papeles",
    "ALI-2-4": "D · Procesos y papeles", "ALI-2-5": "D · Procesos y papeles", "ALI-3-2": "D · Procesos y papeles",
    "EDU-3-2": "D · Procesos y papeles", "SER-4-5": "Otro", "EDU-3-1": "Otro",
}

# Qué hay en Argentina (resumen de las búsquedas 2026-10-13/14) y comentario de Claude (opinión)
AR_Y_COMENTARIO = {
    "SAL-4-2": ("Cuidarlos (gestiona un cuidador que ya tenés, no lo busca), agencias y avisos sueltos. No se encontró una app de pedido de enfermeros por hora.",
                "Hay hueco de intermediario. Riesgos: matrículas, responsabilidad médica e informalidad laboral."),
    "SAL-5-2": ("Mercado Libre Negocios (B2B general, 2,6 millones de productos según la empresa), Markley, Compre Ahora.",
                "Un B2B general es pelear contra Mercado Libre. Solo tiene sentido en un rubro puntual (como Vetcove en veterinarias)."),
    "ALI-2-2": ("Cheaf (más de 700 comercios en Argentina) y Buen Provecho.", "Bajo; Facu ya dudaba."),
    "ALI-2-4": ("ANMAT tiene una calculadora oficial y gratis de sellos (Disposición 2673/2022). Hay un proyecto para derogar la Ley 27.642 (no se confirmó si se aprobó).",
                "Como herramienta para cumplir la ley, débil. La pregunta de Facu ('¿cómo sé qué tan sano es?') es otro producto: transparencia para el que compra."),
    "ALI-2-5": ("Presencia baja según la búsqueda del 2026-10-13.",
                "Se agrupa con ALI-2-4 y ALI-3-2: orden sanitario para productores chicos de alimentos. La bromatología es municipal y el control es desparejo."),
    "ALI-3-2": ("Presencia baja según la búsqueda del 2026-10-13.", "Mismo grupo que ALI-2-4 y ALI-2-5."),
    "ALI-4-4": ("Presencia baja según la búsqueda del 2026-10-13.",
                "Es lo que hacen Clarifresh e Intello Labs. Necesita miles de fotos etiquetadas; paga el empacador o exportador, no el verdulero."),
    "LOG-1-4": ("No se encontró una herramienta local (2026-10-13).",
                "La mejor puntuada del Excel y la más parecida a CEMEVA. Facu: 'medio flojo y complicado'."),
    "LOG-3-4": ("No encontrada en la búsqueda del 2026-10-13.", "Usa lo de Sporting (depósito). Sin nota de Facu."),
    "COM-2-3": ("Treinta opera en Argentina (presencia media).", "Sin nota de Facu."),
    "COM-2-4": ("No se encontró un jugador local enfocado en robo hormiga. Veesion (Francia) opera en Iberoamérica con las cámaras existentes; Sumato ID (Argentina) hace analítica de clientes con cámaras.",
                "Software sobre las cámaras que el local ya tiene: une la tecnología física que le gusta a Facu con lo que ya sabe construir."),
    "COM-3-5": ("No encontrada en la búsqueda del 2026-10-13.",
                "La foto sobre una regla (idea de Facu) es muy buena. Empezar solo con software y dejar el pick-to-light para después."),
    "COM-4-4": ("Sumato ID (Argentina) ya mide aforo y comportamiento con cámaras.", "Menos hueco que el robo hormiga."),
    "CON-2-3": ("Presencia baja según la búsqueda del 2026-10-13.",
                "Hover mide con fotos del celular. El dron suma hardware y permisos (ANAC, a verificar)."),
    "IND-4-4": ("Presencia baja según la búsqueda del 2026-10-13.", "Sin nota. Es más fábrica o e-commerce de packaging que software."),
    "SER-4-4": ("Relojes de fichaje con tarjeta o huella ya se venden en Argentina (GeoVictoria); hay software gratis (Jibble).",
                "RFID en empresas: común → descartable. En colegios e instituciones no se vio: queda pendiente (decisión de Facu, 2026-10-14). Lo que puede tener hueco: validar certificados médicos con IA."),
    "SER-4-5": ("HireRight compró Inquiro Vitae (con sede en Argentina); también Referencias Laborales.",
                "Ya existe. Necesita consentimiento del candidato (Ley 25.326, a verificar)."),
    "EDU-1-4": ("No se encontró en Argentina para jardines o colegios. Caso cercano: Efesur, pulseras RFID en viajes de egresados (Bariloche).",
                "Lo más original de las notas. Detectar al pasar por la puerta exige etiquetas de lectura a distancia (UHF). Riesgos: datos de menores y responsabilidad si falla. Hablar con directoras antes de construir."),
    "EDU-1-5": ("No encontrada en la búsqueda del 2026-10-13.", "Casi sin hardware: el GPS del celular del chofer y una app para los padres."),
    "EDU-2-1": ("Presencia baja según la búsqueda del 2026-10-13.",
                "Fila sin color pero con nota de Facu: su variante de RFID para gimnasios (más un sensor para detectar colados). Creo que existe como 'antipassback' en control de acceso profesional: no verificado."),
    "EDU-3-1": ("Presencia baja; muchas universidades usan SIU-Guaraní.", "Facu duda; coincido: descartar por ahora."),
    "EDU-3-2": ("No encontrada en la búsqueda del 2026-10-13.", "Existe afuera (DegreeSight, TES), no acá. Venderle a universidades es lento."),
    "EDU-5-3": ("Superprof (marketplace que cobra suscripción para contactar profesores; muchas quejas públicas). No se encontró una app local de agenda + cobro anticipado.",
                "Facu la amplía a un 'Instagram de profesores particulares' (ver su nota). Ojo, a verificar: retener la plata hasta que termine la clase es custodiar fondos de terceros, que en Argentina está regulado (ver la ficha de escrow A1, BCRA Com. A 6859). Habría que resolverlo con un procesador de pagos habilitado."),
    "AUT-1-2": ("Autominuto (presupuestos por mail) e Inforepuestos (directorio). No se encontró stock en vivo.",
                "El desafío es conseguir el stock de cada casa de repuestos (cada una usa su sistema)."),
    "AGR-4-2": ("Halter tiene sitio para Argentina y Uruguay; según la 2.ª pasada, todavía no vende acá.",
                "Facu llegó solo a la solución de Halter y Nofence. Hardware pesado: no para la etapa 1."),
    "AGR-4-4": ("Presencia baja según la búsqueda del 2026-10-13.", "Facu: 'tal vez'. Hardware de campo (balanza automática)."),
}

NOTA_EXTRA = {
    "EDU-5-3": ("Ampliación de Facu en el chat (2026-10-14): que nadie se clave con clases (ni alumnos ni profesores); "
                "la app retiene el pago hasta que todos dan por concluida y puntuada la clase; comentarios, reseñas, seguridad, "
                "aprendizaje, puntuación, bonos; se puede sumar publicidad y suscripciones. 'Que sea el Instagram de profesores "
                "particulares'. Le gusta como rubro poco regulado para entrar como intermediario."),
    "SER-4-4": "Facu (chat, 2026-10-14): si el RFID ya está muy usado se descarta, pero no lo ve en colegios e instituciones; decidir más adelante.",
    "EDU-1-4": "Facu (chat, 2026-10-14): el RFID no lo ve en colegios e instituciones; decidir más adelante.",
}

IDEAS_NUEVAS = [
    ("L11", "Plataforma de aprendizaje confiable: hoy la información está muy dispersa, mucha es mala o vaga, hay mucho vendedor de curso barato; una plataforma confiable y que cumpla.",
     "Nueva", "Afuera: Class Central (reseñas propias + comisión cuando alguien se anota a un curso).",
     "La confianza tarda años en construirse y las comisiones en Argentina son chicas. Floja para la etapa 1; mejor como proyecto de largo plazo."),
    ("L12", "Implementar en Argentina tecnología de cámaras de seguridad con IA.",
     "No es nueva: une L10 + COM-2-4 (robos hormiga) + COM-4-4 (conteo de gente)",
     "Veesion (Francia, opera en Iberoamérica), Sumato ID (Argentina, analítica con cámaras), KSI Vision (Uruguay), Batech (México, robo hormiga), Irisity + Intel (seguridad pública).",
     "Es el territorio A ('Ojos'). No se encontró a nadie local enfocado en robo hormiga para autoservicios chicos (búsqueda limitada)."),
    ("L13", "RFID para otras cosas o con stickers lindos, hacer algo distinto.",
     "Nueva", "—",
     "Es una tecnología buscando un problema. Se une a las filas con RFID que Facu marcó (SER-4-4, EDU-1-4, EDU-2-1): territorio B ('Presencia')."),
    ("L14", "Stock muy variado de piezas chicas en mercerías, bulonerías, ferreterías y multimarcas: hay sistemas para ordenar, "
            "pero no uno definitivo ni dominante. Entrar con una buena idea, muy buen desarrollo, muy buen orden, adaptable a "
            "cualquier comercio, que también evite robos y controle todo. Pensar cómo sería la tecnología: ¿por peso? ¿cómo? "
            "(mensaje de Facu en el chat, 2026-10-14)",
     "Parecida: une COM-3-5 (pieza por foto, que Facu marcó), COM-3-3 (conteo de miles de ítems chicos; repetía K14), "
     "X1/X1d (Orden Operativo, pick-to-light), L9 (diagnóstico de stock) y L10 (stock con cámara). Lo nuevo: el foco en "
     "comercios de piezas chicas y el control por peso y contra robos",
     "Sin búsqueda propia todavía. Datos de filas vecinas: afuera CountThings y Scandit (contar con el celular), nyris y "
     "Partium (identificar piezas por foto); en Argentina, Fidel (sistema de gestión para casas de repuestos).",
     "Es el interés más constante de Facu desde septiembre (Orden Operativo, Sporting, pick-to-light, L9, L10, COM-3-5) y une "
     "ingeniería industrial con tecnología física. Tecnologías a evaluar más adelante (ideas sin verificar): balanzas "
     "cuentapiezas (contar por peso unitario); estantes o cajones con sensores de peso que avisan faltantes y retiros; "
     "identificar por foto (pieza sobre una regla); código en cada cajón + pick-to-light; cámaras contra robo. Ojo: el RFID "
     "suele andar mal con piezas metálicas chicas (a verificar)."),
    ("L15", "Plataforma para intercambiar efectivo por transferencia: puntos donde una persona deja efectivo y recibe la "
            "transferencia (o al revés); la plata pasa por una cuenta de la app que libera cuando se completa el intercambio. "
            "Facu: 'medio rebuscado, no creo que funcione, pero se me ocurrió' (chat, 2026-10-14)",
     "Nueva, parecida a A1 (escrow: la app custodia la plata hasta completar la operación)",
     "Ya existe a gran escala: Mercado Pago permite ingresar efectivo con un código en Rapipago, Pago Fácil y Cobro "
     "Express (comisión 1,5-3%) y sacar efectivo con QR en comercios (Carrefour, Coto, Día) y en Rapipago con DNI; Visa "
     "Extracash tiene más de 2.500 puntos (Coto, Carrefour, Farmacity, YPF); también Mastercard Cash Plus y Payway. "
     "Ahí el comercio ya funciona como 'punto de intercambio': cambia su efectivo por tu dinero digital.",
     "Opinión: para descartar. La necesidad ya está cubierta por redes con miles de puntos. Y lo propio de la idea es lo "
     "más difícil: custodiar plata de terceros (regulado, BCRA Com. A 6859 según la ficha A1), manejar efectivo "
     "(prevención de lavado ante la UIF, a verificar) y el riesgo físico de robo o billetes falsos en los puntos."),
]


def snapshot(ws, last_row):
    return [[ws.cell(r, c).value for c in range(1, ws.max_column + 1)] for r in range(1, last_row + 1)]


def marcas_ideas(wb):
    n = 0
    for row in wb["Ideas"].iter_rows(min_row=2):
        if any(c.fill.fill_type and c.fill.fgColor.rgb in ("FFFFFF00", "FF00B0F0") for c in row):
            n += 1
    return n


def copy_style(src, dst):
    dst.font, dst.fill, dst.border = copy(src.font), copy(src.fill), copy(src.border)
    dst.alignment, dst.number_format = copy(src.alignment), src.number_format


def main():
    try:
        open(XLSX, "r+b").close()
    except OSError:
        sys.exit("TODAS-LAS-IDEAS.xlsx está abierto en Excel: cerralo y volvé a correr.")
    BACKUP.parent.mkdir(parents=True, exist_ok=True)
    shutil.copy2(XLSX, BACKUP)

    wb = openpyxl.load_workbook(XLSX)
    ws = wb["Fase 2"]
    if any("C. Ganadores de NICHOS" in str(ws.cell(r, 1).value) for r in range(1, ws.max_row + 1)):
        sys.exit("El bloque C ya existe: no se agrega dos veces.")
    antes_marcas = marcas_ideas(wb)
    ultima = ws.max_row
    antes = snapshot(ws, ultima)

    titulo, intro, header, dato = ws.cell(19, 1), ws.cell(20, 1), ws.cell(21, 1), ws.cell(22, 2)
    h_alto = ws.row_dimensions[21].height

    marcas = json.loads(MARCAS.read_text(encoding="utf-8"))["marcas"]
    filas = {}
    for f in sorted(NICHOS.glob("*.json")):
        for r in json.loads(f.read_text(encoding="utf-8")):
            filas[r["id"]] = r

    def bloque(fila, tit, txt, cols, datos):
        ws.cell(fila, 1, tit); copy_style(titulo, ws.cell(fila, 1))
        ws.cell(fila + 1, 1, txt); copy_style(intro, ws.cell(fila + 1, 1))
        for i, h in enumerate(cols, start=1):
            c = ws.cell(fila + 2, i, h); copy_style(header, c)
        if h_alto:
            ws.row_dimensions[fila + 2].height = h_alto
        r = fila + 3
        for d in datos:
            for i, v in enumerate(d, start=1):
                c = ws.cell(r, i, v); copy_style(dato, c)
            ws.row_dimensions[r].height = 120
            r += 1
        return r

    cols_c = ["Código", "Problema", "Nota de Facu", "Total /25 (investigadores)", "Hueco en AR (1-5)", "Marca de Facu",
              "Territorio (opinión de Claude)", "Nicho", "Especialidad", "¿Es nueva? (Regla N.º 2)",
              "Solución 1 (afuera)", "Solución 2 (afuera)", "Qué hay en Argentina (búsquedas 2026-10-13/14)",
              "Comentario de Claude (opinión, 2026-10-14)", "Estado", "Informe fuente", "Mis notas"]
    orden = {"Celeste": 0, "Amarillo": 1, "Sin color (con nota)": 2}
    datos_c = []
    for m in marcas:
        marca = {"amarillo": "Amarillo", "celeste": "Celeste"}.get(m["color"], "Sin color (con nota)")
        nota = m.get("nota_facu") or ""
        if m["id"] in NOTA_EXTRA:
            nota = f"{nota}\n\n{NOTA_EXTRA[m['id']]}".strip()
        r = filas[m["id"]]
        ar, com = AR_Y_COMENTARIO[m["id"]]
        datos_c.append((orden[marca], m["id"], [
            m["id"], m["problema"], nota, m["total"], m["hueco"], marca, TERRITORIO[m["id"]],
            r.get("nicho"), r.get("especialidad"), m["es_nueva"],
            f"{r['solucion_1']['nombre']}: {r['solucion_1'].get('que_hace', '')}",
            f"{r['solucion_2']['nombre']}: {r['solucion_2'].get('que_hace', '')}",
            ar, com, "En embudo (sin filtrar)",
            "NICHOS-Y-PROBLEMAS.xlsx + research/2026-10-14-marcas-de-facu-nichos.md", ""]))
    datos_c = [d for _, _, d in sorted(datos_c, key=lambda t: (t[0], t[1]))]

    fila_c = ultima + 3
    fin_c = bloque(fila_c, f"C. Ganadores de NICHOS-Y-PROBLEMAS (2026-10-14): {len(datos_c)}",
                   "Lo que Facu marcó en NICHOS-Y-PROBLEMAS.xlsx (celeste = le llamó más la atención; amarillo = le gustó; "
                   "una fila sin color con nota). Puntajes = opinión de los investigadores; 'Qué hay en Argentina' sale de búsquedas rápidas.",
                   cols_c, datos_c)

    cols_d = ["Código", "Idea (palabras de Facu)", "¿Es nueva? (Regla N.º 2)", "Qué existe", "Comentario de Claude (opinión)",
              "Estado", "Informe fuente", "Mis notas"]
    estado_d = {"L15": "Descartada (Facu, 2026-10-14)"}
    datos_d = [[c, idea, nueva, existe, com, estado_d.get(c, "En embudo (sin filtrar)"),
                "research/2026-10-14-marcas-de-facu-nichos.md", ""]
               for c, idea, nueva, existe, com in IDEAS_NUEVAS]
    fila_d = fin_c + 2
    fin_d = bloque(fila_d, f"D. Ideas nuevas de Facu (2026-10-14): {len(datos_d)}",
                   "Escritas por Facu al fondo de NICHOS-Y-PROBLEMAS.xlsx (L11-L13) o en el chat (L14-L15). Cruzadas contra el registro de ideas (Regla N.º 2).",
                   cols_d, datos_d)

    c2 = ws.cell(2, 1)
    if "2026-10-14" not in str(c2.value):
        c2.value = f"{c2.value} 2026-10-14: se agregaron los bloques C (ganadores de NICHOS-Y-PROBLEMAS) y D (ideas nuevas de Facu)."

    wb.save(XLSX)

    wb2 = openpyxl.load_workbook(XLSX)
    ws2 = wb2["Fase 2"]
    despues = snapshot(ws2, ultima)
    cambios = [(r + 1, c + 1) for r in range(len(antes)) for c in range(len(antes[r]))
               if antes[r][c] != despues[r][c] and (r + 1, c + 1) != (2, 1)]
    despues_marcas = marcas_ideas(wb2)
    total = 10 + 33 + len(datos_c) + len(datos_d)
    print(f"bloque C: filas {fila_c + 3}-{fin_c - 1} ({len(datos_c)}) | bloque D: filas {fila_d + 3}-{fin_d - 1} ({len(datos_d)})")
    print(f"celdas cambiadas en bloques A y B: {len(cambios)} | marcas en 'Ideas': {antes_marcas} -> {despues_marcas}")
    print(f"TOTAL en Fase 2: A 10 + B 33 + C {len(datos_c)} + D {len(datos_d)} = {total}")
    if cambios or despues_marcas != antes_marcas:
        sys.exit(f"ERROR: algo cambió fuera de lo previsto. Restaurar desde {BACKUP}")


if __name__ == "__main__":
    main()
