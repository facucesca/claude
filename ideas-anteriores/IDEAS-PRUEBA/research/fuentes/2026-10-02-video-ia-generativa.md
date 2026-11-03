# Video (y foto) con IA generativa como servicio para negocios: herramientas, demanda, reglas y 28 ideas

**Fecha:** 2026-10-02
**Frente:** creación de video y foto con IA generativa vendida a negocios (B2B), con marca anónima y captación por email frío.
**Perfil considerado:** argentino; **no programa** (Claude Code le arma herramientas); capital < USD 500; tiene **Higgsfield** conectado; formación en ingeniería industrial; busca ángulos poco quemados, de ticket alto y con recurrencia.
**Relación con informes previos:** complementa el frente E de `research/2026-10-01-230-ideas-con-claude.md` (E1-E38) y los frentes H, I y L de `research/2026-10-01-200-ideas-rapidas-1-semana.md`. **No repite** esas ideas: cuando retoma una (E1, E4, E7, E11, E16, E21, E36), lo dice y aporta el ángulo nuevo (nicho, precio o método).

---

## 0. Metodología

- **Consultas:** 46 en total, todas del 2026-10-02: 31 con WebSearch (la cuota de la sesión se agotó en la consulta 32) y 15 lecturas con WebFetch de páginas primarias (precios de Luma, Synthesia, Hedra, Pika y Kling; ayuda de Google Business Profile; texto del proyecto de ley S8420A del Senado de Nueva York; el blog y la ayuda de Higgsfield; la página de GitHub de Wan; el análisis del art. 50 del AI Act publicado por ICTRecht; Wikipedia sobre Suno y Udio). DuckDuckGo devolvió un CAPTCHA (**no se intentó resolverlo**), y Bing/Google no devolvieron resultados útiles. Por eso varias ideas de nicho quedan **[NO VERIFICADO]**: son hipótesis razonadas, no datos.
- **Conflictos de interés:** casi toda la literatura de precios y "rendimiento de anuncios IA" la publican **vendedores de herramientas**: Creatify (compite con Higgsfield), Motionbox, VO3 AI, AutoReel, Segwise, Cinerads, Novoads, Adwave, el blog de Higgsfield y el de Kling. Se marcan con **⚠**. Sus cifras sirven como techo, no como mediana.
- **Score 1-10:** pensado para ESTE usuario. Pondera los 7 criterios del `CLAUDE.md`. Para servicios activos, "automatización" se mide como potencial de productizarse, no como castigo. Pesa más lo que el usuario puede hacer sin programar, vender por email frío con marca anónima y cobrar desde Argentina.
- **Costos:** se convierten a USD por segundo de video **generado** (no final). Supuesto de producción: entre 3 y 5 generaciones por clip útil. Un anuncio de 30 s requiere generar 90-150 s.

---

## 1. Hallazgo que cambia el tablero: **Sora ya no existe**

- OpenAI anunció el cierre de Sora el **2026-03-24**: la app y la web cerraron el **2026-04-26** y la API el **2026-09-24**. Motivo declarado: volcar cómputo a herramientas de código y a clientes enterprise ([The Decoder, 2026-03-28](https://the-decoder.com/openai-sets-two-stage-sora-shutdown-with-app-closing-april-2026-and-api-following-in-september/); [invideo ⚠, 2026-08](https://invideo.io/blog/ai-video-model-pricing)).
- **Consecuencias:** (1) la pregunta "¿Sora está disponible en Argentina?" ya no aplica; (2) la tabla de modelos de Higgsfield todavía mostraba Sora 2 el 2026-09-14 ([Krea ⚠](https://www.krea.ai/blog/what-is-higgsfield-ai-pricing-free-plan-and-alternatives-in-2026)), pero después del 2026-09-24 ya no debería funcionar **[NO VERIFICADO en la app]**; (3) es la **prueba más clara del riesgo de plataforma**: un modelo de primera línea desapareció en 7 meses. Todo el negocio tiene que poder cambiar de modelo sin rehacer el método.

---

## 2. Estado de las herramientas (2026-10-02)

### 2.1 Video generativo

| Herramienta | Precio (fuente, fecha) | Costo aprox. por segundo generado | Audio nativo / duración máx. | Licencia comercial | Nota |
|---|---|---|---|---|---|
| **Google Veo 3.1** (API Gemini) | Estándar USD 0,40/s (720p y 1080p), 0,60/s en 4K; Fast USD 0,10-0,12/s (0,30 en 4K); Lite USD 0,05 (720p) - 0,08 (1080p) ([invideo ⚠, 2026-08](https://invideo.io/blog/ai-video-model-pricing); [BenchLM, 2026-09](https://benchlm.ai/media-pricing/veo)) | 0,05 - 0,60 | Sí, siempre incluido / 8 s por clip | Sí (API paga) | Referencia de calidad. Por consumidor: Google AI Pro £18,99 por mes con 1.000 créditos de Flow ([DIYAI ⚠](https://diyai.io/ai-tools/video-generation/google-veo-pricing/)) |
| **OpenAI Sora 2** | Era USD 0,10/s (720p); Pro USD 0,30-0,50/s | — | — | — | **Discontinuado** (app el 2026-04-26, API el 2026-09-24) |
| **Kling 3.0** (directo) | Standard USD 6,99-8,80 por mes (660 créditos); Pro USD 25,99 (3.000); Premier USD 64,99 (8.000); Ultra USD 127,99 (26.000) ([Kling, guía oficial ⚠](https://kling.ai/blog/kling-video-3-0-credit-cost-guide)). 15 s en 1080p con audio = 180 créditos; en modo Pro con audio = 870 créditos ([búsqueda que cita a Kling](https://home.kling.ai/blog/kling-video-3-0-credit-cost-guide)) | 0,06 - 0,58 (las fuentes no coinciden: Creatify ⚠ calcula 0,37 en 1080p con audio) | Sí / 3-15 s, multi-toma ("AI Director"), 4K nativo | Desde Standard; el plan gratis no permite uso comercial y deja marca de agua | Hasta 20% de créditos se acumulan al mes siguiente |
| **Seedance 2.0 / 2.5** (ByteDance) | En Higgsfield: 45 créditos por 5 s en 1080p; en Luma: 126 créditos por segundo | 0,30 - 0,39 | Sí | Según la plataforma que lo revende | Mejor rankeado con audio según Creatify ⚠. **Disney (2026-02-13) y la MPA (2026-02-20) le enviaron cartas documento** por infracción de derechos de autor ([Axios](https://www.axios.com/2026/02/20/hollywood-seedance-intellectual-property)): nunca generar personajes ni celebridades |
| **Runway Gen-4.5 / Aleph 2.0** | Gen-4.5 = 12 créditos/s; Aleph 2.0 (edición de video) = 28 créditos/s; Standard: 625 créditos por mes ([Creatify ⚠, verificado 2026-08](https://creatify.ai/blog/runway-pricing-(2026)-plans-credits-and-what-you-ll-actually-pay)) | Gen-4.5 ≈ 0,12-0,29; Aleph ≈ 0,28-0,67 (precio del crédito **[NO VERIFICADO]**) | — | Plan pago | Aleph sirve para **editar material real del cliente** (cambiar el fondo, el clima o un objeto), no solo para generar |
| **Luma** (Ray3.14 / Ray3.2 + modelos de terceros) | Plus USD 30 por mes (10.000 créditos), Pro USD 90 (40.000), Ultra USD 300 (150.000) ([lumalabs.ai/pricing, 2026-10-02](https://lumalabs.ai/pricing)) | Ray3.14 en 1080p = 80 créditos/s ≈ 0,24; Kling Omni = 49 créditos/s ≈ 0,15 | Según el modelo | **Todos los planes pagos** | Agregador como Higgsfield (Seedance, Kling, Veo, MiniMax, Flux 3) |
| **MiniMax / Hailuo H3** | USD 0,13/s en 2K, audio estéreo ([invideo ⚠](https://invideo.io/blog/ai-video-model-pricing)) | 0,13 | Sí | API paga | — |
| **Pika** | Starter USD 10, Creator USD 35 (3.150 créditos), Fancy USD 95 ([pika.art/pricing, 2026-10-02](https://pika.art/pricing)) | — | — | **Solo desde Creator** | Hoy es un agregador (Seedance 2.5, Wan 3.0, MiniMax H3) |
| **Wan** (Alibaba) | Wan 2.1 y 2.2: open source, Apache-2.0, actualizados hasta 2026-09-21 ([GitHub Wan-Video](https://github.com/Wan-Video)). Wan 3.0 aparece en Pika, sin repositorio abierto | ~0 + GPU propia | — | Apache-2.0 (2.x) | **No sirve para este usuario**: requiere GPU y montaje técnico |
| **Higgsfield** | Starter USD 19 (270 créditos); Plus USD 59 por mes o 47 anual (1.200); Ultra USD 129 por mes o 99 anual (3.000) ([Creatify ⚠, 2026-09-04](https://creatify.ai/blog/higgsfield-vs-kling-ai-quality-cost-per-second-and-which-to-use-for-ads-in-2026); [Kive, actualizado 2026-10-01](https://kive.ai/learn/is-higgsfield-worth-it)) | Kling 3.0 a 720p: 7 créditos por 5 s ≈ **0,05-0,06**; Veo 3.1: 29 créditos por 4 s ≈ 0,24-0,31; Seedance 2.0 en 1080p ≈ 0,30-0,39. Blog propio: "~USD 2 por clip de 8 s a 720p" ⚠ | Según el modelo; Marketing Studio: **máximo 15 s por generación** | Solo planes pagos | Ver 2.4 |

### 2.2 Avatares, voz y música

| Herramienta | Precio | Costo útil | Licencia / riesgo |
|---|---|---|---|
| **HeyGen** | Creator USD 29 (600 créditos); Business USD 149 (1.500), suma SCORM y LMS ([Creatify ⚠](https://creatify.ai/blog/heygen-pricing-(2026)-plans-and-what-you-ll-actually-pay)) | Avatar IV/V: 20 créditos por minuto ≈ USD 1 por minuto; traducción con lip-sync: 5 créditos por minuto ≈ USD 0,25 por minuto | Comercial en planes pagos |
| **Synthesia** | Starter USD 29 (~12 min por mes); Pro USD 89 (~60 min, 5 avatares personales) ([synthesia.io, 2026-10-02](https://www.synthesia.io/pricing)) | ≈ USD 1,5-2,4 por minuto | El plan gratis deja marca de agua |
| **Hedra** | USD 20 / 50 / 100 por mes ([hedra.com, 2026-10-02](https://www.hedra.com/pricing)) | — | Comercial en todos los planes pagos |
| **Captions** | **[NO VERIFICADO]** | — | — |
| **ElevenLabs** | Starter USD 6 (incluye uso comercial); Creator USD 22 (clonación profesional de voz); Pro USD 99. Eleven Music = 900 créditos por minuto ([Smallest.ai ⚠](https://smallest.ai/blog/elevenlabs-pricing-plans-cost-what-you-get-in-2026)) | Locución de 30 s ≈ centavos | El plan gratis no permite uso comercial |
| **Suno** | Lanzó **v6 en 2026-09**, "desarrollado con" Warner (acuerdo del 2025-11-25), BMG (2026-08-12) y Believe (2026-09-08) ([Wikipedia](https://en.wikipedia.org/wiki/Suno_AI); [Pillitteri](https://pasqualepillitteri.it/es/news/17674/suno-v6-licencia-warner-bmg-believe)) | — | Lo creado en cuentas gratis no puede usarse comercialmente. **Siguen los juicios de UMG y Sony** por los datos de entrenamiento: riesgo medio para jingles de marca |
| **Udio** | Acuerdo con UMG en **2025-10**; pasó a un modelo de streaming cerrado y dio 48 h para descargar lo creado ([Wikipedia](https://en.wikipedia.org/wiki/Udio)) | — | **No sirve para entregables a clientes** mientras no permita descargas [estado 2026 NO VERIFICADO] |

### 2.3 Imagen

| Modelo | Precio por imagen | Fuente |
|---|---|---|
| Nano Banana Pro (Gemini 3 Pro Image) | USD 0,134 (1K-2K), 0,24 (4K); 50% menos en batch | [búsqueda que cita la API oficial, 2026](https://www.myarchitectai.com/blog/nano-banana-api-pricing) |
| GPT Image 2 | Desde USD 0,006 (1024 px, calidad baja); se cobra por tokens | [OpenRouter](https://openrouter.ai/compare/black-forest-labs/flux.2-max/openai/gpt-image-2) |
| FLUX.2 Max / Klein 4B | USD 0,07 / 0,014 por megapíxel | OpenRouter |
| Ideogram | [NO VERIFICADO] | — |

**Conclusión de costos:** la imagen cuesta prácticamente cero. El costo real del video está en los **reintentos** y en las **horas humanas**, no en los créditos.

### 2.4 Higgsfield: lo que tiene de propio (y sus problemas)

- **Agrega modelos** (Seedance 2.5/2.0/1.5/Pro, Kling 3.0/2.6/2.5/2.1/Omni, Veo 3/3.1 y, hasta su cierre, Sora 2) bajo una sola billetera de créditos ([Krea ⚠, tabla del 2026-09-14](https://www.krea.ai/blog/what-is-higgsfield-ai-pricing-free-plan-and-alternatives-in-2026)).
- **Marketing Studio** (ayuda oficial, modificada el 2026-09-01): recibe una URL, la web o fotos del producto, y extrae nombre, descripción, hasta 8 fotos, colores y logo. Formatos: Product Shots, Ads con medidas de Meta y Google, Marketplace, Posters, **UGC Videos** (sin cara, cabeza parlante o mudo), **Motion** (Hypermotion, 2D Product Motion, Motion Design para software) y Ref→Video. Audio y lip-sync nativos; **máximo 15 s por generación**. "Todavía no disponible por MCP" ([Higgsfield Help](https://higgsfield.ai/creator-hub/help-center/tools/how-do-i-use-marketing-studio-to-create-video-ads)). **Importante:** el MCP que tiene conectado el usuario **no** maneja Marketing Studio; eso se hace en la web.
- **Soul ID:** se entrena con 20 o más fotos de referencia y mantiene la misma cara en todas las variantes. **Ad Reference** recrea el concepto y el ritmo de un anuncio existente. **Virality Predictor** pronostica rendimiento (dato propio, sin validación externa). El flujo de "100 anuncios por mes" que propone su blog cuesta unos USD 200 en créditos ([Higgsfield ⚠, 2026-08-28](https://higgsfield.ai/blog/make-100-creative-ads)).
- **Problemas documentados:** los créditos no se acumulan de un mes al otro; los modos "ilimitados" funcionan **solo en la web**, no por MCP/CLI, y está **prohibido automatizar o compartir credenciales** ([Kive](https://kive.ai/learn/is-higgsfield-worth-it)). Hay quejas recurrentes por renovación anual automática y reembolsos negados (las responde la propia Higgsfield en [geo.higgsfield.ai ⚠](https://geo.higgsfield.ai/blog/higgsfield-ai-billing-controversy-explained)). Hubo un escándalo de reputación a comienzos de 2026 por material promocional con contenido racista y sexista ([Times of Central Asia](https://timesca.com/kazakh-startup-higgsfield-ai-from-unicorn-to-racism-and-sexism-scandal/)). **Recomendación:** no mencionar "hecho con Higgsfield" ante clientes, revisar en qué ciclo de facturación está el usuario y no poner un plan anual en piloto automático.

### 2.5 Costo estimado de producción (compute + horas)

| Entregable | Generación | Compute | Horas humanas (con método) |
|---|---|---|---|
| Anuncio de producto de 15 s desde fotos (Marketing Studio / Kling) | 3 clips × 3-4 intentos × 5 s ≈ 45-60 s | **USD 3-15** | 1,5-3 h (guion, curaduría, subtítulos, formatos) |
| Anuncio de 30 s "tipo TV", multi-escena (Veo 3.1 / Seedance / Kling) | 90-150 s | **USD 15-60** + voz/música USD 1-5 | 6-12 h |
| Video explicativo de producto industrial de 60 s (animar fotos reales + motion + locución) | 120-200 s | USD 20-80 | 10-20 h |
| Pack mensual de 10 conceptos × 3 variantes (30 piezas) | ~600-900 s | USD 60-250 | 20-30 h |
| Video con avatar de 3 min (capacitación) | — | USD 3-7 | 4-8 h (guion, revisión técnica) |
| **Stack base mensual:** Higgsfield Plus (59) o Ultra (129) + ElevenLabs Creator (22) + Suno pago + editor | — | **USD 100-170 por mes** | — |

Referencias externas: la producción de un comercial de 60 s se estima en USD 72 de compute y USD 229,80 de costo total ([Adwave ⚠](https://adwave.com/resources/ai-tv-commercial-production)). El anuncio de Kalshi para las finales de la NBA (2025) se hizo en unos 2 días con alrededor de USD 2.000 ([DesignRush](https://news.designrush.com/kalshi-nba-finals-ai-ad-why-big-budget-commercials-are-dying), sin acceso al texto completo).

---

## 3. Qué compran realmente los negocios (con evidencia)

### 3.1 Señales de demanda
- **Upwork:** "generación y edición de video con IA" fue la categoría que más creció en 2025: **+329% interanual**, medido sobre ganancias de freelancers en el marketplace de EE.UU. entre enero y diciembre de 2025 ([Upwork In-Demand Skills 2026, vía SelfEmployed, 2026-02](https://www.selfemployed.com/news/upwork-ai-freelance-skills-demand-2026/)).
- **Meta Andromeda:** el sistema agrupa anuncios conceptualmente parecidos (lo que la industria llama "Entity ID") y los hace competir entre sí. Cambiar un color o una palabra **no** crea un anuncio nuevo. La recomendación de 2026 es **8-12 conceptos realmente distintos por campaña** y 2-3 variantes de cada uno ([Segwise ⚠](https://segwise.ai/blog/meta-andromeda-update-creative-strategy-2026); [Atria ⚠](https://www.tryatria.com/blog/andromeda-meta-ads)). El dato de que Meta "confirmó un umbral de similitud del 60%" viene de fuentes secundarias **[NO VERIFICADO en Meta]**. **Lectura:** la demanda no es de "volumen de clips", es de **diversidad de conceptos**. Eso pide estrategia creativa, no créditos, y ahí está la ventaja del operador con método.
- **Lo que hace Meta por su cuenta:** desde Cannes 2025, Advantage+ convierte hasta 20 fotos de producto en un video de varias escenas; en la beta dio en promedio +10% de CTR y +8% de CVR (dato de Meta). En **2026-03** sumó doblaje IA con lip-sync en la voz del anunciante, fondos IA y música IA ([resumen de búsqueda: Campaign Asia, PPC Land, ContentGrip](https://www.campaignasia.com/article/meta-expands-advantage-with-gen-ai-ad-creativity-tools-for-advertisers/503131)). El WSJ (2025-06) informó que Meta apunta a **automatizar la creación de anuncios de punta a punta para fines de 2026** ([Exchange4media](https://www.exchange4media.com/digital-news/meta-aims-to-fully-automate-advertising-with-ai-by-2026-144037.html)). **Lectura:** el video simple de producto a partir de fotos **se vuelve gratis dentro de Meta**. No conviene venderlo como servicio principal.
- **Otras herramientas gratuitas o casi:** Google Pomelli (gratis en beta) y Adwave (comercial de TV generado desde la web en minutos, gratis). Los videos inmobiliarios IA cuestan **unos USD 10 por propiedad** contra USD 300-1.500 de un videógrafo ([AutoReel ⚠, 2026](https://www.autoreelapp.com/blog/real-estate-video-production-cost-in-2026)).

### 3.2 Precios de mercado (techo, no mediana)
| Qué | Precio | Fuente |
|---|---|---|
| Anuncio UGC IA "en bruto" (9:16) | USD 150-350 | [Motionbox ⚠, 2026-08-05](https://motionbox.io/blog/how-much-to-charge-clients-for-ai-ugc-ads) |
| Anuncio UGC IA terminado (subtítulos, placa final, 2 formatos) | USD 250-600 | ídem |
| Pack de 5 anuncios (1 concepto, 5 hooks) / 10 anuncios (3 conceptos) | USD 1.250 / 2.800 | ídem |
| Abono de 12 anuncios por mes | USD 2.500-8.000 | ídem |
| Recargo por derechos de pauta (90 días) / whitelisting (12 meses) | +40% / +100% | ídem |
| UGC en Fiverr (humano o IA) | USD 100-500 por video; Fiverr se queda con 20% | [Unilink ⚠](https://www.unilink.us/blog/best-fiverr-gigs-2026) |
| UGC IA en Upwork | USD 250-5.000 por proyecto; USD 15-80 por hora; Upwork cobra 10% | [UGC Copilot ⚠](https://ugccopilot.ai/blog/ai-ugc-video-creator-software-vs-freelancer-2026/) |
| "Comercial IA" de 30 s | ReelForge USD 500; Contra (freelancer) USD 750; 60 s + 3 cortes USD 1.200; campaña de 4 videos USD 2.500 | [resumen de búsqueda](https://contra.com/s/vArONZ7b-ai-commercial-video-creation), 2026 |
| Comercial IA de estudio | "10-20% del costo tradicional"; cotización a medida | [Animatic Media](https://www.animaticmedia.com/ai-commercials) |
| Comercial tradicional | USD 5.000-50.000 por spot | Adwave ⚠ |
| Video inmobiliario | Videógrafo USD 300-1.500; herramienta IA ~USD 10 | AutoReel ⚠ |

### 3.3 Lo que dice el público (y por qué importa para elegir el nicho)
- **EE.UU., encuesta Bentley-Gallup del 2026-05-04 al 11:** el **49%** ve negativamente que las empresas usen IA en publicidad; el **62%** considera inaceptables las **personas o voces generadas por IA aun con aviso**; entre jóvenes de 18-29 años la mirada negativa llega al 66%. El 79% vio anuncios IA en los últimos 30 días ([FingerLakes1, 2026-08-20](https://www.fingerlakes1.com/2026/08/20/new-york-businesses-face-a-trust-problem-as-consumers-sour-on-ai-generated-advertising/)).
- **EMEA, DoubleVerify (2026-08-06):** el 42% reacciona mal a anuncios IA de baja calidad, pero en el Reino Unido **solo el 29% reacciona mal cuando el anuncio IA se ve pulido y profesional** ([Advanced Television](https://www.advanced-television.com/2026/08/06/study-ai-slop-poses-growing-risk-to-brand-trust/)).
- **Australia, YouGov (2026-05):** el 45% confiaría menos en una marca si descubre que sus anuncios son IA ([AdNews](https://www.adnews.com.au/news/many-australians-lose-brand-trust-when-they-know-they-are-seeing-ai-generated-ads)).
- **Rendimiento de "AI UGC" contra UGC real:** los artículos que hablan de "paridad para productos de menos de USD 100" son todos de vendedores (inBeat, AdCreate, Segwise) **[NO VERIFICADO de forma independiente]**.
- **Implicancia de diseño:** conviene **evitar humanos sintéticos que se hacen pasar por reales**. La IA rinde mejor en **producto, mundo, animación, mascotas, explicativos y edición de material real**, con terminación profesional. Eso define los nichos de la sección 5.

---

## 4. Reglas y riesgos (vigentes al 2026-10-02)

| Regla | Qué exige | Fuente |
|---|---|---|
| **Meta, etiqueta "AI info"** | Se aplica sola si se usan las herramientas generativas de Meta o si el archivo trae C2PA; si no, el anunciante tiene que declarar a mano el contenido sintético fotorrealista. Según una fuente secundaria, "IA no declarada" es el 14% de los rechazos de anuncios **[NO VERIFICADO]** | [Cinerads ⚠](https://www.cinerads.com/blog/ai-ad-disclosure-requirements); [Storrito](https://storrito.com/resources/meta-rejects-14-percent-of-ads-for-undisclosed-ai-content/) |
| **TikTok, desde el 2026-07-21** | Etiqueta de IA obligatoria en Ads Manager **antes de que corra el anuncio** si hay voces clonadas, visuales IA realistas, producto fotorrealista IA o voceros sintéticos. Sanciones escalonadas: advertencia → 7 días → 30 días → **baneo permanente** | [Stellar Search, 2026-08-12](https://www.stellarsearch.co.uk/insight/tiktoks-ai-ad-disclosure-rules-are-live-what-brands-running-ai-creative-need-to-do-now) |
| **YouTube** | Interruptor de "contenido alterado" cuando algo podría confundirse con real. Desde 2025-07-15 rige además la regla de contenido inauténtico | Cinerads ⚠; informe 2026-10-01 |
| **EU AI Act, art. 50** | **Vigente desde el 2026-08-02** (el Digital Omnibus no lo postergó). Etiquetar deepfakes, lo que incluye **productos, lugares u objetos** que parezcan auténticos. Un aviso comercial con elementos ficticios **no** queda exento automáticamente como "obra artística". El marcado legible por máquina tiene transición hasta el **2026-12-02** para sistemas lanzados antes. Multas de hasta EUR 15 M o 3% de la facturación | [ICTRecht, 2026-08-03](https://www.ictrecht.nl/en/blog/heads-up-ai-act-transparency-obligations-now-in-effect) |
| **Nueva York, S8420A** | Aviso visible obligatorio cuando un anuncio usa "intérpretes sintéticos". USD 1.000 la primera infracción y 5.000 las siguientes. Firmada el 2025-12-11, **vigente desde ~2026-06-09** | [NY Senate](https://www.nysenate.gov/legislation/bills/2025/S8420/amendment/A) |
| **FTC** | Regla de reseñas falsas vigente desde el 2024-10-21: prohíbe **testimonios de personas inexistentes, incluidos los generados por IA**. Se habla de las primeras multas (2026-04, USD 27,4 M) en una fuente secundaria **[NO VERIFICADO]** | [Search Engine Land](https://searchengineland.com/ftc-fake-reviews-testimonials-445209) |
| **California, AB 723 (inmobiliario)** | Desde el **2026-01-01**, las imágenes alteradas (staging virtual, reemplazo de cielo) llevan aviso y link a la original. Multas, sanción a la matrícula y posible vía penal | [Inman, 2026-01-23](https://www.inman.com/2026/01/23/what-you-should-know-about-californias-new-listing-photo-law/) |
| **Google Business Profile** | Las fotos deben estar "sin alteraciones significativas ni uso excesivo de filtros o IA" y "representar la realidad" | [Google Help, 2026-10-02](https://support.google.com/business/answer/6123536) |
| **Argentina** | Derecho a la imagen (CCyC art. 53): hace falta consentimiento para captar o reproducir la imagen o la voz de una persona. Hay **proyectos de ley** (no sancionados al 2026-10-02 **[verificar estado]**) de etiquetado obligatorio de contenido IA y prohibición de deepfakes en publicidad ([HCDN](https://rest.hcdn.gob.ar/web/proyectos/290925/adjuntos/105159); [Diario Constitucional, 2025-10-22](https://www.diarioconstitucional.cl/2025/10/22/proyecto-de-ley-busca-crear-una-accion-de-amparo-especial-para-proteger-el-derecho-a-la-imagen-contra-el-uso-indebido-de-ia-especialmente-en-casos-de-deepfakes/)). La publicidad engañosa está regulada por lealtad comercial **[NO VERIFICADO el texto vigente]** | — |
| **Propiedad intelectual** | Seedance 2.0 recibió cartas documento de Disney y la MPA (2026-02). La música IA tiene juicios abiertos (UMG y Sony contra Suno). El material puramente generado por IA no es registrable en EE.UU. según la Copyright Office, que lo dice en su informe de 2025-01 [cita de memoria, **NO VERIFICADO** hoy]: **el cliente no "es dueño" en sentido fuerte de un personaje 100% IA** | Axios; Wikipedia |

**Riesgos de mercado:**
1. **Deflación:** Meta, Google (Pomelli), Adwave y las herramientas inmobiliarias regalan el video básico.
2. **Rechazo del público** a los humanos sintéticos.
3. **Riesgo de plataforma:** el caso Sora, las condiciones de Higgsfield y los modelos que cambian cada 3-6 meses.
4. **Email frío con marca anónima:** sin cara ni casos, la confianza se gana **mostrando una pieza hecha con el producto del prospecto** ("spec ad" privado, que no se publica).

---

## 5. Dónde gana un operador con método frente a "cualquiera con una suscripción"

1. **Diversidad de conceptos, no de clips.** Andromeda castiga lo parecido. Vender una **matriz de conceptos**: ángulo × emoción × formato × gancho, cada concepto con su hipótesis y una regla de "cortar o escalar" leída de los datos del cliente. Es método de experimentos (DOE), el terreno de un ingeniero industrial.
2. **Material real + IA.** Partir de fotos y videos reales del cliente (producto, obra, planta, equipo) y usar la IA para animar, ambientar, editar (Aleph) y versionar. Baja el rechazo, el riesgo legal (art. 50, AB 723, GBP) y las alucinaciones.
3. **Nichos B2B "aburridos" con ticket y calendario:** industria, agro-maquinaria, desarrolladoras, ferias, capacitación, SaaS. Tienen decisores identificables, sirven para email frío y casi no les llegan agencias de "AI UGC".
4. **Consistencia de marca como activo:** una biblia de personaje o de estilo, con referencias, paleta, prompts y Soul ID, que se mantiene mes a mes. Eso es lo que justifica el abono.
5. **Cumplimiento incluido:** archivos entregados con etiqueta y C2PA, una planilla de qué lleva aviso en cada plataforma y un contrato con cláusula de derechos. Para clientes de la UE y de Nueva York es un diferencial vendible.
6. **Independencia de modelo:** el método y la biblia sobreviven aunque el modelo de turno cierre, como pasó con Sora.

---

## 6. Ideas (28)

**Leyenda.** Saturación: B = baja, M = media, A = alta. Riesgo legal y de política: B/M/A. Rec. = hay recurrencia. Anón. = funciona con marca anónima. Margen = (precio − compute − herramientas prorrateadas) / precio, **sin contar las horas humanas**; las horas van aparte.

### Bloque A — Industria, construcción y B2B "aburrido" (el más alineado con su perfil)

**1. Video de preventa para desarrolladoras inmobiliarias (emprendimientos "en pozo")**
- **Qué es:** a partir de los renders del estudio de arquitectura y los planos, un film de 45-60 s del edificio terminado, 8-10 cortes verticales y versiones en inglés y portugués con locución para inversores del exterior. *Diferencia con E7*, que era staging y reels para inmobiliarias que venden usados: acá el cliente es la **desarrolladora**, con presupuesto de marketing de lanzamiento.
- **Cliente:** desarrolladoras medianas de CABA, Córdoba, Rosario, Mendoza y la Costa; también de Uruguay, Paraguay y Miami (latinas).
- **Evidencia:** la animación de renders tradicional es cara (un videógrafo cobra USD 300-1.500 solo por una propiedad usada, [AutoReel ⚠](https://www.autoreelapp.com/blog/real-estate-video-production-cost-in-2026)). Los precios de animación arquitectónica en Argentina están **[NO VERIFICADO]**.
- **Herramientas y costo:** Kling 3.0 / Veo 3.1 image-to-video desde los renders, ElevenLabs y Suno. **USD 30-80** por proyecto.
- **Precio y margen:** USD 900-2.500 por lanzamiento; margen ~95% (15-25 h).
- **Saturación:** B-M. **Riesgo:** M; poner "imagen ilustrativa, no contractual" y no mostrar amenities que no están en el proyecto (en EE.UU. aplica AB 723).
- **Rec.:** por lanzamiento (1-3 por año por cliente). **Anón.:** sí. **Score: 7,5**

**2. "Avance de obra" mensual para inversores (abono)**
- **Qué es:** la desarrolladora manda fotos y videos de celular de la obra; se entrega un video mensual de 60-90 s con línea de tiempo, porcentaje de avance, animación de cómo va a quedar y locución. El material es **real**, la IA solo anima y ambienta: riesgo legal mínimo.
- **Cliente:** el mismo de la idea 1, más fideicomisos al costo (sus inversores exigen informes).
- **Evidencia:** [NO VERIFICADO], es una hipótesis de producto. El informe a inversores es una necesidad recurrente propia de los fideicomisos.
- **Herramientas y costo:** Runway Aleph o Higgsfield para limpiar y ambientar, motion y locución. **USD 15-40 por mes**.
- **Precio y margen:** USD 300-600 por mes por obra; margen ~90% (4-6 h por mes).
- **Saturación:** B. **Riesgo:** B. **Rec.:** **sí** (12-30 meses de obra). **Anón.:** sí. **Score: 7,5**

**3. Explicativos animados de maquinaria y equipos industriales o agrícolas**
- **Qué es:** a partir de fotos reales, folletos y planos de la máquina, un video de 60-90 s que muestra cómo funciona, cuál es el beneficio y para qué aplicaciones sirve, en español, inglés y portugués, para distribuidores y web.
- **Cliente:** fabricantes PyME de agro-maquinaria (clúster de Las Parejas, Armstrong, Marcos Juárez), válvulas, bombas, equipos de frío, autopartistas exportadores.
- **Evidencia:** [NO VERIFICADO], hipótesis de baja saturación: no hay agencias de "AI ads" apuntando a este nicho.
- **Herramientas y costo:** la IA **no** dibuja la máquina desde cero porque inventa piezas. Se animan las fotos reales (Kling, Veo), se suman motion graphics y ElevenLabs. **USD 20-80**.
- **Precio y margen:** USD 1.000-3.000 por video; margen ~95% (12-20 h).
- **Saturación:** **B**. **Riesgo:** B (el riesgo es técnico: que una pieza aparezca mal).
- **Rec.:** media; un video por línea de producto, más versiones por idioma y feria. **Anón.:** sí; vende el criterio técnico. **Score: 7,5**

**4. Loops para pantallas de stand en ferias (Expoagro, AOG, Arminera, ferias de EE.UU. y Brasil)**
- **Qué es:** loops de 60-120 s sin audio para las pantallas LED del stand, más 5 cortes para redes antes y durante la feria.
- **Cliente:** expositores. La **lista de expositores es pública** en la web de cada feria, lo que la vuelve ideal para email frío 6-8 semanas antes.
- **Evidencia:** fechas y listas de expositores [NO VERIFICADO para 2027]; Expoagro se hace normalmente en marzo.
- **Herramientas y costo:** USD 20-60.
- **Precio y margen:** USD 500-1.500 por stand; ~95%.
- **Saturación:** B. **Riesgo:** B. **Rec.:** anual por feria y por cliente. **Anón.:** sí. **Score: 7**

**5. Inducción de seguridad (HSE) para contratistas, multilingüe y con SCORM** (*retoma E11 con ángulo nuevo*)
- **Qué es:** un módulo de inducción de 6-10 min por planta o yacimiento: riesgos, EPP, permisos de trabajo y emergencias. Combina animación de fotos reales de la planta, avatar opcional (uso interno, no publicidad) y versiones en español, inglés y portugués. Se exporta en SCORM para el LMS del cliente.
- **Cliente:** minería (litio en Salta, Catamarca y Jujuy; oro y cobre en San Juan), petroleras de Vaca Muerta, alimenticias, operadores logísticos.
- **Evidencia:** HeyGen Business (USD 149) suma SCORM y LMS; Synthesia Pro cuesta USD 89 ([synthesia.io](https://www.synthesia.io/pricing)). En la ficha A33 del informe previo, lo tradicional se estimó en USD 2-4k por hora de video.
- **Costo:** USD 10-50 por módulo + plan.
- **Precio y margen:** USD 1.500-5.000 por módulo; ~95% (20-35 h, incluida la validación técnica con el responsable de HSE del cliente).
- **Saturación:** B-M. **Riesgo:** M; el contenido técnico lo valida y firma el cliente.
- **Rec.:** actualizaciones y nuevas plantas. **Anón.:** sí. **Score: 7**

**6. Visualización de propuestas para licitaciones y presentaciones de proyectos**
- **Qué es:** un video de 60 s que muestra el proyecto propuesto (nave industrial, planta de tratamiento, parque solar, remodelación) para acompañar una oferta o presentarlo ante un municipio o el directorio.
- **Cliente:** constructoras medianas, consultoras de ingeniería, integradores de energía solar.
- **Evidencia:** [NO VERIFICADO].
- **Costo:** USD 20-60. **Precio y margen:** USD 800-2.500; ~95%.
- **Saturación:** B. **Riesgo:** M; siempre con aviso "imagen conceptual".
- **Rec.:** por licitación (varias por año). **Anón.:** sí. **Score: 6,5**

**7. Video institucional y de reclutamiento para industrias (employer branding)**
- **Qué es:** se mezcla material de celular grabado por el cliente siguiendo una lista de tomas que arma Claude, con b-roll IA no fotorrealista de personas, gráficos y locución. Versión de 90 s más 6 cortes.
- **Cliente:** plantas que no consiguen operarios calificados, logísticas, frigoríficos.
- **Evidencia:** [NO VERIFICADO].
- **Costo:** USD 15-50. **Precio y margen:** USD 800-2.000; ~95%.
- **Saturación:** B-M. **Riesgo:** B. **Rec.:** baja-media. **Anón.:** sí. **Score: 6**

### Bloque B — E-commerce y marcas DTC (ángulos nuevos sobre E1/E4)

**8. "Concept Lab" Andromeda para marcas DTC que ya invierten en pauta** (*retoma E1/E4*)
- **Ángulo nuevo:** no se venden "anuncios" ni "volumen". Se vende **diversidad de conceptos medida**: 10 conceptos distintos por mes × 3 variantes, con una matriz de hipótesis y un informe mensual de qué conceptos cortar y cuáles escalar, leído del Ads Manager del cliente (solo lectura; el usuario no maneja la cuenta).
- **Cliente:** marcas de EE.UU., España o LATAM que gastan USD 10-100k por mes en Meta. Se pueden filtrar por actividad en la Biblioteca de Anuncios de Meta, que es pública.
- **Evidencia:** la recomendación de 8-12 conceptos por campaña ([Segwise ⚠](https://segwise.ai/blog/meta-andromeda-update-creative-strategy-2026)) y el abono de 12 anuncios a USD 2.500-8.000 ([Motionbox ⚠](https://motionbox.io/blog/how-much-to-charge-clients-for-ai-ugc-ads)).
- **Costo:** USD 100-250 por mes en créditos.
- **Precio y margen:** **USD 1.500-3.000 por mes**; ~90% (25-35 h por mes).
- **Saturación:** **A** en "AI UGC", **M** con el ángulo de método. **Riesgo:** M (TikTok y Meta exigen etiqueta; nada de testimonios falsos).
- **Rec.:** sí. **Anón.:** sí, si la carta de presentación es un spec ad hecho con su producto. **Score: 7**

**9. Videos instructivos de uso del producto (post-compra) para bajar devoluciones y consultas**
- **Qué es:** un pack de 8-12 videos de 30-60 s ("cómo armarlo", "cómo usarlo", "errores comunes") a partir de fotos y manuales reales, con callouts animados y locución, para la ficha del producto, el email post-compra y el QR del empaque. **Se mide** la caída de tickets de soporte y devoluciones: es el método de ingeniería industrial aplicado a la posventa.
- **Cliente:** e-commerce de productos que se arman o tienen curva de uso (muebles, electro chico, fitness, bebés, herramientas). Sirve tanto en Argentina (Tiendanube, ML) como afuera.
- **Evidencia:** [NO VERIFICADO], hipótesis. El video instructivo tiene **bajo rechazo** porque no es publicidad ni usa humanos sintéticos.
- **Costo:** USD 20-60 por pack.
- **Precio y margen:** USD 600-1.500 por pack; ~95%.
- **Saturación:** **B**. **Riesgo:** B.
- **Rec.:** un pack por SKU nuevo o lanzamiento. **Anón.:** sí. **Score: 7**

**10. Hero film y cortes para bodegas, destilerías y marcas de bebidas exportadoras**
- **Qué es:** un film de 30-45 s "tipo TV" (viñedo, proceso, maridaje), 10 cortes y versiones en inglés y portugués para importadores y distribuidores.
- **Cliente:** bodegas boutique y medianas de Mendoza, San Juan y Salta, gin y vermut artesanal, yerba exportadora.
- **Evidencia:** [NO VERIFICADO]. **Restricciones:** la publicidad de alcohol tiene límites (Ley 24.788 en Argentina [NO VERIFICADO el texto], segmentación por edad en Meta).
- **Costo:** USD 30-80. **Precio y margen:** USD 1.000-2.500; ~95%.
- **Saturación:** B-M. **Riesgo:** M; no se puede representar consumo excesivo ni menores.
- **Rec.:** vendimia y lanzamientos. **Anón.:** sí. **Score: 6,5**

**11. Lookbook y video de colección por temporada para marcas de ropa** (*retoma E5 con otro formato*)
- **Qué es:** no se cobra por foto suelta, sino por **colección**: 20-30 looks con modelo IA (o sobre la prenda real fotografiada en maniquí), video de lanzamiento de 20 s y 10 piezas para redes. Se renueva en cada temporada (otoño-invierno, primavera-verano y cápsulas).
- **Cliente:** las ~65.000 marcas de Tiendanube (dato del informe previo).
- **Evidencia:** existe rechazo a los modelos IA en moda (caso Guess en Vogue, 2025-08) [cita de memoria, NO VERIFICADO hoy].
- **Costo:** USD 10-40. **Precio y margen:** USD 400-1.200 por colección; ~95%.
- **Saturación:** M-A. **Riesgo:** M; la prenda tiene que verse fiel (si no, hay devoluciones y lealtad comercial).
- **Rec.:** sí (2-4 veces por año). **Anón.:** sí. **Score: 6**

**12. Videos verticales para fichas de Mercado Libre y catálogo de Meta (DPA en video), en escala**
- **Qué es:** plantilla de video de 10-15 s por SKU (producto girando, beneficio, precio) para catálogos de 100-1.000 SKUs.
- **Cliente:** vendedores grandes de ML y distribuidoras.
- **Evidencia:** la existencia y las reglas de video en fichas de ML ("Clips") **[NO VERIFICADO]**: no se pudo confirmar.
- **Costo:** USD 0,5-2 por SKU. **Precio y margen:** USD 3-8 por SKU o abono de USD 200-500 por mes; ~70-80%.
- **Saturación:** M; **Meta lo hace gratis** con Advantage+. **Riesgo:** B.
- **Rec.:** sí. **Anón.:** sí. **Score: 5,5**

**13. Test de concepto antes de fabricar (validación de demanda con anuncios IA)**
- **Qué es:** para un producto todavía no fabricado, 5 conceptos de video y una landing de preventa o lista de espera. El cliente corre una prueba chica en Meta (USD 300-500 de pauta, que pone él) y recibe un informe de qué concepto y qué precio validan. Es un sprint de 2-3 semanas.
- **Cliente:** emprendedores con prototipo, PyMEs que lanzan una línea nueva, estudios de diseño industrial.
- **Evidencia:** [NO VERIFICADO], es método lean aplicado.
- **Costo:** USD 30-80. **Precio y margen:** USD 800-1.500 por sprint; ~95%.
- **Saturación:** B. **Riesgo:** **M-A**; anunciar algo que no existe es engañoso salvo que se presente claramente como preventa o lista de espera.
- **Rec.:** por producto. **Anón.:** sí. **Score: 6,5**

### Bloque C — Personajes, marca y localización

**14. Mascota de marca IA con "biblia de personaje" y serie mensual**
- **Qué es:** un setup de diseño del personaje, hoja de referencia, voz (ElevenLabs), reglas de estilo y un Soul ID o banco de referencias; después, 8 shorts por mes. Evita los "humanos sintéticos" que rechaza el 62% del público ([Bentley-Gallup](https://www.fingerlakes1.com/2026/08/20/new-york-businesses-face-a-trust-problem-as-consumers-sour-on-ai-generated-advertising/)).
- **Cliente:** veterinarias con varias sucursales, aseguradoras y brokers, cooperativas, fintech chicas, cadenas regionales.
- **Evidencia:** solo casos de vendedores ([VO3 ⚠](https://www.vo3ai.com/blog/why-faceless-ai-brand-mascots-now-outperform-2000human-videos-roi-breakdown-for--2026-08-21)).
- **Costo:** USD 30-80 por mes.
- **Precio y margen:** setup de USD 800-1.500 + **USD 400-900 por mes**; ~90%.
- **Saturación:** B-M. **Riesgo:** M; un personaje 100% IA tiene **protección autoral débil** (aclararlo en el contrato y sugerir registrar la marca).
- **Rec.:** **sí**. **Anón.:** sí. **Score: 7**

**15. Localización cultural de anuncios ganadores de marcas extranjeras a LATAM y España** (*E16/E17 eran YouTube y cursos; esto es publicidad*)
- **Qué es:** no es solo doblar, porque **Meta ya dobla gratis con lip-sync desde 2026-03**. Se reescriben el gancho y los textos en pantalla, se adaptan modismos, moneda, talles y medios de pago (cuotas, Pix, Mercado Pago), se rehace el doblaje y se ajusta el cumplimiento local. USD 150-400 por anuncio, o packs de 10 por USD 2.000.
- **Cliente:** marcas DTC de EE.UU. y Europa que entran a México, Brasil, Argentina o España.
- **Evidencia:** traducción con lip-sync en HeyGen a ~USD 0,25 por minuto ([Creatify ⚠](https://creatify.ai/blog/heygen-pricing-(2026)-plans-and-what-you-ll-actually-pay)); doblaje de Meta (ver 3.1).
- **Costo:** USD 2-10 por anuncio. **Margen:** ~95%.
- **Saturación:** M. **Riesgo:** M; lip-sync sobre personas reales solo con la autorización del cliente y del talento original.
- **Rec.:** sí. **Anón.:** sí. **Score: 6,5**

**16. Versionado de un comercial por sucursal para franquicias y cadenas**
- **Qué es:** un comercial maestro de 20-30 s y 20-100 versiones con la dirección, la promo y el horario de cada local, renovado con cada promo mensual.
- **Cliente:** franquiciantes (gastronomía, gimnasios, ópticas, inmobiliarias de red).
- **Evidencia:** [NO VERIFICADO].
- **Costo:** USD 30-60 el maestro y centavos cada versión.
- **Precio y margen:** maestro USD 1.000-1.500 + USD 30-80 por versión; ~90%.
- **Saturación:** B. **Riesgo:** B.
- **Rec.:** **sí** (promos mensuales). **Anón.:** sí. Claude Code puede armar el "versionador" con una planilla y plantillas. **Score: 6,5**

**17. Doble digital del dueño o del vocero, con consentimiento, para preguntas frecuentes y onboarding** (*retoma E21 con otro destino*)
- **Ángulo nuevo:** no es contenido para redes, es **atención y onboarding**: 20-40 respuestas en video a las preguntas frecuentes reales del negocio, para la web, WhatsApp y el email de bienvenida.
- **Cliente:** estudios contables, prepagas chicas, escuelas, SaaS.
- **Costo:** USD 5-30. **Precio y margen:** USD 600-1.500 el setup + actualizaciones de USD 150-300 por mes; ~90%.
- **Saturación:** M. **Riesgo:** M; consentimiento escrito (CCyC art. 53), etiqueta, nunca usarlo en anuncios como si fuera grabado real.
- **Rec.:** sí. **Anón.:** sí. **Score: 6**

### Bloque D — Agencias, productoras, SaaS y eventos

**18. Animatics y previz IA para productoras y agencias (pitch y preproducción)**
- **Qué es:** del guion o storyboard de la agencia a un animatic de 30-60 s con Veo o Kling, para ganar el pitch o aprobar con el cliente antes del rodaje.
- **Cliente:** productoras argentinas de servicios y agencias creativas chicas y medianas.
- **Evidencia:** precios **[NO VERIFICADO]**; Animatic Media vende comerciales IA a "10-20% del costo tradicional" ([sitio](https://www.animaticmedia.com/ai-commercials)).
- **Costo:** USD 20-60. **Precio y margen:** USD 500-2.000 por animatic; ~95%.
- **Saturación:** B-M; las productoras grandes ya lo hacen internamente.
- **Riesgo:** B; es material interno, no se publica.
- **Rec.:** **sí**, por pitch. **Anón.:** white label, sí. Exige criterio audiovisual: curva de aprendizaje. **Score: 6,5**

**19. Videos de lanzamiento de funciones para SaaS (abono con el changelog)**
- **Qué es:** cada vez que el SaaS publica una función nueva, un video de 30-45 s con motion (Higgsfield Motion Design desde logo y web), grabación de pantalla y locución, más 3 cortes.
- **Cliente:** SaaS B2B de 10-200 empleados. **Método de prospección:** las empresas que publican changelog y lanzan seguido (ese dato es público).
- **Evidencia:** [NO VERIFICADO].
- **Costo:** USD 10-30 por video.
- **Precio y margen:** USD 500-1.200 por video o abono de USD 1.500-3.000 por mes; ~95%.
- **Saturación:** M (hay muchos motion designers). **Riesgo:** B. **Rec.:** **sí**. **Anón.:** sí. **Score: 6,5**

**20. Comerciales para TV conectada (CTV) de PyMEs de EE.UU.**
- **Qué es:** spot de 30 s + cortes de 15 y 6 s, con especificaciones de broadcast, para pequeñas empresas que compran CTV autoservicio.
- **Evidencia:** precios de USD 500-2.500 ([ReelForge, Contra](https://contra.com/s/vArONZ7b-ai-commercial-video-creation)), pero **Adwave genera el comercial gratis** desde la web ([Adwave ⚠](https://adwave.com/resources/ai-tv-commercials-small-business)).
- **Costo:** USD 20-60. **Precio y margen:** USD 1.200-3.000; ~95%.
- **Saturación:** M-A. **Riesgo:** M (spots fotorrealistas: etiqueta y la ley S8420A si sale en Nueva York).
- **Rec.:** baja. **Anón.:** sí. **Score: 5,5**

**21. Openers, intros de oradores y videos de premiación para eventos corporativos**
- **Qué es:** el paquete audiovisual de una convención o fiesta de fin de año: opener de 60-90 s, 10 intros de oradores y placas de premios.
- **Cliente:** agencias de eventos (como canal) y RR.HH. de empresas medianas. **Temporada:** noviembre-diciembre.
- **Evidencia:** [NO VERIFICADO].
- **Costo:** USD 20-60. **Precio y margen:** USD 800-3.000 por evento; ~95%.
- **Saturación:** B-M. **Riesgo:** B; no usar caras de empleados sin su consentimiento.
- **Rec.:** anual por cliente. **Anón.:** sí, vía agencia. **Score: 6**

**22. Video de campaña para crowdfunding (Kickstarter, Indiegogo, Catarse)**
- **Qué es:** video de campaña de 2 min (mezcla de prototipo real con escenas IA) + 10 anuncios de prelanzamiento.
- **Costo:** USD 40-100. **Precio y margen:** USD 1.500-4.000; ~95%.
- **Saturación:** M. **Riesgo:** **M-A**; las plataformas penalizan mostrar un producto que no existe [reglas de Kickstarter sobre renders **NO VERIFICADO**].
- **Rec.:** no. **Anón.:** sí. **Score: 5,5**

**23. Revisión de cumplimiento de creatividades IA ("pre-flight") para agencias**
- **Qué es:** no es producción. Antes de pautar, una revisión con checklist: qué pieza lleva etiqueta en Meta, TikTok y YouTube; art. 50 si apunta a la UE; S8420A si apunta a Nueva York; testimonios (FTC); derechos de imagen, música y marcas de terceros; C2PA. Se entrega una planilla de semáforo y un "paquete de evidencias".
- **Cliente:** agencias de performance y marcas que pautan en la UE y EE.UU.
- **Evidencia:** TikTok habilita el baneo permanente ([Stellar Search](https://www.stellarsearch.co.uk/insight/tiktoks-ai-ad-disclosure-rules-are-live-what-brands-running-ai-creative-need-to-do-now)); multas del art. 50 ([ICTRecht](https://www.ictrecht.nl/en/blog/heads-up-ai-act-transparency-obligations-now-in-effect)); 14% de rechazos por IA no declarada [NO VERIFICADO].
- **Costo:** ~USD 0 (Claude).
- **Precio y margen:** USD 300-1.000 por auditoría o USD 500-1.500 por mes; ~98%.
- **Saturación:** **B**. **Riesgo:** **M**; no es asesoramiento legal. Posicionarlo como checklist operativo y cerrar alianza con un abogado.
- **Rec.:** sí. **Anón.:** sí. Encaja con el método de procesos del Sistema A. **Score: 6,5**

### Bloque E — Otros nichos evaluados (para no reabrirlos)

**24. Video de visión y demo para startups que levantan capital.** USD 1.000-2.500, costo USD 30-80, margen ~95%, saturación M, riesgo M (no prometer funciones que no existen), sin recurrencia, anónimo sí. **Score: 5,5**

**25. Anuncios para servicios del hogar de EE.UU. (techistas, climatización, solar) con mascota o explicativo de financiamiento.** USD 500-1.500 por mes por 8 anuncios. Clientes con alto valor de vida, pero **saturados de emails de agencias**; nada de testimonios falsos (FTC). Margen ~90%, saturación **A**, riesgo M, recurrencia sí, anónimo sí. **Score: 5**

**26. Contenido educativo animado para edtech y editoriales escolares.** USD 300-800 por minuto terminado, costo USD 5-20 por minuto, margen ~95%, saturación M, riesgo B (errores conceptuales: hace falta revisión docente), recurrencia sí, anónimo sí. **Score: 5,5**

**27. Video de prospección 1:1 personalizado (avatar del vendedor del cliente + la web del prospecto) para equipos comerciales.** USD 500-1.500 por mes. Para escalar exige integrar la API (Claude Code podría armarla). Competidores: Tavus y Sendspark. Margen ~85%, saturación M, riesgo M (consentimiento y etiqueta), recurrencia sí, anónimo sí. **Score: 5**

**28. Book trailers para autores autopublicados.** USD 150-500. La comunidad lectora (romance, fantasía) es **muy hostil a la IA** y el riesgo reputacional es para el autor. Margen ~95%, saturación M, riesgo M, recurrencia baja, anónimo sí. **Score: 4**

**Descartadas como servicio (trampas, ver sección 9):** video IA para Google Business Profile (la política exige que las imágenes "representen la realidad"); "antes y después" IA para clínicas estéticas u odontológicas (engañoso, y la publicidad de salud está regulada); testimonios con avatar (FTC); jingles con Udio (no permite descargar); cualquier pieza con celebridades o personajes de terceros (Seedance, Disney, MPA).

---

## 7. Tabla resumen

| # | Idea | Precio | Margen* | Saturación | Rec. | Score |
|---|---|---|---|---|---|---|
| 1 | Preventa para desarrolladoras | USD 900-2.500 | ~95% | B-M | lanzamiento | **7,5** |
| 2 | Avance de obra mensual | USD 300-600/mes | ~90% | B | sí | **7,5** |
| 3 | Explicativos de maquinaria industrial/agro | USD 1.000-3.000 | ~95% | B | media | **7,5** |
| 4 | Loops para stands de feria | USD 500-1.500 | ~95% | B | anual | 7 |
| 5 | Inducción HSE multilingüe con SCORM | USD 1.500-5.000 | ~95% | B-M | media | 7 |
| 8 | Concept Lab Andromeda (DTC) | USD 1.500-3.000/mes | ~90% | A (M con método) | sí | 7 |
| 9 | Instructivos post-compra | USD 600-1.500 | ~95% | B | por SKU | 7 |
| 14 | Mascota + serie mensual | USD 800-1.500 + 400-900/mes | ~90% | B-M | sí | 7 |
| 6 | Visualización para licitaciones | USD 800-2.500 | ~95% | B | por oferta | 6,5 |
| 10 | Bodegas y bebidas exportadoras | USD 1.000-2.500 | ~95% | B-M | estacional | 6,5 |
| 13 | Test de concepto antes de fabricar | USD 800-1.500 | ~95% | B | por producto | 6,5 |
| 15 | Localización cultural de anuncios | USD 150-400/anuncio | ~95% | M | sí | 6,5 |
| 16 | Versionado por sucursal | USD 1.000-1.500 + 30-80/versión | ~90% | B | sí | 6,5 |
| 18 | Animatics y previz para agencias | USD 500-2.000 | ~95% | B-M | sí | 6,5 |
| 19 | Lanzamientos de SaaS | USD 1.500-3.000/mes | ~95% | M | sí | 6,5 |
| 23 | Revisión de cumplimiento de creatividades IA | USD 300-1.500 | ~98% | B | sí | 6,5 |
| 7 | Employer branding industrial | USD 800-2.000 | ~95% | B-M | baja | 6 |
| 11 | Colección por temporada (moda) | USD 400-1.200 | ~95% | M-A | sí | 6 |
| 17 | Doble digital para FAQ y onboarding | USD 600-1.500 + 150-300/mes | ~90% | M | sí | 6 |
| 21 | Eventos corporativos | USD 800-3.000 | ~95% | B-M | anual | 6 |
| 12 | Video por SKU (ML / catálogo de Meta) | USD 3-8/SKU | 70-80% | M | sí | 5,5 |
| 20 | Comercial CTV para PyMEs de EE.UU. | USD 1.200-3.000 | ~95% | M-A | baja | 5,5 |
| 22 | Crowdfunding | USD 1.500-4.000 | ~95% | M | no | 5,5 |
| 24 | Video de visión para startups | USD 1.000-2.500 | ~95% | M | no | 5,5 |
| 26 | Edtech animado | USD 300-800/min | ~95% | M | sí | 5,5 |
| 25 | Servicios del hogar de EE.UU. | USD 500-1.500/mes | ~90% | A | sí | 5 |
| 27 | Prospección 1:1 con avatar | USD 500-1.500/mes | ~85% | M | sí | 5 |
| 28 | Book trailers | USD 150-500 | ~95% | M | baja | 4 |

\*El margen excluye las horas humanas. Medido por hora, con 15-25 h por proyecto de USD 1.500, queda en **USD 60-100 por hora**; en los abonos de USD 300-600 por mes con 4-6 h, en USD 75-100 por hora.

---

## 8. Top 5 para este usuario

1. **Desarrolladoras: preventa + avance de obra (ideas 1 y 2).** Combina un ticket de entrada alto (USD 900-2.500) con un abono natural de 12-30 meses. Parte de material real, lo que baja el riesgo legal y las alucinaciones. Los decisores se pueden identificar (el dueño o el gerente comercial de la desarrolladora) y es un rubro poco atacado. El usuario entiende la obra por su formación de ingeniero. **Primer paso:** elegir 3 emprendimientos en preventa de Córdoba o Rosario, hacer gratis un spec de 15 s con sus renders públicos y mandarlo por email frío **sin publicarlo**.
2. **Explicativos de maquinaria + loops de feria (ideas 3 y 4).** Saturación baja, ticket de USD 1.000-3.000, prospección con las listas públicas de expositores y un calendario fijo (Expoagro, marzo de 2027 [fecha NO VERIFICADA]). Es donde la ingeniería industrial se vuelve ventaja real: entender la máquina y no dejar que la IA invente piezas.
3. **Instructivos post-compra con métrica de devoluciones y tickets (idea 9).** El ángulo de "reducir el costo de soporte" lo diferencia de la masa que vende "anuncios", tiene poco rechazo y conecta con el Sistema A (Orden Operativo).
4. **Mascota de marca + serie mensual (idea 14).** Es la forma más limpia de esquivar el rechazo a los humanos sintéticos (62%) y el abono se justifica por la biblia del personaje. Riesgo: el personaje no es registrable si es 100% IA.
5. **Concept Lab Andromeda para DTC con pauta (idea 8).** Es la de mayor ticket recurrente (USD 1.500-3.000 por mes) y la de mayor competencia. Solo conviene si la diferenciación es el **método** (matriz de conceptos + lectura de datos), no los clips. Es la evolución de E1/E4 hacia afuera, para cobrar en USD.

**Combinación sugerida:** el núcleo es 1+2 o 3+4 (B2B local con ticket); como abono, 2, 14 o 16; la revisión de cumplimiento (23) se suma como valor agregado.

---

## 9. Trampas

1. **El modelo desaparece.** Sora cerró en 7 meses. Venderle al cliente un resultado y un método, nunca "videos con X". Guardar prompts, referencias y biblias en formato independiente del modelo.
2. **Lo gratis de Meta, Google y Adwave.** El video básico de producto desde fotos y el doblaje simple **ya son gratis** dentro de Meta Advantage+ (2025-2026). Vender eso es competir contra cero.
3. **Humanos sintéticos y testimonios falsos.** Al 62% del público de EE.UU. le resultan inaceptables. La FTC prohíbe testimonios de personas inexistentes, Nueva York exige aviso desde el ~2026-06-09 y TikTok puede banear de forma permanente desde el 2026-07-21. "AI UGC con avatar que dice 'yo lo usé'" es la **peor** combinación posible.
4. **Google Business Profile e inmobiliarias.** GBP pide imágenes que "representen la realidad", y AB 723 (California) más el art. 50 (UE) obligan a etiquetar inmuebles y productos alterados. Siempre poner "imagen ilustrativa" y conservar las originales.
5. **Propiedad intelectual:** nada de personajes, celebridades, marcas de terceros ni "estilo de" estudios reconocibles (Seedance 2.0 recibió cartas documento de Disney y la MPA). En música, Suno v6 está licenciado con Warner, BMG y Believe, pero **UMG y Sony siguen litigando**; Udio no sirve para entregables.
6. **Higgsfield como único proveedor:** créditos que vencen, renovación anual automática con quejas de facturación, "ilimitado" que no se puede automatizar, Marketing Studio que no está en el MCP y un escándalo de reputación en 2026. Tener un plan B (Kling directo, Luma o Veo vía Flow) y **no nombrar la herramienta** ante el cliente.
7. **Datos de vendedores:** casi todos los precios y las cifras de "AI UGC rinde igual o mejor" salen de blogs de empresas que venden herramientas (Creatify, Motionbox, VO3, Segwise, AutoReel, el blog de Higgsfield). Son techo, no mediana. Validar con 10-20 conversaciones reales antes de fijar precios.
8. **Margen de compute no es margen de negocio:** generar cuesta USD 3-60, pero las horas de guion, curaduría, revisiones y venta son el costo real. Con revisiones ilimitadas el margen se evapora: limitar a 2 rondas por contrato.
9. **Email frío con marca anónima:** sin cara ni casos, la tasa de respuesta va a ser baja. El "spec ad" con el producto del prospecto es la palanca, pero **no se publica** (es su marca) y se manda con tono de muestra privada.
10. **Propiedad del entregable:** el material 100% IA tiene protección autoral débil (EE.UU.) y el cliente no puede impedir copias. Dejarlo escrito en el contrato; para personajes, recomendar registrar la marca.
11. **Cumplimiento en la UE:** si el cliente pauta en la UE, el art. 50 rige desde el 2026-08-02 y un aviso con elementos ficticios **no** está exento automáticamente. Entregar los archivos etiquetados y con C2PA cuando la herramienta lo permita.
12. **Precio en Argentina:** los tickets de USD 1.000-3.000 son realistas afuera y en B2B industrial o inmobiliario, **no** en comercio minorista local. Para el rubro local, usar los tickets de los frentes H e I, no los de este informe.

---

## 10. Pendientes de verificar (cuando haya cuota de búsqueda)

- Si Sora 2 sigue apareciendo en Higgsfield después del 2026-09-24 y qué lo reemplazó.
- Video en fichas de Mercado Libre ("Clips"): existencia, reglas e impacto.
- Precios de animación de renders y de video institucional en Argentina (pesos, 2026).
- Fecha de Expoagro 2027 y listas de expositores de AOG Patagonia y Arminera.
- Estado de los proyectos de ley argentinos de etiquetado de IA y deepfakes en publicidad.
- Reglas de Kickstarter sobre renders fotorrealistas.
- Primeras multas de la FTC bajo la regla de reseñas (2026-04, USD 27,4 M).
- Umbral de "similitud creativa" de Andromeda: ¿Meta lo confirmó oficialmente?

---

## Fuentes principales (consultadas el 2026-10-02)

- The Decoder, cierre de Sora (2026-03-28): https://the-decoder.com/openai-sets-two-stage-sora-shutdown-with-app-closing-april-2026-and-api-following-in-september/
- invideo ⚠, precios por segundo (2026-08): https://invideo.io/blog/ai-video-model-pricing
- BenchLM, precios de Veo: https://benchlm.ai/media-pricing/veo
- Creatify ⚠, Higgsfield vs Kling (2026-09-04): https://creatify.ai/blog/higgsfield-vs-kling-ai-quality-cost-per-second-and-which-to-use-for-ads-in-2026
- Krea ⚠, precios de Higgsfield 2026: https://www.krea.ai/blog/what-is-higgsfield-ai-pricing-free-plan-and-alternatives-in-2026
- Kive, Higgsfield 2026 (actualizado 2026-10-01): https://kive.ai/learn/is-higgsfield-worth-it
- Higgsfield Help, Marketing Studio (2026-09-01): https://higgsfield.ai/creator-hub/help-center/tools/how-do-i-use-marketing-studio-to-create-video-ads
- Higgsfield ⚠, 100 anuncios (2026-08-28): https://higgsfield.ai/blog/make-100-creative-ads
- Kling, guía de créditos 3.0 ⚠: https://kling.ai/blog/kling-video-3-0-credit-cost-guide
- Creatify ⚠, precios de Runway 2026: https://creatify.ai/blog/runway-pricing-(2026)-plans-credits-and-what-you-ll-actually-pay
- Luma, precios: https://lumalabs.ai/pricing · Pika, precios: https://pika.art/pricing · Synthesia, precios: https://www.synthesia.io/pricing · Hedra, precios: https://www.hedra.com/pricing
- Creatify ⚠, precios de HeyGen 2026: https://creatify.ai/blog/heygen-pricing-(2026)-plans-and-what-you-ll-actually-pay
- Smallest.ai ⚠, precios de ElevenLabs 2026: https://smallest.ai/blog/elevenlabs-pricing-plans-cost-what-you-get-in-2026
- Wikipedia, Suno: https://en.wikipedia.org/wiki/Suno_AI · Udio: https://en.wikipedia.org/wiki/Udio
- GitHub Wan-Video: https://github.com/Wan-Video
- Axios, la MPA sobre Seedance (2026-02-20): https://www.axios.com/2026/02/20/hollywood-seedance-intellectual-property
- Motionbox ⚠, precios de AI UGC (2026-08-05): https://motionbox.io/blog/how-much-to-charge-clients-for-ai-ugc-ads
- SelfEmployed, Upwork In-Demand Skills (2026-02): https://www.selfemployed.com/news/upwork-ai-freelance-skills-demand-2026/
- Segwise ⚠, Andromeda: https://segwise.ai/blog/meta-andromeda-update-creative-strategy-2026
- Exchange4media, automatización de Meta (2025-06): https://www.exchange4media.com/digital-news/meta-aims-to-fully-automate-advertising-with-ai-by-2026-144037.html
- Campaign Asia, herramientas generativas de Advantage+: https://www.campaignasia.com/article/meta-expands-advantage-with-gen-ai-ad-creativity-tools-for-advertisers/503131
- FingerLakes1 / Bentley-Gallup (2026-08-20): https://www.fingerlakes1.com/2026/08/20/new-york-businesses-face-a-trust-problem-as-consumers-sour-on-ai-generated-advertising/
- Advanced Television / DoubleVerify (2026-08-06): https://www.advanced-television.com/2026/08/06/study-ai-slop-poses-growing-risk-to-brand-trust/
- AdNews / YouGov (2026-05): https://www.adnews.com.au/news/many-australians-lose-brand-trust-when-they-know-they-are-seeing-ai-generated-ads
- Cinerads ⚠, avisos de IA por plataforma: https://www.cinerads.com/blog/ai-ad-disclosure-requirements
- Stellar Search, TikTok (2026-08-12): https://www.stellarsearch.co.uk/insight/tiktoks-ai-ad-disclosure-rules-are-live-what-brands-running-ai-creative-need-to-do-now
- ICTRecht, art. 50 del AI Act (2026-08-03): https://www.ictrecht.nl/en/blog/heads-up-ai-act-transparency-obligations-now-in-effect
- NY Senate S8420A: https://www.nysenate.gov/legislation/bills/2025/S8420/amendment/A
- Search Engine Land, regla de la FTC: https://searchengineland.com/ftc-fake-reviews-testimonials-445209
- Inman, AB 723 (2026-01-23): https://www.inman.com/2026/01/23/what-you-should-know-about-californias-new-listing-photo-law/
- Google Business Profile, fotos: https://support.google.com/business/answer/6123536
- AutoReel ⚠, costo de video inmobiliario 2026: https://www.autoreelapp.com/blog/real-estate-video-production-cost-in-2026
- Adwave ⚠: https://adwave.com/resources/ai-tv-commercial-production
- HCDN, proyecto de etiquetado de IA: https://rest.hcdn.gob.ar/web/proyectos/290925/adjuntos/105159
