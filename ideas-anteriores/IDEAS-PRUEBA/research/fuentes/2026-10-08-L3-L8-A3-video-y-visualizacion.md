# L3, L8 y A3: clips automáticos, video por plantillas y visualizador de merch

**Fecha:** 2026-10-08
**Pedido:** analizar a fondo tres ideas de la libreta y de las notas de Facu:
- **L3:** automatización absoluta de clips para apps que pagan por vistas.
- **L8:** edición automática de video para empresas con videos parecidos (inmobiliarias, concesionarias).
- **A3:** visualizador de indumentaria y merchandising personalizado.

**Contexto leído antes (no se repite acá):**
- `research/2026-10-02-video-foto-133-ideas.md`
- `research/fuentes/2026-09-02-video-clipping.md`
- `proyectos/clipper-semiauto/PLAN.md`
- `research/fuentes/2026-10-02-video-rubros-parecidos.md`
- `research/fuentes/2026-10-02-video-herramienta-autoedicion.md`
- `research/fuentes/2026-10-01-ideas-software-sin-programar.md`

---

## 0. Método y advertencias

- **Qué se hizo:** ~19 búsquedas web y ~30 lecturas directas de páginas (precios oficiales, documentación de plataformas, artículos), el 2026-10-08.
- **Límite:** **la cuota de búsquedas web de la sesión se agotó a mitad del trabajo** (es compartida con otros agentes). Lo que faltaba se completó leyendo páginas oficiales conocidas. **Quedaron sin verificar:**
  - cuántas inmobiliarias, concesionarias y talleres de estampado hay en Argentina;
  - si Mercado Libre Inmuebles o Argenprop ya generan video;
  - el catálogo completo de apps de Tiendanube.

  Ver §5.
- **Etiquetas:**
  - **DATO** (con fuente y fecha);
  - **ESTIMACIÓN** (propia, con el razonamiento);
  - **OPINIÓN** (de Claude).
- **⚠ = fuente con conflicto de interés** (vende herramientas de clipping, compite con quien critica o es la propia empresa hablando de sí misma). Casi todo lo publicado sobre clipping en 2026 viene de **vendedores de herramientas o de redes de clipping que compiten entre sí**. No hay datos auditados de cuánto gana el clipper típico.

### Correcciones a documentos anteriores del proyecto (Regla N.º 1)
1. **`proyectos/clipper-semiauto/PLAN.md` dice "mediana del clipper: USD 305 de por vida". Es un error: es un promedio, no una mediana.**
   - El artículo de Ascynd (2026-07-24) divide USD 2,58 M pagados por 8.466 personas que cobraron algo.
   - En pagos muy desparejos, el promedio queda muy por encima de la mediana: unos pocos ganan mucho y la mayoría casi nada.
   - **La mediana real no la publica nadie.** ESTIMACIÓN: es bastante menor a USD 305.
2. **El mismo plan proponía vender el "scanner de campañas" a "8.400+ clippers" como mercado demostrado.**
   - Hoy ya existe un scraper de campañas de Whop en Apify con exactamente esa función: tarifa, presupuesto restante y velocidad de gasto.
   - Tiene **83 usuarios en total y 21 por mes** ([Apify, consultado 2026-10-08](https://apify.com/fayoussef/whop-clipping-campaigns-scraper)).
   - Señal: la demanda por esa herramienta existe, pero es chica.

---

## 1. Resumen

| Idea | Puntaje (OPINIÓN) | Veredicto en una línea |
|---|---|---|
| **L3: automatización absoluta de clips** | **3/10** | Lo que se automatiza al 100% es justo lo que las plataformas castigan desde 2026: el clipper automático es el clipper mediano, y gana casi nada |
| **L8: video automático para inmobiliarias y concesionarias** | **5,5/10** | La mejor de las tres. El producto existe en EE.UU. (USD 25-300/mes) y en Argentina no encontré un equivalente local. Pero hay alternativas gratis y los portales pueden sumarlo. Validar antes de construir |
| **A3: visualizador de merch** | **4,5/10** | Ver el mockup es commodity (gratis o USD 7,47/mes). Si hay negocio, está en el **cotizador + aprobación del diseño** para talleres, no en la imagen. Mercado sin datos, a validar con entrevistas |

---

## 2. L3: Automatización absoluta de clips

### 2.1 Qué es
Usar una app de clipping: una marca o un streamer publica una campaña con presupuesto fijo, vos cortás clips de su material, los subís a tus cuentas de TikTok, Instagram y YouTube Shorts y te pagan por cada 1.000 vistas verificadas hasta que se acaba el presupuesto. La idea de Facu es **automatizarlo del todo**: bajar el material, cortar, subtitular, publicar en varios canales y enviar a la campaña, sin intervención humana.

### 2.2 Plataformas que existen (verificado el 2026-10-08)

| Plataforma | Qué es | Estado y datos | Fuente |
|---|---|---|---|
| **Whop Content Rewards** | El marketplace dominante. La marca fija la tarifa por 1.000 vistas, el presupuesto, el pago mínimo y el tope por video | Activo. Whop dice tener 3.500 M de vistas y 100 M por día (cifras propias). Forbes (2026-04-29, citado por un competidor) reporta más de USD 40.000/día pagados | [docs.whop.com](https://docs.whop.com/manage-your-business/growth-marketing/content-rewards); [FindClout ⚠](https://findclout.com/blog/content-rewards-complaints) |
| **Vyro** | Marketplace lanzado en octubre de 2025 con respaldo de MrBeast | Activo. Tarifa publicitada USD 3/1.000; según un competidor, las campañas reales pagan USD 1-2 | [Ssemble ⚠](https://www.ssemble.com/pl/blog/vyro-review-2026); [ClipAffiliates ⚠](https://www.clipaffiliates.com/blog/vyro-review) |
| **ClipFarm** (de Airrack) | Comunidad de clipping montada sobre Whop desde agosto de 2024 | Activo. Dice tener más de 45.000 clippers. Caso citado: Druski, 64 M de vistas por USD 10.000 (≈ USD 0,16/1.000, cálculo propio) | [contentrewards.com](https://contentrewards.com/clipfarm); [FindClout ⚠](https://findclout.com/blog/airrack-clipfarm) |
| **ContentRewards.com** | Marketplace con campañas, incluso en español | Una campaña en español de finanzas: USD 1/1.000, presupuesto USD 2.000, quedaban ~USD 1.210 sin gastar; **el mejor clipper había ganado USD 131,72** | [contentrewards.com](https://www.contentrewards.com/campaigns/ebc7dd27-5d08-4d06-86d5-659706286077) (vía búsqueda) |
| **Clip Rewards de Ssemble** | Marketplace con página en español | 67 campañas activas, USD 0,10-3/1.000 (su propio FAQ dice USD 0,35-4: no coincide) | [Ssemble ⚠](https://www.ssemble.com/es/clip-rewards) |
| **Agencias de clipping** (Clipping Culture, cliphaus, Clip Central y otras) | Del lado de la marca: arman y gestionan campañas | Clipping Culture desde USD 15.000; cliphaus USD 5.000-250.000+ (cifras de las propias agencias) | [OpusClip, 2026-08-12 ⚠](https://www.opus.pro/blog/best-clipping-agencies) |
| **Streamers de LATAM que pagan directo** | Sin plataforma | Perú (2025-09-10): un streamer paga S/30 por 80.000 vistas; otro, S/1.000 por millón. Datos de Argentina: **no encontré** | [La República](https://larepublica.pe/streamers/2025/09/10/streamer-sacha-revela-las-jugosas-ganancias-de-sus-cliperos-8-sueldos-minimos-no-es-broma-evat-769400) |

### 2.3 Cuánto paga y cuánto gana el clipper

**DATOS (con su sesgo):**
- **Tarifas publicadas:** USD 0,20-6 por 1.000 vistas, promedio cercano a USD 1, según trackers de terceros ([ClipSpeed ⚠, 2026-09-13](https://www.clipspeed.ai/blog/whop-content-rewards-clipping-guide.html)).
- **Comisión de Whop: 10% fijo** sobre cada pago de campaña por vistas ([ClipSpeed ⚠](https://www.clipspeed.ai/blog/whop-content-rewards-clipping-guide.html)). ClipAffiliates ⚠ habla de ~7%. Whop no lo publica en su documentación. **Sin resolver.**
- **Tiempos de cobro:** ~10 días desde la aprobación (7 de ventana más 3 de retención); el retiro tarda 3-5 días hábiles, o es instantáneo con fee ([ClipSpeed ⚠](https://www.clipspeed.ai/blog/whop-content-rewards-clipping-guide.html)).
- **Lo realmente cobrado** ([Ascynd, 2026-07-24](https://ascynd.io/en/blog/whop-clipping), con datos de Clippa):
  - USD 2,58 M pagados a **8.466 personas** por 6.600 M de vistas.
  - Eso da un **promedio de USD 305 por persona** y una **tarifa efectiva de USD 0,39 por 1.000 vistas**, contra ~USD 1-1,25 publicitado.
  - En febrero de 2026 se pagaron USD 887.000 en ~65.000 transacciones (≈ USD 13,6 cada una).
- **Otro dato sin fecha ni fuente:** Whop habría repartido "más de USD 1,7 M entre más de 98.000 creadores" ([Virlo ⚠](https://virlo.ai/blog/ultimate-guide-to-clip-farming-for-creators)). Si fuera cierto, el promedio daría **~USD 17 por creador** (cálculo propio). No verificable.
- **El CEO de Ssemble ⚠ (2025-09-30)** afirma, sin fuente, que las campañas grandes tienen "decenas de miles de miembros" y que "la mayoría gana menos de USD 3 en total" ([Ssemble](https://www.ssemble.com/es/blog/clipping-monetization-strategies-in-2026)).
- **Rangos de vendedores ⚠:** principiantes USD 100-500/mes; el top 1%, más de USD 10.000 ([OpenClip](https://openclip.app/guides/how-much-do-clippers-make)). Es un vendedor de herramientas: tomarlo como techo.

**ESTIMACIÓN (cuántas vistas pagas hacen falta):**
- Para cobrar **USD 300/mes netos**, a la tarifa efectiva de USD 0,39/1.000 y con 10% de comisión, hacen falta **~855.000 vistas pagas por mes**.
- A USD 1/1.000 harían falta **~333.000**.
- Las vistas que llegan después de que se agota el presupuesto, o en clips rechazados, no cuentan.

**DATO (problemas reportados):**
- Clips rechazados después de juntar vistas, presupuestos agotados y pagos retenidos por sospecha de bots.
- Una marca (StreamAlive, 2025-09-15) gastó ~USD 1.500 por ~845.000 vistas y estimó, sin auditoría, que casi todas eran bots.
- Según un competidor, Whop sumó un algoritmo antibots, 24 h de demora en los pagos y baneo de por vida a quien use bots (sin fechas) ([FindClout ⚠](https://findclout.com/blog/content-rewards-complaints)).

### 2.4 Qué dicen las plataformas sobre contenido no original (el punto clave)

**Instagram (DATO, fuente oficial, [2026-04-30](https://creators.instagram.com/blog/rewarding-original-creators-on-instagram)):**
- Extendió a fotos y carruseles la regla que ya aplicaba a Reels desde 2024: **las cuentas que publican mayormente contenido no original dejan de ser recomendadas** a quienes no las siguen.
- **No alcanza con agregar borde, marca de agua, subtítulos o créditos.** Hay que aportar valor real: contexto, información o un punto de vista nuevo.
- Se recupera si la mayoría de lo publicado en los últimos 30 días es original (cálculo continuo).

**YouTube (DATO):**
- La política de "contenido inauténtico" existe desde el 2025-07-15 y se aclaró en julio de 2026 ([resumen de prensa](https://outlierkit.com/blog/youtube-updates-july-2026)).
- **El 2026-10-02**, según Android Headlines, YouTube anunció por su Creator Liaison que **el feed de Shorts va a suprimir activamente los re-subidos** con ediciones mínimas, voces automáticas o cambios de plantilla. **Pasar un clip por un auto-editor no cuenta como valor agregado.** El canal puede seguir monetizado pero quedar "prácticamente invisible" ([Android Headlines](https://www.androidheadlines.com/2026/10/youtube-cuts-reach-reuploaded-shorts-originality-push.html)).

**TikTok (DATO secundario):**
- Endureció el control de contenido no original desde el **2025-09-15**: reposts sin aporte propio y clips de TV o películas aunque se borre el logo ([BigSeller](https://www.bigseller.pro/blog/articleDetails/3778/tiktok-unoriginal-content.htm)).
- Lo re-subido puede quedar fuera del For You.
- No pude leer el texto oficial de TikTok de 2026.

**Matiz importante (OPINIÓN):**
- En el clipping, la marca **te autoriza** a usar su material, así que no es robo de derechos.
- Pero los algoritmos no saben que hay autorización: miden si el video aporta algo.
- Un clip cortado y subtitulado por una máquina es, por definición de Instagram y YouTube, poco original. Va a tener alcance bajo justo en las superficies (For You, Explorar, feed de Shorts) de donde salen las vistas que pagan.

### 2.5 APIs, multi-cuenta y baneos

**DATOS:**
- **TikTok (API oficial):** los clientes no auditados solo publican en modo privado ("SELF_ONLY"), con hasta 5 usuarios cada 24 h y cuentas privadas. Para publicar en público hay que pasar una auditoría ([TikTok for Developers](https://developers.tiktok.com/doc/content-sharing-guidelines)). Además hay un tope de ~15 publicaciones por día por cuenta (dato de la documentación, vía búsqueda).
- **Instagram (API oficial):** 50 o 100 publicaciones por cuenta cada 24 h; la propia documentación de Meta se contradice ([Meta](https://developers.facebook.com/docs/instagram-platform/content-publishing)). Solo cuentas profesionales.
- **YouTube:** los proyectos de API no auditados suben videos privados (estudio del proyecto del 2026-09-02).
- **Multi-cuenta en TikTok:** tener varias cuentas no está prohibido en sí. Crear cuentas para evadir un baneo o hacer spam lleva al cierre de todas, y puede terminar en bloqueo del dispositivo y la IP. La app permite 3 cuentas por teléfono (blogs de vendedores de navegadores multi-cuenta ⚠, [Shortimize](https://www.shortimize.com/blog/how-to-manage-multiple-tiktok-accounts-2)). Las "granjas de teléfonos" y navegadores antidetección existen, pero son **evasión explícita de los controles**: no se recomiendan ni se detallan acá.

**Conclusión sobre "automatización absoluta" (OPINIÓN, con base en lo anterior):**
- Técnicamente **se puede** armar de punta a punta con herramientas que existen.
- Pero choca contra cuatro paredes:
  1. Las plataformas castigan en el alcance justo el contenido que sale de una máquina sin aporte humano.
  2. Las APIs oficiales limitan la publicación automática.
  3. Escalar significa más cuentas, y eso viola las reglas.
  4. El mercado está saturado: decenas de miles de clippers por campaña y tarifa efectiva de ~USD 0,39/1.000.
- El "100% automático" no es una ventaja: **es lo que ya hace el clipper mediano**. Lo poco que funciona (diario público de r/whop citado en el estudio de septiembre) viene de **elegir bien campañas y momentos**, que es trabajo humano.

### 2.6 Herramientas de auto-clip: ¿conviene vender la herramienta o el servicio?

| Herramienta | Precio | Fuente |
|---|---|---|
| OpusClip | Gratis (60 créditos, con marca de agua), Starter USD 15/mes (150 min), Pro USD 29/mes o USD 174/año | [Castmagic ⚠, verificado 2026-08-20](https://www.castmagic.io/blog/opus-clip-pricing) |
| Vizard | Gratis con marca de agua; pagos de ~USD 14,50 a 60/mes según la fuente (no coinciden) | [Klap ⚠](https://klap.app/blog/vizard-ai-review); [Kompozy](https://kompozy.io/compare/klap-vs-vizard) |
| Klap | USD 14-199/mes según la fuente (no coinciden) | Ídem |
| Submagic | ~USD 20/mes | [Morphed ⚠](https://morphed.app/blog/vizard-alternatives) |

**DATO sobre OpusClip:**
- Dice tener más de 10 M de usuarios ([Caplight, abril de 2026](https://www.caplight.com/company/opusclip)).
- Ingresos estimados por terceros: ~USD 10 M/año ([Getlatka, estimación](https://getlatka.com/companies/opus.pro/team)).
- Financiación de USD 36,8 M a 79 M según la fuente.

**OPINIÓN:**
- **Vender la herramienta de clipeo:** no. Competirías con OpusClip, Vizard, Klap, Submagic, Ssemble y una docena más, con millones de usuarios, rondas de inversión y precios de USD 15-30/mes. Y la herramienta de "inteligencia de campañas" ya existe en Apify con 83 usuarios.
- **Vender el servicio de clipero:** tampoco. Es destajo digital a USD 0,39/1.000.
- **Lo único con algo de lógica de negocio es el lado de la marca:** una **agencia o red de clipping para streamers, podcasts y marcas de habla hispana**, donde vos armás la campaña, reclutás clipperos y cobrás gestión.
  - Las agencias de EE.UU. cobran presupuestos de USD 5.000-250.000+ (cifras propias ⚠).
  - Eso es venta B2B y gestión de gente, no automatización.
  - **No lo investigué a fondo** (la búsqueda se cortó): ni la demanda de los canales de streaming argentinos ni si ya existe una agencia local.

### 2.7 Cobro desde Argentina
- **DATO:** Whop paga a más de 200 países y **Argentina figura en la lista**. Los métodos (banco por Whop Payments, PayPal, Coinbase) varían según el país. Retiro mínimo: USD 10. Los fees de cada método no están publicados ([docs.whop.com](https://docs.whop.com/manage-your-business/manage-payouts/set-up-payouts.md)).
- **No verificado:** qué métodos concretos aparecen para una cuenta argentina. Se ve recién al crear la cuenta.

### 2.8 Modelo de negocio, números, MVP

**A. Lo que pidió Facu (clipper 100% automático):**
- **ESTIMACIÓN:** con 1 cuenta por plataforma y alcance castigado por originalidad, el escenario mediano es de USD 0-50/mes.
- Para llegar a USD 300/mes hacen falta ~0,3-0,9 M de vistas pagas por mes, sin campañas agotadas ni rechazos.
- **Costo:** USD 15-30/mes de herramienta.
- **Pérdida máxima** (si se hiciera igual): USD 60 y 4 semanas.

**B. Variante "agencia de clipping hispana" (solo hipótesis):**
- **ESTIMACIÓN no verificada:** cobrar 15-30% de gestión sobre presupuestos de campaña de USD 1.000-5.000. Eso da USD 150-1.500 por campaña.
- Requiere vender a marcas y streamers y moderar fraude. No es producto escalable al principio.

**MVP (de B, si se quisiera probar):**
- Facu solo, Whop como infraestructura, 2-4 semanas, menos de USD 50.
- El presupuesto de la campaña lo pone el cliente.

### 2.9 Riesgos
- Cambio de reglas de alcance: Instagram (2026-04-30) y YouTube Shorts (2026-10-02), las dos en los últimos 6 meses.
- Baneo de cuentas por automatización o multi-cuenta.
- Campañas agotadas, rechazos posteriores y pagos retenidos por sospecha de bots.
- Saturación.
- Dependencia total de Whop: un solo intermediario manda.
- Fraude de vistas que hace que las marcas desconfíen del canal y bajen las tarifas.

### 2.10 Cómo validar en 2-4 semanas con menos de USD 200
- **Para A** (no lo recomiendo, pero si Facu quiere sacarse la duda):
  - 3 semanas, 1 cuenta por plataforma, OpusClip Starter (USD 15), 5 campañas elegidas con más del 60% del presupuesto restante.
  - Registrar vistas, vistas pagas, rechazos y USD netos.
  - **Corte:** menos de USD 30 netos en 3 semanas → se cierra.
  - El dato útil que deja es la **tarifa efectiva propia**, no la publicitada.
- **Para B:**
  - Lista de 30 streamers, podcasts y marcas argentinas con contenido largo.
  - 30 mensajes ofreciendo una campaña piloto gestionada.
  - **Corte:** menos de 2 interesados con presupuesto → se cierra. Costo ~USD 0.

### 2.11 Veredicto L3 (OPINIÓN)

| Criterio | Puntaje | Por qué |
|---|---|---|
| Tamaño del problema | 5 | Las marcas sí pagan por distribución (USD 40.000+/día en Whop), pero es un canal de marketing de nicho |
| Disposición a pagar | 3 | Al clipero le llegan ~USD 0,39/1.000 efectivos; las herramientas se venden a USD 15-30/mes |
| Espacio frente a la competencia | 2 | Decenas de miles de clipperos por campaña; OpusClip y compañía con millones de usuarios; el scanner ya existe |
| Ventaja de Facu | 2 | Ninguna específica: la ingeniería industrial no juega; el español ayuda un poco |
| Factibilidad | 6 | Técnicamente armable con herramientas existentes; las APIs oficiales frenan lo "absoluto" |
| Escalabilidad | 2 | Escalar = más cuentas = violar las reglas |
| Riesgo (10 = bajo) | 2 | Baneos, cambios de algoritmo cada pocos meses, fraude |
| **Global** | **3/10** | |

**Opinión:**
- La "automatización absoluta de clips" es la versión más automatizada de un negocio cuyo cuello de botella **no es la automatización sino el criterio**. En 2026 las tres plataformas decidieron explícitamente bajarle el alcance a lo que sale de una máquina sin aporte humano.
- Construirla enseña algo (pipelines de video, APIs), pero **no construye un activo propio**: las cuentas son frágiles y el cliente es Whop.
- No la recomiendo como negocio. Si Facu siente la tentación, que sea un experimento de 3 semanas con pérdida máxima de USD 60.
- El ángulo que podría valer, la **agencia de clipping del lado de la marca para el mundo hispano**, es un negocio distinto (B2B, gestión de red, antifraude) y **queda pendiente de investigar**.

---

## 3. L8: Edición de video automática para empresas con videos parecidos

### 3.1 Qué es
Una aplicación o página donde una inmobiliaria o concesionaria carga las fotos y los datos de cada propiedad o auto (o conecta su sistema) y recibe sola un video con su marca: reel vertical, tour, precio, características. Mismo formato todas las veces. Es el caso ideal de automatización: **el insumo es una planilla y fotos, no video crudo** (estudio 2026-10-02, §1.4).

### 3.2 Parecidos en el mundo

**Inmobiliarias (EE.UU., en inglés):**

| Producto | Precio | Nota | Fuente |
|---|---|---|---|
| **AutoReel** | Sus propias páginas no coinciden. Una dice gratis (2 videos de 720p con marca de agua) / USD 59 (3 videos) / USD 139 (10) / USD 249 (20). Otra (2026-08-13) dice USD 29 (20 videos) / USD 59 (60) / USD 129 (equipo) / USD 299 (ilimitado) | Dice tener **85.000+ agentes** y 225.000+ videos (cifras propias). No menciona español | [AutoReel FAQ ⚠](https://www.autoreelapp.com/faq/cost-effective-realtor-tools/how-much-does-autoreel-cost-per-month-for-individual-real-estate-agents); [AutoReel vs Reel-E ⚠](https://www.autoreelapp.com/compare/autoreel-vs-reel-e) |
| **Reeltors.ai** | Primer video gratis; USD 49 / 99 / 199 por mes | Sube 3-20 fotos y en ~60 s da un video 9:16 o 1:1 con música y subtítulos | [Capterra](https://www.capterra.com/p/10045003/Reeltors-ai/) |
| **Reel-E** | USD 59 / 129 / 599 por mes (Capterra) o USD 25 / 49 (según AutoReel) | Precios contradictorios | [Capterra](https://www.capterra.com/p/10037342/Reel-E/) |

**Concesionarias:**

| Producto | Precio | Nota | Fuente |
|---|---|---|---|
| **Spyne** | No publica precios: cotiza según el volumen de stock y la cantidad de sucursales | Plan Lite: fotos con fondo, patente tapada. Plan Pro: **tour en video y vista 3D** | [Spyne](https://www.spyne.ai/pricing) |
| **CarPixAI** | USD 29-149/mes | Fotos | Estudio 2026-10-02 ([GetApp](https://www.getapp.com/all-software/a/carpixai/)) |
| Edición manual tercerizada | USD 45-120 por vehículo | Referencia de lo que reemplaza | Estudio 2026-10-02 ([Photoroom ⚠](https://www.photoroom.com/blog/ai-car-photography-for-dealerships-cost-workflow-2026)) |

**Plataformas de video por plantilla (la "fábrica" sobre la que se puede construir):**

| Plataforma | Precio (DATO, consultado 2026-10-08) | Comentario |
|---|---|---|
| **Shotstack** | USD 10 por única vez (50 min); Starter USD 39/mes (250 min, 15,6¢/min); Pro USD 99 (750 min); Scale USD 199 (2.000 min, 10¢/min); Volume USD 499 (10.000 min, 5¢/min) | API pura, la más transparente en precio ([Shotstack](https://shotstack.io/pricing/)) |
| **Creatomate** | Prueba con 50 créditos sin tarjeta. Essential 2.000 créditos ("200+ videos"), Growth 10.000+, Beyond 50.000+. **La página no mostró los precios en dólares.** 720p a 25 fps ≈ 14 créditos por minuto | Tiene editor de plantillas visual: sirve sin programar ([Creatomate](https://creatomate.com/pricing)) |
| **Plainly** | Starter USD 69/mes (50 min), Explorer USD 134 (100 min), Team USD 259 (200 min), Pro USD 649 (600 min), ilimitado desde USD 1.500 | Basada en plantillas de After Effects: cara para empezar ([Plainly](https://www.plainlyvideos.com/pricing)) |
| **Bannerbear** | USD 49 / 149 / 299 por mes; video: 2 créditos por segundo | Más orientada a imágenes ([Bannerbear](https://www.bannerbear.com/pricing/)) |
| **Remotion** (código propio) | Gratis para individuos y empresas de hasta 3 empleados | Estudio 2026-10-02 ([Remotion](https://www.remotion.dev/docs/license/pricing)) |

**Alternativas gratis que compiten:**
- Meta Advantage+ arma un video de anuncio con hasta 20 fotos (estudio 2026-10-02).
- Las plantillas de editores de consumo. Ojo: el estudio 2026-10-02 desaconseja CapCut con material de clientes por su licencia.

### 3.3 Argentina

**DATOS:**
- **Zonaprop** pasó de 3.000 a **más de 11.000 clientes** (inmobiliarias) en diez años. Su próximo paso es incorporar IA en la búsqueda y en la gestión, incluidas **herramientas para automatizar la creación de avisos**. **No menciona video** ([Mercado, 2026-05-27](https://mercado.com.ar/ruta-digital/zonaprop-amplio-su-base-a-mas-de-11-000-clientes-en-una-decada)).
- **CUCICBA** (colegio de corredores de CABA) habla de "más de 300.000 inmuebles en venta en AMBA" ([CUCICBA, 2026-01-09](https://www.cucicba.com.ar/)).
- **Tokko Broker** (el CRM inmobiliario más citado): carga propiedades una vez, las difunde a portales y a la web, y registra las consultas. **No encontré ninguna función de video** ([ComparaSoftware](https://www.comparasoftware.com/tokko-broker)). Aparece en el directorio de Zapier, lo que sugiere que se puede integrar ([Zapier](https://zapier.com/find-apps/t/tokko-broker)); no verifiqué qué datos expone.
- **Sensibilidad al precio:** en mayo de 2024 hubo quejas de inmobiliarias de zona norte (240 "referentes") por "subas insólitas" de Zonaprop ([iProfesional, 2024-05-08](https://www.iprofesional.com/economia/405449-inmobiliarias-en-alerta-denuncian-a-zonaprop-por-aumentos-abusivos)). Es viejo, pero muestra que la inmobiliaria ya siente que paga mucho por marketing.

**NO VERIFICADO (se agotó la búsqueda):**
- Cuántas inmobiliarias hay en Argentina. Proxy: los 11.000+ clientes de Zonaprop.
- Cuántas concesionarias oficiales y agencias de usados hay (la página de ACARA no lo muestra).
- Qué gastan en marketing por mes.
- Si Mercado Libre Inmuebles, Argenprop o ML Autos generan video automático.
- Si existe un producto argentino igual. **No encontré ninguno**, pero la búsqueda fue corta.

### 3.4 ¿Producto (SaaS) o servicio? (OPINIÓN)
- **Arrancar como servicio "hecho por vos" con motor propio, y pasar a producto cuando 10-20 clientes paguen.**
  - Vender un SaaS de autoservicio desde el día 1 en Argentina choca con dos cosas: la inmobiliaria chica no quiere "otra app", y hay alternativas gratis.
  - Un servicio permite cobrar desde la semana 1 y aprender qué formato vende.
- **El producto que sí puede tener ventaja no es "un editor"** (eso ya es commodity), sino **cero intervención**: se conecta al CRM o al feed de avisos de la inmobiliaria y cada propiedad nueva genera su reel y lo publica en su Instagram por la API oficial de Meta.
  - El valor es "no tener que hacer nada", no "editar más fácil".
  - Eso es lo que AutoReel y compañía no hacen para Argentina, en español, ni con Tokko.

### 3.5 ¿Qué vertical conviene? (OPINIÓN)

| | Inmobiliarias | Concesionarias y agencias de usados |
|---|---|---|
| Cantidad | Más: Zonaprop tiene 11.000+ clientes | Menos (sin dato) |
| Rotación del stock | Lenta (semanas a meses) | Más rápida. "Rota todos los meses" es una afirmación del estudio 2026-10-02, no verificada |
| Valor por unidad publicada | Alto, pero la venta tarda | Alto y la venta es más rápida |
| Dolor concreto | Video "lindo de tener" para Instagram | Fotos desparejas + video por unidad para Mercado Libre y Marketplace. Referencia de lo que reemplaza: USD 45-120 por vehículo de edición manual (fuente ⚠) |
| Fuente de datos para automatizar | Tokko u otro CRM, o los portales | Mercado Libre (su API: **no verificada**) o una planilla |
| Competencia local | No encontré | No encontré |

- Mi opinión: **no elegir a ciegas**. El motor es el mismo (fotos + ficha → video), así que **la validación debería probar las dos verticales a la vez**, con 15 contactos cada una, y quedarse con la que responda.
- Si hay que apostar sin datos, me inclino un poco por **agencias de usados**: el dolor de las fotos es más medible y el video es un agregado natural. Es opinión, no dato.

### 3.6 Modelo de negocio y números (ESTIMACIÓN)
- **Costo de producir un video de 30-45 s:**
  - Render en Shotstack a 10-15,6¢/min: ~USD 0,08-0,12.
  - Más texto con Claude y voz IA opcional: centavos.
  - **Menos de USD 0,30 por video.** Con render local (FFmpeg o Remotion en la PC de Facu), casi cero.
- **Precio en Argentina:** USD 15-40/mes por inmobiliaria o agencia, cobrado en pesos. Es la mitad o menos que AutoReel en EE.UU., porque el poder de pago es menor y existen alternativas gratis.
- **Escenario:**
  - 100 clientes × USD 20 = **USD 2.000/mes** recurrentes. Equivale a menos del 1% de los clientes de Zonaprop.
  - Llegar a 100 con venta directa por Instagram y WhatsApp: **6-12 meses** si la oferta pega.
- **Margen bruto:** 85-95%. El costo real es la venta y el soporte.
- **Expansión:** las mismas plantillas sirven para LATAM, España y el mercado hispano de EE.UU.

### 3.7 MVP (ESTIMACIÓN)

| Versión | Qué hace | Quién | Tiempo | Costo |
|---|---|---|---|---|
| **v0, concierge** | La inmobiliaria manda fotos y datos por WhatsApp o formulario; Facu genera el video con una plantilla de Creatomate o Shotstack (o un script que arma Claude Code) y lo devuelve en menos de 24 h | Facu solo | 1-2 semanas | Menos de USD 50 |
| **v1, web** | Sube fotos y datos (o pega su propio enlace), elige plantilla y descarga el video con su marca en 2 minutos | Facu + amigo programador | 4-8 semanas | USD 100-300 (Shotstack USD 39/mes, hosting en Cloudflare casi gratis) |
| **v2, cero intervención** | Integración con el CRM (Tokko vía API o Zapier) y publicación automática en Instagram por la API de Meta | Programador | 2-3 meses más | A definir |

**Factibilidad para Facu (OPINIÓN):**
- Alta en v0 y v1: el estudio anterior verificó que su PC alcanza y que las piezas existen.
- v2 necesita a un programador comprometido.
- **No scrapear las fotos de Zonaprop:** no verifiqué sus términos y conviene asumir que no lo permiten. Que el cliente suba sus propias fotos o conecte su CRM.

### 3.8 Riesgos
- **Los portales o el CRM lo suman gratis.** Zonaprop ya anunció IA para "automatizar la creación de avisos"; Meta lo hace en los anuncios. Es el riesgo más grande: ventana estimada de 12-24 meses, sin dato.
- **Disposición a pagar baja en pesos e inflación:** abonos que se desactualizan y bajas frecuentes.
- **"Nice to have":** no tengo ningún dato verificado de que un video venda más una propiedad o un auto. Las cifras que circulan son de vendedores de herramientas. **Esto es lo primero que hay que validar.**
- **Música con derechos comerciales** (ver estudio 2026-10-02).
- **Soporte:** cada inmobiliaria quiere "su" plantilla.

### 3.9 Cómo validar en 2-4 semanas con menos de USD 200
1. **Semana 1:**
   - Armar 2 plantillas (propiedad y auto) en Creatomate (prueba gratis) o Shotstack (USD 10 de pago único).
   - Lista de 30 inmobiliarias y 30 agencias de usados de una zona, con avisos activos y sin video.
2. **Semanas 1-2:**
   - Contacto por Instagram o visita.
   - **Pedir permiso antes** y ofrecer un video gratis de una unidad suya: "¿te lo armo?". Así se resuelve el uso de sus fotos (táctica del estudio 2026-10-02).
3. **Semanas 2-3:**
   - Ofrecer un mes de "todas tus unidades nuevas con video en menos de 24 h" por un precio en pesos equivalente a USD 15-30, **cobrado por adelantado**.
4. **Semanas 3-4:**
   - Medir si lo publican, si les trae consultas (preguntarles) y si renuevan.

**Gate (propuesto):**
- **≥ 5 clientes pagos** entre las dos verticales y **≥ 3 renuevan** el segundo mes → pasar a v1.
- **Menos de 2 pagos** → cerrar o cambiar de oferta.
- **Costo total:** USD 10-60 más tiempo.

### 3.10 Veredicto L8 (OPINIÓN)

| Criterio | Puntaje | Por qué |
|---|---|---|
| Tamaño del problema | 5 | Muchas unidades publicadas (300.000+ inmuebles en AMBA, 11.000+ inmobiliarias en Zonaprop), pero el video es "lindo de tener" hasta que se demuestre lo contrario |
| Disposición a pagar | 4 | En EE.UU. pagan USD 25-300/mes; en Argentina, sin dato y con quejas por costos de portales |
| Espacio frente a la competencia | 5 | No encontré producto local en español; sí hay alternativas gratis y genéricas |
| Ventaja de Facu | 4 | Español y cercanía; ingeniería industrial para estandarizar el proceso. Sin red en el rubro |
| Factibilidad | 7 | Las piezas existen (APIs de plantilla, Remotion); hay amigos programadores |
| Escalabilidad | 6 | SaaS replicable en LATAM con las mismas plantillas |
| Riesgo (10 = bajo) | 4 | Que los portales lo integren, inflación, bajas |
| **Global** | **5,5/10** | |

**Opinión:**
- Es la más sólida de las tres porque **el formato es repetitivo de verdad** (planilla + fotos → video). Ahí la automatización sí funciona y no hay ninguna plataforma castigando nada.
- Además, el modelo existe y cobra en EE.UU.
- Lo débil: **no sé si en Argentina alguien paga por esto** y los portales pueden regalarlo.
- No la veo como startup grande. Sí como **negocio intermedio de producto**, que enseña algo valioso para la etapa 2: vender software a PyMEs, integrar con sistemas, retener clientes.
- La validación es barata y rápida. Haría esa validación antes que cualquier cosa de clipping.

---

## 4. A3: Visualizador de indumentaria y merchandising personalizado

### 4.1 Qué es
Una página o app donde un cliente ve cómo quedaría una remera, buzo, gorra, taza o banner con su logo o diseño antes de encargarlo. Puede ser simple (mockup 2D), un configurador 3D o una prueba virtual con IA (la prenda "puesta" en una persona).

### 4.2 Parecidos en el mundo (DATOS, consultados 2026-10-08)

| Producto | Qué hace | Precio | Fuente |
|---|---|---|---|
| **Placeit** | Biblioteca enorme de mockups, descargas ilimitadas con licencia comercial | **USD 7,47/mes** | [Placeit](https://placeit.net/pricing) |
| **Printful Mockup Generator** | Mockups de sus productos | **Gratis**, uso comercial permitido, requiere cuenta | [Printful](https://www.printful.com/mockup-generator) |
| **Canva (ex Smartmockups)** | Mockups dentro de Canva | No verificado (la página devolvió 403) | — |
| **Dynamic Mockups** | API de mockups (para meter en una web propia) | Gratis 50 créditos; Pro USD 15-19/mes por 300 renders; **USD 0,051 por render** | [Dynamic Mockups](https://dynamicmockups.com/pricing/) |
| **Zakeke** | Personalizador 2D, vista 3D, realidad aumentada y archivos listos para imprimir | **USD 69,90 / 129,90 / 299,90 por mes + 1,9% / 1,7% / 1,5% por producto vendido**; prueba virtual "desde USD 40" | [Zakeke](https://admin.zakeke.com/en-US/pricing) |
| **Customily** | Personalizador + mockups + archivos de impresión | **USD 49/mes por plataforma + USD 1 a 0,10 por ítem personalizado** según volumen | [Customily](https://www.customily.com/pricing) |
| **FASHN** | Prueba virtual con IA y fotos de moda | USD 19 / 49 / 99 por mes (precio de la API no visible) | [FASHN](https://fashn.ai/pricing) |

**Plataformas donde funcionan:**
- Customily: Shopify, Etsy, Amazon, WooCommerce y Shoplazza. **No menciona Tiendanube.**
- Zakeke: "todas las principales"; nombra Shopify, WooCommerce y Etsy.

### 4.3 Argentina

**DATOS:**
- Tiendanube tiene más de 600 partners tecnológicos en 5 países, y **NubeSDK es obligatorio para apps nuevas desde el 2026-08-30** (estudio 2026-10-01, [Tiendanube Partners](https://www.tiendanube.com/socios/tecnologicos); no re-verificado hoy).
- En la página principal de la tienda de apps de Tiendanube (consultada hoy) **no vi apps de personalización de productos**. Lo más cercano: "CaaS", que recomienda talles y muestra cómo queda una prenda.
- **No pude revisar el catálogo completo:** la búsqueda interna no devolvió resultados legibles. **NO VERIFICADO** que no exista un personalizador.

**NO VERIFICADO:**
- Cuántos talleres de estampado, sublimación, DTF o bordado y cuántas empresas de merch corporativo hay en Argentina.
- Si usan algún visualizador hoy.
- Cuánto pagarían.

**HIPÓTESIS a validar (sin dato):** hoy el flujo típico sería así:
- El cliente manda el logo por WhatsApp o Instagram.
- El taller arma un mockup a mano (Photoshop o Canva) y cotiza.
- Hay varias idas y vueltas.

### 4.4 ¿Dónde estaría el negocio? (OPINIÓN)
- **La imagen sola no es negocio:** Printful la da gratis y Placeit cuesta USD 7,47/mes.
- **El configurador 3D o la prueba virtual con IA** existen, a USD 50-300/mes más comisión. Para un taller argentino es caro, y para merch corporativo (remeras y buzos con logo) la prueba en una persona es más chiche que necesidad.
- **Lo que podría valer:** un **"cotizador visual" para talleres y merch corporativo**:
  - El cliente entra a un enlace (o desde WhatsApp), sube su logo, elige prenda, color, técnica y cantidad.
  - Ve el mockup y recibe **al instante el precio por cantidad y técnica y el plazo**.
  - El taller recibe el pedido con el archivo listo.
- **El aporte de Facu sería la parte de ingeniería:** el costeo por técnica (sublimación vs. serigrafía vs. DTF vs. bordado, costos fijos de preparación, escalas por cantidad), la carga de producción y los plazos. Se conecta con su idea de calculadoras (A2/L9).
- **Variante producto:** **personalizador como app de Tiendanube**, cobrado como Customily (abono + centavos por ítem). Depende de verificar que no exista ya.

### 4.5 Modelo de negocio y números (ESTIMACIÓN)
- **Precio:** USD 10-25/mes por taller en pesos, o un pequeño fee por pedido.
- **Escenario:** 100 talleres × USD 15 = **USD 1.500/mes**. Sin el dato de cuántos talleres hay, **no sé si 100 es el 1% o el 30% del mercado**.
- **Costo de render:** USD 0,05 por mockup (Dynamic Mockups) o casi cero con plantillas propias.
- **Merch corporativo** (empresas que compran 200 buzos con logo): ticket alto por pedido. Ahí el negocio podría ser **intermediar el pedido** (comisión), no vender software. Es otro negocio y no lo investigué.

### 4.6 MVP (ESTIMACIÓN)

| Versión | Qué hace | Quién | Tiempo | Costo |
|---|---|---|---|---|
| **v0, concierge** | Facu, en marca blanca para 2-3 talleres: el cliente del taller manda el logo por WhatsApp y en menos de 10 min recibe mockup + cotización (planilla de costeo + Placeit o plantillas) | Facu solo | 1-2 semanas | Menos de USD 30 |
| **v1, enlace propio** | Página con la API de Dynamic Mockups + cotizador; el taller la comparte por WhatsApp o Instagram | Facu + amigo programador | 4-6 semanas | USD 50-150 |
| **v2, app de Tiendanube** | Personalizador dentro de la tienda | Programador (NubeSDK, homologación) | 3-6 meses | A definir |

### 4.7 Riesgos
- **Demanda desconocida:** el riesgo principal. Ningún dato del mercado argentino.
- **Clientes micro**, con poca disposición a pagar software.
- **Herramientas gratis "suficientes":** Canva, Printful, el Photoshop del diseñador del taller.
- **Propiedad intelectual:** clientes que suben logos de marcas ajenas (camisetas de clubes, marcas deportivas). La herramienta generaría mockups de productos infractores. Conviene tener términos y un filtro.
- **Si se usa prueba virtual con fotos de personas:** datos biométricos (Ley 25.326). Hace falta consentimiento y borrado; ver la idea de retratos corporativos en el estudio 2026-10-02.

### 4.8 Cómo validar en 2-4 semanas con menos de USD 200
1. **Semanas 1-2:**
   - 15-20 entrevistas con talleres de estampado y sublimación y con vendedores de merch corporativo, por Instagram o en persona.
   - Preguntas: cuántas cotizaciones hacen por semana, cuánto tardan, cuántas se pierden, cómo hacen hoy los mockups, qué pagan hoy en software.
2. **Semanas 2-4:**
   - Piloto concierge con 2-3 talleres: Facu les cotiza y hace los mockups en marca blanca, gratis por 2 semanas.
   - Medir cotizaciones atendidas, tiempo de respuesta y conversión (pedidos sobre cotizaciones) contra lo que hacían antes.
3. **Cierre del piloto:**
   - Ofrecer seguir por un precio en pesos equivalente a USD 10-20/mes, **cobrado por adelantado**.

**Gate (propuesto):**
- **≥ 2 de 3 talleres pagan** y la conversión o el tiempo mejoran de forma visible → pasar a v1.
- Si no → cerrar.
- **Costo:** Placeit USD 7,47 + Dynamic Mockups USD 19 → **menos de USD 30** más tiempo.

### 4.9 Veredicto A3 (OPINIÓN)

| Criterio | Puntaje | Por qué |
|---|---|---|
| Tamaño del problema | 4 | La fricción de cotizar y mostrar existe (hipótesis), pero el ticket por taller es chico |
| Disposición a pagar | 3 | Micro talleres; las herramientas que hay cuestan USD 7-300 y muchos usan gratis |
| Espacio frente a la competencia | 4 | Globalmente saturado; posible hueco en Tiendanube y en español (no verificado) |
| Ventaja de Facu | 5 | El costeo y la planificación por técnica son ingeniería industrial pura; es lo único difícil de copiar |
| Factibilidad | 7 | Las APIs de mockup existen y son baratas |
| Escalabilidad | 4 | Mercado chico por cliente; la escala depende de Tiendanube o LATAM |
| Riesgo (10 = bajo) | 6 | Poca plata en juego; el riesgo es que nadie pague |
| **Global** | **4,5/10** | |

**Opinión:**
- Tal como está planteada ("ver cómo queda"), A3 ya está resuelta gratis o casi gratis por Printful, Placeit y Canva.
- Si la idea tiene futuro, es girándola a **"cotizador visual para talleres"**, donde la parte valiosa es el número (precio, plazo, capacidad) y no la foto.
- Ese giro la acerca a lo que Facu sabe hacer (costeo, planificación) y a su idea de calculadoras.
- Hoy no hay ningún dato de que los talleres argentinos paguen por eso. Las entrevistas son obligatorias antes de escribir una línea de código.

---

## 5. Comparación y recomendación (OPINIÓN)

| | L3 clips | L8 video por plantilla | A3 visualizador |
|---|---|---|---|
| Puntaje | 3 | **5,5** | 4,5 |
| ¿Producto que escala? | No (cuentas frágiles) | **Sí** (SaaS replicable) | Parcial |
| ¿Activo propio? | No (el cliente es Whop) | Sí (clientes, plantillas, integración) | Sí, si sale el cotizador |
| ¿Qué enseña para la etapa 2? | Pipelines de video | Vender software a PyMEs, integrar, retener | Costeo, producto vertical |
| Costo de validar | USD 0-60 | USD 10-60 | Menos de USD 30 |

1. **L3:** no la recomiendo como negocio. Si Facu quiere sacarse la duda, 3 semanas con pérdida máxima de USD 60. La variante "agencia de clipping hispana" queda anotada como hipótesis sin investigar.
2. **L8:** la que más vale validar ahora, probando inmobiliarias y agencias de usados a la vez con el mismo motor.
3. **A3:** solo como "cotizador visual", y solo después de 15-20 entrevistas.
4. **L8 y A3 comparten motor:** generar piezas visuales desde datos y plantillas. Si L8 valida, A3 se puede probar después casi sin costo técnico extra.

---

## 6. Pendientes de verificar (la búsqueda se agotó)

- [ ] Cantidad de inmobiliarias, concesionarias oficiales (ACARA) y agencias de usados en Argentina.
- [ ] Cantidad de talleres de estampado, sublimación y bordado y de empresas de merch corporativo en Argentina.
- [ ] Si Mercado Libre Inmuebles, Argenprop, ML Autos o Tokko generan video automático. Si Zonaprop lo tiene en su hoja de ruta de IA.
- [ ] Términos de Zonaprop y ML sobre uso de fotos de avisos. Si la API de ML expone fotos de los avisos propios del vendedor.
- [ ] Qué datos expone la integración de Tokko Broker (API o Zapier).
- [ ] Catálogo completo de apps de Tiendanube: ¿existe un personalizador de productos?
- [ ] Comisión real de Whop para clipperos (7% o 10%) y métodos de cobro concretos para una cuenta argentina.
- [ ] Tarifas actuales de Vyro. Existencia de campañas de clipping de streamers argentinos y de agencias locales.
- [ ] Evidencia independiente (no de vendedores) de que el video aumenta consultas en inmuebles o autos.
- [ ] Precios en dólares de Creatomate (la página no los mostró) y de la API de FASHN.

---

## 7. Fuentes (consultadas el 2026-10-08 salvo indicación)

**L3: clipping**
- Whop, documentación de Content Rewards: https://docs.whop.com/manage-your-business/growth-marketing/content-rewards
- Whop, configuración de pagos (más de 200 países, Argentina incluida, mínimo USD 10): https://docs.whop.com/manage-your-business/manage-payouts/set-up-payouts.md
- ClipSpeed ⚠ (2026-09-13), comisión del 10% y retención de 10 días: https://www.clipspeed.ai/blog/whop-content-rewards-clipping-guide.html
- Ascynd (2026-07-24), datos de Clippa (USD 2,58 M, 8.466 personas, USD 0,39/1.000): https://ascynd.io/en/blog/whop-clipping
- Virlo ⚠ (sin fecha), "USD 1,7 M a 98.000 creadores": https://virlo.ai/blog/ultimate-guide-to-clip-farming-for-creators
- Ssemble ⚠ (2025-09-30), "la mayoría gana menos de USD 3": https://www.ssemble.com/es/blog/clipping-monetization-strategies-in-2026
- Ssemble ⚠, Clip Rewards en español: https://www.ssemble.com/es/clip-rewards
- Ssemble ⚠, reseña de Vyro: https://www.ssemble.com/pl/blog/vyro-review-2026
- ClipAffiliates ⚠, reseña de Vyro: https://www.clipaffiliates.com/blog/vyro-review
- FindClout ⚠, quejas sobre Content Rewards: https://findclout.com/blog/content-rewards-complaints
- FindClout ⚠, ClipFarm: https://findclout.com/blog/airrack-clipfarm
- ContentRewards, ClipFarm: https://contentrewards.com/clipfarm
- ContentRewards, campaña en español: https://www.contentrewards.com/campaigns/ebc7dd27-5d08-4d06-86d5-659706286077
- OpusClip ⚠ (2026-08-12), agencias de clipping: https://www.opus.pro/blog/best-clipping-agencies
- OpenClip ⚠, cuánto ganan los clipperos: https://openclip.app/guides/how-much-do-clippers-make
- Apify, scraper de campañas de Whop (83 usuarios): https://apify.com/fayoussef/whop-clipping-campaigns-scraper
- La República (2025-09-10), streamers peruanos que pagan a clipperos: https://larepublica.pe/streamers/2025/09/10/streamer-sacha-revela-las-jugosas-ganancias-de-sus-cliperos-8-sueldos-minimos-no-es-broma-evat-769400

**L3: plataformas, políticas, APIs y herramientas**
- Instagram for Creators (2026-04-30), contenido original: https://creators.instagram.com/blog/rewarding-original-creators-on-instagram
- Android Headlines (2026-10-02), YouTube suprime los Shorts re-subidos: https://www.androidheadlines.com/2026/10/youtube-cuts-reach-reuploaded-shorts-originality-push.html
- OutlierKit, cambios de YouTube de julio de 2026: https://outlierkit.com/blog/youtube-updates-july-2026
- BigSeller, TikTok y el contenido no original (desde el 2025-09-15): https://www.bigseller.pro/blog/articleDetails/3778/tiktok-unoriginal-content.htm
- TikTok for Developers, pautas de publicación por API: https://developers.tiktok.com/doc/content-sharing-guidelines
- TikTok for Developers, referencia de Direct Post: https://developers.tiktok.com/doc/content-posting-api-reference-direct-post
- Meta, publicación de contenido en Instagram por API: https://developers.facebook.com/docs/instagram-platform/content-publishing
- Shortimize ⚠, multi-cuenta en TikTok: https://www.shortimize.com/blog/how-to-manage-multiple-tiktok-accounts-2
- Castmagic ⚠ (verificado 2026-08-20), precios de OpusClip: https://www.castmagic.io/blog/opus-clip-pricing
- Klap ⚠, reseña de Vizard: https://klap.app/blog/vizard-ai-review
- Kompozy (2026-05-29), Klap vs. Vizard: https://kompozy.io/compare/klap-vs-vizard
- Morphed ⚠, alternativas a Vizard: https://morphed.app/blog/vizard-alternatives
- Caplight (abril de 2026), OpusClip: https://www.caplight.com/company/opusclip
- Getlatka (estimación), ingresos de OpusClip: https://getlatka.com/companies/opus.pro/team

**L8: video por plantilla**
- AutoReel ⚠, FAQ de precios: https://www.autoreelapp.com/faq/cost-effective-realtor-tools/how-much-does-autoreel-cost-per-month-for-individual-real-estate-agents
- AutoReel ⚠ (2026-08-13), AutoReel vs. Reel-E: https://www.autoreelapp.com/compare/autoreel-vs-reel-e
- Capterra, Reeltors.ai: https://www.capterra.com/p/10045003/Reeltors-ai/
- Capterra, Reel-E: https://www.capterra.com/p/10037342/Reel-E/
- Spyne, precios (no publicados): https://www.spyne.ai/pricing
- Shotstack, precios: https://shotstack.io/pricing/
- Creatomate, precios: https://creatomate.com/pricing
- Plainly, precios: https://www.plainlyvideos.com/pricing
- Bannerbear, precios: https://www.bannerbear.com/pricing/
- Mercado (2026-05-27), Zonaprop con más de 11.000 clientes: https://mercado.com.ar/ruta-digital/zonaprop-amplio-su-base-a-mas-de-11-000-clientes-en-una-decada
- CUCICBA (entrada del 2026-01-09), más de 300.000 inmuebles en venta en AMBA: https://www.cucicba.com.ar/
- iProfesional (2024-05-08), inmobiliarias contra las subas de Zonaprop: https://www.iprofesional.com/economia/405449-inmobiliarias-en-alerta-denuncian-a-zonaprop-por-aumentos-abusivos
- ComparaSoftware, Tokko Broker: https://www.comparasoftware.com/tokko-broker
- Zapier, Tokko Broker: https://zapier.com/find-apps/t/tokko-broker
- Del estudio 2026-10-02 (no re-verificadas hoy): Photoroom ⚠ (costo por vehículo), GetApp CarPixAI, licencia de Remotion.

**A3: visualizador de merch**
- Placeit, precios: https://placeit.net/pricing
- Printful, generador de mockups: https://www.printful.com/mockup-generator
- Dynamic Mockups, precios: https://dynamicmockups.com/pricing/
- Zakeke, precios: https://admin.zakeke.com/en-US/pricing
- Customily, precios: https://www.customily.com/pricing
- FASHN, precios: https://fashn.ai/pricing
- Tienda de apps de Tiendanube (página principal): https://www.tiendanube.com/tienda-aplicaciones-nube
- Del estudio 2026-10-01 (no re-verificada hoy): Tiendanube Partners, https://www.tiendanube.com/socios/tecnologicos
