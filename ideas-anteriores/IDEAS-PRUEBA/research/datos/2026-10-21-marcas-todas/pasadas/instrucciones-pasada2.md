# Segunda pasada: investigar más a fondo las mejores ideas de Facu

## Contexto
Leé primero `C:\Users\Facuc\AppData\Local\Temp\claude\C--FACU-IDEAS-PRUEBA\e86dcafd-a207-4f61-98cd-f2b55e2d9bfe\scratchpad\marcas\instrucciones-agentes.md`. Ahí está quién es Facu, las reglas duras (nada inventado, honestidad, respetar su comentario, cupo de búsqueda, estilo de escritura) y cómo buscar. **Todo eso rige también acá.**

En la primera pasada otro investigador ya dio una opinión rápida de cada idea. Tu lote trae las 10 que quedaron mejor puntuadas de un tema. Cada idea trae `anotaciones_de_facu`, `puntuacion_actual`, `pasada1` (opinión, hallazgos, variantes, primer paso y riesgo de la primera pasada) y `contexto_previo`. Tu trabajo es **profundizar donde la primera pasada quedó corta** para que Facu pueda decidir con qué empezar. No repitas lo que ya está hecho.

## Presupuesto de búsqueda
Hasta **25 búsquedas y 15 lecturas de página en total para tu lote** (unas 2 búsquedas y 1 lectura por idea, más en las que más lo merezcan). Mandá varias en paralelo en un mismo mensaje. Si WebSearch avisa que se agotó el cupo, respetá el límite: no uses otros buscadores, feeds ni atajos; seguí con lo que sabés y marcá "no verificado". Nunca resuelvas un captcha. Fecha de consulta: 2026-10-23.

## Qué profundizar en cada idea (en este orden de prioridad)
1. **Quién lo intentó en Argentina o Latinoamérica y qué le pasó** (cierres, pivotes, ventas de la empresa, notas de prensa), con fuente.
2. **Competencia argentina de hoy**: nombre, qué hace, si publica precios cuánto cobra, qué deja sin cubrir.
3. **Regulación leída en la fuente** cuando la idea depende de una norma (Boletín Oficial, InfoLEG, organismo). Qué permite y qué prohíbe. "No aplica" si no hay.
4. **Números de unidad**: ticket, comisión o abono, costos por operación. Todo lo que sea estimación va marcado "estimación" con el razonamiento. Si usás tarifas de Mercado Pago u otro medio de cobro, citá la fuente y verificá que sean actuales.
5. **Tamaño del mercado en Argentina** con fuente (INDEC, cámaras, organismos). Si no hay dato, decilo.
6. **La variante de Facu**: si en su comentario propone otra versión, evaluala aparte y decí si es mejor o peor que la original y por qué.

## Qué entregar por idea (claves exactas)
- `n`: el mismo del lote.
- `quien_lo_intento`: texto corto con fuentes entre corchetes. "No encontré a nadie" si buscaste y no apareció, diciendo qué buscaste.
- `competencia`: texto corto con nombres, precios si hay y huecos, con fuentes.
- `regulacion`: texto corto con la norma y la fuente, o "no aplica", o "no verificado".
- `numeros`: texto corto con ticket, costos y margen aproximado por operación, marcando las estimaciones.
- `mercado`: texto corto con el tamaño en Argentina y la fuente, o "sin dato".
- `variante_recomendada`: la versión que vos le recomendarías probar a Facu, en 2 o 3 oraciones. Puede ser la original, la suya o una mezcla.
- `entrevistar_a`: 2 o 3 perfiles concretos y dónde encontrarlos.
- `preguntas_entrevista`: lista de 5 preguntas estilo Mom Test (sobre lo que pasó la última vez, lo que hacen hoy y lo que pagan; nada de "¿usarías...?").
- `experimento`: objeto con `hipotesis` (una oración), `prediccion` (un número concreto que esperás ver), `perdida_maxima` (en USD, menos de 200), `duracion`, `pasos` (lista corta), `sigue_si`, `se_corta_si`.
- `puntuacion_revisada`: de 1 a 10 con un decimal, tu opinión final. Podés subir o bajar respecto de `puntuacion_actual`. Un 8 o más es excepcional. Sé exigente.
- `por_que_revisada`: 1 o 2 oraciones con la razón del cambio o de que se mantenga.
- `veredicto`: una oración que empiece con "Probar ya", "Probar si..." o "No conviene" y diga por qué.
- `fuentes`: lista de todas las URLs usadas.

## Entrega
Escribí un único archivo JSON válido (UTF-8, una lista con un objeto por idea, **todas** las del lote) en la ruta que te indique tu encargo. Verificalo con `python -c "import json;print(len(json.load(open(r'RUTA',encoding='utf-8'))))"`. Tu respuesta final es una sola línea: "OK", la cantidad de ideas y cuántas búsquedas hiciste. No devuelvas el contenido por chat.
