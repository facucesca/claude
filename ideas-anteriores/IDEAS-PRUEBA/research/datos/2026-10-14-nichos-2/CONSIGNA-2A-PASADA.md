# Consigna 2.ª pasada — NICHOS-Y-PROBLEMAS-2 (2026-10-14)

Sos investigador. Español. REGLA N.º 1: nada inventado; "no encontré" no es "no existe".

## Tarea A — presencia en Argentina
Para cada ID que te toca, leé la fila en `C:\FACU\IDEAS-PRUEBA\research\datos\2026-10-14-nichos-2\<archivo del nicho>.json` (problema, detalle, solucion_1, solucion_2) y averiguá si en Argentina ya hay algo que lo resuelva (empresa, app, software local o una de las soluciones extranjeras operando acá).
- **Cuota:** máximo **8 WebSearch** en total. Además podés usar WebFetch a `https://search.brave.com/search?q=...` (funcionó en otra sesión hasta que devolvió 429): si da 429, esperá y probá una vez más; si sigue, dejá de usarlo. DuckDuckGo pide captcha: no lo intentes. No resuelvas captchas.
- Aprovechá cada búsqueda: armá consultas que cubran 2-3 filas parecidas si se puede, y usá WebFetch directo a sitios argentinos obvios (ej. el sitio de la solución extranjera para ver si opera en Argentina, comparasoftware.com.ar, el sitio de una empresa local que ya conozcas — verificándolo).
- Puntaje `hueco_ar`: 5 solo con 2 búsquedas sin resultados; 4 con 1 búsqueda sin resultados; si encontrás competencia local, bajalo según qué tan conocida es (1 = resuelto y conocido). Si no llegaste a buscar una fila, NO la incluyas (sigue "sin buscar").

## Tarea B — verificar soluciones (si te toca)
Para cada solución sin verificar que te toca: abrí su sitio oficial (WebFetch; si WebFetch está limitado, podés descargar la página con Python/curl por Bash). Si existe y hace lo que dice la fila → devolvé el objeto solución completo con `verificado: "sí"`. Si no se puede verificar → reemplazala por otra empresa extranjera que SÍ verifiques (mismo esquema). Si tampoco encontrás reemplazo, no la incluyas.

## Salida
Escribí con Write una LISTA JSON en la ruta que te indico. Un objeto por ID trabajado:
```json
{"id": "BEL-1-3", "presencia_ar": "nula|baja|media|alta", "presencia_ar_detalle": "qué encontraste con URL, o 'no encontré en N búsquedas (2026-10-14): consultas usadas ...'", "hueco_ar": 1-5, "nota": "opcional: corrección", "etiqueta": "2.ª pasada 2026-10-14"}
```
Para la tarea B, en el mismo objeto (o uno propio con solo `id` y `etiqueta`) agregá `"solucion_1": {...}` o `"solucion_2": {...}` con el esquema completo: nombre, pais, url, que_hace, traccion, fuente_traccion, verificado, como_verifique.
Al terminar, respondé ≤60 palabras: cuántas filas buscaste, cuántas quedaron sin buscar, cuántas soluciones verificaste o reemplazaste.
