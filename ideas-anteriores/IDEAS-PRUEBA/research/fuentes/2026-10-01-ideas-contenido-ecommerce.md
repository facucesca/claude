# Ideas de ingresos: contenido, medios, marketing y e-commerce con IA

**Fecha:** 2026-10-01
**Frente:** contenido / medios / marketing / e-commerce con IA
**Perfil considerado:** argentino, cobra por Payoneer / Mercado Pago / merchant of record; **no programa** (usa Claude como asistente, no como herramienta de desarrollo); tiene **Higgsfield** conectado (imagen/video/audio IA, Shorts Studio, clipper, publicación a TikTok); presupuesto < USD 500-1.000; acepta pasivos, semi-pasivos y activos.

> Nota de coherencia con el repo: `MEMORY.md` describe al usuario como "técnico, construye software asistido por IA". Este informe asume lo que pidió el encargo de hoy (2026-10-01): **no sabe programar**. Si eso cambia, varias ideas (GEO como producto, monitoreo de visibilidad, scanner) suben de score.

---

## Metodología

- **Búsquedas:** 32 búsquedas web + 4 lecturas completas de páginas (WebFetch), hechas el 2026-10-01. El presupuesto de búsquedas de la sesión se agotó en la búsqueda 33; algunas ideas (marcadas con **[sin fuente propia]**) se evalúan con datos de ideas vecinas y razonamiento, no con una fuente específica. Tratarlas como hipótesis.
- **Prioridad temporal:** fuentes 2025-2026. Fechas siempre absolutas.
- **Escepticismo:** gran parte de la literatura de "precios de servicios IA" la publican **vendedores de herramientas o de cursos** (Creatify, ClipSpeed, Vantaige, AI Video Bootcamp, Segwise, Billo, Cinerads, GoFaceless, OutlierKit, VoxBooster, agencias de GEO). Se marcan con **⚠ conflicto de interés**. Sus rangos de precio sirven como techo, no como mediana.
- **Score 1-10:** realista para ESTE usuario (no programa, bajo capital, Higgsfield, cobra desde AR). Pondera los 7 criterios del `CLAUDE.md`; para servicios activos el criterio "automatización" se mide como potencial de productizarse, no como castigo.
- **No se repite** lo ya descartado (TikTok Rewards, afiliados SEO desde cero, música IA streaming, KDP low-content, POD, prompts genéricos, Shorts AdSense, stock IA) salvo evidencia nueva fuerte — y **hay una**: el programa de afiliados de Mercado Libre en Argentina + YouTube Shopping AR (ver idea 24).

---

## Contexto de mercado y políticas (lo que cambia el tablero en 2025-2026)

### Políticas de plataforma sobre contenido IA
| Plataforma | Regla vigente | Fuente |
|---|---|---|
| **YouTube** | Desde **2025-07-15** el YPP desmonetiza contenido "inauténtico" (antes "repetitivo"): masivo, repetitivo, plantillas con poca intervención humana. La IA como herramienta sigue permitida. Señales de alto riesgo: voz TTS sobre stock footage, clonación de voz sin disclosure, 10+ videos casi idénticos por día. Revisión humana tras flag algorítmico, con advertencia previa. | [PlagiarismToday 2025-07-08](https://www.plagiarismtoday.com/2025/07/08/youtube-targets-inauthentic-content/), [AlternativeTo 2025-07](https://alternativeto.net/news/2025/7/youtube-updates-its-policy-to-demonetize-inauthentic-mass-produced-ai-generated-content), [GoFaceless ⚠](https://www.gofaceless.ai/blog/youtube-ai-slop-policies-faceless-monetization). Ojo: [TubeToMP4](https://tubetomp4.it.com/blog/youtube-ai-content-crackdown-2026/) dice "2026-07-15" — error de fecha; la fecha correcta es 2025-07-15. |
| **Meta (FB/IG)** | Permite creatividades IA. Etiqueta "AI info" cuando hay humano fotorrealista IA, persona real diciendo algo que no dijo, o escena fotorrealista presentada como real. Detección de metadatos C2PA ampliada a herramientas de terceros desde **2026-06**; la etiqueta auto-aplicada no se puede quitar. No penaliza distribución por sí misma. | [Cinerads ⚠](https://www.cinerads.com/blog/ai-ugc-facebook-ad-policy), [Common Thread Co.](https://commonthreadco.com/blogs/coachs-corner/meta-ai-ad-labels-mandatory-disclosure-ecommerce-2026) |
| **TikTok** | Etiqueta obligatoria para IA que representa personas/escenas realistas; auto-etiquetado por C2PA + clasificador; deepfakes de personas reales sin etiqueta prohibidos; medios sintéticos de **personas privadas reales** prohibidos aun con etiqueta. | [Cinerads ⚠](https://www.cinerads.com/blog/tiktok-ai-content-policy), [Billo ⚠](https://billo.app/blog/ai-labeling/), [Retail TouchPoints](https://www.retailtouchpoints.com/topics/digital-commerce/tiktok-implements-new-standards-for-ai-generated-content) |
| **Legal** | FTC (EE.UU.): prohibidos testimonios de personas inexistentes (16 CFR 255.1). Ley de "synthetic performers" de Nueva York vigente desde **2026-06-09**; obligaciones de transparencia del **EU AI Act** desde **2026-08-02**. | [Digital Applied 2026-09-17](https://www.digitalapplied.com/blog/ai-avatar-ads-vs-real-ugc-creators-cost-trust-2026), [CreatorFlow](https://creatorflow.so/blog/how-ai-influencers-make-money/) |
| **Google Search** | Core + spam update de **marzo 2026** con enforcement duro de "scaled content abuse": granjas de contenido IA -60/80% de tráfico; 71% de sitios de afiliados con caídas. | [ThePublive](https://www.thepublive.com/blog/google/google-fired-twice-in-24-hours-what-the-march-2026-spam-core-update-means-for-seo-aeo-and-llmo-11264463-11435131), [SEOQuick](https://seoquick.com.ua/en/ai-content-google-penalty-2026/) |

**Conclusión operativa:** la IA como *herramienta de producción para un cliente que firma* (marca, creador, PyME) está permitida en todas las plataformas con etiqueta. La IA como *fábrica de contenido propio masivo para monetizar por vistas* es exactamente lo que las plataformas están castigando. Esto inclina el frente hacia **servicios B2B** y **afiliación con contenido curado**, no hacia granjas.

### Demanda y precios (datos duros)
- **Upwork:** la edición de video con IA creció **329%** en 2026 y fue la habilidad freelance de mayor crecimiento; "AI video creator" entre las búsquedas top de julio 2026; tarifas USD 30-80/h o USD 150-500 por video. Fiverr: +66% demanda de creadores de video "AI-fluent" (Business Trends Index Q4 2025). — [Upwork Monthly Hiring Insights jul-2026](https://www.upwork.com/research/upwork-monthly-hiring-insights-july-2026), [goLance](https://golance.com/blogs/top-freelance-jobs-2026)
- **Meta Andromeda:** el algoritmo de anuncios rankea por *creatividad*, no por audiencia. Marcas que testean 20+ anuncios nuevos/mes ven +65% ROAS vs <10; recomiendan 8-12 conceptos distintos por campaña y refresco cada 2-3 semanas. Más de 1 millón de anunciantes usaron las herramientas IA de Meta para 15 M de anuncios en un mes. — [Segwise ⚠](https://segwise.ai/blog/meta-andromeda-update-creative-strategy-2026), [Billo ⚠](https://billo.app/blog/meta-andromeda-update/), [Balistro 2026-06-13](https://www.balistro.com/blog/creative-volume-is-the-new-targeting). *Esto genera demanda estructural de volumen de creatividades: el driver más sólido de todo el frente.*
- **Costo de producción IA vs humano:** un video con avatar IA cuesta USD 0,39-3,90 en herramientas; un creador UGC humano cobra mediana ~USD 150-154/video (Collabstr 2025, inBeat). — [Digital Applied 2026-09-17](https://www.digitalapplied.com/blog/ai-avatar-ads-vs-real-ugc-creators-cost-trust-2026)
- **Desempeño:** estudio de Taboola: CTR IA 0,76% vs humano 0,65%. Pero en verticales emocionales (skincare, testimonios) el humano convierte mejor; Klaviyo 2026: 32% de consumidores confía menos en marcas con IA genérica; Ipsos ago-2025: 2/3 prefieren humanos. — [IT Brief](https://itbrief.co.uk/story/study-finds-ai-ads-rival-humans-when-visuals-build-trust), [inBeat](https://inbeat.agency/blog/ai-ugc-ads-vs-real-ugc), [Digital Applied](https://www.digitalapplied.com/blog/ai-avatar-ads-vs-real-ugc-creators-cost-trust-2026)
- **E-commerce Argentina:** Tiendanube >65.000 marcas activas en AR; ventas online +42,1% en el midterm 2026; 25% de las tiendas ya usa herramientas IA (Chat Nube, Lumi). — [Mercado 2026](https://mercado.com.ar/ruta-digital/tiendanube-midterm-2026-el-e-commerce-argentino-subio-421-y-sumo-ia), [Descubre 2026-08-03](https://www.descubre.vc/noticia/tiendanube-reporta-aumento-de-42-en-ventas-online-en-argentina-2026-08-03)
- **Newsletters:** CPM mediano de sponsorship USD 32 por mil suscriptores; B2B/finanzas USD 85-115; Beehiiv Ad Network USD 25-40 CPM, paga >USD 1 M/mes en total. — [VoxBooster ⚠](https://voxbooster.com/blog/newsletter-sponsorship-statistics-2026/), [eMarketer](https://www.emarketer.com/content/beehiiv-doubles-ad-sales-team-newsletter-monetization-heats-up)
- **Búsqueda IA:** el tráfico de referencia desde IA es **0,32% del tráfico web total** en 2026 (vs 0,24% en 2025); Google orgánico manda 134x más. Pero convierte mejor (ChatGPT 11,4% vs 5,3% orgánico, según una fuente). — [SE Ranking](https://seranking.com/blog/ai-traffic), [eMarketer](https://www.emarketer.com/content/ai-assistants-strong-referral-traffic-drivers-paths-purchase-industry-kpis-show)
- **Higgsfield (herramienta propia):** planes ~USD 19/mes (270 créditos), USD 47-59 (1.200), USD 99-129 (3.000). Marketing Studio con 1.500+ plantillas (Product Shots, Ads, UGC Videos), acepta foto de producto o URL. **Uso comercial solo en planes pagos.** — [Creatify ⚠ competidor](https://creatify.ai/blog/higgsfield-pricing-(2026)-plans-and-what-you-ll-actually-pay)

---

## Lista de ideas (38)

Formato: **Qué es** · **Ejemplo/señal** · **Cobro y precio** · **Cómo lo ejecuta él** · **Tipo y h/sem en régimen** · **Capital / 1er dólar** · **Desde AR** · **Riesgos** · **Score**

### A. Creatividades publicitarias y producción para marcas

#### 1. Estudio de creatividades IA para e-commerce LATAM (volumen para Meta/TikTok Ads)
- **Qué es:** paquetes mensuales de 15-30 creatividades (video corto de producto + estáticos + variantes de hook) para marcas de Tiendanube / Shopify / Mercado Libre que pautan en Meta. Cliente: marca PyME que ya invierte en ads y se le "queman" las creatividades.
- **Señal:** Andromeda premia volumen y diversidad (20+ ads nuevos/mes = +65% ROAS, [Segwise ⚠](https://segwise.ai/blog/meta-andromeda-update-creative-strategy-2026)); 65.000 marcas en Tiendanube AR con ventas +42% ([Mercado 2026](https://mercado.com.ar/ruta-digital/tiendanube-midterm-2026-el-e-commerce-argentino-subio-421-y-sumo-ia)).
- **Cobro:** retainer mensual. Referencia internacional indie USD 500-1.200 por pack de 10 y USD 1.500-3.000 por 30 ([Vantaige ⚠ vende curso](https://vantaige.io/blog/how-to-make-money-selling-ai-ugc-content-brands-2026)). En AR realista: **USD 250-600/mes por cliente** (pesos vía Mercado Pago, facturando como monotributista).
- **Ejecución:** Higgsfield Marketing Studio (foto/URL de producto → video), Claude para guiones, hooks y matriz de ángulos; Canva para estáticos. Cero código.
- **Tipo / horas:** activo → semi-productizable. 3-5 h/sem por cliente al principio, 2-3 con plantillas.
- **Capital / 1er dólar:** USD 50-130/mes (Higgsfield Plus/Ultra). 3-6 semanas (portfolio con 2-3 marcas gratis o a precio de costo).
- **Desde AR:** excelente para clientes locales (pesos, Mercado Pago). Exportable a México/Chile/España vía Payoneer.
- **Riesgos:** commoditización (Meta Advantage+ ya genera variantes solo; Tiendanube suma IA propia); el cliente mide ROAS y te culpa si la pauta falla → vender **volumen y velocidad**, no resultados; etiqueta "AI info" con humanos fotorrealistas.
- **Score: 7,5/10** — mejor combinación demanda estructural + herramienta que ya tiene + cobro local fácil.

#### 2. Packs de UGC con avatares IA para marcas DTC internacionales (Upwork / Contra / outreach)
- **Qué es:** videos tipo "testimonio/demo" con avatar IA, en inglés/español, para tests de hooks. Cliente: marcas DTC de EE.UU./UE, apps móviles.
- **Señal:** Upwork +329% AI video editing 2026 ([Upwork jul-2026](https://www.upwork.com/research/upwork-monthly-hiring-insights-july-2026)); indies cobran USD 50-150 por video y USD 500-1.200 por pack de 10 ([AI Video Bootcamp ⚠ vende curso](https://aivideobootcamp.com/blog/ai-ugc-ads-2026-freelancer-playbook/)).
- **Cobro:** por pack o retainer USD 1.000-3.000/mes (techo de vendedores de cursos; mediana probablemente la mitad).
- **Ejecución:** Higgsfield (avatares, Speak, lip-sync) + Claude para guiones por ángulo.
- **Tipo / horas:** activo. 4-8 h/sem por cliente.
- **Capital / 1er dólar:** USD 60-130/mes + "connects" de Upwork. 4-10 semanas (perfil nuevo en Upwork tarda).
- **Desde AR:** Upwork/Contra → Payoneer. OK.
- **Riesgos:** **FTC prohíbe testimonios de personas inexistentes** (un avatar diciendo "lo probé y me cambió la vida" es ilegal en EE.UU.) → ofrecer solo demo/explicativo, no testimonio. Saturación fuerte: cualquiera con HeyGen ofrece lo mismo. Humano convierte mejor en verticales emocionales.
- **Score: 6,5/10** — buen precio en USD pero competencia global y riesgo legal en el formato más pedido.

#### 3. Subcontratista white-label de creatividades para agencias
- **Qué es:** vender capacidad de producción IA a agencias de performance (AR, MX, ES) que revenden con su marca.
- **Señal:** modelo white-label de 40-60% markup documentado en GEO y UGC ([Ciela ⚠](https://ciela.ai/blogs/ai-ugc-as-a-service-for-agencies)).
- **Cobro:** por pieza USD 15-40 o por pack. **Ejecución:** igual que 1. **Tipo:** activo, 5-10 h/sem.
- **Capital / 1er dólar:** USD 50-130/mes; 2-6 semanas (las agencias pagan rápido si entregás rápido).
- **Desde AR:** bien (pesos o Payoneer).
- **Riesgos:** margen bajo, dependencia de 1-2 agencias, sin marca propia.
- **Score: 6/10** — buen canal de arranque para cash y portfolio, no destino final.

#### 4. Suscripción de creatividades "ilimitadas" (productización de 1)
- **Qué es:** modelo Designjoy aplicado a creatividades IA: tarifa fija mensual, cola de pedidos, una entrega a la vez.
- **Señal:** [sin fuente propia en esta sesión]; el modelo de suscripción de diseño es conocido, aplicado a IA es la evolución natural de 1.
- **Cobro:** USD 300-800/mes (LATAM). **Tipo:** semi-pasivo a medias (siempre requiere producción, pero procesos estándar). 10-15 h/sem con 4-5 clientes.
- **Capital / 1er dólar:** igual que 1; solo tiene sentido con 3+ clientes de 1.
- **Riesgos:** clientes que abusan de la cola; churn mensual alto en PyMEs.
- **Score: 6,5/10** — es la fase 2 de la idea 1, no un arranque.

#### 5. Fotografía de producto IA para vendedores de Mercado Libre / Tiendanube
- **Qué es:** fondos, escenas lifestyle y variantes de color a partir de una foto casera del producto.
- **Señal:** costo IA USD 0,05-0,20 por imagen vs USD 90-270 por SKU tradicional; lifestyle +22-30% conversión ([Xictron 2026](https://www.xictron.com/en/blog/ki-bildgenerierung-produktfotos-e-commerce-2026/)). Un SaaS del rubro con USD 500-650 MRR se vende en Acquire ([Acquire](https://app.acquire.com/startup/cnhgq7flyk-ai-powered-product-photography-saas-for-ecommerce-650-mrr-7k-arr-90-profit-margins)) → el mercado de herramientas está saturado y barato.
- **Cobro:** por SKU (USD 3-10 en AR) o pack de catálogo. **Ejecución:** Higgsfield Product Shots + Claude para briefs.
- **Tipo / horas:** activo, 2-5 h/sem. **Capital / 1er dólar:** USD 20-50/mes; 1-3 semanas.
- **Desde AR:** muy bien (pesos).
- **Riesgos:** **commoditización total** (el vendedor puede hacerlo solo con apps de USD 20/mes; Mercado Libre y Tiendanube integran IA); fotos que no representan el producto real → reclamos y defensa del consumidor.
- **Score: 5,5/10** — sirve como **oferta de entrada** barata para vender la idea 1; sola no escala.

#### 6. Optimización de fichas y catálogo en Mercado Libre ("ficha que vende")
- **Qué es:** reescribir títulos/atributos para el buscador de ML, fotos, descripción, ficha técnica completa, preguntas frecuentes; mensual = mantenimiento de catálogo.
- **Señal:** consultores ML venden "acompañamiento mensual" (catálogo, reputación, precios, Ads) ([Algoritmo Digital 2026](https://algoritmodigital.com.ar/cuanto-cobra-un-consultor-de-mercado-libre-2026/)); comisiones ML 8-20,5% hacen que cada punto de conversión importe.
- **Cobro:** por ficha (USD 5-15) o retainer USD 150-400/mes. **Ejecución:** Claude (títulos, atributos, descripciones en lote desde una planilla) + Higgsfield (fotos).
- **Tipo / horas:** activo, 2-4 h/sem por cliente. **Capital / 1er dólar:** ~USD 0-50; 2-4 semanas.
- **Desde AR:** ideal (el mercado está acá).
- **Riesgos:** precio bajo; competencia de consultores ML establecidos; ML automatiza sugerencias de título con IA.
- **Score: 6/10** — sinergia muy fuerte con 1 y 5 (mismo cliente, misma conversación) y con la consultora de **orden operativo** (vendedores con muchos SKUs).

#### 7. Kit de marketing inmobiliario IA (virtual staging + reels de propiedad)
- **Qué es:** amoblado virtual de fotos de propiedades vacías + reel vertical por propiedad para inmobiliarias locales.
- **Señal:** virtual staging IA USD 0,24-25 por foto; agentes piden 5-8 fotos por publicación ([Bella Virtual 2026-07-20](https://www.bellavirtual.com/blogs/news/virtual-staging-cost-guide), [AI HomeDesign 2026-07](https://aihomedesign.com/blog/services/virtual-staging-software)).
- **Cobro:** por propiedad USD 20-60 o abono mensual a la inmobiliaria USD 100-300.
- **Ejecución:** Higgsfield (imagen→video de recorrida, staging) + Claude (copy de publicación).
- **Tipo / horas:** activo recurrente, 2-4 h/sem por inmobiliaria. **Capital / 1er dólar:** USD 20-60/mes; 2-4 semanas.
- **Desde AR:** bien, mercado local.
- **Riesgos:** herramientas a USD 0,24/foto → la inmobiliaria grande lo hace sola; staging engañoso (hay que marcar "imagen ilustrativa").
- **Score: 5,5/10.**

#### 8. Fotos/videos de menú IA para gastronomía (PedidosYa, Rappi, Instagram) [sin fuente propia]
- **Qué es:** mejorar fotos de platos y crear reels de menú para restaurantes.
- **Cobro:** USD 50-200 por menú + abono de reels. **Tipo:** activo, 2-3 h/sem por cliente.
- **Riesgos:** la foto debe representar el plato real (publicidad engañosa); rubro con poca plata y mucho churn.
- **Score: 4,5/10.**

#### 9. Branding / logos con IA para PyMEs
- **Qué es:** identidad visual básica (logo, paleta, plantillas) con IA.
- **Señal:** [sin fuente propia]; Looka, Canva y similares lo resuelven por <USD 100.
- **Cobro:** USD 50-300 por kit. **Riesgos:** commoditización casi total; Fiverr a USD 5-30.
- **Score: 3,5/10** — solo como add-on de 1.

#### 10. Pitch decks / presentaciones como servicio
- **Señal:** Fiverr USD 15-150+; estudios USD 799-6.000 por deck de 15-20 slides ([ManyPixels](https://www.manypixels.co/blog/presentations/pitch-deck-design-services), [Upmetrics](https://upmetrics.co/blog/pitch-deck-design-cost)).
- **Ejecución:** Claude (narrativa, estructura) + Gamma/Canva. **Tipo:** activo por proyecto, 5-10 h por deck.
- **Riesgos:** Gamma/Claude ya hacen decks decentes; el valor real es la narrativa financiera (requiere experiencia en startups que el usuario no tiene declarada); demanda chica en AR.
- **Score: 4/10.**

#### 11. Videos explicativos / capacitación con avatar para empresas (multi-idioma)
- **Qué es:** videos de onboarding, producto o capacitación interna con avatar y doblaje, para PyMEs y SaaS.
- **Señal:** avatar USD 0,39-1,45 por video de 30 s ([Digital Applied](https://www.digitalapplied.com/blog/ai-avatar-ads-vs-real-ugc-creators-cost-trust-2026)); doblaje IA USD 2-20/min ([Vozo ⚠](https://www.vozo.ai/es/blogs/ai-dubbing/ai-dubbing-vs-traditional-cost)).
- **Cobro:** USD 100-500 por video / paquete. **Tipo:** activo, por proyecto.
- **Riesgos:** ciclo de venta B2B largo; Synthesia apunta directo a empresas.
- **Score: 5/10** — encaja mejor como upsell de la consultora de orden operativo (videos de procedimientos de depósito).

### B. Servicios para creadores

#### 12. Clipping como servicio (retainer) para podcasts y creadores hispanos
- **Qué es:** 15-30 clips/mes con subtítulos, hooks y publicación, para podcasters/streamers de habla hispana. *Distinto del clipper-semiauto en cartera (que cobra por campañas/vistas): acá cobra el creador.*
- **Señal:** retainers USD 200-500 (10-15 clips) a USD 500-1.200 (20-30) ([ClipSpeed ⚠ vende herramienta](https://www.clipspeed.ai/blog/how-to-price-clipping-services.html)).
- **Cobro:** USD 150-500/mes en LATAM. **Ejecución:** clipper de Higgsfield + Claude (títulos, hooks); revisión humana de cortes.
- **Tipo / horas:** activo, 2-4 h/sem por cliente. **Capital / 1er dólar:** USD 20-60/mes; 2-4 semanas.
- **Desde AR:** bien (pesos o Payoneer).
- **Riesgos:** OpusClip y similares a USD 15-30/mes → el creador chico lo hace solo; solo pagan los medianos/grandes que valoran criterio editorial. Reutiliza 100% de lo que se aprenda en clipper-semiauto.
- **Score: 6,5/10.**

#### 13. Post-producción de YouTube long-form con IA (edición + miniaturas + títulos)
- **Señal:** edición de video IA +329% en Upwork; USD 25-100/h ([Upwork](https://www.upwork.com/research/upwork-monthly-hiring-insights-july-2026), [Wirestock 2026-08-04](https://wirestock.io/blog/remote-video-editing-jobs)).
- **Ejecución:** requiere un editor (CapCut/Descript) + Higgsfield para b-roll/miniaturas. **Curva de aprendizaje real de edición.**
- **Tipo / horas:** activo, 6-10 h/sem por cliente.
- **Riesgos:** sin oficio de edición la calidad no compite; mercado global saturado de editores baratos.
- **Score: 5/10.**

#### 14. Miniaturas + títulos A/B como servicio para canales
- **Señal:** [sin fuente propia]; YouTube tiene "Test & Compare" nativo, lo que vuelve medible el servicio.
- **Cobro:** USD 15-60 por miniatura o USD 200-500/mes. **Ejecución:** Higgsfield/imagen + Claude.
- **Riesgos:** commoditizado; el resultado depende del contenido del canal.
- **Score: 4,5/10.**

#### 15. Repurposing: de un podcast/video a newsletter, blog, LinkedIn y carruseles
- **Señal:** [sin fuente propia directa]; la economía la marca la caída de costo de texto (Claude).
- **Cobro:** USD 200-600/mes. **Ejecución:** Claude puro (transcripción → piezas) + Canva.
- **Tipo / horas:** activo muy procesable, 2-3 h/sem por cliente.
- **Riesgos:** fácil de copiar; el cliente lo puede hacer con ChatGPT.
- **Score: 5,5/10** — buen complemento de 12 (mismo cliente).

#### 16. Doblaje / localización de canales de YouTube (revenue share)
- **Qué es:** crear la versión en español o portugués de un canal en inglés y cobrar % de lo que genere.
- **Señal:** Linguana levantó USD 8,5 M y AIR Media-Tech operan a revenue share sin costo inicial ([Slator](https://slator.com/ai-dubbing-startup-linguana-raises-usd-8m-scale-multilingual-youtube-channels/), [AIR](https://air.io/en/how-much-video-translation-costs)).
- **PERO:** YouTube lanzó **auto-dubbing gratis para todos** en 27 idiomas, con lip sync y "Expressive Speech"; 6 M de espectadores diarios en dic-2025 ([Storyboard18](https://www.storyboard18.com/digital/youtube-expands-auto-dubbing-to-27-languages-adds-more-natural-and-expressive-voices-88923.htm), [TechCrunch](https://techcrunch.com/?p=2561000)).
- **Riesgos:** **la plataforma regaló el producto**; queda valor solo en curaduría premium (canales grandes) donde compiten firmas financiadas. Revenue share = cobrás meses después.
- **Score: 3,5/10** — ventana cerrándose.

#### 17. Localización de cursos online al español/portugués
- **Señal:** Hotmart lanzó **Hotmart AI** con traducción y doblaje automático para sus 200.000+ creadores ([DPL News](https://dplnews.com/?p=247389)).
- **Riesgos:** igual que 16: la plataforma de cobro lo integra nativo.
- **Score: 3/10.**

### C. Gestión de redes y escritura

#### 18. Gestión de redes con IA para PyMEs locales (Tucumán / interior)
- **Señal:** retainers internacionales USD 500-5.000 ([Blabla ⚠](https://blabla.ai/es/blog/social-media-management-agency-pricing)); en AR el community manager freelance cobra mucho menos, sin dato 2026 confiable en esta sesión ([iProUP, nota anterior](https://www.iproup.com/empleo/48533-cuanto-cobra-un-community-manager-freelance-en-la-argentina)).
- **Cobro:** USD 80-250/mes por PyME. **Ejecución:** Claude (calendario, copys) + Higgsfield (reels) + programador de publicaciones.
- **Tipo / horas:** activo, 3-5 h/sem por cliente.
- **Riesgos:** oficio saturado, precio bajo, clientes que miden "likes"; poco diferenciable.
- **Score: 5/10** — sirve si se empaqueta con 1 (redes + ads), no sola.

#### 19. Ghostwriting de LinkedIn para ejecutivos y profesionales (español)
- **Señal:** entry USD 500-1.500/mes (8-12 posts), medio USD 2.000-4.000, premium USD 5.000-10.000+ ([BizToolkit](https://www.biztoolkit.co/post/linkedin-ghostwriter-rates-in-2026-per-post-monthly-package), [Ordinal](https://www.tryordinal.com/blog/executive-ghostwriting)). La propia fuente admite que **no hay tarifa verificable** porque casi nadie publica precios.
- **Cobro:** en LATAM realista USD 300-1.000/mes. **Ejecución:** entrevista mensual de 45 min + Claude para redactar en la voz del cliente.
- **Tipo / horas:** activo, 3-4 h/sem por cliente.
- **Desde AR:** bien (Payoneer o pesos).
- **Riesgos:** el valor está en la estrategia y en entender el negocio del cliente; LinkedIn se llenó de texto IA genérico (no pude verificar en esta sesión si hay penalización algorítmica 2026 — búsqueda agotada). Sinergia: el propio usuario puede usarlo para vender la consultora.
- **Score: 6/10.**

#### 20. Ghostwriting de X/Threads para founders
- **Riesgos:** audiencia hispana chica en X para B2B; pago menor que LinkedIn.
- **Score: 4/10.**

#### 21. "Clon digital" en video para profesionales (médicos, abogados, inmobiliarios, contadores)
- **Qué es:** el profesional graba 1 vez, se arma su avatar/voz, y recibe 8-12 videos/mes educativos con su cara para Reels/TikTok/YouTube.
- **Señal:** costo de avatar <USD 2 por video; demanda de video vertical de profesionales. [sin fuente propia de precios del servicio].
- **Cobro:** USD 150-500/mes. **Ejecución:** Higgsfield (Soul ID / Speak / lip-sync) + Claude (guiones).
- **Tipo / horas:** activo productizable, 2-3 h/sem por cliente.
- **Riesgos:** etiquetado IA obligatorio (Meta/TikTok); en salud/derecho, colegios profesionales y regulación de publicidad; el público castiga lo "artificial" en contenido de confianza ([Digital Applied](https://www.digitalapplied.com/blog/ai-avatar-ads-vs-real-ugc-creators-cost-trust-2026)). Consentimiento explícito por escrito siempre.
- **Score: 5,5/10.**

### D. Medios propios (audiencia)

#### 22. Newsletter de nicho con sponsors (inglés)
- **Señal:** CPM mediano USD 32; B2B USD 85-115; Beehiiv Ad Network USD 25-40 CPM ([VoxBooster ⚠](https://voxbooster.com/blog/newsletter-sponsorship-statistics-2026/), [eMarketer](https://www.emarketer.com/content/beehiiv-doubles-ad-sales-team-newsletter-monetization-heats-up)).
- **Cuenta realista:** 5.000 suscriptores × 40% apertura × USD 32 CPM ≈ USD 64 por envío con sponsor. Llegar a 5.000 lleva 6-18 meses para la mediana.
- **Tipo / horas:** semi-pasivo, 3-5 h/sem. **Capital:** USD 0-50/mes (+ pauta de crecimiento opcional).
- **Riesgos:** lento; "AI newsletter 10k en 90 días" son casos de vendedores de cursos ([Vantaige ⚠](https://vantaige.io/blog/ai-niche-newsletter-10k-subscribers-90-days-2026)); verificar pagos de Beehiiv Ad Network a AR (no verificado en esta sesión).
- **Score: 4,5/10.**

#### 23. Newsletter B2B hispana de nicho (ej.: vendedores de Mercado Libre / e-commerce LATAM)
- **Qué es:** semanal con novedades de ML, Tiendanube, logística, ads. Sponsors locales (apps de Tiendanube, logísticas, agencias).
- **Señal:** ventas online AR +42% en 2026; 65.000 marcas solo en Tiendanube ([Mercado 2026](https://mercado.com.ar/ruta-digital/tiendanube-midterm-2026-el-e-commerce-argentino-subio-421-y-sumo-ia)).
- **Cobro:** sponsors directos USD 50-300 por envío cuando haya 2-5k suscriptores; **valor principal = generar clientes para 1, 5, 6** y la consultora de orden operativo.
- **Tipo / horas:** semi-pasivo, 3 h/sem. **Capital:** ~USD 0. **1er dólar:** 4-9 meses.
- **Riesgos:** CPM en español bastante menor; lento.
- **Score: 5,5/10** — como máquina de leads, más que como negocio en sí.

#### 24. Reseñas/comparativas en video + afiliados de Mercado Libre y YouTube Shopping AR — **EVIDENCIA NUEVA**
- **Qué es:** canal (YouTube long-form + Shorts + Reels/TikTok) de comparativas y "lo mejor de X en Mercado Libre" con links de afiliado; en YouTube, productos etiquetados en el video.
- **Señal nueva y fuerte:**
  - Mercado Libre lanzó su **Programa de Afiliados y Creadores en Argentina el 2026-03-11**: comisión **hasta 15%** según categoría, cobro en **Mercado Pago**, **sin mínimo de seguidores**, comisión también sobre otros productos que compre el usuario referido; creadores con +10.000 seguidores en IG/TikTok acceden a campañas que pagan por vistas. Ventas por afiliados en AR +800% entre Q3 y Q4 2025 ([Mercado 2026-03-11](https://mercado.com.ar/marketing/mercado-libre-lanzo-en-el-pais-su-programa-de-afiliados-y-creadores-con-comisiones-de-hasta-15), [Forbes AR](https://www.forbesargentina.com/negocios/mercado-libre-sale-caza-creator-economy-lanza-su-programa-afiliados-monetizar-recomendaciones-n87534)).
  - **YouTube Shopping llegó a Argentina en julio 2026** en alianza con Mercado Libre: etiquetado de productos en videos y lives, requisito **500 suscriptores + condiciones de YPP**, comisión hasta 15% (más alta en consumo masivo/belleza, más baja en tecnología) ([Innovación Digital 360](https://www.innovaciondigital360.com/pago-electronico/youtube-shopping-argentina-mercado-libre/)).
- **Por qué no repite el descarte de "afiliados SEO":** aquel era tráfico de Google a sitios (destruido por AI Overviews y el update de marzo 2026). Esto es **video + red social + marketplace dominante local**, con cobro en pesos sin fricción.
- **Ejecución:** Claude (investigación de productos, guiones comparativos), Higgsfield (b-roll, Shorts Studio, publicación a TikTok). **Clave:** tener el producto o al menos mostrar análisis real; cara o voz propia recomendable.
- **Tipo / horas:** semi-pasivo (los videos de comparativa duran meses), 5-8 h/sem construyendo.
- **Capital / 1er dólar:** USD 20-60/mes; 1-3 meses para primeras comisiones vía Shorts/TikTok; YouTube Shopping recién con 500 subs + YPP.
- **Desde AR:** ideal. **Requisito:** inscribirse como **monotributista** para facturar.
- **Riesgos:** ticket en pesos con inflación; comisiones bajas en tecnología; política de inauténtico de YouTube si se automatiza demasiado (voz TTS + stock = riesgo alto); ML puede bajar comisiones cuando el programa madure (patrón clásico de Amazon Associates 2020); disclosure de afiliado obligatorio.
- **Score: 7/10** — la novedad más relevante del frente para un argentino; sinergia directa con el canal long-form en cartera.

#### 25. Shorts/TikTok de "hallazgos de Mercado Libre" (afiliado ML de formato corto)
- **Qué es:** versión corta de 24 en TikTok/Reels/WhatsApp Canal; objetivo: 10.000 seguidores para entrar a campañas pagas por vistas de ML.
- **Ejecución:** Higgsfield Shorts Studio + publicación directa a TikTok.
- **Riesgos:** etiquetado IA en TikTok; formato hiper-saturado; TikTok no paga Rewards en AR (ya descartado), así que la plata viene solo de comisiones.
- **Score: 6/10** — mejor como brazo de distribución de 24 que como negocio aparte.

#### 26. Podcast de nicho generado con IA (modelo Inception Point)
- **Señal:** Inception Point AI: 5.000 shows, 3.000 episodios/semana a ~USD 1 c/u, rentable con ~20 oyentes vía publicidad programática; 12 M de descargas totales ([Semafor 2025-09-12](https://www.semafor.com/article/09/12/2025/ai-podcast-company-releases-3000-episodes-a-week), [Implicator](https://www.implicator.ai/the-dollar-episode-how-inception-point-ai-turned-podcasting-into-arbitrage/)).
- **Riesgos:** el modelo solo funciona a escala industrial con acceso a programática de EE.UU.; en español los CPM son menores; reacción negativa de la industria y riesgo de políticas de Spotify/Apple contra contenido masivo IA (mismo patrón que la purga musical de Spotify).
- **Score: 2,5/10.**

#### 27. Canal faceless long-form de nicho (nuevo)
- **Señal:** RPM long-form faceless USD 5-12 general; finanzas USD 10-50 ([GoFaceless ⚠](https://www.gofaceless.ai/blog/youtube-ai-slop-policies-faceless-monetization), [OutlierKit ⚠](https://outlierkit.com/resources/faceless-youtube-channel-demonetized/)). La política de inauténtico apunta exactamente a TTS + stock.
- Ver "Ya en cartera": no abrir un segundo canal; si acaso, sumar el ángulo de afiliados ML (24) al que ya está planeado.
- **Score: 4,5/10** (como canal nuevo adicional).

#### 28. Influencer virtual / IA para marcas (SFW)
- **Señal:** Aitana López reportada con ingresos de 5 cifras/mes en brand deals; brand deals USD 100-34.000 por post ([CreatorFlow](https://creatorflow.so/blog/how-ai-influencers-make-money/), [TechBullion](https://techbullion.com/the-virtual-creator-shift-how-to-create-and-monetize-an-ai-influencer-in-2026-complete-revenue-stack-from-subscriptions-to-brand-deals/)). **Survivorship bias extremo**: se citan los 5 que funcionan de miles.
- **Alerta:** gran parte de la plata del sector está en plataformas tipo Fanvue (USD 100 M ARR 2025, [Sacra](https://sacra.com/c/fanvue/)), con fuerte componente de contenido adulto. **No recomendado** para este laboratorio (riesgo reputacional, de pagos y legal).
- **Riesgos:** NY synthetic performer law (2026-06-09), EU AI Act (2026-08-02), etiquetas obligatorias; construir audiencia lleva 6-12+ meses.
- **Score: 3/10.**

#### 29. Afiliado de TikTok Shop
- **Señal:** TikTok Shop opera en México (desde 2025, con beta transfronteriza para vendedores de EE.UU. en mar-2026) y Brasil ([Modern Retail 2026-03-05](https://www.modernretail.co/operations/marketplace-briefing-tiktok-shop-recruits-u-s-sellers-for-cross-border-push-into-mexico/), [Rest of World 2025](https://restofworld.org/2025/tiktok-shop-latin-america-shein-temu/)). **No disponible en Argentina** al 2026-10-01, sin fecha anunciada; AR tiene 33 M de usuarios de TikTok y 60% compró algo tras ver un video ([El Economista](https://eleconomista.com.ar/tech/tiktok-revela-cuantos-usuarios-tiene-argentina-como-cambia-consumo-60-compra-tras-ver-video-n93409)).
- **Riesgos:** operar en MX requiere residencia/cuenta local.
- **Score: 2/10 hoy** — **poner alerta**: si llega a AR, revaluar (sería 6-7 por la combinación con Higgsfield→TikTok).

### E. E-commerce propio

#### 30. Tienda Tiendanube de nicho con marca propia + creatividades IA
- **Qué es:** marca propia de un nicho, stock chico, todo el marketing con IA.
- **Riesgos:** requiere capital de inventario (choca con USD <1.000), logística, devoluciones, pauta (CAC); la mediana de tiendas nuevas no llega a rentabilidad en 12 meses [sin fuente propia en esta sesión].
- **Score: 4/10** — más inteligente vender servicios a las 65.000 tiendas que ya existen.

#### 31. Dropshipping / Shopify internacional desde AR
- **Riesgos:** cobro y pasarelas desde AR, saturación, márgenes, cuentas de Meta Ads suspendidas; clásico territorio de gurús con cursos.
- **Score: 2/10.**

### F. Visibilidad en IA (GEO/AEO) y SEO

#### 32. Auditoría GEO/AEO para marcas y PyMEs hispanas (servicio)
- **Qué es:** auditar cómo aparece una marca en ChatGPT/Gemini/Claude/Perplexity y entregar plan (contenido citable, FAQs, fichas, reseñas, menciones en terceros).
- **Señal:** mercado de servicios GEO USD 1,48 B en 2026 (cifras de consultoras que venden GEO ⚠); auditoría USD 1.500-5.000, retainer USD 3.000-10.000/mes ([Nutshell ⚠](https://www.nutshell.com/blog/geo-costs), [Xpand Digital ⚠](https://xpanddigital.io/geo-pricing), [DemandLocal ⚠](https://www.demandlocal.com/blog/how-to-price-geo-services/)). Tráfico desde ChatGPT a e-commerce de EE.UU. +210% interanual en Q1 2026 ([eMarketer](https://www.emarketer.com/content/ai-assistants-strong-referral-traffic-drivers-paths-purchase-industry-kpis-show)).
- **Contrapeso:** la referencia IA es **0,32% del tráfico web total** ([SE Ranking](https://seranking.com/blog/ai-traffic)) → para una PyME argentina hoy el impacto en ventas es chico y difícil de medir.
- **Cobro:** en LATAM auditoría USD 150-500; retainer USD 200-600.
- **Ejecución:** Claude (consultas sistemáticas a varios asistentes, análisis, plan); sin código es manual pero factible.
- **Tipo / horas:** activo, 4-8 h por auditoría.
- **Riesgos:** **zona de humo**: resultados no garantizables, métricas inestables (las respuestas de los LLM varían); el cliente no sabe qué compra; muchos vendedores de "GEO" son SEO re-etiquetado. Sin base de SEO, el usuario aprendería sobre la marcha.
- **Score: 5/10** — tendencia real, pero es más fácil venderla como **add-on** de 6 (fichas ML) o 1 que como servicio principal.

#### 33. Reporte mensual de "visibilidad en IA" (productizado, semi-pasivo)
- **Qué es:** reporte automatizado: "tu marca vs 3 competidores en 50 preguntas, este mes".
- **Riesgos:** sin programar, la automatización depende de herramientas de terceros (Profound, Peec, etc.) → margen fino. Si el usuario programara, sería un micro-SaaS con buen fit (encaja con el stack de datos).
- **Score: 4,5/10** (sin código) / 6,5 (con código).

#### 34. SEO programático
- **Señal:** update de marzo 2026: granjas IA -60/80%; solo sobreviven páginas con datos reales o utilidad ([ThePublive](https://www.thepublive.com/blog/google/google-fired-twice-in-24-hours-what-the-march-2026-spam-core-update-means-for-seo-aeo-and-llmo-11264463-11435131), [MadX](https://www.madx.digital/learn/programmatic-seo-ai-overviews)).
- **Score: 2,5/10** para este perfil (requiere datos propios y código).

### G. Personalizados y regalos (B2C)

#### 35. Canciones personalizadas con IA para regalos y eventos (no streaming)
- **Señal:** Songfinch (canciones por músicos humanos a USD 199): ingresos USD 75 M en 2023, Series A de USD 17 M ([Music Business Worldwide](https://www.musicbusinessworldwide.com/the-weeknd-backed-personalized-song-creation-firm-songfinch-raises-17m), [CB Insights](https://www.cbinsights.com/company/songfinch/financials)). La demanda de "canción para cumpleaños/aniversario" está probada; la IA baja el costo a centavos.
- **Cobro:** en AR USD 10-40 por canción (pesos, Mercado Pago); con video lyric +USD 10-20.
- **Ejecución:** Claude (letra con la historia del cliente) + generador musical con licencia comercial + Higgsfield (video con fotos).
- **Tipo / horas:** activo de bajo ticket; semi-productizable con formulario. 3-6 h/sem.
- **Capital / 1er dólar:** USD 10-30/mes; 1-3 semanas (Instagram/WhatsApp, fechas: Día de la Madre AR es en octubre).
- **Riesgos:** **verificar términos de uso comercial** del generador musical (y litigios de discográficas en curso contra generadores IA); saturación rápida (cualquiera lo ofrece); ticket bajo → necesita volumen.
- **Score: 5,5/10.**

#### 36. Jingles y música para marcas/PyMEs (spots, radio local, reels)
- **Cobro:** USD 50-300 por jingle. **Ejecución:** igual que 35.
- **Riesgos:** derechos (la marca quiere propiedad clara; la obra 100% IA puede no tener copyright protegible); demanda local limitada.
- **Score: 4,5/10.**

#### 37. Videos personalizados para eventos (bodas, 15, jubilaciones, homenajes, cumpleaños)
- **Qué es:** video emotivo con fotos animadas IA, música personalizada (35) y narración, para proyectar en el evento o regalar.
- **Señal:** [sin fuente propia en esta sesión]; mercado de eventos tradicional donde ya se pagan "videos de fotos" — la IA sube la calidad y baja el tiempo.
- **Cobro:** USD 30-150 por video en AR.
- **Ejecución:** Higgsfield (imagen→video, animar fotos viejas, música) + Claude (guion). Muy alto fit con la herramienta que ya tiene.
- **Tipo / horas:** activo estacional, 3-6 h/sem.
- **Capital / 1er dólar:** USD 20-60/mes; 1-3 semanas (conocidos, salones de eventos, organizadores de bodas como canal).
- **Riesgos:** ética y consentimiento (animar fotos de fallecidos, menores); TikTok prohíbe sintéticos de personas privadas reales — **no publicar los trabajos de clientes como portfolio sin permiso**; ticket bajo.
- **Score: 6/10** — rápido al primer peso, buen fit, techo bajo.

#### 38. Libros infantiles personalizados con IA (digital o impreso)
- **Señal:** distribución muy desigual: Little Hero Book USD 74k MRR (outlier) vs la mayoría de proyectos con ARR de USD 229-1.400 ([TrustMRR](https://trustmrr.com/startup/little-hero-book?metric=mrr), [Microns](https://www.microns.io/startup-listings/ai-storybook-generator)). Precio de mercado USD 20-50 por libro.
- **Riesgos:** survivorship bias claro; impresión y envío en AR caros; consistencia de personajes (Higgsfield Soul ID ayuda); fotos de menores (privacidad).
- **Score: 4/10.**

---

## Ya en cartera (datos actualizados breves)

- **Clipper semi-automático (proyecto `proyectos/clipper-semiauto/`):** nada nuevo en esta sesión que cambie el gate de la semana 8. Dato útil: la línea "clipping como servicio" (idea 12) reutiliza todo lo que el clipper aprenda y cobra fijo mensual en vez de por vistas — es un **plan B natural** si las campañas de Whop no pagan bien desde AR (el payout a AR sigue pendiente de verificar según `AVANCE.md`). Precios de referencia retainer: USD 200-1.200/mes ([ClipSpeed ⚠](https://www.clipspeed.ai/blog/how-to-price-clipping-services.html)).
- **YouTube long-form editorial:** (a) la política de inauténtico rige desde **2025-07-15** (no 2026); TTS + stock = patrón de mayor riesgo; voz propia o voz humana revisada = seguro ([GoFaceless ⚠](https://www.gofaceless.ai/blog/youtube-ai-slop-policies-faceless-monetization)). (b) **Novedad que suma:** YouTube Shopping AR (julio 2026) permite monetizar con comisiones de Mercado Libre desde **500 suscriptores + YPP**, antes del AdSense pleno → conviene elegir el nicho del canal pensando en productos de ML (idea 24). (c) Auto-dubbing gratis de YouTube en 27 idiomas: el canal en español puede ganar audiencia en portugués/inglés sin costo ([Storyboard18](https://www.storyboard18.com/digital/youtube-expands-auto-dubbing-to-27-languages-adds-more-natural-and-expressive-voices-88923.htm)).

---

## Top 5 del frente

| # | Idea | Por qué |
|---|---|---|
| 1 | **Estudio de creatividades IA para e-commerce LATAM** (1, con escalera 5→6→1→4) | Demanda estructural creada por Meta Andromeda (volumen de creatividades), 65.000 tiendas Tiendanube en AR + vendedores ML, herramienta ya pagada (Higgsfield Marketing Studio), cobro en pesos sin fricción. Oferta de entrada barata (fotos/fichas) → retainer de creatividades → suscripción. |
| 2 | **Reseñas/comparativas en video + afiliados ML / YouTube Shopping AR** (24 + 25) | Evidencia nueva fuerte (programa ML AR 2026-03-11, YouTube Shopping AR jul-2026), cobro en Mercado Pago, semi-pasivo, se fusiona con el canal long-form en cartera. |
| 3 | **Packs de UGC/explainers con avatar para marcas internacionales** (2) | Cobra en USD vía Upwork/Payoneer, demanda +329%; evitar el formato "testimonio" (FTC). |
| 4 | **Clipping retainer para podcasts/creadores hispanos** (12 + 15) | Reutiliza el clipper en cartera; ingreso fijo mensual en vez de por vistas; plan B si Whop no paga a AR. |
| 5 | **Videos personalizados para eventos + canción IA** (37 + 35) | El más rápido al primer peso (1-3 semanas), máximo fit con Higgsfield, cero capital; techo bajo, útil como caja y práctica de producción. |

**Lectura de conjunto:** 1, 3 y 6/5 son en realidad **un solo negocio** ("estudio de producción IA para marcas") con tres puertas de entrada (local en pesos, internacional en USD, oferta barata de fichas/fotos). La idea 24 es la única con componente semi-pasivo real y encaja con lo ya planeado. Además, la idea 6 (fichas ML) y 23 (newsletter para vendedores ML) se cruzan con la consultora de **orden operativo**: el mismo cliente (vendedor con muchos SKUs) compra catálogo, creatividades y orden de depósito.

---

## Trampas comunes

1. **Precios de "cuánto cobrar" escritos por quien vende la herramienta o el curso.** Casi todos los rangos USD de UGC IA, clipping, newsletters y GEO vienen de Vantaige, AI Video Bootcamp, ClipSpeed, Creatify, Segwise, VoxBooster o agencias de GEO. Tomar el piso del rango como techo realista para un principiante en LATAM.
2. **Survivorship bias en influencers IA, libros personalizados y newsletters:** Aitana López y Little Hero Book son outliers; la mediana de proyectos similares factura cientos de dólares por año.
3. **La plataforma te come el negocio:** YouTube auto-dubbing gratis (mata 16), Hotmart AI (mata 17), Meta Advantage+ y la IA de Tiendanube (presionan 1 y 5), OpusClip (presiona 12). Vender **criterio, velocidad y gestión**, no "acceso a la herramienta".
4. **Fábricas de contenido propio para monetizar por vistas:** es exactamente lo que YouTube (2025-07-15), Google (marzo 2026) y Spotify castigan. La IA es segura como herramienta de producción para un cliente o una voz propia, no como granja.
5. **Testimonios con avatar:** ilegales en EE.UU. (FTC 16 CFR 255.1) si simulan personas reales que probaron el producto; además rinden peor en verticales emocionales. Usar avatares para demos, explicativos y variantes de hooks.
6. **Etiquetado y C2PA:** Meta y TikTok detectan metadatos automáticamente; la etiqueta "AI info" no se puede quitar. Nunca prometer al cliente que "no se va a notar que es IA".
7. **Personas reales privadas:** TikTok prohíbe medios sintéticos de personas privadas reales aun con etiqueta → cuidado con portfolio de videos de eventos y clones.
8. **GEO como humo:** 0,32% del tráfico web viene de IA (2026); vender "aparecer en ChatGPT" sin métricas estables es receta para clientes insatisfechos. Venderlo como add-on medible, no como promesa.
9. **Cobro desde AR:** clientes locales → monotributo + Mercado Pago (el programa de afiliados de ML **exige** monotributo). Clientes del exterior → Upwork/Contra → Payoneer. Los merchant of record (Lemon Squeezy, Hotmart) son para productos digitales, **no para servicios** — verificar términos antes de usarlos para cobrar servicios.
10. **Licencias de las herramientas:** Higgsfield da uso comercial solo en planes pagos; los generadores de música IA tienen términos comerciales y litigios en curso. Leer los términos antes de vender lo generado.
11. **Afiliación sujeta a recortes:** los programas nuevos (ML 2026) suelen pagar bien al principio para atraer creadores y recortar comisiones al madurar. No construir un plan cuya rentabilidad dependa del 15% máximo.

---

## Fuentes principales (todas consultadas el 2026-10-01)

- Upwork Monthly Hiring Insights jul-2026 — https://www.upwork.com/research/upwork-monthly-hiring-insights-july-2026
- Digital Applied, "AI avatar ads vs real UGC creators" (2026-09-17) — https://www.digitalapplied.com/blog/ai-avatar-ads-vs-real-ugc-creators-cost-trust-2026
- Mercado (2026-03-11), Programa de Afiliados y Creadores ML AR — https://mercado.com.ar/marketing/mercado-libre-lanzo-en-el-pais-su-programa-de-afiliados-y-creadores-con-comisiones-de-hasta-15
- Innovación Digital 360, YouTube Shopping AR + ML (jul-2026) — https://www.innovaciondigital360.com/pago-electronico/youtube-shopping-argentina-mercado-libre/
- Mercado, Tiendanube midterm 2026 — https://mercado.com.ar/ruta-digital/tiendanube-midterm-2026-el-e-commerce-argentino-subio-421-y-sumo-ia
- PlagiarismToday (2025-07-08), YouTube inauthentic content — https://www.plagiarismtoday.com/2025/07/08/youtube-targets-inauthentic-content/
- Segwise ⚠, Meta Andromeda 2026 — https://segwise.ai/blog/meta-andromeda-update-creative-strategy-2026
- SE Ranking, AI traffic 2026 — https://seranking.com/blog/ai-traffic
- eMarketer, AI assistants referral traffic — https://www.emarketer.com/content/ai-assistants-strong-referral-traffic-drivers-paths-purchase-industry-kpis-show
- Storyboard18, YouTube auto-dubbing 27 idiomas — https://www.storyboard18.com/digital/youtube-expands-auto-dubbing-to-27-languages-adds-more-natural-and-expressive-voices-88923.htm
- Slator, Linguana USD 8,5 M — https://slator.com/ai-dubbing-startup-linguana-raises-usd-8m-scale-multilingual-youtube-channels/
- DPL News, Hotmart AI — https://dplnews.com/?p=247389
- Semafor (2025-09-12), Inception Point AI — https://www.semafor.com/article/09/12/2025/ai-podcast-company-releases-3000-episodes-a-week
- Music Business Worldwide, Songfinch — https://www.musicbusinessworldwide.com/the-weeknd-backed-personalized-song-creation-firm-songfinch-raises-17m
- TrustMRR, Little Hero Book — https://trustmrr.com/startup/little-hero-book?metric=mrr
- Modern Retail (2026-03-05), TikTok Shop México — https://www.modernretail.co/operations/marketplace-briefing-tiktok-shop-recruits-u-s-sellers-for-cross-border-push-into-mexico/
- ThePublive, Google marzo 2026 — https://www.thepublive.com/blog/google/google-fired-twice-in-24-hours-what-the-march-2026-spam-core-update-means-for-seo-aeo-and-llmo-11264463-11435131
- Creatify ⚠ (competidor), precios Higgsfield 2026 — https://creatify.ai/blog/higgsfield-pricing-(2026)-plans-and-what-you-ll-actually-pay
- ClipSpeed ⚠, precios de clipping — https://www.clipspeed.ai/blog/how-to-price-clipping-services.html
- VoxBooster ⚠, newsletter sponsorship 2026 — https://voxbooster.com/blog/newsletter-sponsorship-statistics-2026/
- Nutshell ⚠ / Xpand Digital ⚠, precios GEO — https://www.nutshell.com/blog/geo-costs , https://xpanddigital.io/geo-pricing
- BizToolkit / Ordinal, tarifas ghostwriting LinkedIn — https://www.biztoolkit.co/post/linkedin-ghostwriter-rates-in-2026-per-post-monthly-package , https://www.tryordinal.com/blog/executive-ghostwriting

## Pendientes de verificar (búsqueda agotada en esta sesión)

- Pagos de Beehiiv Ad Network a cuentas argentinas.
- Si LinkedIn penaliza en 2026 posts detectados como IA.
- Tarifas 2026 en pesos de community managers y servicios de creatividades en AR (encuesta o listados de Workana).
- Términos de uso comercial vigentes de los generadores de música IA y estado de los litigios.
- Fecha de llegada de TikTok Shop a Argentina (poner alerta).
