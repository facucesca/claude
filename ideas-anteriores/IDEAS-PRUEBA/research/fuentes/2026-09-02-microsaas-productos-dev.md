# Informe fuente: Micro-SaaS y productos de desarrollador (2026-09-02)

> Informe crudo del agente de investigación #3. Se sintetiza en `research/2026-09-02-estudio-mercado-ingresos-pasivos-ia.md`.
> Marcas: **[PRIMARIA]** = reporte oficial/dashboard verificado; **[ANECDÓTICO]** = blog/self-report.

---

## 0. Los datos duros primero (base para todo lo demás)

### RevenueCat — State of Subscription Apps 2026 [PRIMARIA] (marzo 2026, 115.000+ apps, $16B en transacciones)
- **Mediana de ingresos de una app al año de lanzada: ~USD 72/mes.** Top cuartil: ≥ $429/mes. Top 10%: ≥ $2.574/mes (36x la mediana).
- **17,3% de las apps llega a $1.000/mes en 2 años; solo 4,6% llega a $10.000/mes.**
- LTV realizado año 1 por pagador (mediana global): **$23**.
- Churn brutal: 35% de las suscripciones anuales cancela en el primer mes; ~72% no llega al año.
- Trials largos (17-32 días) convierten 42,5% vs 25,5% los cortos; hard paywall convierte a pago 10,7% (D35) vs 2,1% freemium.
- **Apps de IA: +41% de LTV año 1, pero retención a 12 meses 36% peor.** La IA cobra más caro y retiene peor.
- Concentración: apps lanzadas antes de 2020 capturan el 69% del revenue; las lanzadas en 2025+ apenas el 3%.

### ChartMogul — SaaS Growth Report 2025 / Retention Report [PRIMARIA] (web SaaS)
- SaaS < $1M ARR: **churn bruto de MRR mediano 9,1%/mes** (neto 6,2%). Sobre $1M ARR baja a 5,3%/2,3%.
- ~La mitad llega a $1M ARR en 10 años, típicamente en 2-5 años; solo 3,3% en menos de 12 meses (sesgo de selección: ya usan ChartMogul).
- Reporte de retención 2025-26: "The AI churn wave" — el churn de productos IA es la tendencia dominante.

### MicroConf / agregadores indie [ANECDÓTICO]
- Mediana de micro-SaaS estudiados: ~$500/mes MRR; mediana de los *rentables*: ~$4.200 MRR (metodología opaca — baja confianza).
- MicroConf 2025: 28% de 230 founders reportó >$100k MRR — survivorship bias puro; no usar como expectativa.

**Lectura honesta:** el resultado mediano de lanzar algo es ~$70-500/mes. El plan tiene que asumir eso y diseñar para el top cuartil vía nicho + distribución, o vía portfolio de varios intentos.

Fuentes: RevenueCat State of Subscription Apps 2026 (revenuecat.com/state-of-subscription-apps, mar 2026) · Benchmarks (revenuecat.com/blog/growth/subscription-app-trends-benchmarks-2026, 19-mar-2026) · ChartMogul "Against the Odds 2025" y "SaaS Retention: The AI churn wave" (chartmogul.com/reports/) · MicroConf State of Indie SaaS (microconf.com/state-of-indie-saas) · SaaSRanger [ANECDÓTICO].

---

## 1. Micro-SaaS de nicho "aburrido" (monitores, alertas, compliance, conversores)

**(a) Modelo:** suscripción B2B USD 9-49/mes. Los nichos que sobrevivieron a la muerte del AI-wrapper genérico comparten: dato o workflow propietario, comprador que paga por resultado, problema demasiado chico para una plataforma grande. Consistentes en 2026: monitoreo/alertas (webs, precios, stock, competidores, cron jobs), dunning/recupero de pagos, compliance vertical, integraciones entre nichos, schedulers.

**(b) Números realistas:**
- **Healthchecks.io** (monitoreo de cron jobs, un solo founder): **$14.043 MRR con 652 clientes a los 9 AÑOS** [PRIMARIA — blog del founder, jul 2024]. Techo realista de un monitor de nicho bien ejecutado sin marketing agresivo.
- **Post Bridge** (Jack Friks, scheduler social): $8k MRR (mar 2025) → $43.471 MRR (jun 2026, verificado vía TrustMRR), churn 24%/mes en el camino. Pero el growth vino de una audiencia build-in-public enorme — no pasivo ni replicable sin distribución.
- **Mediana a 6 meses: $0-300 MRR. A 12 meses: $200-1.000 MRR. Top 10% a 12 meses: $2-8k MRR.**

**(c) Automatización real:** los monitores son de lo más pasivo que existe (cron + workers). En régimen: 2-6 h/semana (soporte, scrapers rotos, falsos positivos). Con churn 9%/mes, "pasivo" = "se encoge solo si no hacés nada".

**(d) Capital:** $20-80/mes (VPS/Workers + dominio + email + proxies).

**(e) Primer dólar:** 4-10 semanas con hard paywall + trial (los datos de RevenueCat favorecen hard paywall + trial 2-4 semanas sobre freemium).

**(f) Riesgos:** saturación alta en monitores genéricos (Visualping con $8M levantados, Distill, changedetection.io gratis). Se sobrevive solo en el sub-nicho: "monitor de licitaciones públicas de X industria", "alertas regulatorias de Y", "stock de Z para revendedores". El churn es el asesino silencioso.

**(g) Ángulo 2026:** agentes (Claude Code + browser automation) para scrapers que se auto-reparan cuando cambia el HTML — baja 10x el costo de mantenimiento, que era la barrera clásica. También: "AI visibility monitoring" (¿qué dice ChatGPT/AI Overviews de mi marca?) — categoría emergente real.

**(h) Veredicto: 7/10.** Mejor riesgo/retorno para el perfil. Lento pero componible, margen 70%+, vendible después.

Fuentes: blog.healthchecks.io/2024/07/running-one-man-saas-9-years-in (jul 2024) · Post Bridge en X/TrustMRR (2025-26) · Flowjam/StartuPage [ANECDÓTICO] · CB Insights Visualping.

---

## 2. Extensiones de Chrome

**(a) Modelo:** Chrome Web Store **no tiene pagos nativos** → ExtensionPay (requiere Stripe → problema desde Argentina; alternativa: Paddle/Dodo o licencias por key), o freemium con licencia. Precios: $3-10/mes o one-time $29-79.

**(b) Números:** casos publicados por ExtensionPay reales pero **viejos** (GMass $130k/mes en 2019, GoFullPage $10k/mes en 2021, Night Eye $3,1k/mes...). El "la extensión promedio gana $862k/año" que circula es basura estadística. **Realista 2026: mediana ~$0; nicho con pago funciona en $200-2.000/mes; top 5% $5-40k/mes.** A 6 meses: $0-500/mes; a 12: $300-2k/mes si hay nicho con intención de pago.

**(c) Automatización:** altísima — sin servidor o mínimo. 1-4 h/semana. De lo más pasivo del informe.

**(d) Capital:** $5 (registro developer CWS) + dominio.

**(e) Primer dólar:** 2-6 semanas — el ciclo más corto (CWS da discovery orgánico por keywords).

**(f) Riesgos:** dependencia total de Google. Purga MV2 completada (extensiones borradas 31-ago-2026); políticas permiten **suspender cuentas developer enteras** con apelaciones opacas (foros chromium-extensions llenos de casos). Saturación media: nichos B2B (e-commerce sellers, recruiters, agencias) aún con demanda pagante.

**(g) Ángulo 2026:** extensiones que inyectan IA en SaaS caros donde el usuario ya trabaja (modelo Closet Tools/GMass). Cross-publicar en Edge/Firefox para diversificar.

**(h) Veredicto: 6/10.** Mejor como *primer producto* (aprender a cobrar rápido y barato) o canal de adquisición, no activo principal.

Fuentes: extensionpay.com/articles/browser-extensions-make-money (2019-2021, datados) · developer.chrome.com/docs/webstore/program-policies/repeat-abuse y /review-process · ChromeUnboxed purga MV2 (ago 2026) · hilos chromium-extensions [ANECDÓTICO].

---

## 3. Bots de Telegram / Discord con suscripción

**(a) Telegram:** Stars para bienes digitales y **suscripciones recurrentes nativas de bots**. Payout: **Stars → TON vía Fragment → exchange cripto → pesos/USD. ~$0,013 por Star** (desktop/web; compras iOS/Android pierden 30% → ~$0,009). Telegram casi no cobra comisión; umbral de retiro ~1.000 Stars. Período de retención no confirmado (~21 días históricos — **verificar en doc oficial**).

**(b) Números:** bots utilitarios con Stars: **$100-2.000/mes** [ANECDÓTICO — no hay casos con dashboards verificados, lo cual es en sí una señal]. A 6 meses: $0-200/mes mediana; top 10%: $1-3k/mes.

**(c) Automatización:** muy alta (webhook + cron; billing lo maneja Telegram). 1-4 h/semana. Descubrimiento débil → el growth no es pasivo.

**(d) Capital:** $5-20/mes de servidor.

**(e) Primer dólar:** 2-5 semanas.

**(f) Cobro desde Argentina — acá brilla:** Stars→TON→cripto **no requiere Stripe, ni LLC, ni Payoneer**; Argentina tiene rieles cripto-a-pesos triviales. Único modelo sin fricción extra por ser argentino. Riesgos: volatilidad de TON entre cobro y venta; impuestos cripto (contador).

**Discord — peor:** monetización nativa (Premium Apps, 15% comisión) limitada a **EE.UU., UE y UK** → desde Argentina requiere LLC o cobro externo.

**(g) Ángulo 2026:** bots de alertas hiperlocales (stock/precios Argentina/LatAm, dólar, tarifas) cobrados en Stars; mini-apps de Telegram con la misma infra de pago.

**(h) Veredicto: Telegram 6,5/10** (techo bajo, fricción de cobro mínima desde AR, primer dólar rapidísimo); **Discord 4/10**.

Fuentes: telestars.io/blog/telegram-stars (may 2026) · scrile.com/blog/telegram-monetization · support-dev.discord.com (elegibilidad US/EU/UK) · discord.com/blog (comisión 15%) · dodopayments.com/blogs/monetize-discord-bot.

---

## 4. Cobro desde Argentina (transversal — decide todo)

De menor a mayor fricción:

1. **Merchant of Record que acepte sellers argentinos:**
   - **Paddle**: paga por **Payoneer o wire** (Payoneer opera normal en AR). Ruta MoR más probada. Contras: onboarding exigente, fees ~5%+.
   - **Lemon Squeezy: en transición.** Stripe la compró (jul 2024), migrando a **Stripe Managed Payments** (preview feb 2026, 5% + $0,50). **Riesgo: si el onboarding queda atado a países Stripe, Argentina queda afuera.** No construir sobre esto sin verificar.
   - **Dodo Payments / Creem / Polar**: camada post-LS. Dodo se promociona como MoR global para devs sin Stripe; Argentina aparece en sus listas pero **no queda claro si como seller o comprador → verificar con soporte**. Polar usa Stripe Connect → probablemente no sirva desde AR.
2. **LLC en EE.UU. + Mercury + Stripe** (ruta "en serio", común entre devs argentinos): Atlas ~$500 o Wyoming ~$150-250; recurrentes ~$60 (WY) + agente ~$50-125/año + contador filing 5472/1120 (~$300-500/año). Con capital <$1.000 se come la mitad → **hacerlo recién con revenue (~$1k MRR), no antes**.
3. **Cripto (Telegram Stars→TON)**: cero fricción de entrada.
4. **dLocal no es para esto** (payins LatAm para merchants globales).

**Recomendación práctica:** empezar con Paddle (o Dodo si valida onboarding) → migrar a LLC+Stripe pasado ~$1k MRR.

Fuentes: paddle.com/help (wire/Payoneer) · lemonsqueezy.com/blog/2026-update (feb 2026) · TechCrunch adquisición LS (jul 2024) · docs.dodopayments.com (lista países, ambigua) · wise.com Payoneer Argentina.

---

## 5. Distribución: el verdadero cuello de botella

| Canal | Evidencia | Pasividad real |
|---|---|---|
| **Shopify App Store** | Mediana de app listada: **<$1.000/mes**; top 25% de devs ~$167k/año; **0% fee primer $1M/año**; ecosistema $1.3B+ pagado a devs | La mejor distribución compuesta: merchants buscan con tarjeta en mano. Contra: soporte demandante |
| **Chrome Web Store** | Discovery orgánico decente; sin pagos nativos | Alta pasividad, alto riesgo plataforma |
| **Zapier App Directory** | 8.000+ apps, 3M+ usuarios navegando, listing gratis | Canal secundario de intención alta |
| **SEO de herramienta gratuita + upsell** | AI Overviews recorta ~70% CTR en queries afectadas (Seer); crackdown a pSEO escalado (core update mar 2026: sitios de bajo valor -50/80% tráfico). Funciona solo si la página ES la herramienta | Media y decreciente. El juego nuevo: aparecer en respuestas de LLMs (AEO/GEO) |
| **AppSumo** | Revenue **cayó ~50% en 2 años** (Noah Kagan vía ppc.land); se queda ~70% del ticket; ~40% de productos listados muere en 3 años | Solo inyección de caja inicial; envenena modelo recurrente |

**Conclusión:** orden 2026 para growth semi-pasivo: (1) marketplace con billetera integrada (Shopify), (2) tienda con búsqueda propia (CWS, Telegram), (3) SEO utilitario de nicho + Zapier. Los primeros 50 clientes casi nunca llegan pasivamente.

Fuentes: shopify.dev/docs/apps/launch/distribution/revenue-share · weekonelabs.com / uptek.com [semi-ANECDÓTICO] · shopify.com/news/billion-dollar-ecosystem · zapier.com/blog · gracker.ai [ANECDÓTICO] · ppc.land AppSumo.

---

## 6. Venta del activo (la salida que hace rentable el portfolio)

- **Acquire.com, reporte bianual (feb 2026, datos 2025)** [PRIMARIA]: mediana de ventas confirmadas **3,9x profit (SDE)**; tiempo promedio en mercado **81 días**; márgenes medianos 71%.
- Micro-SaaS chico ($1-5k MRR): **2-3x SDE** [ANECDÓTICO, consistente].
- **Tiny Acquisitions**: proyectos **<$5.000** (liquidar experimentos fallidos o pre-revenue). Microns/BuyMicroStartups: mayoría <$25k.
- **Matemática:** monitor de nicho a $2.000 MRR con 80% margen ≈ $19k SDE/año → venta plausible **$40-75k**. Construir-crecer-vender 2-3 veces es más realista que "llegar a $50k MRR".

Fuentes: blog.acquire.com/acquire-com-biannual-acquisition-multiples-report-jan-2026 (feb 2026) · blog.acquire.com/saas-valuation-multiples · Product Hunt Tiny Acquisitions · movemrr.com [ANECDÓTICO].

---

## 7. Ángulos emergentes 2026

1. **Monetizar MCP servers / tools para agentes:** 20.000+ MCP servers, "menos del 5% cobra" [ANECDÓTICO]. Infra de cobro recién madura: Apify (afirma pagar **$1,2M/mes a developers**, 80% share [dato del vendor]), MCPize, x402, Stripe machine payments. **Ventana de timing real, revenue no probado a escala indie.** Play concreto: MCP server de datos de nicho (regulatorio/precios LatAm) cobrado por llamada.
2. **"Picos y palas" para agentes:** los agentes que navegan y compran necesitan monitoreo, gateways, auth, datos estructurados. Un scraper de nicho expuesto como API/MCP = micro-SaaS con comprador nuevo.
3. **Auto-mantenimiento como moat:** operar 3-5 productos con Claude Code (scrapers auto-reparables, soporte semi-automatizado) invierte la economía del portfolio indie (modelo Marc Lou: $1,03M en 2025 con ~12 productos [self-report público]). Mantener es barato con agentes — **conseguir usuarios sigue sin serlo**.
4. **Evitar:** GPT Store (monetización nunca llegó), AI wrappers genéricos (churn 30% peor, clonables), dependencia de una sola API de terceros sin datos propios.

Fuentes: dev.to monetize MCP 2026 [ANECDÓTICO] · nevermined.ai · mcpize.com [vendor] · Marc Lou en X (oct 2025) · Indie Hackers.

---

## Veredicto final comparado

| Opción | Nota | Por qué |
|---|---|---|
| Micro-SaaS monitor/alertas B2B de nicho (web) | **7/10** | Mejor riesgo/retorno; margen 71%+; vendible a 3-4x SDE; 12-24 meses hasta ser semi-pasivo real |
| App de Shopify (nicho e-commerce) | **6,5/10** | Distribución pasiva más real (0% fee primer $1M), pero soporte demandante |
| Bot de Telegram con Stars | **6,5/10** | Único sin fricción de cobro desde AR; primer dólar en semanas; techo bajo ($1-3k/mes top) |
| Extensión Chrome paga | **6/10** | Capital ~$0, ciclo cortísimo; riesgo unilateral de Google; ideal producto #1 |
| MCP/tools para agentes | **5/10** | Timing excelente, evidencia de revenue casi nula; una apuesta del portfolio, no todo |
| Bot de Discord | **4/10** | Monetización nativa vedada para Argentina |
| AI wrapper genérico / GPT Store | **2/10** | Churn peor, clonable, monetización rota |

**Verdad incómoda:** la mediana de todo esto es ~$72-500/mes al año. Plan racional para 3-5 meses y <$1.000: (1) lanzar 2-3 apuestas baratas (extensión + bot Telegram + monitor B2B), (2) cobrar vía Paddle/Payoneer o Stars desde el día uno, (3) matar rápido lo que no traccione, (4) duplicar en lo que llegue a ~$500 MRR y recién ahí LLC+Stripe, con venta a 3-4x SDE como plan B. "Semi-pasivo" es el estado final de un activo que funcionó, no una propiedad del mes 1.

**Pendientes de verificación:** Dodo/Stripe Managed Payments aceptan sellers argentinos (mail a soporte); retención exacta de Telegram Stars (~21 días); revenue auditado de bots Telegram (no existe); números 2025-26 de extensiones citadas por ExtensionPay (casos de 2019-2021).
