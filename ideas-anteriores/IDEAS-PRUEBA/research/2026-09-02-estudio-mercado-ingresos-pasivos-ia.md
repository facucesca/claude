# Estudio de mercado: ingresos semi-pasivos con IA (2026-09-02)

**Metodología:** 5 investigaciones paralelas con ~75 búsquedas web y ~30 fuentes primarias verificadas (políticas oficiales con fecha, reportes de plataformas, estudios académicos y de CTR, casos con revenue verificable). Perfil evaluado: dev solo en Argentina, Claude Code + APIs de IA, capital asumido < USD 500-1.000, horizonte de construcción 3-5 meses. Detalle completo por dominio en [`fuentes/`](fuentes/).

---

## Resumen ejecutivo

1. **"Dejar la compu trabajando" al 100% no existe en 2026.** Las plataformas lo prohibieron formalmente (YouTube 15/7/2025, TikTok 15/9/2025, Spotify 9/2025, Amazon KDP a nivel cuenta) y los mercados lo arbitraron (trading, SEO de contenido). Lo que sí existe: **activos que corren solos con 2-8 h/semana de guardia técnica**, construidos durante 2-4 meses.
2. **La verdad estadística: la mediana de casi todo esto es ~USD 0-500/mes.** App mediana al año: $72/mes (RevenueCat, 115k apps). Creador mediano de Gumroad: < $100 en toda su vida. Clipper mediano: $305 de por vida (corrección 2026-10-08: es un promedio, no una mediana). El plan serio no busca "la idea ganadora": arma un **portfolio de apuestas baratas** y duplica en la que muestra señal.
3. **Tu ventaja real no es una idea, es una asimetría:** podés construir y *mantener* software con agentes a un costo que hace 2 años era imposible (scrapers que se auto-reparan, catálogos de 20 productos operados por una persona). Las ideas elegidas explotan exactamente eso.
4. **La tendencia emergente más fuerte encontrada: la economía agéntica.** Apify pagó USD 1M a creadores en un solo mes (5x año contra año) y habilitó pagos de agente-a-máquina (x402); los agentes de IA ya descubren, ejecutan y **pagan** herramientas solos. Venderle picos y palas a los agentes es la ventana de timing de 2026.
5. **Trading bots: descartado como fuente de ingreso con este capital.** La evidencia es de las más robustas de las finanzas: 70-97% de traders retail pierde (97% en el estudio brasileño de day traders persistentes), y con USD 1.000 hasta un milagroso 15% anual son $12,50/mes. Detalle en la ficha D1.
6. **Argentina no es el problema que parecía.** Cepo levantado (14/4/2025), Payoneer resuelve Etsy/KDP/Adobe/Paddle, Apify paga por SWIFT, Telegram Stars sale por cripto. Los canales rotos: Stripe directo (no opera AR), Notion Marketplace, Discord nativo, TikTok Creator Rewards (no disponible), Gumroad (frágil).

**Recomendación central:** construir el **"stack de datos"** — un solo activo subyacente (scrapers/datos de nichos LATAM y agénticos) monetizado por varios canales a la vez (Apify + micro-herramientas SEO + MCP + bot de Telegram + eventual SaaS de alertas B2B), con el clipping como experimento de cash-flow rápido aparte. Roadmap por fases al final.

---

## Ranking de ideas (filtradas de ~25 evaluadas)

Puntaje compuesto según los 7 criterios de CLAUDE.md (rentabilidad mediana, automatización, capital, tiempo al primer dólar, riesgo, durabilidad, fit con tu stack).

| # | Idea | Score | Primer dólar | Mediana 12m | Techo 12m (top 10%) | Horas/sem en régimen |
|---|------|-------|--------------|-------------|---------------------|----------------------|
| 1 | Actores de scraping en Apify Store (nichos LATAM + agénticos) | **8/10** | 2-6 semanas | USD 300-1.000/mes | USD 5-10k/mes | 4-8 |
| 2 | Portfolio de micro-herramientas web + MCP (tool-SEO) | **7/10** | 4-8 meses | USD 100-500/mes | USD 1,5-5k/mes | 2-5 |
| 3 | Micro-SaaS de monitoreo/alertas B2B de nicho | **7/10** | 4-10 semanas | USD 200-1.000/mes | USD 2-8k/mes | 2-6 |
| 4 | Clipping economy + scanner de campañas propio | **6,5/10** | Días | USD 300-1.500/mes | USD 2k/mes + venta del tooling | 7-15 (no pasivo) |
| 5 | Bots de Telegram utilitarios (Stars / Mercado Pago) | **6/10** | 2-5 semanas | USD 50-300/mes | USD 1-3k/mes | 1-4 |
| 6 | Templates n8n + afiliados 30% (nicho hispano) | **6/10** | 1-3 meses | USD 0-300/mes | USD 500-3k/mes | 6-10 |
| 7 | Extensión de Chrome de nicho B2B | **6/10** | 2-6 semanas | USD 0-500/mes | USD 2k/mes | 1-4 |
| 8 | Canal YouTube long-form editorial (RPM alto) | **5/10** | 4-8 meses | USD 0 | USD 0,5-3k/mes | 4-10 |
| 9 | Stock IA curado (Adobe Stock video / Freepik) | **4/10** | 6-13 semanas | USD 50-300/mes | USD 1k/mes | 3-6 |

---

## Fichas de las ideas

### 1. Actores de scraping en Apify Store — 8/10 ⭐ NÚCLEO RECOMENDADO

**Qué es:** publicar "actores" (scrapers/automatizaciones) en el marketplace de Apify; usuarios **y agentes de IA** pagan por uso (pricing pay-per-event). Vos cobrás el 80% del revenue menos costos de plataforma.

**Por qué ahora (3 vientos de cola verificados):**
- Apify pagó **USD 1M a creadores en un solo mes** (5x vs un año antes; dato oficial).
- **Pagos agénticos habilitados** (x402/USDC + Skyfire): agentes descubren, ejecutan y pagan actores sin cuenta. Diseñar actores para agentes (MCP-friendly) es la frontera con menos competencia.
- **Migración forzada a pricing PPE en octubre 2026**: reordena el store completo y deja mal precificados a los actores viejos — ventana para entrar con pricing correcto.

**Números realistas:** promedio ~USD 470/dev/mes entre ~3.000 devs que cobran (mediana menor, cola larga). Caso documentado de referencia: 98 actores en 6 meses → 2.500 usuarios; lo que paga son **nichos sin competencia**, no LinkedIn/Amazon. Estimación honesta: 6 meses con 15-30 actores de nicho: USD 100-500/mes; 12 meses: USD 300-1.000 mediana, USD 5-10k top 10%.

**Tu ángulo:** (a) fuentes LATAM/hispanas casi vírgenes (Mercado Libre por vertical, inmobiliarias/empleo AR, boletines oficiales, licitaciones, datos BCRA); (b) actores auto-reparables con Claude Code (el costo clásico del scraping es el mantenimiento — tu moat); (c) cada actor se re-expone como MCP server y alimenta las ideas 2, 3 y 5.

**Riesgos:** dependencia de una plataforma privada; ToS/legalidad del scraping recae en vos; 20.000+ actores ya publicados (los nichos obvios están tomados); mantenimiento perpetuo (HTML cambia). Cobro AR: SWIFT (mín USD 100) + Factura E, viable.

### 2. Portfolio de micro-herramientas web + MCP — 7/10 ⭐ SATÉLITE

**Qué es:** 20-50 calculadoras/conversores/generadores gratuitos apuntando a long-tail de nichos, monetizados con ads (Journey by Mediavine acepta desde **1.000 sesiones/mes**, 70% revenue share) + afiliados + tier pro vía Paddle.

**Por qué resiste:** es la tesis anti-AI-Overviews mejor documentada de 2026 (Ahrefs, 16/7/2026): un resumen de IA puede explicar la fórmula pero **no puede ejecutar el cálculo**. Referencias: Omni Calculator ~2,3M visitas US/mes; FreeConvert 1,5M/mes. Mientras tanto, el CTR de contenido leíble se derrumbó (-34,5% a -61% con AIO según Ahrefs/Seer; el core update de marzo 2026 les sacó 50-80% a los sitios programáticos de bajo valor). **Lo que se lee muere; lo que se usa sobrevive.**

**Tu ángulo:** gap enorme en español (sueldo neto AR, monotributo, plazo fijo vs dólar, calculadoras regulatorias — competencia ~nula); hosting ~$0 en Cloudflare (ya lo tenés); cada herramienta reutiliza datos de los actores de la idea 1 y se expone también como MCP; páginas diseñadas para ser **citadas por LLMs** (datos + herramienta en la misma página, llms.txt).

**Contras:** lento (AdSense paga a los 4-8 meses típicamente); RPM modesto salvo tráfico US; dependencia de Google; las tools triviales corren riesgo con AI Mode a 2-3 años. Es el activo compuesto de largo plazo, no el cash inicial.

### 3. Micro-SaaS de monitoreo/alertas B2B de nicho — 7/10 ⭐ EL ACTIVO VENDIBLE

**Qué es:** suscripción B2B (USD 9-49/mes) por monitorear algo específico que a un negocio le duele: licitaciones de una industria, cambios regulatorios, stock/precios de competidores, menciones de marca en respuestas de IA ("AI visibility monitoring" — categoría emergente real).

**Números realistas:** referencia de techo honesto: Healthchecks.io, un solo founder, $14k MRR... a los 9 años. Mediana a 12 meses: USD 200-1.000 MRR. El churn es el enemigo (9,1%/mes bruto en SaaS chico — ChartMogul). **El premio está en la salida:** micro-SaaS rentables se venden a **~3,9x profit anual** en Acquire.com (mediana feb-2026, 81 días promedio en mercado). Un monitor que llega a $2k MRR ≈ venta plausible de USD 40-75k.

**Tu ángulo:** es la versión premium del mismo stack de datos de las ideas 1-2; scrapers auto-reparables bajan 10x el costo de mantenimiento que mató a otros; cobro vía Paddle→Payoneer (probado desde AR).

**Contras:** distribución = el cuello de botella real (los primeros 50 clientes nunca llegan solos); hard paywall + trial largo según datos de RevenueCat; hay que elegir sub-nicho quirúrgicamente (los monitores genéricos están regalados o fondeados con VC).

### 4. Clipping economy + scanner de campañas — 6,5/10 ⭐ CASH-FLOW INMEDIATO

**Qué es:** marcas/streamers pagan por 1.000 vistas de clips (Whop Content Rewards: $0,20-6/1k, promedio real cobrado ~$0,39/1k; campañas B2B/IA pagan hasta **$25/1k**). Primer dólar en **días**, capital ~$0, cobro vía PayPal/cripto desde AR.

**La verdad:** la mediana del clipper es $305 *de por vida* (corrección 2026-10-08: es un promedio, no una mediana; además, el scanner de campañas ya existe en Apify con 83 usuarios en total) — es destajo digital saturado, no ingreso pasivo. **El ángulo que lo cambia:** casi nadie vende *inteligencia de campañas* (qué campaña tiene presupuesto restante, velocidad de quema, historial de pago del dueño). Un scanner hecho con Claude Code en 2-4 semanas te da ventaja para clipear con criterio **y es en sí un producto vendible** a un mercado demostrado de 8.400+ clippers activos. Bonus: ya tenés Higgsfield conectado (clipper + publicación TikTok).

**Rol en el plan:** financiar los meses de construcción de las ideas 1-3 y validar todo el circuito de cobro. No es el destino.

### 5. Bots de Telegram utilitarios — 6/10 (satélite de la idea 1)

Alertas de nicho (precios, dólar, tarifas, vuelos, restocks) sobre los datos que ya scrapeás. 95% automatizable, primer dólar en 2-5 semanas, y **el único canal sin fricción de cobro desde AR** (Stars→TON→exchange local; o Mercado Pago para público argentino). Techo bajo standalone (USD 1-3k/mes top; caso grande: AirTrackBot ~$8k/mes con 2M usuarios), pero como capa extra sobre datos existentes es casi gratis. Discovery débil: el growth no es pasivo.

### 6. Templates n8n + afiliados (nicho hispano) — 6/10

Dato clave verificado: **n8n no paga por templates** (no hay marketplace oficial pago; la librería gratis ya tiene 11.700+ workflows). Lo que sí funciona: templates de nicho en español (WhatsApp Business, Mercado Libre/Mercado Pago, facturación ARCA — competencia ~nula) vendidos a USD 29-299 vía Paddle/Whop + **afiliado 30% primer año de n8n Cloud** + template gratis en la librería oficial como funnel. Mediana sin canal de distribución: ~$0 — esto es un negocio de distribución. La plata grande del nicho está en implementación (no pasivo). Los marketplaces de MCP/agentes todavía **no pagan** (Smithery no monetiza creadores; GPT Store sigue en piloto) — cobrar un MCP propio como micro-SaaS sí es viable (entra en ideas 1/3).

### 7. Extensión de Chrome de nicho B2B — 6/10 (producto de aprendizaje)

Capital ~$5, primer dólar en 2-6 semanas, discovery orgánico del Web Store, 1-4 h/semana. Realista: $200-2.000/mes en nicho con intención de pago (e-commerce sellers, recruiters, agencias). Riesgo: Google puede suspender cuentas developer enteras con apelaciones opacas. Ideal como primer producto para validar el circuito completo (build→cobro→soporte) barato; no como activo principal.

### 8. Canal YouTube long-form editorial — 5/10 (opcional, con fecha límite)

La mediana es $0 y el 80-90% de los canales "de automatización" muere o queda desmonetizado en 12 meses. Solo sobrevive como **negocio editorial asistido por IA** (investigación propia, punto de vista, 4-10 h/semana; costo de producción colapsado a $2,5-5/video de 10 min). Nichos RPM alto: finanzas US $15-30, documental/historia $5-12. **Dato crítico: los requisitos del YPP se duplican el 1/2/2027** (8.000 h de watch/año o 20M vistas Shorts/90 días para nuevos aplicantes) — si esta idea entra al portfolio, hay que empezar antes de esa fecha. Política de "inauthentic content" (15/7/2025) desmonetiza retroactivamente lo mass-produced; la purga de enero 2026 lo demostró (16 canales, 35M subs).

### 9. Stock IA curado — 4/10 (experimento B de bajo esfuerzo)

**El único modelo genuinamente pasivo post-upload que sobrevivió la verificación.** Adobe Stock acepta imagen y video IA (royalty 33%/35%, Payoneer OK); Freepik acepta volumen (€0,04-0,07/descarga; tramitar certificado CDI para evitar retención española del 24%). Realista: USD 100-500/mes a los 12 meses con 10.000+ assets curados. Contra: sobreoferta estructural, earnings por asset cayendo. Ángulo: video IA (el costo de generar es el moat) y nichos que los generadores hacen mal. Shutterstock/Getty no aceptan IA — no intentar.

---

## Descartadas (y por qué — esto vale tanto como el ranking)

| Idea | Veredicto | Razón (con evidencia) |
|------|-----------|------------------------|
| **Bots de trading retail** (grid, DCA, arbitraje, copy, market making, DIY Freqtrade) | 1-3/10 | 70-97% de retail pierde (estudios Brasil/Taiwán/EEUU, disclosures legales de brokers); todo edge simple ya arbitrado (funding negativo récord 2026, ventanas de arbitraje de 12s→2,7s); con USD 1.000, hasta un 15% anual son $12,50/mes. El único ganador seguro es quien vende la pala. Freqtrade en dry-run vale como educación, no como ingreso. |
| **Staking / DeFi yields** | 4/10 | No es un negocio, es interés sobre un activo volátil: USD 500 → $15-70/año, con el precio del subyacente cayendo más que el yield (ETH 2026: +3% yield, -37% precio). Como estacionamiento de capital ocioso, aparte del proyecto. |
| **TikTok Creator Rewards desde AR** | 1/10 | No disponible en Argentina (8 países al 22/5/2026; México único hispano). Workaround con cuenta US = detección + suspensión. Revisar cada trimestre. |
| **Sitio de contenido + afiliados desde cero** | 2/10 | CTR orgánico -34% a -61% con AI Overviews (Pew/Ahrefs/Seer); core update mar-2026 golpeó afiliados -20/50%; el perfil "contenido IA sin autoridad" es exactamente el castigado. |
| **Música IA en streaming** | 2/10 | Spotify borró 75M de tracks (9/2025), spam filter contra uploaders masivos, discovery bloqueado por diseño; terreno legal en transición (settlements Suno/Udio). Campo minado. |
| **KDP low-content / POD genérico** | 3/10 | Saturación máxima, enforcement a nivel cuenta (KDP), aprobación Merch 30-40%, mediana < $50-100/mes, riesgo IP manual. Solo funciona con audiencia previa. |
| **Prompts / GPT Store / AI wrappers** | 2/10 | PromptBase: ~5 de cada 1.000 prompts superan $500 acumulado; GPT Store revenue share sigue en piloto US; wrappers = churn 30% peor y clonables. |
| **YouTube Shorts por AdSense** | 2/10 | RPM $0,01-0,07/1k. Solo útil como distribución para clipping (las mismas vistas pagan 10-100x vía Whop). |
| **Bots de Discord** | 4/10 | Monetización nativa limitada a US/EU/UK — vedada desde AR sin LLC. |
| **RapidAPI y venta de MCP en marketplaces** | — | RapidAPI desmantelado post-Nokia (2024). Marketplaces de MCP aún no pagan a creadores (Smithery confirmado). Cobrar MCP propio como micro-SaaS: sí (ideas 1/3). |
| **Newsletter automatizada standalone** | 4/10 | Producción automatizable, crecimiento no; conversión mediana a pago 0,62%; Stripe-AR sin resolver. Útil como capa de retención de otras ideas (ahí sube a 7/10). |

---

## Estrategia recomendada: el "stack de datos" + una línea de cash

La síntesis clave: **las ideas 1, 2, 3 y 5 son el mismo activo con cuatro bocas de cobro.** Scrapers de datos de nicho (LATAM + agénticos) →

```
                    ┌→ Apify Store (pagan usuarios y agentes, PPE)     [idea 1]
Datos de nicho ─────┼→ Micro-herramientas SEO + ads + tier pro          [idea 2]
(scrapers auto-     ┼→ MCP servers (agentes pagan por llamada)          [ideas 1/6]
 reparables)        ┼→ Bot Telegram de alertas (Stars/Mercado Pago)     [idea 5]
                    └→ SaaS de alertas B2B premium → venta 3,9x SDE     [idea 3]
```

Y en paralelo, **clipping + scanner (idea 4)** como línea de cash independiente que paga los meses de construcción.

### Roadmap 3-5 meses (con gates de corte)

**Fase 0 — Rieles (semanas 1-2):**
- Abrir/verificar: Payoneer, cuenta Apify (+ configurar payout SWIFT), onboarding de Paddle, cuenta Whop (verificar payout AR — 10 minutos).
- Hablar con contador: Factura E / monotributo exportación de servicios.
- Elegir 3 nichos de datos con demanda comprobable (buscar: qué buscan los agentes/empresas y nadie scrapea; verticales AR/LATAM).

**Fase 1 — Primer dólar (mes 1-2):**
- 10-15 actores Apify PPE en los nichos elegidos, con READMEs orientados a agentes (MCP-friendly).
- Scanner de campañas de clipping + clipear con criterio (cash-flow + validación del circuito de cobro).
- **Gate al día 60:** ≥1 actor con usuarios pagos y ≥USD 50 cobrados en total por cualquier vía. Si no: revisar nichos, no insistir en los mismos.

**Fase 2 — Compuesto (mes 2-4):**
- 15-25 micro-herramientas sobre los mismos datos (Cloudflare, gratis) + solicitar Journey al llegar a 1.000 sesiones/mes.
- Exponer los actores como MCP servers; bot de Telegram si algún dato tiene público local.
- **Gate al día 120:** el portfolio combinado ≥ USD 150-300/mes. Duplicar solo en lo que traccionó; matar el resto (Tiny Acquisitions existe para liquidar).

**Fase 3 — Activo grande (mes 4-5+):**
- Sobre el nicho ganador: micro-SaaS de alertas B2B (hard paywall + trial 2-4 semanas, Paddle).
- Newsletter de retención sobre la audiencia que ya llega a las herramientas.
- Decisión YouTube editorial: solo si sobran horas y siempre antes del 1/2/2027.

### Expectativas honestas

- **Mes 6:** USD 150-800/mes combinado si la ejecución es buena. La mediana de quien intenta esto es bastante menos — el plan apunta al cuartil alto vía nicho + ventaja técnica + portfolio.
- **Mes 12:** USD 500-2.500/mes combinado en el escenario bueno, más activos vendibles (un SaaS a $2k MRR vale USD 40-75k en Acquire).
- **Régimen:** 5-10 h/semana de guardia total con el stack andando. Nunca cero.

---

## Preguntas abiertas (afinan el plan cuando las respondas)

1. Presupuesto real disponible (asumimos < USD 1.000).
2. Horas/semana disponibles durante la construcción y en régimen.
3. Qué proyectos ya tenés en marcha (por superposición y sinergias).
4. ¿Tenés ya Payoneer / cuenta en exchange / AdSense / audiencia en alguna red?
5. Tolerancia a mantener múltiples frentes vs preferencia por un solo proyecto.

## Verificaciones pendientes de 1 día (antes de la Fase 1)

- [ ] Whop: método de payout concreto para Argentina (crear cuenta y mirar).
- [ ] Paddle: completar onboarding como seller AR (revisan el producto).
- [ ] Apify: confirmar términos de payout SWIFT + requisitos KYC para pagos agénticos.
- [ ] Contador: Factura E, monotributo, tratamiento de cobros en cripto (Stars/Whop).
- [ ] Journey by Mediavine: requisitos vigentes de aplicación para sitios nuevos.

*Estudio realizado el 2026-09-02. Las políticas de plataformas citadas cambiaron cada pocos meses durante 2025-2026: re-verificar cada dato en el onboarding de la plataforma el día que se invierta en ella. Fuentes completas con URLs en `research/fuentes/*.md`. Nada de esto es consejo financiero.*
