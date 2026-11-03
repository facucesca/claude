# Rubros "parecidos a la edición de video": servicios tech-enabled con herramienta propia

- **Fecha:** 2026-10-02
- **Autor:** subagente de investigación (Claude Code) para IDEAS-PRUEBA
- **Pregunta:** ¿qué rubros vecinos a la edición de video permiten el modelo "herramienta propia que automatiza la mayor parte del trabajo + revisión humana + venta B2B por email frío con marca anónima", con ticket más alto y menos saturación que las ideas ya evaluadas?
- **Perfil para el score:** argentino, no programa (Claude Code le construye las herramientas locales), ingeniería industrial, capital < USD 500, tiene Higgsfield, sin mostrar la cara, prospección por email frío, quiere ticket mayor y ángulos menos quemados.
- **No repite sin aportar:** `research/2026-10-01-230-ideas-con-claude.md` y `research/2026-10-01-200-ideas-rapidas-1-semana.md`. Cuando se retoma una idea de esos estudios (E5, E7, E8, E12, E15, H32, C22, L12), se dice cuál es y qué ángulo nuevo se suma: B2B, volumen o automatización.

---

## Metodología

1. **Búsquedas:** 35 consultas WebSearch el 2026-10-02 (la cuota funcionó). Fuentes: páginas de precios de SaaS del rubro, guías de precios 2026 de proveedores, regulaciones oficiales o comentadas por estudios jurídicos y universidades (Federal Register, Plante Moran, Duane Morris), notas de prensa y páginas de producto.
2. **Nivel de confianza.** Muchas guías de precios las publican **vendedores del mismo rubro**, por ejemplo Imagen AI, que vende edición con IA y escribe sobre lo que cuesta tercerizar. Hay conflicto de interés: el rango sirve como orden de magnitud, no como dato exacto. Las cifras de impacto que dan las plataformas ("+500% de visitas", "+30% de pedidos") son **del vendedor** y se tratan como optimistas.
3. **[NO VERIFICADO]** marca lo que no pude contrastar con una fuente primaria o lo que es estimación propia. Los precios para Argentina y LatAm son en su mayoría **estimaciones propias**, porque casi no hay listas públicas.
4. **Columnas de cada ficha:** qué es · cliente · evidencia · precio y ticket mensual · % automatizable y stack · margen · saturación · recurrencia · ¿anónimo por email? · score.
5. **Score 1-10 para ESTE usuario.** Pondera ticket, saturación, % automatizable con herramientas que Claude Code puede armar sin que él programe, fit con la ingeniería industrial, viabilidad con marca anónima y capital < USD 500. No es un score de mercado general.
6. **Margen:** (precio − costo de APIs y SaaS) / precio. No incluye las horas del usuario, que figuran aparte en el % automatizable.

---

## Lista numerada (33 ideas)

### A. FOTO

#### 1. Normalización masiva de catálogo para distribuidoras y mayoristas (retoma E5 y H32 con ángulo de volumen)
- **Qué es:** las fotos heterogéneas de proveedores o de celular, para 500-5.000 SKUs, entran a un pipeline que recorta, pone fondo blanco o gris uniforme, sombra, encuadre y tamaño estándar, renombra por SKU y exporta para Mercado Libre, Tiendanube o el catálogo B2B.
- **Cliente:** distribuidoras (ferretería, electricidad, librería, bazar, autopartes), mayoristas de Once y Avellaneda, sellers grandes de ML.
- **Evidencia:** la tercerización de edición de e-commerce cuesta **USD 0,70-2,50 por imagen** y el fondo blanco en volumen baja a **USD 0,30**; la edición pura con IA cuesta USD 0,05-0,08 ([Imagen AI, guía 2026](https://imagen-ai.com/post/outsource-photo-editing-cost-per-image/), consultado 2026-10-02; fuente con conflicto de interés).
- **Precio/ticket:** proyecto inicial de USD 400-1.500 (catálogo de 1.000 SKUs a USD 0,4-1,5 cada uno) más un abono de USD 100-300/mes por las altas nuevas [estimación propia].
- **% automatizable:** 85-90%. Stack: rembg o API de Photoroom/Claid para el recorte; Python con PIL para encuadre y sombra; Claude para mapear nombres de archivo a SKUs y detectar fotos malas; revisión por grilla de miniaturas.
- **Margen:** 80-90%.
- **Saturación:** **media-alta** a nivel global (offshore asiático a USD 0,30) y **media-baja** en distribuidoras argentinas, que hoy no tercerizan esto.
- **Recurrencia:** media (altas de productos y cambios de proveedor).
- **Anónimo por email:** sí.
- **Score: 6,5.** Funciona mejor como puerta de entrada a la idea 8.

#### 2. Fotos "en modelo" con IA para marcas de indumentaria (prenda plana → modelo)
- **Qué es:** la foto de la prenda sobre mesa o maniquí se convierte en foto con modelo IA, en varias poses, con modelos consistentes por marca y por temporada.
- **Cliente:** marcas de ropa de Avellaneda, Flores y Tiendanube con 100-500 SKUs por temporada; marcas de uniformes.
- **Evidencia:** Botika cobra **USD 0,73-1,15 por foto** en planes de USD 22 o más al mes ([Botika pricing](https://botika.io/pricing), consultado 2026-10-02); Claid desde USD 15/mes ([nightjar](https://nightjar.so/blog/best-botika-alternatives)). Tiendanube ya tiene "editar fondo" y lanzó **Lumi Studio** para generar imágenes ([Ayuda Tiendanube](https://ayuda.tiendanube.com/es_AR/fotos-del-producto/editar-imagenes-para-tus-productos-tiendanube-usando-inteligencia-artificial); [DPL News, 2026](https://dplnews.com/?p=316889)).
- **Precio/ticket:** USD 3-8 por foto final revisada; USD 300-1.200 por temporada o mes [estimación propia].
- **% automatizable:** 70%. Stack: Botika o Claid por API, Higgsfield, Claude para el brief de poses. Es clave la revisión humana de manos, logos y caída de la tela.
- **Margen:** 70-80%.
- **Saturación:** **media**. Crece, y la plataforma lo absorbe en parte.
- **Recurrencia:** alta en moda (dos temporadas más cápsulas).
- **Anónimo:** sí.
- **Score: 6,5.**

#### 3. Edición inmobiliaria mayorista (HDR, cielo, enderezado) para fotógrafos de EE.UU.
- **Qué es:** el fotógrafo inmobiliario sube brackets y el servicio devuelve las fotos fusionadas, enderezadas, con cielo y ventanas corregidos.
- **Cliente:** fotógrafos inmobiliarios de EE.UU., Canadá y Australia.
- **Evidencia:** la edición inmobiliaria con HDR y cielo cuesta **USD 0,60-1,50 por foto** en el tramo básico; el reemplazo de cielo suma USD 1-3 ([Imagen AI](https://imagen-ai.com/post/outsource-photo-editing-cost-per-image/); [PhotoUp](https://www.photoup.net/learn/11-best-real-estate-photo-editing-services), consultados 2026-10-02).
- **Precio/ticket:** USD 15-40 por propiedad; USD 300-1.500/mes por fotógrafo con volumen.
- **% automatizable:** 75-85%. Stack: fusión HDR con OpenCV/enfuse, segmentación de cielo, corrección de verticales.
- **Margen:** 60-75%.
- **Saturación:** **ALTA**. PhotoUp, BoxBrownie y cientos de estudios de Bangladesh, India y Filipinas compiten con plazos de 12-24 h.
- **Recurrencia:** alta.
- **Anónimo:** sí.
- **Score: 4,5.** Carrera de precios a la baja.

#### 4. Paquete de publicación por propiedad para inmobiliarias de AR y LatAm (retoma E7 con ángulo de flujo)
- **Qué es:** con las fotos de celular del corredor, la herramienta devuelve en menos de 24 h fotos corregidas (luz, verticales, cielo, borrado de objetos), un reel vertical, el texto del aviso para Zonaprop/ML/Argenprop y un plano esquemático si lo hay. Es un abono por la cartera de la inmobiliaria.
- **Cliente:** inmobiliarias medianas de 20-150 propiedades activas.
- **Evidencia:** los SaaS de video desde fotos cobran USD 49-199/mes (Reeltors) o USD 59-599/mes (Reel-E); un video IA desde fotos puede costar USD 10 contra USD 150-500 de una sesión profesional ([Capterra Reeltors](https://www.capterra.com/p/10045003/Reeltors-ai/); [Capterra Reel-E](https://www.capterra.com/p/10037342/Reel-E/); [AutoReel](https://www.autoreelapp.com/blog/real-estate-video-production-cost-in-2026), consultados 2026-10-02). En AR no encontré tarifas públicas de edición por propiedad [NO VERIFICADO].
- **Precio/ticket:** USD 15-35 por propiedad; USD 150-600/mes por inmobiliaria [estimación propia].
- **% automatizable:** 85%. Stack: Python con OpenCV, Higgsfield o Kling para movimiento, ffmpeg, Claude para el texto.
- **Margen:** 80%.
- **Saturación:** **media**. Hay SaaS en inglés y en AR es casi todo manual.
- **Recurrencia:** alta (rotación de cartera).
- **Anónimo:** sí.
- **Score: 6.** Riesgo: los portales integren la función (ver F21 en el estudio de 230 ideas).

#### 5. Headshots corporativos IA "uniformes de marca" para equipos (B2B, no consumidor)
- **Qué es:** el empleado manda selfies y la empresa recibe retratos homogéneos (mismo fondo, luz y vestimenta) para la web "Equipo", LinkedIn y credenciales. Las altas se suman por abono.
- **Cliente:** estudios jurídicos y contables, consultoras, inmobiliarias y empresas de 20-300 personas de LatAm.
- **Evidencia:** Aragon cobra **USD 45 por persona** en su plan Teams; HeadshotPro, **USD 39**; AI SuitUp, USD 25-37 ([fast.io, 2026](https://fast.io/resources/best-ai-headshot-generators-2026/); [Aragon Teams](https://www.aragon.ai/headshots-for-teams), consultados 2026-10-02).
- **Precio/ticket:** USD 15-30 por persona en LatAm, con versión "lista para usar"; USD 300-3.000 por empresa una sola vez más altas [estimación propia].
- **% automatizable:** 85%. Stack: Higgsfield o un LoRA tipo Flux por API; Claude para el control de consistencia; revisión de parecido.
- **Margen:** 85%.
- **Saturación:** **alta** en el autoservicio de EE.UU. y **media** en el B2B hispano "hecho por vos".
- **Recurrencia:** baja (solo altas).
- **Anónimo:** sí.
- **Score: 5,5.** Atención: son **datos biométricos** (Ley 25.326); hace falta consentimiento firmado y borrar las selfies.

#### 6. Fotos de stock para agencias de autos usados y concesionarias (fondo uniforme, patente difuminada)
- **Qué es:** el vendedor saca 12-20 fotos siguiendo una guía de ángulos; en menos de 2 h vuelven con fondo de showroom de la marca, exposición corregida, patente oculta y formato para ML, Marketplace y la web.
- **Cliente:** agencias multimarca de usados con 20-150 autos en stock y concesionarias oficiales (sector de usados).
- **Evidencia:** la edición manual tercerizada cuesta **USD 45-120 por vehículo** y la IA por lote menos de USD 0,50 por imagen; CarPixAI cobra USD 29-149/mes; Spyne procesa 15 fotos en menos de 60 s ([Photoroom, 2026](https://www.photoroom.com/blog/ai-car-photography-for-dealerships-cost-workflow-2026); [GetApp CarPixAI](https://www.getapp.com/all-software/a/carpixai/), consultados 2026-10-02).
- **Precio/ticket:** USD 3-6 por auto, o abono de USD 150-400/mes por agencia de 30-60 autos al mes [estimación propia].
- **% automatizable:** 85-90%. Stack: segmentación de auto, compositor de fondo con sombra de contacto, detección y blur de patente (OCR), Claude para la ficha.
- **Margen:** 85%.
- **Saturación:** **media**. Los SaaS existen pero son en inglés y autoservicio; la agencia argentina no los usa.
- **Recurrencia:** **alta** (el stock rota todos los meses).
- **Anónimo:** sí.
- **Score: 7.**

#### 7. Edición y culling al por mayor para fotógrafos de eventos
- **Qué es:** selección y edición de las galerías de fotógrafos de casamientos, eventos o deportes escolares.
- **Evidencia:** la edición IA cuesta **USD 0,05-0,10 por foto** (Imagen); la tercerización offshore, USD 0,20-0,50 (ShootDotEdit, FixThePhoto); ShootDotEdit cobra USD 119-299/mes y USD 0,16 por imagen en culling ([Imagen AI](https://imagen-ai.com/post/outsource-photo-editing-cost-per-image-2/); [FixThePhoto](https://fixthephoto.com/shootdotedit-review.html), consultados 2026-10-02).
- **Precio/ticket:** USD 50-150 por evento.
- **% automatizable:** 80% (Aftershoot e Imagen ya lo hacen).
- **Margen:** 50-70%.
- **Saturación:** **muy alta**.
- **Recurrencia:** alta en temporada.
- **Anónimo:** sí.
- **Score: 3.** Se incluye como contraejemplo: la IA de la propia herramienta del fotógrafo cuesta 5 centavos.

#### 8. Catálogo B2B en PDF y "catálogo WhatsApp" que se regenera solo desde la lista de precios (retoma H32 con motor de regeneración)
- **Qué es:** se conecta el Excel o Sheets de precios y stock de la distribuidora. Cada vez que cambian los precios (en AR, mensual o quincenal), la herramienta regenera el PDF con fotos, códigos, precios por lista (mayorista, minorista, revendedor), un flipbook web, imágenes por rubro para estados de WhatsApp y un video catálogo corto.
- **Cliente:** distribuidoras y mayoristas con vendedores en calle y revendedores (bazar, golosinas, ferretería, cosmética, repuestos).
- **Evidencia:** existen SaaS de catálogo desde CSV o Excel (Catalog Machine, Templated, Pagination) y apps de Shopify a **USD 19,90-99,90/mes** ([Templated](https://templated.io/alternative-to/catalog-machine/); [PickYourApp](https://pickyourapp.com/products/linesheet-pro), consultados 2026-10-02). En AR el dolor es la frecuencia de cambio de precios [inferencia, NO VERIFICADO con encuesta].
- **Precio/ticket:** setup de USD 300-800 más un abono de USD 80-250/mes por regeneraciones ilimitadas [estimación propia].
- **% automatizable:** **90-95%**. Stack: Python con Typst/WeasyPrint o ReportLab, plantillas HTML, ffmpeg para el video catálogo, Claude para descripciones y para detectar inconsistencias de precios (por ejemplo, margen negativo).
- **Margen:** 90%.
- **Saturación:** **baja** en AR, donde las distribuidoras usan Canva a mano o PDFs viejos.
- **Recurrencia:** **muy alta** (cada cambio de lista).
- **Anónimo:** sí.
- **Score: 7,5.** Es procesos más contenido, el cruce exacto con la ingeniería industrial; se combina con la idea 1.

#### 9. Fotos y video de menú para cadenas y dark kitchens multimarca (retoma E8 con ángulo de volumen)
- **Qué es:** se estandariza la carta completa (50-200 platos y marcas virtuales) para PedidosYa y Rappi: foto mejorada o generada desde una foto real, más un clip de 6-10 s por plato.
- **Cliente:** dark kitchens con 3-10 marcas y cadenas de 5-30 locales.
- **Evidencia:** según vendedores, los platos con fotos profesionales reciben hasta 30% más pedidos y las fichas con video entre 25% y 40% más ([Genra](https://genra.ai/es/blog/ai-video-restaurant-food-marketing-guide); [Teknofilo](https://www.teknofilo.com/las-fotos-de-la-comida-que-pides-a-domicilio-pueden-estar-generadas-por-la-ia-de-esta-empresa/), consultados 2026-10-02). Son cifras de vendedor, sesgadas.
- **Precio/ticket:** USD 3-8 por plato; USD 300-1.000 por proyecto más rotación de carta [estimación propia].
- **% automatizable:** 75%. Stack: Higgsfield, mejora sobre foto real (no inventar el plato).
- **Margen:** 80%.
- **Saturación:** **media**. Rubro de márgenes chicos.
- **Recurrencia:** baja-media.
- **Anónimo:** sí.
- **Score: 5.** Riesgo: una foto IA que no representa el plato puede violar políticas de las apps y generar reclamos de consumidores [NO VERIFICADO: política específica de PedidosYa].

### B. AUDIO

#### 10. Posproducción de podcasts B2B en marca blanca para productoras y agencias hispanas (retoma E12 con ángulo B2B2B)
- **Qué es:** el pipeline recibe el multipista y devuelve audio limpio y nivelado, cortes de muletillas, capítulos, show notes SEO, transcripción, 3-5 clips verticales y una newsletter. La productora o agencia revende con su marca.
- **Cliente:** productoras de podcasts corporativos, agencias de marketing B2B y consultoras con videopodcast.
- **Evidencia:** la edición básica cuesta USD 30-80 por episodio; la producción completa, **USD 150-350**; producción más redes, **USD 250-550**; las agencias medianas cobran **USD 1.500-3.000/mes** ([BizToolkit, 2026](https://www.biztoolkit.co/post/podcast-editor-rates-in-2026-per-episode-pricing-guide); [The Podcast Consultant](https://thepodcastconsultant.com/blog/podcast-editing-services), consultados 2026-10-02). En la edición de texto con IA (Descript), recortar muletillas reduce el tiempo de edición "más de la mitad" ([Descript](https://www.descript.com/blog/article/the-best-ai-tools-for-podcasters-from-scriptwriting-to-audio-editing-to-marketing-your-show)).
- **Precio/ticket:** a productoras, USD 40-100 por episodio en volumen; 20-40 episodios al mes = USD 800-4.000/mes [estimación propia].
- **% automatizable:** 70-80%. Stack: Whisper o Gemini para la transcripción, ffmpeg con loudnorm y denoise, cortes por transcripción, Claude para notas y capítulos, el clipper que ya está en cartera.
- **Margen:** 75%.
- **Saturación:** **alta** en inglés, **media** en español en marca blanca.
- **Recurrencia:** **alta**.
- **Anónimo:** sí (marca blanca ideal).
- **Score: 6,5.**

#### 11. Audiolibros con voz IA para editoriales chicas con fondo editorial (fuera de ACX)
- **Qué es:** se convierte el backlist de una editorial independiente en audiolibros para Spotify, Google Play, Apple y Kobo, con léxico de pronunciación, voces por personaje, QA auditivo y especificaciones de cada tienda.
- **Cliente:** editoriales independientes de AR, México y España, y universidades con editorial propia.
- **Evidencia:** **ACX prohíbe la narración TTS o IA no autorizada** (requisitos actualizados el 2026-04-15); Audible solo admite IA por Virtual Voice (KDP) y Voice Replica beta. Spotify, Google Play, Apple y Kobo aceptan IA con declaración ([InkfluenceAI, 2026](https://www.inkfluenceai.com/blog/ai-narration-audible-acx-policy-2026), consultado 2026-10-02, fuente secundaria). La narración humana cuesta **USD 200-400 por hora terminada**; los servicios IA, £60 PFH ([DEV](https://dev.to/stanlymt/ai-audiobook-pricing-what-to-charge-in-2026-27pp); [Walnut](https://audiobookone.walnutpublication.com/)). **Spotify da narración IA gratis con ElevenLabs a cualquier autor** ([Complete AI Training](https://completeaitraining.com/news/spotify-opens-ai-audiobook-narration-to-all-authors/)); Storytel tiene una alianza con ElevenLabs ([ElevenLabs](https://elevenlabs.io/es/blog/storytel-enters-strategic-partnership-with-elevenlabs-and-announces-upcoming-launch-of-new-voiceswitcher-feature)). En España hay unos 30-40 mil títulos de audiolibro en castellano ([Primicias](https://www.primicias.ec/ciencia-tecnologia/audiolibros-inteligencia-artificial-libros-voces-96685/)).
- **Precio/ticket:** USD 40-90 por hora terminada; libro de 8 h = USD 300-700; lote de 20 títulos = USD 6.000-14.000 una sola vez [estimación propia].
- **% automatizable:** 80%. Stack: ElevenLabs o Gemini TTS, Claude para diccionario y marcado de diálogos, ffmpeg para normas de loudness, escucha muestral.
- **Margen:** 70%.
- **Saturación:** **media**, pero con **absorción de plataforma ALTA** (gratis en Spotify).
- **Recurrencia:** baja (por lotes).
- **Anónimo:** sí.
- **Score: 5.** Lo que se vende es catálogo masivo, metadatos y distribución, no la voz. Verificar que la editorial tenga los derechos de audio.

#### 12. Remasterizado de bibliotecas de cursos y clases (audio limpio, capítulos, subtítulos, índice buscable)
- **Qué es:** institutos, academias y creadores con cientos de horas grabadas con mal audio pasan por lotes de limpieza, nivelación, capítulos con Claude, subtítulos y transcript buscable.
- **Cliente:** institutos terciarios privados, academias online hispanas y empresas con webinars acumulados.
- **Evidencia:** no encontré tarifas públicas específicas del nicho [NO VERIFICADO]. Como referencia, la transcripción y captions en español de Rev cuestan USD 3,25/min ([Rev support](https://support.rev.com/hc/en-us/articles/18893487380365-Pricing), consultado 2026-10-02).
- **Precio/ticket:** USD 15-40 por hora de contenido; un lote de 200 h = USD 3.000-8.000 [estimación propia].
- **% automatizable:** 85-90%. Stack: ffmpeg, DeepFilterNet o RNNoise, Whisper, Claude.
- **Margen:** 85%.
- **Saturación:** **baja-media**.
- **Recurrencia:** baja (lotes); abono por lo nuevo.
- **Anónimo:** sí.
- **Score: 6.**

#### 13. Voz de marca IA con licencia de un locutor real (IVR, e-learning, institucional)
- **Qué es:** se licencia la voz clonada de un locutor argentino o mexicano con revenue share y se vende "locución ilimitada con la misma voz" para centrales telefónicas, e-learning y tutoriales.
- **Cliente:** empresas con IVR y equipos de capacitación.
- **Evidencia:** [NO VERIFICADO] tarifas de locución en LatAm; ElevenLabs es autoservicio.
- **Precio/ticket:** USD 100-400/mes.
- **% automatizable:** 90%.
- **Margen:** 50-60% (el locutor cobra parte).
- **Saturación:** **media-alta**.
- **Recurrencia:** media.
- **Anónimo:** sí.
- **Score: 4,5.** Tiene riesgo de derechos de voz y contratos.

### C. TEXTO Y DISEÑO DESDE VIDEO

#### 14. Subtitulado de accesibilidad en español con QA para universidades y organismos (retoma L12 con ángulo regulatorio)
- **Qué es:** captions y transcripciones con calidad WCAG (precisión, identificación de hablantes, sonidos), en SRT/VTT, por lote.
- **Cliente:** universidades e institutos que publican en español; instituciones de EE.UU. con contenido en español; organismos y concesionarias de servicios públicos de AR.
- **Evidencia:**
  - **ADA Title II:** el DOJ publicó el 2026-04-20 un Interim Final Rule que **corre los plazos a 2027-04-26** (entidades de 50.000 habitantes o más) y **2028-04-26** (menores); el estándar sigue siendo WCAG 2.1 AA ([Federal Register](https://www.federalregister.gov/documents/2026/04/20/2026-07663/extension-of-compliance-dates-for-nondiscrimination-on-the-basis-of-disability-accessibility-of-web); [Plante Moran](https://plantemoran.com/explore-our-thinking/insight/2026/04/doj-extends-ada-title-ii-web-accessibility-compliance-deadlines), consultados 2026-10-02). Alcanza a universidades públicas y cubre contenido detrás de login ([Verbit](https://verbit.ai/accessibility-hub/ada-title-ii-update-mandates-digital-accessibility-for-colleges-and-universities-by-2026)).
  - **European Accessibility Act**, vigente desde 2025-06-28 para e-commerce: exige WCAG 2.1 AA con captions de video pregrabado en el sitio propio y exime a las microempresas (menos de 10 empleados y menos de EUR 2 M de facturación) ([accessible.org](https://accessible.org/eaa-ecommerce-services-requirements/); [MakeInfluence](https://www.makeinfluence.com/en/academy/eu-accessibility-act-and-caption-requirements-for-influencer-and-brand-video-content)).
  - **España:** RD 1112/2018 para el sector público y las universidades ([Univ. de Alicante](https://web.ua.es/en/accesibilidad/informacion-general.html)).
  - **Argentina:** Ley 26.653 y Decreto 656/2019 para el Estado, concesionarias y contratistas, con videos subtitulados ([Diario Judicial](https://www.diariojudicial.com/news-26857-para-que-accedan-todos-de-verdad); [argentina.gob.ar](https://www.argentina.gob.ar/normativa/nacional/175694/texto)).
  - **Referencias de precio:** Rev cobra USD 3,25/min por captions en español y USD 6,49/min por subtítulos traducidos ([Rev](https://support.rev.com/hc/en-us/articles/18893487380365-Pricing)).
- **Precio/ticket:** USD 1,2-2,5/min con QA humano; una universidad con 300 h/año = USD 20.000-45.000/año en teoría [estimación propia].
- **% automatizable:** 85-90%. Stack: Whisper large o Gemini, Claude para corrección contra glosario de la materia, reglas de segmentación (42 caracteres por línea), revisión por muestreo.
- **Margen:** 80%.
- **Saturación:** **ALTA** en inglés (3Play, Verbit, Rev, captions automáticos de YouTube y Zoom) y **media** en español con QA.
- **Recurrencia:** alta por contrato.
- **Anónimo:** **parcial**. Las universidades compran por proveedor registrado, licitación y VPAT; una marca sin persona visible y sin empresa formal tiene fricción.
- **Score: 5,5.** No vender por miedo: el plazo se corrió un año.

#### 15. Captions y versiones accesibles de videos de producto para tiendas que venden a la UE (EAA)
- **Qué es:** subtítulos, transcripción y audiodescripción breve de los videos del sitio propio para e-commerce de 10 empleados o más que venden a la UE.
- **Cliente:** tiendas online españolas medianas y marcas latinoamericanas con tienda en la UE.
- **Evidencia:** la EAA exige captions en el video del sitio o app propios, no automáticamente en redes ([MakeInfluence](https://www.makeinfluence.com/en/academy/eu-accessibility-act-and-caption-requirements-for-influencer-and-brand-video-content); [StoryStream](https://storystream.ai/blog/how-storystream-is-futureproofing-video-commerce-for-the-european-accessibility-act), consultados 2026-10-02).
- **Precio/ticket:** USD 200-800/mes [estimación propia].
- **% automatizable:** 85%.
- **Margen:** 85%.
- **Saturación:** **media** (agencias de accesibilidad europeas como Acolad).
- **Recurrencia:** media.
- **Anónimo:** sí.
- **Score: 5.** Mercado lejano y cobranza en EUR desde AR (requiere Payoneer o un merchant of record).

#### 16. Repurposing de webinars B2B en español (1 webinar → 15-25 piezas) (retoma E15 con ángulo B2B y SaaS)
- **Qué es:** el webinar o evento online se convierte en clips, artículo SEO, newsletter, carrusel de LinkedIn, secuencia de emails y quote cards.
- **Cliente:** SaaS y fintech hispanas y empresas B2B que hacen webinars mensuales.
- **Evidencia:** "Repurposing used to be a USD 4.000/month agency line item", hoy SaaS de USD 15-25/mes (Repurpose.io); Goldcast Content Lab cuesta USD 500-2.000/mes ([AIPromptsHub](https://aipromptshub.co/creator/ai-content-repurposing-tools-cost); [StackScored](https://www.stackscored.com/pricing/virtual-events/goldcast/), consultados 2026-10-02).
- **Precio/ticket:** USD 400-1.500/mes [estimación propia].
- **% automatizable:** 75%.
- **Margen:** 85%.
- **Saturación:** **media-alta** (el SaaS lo comoditiza).
- **Recurrencia:** alta.
- **Anónimo:** sí.
- **Score: 5,5.** El valor está en el criterio editorial, no en el corte.

#### 17. Miniaturas por suscripción con variantes A/B para canales medianos
- **Qué es:** 3 variantes por video para "Test & Compare" de YouTube, con plantillas de marca.
- **Evidencia:** USD 5-30 en Fiverr (promedio USD 18); los especialistas cobran USD 100-300; retainers de USD 500-2.000/mes ([AdSnipper](https://adsnipper.com/?p=2496); [Overseer](https://www.overseeros.com/blog/youtube-agency-pricing-guide), consultados 2026-10-02).
- **Precio/ticket:** USD 300-1.000/mes.
- **% automatizable:** 50-60%. Stack: Higgsfield, plantillas, Claude para conceptos.
- **Margen:** 85%.
- **Saturación:** **ALTA**.
- **Recurrencia:** alta.
- **Anónimo:** sí.
- **Score: 4,5.** Depende del gusto y de la CTR, no del pipeline.

#### 18. Sets de imágenes de listing y contenido A+ por ASIN para marcas en Amazon (EE.UU. y México) y fichas premium en ML
- **Qué es:** 7 imágenes por producto (hero, infografías de atributos, lifestyle, medidas, comparativa) más los módulos A+, generados con plantillas y revisados.
- **Cliente:** marcas propias que venden en Amazon (muchos sellers hispanos en EE.UU. y México).
- **Evidencia:** A+ cuesta **USD 199 por ASIN (estándar) y USD 499 (premium)**; un paquete de listing de 7 imágenes, **USD 795**; listing más A+, **USD 1.195 por ASIN**; la optimización completa, USD 3.000 por ASIN ([Bonnie Sorsby](https://bonniesorsby.com/amazon-listing-photography-design-pricing/); [publishing.co.uk](https://publishing.co.uk/guides/a-plus-content-services-compared/), consultados 2026-10-02).
- **Precio/ticket:** USD 150-400 por ASIN; una marca con 5-15 ASIN = USD 750-6.000 por proyecto más altas [estimación propia].
- **% automatizable:** 60-70%. Stack: plantillas HTML→PNG, Claude para el copy de beneficios, Higgsfield para lifestyle. El diseño exige ojo.
- **Margen:** 85%.
- **Saturación:** **media-alta** en inglés y **media** en Amazon México.
- **Recurrencia:** media (lanzamientos).
- **Anónimo:** sí (rubro 100% remoto).
- **Score: 6,5.** El ticket por unidad es de los más altos del informe.

### D. FORMACIÓN

#### 19. De manual o PowerPoint de inducción a microvideos con voz IA más SCORM (e-learning corporativo LatAm)
- **Qué es:** los PPT y PDF de inducción, compliance o producto se convierten en microvideos de 2-5 min con voz IA (o avatar sin cara real), subtítulos, quiz y paquete SCORM para el LMS. La actualización se hace por abono.
- **Cliente:** RR.HH. y capacitación de empresas de 200-2.000 empleados, cadenas de retail, bancos regionales y cooperativas.
- **Evidencia:** la producción tradicional cuesta **USD 1.000-3.000 por minuto** y un módulo, **USD 5.000-10.000** ([Vidpros](https://vidpros.com/corporate-training-video-production/); [Vidizmo](https://vidizmo.ai/blog/manufacturing-training-with-video), consultados 2026-10-02). Synthesia Creator cuesta USD 67/mes (unos USD 1,97 por minuto efectivo) y tiene SCORM en planes altos ([Arcade](https://www.arcade.software/post/synthesia-pricing); [anam.ai](https://anam.ai/blog/heygen-vs-synthesia)). Würth informa 80% menos de costo de traducción con HeyGen ([HeyGen](https://www.heygen.com/use-cases/corporate-training); dato del vendedor).
- **Precio/ticket:** USD 80-200 por minuto terminado; un proyecto de 15 microvideos = USD 1.500-5.000, más un abono de actualización de USD 200-600/mes [estimación propia].
- **% automatizable:** 70%. Stack: Claude para guion, pedagogía y quiz; ElevenLabs o HeyGen por API; slides renderizados con Remotion o ffmpeg; Whisper para subtítulos; empaquetado SCORM con plantilla.
- **Margen:** 80%.
- **Saturación:** **media**. Las herramientas existen, pero los equipos de RR.HH. de LatAm no tienen tiempo ni guionista.
- **Recurrencia:** media-alta (cambios de proceso, nuevos ingresos).
- **Anónimo:** **parcial**. Lo corporativo quiere una persona que responda (por videollamada sin cámara o por email).
- **Score: 7,5.**

#### 20. Videos de SOP y seguridad para operarios de planta, con QR en el puesto (retoma C22 con el formato video)
- **Qué es:** cada SOP o instrucción de trabajo se convierte en un video de 60-120 s: el supervisor filma con el celular siguiendo una guía de tomas y la herramienta corta, subtitula, agrega voz IA en español neutro (y en guaraní o portugués si hay operarios extranjeros), resalta los EPP y genera un QR para pegar en la máquina. Abono de actualización con cada cambio de proceso.
- **Cliente:** PyMEs industriales (alimentos, metalmecánica, plásticos), depósitos y centros logísticos, frigoríficos.
- **Evidencia:** la producción tradicional de un video de manufactura cuesta USD 15.000-30.000 y el formato microlearning crece porque la retención cae después de los 6 min ([Vidizmo](https://vidizmo.ai/blog/manufacturing-training-with-video), consultado 2026-10-02). Hay SaaS específicos (Knowlify, USD 29-399/mes) ([Knowlify](https://knowlify.com/manufacturing-training-videos)), en inglés. En AR, la capacitación en higiene y seguridad es obligatoria por la Ley 19.587 y el Decreto 351/79 [NO VERIFICADO el detalle del artículo en esta sesión].
- **Precio/ticket:** proyecto de 20-50 SOPs = USD 1.500-6.000; abono de USD 200-500/mes por actualizaciones y nuevos puestos [estimación propia].
- **% automatizable:** 60-70%. El rodaje lo hace el cliente con la guía; el guion sale de su SOP en papel o de la idea C22. Stack: Whisper, Claude para guion y puntos de control, ElevenLabs, ffmpeg para overlays, generador de QR y página estática en Cloudflare.
- **Margen:** 85%.
- **Saturación:** **BAJA** en AR y LatAm en español.
- **Recurrencia:** media-alta.
- **Anónimo:** parcial. Se vende por email, pero la planta valora el título de ingeniero; la marca puede ser anónima con firma profesional.
- **Score: 8.** Es el mejor fit con su perfil y se vende junto con la consultora de procesos.

#### 21. Videos de ayuda y onboarding de software que se regeneran cuando cambia la interfaz (SaaS y fintech LatAm)
- **Qué es:** un script de navegación (Playwright) graba los flujos clave de la app del cliente, Claude escribe la locución, se agregan voz IA y zooms, y se exporta a la base de ayuda. Cuando cambia la interfaz, se vuelve a correr.
- **Cliente:** SaaS B2B hispanos, fintech y software de gestión (ERP para PyMEs).
- **Evidencia:** hay herramientas del rubro (Guidde, VibrantSnap) ([Guidde](https://www.guidde.com/knowledge-hub/types-of-training-videos-and-their-uses-complete-guide); [VibrantSnap, 2026-09-14](https://www.vibrantsnap.com/blog/how-to-make-training-videos)); precios de servicio [NO VERIFICADO].
- **Precio/ticket:** USD 800-2.500/mes [estimación propia].
- **% automatizable:** 75%.
- **Margen:** 85%.
- **Saturación:** **baja-media**.
- **Recurrencia:** alta.
- **Anónimo:** sí.
- **Score: 6.** Pide mantenimiento técnico de scripts (Claude Code lo hace, pero hay fricción).

### E. DEPORTES Y EVENTOS

#### 22. Reels de scouting y reclutamiento en marca blanca para academias y agencias de becas
- **Qué es:** la academia o agencia manda partidos completos de 20-40 jugadores. Se devuelve un reel de 3-5 min por jugador (las acciones marcadas, con spotlight del jugador), una ficha con datos y una versión en inglés para coaches de EE.UU. o clubes de Europa.
- **Cliente:** agencias de becas deportivas a EE.UU. y academias privadas de fútbol, hockey y básquet en AR, que es un gran exportador de jugadores.
- **Evidencia:** un reel básico cuesta **USD 500** y un paquete full con outreach, **USD 5.000 o más** ([Veo](https://www.veo.com/article/how-much-does-a-recruiting-video-cost)); los servicios directos, desde **USD 149-150** ([Contra](https://contra.com/s/lQNosckR-complete-soccer-recruiting-package); [Gumroad](https://prohighlight.gumroad.com/l/soccerhighlightvideo)); el reel ideal dura 3-5 min. Hay torneos y agencias que llevan juveniles argentinos a EE.UU. ([Mercado](https://mercado.com.ar/varios/becas-deportivas-en-estados-unidos), consultados 2026-10-02).
- **Precio/ticket:** a agencias, USD 40-120 por jugador; un lote de 30 = USD 1.200-3.600 por temporada [estimación propia].
- **% automatizable:** 40-60%. Stack: tracking de jugador con YOLO y ByteTrack, marcado de acciones asistido (el humano marca y la herramienta corta), ffmpeg para el spotlight. El "ojo" de qué acción mostrar sigue siendo humano.
- **Margen:** 75%.
- **Saturación:** **media** (Fiverr para el consumidor final; poco en marca blanca B2B en español).
- **Recurrencia:** estacional (ventanas de reclutamiento).
- **Anónimo:** sí.
- **Score: 6,5.**

#### 23. Highlights automáticos para complejos de fútbol 5/7 y torneos amateur
- **Qué es:** una cámara fija por cancha y highlights automáticos por turno, vendidos a los jugadores o incluidos en el alquiler.
- **Evidencia:** Veo cobra desde £999/año más la cámara; Pixellot levantó USD 35 M en 2026 para un modelo de revenue share que elimina el costo de la cámara, con 16.000 sistemas en EE.UU. ([Pulse 2.0](https://pulse2.com/pixellot-35-million-closed-to-expand-ai-driven-youth-sports-streaming-and-monetization/amp/); [toolmage](https://www.toolmage.com/en/tool/veo/), consultados 2026-10-02).
- **Precio/ticket:** USD 150-500/mes por complejo.
- **% automatizable:** 70% una vez instalado, pero la detección de gol es difícil.
- **Margen:** 50% (hardware).
- **Saturación:** **media**, con incumbentes de hardware.
- **Recurrencia:** alta.
- **Anónimo:** **no** (requiere instalar en el lugar).
- **Score: 3,5.** Sin hardware no existe y con hardware ya no es "solo compu".

#### 24. Editor backend de recaps de eventos corporativos (same-day edit) para productoras de eventos
- **Qué es:** el fotógrafo o filmmaker del evento sube el material crudo durante el día y la herramienta arma 1 recap de 60-90 s y 5 reels verticales con logos y graphics del evento, el mismo día. Se vende a la productora, no a la empresa.
- **Cliente:** productoras de eventos corporativos, congresos y lanzamientos (AR y LatAm).
- **Evidencia:** en NYC un recap de medio día cuesta USD 1.500-3.000; el same-day edit lleva un recargo de 25-50% ([Clip Charm](https://clip-charm-works.lovable.app/blog/event-video-production-cost-nyc); [FotoOwl](https://fotoowl.ai/blogs/corporate-event-photography-complete-buyers-guide-2026), consultados 2026-10-02).
- **Precio/ticket:** USD 150-400 por evento a la productora; 4-10 eventos al mes = USD 600-4.000/mes [estimación propia].
- **% automatizable:** 50-60%. Stack: detección de escenas, mejores tomas por calidad y caras, beat-sync con la música, plantillas; el armado final necesita ojo.
- **Margen:** 80%.
- **Saturación:** **media**.
- **Recurrencia:** alta con 2-3 productoras.
- **Anónimo:** sí (marca blanca).
- **Score: 5,5.**

#### 25. Pre-edición ("rough cut") automática para videógrafos de casamientos y quinceañeras (marca blanca)
- **Qué es:** 6-10 h de material entran al pipeline, que ordena, sincroniza audio, marca votos, discursos y momentos clave y entrega un primer corte del resumen para que el videógrafo termine.
- **Cliente:** videógrafos de bodas de AR, México y España.
- **Evidencia:** hay herramientas de highlights de boda (MomentCut, VIDIO), sin tarifas claras ([Contra MomentCut](https://contra.com/p/MZANRvO7-moment-cut-ai-video-highlight-tool); [VIDIO](https://www.vidio.ai/tools/wedding-highlight-maker), consultados 2026-10-02).
- **Precio/ticket:** USD 50-150 por boda; USD 300-1.500/mes en temporada [estimación propia].
- **% automatizable:** 60%.
- **Margen:** 85%.
- **Saturación:** **media**.
- **Recurrencia:** estacional.
- **Anónimo:** sí.
- **Score: 5.**

### F. COMERCIO

#### 26. Del feed de productos a videos por SKU para Clips de Mercado Libre y catálogos de Meta/TikTok
- **Qué es:** se conecta el catálogo (export de ML, Tiendanube o planilla) y por cada SKU se genera un video vertical de 10-30 s con fotos, movimiento IA en los productos estrella, precio, cuotas y beneficios, más la versión para el catálogo de anuncios. Abono por las altas y por los cambios de precio.
- **Cliente:** sellers de ML con 200-5.000 publicaciones (Mercado Líder Platinum) y marcas de Tiendanube que hacen anuncios de catálogo.
- **Evidencia:** según ML, los sellers vieron **+500% de visitas** con Clips; en 2024 Clips acumuló **5.600 millones de vistas y 70 millones de espectadores** en la región ([RCN](https://www.noticiasrcn.com/economia/mercado-libre-se-une-a-la-revolucion-de-videos-cortos-465304); [Algoritmo Digital, 2026](https://algoritmodigital.com.ar/?p=2950), consultados 2026-10-02; dato del vendedor). En el exterior ya hay SaaS de feed a video (Wavemaker para catálogos de 12 a 100.000 SKUs; GliaCloud) ([Wavemaker](https://wavemaker.adwave.com/product/catalog-video-ads); [GliaCloud](https://gliacloud.com/en/blog/automated-video-ads-for-e-commerce-scale-without-increasing-costs/)).
- **Precio/ticket:** USD 1-3 por video; USD 300-1.500/mes por seller grande [estimación propia].
- **% automatizable:** **90%**. Stack: Python con ffmpeg o Remotion, plantillas por rubro, Higgsfield image-to-video solo en el top 10% de SKUs, Claude para los "3 beneficios" de cada ficha.
- **Margen:** 85-90%.
- **Saturación:** **baja** en ML/AR.
- **Recurrencia:** **alta**.
- **Anónimo:** sí.
- **Score: 8.** Riesgo a verificar: si Clips permite **carga masiva** o solo desde la app, la subida es manual y quedaría a cargo del seller [NO VERIFICADO]. También puede que ML genere los clips automáticamente en el futuro.

#### 27. Video del stock de concesionarias (walkaround desde fotos más ficha) — upsell de la idea 6
- **Qué es:** con las mismas fotos de la idea 6, la herramienta arma un video vertical por auto con especificaciones, precio y cuotas para Marketplace, IG, TikTok y ML.
- **Cliente:** agencias de usados.
- **Evidencia:** el AI batch procesa el set completo de un vehículo en menos de 60 s (Spyne) ([Photoroom](https://www.photoroom.com/blog/ai-car-photography-for-dealerships-cost-workflow-2026)); precio de servicio en AR [NO VERIFICADO].
- **Precio/ticket:** USD 2-5 por auto adicional; abono combinado con la idea 6 de USD 250-600/mes [estimación propia].
- **% automatizable:** 90%.
- **Margen:** 85%.
- **Saturación:** **baja-media**.
- **Recurrencia:** alta.
- **Anónimo:** sí.
- **Score: 6,5.** Sumada a la idea 6 da un **7**.

#### 28. Pantallas de precios y menú que se actualizan solas desde la planilla (digital signage para cadenas)
- **Qué es:** la cadena (farmacias, gimnasios, panaderías, heladerías, franquicias gastronómicas) cambia el precio en el Sheet y cada pantalla del local muestra un loop de video regenerado con promos, combos y fotos. Es ideal en contexto inflacionario.
- **Cliente:** cadenas de 3-50 locales con TV o pantallas.
- **Evidencia:** el software de señalética cuesta **USD 20-80 por pantalla al mes**; las cadenas de fast food pagan **£300-500 por local al mes** en actualizaciones y soporte ([Smartersign](https://smartersign.com/articles/how-much-do-digital-menu-boards-cost); [Amplitude](https://www.amplitudenet.pt/en/restaurants-costs-digital/), consultados 2026-10-02); MustHaveMenus cobra USD 19-49/mes por diseño ([Intercom MHM](https://intercom.help/musthavemenus-289b0117ae34/en/articles/11556956-plan-options-pricing)).
- **Precio/ticket:** USD 40-120 por pantalla al mes; una cadena de 10 locales = USD 400-1.200/mes [estimación propia].
- **% automatizable:** **90-95%**. Stack: Sheets como fuente, Python que renderiza HTML a MP4, Claude para textos de promo y detección de errores de precio, distribución por un player barato (Chromecast o stick Android con URL de Cloudflare).
- **Margen:** 85%.
- **Saturación:** **baja-media** en AR.
- **Recurrencia:** **muy alta**.
- **Anónimo:** sí, salvo la instalación inicial, que hace el cliente con una guía.
- **Score: 7.**

#### 29. Videos y fotos semanales para Google Business Profile de cadenas multi-sucursal
- **Qué es:** publicaciones semanales automáticas por sucursal (fotos, video corto y oferta) para mejorar la ficha local.
- **Cliente:** cadenas de 5-50 sucursales (ópticas, gomerías, farmacias).
- **Evidencia:** [NO VERIFICADO] (no busqué el impacto de video en GBP en esta sesión).
- **Precio/ticket:** USD 20-50 por sucursal al mes.
- **% automatizable:** 85%.
- **Margen:** 85%.
- **Saturación:** **media** (las agencias de SEO local lo hacen).
- **Recurrencia:** alta.
- **Anónimo:** sí.
- **Score: 5.**

### G. DATOS Y VIDEO

#### 30. Video-reporte mensual personalizado por cliente final: consorcios, inmobiliarias (rendición al propietario) y estudios contables
- **Qué es:** el administrador o estudio exporta la planilla de cada edificio, propietario o cliente. La herramienta genera por cada uno un video de 60-90 s con gráficos ("tus expensas subieron 8%: 5 puntos por paritaria de encargado, 3 por ascensor"), voz IA y el PDF. Se envía por WhatsApp o email.
- **Cliente:** administradores de consorcios (30-150 edificios), inmobiliarias que administran alquileres y estudios contables con 50-300 clientes PyME.
- **Evidencia:** existen soluciones en finanzas: **Digital Rapport** (app de Xero, video-reportes mensuales y trimestrales para contadores) y **Croesus Vidia** (estados de cartera en video) ([Xero Apps](https://apps.xero.com/au/app/digital-rapport); [Investment Executive](https://www.investmentexecutive.com/partner-content/brand-knowledge/croesus/croesus-vidia-brings-investment-information-to-life/), consultados 2026-10-02). Las cifras de retención "+95%" son del vendedor. En español para consorcios o rendiciones no encontré nada [NO VERIFICADO: ausencia].
- **Precio/ticket:** USD 1-5 por video; USD 150-600/mes por administración o estudio [estimación propia].
- **% automatizable:** **95%**. Stack: Excel a Python; Claude para la narrativa con reglas ("no inventar causas"); TTS; Remotion o matplotlib más ffmpeg; revisión por muestreo.
- **Margen:** 90%.
- **Saturación:** **BAJA**.
- **Recurrencia:** **muy alta** (mensual por naturaleza).
- **Anónimo:** sí.
- **Score: 7,5.** Riesgos: datos personales (Ley 25.326, hace falta un contrato de encargado de tratamiento) y el error de un número en el video de un vecino enojado. La revisión no es opcional.

#### 31. Informe de avance de obra mensual en video para desarrolladoras y fideicomisos
- **Qué es:** el jefe de obra saca fotos desde 6-10 puntos fijos marcados, cada semana. La herramienta arma el timelapse comparativo, la curva S de avance real contra el plan (desde el cronograma en Excel), el informe PDF y un video de 90 s para inversores con narración IA.
- **Cliente:** desarrolladoras medianas y fideicomisos al costo (sus inversores exigen informes) en AR y Uruguay; constructoras PyME.
- **Evidencia:** el monitoreo mensual con dron se cobra **USD 1.200-3.000 por obra al mes** y como retainer ([Unmanned Aerial](https://unmanned-aerial.com/monthly-construction-progress-capture-with-drones/)); hay paquetes de USD 199 por visita mensual con timelapse final ([Dronegenuity](https://www.dronegenuity.com/product/construction-progress-drone-media-12-site-visits/), consultados 2026-10-02).
- **Precio/ticket:** USD 100-300 por obra al mes sin dron (fotos del cliente); una desarrolladora con 4 obras = USD 400-1.200/mes [estimación propia].
- **% automatizable:** 80%. Stack: alineación de fotos (OpenCV), ffmpeg, Claude para el informe a partir de cronograma y fotos, gráficos de curva S.
- **Margen:** 90%.
- **Saturación:** **BAJA** en la versión sin dron y en español.
- **Recurrencia:** **alta** (12-30 meses por obra).
- **Anónimo:** sí.
- **Score: 7,5.** La planificación y control de obra es ingeniería industrial pura.

#### 32. Videos personalizados a escala para outbound y retención (nombre y web del prospecto)
- **Qué es:** campañas de miles de videos personalizados para equipos de ventas.
- **Evidencia:** Sendspark cuesta **USD 49/mes con 5.000 videos**; Tavus, USD 59-397/mes más uso ([Sendspark pricing](https://sendspark.com/pricing); [Fluxnote](https://fluxnote.io/guides/tavus-pricing), consultados 2026-10-02).
- **Precio/ticket:** USD 500-1.500/mes.
- **% automatizable:** 90%.
- **Margen:** 85%.
- **Saturación:** **ALTA**. El SaaS de USD 49 lo hace autoservicio.
- **Recurrencia:** media.
- **Anónimo:** sí.
- **Score: 4.**

#### 33. Biblioteca de videos de educación al paciente en español, licenciada por consultorio
- **Qué es:** se produce **una vez** una biblioteca de 40-80 videos (implantes, ortodoncia, blanqueamiento, cuidados posoperatorios) con voz IA y animación, y se licencia con el logo del consultorio para la sala de espera, la web y WhatsApp.
- **Cliente:** consultorios odontológicos y de estética de AR y LatAm.
- **Evidencia:** en EE.UU., Optio cobra USD 49/mes por la biblioteca, USD 69/mes por la TV de sala de espera y USD 99 el bundle; Consult-PRO, desde USD 99/mes ([Optio](https://optiopublishing.com/order); [G2 Consult-PRO](https://www.g2.com/products/consult-pro/discuss), consultados 2026-10-02).
- **Precio/ticket:** USD 20-50/mes por consultorio [estimación propia].
- **% automatizable:** 90% una vez armada la biblioteca (semi-pasivo).
- **Margen:** 90%.
- **Saturación:** **baja** en español.
- **Recurrencia:** alta.
- **Anónimo:** sí.
- **Score: 5,5.** Necesita revisión clínica de un odontólogo (contenido médico), ticket bajo por cliente y churn de consultorios.

---

## Top 5 para este usuario

| # | Idea | Por qué |
|---|---|---|
| 20 | **Videos de SOP y seguridad para operarios, con QR** | Saturación baja, recurrencia por cambios de proceso, se vende junto con la consultora de procesos (C22) y usa su título. El cliente filma y la herramienta hace el resto. |
| 26 | **Del feed de productos a videos por SKU para Clips de ML y Meta** | 90% automatizable y abono por volumen. ML empuja el video (dato del vendedor: +500% de visitas). Riesgo a verificar: carga masiva. |
| 8 (+1) | **Catálogo B2B que se regenera solo desde la lista de precios** (con fotos normalizadas) | La inflación argentina convierte un entregable de una vez en abono; 90-95% automatizable; es procesos más contenido. |
| 31 | **Informe de avance de obra en video para desarrolladoras y fideicomisos** | Ticket por obra y 12-30 meses de recurrencia; no hay competencia hispana sin dron; usa planificación y control. |
| 30 | **Video-reporte mensual por cliente final (consorcios, rendiciones, contadores)** | 95% automatizable, recurrencia mensual natural, saturación baja. Hay que cuidar los datos personales. |

**Cerca del podio:** la idea 19 (de PPT de inducción a microvideos más SCORM, 7,5), con ticket alto pero venta corporativa más lenta y menos anónima; y la 6 más la 27 (concesionarias, 7), con recurrencia alta y SaaS gringos que no llegan al usuario argentino.

## Los más automatizables (≥ 90% con herramienta propia)

1. **30. Video-reporte mensual** (95%): Excel → Claude → TTS → render. El humano revisa por muestreo.
2. **8. Catálogo regenerable** (90-95%): plantilla más datos; el humano solo aprueba el PDF.
3. **28. Pantallas que se actualizan desde la planilla** (90-95%).
4. **26. Del feed a videos por SKU** (90%).
5. **27. Video del stock de concesionarias** (90%) y **6. fotos de autos** (85-90%).
6. **14 y 12. Subtitulado y remasterizado de audio** (85-90%). Están muy automatizados, pero el mercado en inglés está comoditizado.

Patrón: **lo más automatizable es lo que parte de DATOS ESTRUCTURADOS (planillas, feeds, cronogramas) y no de material creativo crudo.** Ahí la IA no tiene que "tener gusto": formatea, narra y renderiza. Las ideas con material crudo (eventos, deportes, bodas, miniaturas) quedan en 40-60%.

## Trampas

1. **Foto "por imagen" = commodity global.** La edición con IA cuesta USD 0,05-0,10 por foto y la offshore USD 0,20-0,50 (ideas 3 y 7). Competir por imagen contra Bangladesh y contra la IA de la propia herramienta del cliente es perder. Hay que vender **flujo y abono** (catálogo, stock, cartera), nunca "fotos editadas".
2. **La plataforma absorbe el servicio.** Tiendanube ya tiene fondo automático y Lumi Studio; Spotify da narración IA gratis; YouTube y Zoom subtitulan solos; ML puede automatizar Clips. Para cada idea, preguntar si la plataforma lo va a hacer gratis en 12 meses (regla ya anotada en el estudio de 230 ideas).
3. **ACX y Audible no admiten TTS externo** (requisitos del 2026-04-15). Un servicio de audiolibros IA "para Audible" que no use Virtual Voice o Voice Replica es venderle humo al cliente.
4. **Vender por miedo regulatorio con plazos que se mueven.** ADA Title II se corrió a 2027-04-26 y 2028-04-26 (IFR del 2026-04-20). La EAA exime a las microempresas y solo obliga en el sitio o app propios, no en redes. Además, las universidades compran por licitación y con proveedor registrado, no por email frío anónimo.
5. **Cifras de impacto del vendedor.** "+500% de visitas" (ML Clips), "+30% de pedidos" (fotos de menú) y "+95% de retención" (video-reportes) salen de quienes venden la herramienta. En la propuesta al cliente, usar pilotos medidos propios, no esos números.
6. **Hardware y presencia física.** Los highlights de complejos y pádel (PlaySight, PUSHIT, Pixellot con USD 35 M de funding) piden cámaras instaladas; no es un negocio de "compu sola" ni anónimo.
7. **Datos personales y biométricos.** Headshots (selfies), video-reportes de consorcios y rendiciones: Ley 25.326, consentimiento, contrato de encargado de tratamiento y borrado. Un error en el video de un propietario es un reclamo.
8. **IA que "inventa" el producto.** Fotos de menú generadas, prendas en modelo con caída irreal o autos con detalles alterados pueden caer en publicidad engañosa y reclamos. La regla es mejorar la foto real, no reemplazarla.
9. **Ticket por unidad bajo × volumen que no llega.** USD 1-5 por video o foto solo cierra con clientes grandes. Con 5 clientes chicos el abono no paga el tiempo de revisión. Conviene apuntar a 3-5 cuentas medianas antes que a 50 chicas.
10. **"Marca anónima" en lo corporativo.** RR.HH., plantas y universidades quieren una persona y una factura. Se resuelve con marca sin cara, pero con firma profesional, contrato y facturación (monotributo o merchant of record). No se resuelve con anonimato total.

---

## Fuentes principales (todas consultadas el 2026-10-02)

- Federal Register, IFR ADA Title II, 2026-04-20: https://www.federalregister.gov/documents/2026/04/20/2026-07663/extension-of-compliance-dates-for-nondiscrimination-on-the-basis-of-disability-accessibility-of-web
- Plante Moran (2026-04): https://plantemoran.com/explore-our-thinking/insight/2026/04/doj-extends-ada-title-ii-web-accessibility-compliance-deadlines
- EAA e-commerce: https://accessible.org/eaa-ecommerce-services-requirements/ · https://www.makeinfluence.com/en/academy/eu-accessibility-act-and-caption-requirements-for-influencer-and-brand-video-content
- Ley 26.653 / Dto. 656/2019: https://www.argentina.gob.ar/normativa/nacional/175694/texto
- RD 1112/2018 (Univ. Alicante): https://web.ua.es/en/accesibilidad/informacion-general.html
- ACX / IA 2026: https://www.inkfluenceai.com/blog/ai-narration-audible-acx-policy-2026
- Spotify + ElevenLabs: https://completeaitraining.com/news/spotify-opens-ai-audiobook-narration-to-all-authors/
- Storytel + ElevenLabs: https://elevenlabs.io/es/blog/storytel-enters-strategic-partnership-with-elevenlabs-and-announces-upcoming-launch-of-new-voiceswitcher-feature
- Precios de edición de fotos 2026 (Imagen AI, con conflicto de interés): https://imagen-ai.com/post/outsource-photo-editing-cost-per-image/
- Autos: https://www.photoroom.com/blog/ai-car-photography-for-dealerships-cost-workflow-2026 · https://www.getapp.com/all-software/a/carpixai/
- Headshots: https://fast.io/resources/best-ai-headshot-generators-2026/
- Botika: https://botika.io/pricing
- Tiendanube IA: https://ayuda.tiendanube.com/es_AR/fotos-del-producto/editar-imagenes-para-tus-productos-tiendanube-usando-inteligencia-artificial
- Podcasts: https://www.biztoolkit.co/post/podcast-editor-rates-in-2026-per-episode-pricing-guide
- Rev: https://support.rev.com/hc/en-us/articles/18893487380365-Pricing
- Repurposing: https://aipromptshub.co/creator/ai-content-repurposing-tools-cost
- Miniaturas: https://adsnipper.com/?p=2496
- Amazon A+: https://bonniesorsby.com/amazon-listing-photography-design-pricing/
- Video de capacitación: https://vidpros.com/corporate-training-video-production/ · https://vidizmo.ai/blog/manufacturing-training-with-video · https://knowlify.com/manufacturing-training-videos
- Synthesia: https://www.arcade.software/post/synthesia-pricing
- Recruiting deportivo: https://www.veo.com/article/how-much-does-a-recruiting-video-cost
- Pixellot: https://pulse2.com/pixellot-35-million-closed-to-expand-ai-driven-youth-sports-streaming-and-monetization/amp/
- Eventos: https://clip-charm-works.lovable.app/blog/event-video-production-cost-nyc
- ML Clips: https://www.noticiasrcn.com/economia/mercado-libre-se-une-a-la-revolucion-de-videos-cortos-465304 · https://algoritmodigital.com.ar/?p=2950
- Feed a video: https://wavemaker.adwave.com/product/catalog-video-ads
- Inmobiliario: https://www.capterra.com/p/10045003/Reeltors-ai/ · https://www.capterra.com/p/10037342/Reel-E/
- Señalética: https://smartersign.com/articles/how-much-do-digital-menu-boards-cost
- Video-reportes: https://apps.xero.com/au/app/digital-rapport
- Obra: https://unmanned-aerial.com/monthly-construction-progress-capture-with-drones/ · https://www.dronegenuity.com/product/construction-progress-drone-media-12-site-visits/
- Odontología: https://optiopublishing.com/order
- Sendspark: https://sendspark.com/pricing
- Catálogos PDF: https://templated.io/alternative-to/catalog-machine/

**Pendientes de verificación:** (a) si ML Clips admite carga masiva o por API; (b) los artículos exactos de capacitación del Decreto 351/79; (c) las tarifas reales de edición y video inmobiliario en AR; (d) la política de PedidosYa y Rappi sobre fotos generadas con IA; (e) el impacto del video en Google Business Profile.
