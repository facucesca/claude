# Análisis a fondo de las ideas de Facu (2026-10-08)

Síntesis de **7 investigaciones en paralelo** sobre las 10 ideas de la libreta de Facu (L1-L10) y su idea del visualizador de merch (A3). Los informes completos, con todas las fuentes y fechas, están en `research/fuentes/2026-10-08-*.md` (lista al final).

**Cómo leer (Regla N.º 1):**
- **DATO** = tiene fuente y fecha (en el informe correspondiente).
- **ESTIMACIÓN** = cálculo con supuestos a la vista.
- **OPINIÓN** = juicio de Claude.
- **No verificado** = no se pudo confirmar.

**Límites honestos:**
- Se hicieron unas 210 búsquedas web y más de 120 lecturas de páginas, hasta que **se agotó el cupo de búsquedas de la sesión**. Cada informe lista lo que quedó sin verificar.
- Los puntajes son opinión fundada en los datos, no una medición. El "promedio" es simple: los 7 criterios no pesan igual. Para Facu pesan más la disposición a pagar y la factibilidad.
- **Ninguna idea tiene todavía evidencia de que alguien en Argentina pague por ella.** Eso solo se averigua hablando con clientes.

**Criterios (1 a 10):** tamaño del problema · disposición a pagar · espacio frente a la competencia · ventaja de Facu · factibilidad con sus recursos · escalabilidad · riesgo (10 = bajo riesgo).

**Correcciones a documentos anteriores, aplicadas hoy:**
- Payoneer Escrow **cerró en 2018**. La ficha del 2026-10-07 decía "no verificado".
- Los "USD 305 del clipper" son un **promedio, no una mediana** (en el plan del clipper y en el estudio del 2026-09-02).
- Los precios de Fiverr para restaurar fotos son **por pedido o paquete**, no claramente por foto (estudio del 2026-10-01).

---

## 1. Tabla resumen

| # | Tu idea | Versión que tiene sentido (OPINIÓN) | Puntaje (promedio simple) | Veredicto corto |
|---|---|---|---|---|
| **L9 + L5** | Calculadora de ingeniería + IA + 1:1 · IA analista de negocios | **"Diagnóstico de stock en 5 minutos"**: subís tu Excel y recibís ABC, plata parada, quiebres y punto de pedido explicados; puerta a la consultoría. L5 entra como módulo de "qué productos te dejan plata" | **L9: 6,0** · L5 sola: 3,0 | **El mejor vehículo de etapa 1.** Barato, rápido y con tu ventaja real |
| **L4** | Revivir seres queridos con IA | **"Homenaje"**: restaurar, video homenaje y animación sin voz; piloto B2B con cocherías | Homenaje: **5,6** · "Revivir": 3,9 | "Revivir" no. Homenaje es un servicio chico y real |
| **L8** | Edición automática de video para empresas con videos parecidos | **Video automático por unidad** para inmobiliarias y agencias de usados (fotos + ficha → video) | **5,5** | El mejor "producto" de etapa 1: existe y cobra en EE.UU.; en Argentina no encontré uno local |
| **L10** | Stock con IA y cámara para supermercados | **Auditoría de góndola y faltantes por foto de celular**, que pagan distribuidoras y marcas medianas del canal tradicional | Esta versión: **5,4** · "Amazon Go argentino": 2,0 | **El mejor candidato a startup**, en esta versión |
| **L6** | Uber de la logística empresarial | **Broker manual** en un corredor frutihortícola, centrado en el viaje de vuelta vacío, **sin poner capital de trabajo** | **4,7** | "Uber para todo el país": no. Sirve como experimento para aprender el sector |
| **L1** | Intermediario de transacciones | **"Cierre seguro" de autos usados entre particulares**: verificar y coordinar que pago y firma pasen juntos, sin custodiar plata | **4,6** | El escrow genérico es chico. Solo vale dentro de un nicho |
| **A3** | Visualizador de ropa y merch personalizado | **"Cotizador visual" para talleres**: mockup + precio por técnica y cantidad + plazo | **4,5** | El mockup es commodity; el valor está en el número |
| **L7** | App de huella de carbono | Persona: no. **Empresas obligadas** (EUDR, Mendoza): servicio, mejor como módulo de la consultora | Empresas: **4,0** · App para personas: 2,0 | La app de consumo se descarta |
| **L2** | Fotos a precios del súper | — | **3,0** | Ya existe gratis en al menos 5 apps |
| **L3** | Automatización absoluta de clips | — | **3,0** | Lo 100% automático es justo lo que las plataformas castigan desde 2026 |

---

## 2. Lo que se ve mirando todas juntas (OPINIÓN)

1. **La versión grande de casi todas tus ideas ya se probó afuera, con muchísima más plata, y fracasó o tuvo que cambiar:**
   - Convoy cerró en 2023 después de levantar más de USD 900 M.
   - Amazon anunció en enero de 2026 el cierre de sus tiendas físicas Amazon Go y Fresh (TechCrunch, 2026-01-27).
   - Grabango cerró en 2024.
   - StoryFile entró en concurso preventivo en 2024.
   - Klima se cerró en 2025.
   - Payoneer cerró su escrow en 2018.

   No quiere decir que tus ideas sean malas. Quiere decir que el problema que viste es real (por eso alguien lo intentó), pero **la forma "para todos, en todo el país" no funcionó ni con cientos de millones**.
2. **Los que sí ganaron se metieron en un nicho y le cobraron a quien pierde plata con el problema:**
   - Caramel: autos entre particulares, comprada por eBay.
   - Porter: fletes urbanos chicos, rentable.
   - Trax e Involves: góndola para marcas.
   - BlackBuck: servicios al camionero.
   - Vivo Recuerdo: homenajes para funerarias.

   Esa es la lección más útil de todo el estudio.
3. **"Ser el primero" no está disponible en ninguna de las 11.** En Argentina ya existen Avancargo, Go2Future, Carrefour Flash, Sensify y Mirá Precios. La ventaja tiene que salir de elegir bien el nicho, del precio y de la ejecución, no de llegar primero.
4. **Tus mejores ideas convergen en el mismo lugar: las operaciones de las PyMEs y del canal tradicional.**
   - L9 (stock de PyMEs), L10 (faltantes en almacenes para distribuidoras) y L6 (fletes de productores) son todas ingeniería industrial aplicada con datos de campo.
   - **Ahí está tu ventaja real.** Donde no la hay (clips, precios del súper, huella personal, revivir), el puntaje cae a 2-4.
5. **El cuello de botella nunca es la app, es saber si alguien paga.** Las 7 investigaciones llegan a lo mismo: **antes de programar, hablar con 15-30 clientes posibles** y probar a mano. Todavía no hiciste ninguna entrevista. Ese es el paso que falta, no más investigación.
6. **Tu idea más ambiciosa (L10) y tu mejor vehículo (L9) son parientes:**
   - Las dos tratan del stock de comercios.
   - Las distribuidoras pueden ser clientes de las dos.
   - Lo que aprendas en una sirve para la otra.

---

## 3. Cada idea, desarrollada

### L6 — "Uber de la logística empresarial" (favorita)
**Informe:** `research/fuentes/2026-10-08-L6-logistica.md`

- **El problema es enorme (DATOS):**
  - ~91% de la carga argentina va en camión (BCR, 2018).
  - Unas 2 unidades por empresa transportista (UNTREF, 2019).
  - Solo el 5% de los transportistas tiene una digitalización "significativa", según un índice que armó Avancargo (Forbes, 2023-04-12). Ojo: la fuente es interesada, porque Avancargo vende software.
- **Parecidos afuera (DATOS):**
  - Convoy (EE.UU.) cerró en 2023 tras levantar más de USD 900 M.
  - Kobo360 (Nigeria) se fundió porque les pagaba a los camioneros antes de cobrar.
  - Transfix y BlackBuck vendieron su negocio de fletes.
  - Uber Freight sigue perdiendo plata en 2026.
  - **Ganan plata** Porter (India, fletes urbanos chicos, rentable) y los que **le venden servicios al camionero** (BlackBuck, Frete.com en Brasil).
- **Argentina (DATOS):**
  - **Avancargo** existe desde ~2017: facturó USD 5 M en 2022 y pasó de marketplace a software y servicios.
  - Hay apps de granos (Humber, MuvinApp, que compró la Bolsa de Comercio de Rosario) y de fletes chicos (Fletalo, Kargho).
  - Los grupos de WhatsApp de transportistas son probablemente el competidor real (no se pudieron medir).
- **Tu nicho de frutas y verduras (DATOS):**
  - El Mercado Central mueve ~1,4 M t por año.
  - El flete lo termina pagando el productor.
  - Hay camiones que vuelven vacíos.
  - No apareció ninguna startup de este nicho, pero la búsqueda quedó corta.
- **La trampa (ESTIMACIÓN):** si pagás al camionero antes de cobrar al cliente (30-90 días), cada viaje de ~USD 1.500 inmoviliza ~USD 1.350 durante ~53 días. **Con tus USD 1.300 alcanza para un viaje a la vez.** Así se fundió Kobo360.
- **Versión que sí (OPINIÓN):**
  - **Etapa 1:** broker por WhatsApp + planilla, en **un solo corredor** (por ejemplo, la vuelta desde el Mercado Central hacia una zona productora). El cliente le paga directo al camionero y vos cobrás tu comisión aparte.
  - **Etapa 2 (hipótesis):** servicios para el camionero chico (cobros, documentos, pagos).
- **Validación:** 4 semanas, USD 200 como máximo.
  - 15-20 entrevistas en la playa de camiones del Mercado Central (de 2 a 10 h), con productores y con dadores de carga.
  - Después, intermediar 3-5 viajes reales.
  - Sigue si hay ≥3 viajes cerrados y ≥1 cliente que repite **a través tuyo**.
- **Puntajes:** problema 8 · pago 5 · competencia 4 · tu ventaja 3 · factibilidad 4 · escalabilidad 6 · riesgo 3 → **4,7**.
- **Mi opinión:** es la idea donde el problema es más grande y donde más fracasó la solución. Tu ventaja hoy es baja porque no tenés red en el sector. Como **experimento para aprender una industria por dentro**, vale. Como startup "Uber para todo el país", no.

### L10 — Stock con IA y cámara para supermercados (favorita)
**Informe:** `research/fuentes/2026-10-08-L10-stock-ia-camara.md`

- **El "agarrás y te vas" está en retirada (DATOS):**
  - Amazon sacó Just Walk Out de sus Amazon Fresh en abril de 2024 y anunció el 2026-01-27 el cierre de sus tiendas físicas Go y Fresh: dijo que no encontró "el modelo económico correcto". Sigue vendiendo la tecnología a terceros (estadios, por ejemplo).
  - Hubo reportes (The Information, 2024) de revisores humanos en India que miraban las compras; Amazon lo negó. Las dos versiones están en el informe.
  - Grabango cerró en 2024 y Standard AI abandonó el checkout autónomo.
- **En Argentina ya se intentó (DATOS):**
  - Go2Future/MiniGo abrió una tienda autónoma en 2022 (~USD 900.000).
  - Carrefour Flash en Pilar (2023): 20 cámaras y unos 200 sensores.
  - **Sensify**, startup argentina, pone cámaras con IA en heladeras del canal tradicional. Tiene inversión de Kamay Ventures (Arcor, Coca-Cola, Bimbo) y de Arca Continental (2025).
- **Lo que crece es "ver la góndola" (DATOS):** robots (Simbe), cámaras fijas (Focal), carritos (Caper) y, sobre todo, **reconocimiento de góndola por foto de celular para marcas** (Trax, Ailet, Involves, Teamcore).
- **El mercado que importa (DATO):** almacenes y autoservicios independientes son ~35% del consumo masivo en Argentina, con más de 194.700 puntos de venta (NielsenIQ, junio de 2026). Ahí casi no hay tecnología, y **pierden plata con el faltante la marca y el distribuidor**.
- **Qué puede hacer la IA hoy:**
  - Costo: USD 0,0005 a 0,006 por foto (ESTIMACIÓN con precios oficiales). La plata no es la barrera.
  - **Contar unidades exactas no anda:** en un benchmark de 2025, el mejor modelo acierta el 42,9%, y el 13,9% con más de 50 objetos (DATO).
  - Detectar huecos y si está o no una lista corta de productos parece factible, pero **hay que medirlo con fotos reales**.
- **Versión que sí (OPINIÓN):** **auditoría de góndola y faltantes por foto de celular**, vendida a **distribuidoras y marcas medianas**. Variante: "pedido sugerido por foto" para preventistas.
  - Etapa 1: servicio hecho a mano.
  - Etapa 2: software y una **red de datos de qué hay y qué falta en miles de almacenes**.
- **Validación:** 4 semanas, USD 200 como máximo.
  1. Entrevistas a almaceneros, preventistas y gente de trade marketing.
  2. Prueba técnica con 100 fotos, contadas a mano; hay que llegar a ≥90% de acierto.
  3. Piloto con 1-2 distribuidoras; hacen falta ≥3 de 10 que acepten un piloto pago o firmen una carta de intención.
- **Puntajes (esta versión):** problema 7 · pago 5 · competencia 4 · tu ventaja 4 · factibilidad 6 · escalabilidad 7 · riesgo 5 → **5,4**. El "Amazon Go argentino" sacó 2,0.
- **Mi opinión:** tu intuición de "tecnología con cámara para el súper" apunta a algo real, pero la parte de "descontar lo que se lleva el cliente" ya la resuelve el lector de código de barras. **El problema del stock no está en las salidas: está en las entradas, en la reposición y en que nadie mira la góndola.** La versión por foto de celular es la única que podés empezar con tus recursos y la que más potencial de startup tiene de toda la lista. La gran incógnita es si las distribuidoras pagan.

### L9 + L5 — Calculadora de ingeniería + IA analista (favorita)
**Informe:** `research/fuentes/2026-10-08-L5-L9-herramientas-analisis.md`

- **Parecidos (DATOS):**
  - Las calculadoras sueltas ya existen gratis en español y viven de publicidad. No hay espacio para cobrar por eso.
  - El software de inventario que sí cobra (Prediko desde USD 49/mes, Netstock desde USD 900/mes) cobra porque **se conecta a los datos del cliente y se usa todos los meses**.
  - **No apareció ninguna herramienta en español** donde subas tu Excel y te devuelva el diagnóstico de stock (eso no prueba que no exista).
- **L5 sola (DATOS):** categoría saturada y que se volvió gratis. ValidatorAI es gratis y dice haber analizado ~288.000 ideas. ChatGPT hace lo mismo.
- **Argentina (DATOS):** 1,77 M de certificados MiPyME (2023). No hay ninguna encuesta de cuánto pagaría una PyME por esto. Hay una señal de desconfianza a subir datos a la nube.
- **Diseño propuesto (OPINIÓN):** "**Diagnóstico de stock en 5 minutos**".
  - Los números salen de **fórmulas fijas**; la IA solo los explica.
  - Gratis como imán → proyecto de USD 200-600 → seguimiento de USD 50-150 por mes (rangos del estudio del 2026-10-01, a validar).
  - L5 entra como módulo de "rentabilidad de lo que ya vendés".
- **Validación:** 2-4 semanas, menos de USD 200.
  - Ofrecer el diagnóstico gratis a 30 negocios de 2 segmentos (vendedores de Mercado Libre/Tiendanube y ferreterías/distribuidoras).
  - Si ≥10 mandan su archivo, la fricción con los datos es manejable.
  - Si ≥2-3 pagan algo, se construye la web.
- **Puntajes L9:** problema 6 · pago 4 · competencia 6 · tu ventaja 6 · factibilidad 8 · escalabilidad 5 · riesgo 7 → **6,0**. L5 sola: 3,0.
- **Mi opinión:** las calculadoras son lo menos valioso de tu idea. Lo valioso es que **el cliente suba sus datos reales** y que **un ingeniero se haga cargo** del resultado. Así encaja perfecto en la etapa 1: te paga, te mete en PyMEs reales y, si después de 20-50 diagnósticos aparece un patrón, ahí puede estar el software.

### L1 — Intermediario de transacciones (favorita)
**Informes:** `ideas/2026-10-07-intermediario-pagos-seguros.md` y `research/fuentes/2026-10-08-L1-intermediario.md`

- **El dolor en Argentina (DATOS):**
  - 34.468 reportes de delitos informáticos en 2024 (UFECI). De ellos, 21.729 son fraudes en línea, y el 56% son compraventas por internet: ≈12.170 casos (ESTIMACIÓN).
  - 488 reportes por alquileres temporarios.
  - No se encontró cuánta plata se pierde por caso.
- **El escrow genérico es chico (DATOS):**
  - Escrow.com, el líder mundial con 26 años, facturó A$12,3 M en 2025, con volumen en caída por cuarto año seguido.
  - Payoneer cerró el suyo en 2018.
- **Los que ganaron eran de nicho (DATOS):**
  - Caramel (autos entre particulares) fue comprada por eBay en 2025.
  - En Colombia (CarroYa) y Brasil hay pago custodiado para autos.
- **Tu duda de "la caja vacía" (OPINIÓN):** no tiene solución barata cuando hay envío a distancia. La salida es elegir **nichos sin caja**: entrega en persona, o bienes que pasan por un registro, donde el registro hace de juez.
- **Versión que sí (OPINIÓN):** **"cierre seguro" de autos usados entre particulares** (1.887.024 transferencias en 2025, DATO). Verificás el auto y coordinás que pago y firma pasen en el mismo momento, **sin tocar la plata**. Así no hace falta licencia de PSP. Hay que consultar con un abogado igual.
- **Validación:** 4 semanas, USD 200 como máximo.
  - 15-20 entrevistas a gente que compró o vendió un auto a un particular.
  - Una página con precio visible.
  - 1-3 operaciones reales.
- **Puntajes:** problema 7 · pago 4 · competencia 6 · tu ventaja 3 · factibilidad 4 · escalabilidad 5 · riesgo 3 → **4,6**.
- **Mi opinión:** es una buena idea que nace de un dolor real, pero **no tenés ventaja en autos ni en fintech**. La duda principal es que la gente ya lo resuelva gratis "a la argentina", encontrándose en el registro con la plata en mano. La dejaría como **candidata de etapa 2**, con una validación barata cuando quieras.

### L8 — Edición automática de video para empresas
**Informe:** `research/fuentes/2026-10-08-L3-L8-A3-video-y-visualizacion.md`

- **Parecidos (DATOS):**
  - En EE.UU. hay productos que convierten fotos + ficha en un video y cobran USD 25-300 por mes (AutoReel, Reeltors, Reel-E).
  - En Argentina no apareció uno local.
  - Zonaprop tiene más de 11.000 clientes y anunció IA para automatizar avisos: es el riesgo más grande.
- **Costo (DATO/ESTIMACIÓN):** menos de USD 0,30 por video.
- **Versión que sí (OPINIÓN):** empezar como servicio con motor propio y pasar a producto con 10-20 clientes. A la larga el valor es "**cero intervención**": se conecta al sistema de la inmobiliaria y publica solo.
- **Validación:** 3-4 semanas, USD 10-60. Probar con 30 inmobiliarias y 30 agencias de usados a la vez. Sigue si hay ≥5 clientes pagos y ≥3 que renuevan.
- **Puntajes:** problema 5 · pago 4 · competencia 5 · tu ventaja 4 · factibilidad 7 · escalabilidad 6 · riesgo 4 → **5,5**.
- **Mi opinión:** es la opción más directa si querés un **producto de software** en la etapa 1. No la veo como startup grande, pero enseña a vender software a PyMEs. Lo débil: no hay ningún dato de que un video haga vender más una propiedad o un auto.

### L4 — Revivir seres queridos con IA
**Informe:** `research/fuentes/2026-10-08-L4-recuerdos-ia.md`

- **"Revivir" ya se probó y le fue mal (DATOS):**
  - StoryFile entró en concurso preventivo en 2024.
  - Eternos pivoteó en 2025.
  - 2wai generó rechazo masivo en 2025.
  - En una encuesta canadiense de 2026, solo el 6% quería seguir hablando con una versión digital de su pareja.
  - En China sí hay mercado pago.
- **Legal (DATOS):**
  - El art. 53 del Código Civil y Comercial exige consentimiento para usar imagen y voz; si la persona murió, deciden los herederos.
  - HeyGen pide un video de consentimiento de la propia persona.
  - ElevenLabs prohíbe clonar una voz sin consentimiento.
- **Lo que se paga (DATOS):** homenajes en el Reino Unido (£50-110 por video en crematorios) y Vivo Recuerdo en España (más de 150 funerarias).
- **Argentina (DATOS):** 353.428 muertes en 2024. No se encontró ninguna cochería con video homenaje (búsqueda limitada).
- **Versión que sí (OPINIÓN):** pack "homenaje" (restaurar fotos, video homenaje y animación **sin voz**), con una **línea roja pública**: sin voz clonada, sin chatbots, con consentimiento escrito. Piloto B2B con cocherías.
- **Puntajes:** homenaje **5,6** · "revivir" **3,9**.
- **Mi opinión:** "revivir" no. No por miedo a equivocarte, sino porque **si sale mal, lo paga una familia en duelo**. El homenaje es un servicio chico y ético. Si pega con cocherías, aparece una pregunta más grande: una plataforma de homenaje digital para funerarias en Latinoamérica.

### A3 — Visualizador de merch personalizado
**Informe:** `research/fuentes/2026-10-08-L3-L8-A3-video-y-visualizacion.md`

- **Parecidos (DATOS):**
  - El mockup es commodity: Printful lo da gratis y Placeit cuesta USD 7,47 por mes.
  - Los configuradores cuestan USD 49-300 por mes.
- **Versión que sí (OPINIÓN):** **cotizador visual para talleres**. El cliente sube su logo, elige prenda, técnica y cantidad, y ve el mockup con **el precio y el plazo al instante**. El costeo por técnica es ingeniería industrial pura, y conecta con L9.
- **Validación:** 15-20 entrevistas a talleres y un piloto a mano con 2-3 talleres, por menos de USD 30.
- **Puntaje:** **4,5**.
- **Mi opinión:** no hay datos de demanda en Argentina; primero van las entrevistas.

### L7 — Huella de carbono
**Informe:** `research/fuentes/2026-10-08-L2-L7-apps-consumo-y-carbono.md`

- **App para personas (DATOS):** Klima se cerró en 2025 y Joro/Commons dejó el seguimiento "gratis para siempre". No apareció ninguna que viva de suscripciones. **2,0: descartar.**
- **Empresas (DATOS):**
  - Hay obligación real: la norma europea contra la deforestación (EUDR) se aplica desde el 2026-12-30 a soja, carne y cueros, y Mendoza obliga a reportar emisiones.
  - Pero VISEC (gratis) cubre soja y carne, la Unión Europea recortó obligaciones en 2026 y el mercado de software está en consolidación.
  - **4,0.** Mejor como módulo de la consultora que como empresa aparte.

### L2 — Fotos a los precios del súper
**Informe:** mismo que L7.

- **DATOS:**
  - Ya existe gratis en al menos 5 apps de Google Play y en la app de Carrefour Argentina.
  - Mirá Precios tenía ~15.000 usuarios y no pensaba cobrar.
  - Según RevenueCat (2026), solo el 17% de las apps de suscripción llega a USD 1.000 por mes en dos años.
- **3,0: no como negocio.**

### L3 — Automatización absoluta de clips
**Informe:** mismo que L8.

- **DATOS:**
  - El pago efectivo es ~USD 0,39 cada 1.000 vistas.
  - Instagram (2026-04-30) y YouTube (2026-10) le bajan el alcance a lo re-subido con edición mínima.
  - Escalar con más cuentas viola las reglas.
  - El "scanner de campañas" del plan de septiembre ya existe en Apify, con 83 usuarios.
- **3,0: no.** Lo único con lógica sería una agencia de clipping del lado de la marca, sin investigar.

---

## 4. Propuesta para debatir (OPINIÓN de Claude)

Respetando las reglas de la etapa 1 (**un negocio principal + como máximo un experimento chico**, con pérdida máxima y fecha de corte):

1. **Negocio principal de la etapa 1: L9, "Diagnóstico de stock".** Es el de mejor puntaje, el más barato (menos de USD 200) y el que usa tu ventaja real. Además es el mejor **canal de descubrimiento**: cada diagnóstico te muestra por dentro el stock, las compras y los faltantes de una PyME.
2. **Experimento en paralelo: validar L10 en su versión "auditoría de góndola por foto".** Casi todo es entrevistar y una prueba técnica de 100 fotos. Es tu candidato más fuerte a startup, y **las distribuidoras pueden ser clientes de L9 y de L10 a la vez**.
3. **En reserva, por orden:**
   - L8 (si querés un producto de software ya);
   - L1, autos (candidata de etapa 2);
   - L6, corredor frutihortícola (si conseguís un contacto en el Mercado Central o en transporte);
   - L4, homenaje;
   - A3, cotizador;
   - L7, empresas.
4. **Descartadas por ahora:** L2, L3, L5 como producto suelto (pasa a ser módulo de L9), L7 para personas, L4 "revivir".

**Por qué así:** tus dos favoritas grandes (L6 y L10) tienen versiones gigantes que fracasaron con cientos de millones. La forma de llegar a algo grande no es copiar la versión gigante, sino **meterte en el problema desde abajo** (diagnósticos y fotos de góndola) hasta ver algo que los grandes no ven. Es lo que Paul Graham llama "vivir en el futuro y construir lo que falta" (ensayo de 2012).

**El paso que falta en todas, sin excepción:** hablar con clientes. Ninguna idea tiene todavía evidencia de que alguien en Argentina pague por ella.

---

## 5. Preguntas para Facu

1. ¿Te convence la propuesta (L9 principal + validar L10)? ¿O preferís otro orden? Si no estás de acuerdo, decímelo y lo discutimos con datos.
2. **Contactos (esto define por dónde empezar):** ¿conocés a alguien en distribuidoras, almacenes o autoservicios, transporte o el Mercado Central, inmobiliarias, agencias de autos o talleres de estampado? La ventaja más grande al principio es **tener acceso**.
3. **Tus amigos programadores:** ¿serían socios (con participación), ayuda paga o un favor? Conviene definirlo antes de construir nada.
4. ¿Leíste "The Mom Test"? Las 7 validaciones arrancan con entrevistas, y ese libro es la herramienta para hacerlas bien.

---

## 6. Informes completos

| Idea | Archivo |
|---|---|
| L6 logística | `research/fuentes/2026-10-08-L6-logistica.md` |
| L10 cámara/stock | `research/fuentes/2026-10-08-L10-stock-ia-camara.md` |
| L1 intermediario | `research/fuentes/2026-10-08-L1-intermediario.md` + `ideas/2026-10-07-intermediario-pagos-seguros.md` |
| L9 + L5 herramientas | `research/fuentes/2026-10-08-L5-L9-herramientas-analisis.md` |
| L2 + L7 | `research/fuentes/2026-10-08-L2-L7-apps-consumo-y-carbono.md` |
| L3 + L8 + A3 | `research/fuentes/2026-10-08-L3-L8-A3-video-y-visualizacion.md` |
| L4 recuerdos | `research/fuentes/2026-10-08-L4-recuerdos-ia.md` |

**Verificación propia de Claude (2026-10-08):** el cierre de Amazon Go y Fresh se confirmó en [TechCrunch, 2026-01-27](https://techcrunch.com/2026/01/27/amazon-is-closing-its-physical-amazon-go-and-amazon-fresh-stores). La nota no da la cantidad de tiendas ni el calendario de cierre.
