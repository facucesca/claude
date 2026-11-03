# Formato de extracción de ideas (común a todos los agentes) — 2026-10-02

Objetivo: el usuario (argentino, NO programa, formación en ingeniería industrial, usa Claude a diario, capital < USD 500) va a LEER TODAS las ideas del proyecto en un Excel y marcar en amarillo las que le gustan. Cada fila tiene que entenderse SOLA, sin haber leído los informes, en español rioplatense claro, sin jerga sin explicar (si usás un término técnico, explicalo entre paréntesis: ej. "SOP (manual de procedimientos)", "white-label (marca blanca: vos hacés el trabajo, otro lo vende con su marca)").

Salida: un archivo JSON (UTF-8, válido, un ARRAY de objetos) con UNA entrada por idea. No omitas ninguna idea de tus informes. Verificá al final con: python -c "import json;d=json.load(open(r'RUTA',encoding='utf-8'));print(len(d))"

Campos de cada objeto (todos obligatorios; usá "sin dato" si de verdad no hay info):
- "id": código de la idea tal como aparece en la síntesis (ej. "A8", "H11", "M3"). Para el primer estudio usá los códigos que se indiquen en tu encargo.
- "nombre": nombre corto y claro (máx. ~70 caracteres).
- "estudio": de qué investigación sale (ej. "2026-10-01 · 230 ideas · Frente A Cursos").
- "categoria": rubro, UNO de: "Educación y cursos", "Automatización y agencia IA", "Ingeniería industrial y operaciones", "Software y herramientas", "Contenido y marketing", "E-commerce y marketplaces", "IA emergente y verticales", "Freelance y trabajo remoto", "Servicios a comercios locales", "Servicios a personas", "Comercio y reventa", "Video y producción audiovisual", "Foto y diseño", "Audio y podcast", "Ventas y prospección", "Datos y scraping", "Trading y finanzas", "Hardware y dispositivos".
- "tipo_negocio": UNO de: "Servicio", "Servicio productizado (precio y alcance fijos)", "Abono / suscripción de servicio", "Producto digital", "Infoproducto / curso", "Software / SaaS", "Contenido / medios", "Comercio / reventa", "Producto físico", "Afiliación / comisión", "Trabajo por hora / empleo", "Híbrido (servicio + producto)".
- "modalidad": UNO de "Activo", "Semi-pasivo", "Pasivo" (según el informe).
- "cliente": a quién se le vende, concreto (ej. "PyMEs con depósito y muchos productos (distribuidoras, ferreterías)"; "Personas: hijos que regalan el Día de la Madre").
- "mercado": "Argentina", "Exterior" o "Argentina + exterior".
- "explicacion": 3-5 frases (60-120 palabras): qué es exactamente, qué problema le resuelve al cliente, por qué ahora (señal de auge con dato y fecha si el informe la tiene), y lo más importante a favor y en contra.
- "como_se_hace": pasos numerados concretos (3-6 pasos, 60-130 palabras): cómo se consigue el cliente, qué se entrega, qué herramientas, qué hace Claude y qué hace el usuario.
- "tiempo_primer_dolar": texto (ej. "2-4 días (seña por Mercado Pago)", "2-3 meses").
- "dias_primer_dolar": número entero aproximado (punto medio del rango, en días) para poder ordenar. Si es >1 año o desconocido usá 999.
- "precio": ticket típico (ej. "USD 300-450/mes", "ARS 40.000 por pieza (~USD 26)").
- "capital_inicial": texto corto (ej. "USD 0", "USD 50-100 en herramientas").
- "horas_semana": texto corto (ej. "5-10 h/sem en régimen").
- "pct_argentina": número entero 0-100 = ESTIMACIÓN del % del público objetivo EN ARGENTINA que hoy necesita esto Y podría/estaría dispuesto a pagarlo, teniendo en cuenta cultura y economía argentina 2026: sensibilidad al precio y desconfianza a pagar intangibles (consultoría, "asesoría"), informalidad alta, preferencia por WhatsApp y trato cara a cara, Mercado Libre/Mercado Pago dominantes, inflación que obliga a actualizar precios seguido, industria en contracción en 2026 (índice UIA 36,5 ene-2026, capacidad usada ~58%), comercio con cierres, dificultad para pagar suscripciones en USD, cultura de "lo hago yo/lo hace un sobrino", alta adopción de celular. Si la idea es para clientes del exterior, igual estimá el % para Argentina (puede ser muy bajo) y aclaralo en la base.
- "pct_argentina_base": 1-2 frases: sobre qué universo se calcula el % (ej. "comercios minoristas con local") y el razonamiento cultural/económico. Siempre decir que es estimación propia.
- "cobro_desde_ar": cómo se cobra desde Argentina (ej. "Mercado Pago / transferencia", "Payoneer vía Upwork (retiene 5 días)").
- "riesgos": 1-2 frases con los riesgos/trampas principales.
- "score": número del informe (escala 1-10). Si la idea no tiene score, null.
- "estado": UNO de "Recomendada / Top", "Evaluada", "Descartada / trampa", "En cartera (proyecto)". Usá "Recomendada / Top" si está en el Top 5/Top 15 de su informe o síntesis; "Descartada / trampa" si el informe la descarta o score ≤ 2,5.
- "fuente": ruta relativa del informe crudo (ej. "research/fuentes/2026-10-01-ideas-cursos-educacion.md").

Reglas: no inventes datos de mercado que no estén en los informes (podés resumir y reformular). El % para Argentina sí es estimación tuya razonada. Escribí en español; números con formato argentino en texto (ej. "USD 1.500"). Fechas absolutas.
