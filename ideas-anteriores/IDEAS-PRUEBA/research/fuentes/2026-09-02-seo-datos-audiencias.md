# Informe fuente: SEO programático, datos y audiencias (2026-09-02)

> Informe crudo del agente de investigación #5.

**Ranking del agente:** Apify Store (8/10) > micro-herramientas (6,5/10) > job board de nicho (6/10) > directorios (5/10) > newsletter automatizada (4/10) ≈ Telegram pago (4/10) > GEO/AEO pasivo (3/10) > sitio de contenido + afiliados desde cero (2/10).

---

## 1. SEO/afiliados post-AI Overviews: datos duros — 2/10 como modelo principal

- **Pew Research (22-jul-2025, 900 usuarios):** con AI Overview, el click a resultados cae de 15% a 8%; links dentro del AIO reciben click 1% de las veces; 26% de sesiones terminan sin click (vs 16%).
- **Ahrefs (abr-2025, 300k keywords):** -34,5% CTR en posición 1 con AIO.
- **Seer (2025, 3.119 queries):** CTR orgánico -61% (1,76% → 0,61%).
- **Amsive (2025, 700k keywords):** -15,5% promedio; -19,98% no-brand; -37% con AIO + featured snippet. Keywords de marca con AIO: +18,7%.
- **Core update marzo 2026:** afiliados la categoría más golpeada (~71% de monitoreados cayendo; -20/35% promedio, >50% en money pages); publishers chicos ~-60%. Sobrevivió: experiencia de primera mano, autoría real, testing propio. Murió: contenido IA escalado sin edición (-60/80%).

**Qué sobrevive:** (a) herramientas interactivas y calculadoras (no se pueden "resumir"); (b) datos únicos que los LLMs citan; (c) marcas; (d) experiencia demostrable. **Sitio de contenido + afiliados desde cero hoy: funcionalmente muerto para este perfil.**

Fuentes: pewresearch.org 22-jul-2025 · searchengineland.com (Ahrefs) · amsive.com · affiversemedia.com / getasa2.com (core update mar-2026, secundarias).

## 2. Portfolio de micro-herramientas gratuitas — 6,5/10

- **Tesis mejor documentada de 2026:** Ahrefs publicó el 16-jul-2026 "The Free Tools SEO Strategy": su /writing-tools/ ~1M visitas orgánicas US/mes; Omni Calculator ~2,3M; FreeConvert 380k→1,5M/mes en 5 años; Coolors ~590k. Lógica: un AIO explica la fórmula pero no ejecuta el cálculo. Advertencia: Ahrefs tiene conflicto (le funciona a su embudo); keywords genéricas en inglés brutalmente saturadas. La oportunidad: **long-tail de nichos** (calculadoras regulatorias, industria específica, español) y herramientas citables por LLMs.
- **Números:** AdSense RPM ~USD 2-5; **Journey by Mediavine acepta desde 1.000 sesiones/mes (desde 15-ene-2026), revenue share 70%**; caso real: RPM 7,50→15,99 en 3 meses, USD 717 con ~56k sesiones en 90 días (blog de viajes, 27% US). Raptive ~100k pageviews. Con 30 herramientas de nicho a 6 meses: 5k-30k visitas/mes = USD 20-200/mes. A 12 meses: mediana USD 100-500/mes; top 10%: USD 1.500-5.000/mes. Referencia techo: TinyWow ~2M visitas/mes ≈ USD 150/día ads + pro $5,99/mes [estimaciones de terceros, baja confianza].
- Automatización: construir 20-50 tools con Claude Code totalmente viable (estático + JS, hosting ~0 en Cloudflare). Régimen: 2-5 h/semana. Primer pago AdSense: típico 4-8 meses (rankeo dominio nuevo + umbral $100).
- Riesgos: dependencia total de Google; la misma accesibilidad que te habilita te comoditiza; AI Mode ya ejecuta cálculos simples inline (riesgo 2-3 años para tools triviales).
- **Ángulos:** herramientas en español (gap enorme: sueldo neto AR, monotributo, plazo fijo vs dólar — RPM local bajo pero competencia ~nula); diseñar para citación por LLMs (datos + tool en la misma página, llms.txt); **reutilizar cada herramienta como actor de Apify/servidor MCP (un codebase, dos canales)**; tier pro vía Paddle/LS.

Fuentes: ahrefs.com/blog/the-free-tools-seo-strategy (16-jul-2026) · journeymv.zendesk.com (requisitos oficiales) · danny-cph.com (RPMs reales) · siteworthtraffic.com (TinyWow, baja confianza).

## 3. Apify Store — monetización de scrapers/actores — 8/10 (LA prioridad)

- **Modelo:** publicás "actores" (scrapers/automatizaciones); usuarios y agentes IA pagan por uso. Pricing dominante: **pay-per-event (PPE)**. Fórmula oficial: **ganancia = 80% del revenue − costos de plataforma que consume tu actor**. Payout mensual día 11; PayPal (mín USD 20) o SWIFT desde Chequia (mín USD 100, fees 10-50). **Apify discontinúa el pricing "standard" en octubre 2026** — todo migra a PPE → reordena el store y abre ventana para entrar con PPE bien diseñado.
- **Números:** oficial (X de Apify): **USD 1M pagado a creadores en un solo mes**, 5x vs USD 222k un año antes. Secundaria: USD 1,4M/mes entre ~3.000 devs = promedio ~USD 470/dev/mes (mediana seguramente menor, cola larga). Marketing oficial: top creators >USD 10k MRR; "muchos" >USD 1k/mes. **Caso detallado (blog oficial 2026): Olivier Reynaud, 98 actores en 6 meses**, 2.500 usuarios, 855 activos mensuales; PPE superó al standard 3-12,7x; lo que pagó fueron **nichos sin competencia** (Welcome to the Jungle, Skool, ZipRecruiter, verticales regionales), no LinkedIn/Amazon.
- **Estimación honesta:** 6 meses con 15-30 actores de nicho: mediana USD 100-500/mes; top 10% USD 1.500-4.000/mes. 12 meses: mediana USD 300-1.000/mes; top 10% USD 5.000-10.000+/mes.
- **Carga real:** Reynaud reporta 15-20 h/semana con 98 actores (5-7 mantenimiento, 3-4 soporte, 2-3 monitoreo). Con 15-25 actores: **4-8 h/semana**. Los sitios cambian el HTML: "semi-pasivo con guardia técnica". Una review de 1 estrella cuesta semanas de uso.
- **Capital:** ~USD 0-50/mes. **Primer dólar: 2-6 semanas** — el más rápido del informe.
- **Riesgos:** saturación creciente (20.000+ actores; el $1M Challenge cerró 31-ene-2026 y atrajo ola de creadores); dependencia de plataforma privada; riesgo legal/ToS del scraping recae en vos; mantenimiento perpetuo.
- **Ángulos fuertes:** (1) **pagos agénticos: x402 (USDC en Base) y Skyfire habilitados** — agentes descubren, ejecutan y pagan actores sin cuenta Apify; diseñar actores para consumo por agentes (MCP-friendly) es la frontera con menos competencia; (2) **fuentes LATAM/hispanas casi vírgenes** (Mercado Libre por vertical, inmobiliarias/empleo AR, boletines oficiales, datos BCRA); (3) migración PPE oct-2026 deja actores viejos mal precificados; (4) **RapidAPI descartado**: adquirida por Nokia (nov-2024), marketplace desmantelado.

Fuentes: docs.apify.com/actors/publishing/monetize · help.apify.com (payouts, 80/20) · blog.apify.com/building-98-actors-on-apify-store (caso con horas) · X de Apify ($1M/mes) · blog.apify.com/introducing-x402-agentic-payments · docs.apify.com/legal/challenge-terms · techcrunch.com 13-nov-2024 (RapidAPI/Nokia).

## 4. Job boards y directorios de nicho — 6/10 y 5/10

Casos (self-reported con nombres): Real Work From Anywhere USD 16.439 acumulado a mitad de 2025 (>USD 5k/mes últimos meses); JobBoardSearch (Rodrigo Rocco, argentino) >USD 3k/mes; MoAIJobs USD 2.300+/mes a $199/post ~99% margen; Work With Indies ~USD 5k MRR; **Jobleads (venta del feed de datos a recruiters) USD 8k MRR**. Directorios: John Rush ~30 en un año, monetizó ~un tercio, vendió AllGPTs.co por 5 cifras — y el playbook público generó miles de copias. **Mediana honesta: ~USD 0** (la gran mayoría del boom 2024-25 factura nada). A 12 meses bien ejecutado: USD 500-3k/mes. Lo que monetiza NO es automatizable: curación con criterio, ventas de listings (outreach). 5-10 h/semana. Cobro: listings con Stripe → desde AR requiere MoR o LLC. Ángulo: ser el dataset de referencia citado por LLMs; **vender el feed vía API/Apify además del sitio** (doble monetización); nichos AR/LATAM remote-first.

Fuentes: indiehackers.com (job board $5k MRR) · gaps.com/job-boards (15 casos) · founderoo.co (playbook Rush).

## 5. Newsletters automatizadas (beehiiv) — 4/10 standalone; 7/10 como capa

Datos primarios (beehiiv State of Newsletters 2026, 5-ene-2026): Boosts CPA USD 1-15/suscriptor referido, promedio real ~USD 1,63, beehiiv retiene 20%. Ad Network: CPMs USD 10-30, entrada ~1.500 subs activos. Suscripciones pagas: precio mediano USD 10/mes; **conversión mediana a pago 0,62%**; mediana de tiempo al primer dólar: 66 días; USD 19M pagados en 2025 (+138%). Mediana global: la mayoría no supera cientos de subs y USD 0. A 12 meses bien ejecutada: 2-8k subs, USD 100-500/mes; top 10%: USD 2-5k/mes. **Producción automatizable (1-3 h/semana con revisión humana — una alucinación mata la confianza); el crecimiento NO.** Fatiga de contenido IA: preferencia cayó de 60% (2023) a 26%. Monetización corre por **Stripe** (AR no soportada como merchant; Stripe agregó AR como destino de cross-border payouts feb/mar-2026 pero beehiiv sin confirmar) → plan B: LLC. **Uso correcto: canal de retención para tus herramientas/actores, no negocio standalone.**

Fuentes: beehiiv.com/blog/the-state-of-newsletters-2026 (5-ene-2026) · state-of-paid-newsletters-2026 · beehiiv support (Boosts) · pressgazette.co.uk.

## 6. Telegram pago (Stars) — 4/10 standalone; 6/10 sobre datos propios

1 Star ≈ USD 0,013 al retirar (Fragment→TON, mín 1.000 Stars); compras vía app stores pierden ~30%. Ejemplo documentado: canal 4.800 subs a 200 Stars → USD 108-162/mes [secundario]. Caso grande utilitario: **AirTrackBot (alertas de vuelos): 2M usuarios, ~USD 8.000/mes** [anecdótico] — monetiza como bot freemium, no canal de contenido. Mediana desde cero sin audiencia: USD 0-50/mes a 6 meses. Bot de alertas 95% automatizable; el problema es distribuir (Telegram no tiene discovery). Desde AR el cash-out cripto es fácil; alternativa mejor para público local: **cobrar por Mercado Pago** y usar el canal como delivery. Ángulo: bots utilitarios con datos que ya scrapeás (sinergia Apify/tools) para mercado argentino (precios, dólar, tarifas, vuelos).

Fuentes: tribute.top · startupspells.com (AirTrackBot) · floqal.com (mecánica Stars).

## 7. GEO/AEO — 3/10 como negocio pasivo hoy

Demanda explosiva pero como **servicio** (búsquedas "GEO agency" +2.300% YoY; retainers premium). SaaS de monitoreo de citaciones ya con VC (Profound, Peec). No existe modelo semi-pasivo probado. **Forma correcta de jugarlo: ser el citado** — publicar datasets únicos, benchmarks, estadísticas y herramientas (los LLMs sobre-citan fuentes de referencia); optimizar cada tool/dataset para citación (datos con fecha, estructura, llms.txt). Tráfico IA chico pero convierte muy bien (claim vendor: 23x).

## 8. Cobro desde Argentina (transversal)

**El cepo se levantó el 14-abr-2025** para personas humanas → cobrar del exterior se simplificó muchísimo. Hace falta **Factura E** (exportación de servicios, exenta de IVA; monotributo aplica). Verificar límites vigentes con contador.

| Canal | Método | Viabilidad AR |
|---|---|---|
| AdSense | Wire USD a banco local | Alta; umbral $100; proceso documentado |
| Journey/Mediavine | Wire internacional | Alta (net-65) |
| Apify | SWIFT desde Chequia (mín $100) o PayPal | Alta vía SWIFT + Factura E |
| beehiiv | Stripe/Stripe Express | Baja-media (sin confirmación; plan B LLC) |
| Tier pro / listings | Paddle, Lemon Squeezy (MoR); Mercado Pago para público local | Alta; estándar entre indies argentinos |
| Telegram Stars | Fragment → TON | Alta operativamente; contabilidad gris |

Fuentes: infobae dic-2025 / argentina.gob.ar abr-2025 (cepo) · migueleonardortiz.com.ar (AdSense AR) · docs.stripe.com/changelog (payouts AR) · docs.apify.com (payouts).

---

## Recomendación del agente

1. **Núcleo: Apify (8/10).** Primer dólar en semanas, capital ~0, cobro viable, único canal con viento de cola estructural (x402/MCP + migración PPE oct-2026). Nichos que nadie cubrió (hispanos/LATAM), no LinkedIn/Amazon. 5-10 h/semana reales.
2. **Satélite: micro-herramientas (6,5/10)** reutilizando el mismo código como páginas SEO + actores + MCP servers. Journey desde 1.000 sesiones/mes. Horizonte 6-12 meses.
3. **Capa de distribución:** newsletter + bot de Telegram alimentados por los mismos datos — activos anti-dependencia-de-Google, no negocios standalone.
4. **Evitar:** sitio de contenido + afiliados desde cero, RapidAPI, cursos de gurús de directorios.

Los únicos datos duros del espacio son los estudios de CTR (Pew/Ahrefs/Amsive/Seer) — y todos apuntan igual: **lo que se lee muere, lo que se usa (herramientas, datos, APIs) sobrevive.**
