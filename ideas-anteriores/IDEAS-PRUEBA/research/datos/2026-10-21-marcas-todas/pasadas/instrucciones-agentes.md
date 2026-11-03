# Instrucciones para investigar las ideas que marcó Facu

## Quién es Facu y qué pidió
Facu tiene 22 años, es argentino y está por recibirse de ingeniero industrial. Quiere una empresa propia, sin jefe. No programa, pero trabaja con Claude y herramientas no-code. Tiene unos USD 1.300 de ahorros. Su papá tiene una empresa de granos (CEMEVA) y Facu ya llevó a producción una app para ella. Le atraen la tecnología del mundo físico, las apps que conectan dos partes y automatizar papeles y procesos, siempre como producto global y no como trabajo a medida. No quiere mostrar la cara en redes. Contexto más completo en `C:\Users\Facuc\AppData\Local\Temp\claude\C--FACU-IDEAS-PRUEBA\e86dcafd-a207-4f61-98cd-f2b55e2d9bfe\scratchpad\insumos\contexto-facu.md`.

Hoy te toca investigar **un lote de ideas que él marcó** en sus Excel, **una por una**, **teniendo en cuenta sus comentarios** (a veces el comentario cambia o agranda la idea). Va a clasificar y filtrar las ideas de a poco y de ahí elegir con qué empezar. No se borra ninguna idea.

## Reglas duras
1. **Nada inventado.** Toda cifra, empresa o dato nuevo lleva URL y fecha de consulta (2026-10-23). Si no lo pudiste confirmar, escribí "no verificado". Separá dato verificado, estimación tuya (marcala "estimación" y explicá el razonamiento) y opinión.
2. **Honestidad antes que simpatía.** Si una idea es floja, decilo y explicá por qué con datos. No endulces.
3. **Respetá el comentario de Facu.** Si propone una variante o un giro, evaluá ESA versión y decí qué cambia respecto de la idea original.
4. **Búsqueda web con presupuesto.** Cargá `WebSearch` y `WebFetch` con ToolSearch ("select:WebSearch,WebFetch"). Cada idea ya trae `contexto_previo` con lo verificado antes: **no repitas esa búsqueda**. Buscá solo lo que falte: la variante que plantea Facu, lo que figura como "no verificado", o si apareció un competidor argentino nuevo. Presupuesto: **hasta 12 búsquedas y 8 lecturas de página en total para todo tu lote**, repartidas donde más sirvan. Mandá varias búsquedas en paralelo en un mismo mensaje. Si WebSearch avisa que se agotó el cupo, **respetá el límite**: no uses otros buscadores, feeds ni atajos, y seguí con lo que ya sabés marcando "no verificado". Nunca intentes resolver un captcha.
5. **Buscá como un argentino**: en español, con "argentina", "app", "plataforma", "startup", y el nombre de la empresa de afuera más "argentina".
6. **Sin repetir ideas ya rechazadas.** Facu no quiere volver a rechazar lo mismo. Si una variante tuya se parece a algo que ya rechazó (el registro está en `C:\FACU\IDEAS-PRUEBA\research\datos\registro-de-ideas.csv`, columna `decision_facu`), no la propongas o marcalo.
7. **Estilo de lo que escribas** (lo va a leer él en un Excel): español rioplatense, oraciones cortas, una idea por oración, sin guiones largos, sin paréntesis de relleno, sin jerga sin explicar. Números en formato argentino (USD 1.500).

## Qué hacer con cada idea
Leé el archivo de tu lote (JSON con una lista de ideas; cada una trae `n`, `origen`, `codigo`, `idea`, `anotaciones_de_facu`, `puntuacion_previa` y `contexto_previo`). Podés leer también, si ayuda, los informes en `C:\FACU\IDEAS-PRUEBA\research\` y `research\fuentes\` (buscá por código con grep; por ejemplo `research/2026-10-15-indagacion-*.md` y `research/2026-10-19-gimnasio-top-a-fondo.md`).

Para cada idea producí un objeto con **exactamente** estas claves:

- `n`: el mismo `n` del lote.
- `opinion`: 3 a 5 oraciones. Qué pensás de verdad. Incluí qué entendiste del comentario de Facu y cómo cambia la idea.
- `hallazgos`: lo que averiguaste hoy, con URL entre corchetes al final de cada dato. Si no hiciste búsqueda nueva, escribí "Sin búsqueda nueva: se usó lo verificado antes".
- `variantes`: lista de 2 o 3 variantes concretas. Una tiene que respetar el comentario de Facu. Otra tiene que ser una vuelta de tuerca distinta (otro cliente, otro cobro, sacar o poner hardware, otro país, modo un solo jugador, etc.).
- `puntuacion`: número de 1 a 10 con un decimal. Es tu opinión final sobre qué tan buena es para ESTE Facu hoy. Considerá: demanda probable, hueco en Argentina (verificado), qué tan construible es sin programar y con poca plata, si es producto global o trabajo a medida, regulación y riesgo, ventaja de Facu (ingeniería industrial, CEMEVA, agro), y la evidencia que hay. Partí de `puntuacion_previa` y corregila si lo nuevo lo justifica. No inflés: un 8 o más es excepcional.
- `por_que_puntuacion`: 1 o 2 oraciones con la razón principal del número.
- `tema`: uno exacto de estos: "Stock y depósito", "Logística y reparto", "Cámaras, sensores y hardware", "Software e IA para PyMEs", "Marketplace o intermediario", "Educación y trabajo", "Salud y cuidado", "Comida y alimentos", "Hogar, obra y barrio", "Agro e industria", "Trámites, seguros y finanzas", "Video y contenido con IA", "Otro".
- `tipo`: uno exacto de: "Producto web o app", "Marketplace o intermediario", "Hardware más software", "Servicio con personas", "Contenido o infoproducto", "Datos o información".
- `etapa`: uno exacto de: "Empezar ya", "Probar barato", "Reserva para etapa 2", "Combinar con otra", "Pausar por ahora".
- `dificultad`: "Baja", "Media" o "Alta" (para Facu, sin programar).
- `plata_para_probar`: texto corto con una estimación en USD del primer experimento (por ejemplo "USD 50 a 150"), marcada como estimación.
- `primer_paso`: una oración con el primer paso concreto y barato, de menos de dos semanas.
- `riesgo_principal`: una oración.
- `agrupar_con`: lista de `n` de otras ideas de tu lote (o códigos que conozcas) que son la misma familia o conviene combinar. Lista vacía si no hay.

## Entrega
Escribí un único archivo JSON válido (UTF-8, una lista con un objeto por idea, **todas** las ideas del lote, sin omitir ninguna) en la ruta de salida que te indique tu encargo. Después de escribirlo, verificalo con `python -c "import json;print(len(json.load(open(r'RUTA',encoding='utf-8'))))"`. Tu respuesta final tiene que ser una sola línea: "OK" más la cantidad de ideas y cuántas búsquedas hiciste. No devuelvas el contenido por chat.
