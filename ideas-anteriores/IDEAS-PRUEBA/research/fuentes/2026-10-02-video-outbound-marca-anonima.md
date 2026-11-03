# Sistema de prospección y venta outbound con marca anónima: servicios de video y fotos

- **Fecha:** 2026-10-02 (viernes).
- **Frente:** cómo conseguir clientes por **email frío** (y canales complementarios) para un servicio de creación/edición de video y fotos, operando con una **marca** y sin mostrar cara ni nombre completo. Tiene que ser legal, llegar a la bandeja de entrada y convertir.
- **Perfil asumido:** argentino, no programa (Claude Code le arma las herramientas), capital < USD 500. Tiene Gmail, Cloudflare, GitHub y Higgsfield conectados, y una cuenta Apify en evaluación. Nivel de inglés **sin confirmar** (pregunta abierta en `MEMORY.md` desde 2026-10-01).
- **Pedido original:** "buscar 100 negocios y mandarles un mail ofreciendo creación/edición de video".
- **Complementa a:** `research/2026-10-01-230-ideas-con-claude.md` (B23 "agencia de cold email" = 3,5; E7, E11, E21, E37) y `research/2026-10-01-200-ideas-rapidas-1-semana.md` (H14 "5 reels con Higgsfield", I20/I28). **Acá no se repiten esas fichas.** Se agrega lo que faltaba: el **sistema de venta** (legal, entregabilidad, leads, conversión) y **ofertas outbound** con gancho de muestra gratis.

---

## 0. Metodología y advertencias

- **Cómo se hizo:** ~45 consultas: ~40 WebSearch hasta agotar la cuota de la sesión (200/200, incluyendo otras sesiones) y WebFetch a páginas primarias. Primarias leídas: guía CAN-SPAM de la FTC, requisitos de remitentes de Google (support.google.com/a/answer/81126), precios de Instantly, Smartlead, Saleshandy, lemlist, Mailmeteor, Hunter, Google Workspace y Zoho, ficha del actor Apify Google Maps Scraper, Cold Email Benchmark Report 2026 de Instantly y una guía de cold email B2B en España (Overloop, 2026-05). Lo demás sale de fuentes secundarias fechadas.
- **[NO VERIFICADO]** = no lo pude confirmar en una fuente primaria en esta sesión.
- **Conflictos de interés:** **todos** los benchmarks de cold email vienen de empresas que venden herramientas de cold email (Instantly, lemlist, Belkins, Woodpecker, Snov, Sendspark, Loom/Vidyard). Tienden a mostrar el mejor caso y a medir solo a sus usuarios activos. Uso la **mediana**, no el "top 10%".
- **No es asesoramiento legal.** Es un mapa de riesgos para decidir. Antes de facturar fuerte en un país, conviene una consulta con un abogado de ese país (~USD 100-200).

---

## 1. Legalidad y anonimato

### 1.1 La conclusión en una línea

**"Marca sin cara" es legal en todos los mercados analizados. "Remitente oculto o engañoso" no lo es en ninguno.** Podés no mostrar tu cara ni tu apellido en el marketing. Lo que no podés hacer es esconder **quién manda el mail** (el negocio), mentir en el asunto o en los encabezados, ni omitir la baja y la identificación que pide cada ley.

### 1.2 Tabla por país (cold email B2B ofreciendo un servicio)

| Mercado | Régimen | ¿Se puede mandar el primer mail sin consentimiento? | Requisitos mínimos en cada mail | Sanción / riesgo real | Veredicto para este proyecto |
|---|---|---|---|---|---|
| **EE.UU.** (CAN-SPAM) | **Opt-out**: se puede mandar hasta que la persona pida la baja. **No hay excepción B2B**: la ley aplica igual a mails entre empresas (FTC) | **Sí** | (1) Encabezados From/Reply-To verdaderos que identifiquen **a la persona o negocio** que envía. (2) Asunto no engañoso. (3) Identificarlo como mensaje comercial. (4) **Dirección postal física válida**: domicilio, casilla registrada (PO Box) o **buzón privado registrado** (CMRA). (5) Mecanismo de baja que funcione al menos 30 días después del envío. (6) Cumplir la baja en ≤ 10 días hábiles, sin cobrar ni pedir más datos que el email. (7) El que contrata a otro para enviar sigue siendo responsable | Hasta **USD 53.088 por mail** en infracción (FTC). En la práctica la FTC persigue spam masivo y engaño, no a una persona que manda 150 mails personalizados bien hechos | **Mercado #1 por ley.** Es el régimen más permisivo. Incluye a los negocios **hispanos de EE.UU.** |
| **Canadá** (CASL) | **Opt-in**, con consentimiento implícito posible | Solo si hay **consentimiento implícito por "publicación conspicua"**: el negocio publicó su email (por ejemplo en su web), **no** puso un aviso tipo "no queremos mails comerciales" y el mensaje se relaciona con su rol de negocio. Un fallo de 2020 (Federal Court of Appeal) **no permite** sacar emails de directorios de terceros | Identificación del remitente, datos de contacto y baja en cada mensaje | Multas altas (hasta CAD 10 M por infracción para empresas [NO VERIFICADO el tope exacto]) | **Usable con cuidado**: solo emails publicados por el propio negocio en su web, nunca de directorios |
| **España / UE** (RGPD + **LSSI art. 21**) | **Opt-in** para comunicaciones comerciales electrónicas | **En principio no.** El art. 21.1 LSSI prohíbe el email publicitario "no solicitado o expresamente autorizado". La AEPD dice que la LSSI prevalece sobre el RGPD en esta materia y que el art. 19 LOPDGDD **no** habilita campañas B2B. Una guía de un vendedor (Overloop, 2026-05) sostiene que se puede escribir a direcciones genéricas (`info@`) o a cargos profesionales con interés legítimo documentado. **Eso es una lectura agresiva**: el interés legítimo resuelve el lado RGPD, no la prohibición de la LSSI | Si igual se hace: identificación del prestador, baja simple en cada mail, aviso del art. 14 RGPD (de dónde sacaste el dato) y análisis de interés legítimo (LIA) documentado | Multas de la AEPD por art. 21 LSSI en casos chicos: **EUR 800, 1.000** (a una agencia de marketing, Headblue), **2.700** (Douglas), **5.000** y **12.000** (genbeta, lawwwing, economistjurist, 2023-2024). Una baja rota (link 404) costó EUR 2.000 (2024, vía Overloop) | **No arrancar por España con email frío.** Si se quiere España: formularios de contacto, LinkedIn de marca, Upwork o partners. Reevaluar con un abogado |
| **Reino Unido** (PECR + UK GDPR) | Opt-out para "corporate subscribers" (sociedades); **opt-in** para autónomos (sole traders) y algunas sociedades de personas | Sí a sociedades; no a autónomos [NO VERIFICADO en esta sesión, conocimiento previo] | Identidad del remitente y dirección de contacto válida + baja | ICO multa sobre todo campañas masivas | Secundario. Muchos negocios chicos del Reino Unido son autónomos, así que hay riesgo |
| **Argentina** (Ley 25.326 + Decreto 1558/2001) | **No hay ley anti-spam específica** (diariojudicial; hubo varios proyectos que no se sancionaron, por ejemplo 5051-D-2022). Rige el **art. 27** de la ley de datos personales, que permite tratar datos para publicidad si son de fuentes accesibles al público o se obtuvieron con consentimiento | Sí, con datos de negocio que el propio negocio publicó | **Leyenda obligatoria en cada comunicación publicitaria**, "en forma expresa y destacada": la posibilidad de pedir el **retiro o bloqueo** de los datos de la base, junto con el mecanismo para hacerlo (art. 27 inc. 3 Ley 25.326 + art. 27 Decreto 1558/01). Además hay que respetar el registro **"No Llame"** (Ley 26.951), que cubre teléfono; el proyecto para extenderlo a email no figura como sancionado [NO VERIFICADO] | Órgano de control: **AAIP**. Riesgo bajo con volumen chico y bien hecho | Legal. Pero **el email frío rinde poco** con las PyMEs argentinas (ver §6) |
| **México** (LFPDPPP **nueva**, DOF 2025-03-20, vigente desde 2025-03-21) | El consentimiento **tácito** es válido como regla general (EY, Hogan Lovells). La autoridad pasó del INAI a la Secretaría Anticorrupción y Buen Gobierno | Sí para datos de negocio, con aviso de privacidad y derecho de oposición | Aviso de privacidad (puede ser un link), baja / derecho de oposición. Hay que respetar el **REPEP de Profeco** (registro para no recibir publicidad) [NO VERIFICADO si cubre email] | Bajo para B2B chico | Legal y secundario. Mismo problema que AR: en México manda WhatsApp |

### 1.3 Cómo operar "con marca" sin romper nada

| Pieza | Cómo hacerlo | Riesgo / nota |
|---|---|---|
| **Nombre comercial** | Una marca corta y pronunciable en ES y EN (ej.: estilo "ReelForge Studio"). Antes de usarla, chequear USPTO/INPI y que el `.com` esté libre | Registrar la marca en INPI cuesta plata; no hace falta al principio |
| **Dominio** | Uno principal (`marca.com`) para la web y la facturación, y **2 secundarios** (`getmarca.com`, `marcastudio.com`) solo para mandar mails fríos. Cloudflare Registrar: **USD 10,46/año** por `.com`, mismo precio al renovar (domainoffer.net, 2026). WHOIS con privacidad | Nunca mandar cold email desde el dominio principal |
| **Firma: ¿nombre real, nombre de pila o pseudónimo?** | **Recomendado: nombre de pila real + marca** ("Facu · ReelForge Studio"). Un nombre de pila no es "mostrar la cara" y cumple CAN-SPAM, porque identifica al negocio. **Alias de rol aceptable**: "Equipo de Edición – ReelForge", si la empresa está bien identificada | **Pseudónimo completo** ("Jessica Martínez", con foto IA y LinkedIn falso): CAN-SPAM prohíbe encabezados engañosos, y cuando el prospecto busca a la persona y no existe, **se rompe la confianza** y la venta se cae (fullenrich, mailtrap). Además las **cuentas falsas** violan los términos de LinkedIn e Instagram. **Desaconsejado** |
| **Dirección postal (CAN-SPAM)** | Buzón virtual de EE.UU.: **Anytime Mailbox desde USD 4,99/mes** (muchas sedes a ~USD 9,99) o **iPostal1 desde USD 9,99/mes (USD 99/año)** (quicksprout, G2 2026). Otra opción es una casilla de correo en Argentina [NO VERIFICADO costo] | La FTC acepta "registered private mailbox". El buzón virtual también protege tu domicilio real |
| **Cobro a nombre de la marca** | Monotributo con **nombre de fantasía** + **Factura E** para clientes del exterior (IVA 0%), cobrando por **Payoneer**, Wise o Deel. Lo facturado afuera suma al tope de la categoría (iprofesional 2026-06, yo-facturo) | **Límite del anonimato:** la Factura E muestra **tu nombre legal y tu CUIT** (ARCA lo exige para personas humanas). Payoneer tiene KYC a tu nombre. **El anonimato es de marketing, no legal.** Para anonimato legal hace falta una sociedad (SAS en AR, o LLC en EE.UU., con costos de USD 300+ al año [NO VERIFICADO]). Con < USD 500 de capital: **aceptarlo** |
| **Web de la marca** | Landing en Cloudflare Pages (gratis), con portfolio, precios "desde", política de privacidad, link de baja y la dirección postal | Ver §8: el portfolio solo con material propio o con permiso |
| **Voz en videos de venta** | Voz propia (no identifica mucho) o voz IA de catálogo | **No clonar la voz de otra persona sin permiso.** Tavus clona tu cara y tu voz, y eso contradice el anonimato |

### 1.4 Lo que este informe **desaconseja explícitamente** (y por qué)

1. **Spam masivo sin baja**: es ilegal en todos los países de la tabla y además quema el dominio en días.
2. **Comprar listas**: datos viejos (rebotes > 5%), sin base legal en la UE y Canadá, y trampas de spam (spam traps) que te ponen en listas negras.
3. **Scrapear datos personales sensibles** o datos de reseñadores (el actor de Apify los trae **apagados por defecto**: hay que activar `scrapeReviewsPersonalData`; **no activarlo**).
4. **Suplantación** (hacerse pasar por otra empresa, falsear el From).
5. **Cuentas falsas** en LinkedIn o Instagram para mandar DMs.
6. **Remitentes engañosos**: asuntos tipo "Re: tu pedido" o "Factura pendiente" cuando no hubo contacto previo. CAN-SPAM lo prohíbe.

---

## 2. Entregabilidad 2026 (que el mail llegue a la bandeja y no a spam)

### 2.1 Reglas de los proveedores

| Proveedor | Para **todos** los remitentes | Para remitentes masivos | Fuente |
|---|---|---|---|
| **Gmail** (desde 2024-02-01) | SPF **o** DKIM; DNS directo e inverso (PTR) válidos; TLS; **tasa de spam < 0,3%** (Postmaster Tools); formato RFC 5322; no imitar encabezados de Gmail | ≥ 5.000 mails/día: SPF **y** DKIM, **DMARC**, alineación del From con SPF o DKIM, **baja en un clic** visible en mails de marketing | support.google.com/a/answer/81126 (leída 2026-10-02) |
| **Gmail, endurecimiento** | Desde **noviembre de 2025** el tráfico que no cumple puede recibir rechazos temporales o permanentes | Con tasa de spam ≥ 0,3% sostenida, Google no da soporte de mitigación | Zoho Community, suped.com [secundario] |
| **Yahoo** | Mismas reglas que Google desde 2024-02 | Igual | Conocimiento previo [NO VERIFICADO en esta sesión] |
| **Microsoft** (Outlook.com, Hotmail, Live) | — | ≥ 5.000/día: desde **2025-05-05** pide SPF + DKIM + DMARC (p=none como mínimo) y alineación; si no cumple, **rechaza** con el error `550 5.7.15` (no lo manda a la carpeta de no deseados) | dmarcian, Resend, InboxAlly (2025) |

**Traducción para 100-200 prospectos:** no sos "remitente masivo". Igual configurá **todo** (SPF + DKIM + DMARC + baja), porque cuesta cero y los filtros te juzgan con esos criterios. Lo que de verdad te puede hundir es la **tasa de quejas**: con 150 mails, **un** "marcar como spam" ya equivale al 0,67%. Por eso la segmentación y la personalización no son lujo: son entregabilidad.

### 2.2 Arquitectura recomendada (chica y prolija)

- **2 dominios secundarios × 1-2 buzones cada uno** = 2-4 buzones. Para mandar 1.000 mails se usan ~7 dominios (Smartlead), pero para 200 alcanzan 2.
- **Warm-up (calentamiento) de 2-3 semanas:** primera semana solo warm-up, sin campaña. Segunda semana, 5-15 mails de campaña por día a los mejores leads. Recién después, 20-40 por día por buzón (leadhaste, Unify, Smartlead 2026). **Techo prudente por buzón ya calentado: 25-50 mails fríos por día.**
- **SPF + DKIM + DMARC** (arrancar con `p=none` y monitorear) en Cloudflare DNS. Claude Code lo puede configurar por MCP de Cloudflare.
- **Dominio de seguimiento personalizado** (custom tracking domain) o, mejor, **desactivar el seguimiento de aperturas**: el píxel de apertura empeora la entrega y la "apertura" como métrica ya no es confiable (práctica de la industria [NO VERIFICADO con estudio]).
- **Primer mail sin links ni adjuntos.** El link o el video van en el segundo mail, cuando la persona responde "sí, mandalo" (ver §4.3). Mejora la entrega y además resuelve el tema de derechos de la muestra.
- **Rebotes < 2%:** verificar todos los emails antes de mandar.

### 2.3 Por qué NO mandar desde el Gmail personal

1. Si quemás la reputación, perdés **tu** cuenta personal (tus cosas, tu login de todo).
2. Rompe el anonimato: el From muestra tu nombre y tu foto.
3. Tope de ~500 mails/día en Gmail de consumo, sin SPF/DKIM de tu dominio, y luce poco profesional.
4. **Ojo: Google Workspace tampoco es "zona libre".** Su política de uso aceptable prohíbe el "unsolicited bulk commercial email", y hay suspensiones documentadas de cuentas usadas con herramientas de prospección (suped, Amplemarket). Se mitiga con volumen bajo, alta relevancia, baja en cada mail y dominios separados del principal. **El riesgo no es cero.**

### 2.4 Herramientas y precios (leídos el 2026-10-02 salvo aclaración)

| Herramienta | Plan de entrada | Precio | Límites | Warm-up | Para quién |
|---|---|---|---|---|---|
| **Mailmeteor** (sobre Gmail/Workspace) | Free / Starter / **Premium** | Gratis (50/día) / USD 5,99 / **USD 17,99 por mes** | Premium: 1.000/día, 30.000/mes, **seguimientos**, warm-up, dominio de seguimiento propio | Sí (Premium) | **Opción más barata** para 100-200 prospectos con 1-2 buzones |
| **Instantly** | **Growth** | **USD 47/mes** (USD 37,60 con pago anual) | 5.000 mails/mes, 1.000 contactos cargados, **buzones ilimitados** | Ilimitado | **Recomendado** si se quieren 3-4 buzones con rotación y un panel simple. Base de leads aparte: USD 47/mes por 1.500 créditos |
| **Smartlead** | Base | USD 39/mes (USD 32,50 anual) | 2.000 contactos, 6.000 envíos, buzones ilimitados | Incluido | Alternativa a Instantly, algo más técnica |
| **Saleshandy** | Starter | USD 34/mes con pago anual (USD 408/año) | 2.000 prospectos activos, 6.000 mails/mes, 1.500 créditos de leads | Ilimitado | Buena relación precio/calidad |
| **lemlist** | Email | USD 55/mes anual | Base de 650 M de leads, buscador de emails, warm-up | Sí | Caro para este tamaño. Su fuerte es la personalización de imágenes y video |
| **Apollo** | Free / Basic | Gratis / USD 49 por usuario por mes (anual) | Free: créditos limitados y tope de ~250 envíos/día (las fuentes no coinciden en los números [NO VERIFICADO]) | No nativo | Útil como **base de leads** en EE.UU. (contactos B2B), no para negocios locales |
| **Woodpecker / YAMM** | — | [NO VERIFICADO] (no leídos esta sesión) | — | — | Alternativas; YAMM es como Mailmeteor (mail merge sobre Sheets) |

**Casillas:** Google Workspace Business Starter: **USD 7 por usuario por mes** con plan flexible; plan anual con promo a USD 4,90 los primeros 12 meses, válida para los primeros 20 usuarios (workspace.google.com, leído 2026-10-02). Zoho Mail Lite: plan anual, ~USD 1 por usuario por mes [NO VERIFICADO el precio exacto: la página no lo mostró]. Zoho Forever Free no tiene IMAP, así que **no sirve** para conectar herramientas. **Recomendación:** Workspace, porque la mayoría de las PyMEs de EE.UU. usan Gmail/Workspace o Microsoft y la entrega entre Google y Google es la más predecible [inferencia].

---

## 3. Fuentes de leads (cómo armar los 100-200 negocios)

### 3.1 Dónde sacar la lista

| Fuente | Qué da | Costo (2026) | Legal / ToS |
|---|---|---|---|
| **Apify – Google Maps Scraper** (`compass/crawler-google-places`) | Nombre, rubro, web, teléfono, reseñas, puntaje, redes. Con add-on: **emails de contacto sacados de la web del negocio** | Desde **USD 1,50 cada 1.000 lugares**. Add-on de contactos: la página dice "USD 0,20-0,15 por lugar" ([NO VERIFICADO] si es por lugar o por cada 1.000; probar con 50 lugares y mirar el costo). El plan gratis de Apify trae crédito mensual [NO VERIFICADO el monto 2026] | Apify: "el scraping es legal si extraés datos públicos"; los **datos personales** solo con motivo legítimo; los datos de reseñadores vienen apagados por defecto. Los **términos de Google** prohíben el scraping: el riesgo contractual lo corre sobre todo el operador de la herramienta. El fallo **Meta v. Bright Data (2024-01-23)** sostiene que scrapear datos públicos sin loguearse no viola los términos (fbm.com). Datos de **negocios**, no de personas: riesgo bajo |
| **Outscraper** | Lo mismo que Apify, más un "Emails & Contacts Scraper" por dominio | **Gratis: 500 negocios por mes**; después USD 3 cada 1.000. Emails/contactos: según la fuente, gratis hasta 25 o 500, después USD 3 cada 1.000 dominios. Un lead completo cuesta ~USD 14 cada 1.000 (syncgtm, fitgap 2026) | Igual que Apify |
| **Meta Ad Library** | Quién **está pautando ahora** en Facebook/Instagram, con cuántos anuncios y qué creativos | Gratis, pública, sin login. Hay actores Apify que la cruzan con listas (por ejemplo "Lead Radar") [precio NO VERIFICADO] | Datos públicos de transparencia. Es la **señal de compra más fuerte** para vender creativos (§3.3) |
| **Instagram de negocios** | Frecuencia y calidad de reels, último posteo, email en la bio | Manual o con actor Apify | Scrapear perfiles **públicos de negocios** es defendible; no automatizar acciones desde tu cuenta |
| **Apollo / bases B2B** | Decisores con nombre y cargo (para agencias y e-commerce medianos) | Free o USD 49 | Datos personales de profesionales: en la UE aplica el art. 14 RGPD |
| **Directorios** (Yelp, Páginas Amarillas, cámaras) | Listas por rubro | Variable | **CASL: no sacar emails de directorios.** En la UE, base legal dudosa |

### 3.2 Encontrar y verificar emails

- **Orden de preferencia:** (1) el email publicado en la **web del propio negocio** (el mejor legalmente, sobre todo para CASL); (2) Hunter "Domain Search" (**gratis: 50 créditos por mes**; Starter USD 34-49 por 2.000); (3) Snov o Findymail [precios NO VERIFICADOS esta sesión].
- **Verificación obligatoria:** NeverBounce USD 8 cada 1.000, con **1.000 verificaciones gratis** para probar. ZeroBounce USD 19,50 cada 1.000, con 100 gratis por mes (bouncezero, leadmagic 2026). Para 200 leads: **USD 0-2**.
- Descartar los emails "catch-all" o "desconocidos" en el primer envío, o mandarles solo a los de mayor puntaje.
- `info@` o `contacto@` funcionan en negocios chicos (los lee el dueño). En negocios medianos conviene buscar al decisor (marketing o dueño).

### 3.3 Señales de compra para priorizar (score de lead 0-10)

| Señal | Cómo se detecta | Peso | Por qué |
|---|---|---|---|
| **Pauta activa en Meta con ≥ 3 creativos** | Meta Ad Library | +3 | Tiene presupuesto y quema creativos todas las semanas. Es quien más compra video (omnionlinestrategies 2026) |
| **Buenas reseñas (≥ 4,5, ≥ 50) pero redes flojas** | Google Maps + Instagram | +2 | Producto validado, marketing atrasado: el "gap" es obvio y fácil de mostrar |
| **Último reel hace > 45-60 días, o reels sin edición** (planos fijos, sin subtítulos, audio malo) | Instagram (revisión manual o con IA sobre capturas) | +2 | Dolor visible: "sé que tengo que hacer video y no lo hago" |
| **YouTube abandonado** (videos largos, último upload > 6 meses) | YouTube | +1 | Material crudo para reciclar en clips |
| **Web sin video / fichas de producto con fotos pobres** | Revisión de la web | +1 | Oferta de foto y video de producto |
| **Negocio nuevo** (ficha de Google reciente, "grand opening") | Fecha de las primeras reseñas | +1 | Está armando su marketing desde cero |
| **Ya tiene agencia o un editor visible** (créditos, reels muy pulidos) | Instagram | −2 | Difícil de desplazar |
| **Cadena o franquicia** | Nombre y cantidad de sedes | −2 | El marketing se decide en otro lado |

Claude Code puede armar el pipeline: Apify/Outscraper → planilla → puntaje automático (rating, reseñas, web, Ad Library) → revisión humana de los 50 mejores (5-10 min cada uno, mirando su Instagram) → muestra para los 20-30 mejores.

---

## 4. Qué convierte en 2026

### 4.1 Benchmarks (todos de vendedores: mirarlos con desconfianza)

| Fuente (conflicto de interés) | Dato | Período |
|---|---|---|
| **Instantly**, Cold Email Benchmark Report 2026 (vende la herramienta) | Respuesta promedio **3,43%**; cuartil superior **≥ 5,5%**; top 10% **≥ 10,7%**. **58% de las respuestas llegan con el primer mail**. Secuencias de 4-7 pasos; primer mail **< 80 palabras**; el miércoles tiene la mayor respuesta | 2025-01-01 a 2025-12-18 |
| **Belkins** (agencia de lead gen), 16,5 M de mails, 93 dominios | Respuesta promedio **5,8%** (6,8% en 2023, o sea −15% en un año); **8,4% en campañas de un solo mail**. Mandar **4 mails o más triplica las bajas y las quejas de spam**. Las PyMEs toleran más seguimientos que las grandes empresas | 2024 |
| Agregadores 2026 (getboomerang, mailshake, bouncezero) | Campañas de **< 50 destinatarios: 5,8%**, contra **2,1% en las de 500+**. Otra lectura: el promedio B2B "real" cayó a **~1,4%** (contra 3,5% en 2018) | 2026 [secundario] |
| **Snov.io** (vendedor) en Brasil | El multicanal (email + LinkedIn/WhatsApp/teléfono) da **+85% de respuestas** que solo email. En LATAM, la personalización IA + manual llevaría la respuesta del 2-3% al 8-12% | 2025-2026 |
| **Video personalizado** (Loom, Vidyard, Sendspark: todos venden video) | +2-4x de respuesta frente a solo texto; 10-16% contra 4,1% de base; la miniatura con el nombre o la web del prospecto genera la mayor parte de la mejora | 2025 |

**Mediana honesta para este usuario (estimación propia):** con una lista **chica, bien elegida por señales** y un primer mail con observación concreta: **2-6% de respuestas totales** y **1-3% de respuestas positivas**. Con muestra gratis personalizada para los mejores leads: **5-12% de respuesta** en ese segmento [inferencia, sin estudio independiente]. **Para 150 prospectos, eso son ~2-8 conversaciones y 0-3 clientes pagos en la primera tanda.** El primer envío sirve para **aprender qué oferta pega**, no para vivir de él.

### 4.2 Personalización con IA a escala (lo que funciona y lo que no)

- **Funciona:** 1-2 líneas **verificables y específicas** ("tu reel del 2026-09-12 sobre el brunch tiene 3 s muertos al principio y no tiene subtítulos; el 85% lo ve sin audio" [el dato del 85% es NO VERIFICADO, no usarlo sin fuente]). Claude puede redactarlas a partir de capturas y datos, **pero un humano revisa cada una**.
- **No funciona:** el "Vi que tu empresa es líder en..." genérico generado por IA. Hoy se detecta y baja la respuesta. El factor que más pesa en la respuesta es la **segmentación** (lista + señal), no la prosa.
- **Variables útiles para que Claude complete:** `{{observacion_reel}}`, `{{dato_resenas}}` ("4,8 con 212 reseñas"), `{{anuncio_activo}}` ("tenés 6 anuncios activos en Meta, todos estáticos"), `{{muestra_link}}`.

### 4.3 La táctica de "muestra gratis personalizada": cómo hacerla legal y efectiva

**Opciones de muestra, de menor a mayor riesgo legal:**

1. **Muestra hecha con material propio o de stock**, con la marca y el producto del prospecto **solo como mockup** (por ejemplo, un video IA con Higgsfield donde aparece su logo en un vaso o en una vidriera). Mostrar una marca ajena en un pitch privado es de muy bajo riesgo (uso referencial, no comercial). **No publicarlo.**
2. **Reedición de un video público del prospecto** (su reel). Técnicamente es una **obra derivada** de material con derechos de autor (en EE.UU. el "fair use" se analiza caso por caso; en Argentina, la Ley 11.723 no tiene un fair use amplio). **El riesgo práctico es mínimo** si (a) se manda **solo al titular** (el propio negocio), (b) es privado, (c) tiene marca de agua "MUESTRA – no publicar" y (d) **no se usa en el portfolio sin permiso escrito**. **Cuidado con la música:** el audio de su reel lo licenció Instagram para su uso en la plataforma, no para vos. Reemplazarla por música libre o de stock.
3. **Flujo con permiso (recomendado):** primer mail **sin link**: "Rehíce tu reel del 12/09 en 3 versiones, ¿te las mando?". Si responde "sí", hay consentimiento implícito para mandar el material. Se gana entregabilidad (no hay link en el primer mail) y se resuelven los derechos (te lo pidió). Además, la respuesta "sí" es una señal positiva para los filtros de spam.
4. **Prohibido en la muestra:** clonar la voz o la cara del dueño o de sus clientes; inventar testimonios; usar reseñas de Google en video sin permiso del autor (ver idea #4).

**Formato de entrega:** página privada en Cloudflare Pages (`marca.com/m/nombre-negocio`) con el video de 10-20 s, el antes y después, un botón "lo quiero" y un link de baja. En el mail va **una miniatura estática** con el nombre del negocio (tipo Sendspark), no un video adjunto.

**Videos de prospección "sin cara":**
- **Loom/grabación de pantalla con tu voz** sobre el Instagram del prospecto: "mirá estos 3 puntos" (gratis con Loom free [NO VERIFICADO límites 2026] u OBS).
- **Sendspark Solo: USD 49/mes** (100 minutos de video dinámico; prueba de 14 días desde 2026-06-30). Personaliza el fondo con la web del prospecto y el nombre con voz clonada (**la tuya**).
- **Tavus: USD 97-150/mes.** Clona cara y voz: **contradice el anonimato** y no se justifica para 150 prospectos.
- **Con avatar IA de catálogo** (HeyGen, etc.): se puede, pero en un pitch frío baja la confianza ("ni siquiera hay una persona"). Si se usa, **decir que es un avatar**.

### 4.4 Secuencia, asuntos, llamado a la acción y oferta de entrada

- **Secuencia:** **3 mails** (a lo sumo 4) en 8-10 días: día 0, día 3 y día 8. Instantly recomienda 4-7, pero Belkins muestra que **4 o más triplican quejas y bajas**, y con 2 dominios nuevos una queja pesa mucho. **3 es el punto óptimo para este caso.**
- **Asuntos:** 2-5 palabras, en minúscula, sin clickbait. Ejemplos: "tu reel del brunch", "idea para {{negocio}}", "3 versiones de tu anuncio". Prohibido "Re:" o "Fwd:" falsos.
- **CTA:** una sola pregunta de baja fricción. "¿Te mando la muestra?" > "¿Agendamos 30 min?". **No pedir llamada en el primer mail** (además, para alguien "sin cara", vender por mensajes asíncronos es la ventaja).
- **Oferta de entrada:** algo **chico, concreto y con plazo**: "4 reels en 7 días por USD 149", con garantía "si no te sirven, no pagás el segundo pack". El upsell es mensual (USD 400-900 por mes). Los paquetes son mejores que la tarifa por hora (vidico, videotto 2026).

---

## 5. Canales complementarios sin cara

| Canal | Límites y políticas | Riesgo | Uso recomendado |
|---|---|---|---|
| **DMs de Instagram con cuenta de marca** | Instagram no publica sus límites. Fuentes de 2026: cuentas nuevas (0-3 meses) **10-20 DMs fríos por día a no-seguidores**, 5-15 por hora; pasarse da un **bloqueo de 24-48 h**. El mismo texto repetido y los links a desconocidos disparan bloqueos (inro, metricool, instantdm 2026) | Medio | **Seguimiento** del email ("te escribí por mail, te dejo la muestra acá") o **primer contacto manual** con 10-15 por día. Ningún bot de DMs |
| **LinkedIn** | Una página de empresa **no puede mandar DMs**: hace falta un perfil personal | Alto para el anonimato (un perfil falso viola sus términos) | Solo con perfil real. Si no, usarlo nada más como página de marca para dar credibilidad |
| **WhatsApp** | Política de Meta: hace falta **opt-in** antes de mensajear (actualización 2024-11, exigible desde 2025-11). Mandar mensajes no solicitados en volumen termina en **número restringido o baneado** (respond.io, chakrahq 2026) | Alto | **Nunca masivo en frío.** Pasar a WhatsApp **solo cuando el prospecto responde** el mail o el DM y acepta ("¿te paso la muestra por WhatsApp?"). En AR es el canal de cierre |
| **Upwork / Contra con perfil de agencia** | La agencia se muestra con su marca; el dueño pasa por KYC (verificación de identidad) con su nombre real [NO VERIFICADO el detalle 2026]. Ya evaluado en el estudio del 2026-10-01 (B35, freelance USD) | Bajo | Canal **inbound paralelo**. Primer cobro en ≥ 7-14 días |
| **White-label para agencias de marketing** | La agencia ya tiene los clientes y revende tu trabajo con su marca. Los retainers de creativos de las agencias van de **USD 5.000 a 15.000 por mes** e incluyen 3-5 ediciones de video en los niveles de entrada (vidpros, enrichlabs 2026) | Bajo | **El canal más compatible con el anonimato**: el cliente final nunca te ve. Un cliente-agencia = volumen recurrente. Prospectarlas también por email frío, mostrando una edición de prueba **con material que manda la agencia** (cero tema de derechos) |

---

## 6. Mercado objetivo: ¿dónde funciona el email frío?

| Mercado | Email frío B2B | Ticket de video | Ley | Idioma | Veredicto |
|---|---|---|---|---|---|
| **Negocios hispanos en EE.UU.** (restaurantes, inmobiliarias, abogados de inmigración, contadores, estéticas en TX, FL, CA y NY) | Canal normal en EE.UU. | USD; reel freelance de USD 25-75 (principiante) a USD 75-200 (intermedio) (vidico, videotto 2026) | CAN-SPAM (opt-out) | **Español nativo = ventaja**; menos competencia que en el mercado en inglés [inferencia] | **#1 recomendado** |
| **EE.UU. en inglés** (e-commerce DTC, agentes inmobiliarios, agencias) | Canal estándar, muy saturado | El más alto | CAN-SPAM | Necesita inglés escrito sólido | **#2**, si el inglés da |
| **Canadá** | Funciona | Alto | CASL (solo emails publicados por el negocio) | EN/FR | Secundario |
| **España** | Funciona culturalmente, pero **está prohibido por la LSSI** sin consentimiento | EUR | Riesgo de multa AEPD (EUR 800-12.000 en casos chicos) | Español | **No con email frío.** Upwork, partners o formularios |
| **Argentina / LATAM** | Rinde menos: en LATAM manda el multicanal (Snov, Brasil). Las PyMEs argentinas viven en WhatsApp e Instagram | Bajo, en pesos | Ley 25.326 (leyenda de baja) | Español | **El email frío no es el canal.** Para AR: Instagram + WhatsApp con opt-in, grupos, presencial (ver el estudio del 2026-10-01) |

**Conclusión:** el pedido "100 negocios por mail" tiene sentido **apuntando a EE.UU. (hispanos primero)**, no a Argentina. Si el inglés del usuario es básico, igual se puede: el mercado hispano de EE.UU. se trabaja en español y Claude puede ayudar a redactar en inglés, pero las respuestas y las negociaciones en vivo necesitan fluidez.

---

## 7. Ofertas outbound concretas (18)

Escala de score 1-10 para **este usuario**: rentabilidad realista × respuesta esperada × fit (sin cara, no programa, Higgsfield/Claude) × riesgo legal o de commodity. Las tasas de respuesta son **estimaciones propias** apoyadas en los benchmarks de §4 (mediana 3-6%), ajustadas por la fuerza de la señal y de la muestra.

| # | Oferta | Público | Gancho / muestra gratis | Entrada → upsell | Canal | Respuesta esperada | Score |
|---|---|---|---|---|---|---|---|
| 1 | **"Rehíce tu último reel"** (auditoría de 3 puntos + 1 reel rehecho) | Locales hispanos de EE.UU. con Instagram activo y reels flojos (restaurantes, estéticas, gimnasios) | Su reel reeditado en 15 s (subtítulos, gancho, ritmo, música libre), con marca de agua; flujo con permiso (§4.3) | USD 149 por 4 reels → USD 400-600/mes (12-16 reels) | Email → DM de IG como seguimiento | 4-10% | **7,5** |
| 2 | **"Ad creative test: 5 variantes en 72 h"** | Anunciantes activos en Meta Ad Library (e-commerce DTC, clínicas, cursos) con ≥ 3 anuncios, todos estáticos o repetidos | 1 variante en video de uno de sus anuncios actuales (gancho distinto, formato 9:16) | USD 249-399 por sprint de 5 → USD 800-2.000/mes (20 creativos) | Email | 3-8% | **8** |
| 3 | **White-label para agencias:** "tu equipo de edición sin contratar" | Agencias de marketing chicas (2-15 personas) en EE.UU. y LATAM que publican casos de redes sociales | Edición de prueba gratis **con material que manda la agencia** | USD 25-60 por reel por volumen → retainer USD 800-2.000/mes | Email + Contra | 2-6% (pero un cliente vale 5-10 locales) | **8** |
| 4 | **"Tus mejores reseñas, en video"** (tipografía animada con la reseña real) | Negocios con ≥ 4,7 y ≥ 100 reseñas y redes flojas | 1 video de 10 s con una reseña **anonimizada** ("— Cliente verificado") | USD 99 por 5 videos → mensual | Email | 3-6% | **5,5**: el texto de la reseña es del reseñador, así que hace falta su permiso (las pautas de Google lo sugieren). La regla FTC 16 CFR 465 (vigente desde 2024-10-21, hasta USD 51.744 por infracción) prohíbe testimonios falsos o de personas generadas por IA. **Nunca un avatar IA "diciendo" la reseña** |
| 5 | **Fotos de producto con IA** (fondo, lifestyle, packshots) | Tiendas Shopify/Etsy chicas con fotos caseras | 3 fotos de su ficha rehechas (privadas) | USD 99 por 10 fotos → catálogo o mensual | Email | 4-8% | **7** |
| 6 | **"Video de tu propiedad en 24 h"** (reel desde las fotos del listado) | Agentes inmobiliarios de EE.UU. (hispanos primero) con listados sin video | Reel de 15 s de un listado activo (las fotos son del fotógrafo o del agente: uso privado, solo para él) | USD 49-79 por listado → USD 249/mes ilimitado (hasta 8 listados) | Email | 3-7% | **6**: **commodity**: hay video IA de inmobiliaria desde USD 0,38 hasta USD 50 (vo3ai, 2026) y edición tercerizada a USD 30-150 por video (fotober). Diferenciarse por velocidad + gancho + versión en español |
| 7 | **"De tu webinar/podcast a 10 clips"** | Consultores, coaches, SaaS B2B con YouTube o podcast | 1 clip de 30-45 s sacado de su último episodio | USD 300-450/mes (12-20 clips) | Email | 3-7% | **7**: sinergia con el proyecto `clipper-semiauto` |
| 8 | **"YouTube resucitado"** | Negocios con canal abandonado (último video > 6 meses) | 3 shorts sacados de sus videos viejos | USD 199 por pack único → mensual | Email | 3-6% | **6,5** |
| 9 | **Subtitulado y versión en español de sus videos** | Marcas de EE.UU. que venden a hispanos (o quieren hacerlo) | 30 s de su video con subtítulos en español (y opcionalmente voz IA **de catálogo**, nunca clonada sin permiso) | USD 150-500 por video → paquete mensual | Email | 3-8% | **7,5**: el español nativo es una ventaja real, competencia menor [inferencia] |
| 10 | **Refresh de la ficha de Google** (video + fotos) | Locales con buen puntaje y la ficha con fotos pobres (sin video) | 1 foto mejorada + 1 video corto para la ficha | USD 99 único → mensual de posteos | Email (EE.UU.); WhatsApp con opt-in (AR) | 3-6% | **6,5** (ya existe la versión AR en el estudio del 2026-10-01, H1. Acá es la versión outbound en USD) |
| 11 | **Pack de temporada: Black Friday / Navidad** (6 creativos) | E-commerce y locales con pauta activa | 1 creativo navideño con su producto | USD 299 por 6 → mensual en enero | Email | 4-8% en **octubre-noviembre de 2026** (después cae) | **7,5**: ventana de tiempo concreta (BFCM 2026-11-27 a 11-30) |
| 12 | **Reels de "antes y después"** | Contratistas, odontólogos, peluquerías, detailing de autos con fotos de antes y después | 1 reel con sus propias fotos de antes y después | USD 200/mes por 4 reels | Email + DM de IG | 3-6% | **6,5**: ojo con fotos de pacientes, necesitan consentimiento (lo gestiona el cliente) |
| 13 | **Motor mensual de contenido "sin cara"** para profesionales (b-roll IA + voz en off + texto) | Abogados de inmigración, contadores y realtors hispanos | 1 reel educativo de 20 s con su tema ("3 errores al renovar la green card") | USD 500-900/mes (12 reels) | Email | 2-5% | **7**: ticket alto, pero en temas legales los textos los valida el profesional |
| 14 | **Video explicativo para la home** (motion graphics IA) | SaaS chicos y servicios B2B sin video en la web | Guion + storyboard de 6 cuadros gratis | USD 500-1.500 por video | Email | 1-4% | **6** |
| 15 | **Anuncios estilo UGC con avatar IA, declarados** | E-commerce DTC chico | 1 anuncio de 15 s con avatar de catálogo | USD 300 por 3 | Email | 3-6% | **5,5**: competencia directa de herramientas autoservicio: Creatify desde USD 19-39/mes, Arcads USD 77-110/mes (creatify.ai, eesel 2026). Riesgo FTC si se presenta como cliente real. Hay que etiquetar el contenido IA |
| 16 | **Tour de 30 s de un salón de eventos o venue** | Salones, venues de casamientos, coworkings | Tour hecho con sus fotos públicas | USD 150 → contenido mensual | Email | 2-5% | **5,5** |
| 17 | **Auditoría en video "sin cara"** (grabación de pantalla con voz: "3 cosas que te restan views") | Cualquiera de los públicos de las ideas 1, 2 y 12 | La auditoría **es** la muestra (2-3 min) | Gratis → USD 149 → mensual | Email (2º mail) | 5-12% en los leads de mayor puntaje (vendedores de video dicen 2-4x [sesgo]) | **7**: barata de producir (~10 min por prospecto) y no expone la cara |
| 18 | **Reels para inmobiliarias y desarrolladoras de AR** | AR/LATAM | Reel de una unidad publicada en Zonaprop o en su Instagram | ARS (equivalente a USD 30-80) por unidad → mensual | **Instagram + WhatsApp con opt-in, no email** | 5-15% por DM manual [inferencia] | **5,5**: ticket bajo en pesos; sirve como gimnasio de portfolio |

**Top 4 para arrancar:** #2 (ad creative test), #3 (white-label para agencias), #1 (reel rehecho para hispanos de EE.UU.) y #11 (temporada BFCM, con ventana hasta ~2026-11-20). La #9 queda como diferencial de idioma.

---

## 8. Plan de 14 días (de 2026-10-05 a 2026-10-18)

**Principio:** el warm-up corre **en paralelo** mientras se arman la lista y las muestras. El primer envío real a los mejores leads sale el **día 12**, con volumen bajo.

| Día | Fecha | Tareas | Horas | Entregable |
|---|---|---|---|---|
| 1 | 2026-10-05 | Elegir el nombre de la marca y chequear disponibilidad (USPTO/INPI y `.com`). Comprar el **dominio principal + 2 secundarios** en Cloudflare (~USD 31). Elegir **un** público inicial (recomendado: #2 o #1, hispanos de EE.UU.) | 3 | Marca + 3 dominios |
| 2 | 2026-10-06 | Google Workspace (2 usuarios, 1 por dominio secundario). Claude configura **SPF, DKIM y DMARC (p=none)** por el MCP de Cloudflare. Redirección de los secundarios a la web principal. Buzón virtual en EE.UU. (Anytime Mailbox/iPostal1) | 3 | Buzones autenticados |
| 3 | 2026-10-07 | Conectar los buzones a Instantly Growth (o Mailmeteor Premium) y **prender el warm-up** (no tocar más hasta el día 12). Abrir Payoneer y revisar el monotributo (nombre de fantasía, Factura E) | 2 | Warm-up corriendo |
| 4 | 2026-10-08 | Scraping con Apify u Outscraper: **400-600 negocios** de 1-2 rubros × 2-3 ciudades (por ejemplo, restaurantes y estéticas hispanas en Houston, Miami y LA). Cruce con Meta Ad Library | 3 | Planilla cruda |
| 5 | 2026-10-09 | Enriquecer emails (web propia → Hunter free). Verificar con NeverBounce (1.000 gratis). **Puntaje de señales** (§3.3) automático. Quedarse con **150-200** | 3 | Lista verificada y puntuada |
| 6-7 | 2026-10-10/11 | **Portfolio inicial:** 3-4 piezas con material propio o de stock + Higgsfield (sin material de terceros). Landing en Cloudflare Pages: portfolio, paquetes, política de privacidad, dirección y baja | 6 | Web de la marca |
| 8 | 2026-10-12 | Revisión humana de los 50 mejores (Instagram, anuncios). Claude redacta `{{observacion}}` para cada uno y vos lo corregís. Escribir las secuencias ES/EN (§9) con el pie legal | 4 | 50 líneas personalizadas + secuencias |
| 9-10 | 2026-10-13/14 | Producir **20-30 muestras** para los mejores (15-30 min cada una con plantilla). Páginas privadas `/m/negocio` | 8 | 20-30 muestras listas |
| 11 | 2026-10-15 | **Prueba de entrega:** mandar a 5-10 casillas propias (Gmail, Outlook, Yahoo) y revisar si cae en la bandeja o en spam. Verificar la baja de punta a punta. Revisar DMARC | 2 | Checklist de entrega OK |
| 12 | 2026-10-16 | **Primer envío:** 20-30 mails (los mejores leads, los que tienen muestra), **10-15 por buzón**, con el warm-up siempre prendido | 1 | Tanda A enviada |
| 13 | 2026-10-17 | Responder dentro de las 2 h hábiles. Mandar las muestras a quienes dijeron "sí". Pasar a WhatsApp solo con permiso | 2 | Conversaciones |
| 14 | 2026-10-18 | Medir y decidir: si rebotes < 2%, quejas = 0 y respuesta ≥ 3%, programar los 120-170 restantes en ~7-10 días (20-30 por buzón por día). Si la respuesta es < 2%, **cambiar la oferta o el público antes que el volumen** | 2 | Tablero + decisión |

**Total: ~40 h en 14 días** (dentro de las 10-15 h/semana de construcción, estirándolo un poco). La secuencia completa de los 200 termina alrededor del **2026-10-31**.

**Métricas objetivo (por tanda de 150-200 prospectos):**

| Métrica | Umbral rojo | Objetivo | Bueno |
|---|---|---|---|
| Rebote | > 3% (frenar) | < 2% | < 1% |
| Quejas de spam | ≥ 0,3% (frenar todo) | 0 | 0 |
| Bajas | > 3% | < 2% | < 1% |
| Respuesta total | < 2% | 3-6% | ≥ 8% |
| Respuesta positiva ("mandala", "¿cuánto?") | < 1% | 1,5-3% | ≥ 4% |
| Muestras pedidas | — | 4-8 | 10+ |
| Clientes pagos al día 30 (2026-11-04) | 0 | 1-2 | 3+ |

---

## 9. Plantillas (3 mails, ES y EN)

**Reglas:** < 80 palabras, sin links ni imágenes en el mail 1, texto plano, una sola pregunta, firma con nombre de pila + marca, y el **pie legal siempre**.

### 9.1 Español (público: negocio hispano en EE.UU.; para AR se agrega la leyenda de la Ley 25.326)

**Mail 1 (día 0). Asunto:** `tu reel del {{fecha_reel}}`

> Hola {{nombre_o_equipo}},
>
> Vi el reel de {{tema_reel}} de {{negocio}}. {{observacion}} (ej.: "los primeros 3 segundos no muestran el plato y no tiene subtítulos").
>
> Me tomé el atrevimiento de rehacerlo en 2 versiones de 15 s, con gancho y subtítulos. Es una muestra privada, no la publico.
>
> ¿Te la mando?
>
> Facu · {{Marca}}

**Mail 2 (día 3). Asunto:** (en el mismo hilo)

> {{nombre}}, te dejo la muestra por si te sirve: {{link_muestra}} (20 s, sin registro).
>
> Si te gusta, armamos 4 así por mes desde USD 149, con entrega en 7 días. Si no te sirve, no pasa nada.
>
> Facu · {{Marca}}

**Mail 3 (día 8). Asunto:** (en el mismo hilo)

> Último mensaje, {{nombre}}. ¿Quién maneja el contenido de {{negocio}}? Si no sos vos, ¿me pasás a quién escribirle?
>
> Si ahora no es momento, respondé "no" y no te escribo más.
>
> Facu · {{Marca}}

**Pie legal (en todos los mails):**

> {{Marca}} · {{Dirección postal (buzón virtual)}} · Te escribimos porque tu email figura públicamente en {{fuente: el sitio web de tu negocio}}. Si no querés recibir más mensajes, respondé "BAJA" o entrá a {{link_baja}}: te damos de baja de inmediato. *(Para destinatarios en Argentina:)* Podés solicitar el retiro o bloqueo, total o parcial, de tus datos de nuestra base (art. 27 inc. 3 Ley 25.326).

### 9.2 English (US businesses)

**Email 1 (day 0). Subject:** `your {{reel_topic}} reel`

> Hi {{first_name_or_team}},
>
> Saw {{business}}'s reel about {{reel_topic}}. {{observation}} (e.g., "the first 3 seconds don't show the product and there are no captions").
>
> I re-cut it into two 15-second versions with a stronger hook and captions, as a private sample. I won't post it anywhere.
>
> Want me to send it over?
>
> Facu · {{Brand}}

**Email 2 (day 3). Subject:** (same thread)

> {{first_name}}, here's the sample in case it's useful: {{sample_link}} (20 sec, no login).
>
> If you like it, we can do 4 like this per month starting at $149, delivered in 7 days. If not, no worries.
>
> Facu · {{Brand}}

**Email 3 (day 8). Subject:** (same thread)

> Last note, {{first_name}}. Who handles content at {{business}}? If it's not you, could you point me to the right person?
>
> If now's not a good time, just reply "no" and I won't follow up.
>
> Facu · {{Brand}}

**Footer:**

> {{Brand}} · {{US virtual mailbox address}} · This is a one-time business inquiry sent to the email listed on your website. Reply "unsubscribe" or click {{unsubscribe_link}} and you won't hear from us again.

**Variante para la oferta #2 (ad creative test), mail 1, ES:** "Vi que {{negocio}} tiene {{n}} anuncios activos en Meta y todos son {{estáticos / el mismo video}}. Armé una variante en video de tu anuncio '{{titulo}}' con otro gancho. ¿Te la mando?"

---

## 10. Presupuesto mensual del sistema

| Concepto | Austero | Estándar | Nota |
|---|---|---|---|
| Dominios (3 × USD 10,46/año) | USD 2,60 | USD 2,60 | Pago anual de USD 31 por adelantado |
| Casillas (Workspace USD 7 por usuario) | USD 14 (2 usuarios) | USD 28 (4 usuarios) | Promo anual: USD 4,90 por usuario el primer año |
| Herramienta de envío y warm-up | USD 17,99 (Mailmeteor Premium) | USD 47 (Instantly Growth) | Smartlead Base USD 39 / Saleshandy USD 34 como alternativas |
| Leads (Apify/Outscraper) | USD 0 (planes gratis: 500 por mes en Outscraper) | USD 5-10 | Para 200-600 lugares por mes |
| Búsqueda y verificación de emails | USD 0 (Hunter 50 + NeverBounce 1.000 gratis) | USD 5-10 | NeverBounce USD 8 cada 1.000 después |
| Buzón virtual en EE.UU. (CAN-SPAM) | USD 5 (Anytime Mailbox) | USD 10 (iPostal1) | Obligatorio para EE.UU. |
| Web y páginas de muestras | USD 0 (Cloudflare Pages) | USD 0 | — |
| Video de prospección | USD 0 (Loom free / OBS) | USD 49 (Sendspark Solo) | Solo si las auditorías en video rinden |
| Producción (Higgsfield, música de stock, CapCut) | [ya tiene Higgsfield; música de stock ~USD 10-15, NO VERIFICADO] | USD 15-30 | El plan comercial de Higgsfield ya está recomendado en el estudio del 2026-10-01 |
| **Total mensual** | **≈ USD 40-55** | **≈ USD 110-160** | Inicial único: ~USD 31 de dominios + primer mes |

**Recomendación:** arrancar en **Austero** (Mailmeteor + 2 casillas de Workspace) y pasar a Instantly solo si se superan ~300 prospectos por mes o hacen falta más de 2 buzones. Con < USD 500 de capital, el sistema consume **~10% del capital por mes**: si a los 60 días (2026-12-05) no hay ≥ 2 clientes pagos, se apaga y se reevalúa.

---

## 11. Trampas (leer antes de mandar el primer mail)

1. **Mandar a Argentina por email "porque es más fácil".** Es legal, pero las PyMEs argentinas responden por WhatsApp e Instagram, y el ticket es en pesos.
2. **España en frío.** La LSSI art. 21 lo prohíbe sin consentimiento; las guías de vendedores que dicen "con `info@` se puede" son lecturas interesadas.
3. **Gmail personal o dominio principal.** Si se quema, perdés la cuenta o la marca.
4. **Links o adjuntos en el primer mail, y seguimiento de aperturas.** Bajan la entrega.
5. **4 o más seguimientos con dominios nuevos.** Triplican quejas (Belkins); a escala de 150 mails, una queja ya supera el 0,3%.
6. **Publicar en el portfolio la muestra hecha con material del prospecto** sin su permiso escrito, o con su música. Es infracción de derechos y además te expone.
7. **Avatares IA "haciendo de clientes"**, o reseñas convertidas en testimonios sin permiso: regla FTC 16 CFR 465 (hasta USD 51.744 por infracción) y pautas de Google.
8. **Clonar voces o caras ajenas** para "personalizar" (deepfake). Solo tu voz, o voces de catálogo.
9. **Pseudónimo completo + LinkedIn falso.** Destruye la confianza al primer chequeo y viola los términos de la plataforma.
10. **WhatsApp masivo o bots de DMs en Instagram.** Baneo del número o bloqueos de la cuenta de marca.
11. **Competir por precio contra la IA autoservicio.** Video de inmobiliaria desde USD 0,38; Creatify desde USD 19 por mes. Vender **resultado y tiempo ahorrado** (constancia mensual, gancho, testeo de creativos), no "edición".
12. **Creerle a los benchmarks.** El 10,7% es el top 10% de los usuarios de Instantly. Planificar con 2-6%.
13. **Escalar volumen cuando la respuesta es baja.** Si la respuesta es < 2%, el problema es la oferta o la lista, no la cantidad.
14. **Olvidar el lado fiscal.** Factura E + monotributo: todo suma al tope, y la factura muestra tu nombre legal (límite del anonimato).
15. **Workspace no es inmune.** Su política de uso aceptable prohíbe el email masivo no solicitado. Volumen bajo + relevancia + baja visible, o se arriesga la suspensión.

---

## 12. Fuentes (consultadas el 2026-10-02)

**Legal**
- FTC, CAN-SPAM Act: A Compliance Guide for Business: https://www.ftc.gov/business-guidance/resources/can-spam-act-compliance-guide-business
- CRTC, guía de consentimiento implícito CASL: https://crtc.gc.ca/eng/com500/guide.htm · OBA 2020 (FCA, excepción de comunicaciones de negocio): https://oba.org/Sections/Privacy-Law/Articles/Articles-2020/June-2020/FCA-confirms-CASL-is-constitutional,-but-limits-bu
- Overloop, guía de cold email B2B en España (2026-05, vendedor): https://overloop.com/blog/es/b2b-cold-email-espana-rgpd-aepd
- Multas de la AEPD por art. 21 LSSI: https://www.genbeta.com/actualidad/que-te-envien-correos-publicidad-que-te-dejen-rechazarlos-puede-salir-caro-a-quien-envia-aepd-multa · https://www.economistjurist.es/actualidad-juridica/jurisprudencia/sancionada-con-5-000-euros-una-consultora-energetica-por-el-envio-constante-y-no-autorizado-de-publicidad-a-una-persona · https://lawwwing.com/nueva-sancion-por-el-envio-de-spam-es-posible-hacerlo-legalmente · Fieldfisher: https://www.fieldfisher.com/es-es/locations/spain/insights/bases-datos-empresariales
- Argentina: Decreto 1558/2001: https://www.argentina.gob.ar/normativa/nacional/norma-151221/texto · Ley 26.951 / Decreto 2501/2014: https://www.argentina.gob.ar/normativa/nacional/240407/texto · Diario Judicial (sin ley anti-spam, 2010): https://www.diariojudicial.com/news-21287-tienes-un-e-mailno-deseado · Proyecto 5051-D-2022: https://www4.hcdn.gob.ar/dependencias/dsecretaria/Periodo2022/PDF2022/TP2022/5051-D-2022.pdf
- México, nueva LFPDPPP 2025: https://www.hoganlovells.com/en/publications/mexicos-new-federal-data-protection-law-what-it-means-for-companies · https://www.ey.com/es_mx/technical/tax/boletines-fiscales/nueva-ley-federal-proteccion-datos-personal-posesion-particulares
- Regla FTC de reseñas falsas (16 CFR 465): https://www.whitecase.com/insight-our-thinking/no-fake-clout-ftc-issues-new-rule-crack-down-fake-consumer-reviews-and · https://frostbrowntodd.com/ftcs-new-rule-on-consumer-reviews-ensuring-compliance-with-human-and-ai-generated-content
- Meta v. Bright Data (2024-01-23): https://www.fbm.com/data-analytics/publications/major-decision-affects-law-of-scraping-and-online-data-collection-meta-platforms-v-bright-data/
- Pseudónimos en cold email: https://fullenrich.com/content/should-i-use-my-real-name-for-cold-email · https://mailtrap.io/blog/can-spam-cold-emails/
- Monotributo y Factura E: https://www.iprofesional.com/impuestos/387600-como-facturar-al-exterior-siendo-monotributista-2023 · https://yo-facturo.com/blog/como-facturar-al-exterior-monotributo/

**Entregabilidad**
- Google, requisitos para remitentes: https://support.google.com/a/answer/81126
- Endurecimiento de Gmail desde 2025-11: https://help.zoho.com/portal/en/community/topic/gmail-is-ramping-up-its-email-sender-policy-as-of-november-2025 · https://www.suped.com/knowledge/email-deliverability/compliance/how-likely-is-gmail-to-enforce-the-less03percent-spam-rate-limit-within-the-next-year
- Microsoft 2025-05-05: https://dmarcian.com/microsoft-enforces-spf-dkim-dmarc/ · https://resend.com/blog/microsoft-bulk-sending-requirements-2025
- Política de uso aceptable de Workspace y suspensiones: https://workspace.google.com/intl/en_sg/terms/use_policy.html · https://suped.com/email-deliverability/answers/why-are-sales-reps-google-workspace-emails-suspended-when-using-sales-tools-like-outreach-or-yes
- Límites y warm-up: https://www.smartlead.ai/blog/how-many-cold-emails-per-day · https://leadhaste.com/blog/email-warmup-best-practices · https://instantly.ai/blog/secondary-domains/ · https://helpcenter.smartlead.ai/en/articles/147-all-you-need-to-know-about-secondary-sending-domains-for-cold-email-campaigns
- Precios: https://instantly.ai/pricing · https://www.smartlead.ai/pricing · https://www.saleshandy.com/pricing/ · https://www.lemlist.com/pricing · https://mailmeteor.com/pricing · https://workspace.google.com/pricing · https://www.zoho.com/mail/zohomail-pricing.html · Apollo (secundario): https://www.zeliq.com/blog/apolloio-pricing · Cloudflare .com: https://domainoffer.net/tld/com/cloudflare

**Leads**
- Apify Google Maps Scraper: https://apify.com/compass/crawler-google-places
- Outscraper (secundario): https://syncgtm.com/blog/outscraper-review-2026 · https://us.fitgap.com/products/outscraper
- Hunter: https://hunter.io/pricing · NeverBounce/ZeroBounce: https://bouncezero.io/zerobounce-vs-neverbounce · https://leadmagic.io/comparisons/neverbounce-vs-zerobounce
- Meta Ad Library como señal: https://omnionlinestrategies.com/blog/marketing-agencies-meta-ad-library-new-clients · https://apify.com/peaceably_sitar/lead-radar

**Conversión y mercado**
- Instantly Cold Email Benchmark Report 2026: https://instantly.ai/cold-email-benchmark-report-2026
- Belkins 2025: https://belkins.io/blog/sales-follow-up-statistics · resumen: https://prospeo.io/s/cold-email-reply-rate
- Agregadores: https://www.getboomerang.ai/glossaries/cold-email-reply-rate-benchmarks-2026 · https://mailshake.com/blog/cold-email-benchmarks-2026/
- Snov.io, multicanal en Brasil: https://snov.io/blog/web-summit-multichannel-outreach-research/
- Video personalizado: https://smartreach.io/blog/ai-video-for-cold-email-outreach/ · https://syncgtm.com/blog/personalized-video-emails-sales · Sendspark: https://pricingsaas.com/companies/sendspark · https://blog.sendspark.com/best-video-prospecting-tools · Tavus: https://supersend.io/ai/tavus
- Política de WhatsApp: https://developers.facebook.com/documentation/business-messaging/whatsapp/getting-opt-in · https://respond.io/blog/whatsapp-business-banned
- Límites de DMs en Instagram: https://inro.social/blog/how-many-direct-messages-can-you-send-on-instagram · https://metricool.com/instagram-limits/
- Precios de edición de video: https://vidico.com/news/video-editor-cost/ · https://www.videotto.com/blog/how-much-does-video-editing-cost-global-2026
- Video inmobiliario: https://www.vo3ai.com/blog/38-vs-800-real-estate-listing-videos-without-a-videographer-in-2026-2026-07-10 · https://fotober.com/real-estate-video-pricing
- Herramientas de UGC con IA: https://creatify.ai/blog/the-8-best-ai-ugc-ad-tools-in-2026 · https://www.eesel.ai/en/blog/arcads-ai-pricing
- White-label y agencias: https://vidpros.com/marketing-agency-video-production/ · https://www.enrichlabs.ai/blog/video-marketing-agency-complete-guide-2026
- Buzones virtuales: https://www.quicksprout.com/best-virtual-mailbox · https://g2.com/products/ipostal1/pricing
- Reseñas de Google y permiso del autor: https://seroundtable.com/archives/022797.html

## 13. Pendientes para verificar (cuando haya cuota de búsqueda)

- Precio exacto del add-on de contactos del actor de Apify (¿por lugar o cada 1.000?) y el crédito gratis de Apify en 2026.
- Si el REPEP de Profeco (México) cubre email; tope de multas CASL; detalle de PECR para autónomos (Reino Unido).
- Si el proyecto argentino de "No Llame" para email se sancionó (la Ley 26.951 cubre telefonía).
- Precios 2026 de Woodpecker, YAMM, Snov, Findymail y Zoho Mail Lite.
- Un benchmark **independiente** (no de un vendedor) de respuesta a cold email con muestra gratis.
