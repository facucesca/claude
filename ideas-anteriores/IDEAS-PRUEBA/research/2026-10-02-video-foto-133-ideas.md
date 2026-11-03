# Video y foto con marca anónima: 133 ideas + diseño del sistema

**Fecha:** 2026-10-02
**Pedido del usuario:** las ideas anteriores están "quemadas" y dan poca plata. Quiere ir más a fondo en video y fotos para negocios (editar, crear con IA, automatizar):
- operar **con una marca, sin mostrar la cara**;
- conseguir clientes por **email frío a ~100 negocios**;
- tener una **herramienta propia que edite sola** (el cliente sube los videos, el sistema los edita y él revisa y entrega);
- investigar este rubro y los parecidos, y traer ~100 ideas.

---

## 0. Método

5 frentes investigados en paralelo, con ~190 búsquedas + ~45 lecturas directas el 2026-10-02:

| Frente | Ideas | Informe |
|---|---|---|
| M. Mercado de video: dónde está la plata | 34 | [video-mercado-nichos](fuentes/2026-10-02-video-mercado-nichos.md) |
| T. Herramienta de auto-edición (construir vs. comprar) | 20 | [video-herramienta-autoedicion](fuentes/2026-10-02-video-herramienta-autoedicion.md) |
| O. Outbound por email con marca anónima | 18 | [video-outbound-marca-anonima](fuentes/2026-10-02-video-outbound-marca-anonima.md) |
| N. Video y foto con IA generativa | 28 | [video-ia-generativa](fuentes/2026-10-02-video-ia-generativa.md) |
| R. Rubros parecidos automatizables | 33 | [video-rubros-parecidos](fuentes/2026-10-02-video-rubros-parecidos.md) |
| **Total** | **133** | Hay solapamiento entre frentes, a propósito: el mismo nicho visto desde el mercado, la herramienta, la IA y la venta |

**Advertencia de fuentes:** casi todos los precios del rubro vienen de **blogs de las propias agencias y herramientas** (marcados ⚠ en los informes). Sirven como **techo, no como mediana**. Estimación propia: un recién llegado cobra **30-50% de esos precios** los primeros 6 meses. Las tasas de respuesta de cold email salen de benchmarks de empresas que venden esas herramientas.

**Verificado por mí:** el repositorio `browser-use/video-use`, base de la herramienta propia, existe (licencia MIT, 27.856 estrellas, último cambio 2026-09-24).

---

## 1. La verdad incómoda primero (5 hallazgos que cambian el plan)

1. **"Editar videos" ya es commodity.** Vidchops cobra USD 495/mes por 4 videos largos. La mediana en Upwork es ~USD 35/h, y en el 2T-2026 las publicaciones de edición subieron 31% mientras la tarifa promedio bajó 8% (dato de un blog). Hay **editores argentinos cobrando USD 5,50-8,50/h**. Vender "edición" es competir contra tus compatriotas por precio.
2. **El video simple hecho con IA ya es gratis:**
   - Meta Advantage+ arma un video con hasta 20 fotos y dobla con sincronización de labios desde 2026-03.
   - Google Pomelli es gratis.
   - Un video inmobiliario con IA cuesta ~USD 10.
   - **Sora cerró:** la app el 2026-04-26 y la API el 2026-09-24. Es el ejemplo más claro del riesgo de plataforma.
   
   Hay que vender **método y resultado**, no "videos hechos con X".
3. **La plata está en el resultado, no en el corte.** Testimonial Hero cobra USD 3.750-6.200 por historia de cliente filmada a distancia; un podcast corporativo cuesta USD 3.000-15.000/mes; los abogados pagan retainers de video desde USD 4.500. Se paga por coordinar, guionar, conocer las reglas del rubro y entregar piezas que **venden**.
4. **La herramienta propia no te diferencia, te da margen.** Descript, Opus, Gling y Submagic hacen lo mismo por USD 15-200/mes. La tuya sirve para producir con 80-97% de margen bruto en formatos repetitivos y cobrar como agencia. **Lo que más se automatiza (90-95%) arranca de una planilla** (catálogo, lista de precios, cronograma de obra), **no de video crudo**.
5. **"Sin cara" sí, "anónimo" no del todo:**
   - **Legal:** cada mail tiene que identificar a la marca, con dirección postal y opción de baja (CAN-SPAM en EE.UU., Ley 25.326 en AR).
   - **Cobro:** la factura E y Payoneer muestran tu nombre legal.
   - **Ventas:** arriba de USD 1.500 los compradores B2B piden videollamada.
   
   El anonimato es **de marketing**: marca, sin cara en el contenido y firma con nombre de pila. Un pseudónimo total con LinkedIn falso destruye la confianza y viola las reglas de las plataformas.

---

## 2. Las 3 reglas del mercado de email frío

| País | ¿Email frío B2B? | Nota |
|---|---|---|
| **EE.UU.** | **Sí**, sin permiso previo (opt-out) | Es el mercado del email: ticket alto, y el **hispano de EE.UU.** tiene poca oferta en español |
| España / UE | **No** (LSSI art. 21 lo prohíbe sin consentimiento, también entre empresas) | La AEPD multa EUR 800-12.000 en casos chicos |
| Canadá | No (CASL exige consentimiento) | — |
| **Argentina / LATAM** | Legal con la leyenda de retiro de datos, pero **rinde poco** | Acá funcionan Instagram y WhatsApp, este último **solo con permiso del contacto** |

**Entregabilidad:**
- Nunca mandar desde tu Gmail ni desde el dominio principal. Usar 2 dominios secundarios con SPF, DKIM y DMARC, 2-3 semanas de warm-up y 25-50 mails por día por buzón.
- El primer mail va **sin links ni adjuntos**.
- Con 150 envíos, **1 sola queja de spam ya supera el umbral de 0,3% de Google**.
- **Respuesta realista:** 2-6%, o sea **0-3 clientes por cada 150 prospectos** en la primera tanda.

**La táctica que mejor funciona: "muestra con permiso".** El mail 1 dice "rehíce tu último reel, ¿te lo mando?" y la muestra va solo a quien dice que sí. Mejora la entrega y resuelve los derechos de usar su material. Nunca usar avatares IA como si fueran clientes reales ni reseñas sin permiso: la FTC multa hasta USD 51.744 por infracción.

**Costo del sistema:**
- **Austero: ~USD 40-55/mes.** Incluye Mailmeteor, 2 casillas de Google Workspace, buzón virtual en EE.UU. y dominios.
- Estándar con Instantly: USD 110-160/mes.
- Gasto inicial: ~USD 31 en dominios.

---

## 3. La herramienta: qué es, cómo se arma, cuánto cuesta

**Tu PC alcanza** (medido el 2026-10-02): Intel Core Ultra 7 258V, 32 GB de RAM y FFmpeg 9.0 con Quick Sync. Un minuto de 1080p se codifica en ~5 s. Un video de 10 min necesita **8-25 min de máquina**. No hace falta GPU ni nube.

**Arquitectura recomendada** (todo local, nada expuesto a internet):
```
Cliente sube material ─► Carpeta de Google Drive compartida (una por cliente)
                              │  (sincroniza a la PC)
                              ▼
                 Vigilante de carpeta ─► Cola de trabajos
                              │
   ┌──────────────────────────┼───────────────────────────────┐
   │ 1. Limpieza de audio (loudnorm, ruido)                   │
   │ 2. Transcripción por palabra (faster-whisper / Groq)     │
   │ 3. Corte de silencios y muletillas (auto-editor)         │
   │ 4. Claude lee la transcripción y decide: hook, cortes,   │
   │    títulos, qué clips sacar (estilo video-use)           │
   │ 5. Render: subtítulos animados (ASS), zooms, logo,       │
   │    intro/outro, música libre, 9:16 con seguimiento de     │
   │    cara (OpenShorts) — según la "receta" del cliente      │
   └──────────────────────────┼───────────────────────────────┘
                              ▼
            Panel local de revisión (aprobar / pedir ajuste)
                              ▼
            Carpeta de entrega en Drive + aviso por mail
```
- **"Receta" por cliente** en un archivo simple: colores, tipografía, logo, estilo de subtítulos y cuántos clips. Se escribe una vez.
- **Costo directo por video:** USD 0,05-0,60 con la herramienta propia, contra USD 0,4-3 por video + USD 30-100/mes con SaaS. El costo real es **tu tiempo de revisión**, con meta de ≤15 min por pieza.
- **Qué se auto-edita bien:** cámara a cara, podcasts, webinars, entrevistas, testimonios, clases, grabaciones de pantalla, y videos armados desde fotos o planillas (catálogos, propiedades, autos, avance de obra).
- **Qué no:** narrativos, cinemáticos, eventos complejos, bodas, y deportes, donde marcar al jugador sigue siendo manual (40-60% automatizable).
- **No usar CapCut con material de clientes:** sus términos le dan una licencia perpetua sobre lo subido y su música no es comercial. La música de YouTube Audio Library solo es segura dentro de YouTube.
- **Higgsfield:** Marketing Studio no está en el MCP (se usa desde la web), los créditos vencen cada mes y **sus términos prohíben automatizar**. Sirve para crear piezas a mano, no como pieza del pipeline.
- **No conviene venderla como SaaS:** competiría contra Captions/Mirage (USD 75 M levantados en 2026-03), Opus, Descript, Adobe y los open source gratis. Usala como **motor interno** de tu agencia. Así se resuelve tu miedo a vender software: **no vendés software, vendés el resultado**.
- **Plan:** en las semanas 0-2 vendés los pilotos con Submagic + Gling (~USD 50/mes) mientras Claude Code arma el MVP (cámara a cara → versión horizontal limpia + 3 reels + panel de aprobación). En la semana 3, comparación a ciegas SaaS vs. propio. **Gate en la semana 8:** ≥3 clientes, ≥USD 300/mes y ≤15 min humanos por pieza.
- **Reutiliza el proyecto `clipper-semiauto`:** la cola de aprobación, la etapa de corte, subtítulos, 9:16 y hook, y el registro por pieza.

---

## 4. Top 15 consolidado (de las 133)

| # | Idea | Códigos | Ticket | Saturación | Por qué |
|---|---|---|---|---|---|
| 1 | **Contenido a partir de una charla:** webinar, podcast o entrevista → 4 semanas de piezas (B2B) | M3, T5, O7, R16 | USD 300-450/mes de entrada → 1.200-4.000 | media | ~75-80% automatizable; la muestra se hace con su propio webinar público |
| 2 | **Historias de clientes / testimonios remotos** para software y servicios B2B (español → inglés) | M1, M2, T8 | USD 1.500-3.000/mes | **baja-media** | Testimonial Hero cobra 3.750-6.200 por historia y el rango medio está vacío. En inglés requiere conducir entrevistas en inglés |
| 3 | **Edición white-label para agencias de marketing** | O3, T2, M26 | USD 800-1.500/mes por agencia | alta, pero canal ideal | El cliente final nunca te ve: **el canal más compatible con el anonimato**; un cliente vale 5-10 locales |
| 4 | **"5 variantes de anuncio en 72 h"** para marcas que ya pautan en Meta (laboratorio de conceptos) | O2, N8 | USD 300 de entrada → 1.500-3.000/mes | alta (media con método) | Leads con señal de compra en la Biblioteca de anuncios de Meta; se vende variedad de conceptos, no cantidad |
| 5 | **Pack Black Friday / Navidad** (6 creativos) | O11 | USD 299 | media | **Ventana hasta ~2026-11-20**: caja y casos ya |
| 6 | **Videos de procedimientos y seguridad para operarios, con QR en la máquina** | R20, M14, N5, T3 | proyecto USD 1.500-6.000 + 200-500/mes | **baja** | **Tu ingeniería industrial diferencia**; se suma a la consultora Orden Operativo; casi sin competencia en español |
| 7 | **Avance de obra mensual** para desarrolladoras e inversores (+ video de preventa desde renders) | M13, R31, N1, N2, T12 | USD 300-600/mes por obra; preventa USD 900-2.500 | **baja** | Curva S + video = ingeniería pura; formato repetitivo |
| 8 | **Catálogo → un video por producto** (Clips de ML, catálogo de Meta) | R26, T15, N12 | USD 300-1.500/mes | baja (AR) | 90% automatizable desde la planilla. ⚠ Verificar si Clips de ML acepta carga masiva |
| 9 | **Catálogo PDF/WhatsApp y pantallas de precios que se regeneran desde la lista de precios** | R8, R28 | USD 80-250/mes + setup; cadenas USD 400-1.200 | **baja** | 90-95% automatizable; **la inflación es el motor del abono** |
| 10 | **Contenido mensual sin cara para profesionales hispanos de EE.UU.** (abogados de inmigración, contadores, realtors) | O13, M8 | USD 500-2.500/mes | baja-media | Poca oferta en español; ojo con las reglas de publicidad de abogados |
| 11 | **Explicativos de maquinaria industrial/agro + loops para ferias** | N3, N4, M15 | USD 500-3.000 por proyecto | **baja** | Fotos reales animadas; listas de expositores públicas = leads |
| 12 | **Instructivos post-compra** que bajan devoluciones y consultas | N9, M19, R21 | USD 600-1.500 + abono | baja | Vende ahorro medible |
| 13 | **Clips semanales de sermones para iglesias hispanas de EE.UU.** | M12, T14 | USD 400-900/mes | media-baja | 85-90% automatizable; formato idéntico cada semana |
| 14 | **Video-reporte mensual personalizado** (consorcios, rendiciones de alquiler, clientes de contadores) | R30 | USD 150-600/mes | **baja** | 95% automatizable desde los datos; novedoso |
| 15 | **Mascota de marca** con guía de personaje + serie mensual | N14 | USD 800-1.500 + 400-900/mes | baja-media | Esquiva el rechazo a las "personas IA" (62% en EE.UU. las rechaza) |

**Cerca del top:** inducción multilingüe para minería y petróleo (N5), fotos uniformes y video de cada auto para agencias de usados (R6+R27), manual de inducción → microvideos para plataforma de cursos (R19), reels mensuales para profesionales (T1), YouTube B2B para firmas de expertos (M7), "rehíce tu reel" para hispanos de EE.UU. (O1) y subtítulos/versión en español para marcas de EE.UU. (O9).

---

## 5. Los 3 negocios posibles (en vez de 133 ideas sueltas)

### Negocio 1 — "Productora B2B de contenido a partir de charlas" (EE.UU. hispano → inglés)
- **Qué vende:** webinars, podcasts, entrevistas y testimonios convertidos en contenido que vende (ideas 1, 2, 10 y 13).
- **Motor:** la herramienta propia, con una sola familia de formatos (charla grabada), que es la que mejor se auto-edita.
- **Captación:** email frío a EE.UU. con muestra con permiso, más white-label para agencias (idea 3).
- **Ticket:** de USD 300-450/mes de entrada a USD 1.500-3.000/mes con historias de clientes.
- **Condición:** **tu nivel de inglés** (para entrevistar). En español se arranca igual.
- **Sin cara:** sí (marca + videollamadas como productor).

### Negocio 2 — "Video operativo e industrial" (tu diferencial)
- **Qué vende:** videos de procedimientos y seguridad con QR, inducción multilingüe, explicativos de maquinaria, ferias y avance de obra (ideas 6, 7 y 11).
- **Ventaja:** **baja saturación + tu ingeniería**. Se vende junto con la consultora Orden Operativo. Ticket por proyecto de USD 1.500-6.000.
- **Contra:** la venta industrial **no** se hace bien con email frío anónimo; pide relación, visitas y LinkedIn con nombre.

### Negocio 3 — "Video y catálogos desde planillas" (AR, abono por inflación)
- **Qué vende:** catálogo → videos por producto, catálogo PDF/WhatsApp y pantallas de precios que se regeneran solas, video-reportes mensuales y videos del stock de autos (ideas 8, 9 y 14).
- **Ventaja:** **90-95% automatizable**, abono natural y cliente local.
- **Contra:** ticket en pesos y más bajo. Se vende por WhatsApp e Instagram, no por email. Sinergia total con Orden Operativo (maestro de SKUs).

---

## 6. Recomendación (para decidir)

**Empezar por el Negocio 1, con el motor propio, y dejar el 2 como línea de la consultora:**

1. **Semanas 1-2:** armar el sistema de email (dominios + warm-up, que lleva 2-3 semanas igual) **en paralelo** con el MVP de la herramienta. Mientras tanto, vender **white-label a agencias** (idea 3) y el **pack Black Friday / Navidad** (idea 5) con Submagic/Gling para tener caja y casos antes de ~2026-11-20.
2. **Semanas 3-8:** email frío a negocios **hispanos de EE.UU.** con la oferta "tu webinar/podcast → 10 clips" (idea 1) y "5 variantes de anuncio" (idea 4). Sumar a la cartera a quien pague.
3. **Gate en la semana 8** (~2026-11-27): ≥3 clientes, ≥USD 300/mes recurrentes, ≤15 min humanos por pieza. Si se cumple, subir a historias de clientes (idea 2, ticket alto). Si no, cambiar de oferta antes que de canal.
4. **En paralelo, sin email:** ofrecer la idea 6 (videos de procedimientos con QR) a los clientes de Orden Operativo. Es la que más vale por hora para vos.

**Expectativa honesta** (estimación propia): con 10-15 h/semana, llegar a **USD 1.000-2.000/mes en 4-6 meses** es posible **si** la oferta pega. Los primeros 2 meses es más probable estar en USD 0-500. El cuello de botella va a ser la **venta**, no la edición.

---

## 7. Catálogo completo (133)

### M — Mercado de video: nichos y ofertas (34)
| # | Idea | Ticket mensual (USD) | Saturación | Score |
|---|---|---|---|---|
| M1 | Testimonios remotos de clientes para SaaS B2B (inglés) | 1.500-2.500 por cliente | media-baja | 8,5 |
| M2 | Historias de clientes en español (fintech/SaaS LATAM, España, EE.UU. hispano) | 1.600-3.000 | baja | 8 |
| M3 | Webinar → 4 semanas de contenido (B2B) | 1.200-4.000 | media | 8 |
| M14 | Biblioteca de video-procedimientos en planta (+ procedimiento escrito + quiz) | 1.000-2.000 (proyecto 3-6k) | baja | 8 |
| M13 | Video mensual de avance de obra para desarrolladoras | 1.500-3.500 | baja | 7,5 |
| M8 | Videos FAQ en español para abogados hispanos de EE.UU. | 1.200-2.500 | baja-media | 7,5 |
| M4 | Podcast corporativo B2B llave en mano | 1.500-3.000 | media | 7,5 |
| M6 | Tutoriales y onboarding en video para SaaS (suscripción) | 1.000-2.500 | media | 7 |
| M7 | YouTube B2B con estrategia para firmas de expertos | 1.000-2.500 | media | 7 |
| M9 | "La cuadrilla filma, nosotros cortamos" para contratistas de EE.UU. | 1.200-2.500 | media | 7 |
| M12 | Clips de sermón + devocional para iglesias hispanas de EE.UU. | 400-900 | media-baja | 7 |
| M5 | Banco de cortes de llamadas de ventas para entrenar vendedores | 1.000-2.000 | baja | 6,5 |
| M15 | Videos de aplicación de producto para fabricantes exportadores | 600-1.200 | baja | 6,5 |
| M17 | Video de reclutamiento con kit remoto | 800-1.500 | baja-media | 6,5 |
| M20 | Reels de highlights para becas deportivas en EE.UU. (white-label) | 1.500-5.000 en temporada | media | 6,5 |
| M10 | Videos para asesores financieros listos para compliance | 1.500-3.000 | baja-media | 6 |
| M18 | Recap de eventos en 48 h + clip por orador | 800-2.500 por evento | media | 6 |
| M19 | Videos FAQ para bajar consultas de soporte | 400-800 + setup | baja | 6 |
| M21 | Postproducción de cursos Hotmart | 800-2.500 por curso | media | 6 |
| M11 | Med spas en EE.UU. | 800-2.000 | media-alta | 5,5 |
| M16 | Video de cierre de proyecto para estudios de arquitectura | 600-1.500 | baja-media | 5,5 |
| M22 | Clases → microlearning para institutos privados | 1.000-3.000 | baja | 5,5 |
| M29 | Video de cada auto + reel del stock para concesionarias | 500-1.500 | media | 5,5 |
| M24 | Edición white-label para videógrafos de casamientos | 1.500-5.000 en temporada | media-alta | 5 |
| M26 | Edición de fondo white-label para agencias de EE.UU. | 800-1.500 | alta | 5 |
| M27 | Versiones bilingües de videos inmobiliarios de lujo | 200-500 por propiedad | media | 5 |
| M28 | Videos para fichas de Amazon (marcas latinas en EE.UU.) | 400-1.000 por producto | media-alta | 5 |
| M30 | Hoteles boutique y bodegas que venden a extranjeros | 500-1.200 | media | 5 |
| M31 | Video de prospección personalizado para vendedores | 800-1.500 | media | 4,5 |
| M34 | Reels para clínicas dentales en España | — | alta | 4,5 |
| M23 | Highlights de torneos amateur (pádel, fútbol) | 200-600 por torneo | alta | 4 |
| M32 | Video para licitaciones y propuestas B2B | 500-1.500 por propuesta | ? | 4 |
| M25 | Edición white-label para fotógrafos inmobiliarios | 30-150 por video | alta | 3,5 |
| M33 | Tributos fúnebres para funerarias | — | alta | 3 |

### T — Productos y servicios que salen de la herramienta (20)
| # | Idea | % automatizable | Margen bruto* | Score |
|---|---|---|---|---|
| T1 | Reels mensuales para profesionales | 80% | ~97% | 8 |
| T2 | Edición white-label para agencias | 75% | ~95% | 7,5 |
| T3 | Instructivos desde grabaciones de pantalla (con la consultora) | 75% | ~98% | 7,5 |
| T4 | Videopodcast completo (episodio + 5 shorts) | 70% | ~98% | 7 |
| T5 | Webinar → paquete de contenido | 75% | ~98% | 7 |
| T6 | Limpieza de clases para cursos online | 85% | ~98% | 7 |
| T7 | Videos de propiedades desde fotos de la ficha | 90% | ~97% | 7 |
| T8 | Testimoniales editados | 80% | ~99% | 6,5 |
| T9 | Videos de inventario para concesionarias | 90% | ~99% | 6,5 |
| T10 | Pre-edición para editores freelance | 85% | ~95% | 6 |
| T11 | Recaps de eventos con clips subidos por invitados | 60% | ~97% | 6 |
| T12 | Avance de obra mensual para constructoras | 85% | ~99% | 6 |
| T13 | Reels gastronómicos | 80% | ~99% | 6 |
| T14 | Clips de prédicas o charlas (iglesias, ONGs) | 85% | ~99% | 6 |
| T15 | Catálogo de productos en video | 90% | ~97% | 6 |
| T16 | Subtitulado + doblaje ES↔EN/PT | 70% | 70-90% | 5,5 |
| T17 | Video-presentaciones de candidatos para RR. HH. | 80% | ~99% | 5 |
| T18 | Recetas de edición en español para Claude Code (producto) | 95% | ~90% | 5 |
| T19 | Plantillas Remotion vendibles | 95% | ~90% | 4,5 |
| T20 | Highlights de fútbol amateur | 40-50% | ~80% | 4,5 |

\*Sin contar el tiempo humano.

### O — Ofertas outbound con marca anónima (18)
| # | Oferta | Canal | Respuesta esperada | Score |
|---|---|---|---|---|
| O2 | "5 variantes de anuncio en 72 h" (a quienes pautan en Meta) | Email | 3-8% | 8 |
| O3 | White-label para agencias: "tu equipo de edición sin contratar" | Email | 2-6% (cliente = 5-10 locales) | 8 |
| O1 | "Rehíce tu último reel" (locales hispanos de EE.UU.) | Email | 4-10% | 7,5 |
| O9 | Subtítulos y versión en español para marcas de EE.UU. | Email | 3-8% | 7,5 |
| O11 | Pack Black Friday / Navidad (6 creativos, hasta ~2026-11-20) | Email | 4-8% | 7,5 |
| O5 | Fotos de producto con IA para Shopify/Etsy | Email | 4-8% | 7 |
| O7 | "De tu webinar/podcast a 10 clips" | Email | 3-7% | 7 |
| O13 | Motor mensual de contenido sin cara para profesionales hispanos | Email | 2-5% | 7 |
| O17 | Auditoría en video sin cara (pantalla + voz) | Email (2º mail) | 5-12% en los mejores leads | 7 |
| O8 | "YouTube resucitado" (shorts de videos viejos) | Email | 3-6% | 6,5 |
| O10 | Refresh de la ficha de Google (⚠ fotos IA prohibidas por Google) | Email / WA con opt-in | 3-6% | 6,5 |
| O12 | Reels de antes y después | Email + DM de IG | 3-6% | 6,5 |
| O6 | Video de la propiedad en 24 h | Email | 3-7% | 6 |
| O14 | Video explicativo para la home | Email | 1-4% | 6 |
| O4 | Tus mejores reseñas, en video | Email | 2-6% | 5,5 |
| O15 | Anuncios estilo UGC con avatar IA, declarados | Email | 3-6% | 5,5 |
| O16 | Tour de 30 s de salones y venues | Email | 2-5% | 5,5 |
| O18 | Reels para inmobiliarias de AR | IG + WA con opt-in | 5-15% por DM manual | 5,5 |

### N — Video y foto con IA generativa (28)
| # | Idea | Precio (USD) | Saturación | Score |
|---|---|---|---|---|
| N1 | Video de preventa para desarrolladoras (desde renders) | 900-2.500 | baja-media | 7,5 |
| N2 | Video mensual de avance de obra para inversores | 300-600/mes | baja | 7,5 |
| N3 | Explicativos de maquinaria industrial y agrícola | 1.000-3.000 | baja | 7,5 |
| N4 | Loops para pantallas de stands en ferias | 500-1.500 | baja | 7 |
| N5 | Inducción de seguridad multilingüe para minería y petróleo | 1.500-5.000 | baja-media | 7 |
| N8 | Laboratorio de conceptos de anuncios (marcas que pautan) | 1.500-3.000/mes | alta (media con método) | 7 |
| N9 | Instructivos post-compra que bajan devoluciones | 600-1.500 | baja | 7 |
| N14 | Mascota de marca + serie mensual | 800-1.500 + 400-900/mes | baja-media | 7 |
| N6 | Visualización de proyectos para licitaciones | 800-2.500 | baja | 6,5 |
| N10 | Video principal + cortes para bodegas y bebidas exportadoras | 1.000-2.500 | baja-media | 6,5 |
| N13 | Test de concepto antes de fabricar (anuncios para validar demanda) | 800-1.500 | baja | 6,5 |
| N15 | Adaptación cultural de anuncios extranjeros a LATAM y España | 150-400 por anuncio | media | 6,5 |
| N16 | Comercial versionado por sucursal para franquicias | 1.000-1.500 + 30-80 por versión | baja | 6,5 |
| N18 | Maquetas animadas (animatics) para productoras y agencias | 500-2.000 | baja-media | 6,5 |
| N19 | Videos de lanzamiento de funciones para empresas de software | 1.500-3.000/mes | media | 6,5 |
| N23 | Revisión de cumplimiento de anuncios IA antes de pautar | 300-1.500 | baja | 6,5 |
| N7 | Video institucional industrial | 400-3.000 | baja-media | 6 |
| N11 | Colección de moda por temporada | 400-3.000 | media | 6 |
| N17 | Doble digital para preguntas frecuentes (con consentimiento) | 400-3.000 | media | 6 |
| N21 | Video para eventos corporativos | 400-3.000 | media-alta | 6 |
| N12 | Video por producto para ML y catálogo de Meta | variable | media | 5,5 |
| N20 | Comercial para TV por internet de PyMEs de EE.UU. | variable | media | 5,5 |
| N22 | Video para crowdfunding | variable | media | 5,5 |
| N24 | Video para startups | variable | media-alta | 5,5 |
| N26 | Contenido educativo | variable | media-alta | 5,5 |
| N25 | Servicios del hogar en EE.UU. | variable | media-alta | 5 |
| N27 | Video de prospección personalizado | variable | media-alta | 5 |
| N28 | Tráilers de libros | variable | media-alta | 4 |

### R — Rubros parecidos automatizables (33)
| # | Idea | Ticket mensual (USD) | % automatizable | Saturación | Score |
|---|---|---|---|---|---|
| R20 | Videos de procedimientos y seguridad para operarios, con QR en la máquina | 200-500 + proyecto 1.500-6.000 | 60-70 | baja | 8 |
| R26 | Catálogo → un video por producto (Clips de ML, Meta) | 300-1.500 | 90 | baja | 8 |
| R8 | Catálogo PDF/WhatsApp que se regenera desde la lista de precios | 80-250 + setup | 90-95 | baja | 7,5 |
| R19 | Manual/PPT de inducción → microvideos + paquete para plataforma de cursos (SCORM) | 200-600 + proyecto 1.500-5.000 | 70 | media | 7,5 |
| R30 | Video-reporte mensual por cliente (consorcios, alquileres, contadores) | 150-600 | 95 | baja | 7,5 |
| R31 | Video de avance de obra para desarrolladoras e inversores de fideicomisos | 100-300 por obra | 80 | baja | 7,5 |
| R6 | Fotos con fondo uniforme para agencias de autos usados | 150-400 | 85-90 | media | 7 |
| R28 | Pantallas de precios del local que se actualizan desde la planilla | 400-1.200 por cadena | 90-95 | baja-media | 7 |
| R1 | Fotos de catálogo uniformes para distribuidoras (500-5.000 productos) | 100-300 + proyecto | 85-90 | media-baja AR | 6,5 |
| R2 | Ropa "puesta" en modelo IA para marcas de indumentaria | 300-1.200 | 70 | media | 6,5 |
| R10 | Edición de podcasts white-label para productoras | 800-4.000 | 70-80 | alta EN / media ES | 6,5 |
| R18 | Imágenes de listing y A+ para marcas en Amazon | 750-6.000 por proyecto | 60-70 | media-alta | 6,5 |
| R22 | Videos de scouting para academias y agencias de becas | 1.200-3.600 por temporada | 40-60 | media | 6,5 |
| R27 | Video de cada auto en stock (complemento de R6) | 250-600 combinado | 90 | baja-media | 6,5 |
| R4 | Paquete por propiedad para inmobiliarias AR (fotos + reel + aviso) | 150-600 | 85 | media | 6 |
| R12 | Limpieza de audio de bibliotecas de cursos | lotes 3.000-8.000 | 85-90 | baja-media | 6 |
| R21 | Videos de ayuda de software que se regeneran cuando cambia la app | 800-2.500 | 75 | baja-media | 6 |
| R5 | Retratos corporativos IA uniformes para equipos | una vez 300-3.000 | 85 | alta EE.UU. / media LATAM | 5,5 |
| R14 | Subtítulos de accesibilidad en español para universidades | 1,2-2,5 por minuto | 85-90 | media ES | 5,5 |
| R16 | 1 webinar B2B → 15-25 piezas | 400-1.500 | 75 | media-alta | 5,5 |
| R24 | Resumen del evento el mismo día, para productoras de eventos | 600-4.000 | 50-60 | media | 5,5 |
| R33 | Biblioteca de videos para pacientes, licenciada por consultorio | 20-50 por consultorio | 90 | baja | 5,5 |
| R9 | Fotos y video de menú para dark kitchens y cadenas | proyecto 300-1.000 | 75 | media | 5 |
| R11 | Audiolibros con voz IA para editoriales chicas (fuera de Audible) | 300-700 por libro | 80 | media | 5 |
| R15 | Subtítulos para tiendas que venden en la UE | 200-800 | 85 | media | 5 |
| R25 | Primer corte automático para videógrafos de bodas | 300-1.500 | 60 | media | 5 |
| R29 | Publicaciones semanales en Google por sucursal de una cadena | 20-50 por sucursal | 85 | media | 5 |
| R3 | Edición de fotos inmobiliarias para fotógrafos de EE.UU. | 300-1.500 | 75-85 | alta | 4,5 |
| R13 | Voz de marca IA con licencia de un locutor real | 100-400 | 90 | media-alta | 4,5 |
| R17 | Miniaturas de YouTube por suscripción | 300-1.000 | 50-60 | alta | 4,5 |
| R32 | Videos personalizados en masa para ventas | 500-1.500 | 90 | alta | 4 |
| R23 | Resúmenes automáticos para canchas de fútbol 5 | 150-500 | 70 | media (necesita cámaras) | 3,5 |
| R7 | Edición al por mayor para fotógrafos de eventos | 50-150 por evento | 80 | muy alta | 3 |

---

## 8. Trampas del rubro

1. **Vender "edición"** o "videos con IA" a secas: es commodity y las plataformas lo dan gratis.
2. **Personas sintéticas:**
   - Al 62% del público de EE.UU. le parecen inaceptables, aun con aviso (Bentley-Gallup, 2026-05).
   - La UE exige transparencia por el art. 50 del AI Act desde el 2026-08-02.
   - TikTok exige etiqueta desde el 2026-07-21 y puede banear la cuenta de forma permanente.
   - Nueva York exige aviso de "intérpretes sintéticos".
   - La FTC prohíbe testimonios de personas inexistentes.
3. **Google Business Profile** pide fotos "sin uso excesivo de IA" que "representen la realidad": no vender imágenes IA para la ficha de Maps.
4. **Música:** con CapCut y YouTube Audio Library, fuera de YouTube no hay derechos comerciales. Udio no sirve para entregar a clientes. Suno v6 tiene licencias parciales (UMG y Sony siguen en litigio).
5. **Personajes, celebridades y marcas ajenas:** nunca. Seedance recibió cartas documento de Disney y la MPA.
6. **Email:** mandar desde el Gmail personal, más de 3 mails por secuencia, links en el primer mail o comprar listas lleva a quemar el dominio y al riesgo de suspensión de Workspace. **No mandar email frío a España ni a Canadá.**
7. **Muestras sin permiso:** usar el material del cliente en tu portfolio sin autorización escrita.
8. **Dependencia de una plataforma de IA** (el caso Sora): mantener el pipeline intercambiable.
9. **Tomar los precios de agencias como mediana:** son el techo.
10. **Construir la herramienta antes de vender:** primero 2-3 pilotos con SaaS, después el motor propio.

---

## 9. Pendientes de verificar

- [ ] **Tu nivel de inglés** (define si el Negocio 1 llega al ticket alto).
- [ ] Si Clips de Mercado Libre acepta carga masiva de videos (crítico para R26).
- [ ] Si Higgsfield sigue ofreciendo Sora 2 y qué modelos tiene hoy; límites de uso comercial de tu plan.
- [ ] Precios de Premiere, Descript, Captions, TimeBolt, Recut y Selects.
- [ ] Tarifas de edición y animación de renders en Argentina.
- [ ] Qué artículos del Decreto 351/79 exigen capacitación con constancia (para R20).
- [ ] Política de PedidosYa y Rappi sobre fotos de platos hechas con IA.
- [ ] Estado de los proyectos de ley argentinos de etiquetado de IA.
