# Informe fuente: Olas emergentes de la economía IA + verticales de nicho (2026-10-01)

> Informe crudo de investigación (frente "olas emergentes + verticales + arbitraje geográfico"). Pensado para sintetizarse junto con los otros frentes.
> Marcas: **[PRIMARIA]** = fuente oficial, oferta de empleo real, comunicado o prensa con dato verificable; **[ANECDÓTICO]** = blog, vendedor de herramientas, self-report; **[CONFLICTO]** = la fuente vende algo relacionado con lo que afirma; **[NO VERIFICADO]** = dato de conocimiento previo que no se pudo chequear en esta sesión.

---

## 0. Encabezado y supuestos del usuario

- **Perfil (según el pedido de esta investigación, 2026-10-01):** argentino, cobra desde AR (Payoneer, Mercado Pago, merchant of record). Usa Claude / Claude Code pero **no sabe programar**. Formación/pasantía en ingeniería industrial. Presupuesto < USD 500-1.000. Acepta pasivo, semi-pasivo y activo. Quiere subirse a olas que estén naciendo (2025-2026).
- **Ojo con MEMORY.md:** ahí figura "técnico, puede construir software asistido por IA". Este informe asume el perfil más conservador (no programa) → se castigan las ideas que dependen de construir y mantener software propio.
- **Excluido por el pedido:** agencias de automatización generales, cursos generales, contenido/redes, AI receptionist (lo cubren otros frentes) y los descartes del proyecto (trading bots, TikTok Rewards, afiliados desde cero, música IA, KDP, POD, prompts, GPT Store, RapidAPI).
- **Sinergia a tener en cuenta:** el usuario ya tiene la ficha **"Orden Operativo"** (`ideas/2026-09-07-consultora-mejora-procesos.md`) y el **stack de datos** (Apify + x402). Donde una idea se cruza con eso, se marca.

## 1. Metodología

- 2026-10-01: ~34 búsquedas web + ~12 lecturas de páginas (ofertas de empleo de Mercor, notas de iProfesional/iProUP, agregadores de empleo IA, comunicados de funding).
- **Limitación importante:** el presupuesto de búsquedas web de la sesión se agotó a mitad del relevamiento (límite global de 200 por sesión, compartido con otros agentes). Por eso los verticales **gastronomía, logística, subsidios PyME, Verifactu (España) y nearshoring** tienen evidencia más débil (marcados como tal). Se priorizó verificar con lectura directa los datos más decisivos (requisitos reales de Mercor, pagos agénticos en AR, IA en contadores y RRHH en AR).
- **Señal de demanda usada:** (1) funding reciente de startups del rubro (alguien apostó plata a que el problema existe y paga), (2) ofertas de empleo/gigs activos, (3) regulación nueva con fecha, (4) lanzamientos de big tech que crean necesidad de implementación.
- **Regla de escepticismo:** funding en EE.UU. ≠ cliente pagador en AR. Las tarifas de EE.UU. se traducen a LATAM dividiendo por 3-10. Fuentes que venden la herramienta o el curso se marcan [CONFLICTO].
- **Score 1-10:** realista **para este usuario** (no programa, poco capital, AR, quiere ganar bien), pondera los 7 criterios de CLAUDE.md; para servicios no se castiga la falta de pasividad (nota 2026-09-07).

---

## 2. Contexto macro (datos que atraviesan varias ideas)

1. **Anthropic empuja la adopción en PyMEs y vía partners.** "Claude for Small Business" lanzado el **2026-05-13**: 15 workflows agénticos + 10+ conectores (QuickBooks, PayPal, HubSpot), sin costo extra sobre la suscripción ([pasqualepillitteri.it](https://pasqualepillitteri.it/en/news/2524/claude-for-small-business-anthropic-smb-2026)) [ANECDÓTICO, coincide con varias fuentes]. **Claude Partner Network** lanzado en **marzo 2026** con USD 100M; 4 niveles; membresía gratis; >40.000 firmas aplicaron en 3 meses; el nivel Select exige 10 profesionales certificados + 2 clientes en producción ([kanerika.com](https://kanerika.com/blogs/claude-partner-network/), [channelinsider.com](https://www.channelinsider.com/ai/anthropic-claude-partner-network-launch/)). → Hay demanda de "implementadores", pero la big tech está armando su propio canal: el freelance chico compite con un ecosistema subsidiado.
2. **Demanda de "aplicar IA en el trabajo" en plataformas freelance:** Upwork reporta +109% interanual en skills de aplicación de IA, +178% "AI integration" (citado por [ruul.io](https://ruul.io/blog/freelance-ai-consultant-rates)) [ANECDÓTICO]. El dato "LinkedIn: AI implementation specialist +312%" de la misma fuente **no pudo verificarse** — no usarlo.
3. **Forward deployed engineers (FDE):** postings en Indeed de 643 (abr-2023) a 5.330 (abr-2026); Lightcast: +1.000% ene-ago 2026 vs 2025 ([bloomberry.com](https://bloomberry.com/blog/i-analyzed-1000-forward-deployed-engineer-jobs/), [algeriatech.news](https://algeriatech.news/the-forward-deployed-engineer-boom-800-growth-and-the-career-pivot-of-2026/)). Son roles de ingeniería full-time → la ola es real, pero el usuario entra por la versión no-técnica (implementación/adopción), no como FDE.
4. **Mercado de "datos expertos" bifurcado:** generalistas en caída (Outlier bajó de ~USD 50/h a ~USD 20/h efectivos en dic-2025; baneos automáticos; Scale despidió 500 contratistas en jul-2025), expertos en auge (USD 45-250/h). Mercor: run-rate bruto USD 2.000M, tarifa promedio contratada ~USD 122/h (jul-2026), pero con 5 demandas por clasificación de contratistas ([breakingeven.online](https://breakingeven.online/newsletter/2026-04-08), [herohunt.ai](https://www.herohunt.ai/blog/mercor-2026-how-it-works-pay-alternatives/)) [ANECDÓTICO, newsletter del rubro].
5. **EU AI Act se corrió:** el "Digital Omnibus" (acuerdo 2026-05-07, en vigor 2026-07-27) posterga obligaciones de alto riesgo a **2027-12-02** (Anexo III) y **2028-08-02** (Anexo I) ([secureprivacy.ai](https://secureprivacy.ai/blog/eu-ai-act-digital-omnibus-the-new-high-risk-ai-deadlines-after-council-approval), [holisticai.com](https://www.holisticai.com/blog/eu-ai-acts-deadline-moved-2027)). Muchos blogs todavía venden "el deadline de agosto 2026" — información vencida.
6. **Pagos agénticos llegaron a Argentina:** primer caso concreto **MODO + Frávega dentro de ChatGPT, 2026-09-23**; Visa y Mastercard hicieron pilotos en vivo en 2026 con Santander, Nación, Galicia, Itaú (Mastercard pagó dentro de ChatGPT vía Pomelo); Tiendanube lanzó Lumi y Chat Nube; Mercado Pago, asistente con 100+ funciones ([iproup.com 2026-08-12](https://www.iproup.com/finanzas/70397-mercado-libre-tiendanube-y-tarjetas-ya-prueban-compras-agenticas-en-argentina.amp), [diegoceredi.com 2026-09-25](https://www.diegoceredi.com/blog/pagos-agenticos-argentina-mercado-libre-tiendanube)). Contrapeso: en EE.UU. el ACP de OpenAI tenía **~30 comercios Shopify vivos en feb-2026** según Forrester ([naturaily.com](https://naturaily.com/blog/agentic-commerce-shopify-guide) / [explodingtopics.com](https://explodingtopics.com/blog/agentic-commerce-protocol)); x402 mueve ~USD 28.000/día pese a 160M+ transacciones ([kucoin.com](https://www.kucoin.com/news/flash/coinbase-processes-1t-in-stablecoin-payments-annually-x402-hits-160m-transactions), [cointelegraph / a16z](https://regional-front.cointelegraph.com/news/ai-agent-payment-volume-closer-to-1-6m-says-a16z)). → Ola real en titulares, chica en dólares.

---

## 3. Lista de ideas (38)

Formato por idea: **Qué es** · **Evidencia/señal** · **Cobro y precio** · **Ejecución con Claude sin programar** · **Tipo / h/sem en régimen** · **Capital / 1er dólar** · **Viabilidad AR** · **Riesgos/escepticismo** · **Ventana** · **Score**.

### A. Trabajos y servicios nuevos creados por la IA

#### 1. Evaluador/entrenador de modelos en español (Mercor, Micro1, Turing, Meridial, etc.)
- **Qué es:** contratista que evalúa respuestas de LLMs, escribe prompts difíciles, rubricas y datos "de referencia" en español (incluido rioplatense).
- **Evidencia:** Mercor "Spanish Linguistic Expert" USD 50/h, pago semanal por Stripe o Wise, horario libre, sin título formal exigido ([work.mercor.com](https://work.mercor.com/jobs/list_AAABlzm1ivVlu6gNwf5KAb6V/spanish-linguistic-expert)) [PRIMARIA]; "Spanish Language Specialist" LATAM USD 25/h, 10-20 h/sem ([remotive.com](https://remotive.com/remote/jobs/all-others/spanish-language-specialist-5019511)) [PRIMARIA]. Agregador [aitrainer.work](https://aitrainer.work/jobs/argentina) al 2026-10-01: **929 ofertas abiertas para Argentina**, mediana USD 70/h (Micro1 311, SME Careers 221, Ethos 207, Turing 114, Mercor 33) [ANECDÓTICO, agregador; la mediana mezcla roles expertos que el usuario no califica].
- **Cobro:** USD 25-60/h para lingüística/generalista bilingüe; pago semanal.
- **Ejecución:** no requiere programar; requiere inglés escrito bueno, exámenes de ingreso (assessments) y constancia. Claude ayuda a prepararse, NO a hacer las tareas (las plataformas detectan y banean uso de IA en las respuestas).
- **Tipo:** activo (horas por plata). 10-20 h/sem.
- **Capital:** 0. **1er dólar:** 2-6 semanas (screening de Mercor puede tardar 3+ semanas).
- **Viabilidad AR:** buena en la práctica (hay ofertas listadas para AR). Riel: Stripe Connect / Wise → **verificar en el onboarding**; Wise históricamente no abre cuentas a residentes argentinos [NO VERIFICADO]; Payoneer como fallback según plataforma.
- **Riesgos:** sequías de proyectos, recortes de tarifa sin aviso (caso Outlier dic-2025), baneos automáticos, demandas por clasificación laboral (Mercor), trabajo que entrena a la IA que lo reemplaza. No construye activo propio.
- **Ventana:** 1-3 años para expertos; la parte generalista ya se está cerrando.
- **Score: 7/10** — mejor "puente de caja" en dólares sin capital ni código; no es un negocio.

#### 2. Experto de dominio (ingeniería industrial / supply chain) para evaluación de IA
- **Qué es:** igual que #1 pero vendiendo el conocimiento de ingeniería industrial.
- **Evidencia:** Mercor "Industrial Engineers" USD 70-110/h; "Supply Chain Expert" USD 60-70/h; "Manufacturing Operations" y "Logistics Consultant" hasta USD 110/h ([work.mercor.com IE](https://work.mercor.com/jobs/list_AAABoCWbRrO5te8zK09LMLK-/industrial-engineers), [jobgether](https://jobgether.com/offer/6a235dcef8af0ea2c408acf2-logistics-consultant-upto-110-hr)) [PRIMARIA].
- **Pero (dato decisivo, leído 2026-10-01):** el rol de Industrial Engineers exige **4+ años de experiencia, solo residentes de EE.UU., 20+ h/sem**.
- **Cobro:** USD 60-110/h. **Ejecución:** sin código. **Tipo:** activo.
- **Viabilidad AR:** **hoy no** para este perfil (pasantía, no 4 años; geo-restringido). Re-chequear cada 2-3 meses: Micro1/Turing a veces abren por región.
- **Riesgos:** los mismos que #1. **Ventana:** 1-3 años.
- **Score: 3/10 hoy** (sube a 7 si aparece un rol LATAM con requisitos alcanzables).

#### 3. Red teaming de IA (jailbreaks, seguridad de modelos)
- **Evidencia:** contratistas USD 100-200/h ([theinterviewguys](https://blog.theinterviewguys.com/?p=12745)) [ANECDÓTICO]; desafío HackerOne sobre Claude: 339 investigadores, 300.000 interacciones, USD 55.000 repartidos entre 4 equipos ([hackerone.com](https://www.hackerone.com/blog/emerging-playbook-ai-red-teaming-hackerone)) [PRIMARIA].
- **Cobro:** bounties (todo o nada) o contrato por hora para perfiles de seguridad.
- **Ejecución:** no requiere programar para jailbreaks de texto, pero sí creatividad y mucha práctica; ganan pocos.
- **Tipo:** activo / lotería. **Capital:** 0. **1er dólar:** incierto (meses o nunca).
- **Viabilidad AR:** HackerOne paga a AR (Payoneer/PayPal históricamente) [NO VERIFICADO 2026].
- **Riesgos:** distribución tipo torneo (4 de 339 cobraron). **Ventana:** larga, pero profesionalizándose.
- **Score: 3/10.**

#### 4. Implementador de Claude / Claude Cowork para equipos no técnicos (PyMEs y profesionales hispanohablantes)  ⭐
- **Qué es:** "llave en mano" de adopción: configurar Claude (Team/Pro) + Projects + conectores + Skills para un equipo; capacitar en 2-4 sesiones; dejar 3-5 flujos funcionando (propuestas, informes, atención por mail, conciliaciones, etc.). Variante: cohortes en español para profesionales.
- **Evidencia:** Claude for Small Business (2026-05-13) trae workflows listos → alguien tiene que configurarlos y enseñarlos; Cowork Academy (comunicado **2026-07-06**) apunta exactamente a no-devs: dueños de agencia, contadores, inmobiliarios ([accessnewswire](https://www.accessnewswire.com/newsroom/en/business-and-professional-services/cowork-academy-guided-claude-cowork-training-early-admission-now-1186878)) [PRIMARIA, sin precio]; gigs de "Claude Cowork training" activos en Fiverr y Upwork ([fiverr wallex_5](https://br.fiverr.com/wallex_5/be-claude-cowork-expert-coaching-for-non-technical-users-and-team-workflows), [upwork](https://www.upwork.com/services/product/development-it-claude-cowork-training-claude-ai-live-coaching-sessions-in-claude-desktop-2046652695562212073)); aivancity/hackceleration: 300+ personas capacitadas en Francia/Europa ([hackceleration](https://hackceleration.com/training/claude-cowork)) [ANECDÓTICO]; workshop "Claude for Small Business" de OmbuLabs ([ombulabs.ai](https://www.ombulabs.ai/workshops/claude-for-small-business)).
- **Cobro y precio:** paquete de implementación USD 300-1.500 (LATAM) / USD 1.500-5.000 (EE.UU./España); retainer de soporte USD 150-600/mes; taller grupal USD 30-80 por persona. (Rangos estimados a partir de tarifas freelance USD 75-200/h de [theaiconsultingnetwork](https://www.theaiconsultingnetwork.com/blog/ai-consulting-small-businesses-cost-how-it-works) [ANECDÓTICO] ajustadas a LATAM.)
- **Ejecución sin programar:** es justamente el caso de uso de Cowork/Projects/Skills (texto, no código). Claude prepara el diagnóstico, los manuales y las Skills. El método de ingeniería industrial (relevar proceso → medir → rediseñar) es el diferencial.
- **Tipo:** activo → semi-pasivo si se productiza (paquete fijo + biblioteca de Skills reutilizable). 10-20 h/sem con 3-6 clientes.
- **Capital:** USD 0-100 (suscripción Claude propia + dominio). **1er dólar:** 3-8 semanas (primer cliente por red propia).
- **Viabilidad AR:** alta. Clientes AR pagan en ARS (Mercado Pago); EE.UU./España vía Payoneer/merchant of record. Encaja con Factura E.
- **Riesgos:** (1) Anthropic y la Partner Network (Accenture, Deloitte, KPMG) bajan al SMB con producto cada vez más autoconfigurable → el valor de "configurar" cae; (2) si un cliente usa ChatGPT/Gemini/Copilot hay que ser agnóstico; (3) muchos "consultores IA" sin casos → hay que mostrar resultados medibles; (4) datos sensibles del cliente (acuerdos de confidencialidad).
- **Ventana:** 18-36 meses como servicio de configuración; después sobrevive el que vende **rediseño de procesos + adopción** (lo humano), no la configuración.
- **Sinergia:** es la puerta de entrada natural a la ficha "Orden Operativo".
- **Score: 8/10.**

#### 5. Constructor de Claude Skills a medida (empaquetar el know-how de una empresa)
- **Qué es:** convertir procedimientos internos (cómo cotizamos, cómo respondemos reclamos, formato de informes, voz de marca) en Skills reutilizables; venta por skill o por paquete.
- **Evidencia:** marketplaces de Skills con 30.000-500.000 entradas, catálogo abierto ([agent37.com](https://www.agent37.com/blog/claude-skills-marketplace), [intempt.com](https://intempt.com/blog/claude-skills-marketplace)) [ANECDÓTICO]; guías para freelancers sobre vender Skills ([useme.com](https://useme.com/en/blog/how-to-use-claude-skills/)).
- **Cobro:** USD 100-500 por skill a medida; paquete de 5 skills + capacitación USD 500-1.500.
- **Ejecución:** las Skills básicas son Markdown + instrucciones; Claude las escribe. Sin código para la mayoría.
- **Tipo:** activo, productizable. 5-15 h/sem.
- **Capital:** 0. **1er dólar:** 2-6 semanas.
- **Viabilidad AR:** alta.
- **Riesgos:** las Skills genéricas valen ~0 (hay cientos de miles gratis) → solo vale lo específico del cliente; Anthropic puede generar Skills automáticamente desde la conversación.
- **Ventana:** 12-24 meses como servicio separado; conviene venderlo como parte de #4.
- **Score: 7/10** (como complemento de #4; solo, 5/10).

#### 6. Responsable de IA fraccional ("fractional AI lead") para PyMEs LATAM
- **Evidencia:** en EE.UU. retainers USD 8.000-25.000/mes por 2 días/semana ([betonai.net](https://betonai.net/ai-consulting-rate-card-2026-what-to-charge-for-strategy-implementation-and-fractional-ai-leadership-real-rates-from-68-consultants/), [hatchworks](https://hatchworks.com/blog/gen-ai/fractional-chief-ai-officer/)) [CONFLICTO: venden el servicio].
- **Cobro LATAM realista:** USD 400-1.500/mes por 4-8 h/sem.
- **Ejecución:** sin código; requiere credibilidad y casos.
- **Tipo:** activo. 4-8 h/sem por cliente.
- **Capital:** 0. **1er dólar:** 2-4 meses (requiere casos previos de #4).
- **Viabilidad AR:** media (el dueño de PyME argentina no compra "CAIO"; compra "alguien que me ordene esto").
- **Riesgos:** sin trayectoria no se vende; es la etapa 2 de #4, no una idea de arranque.
- **Ventana:** 2-4 años. **Score: 6/10** (como evolución de #4).

#### 7. Kit de política de uso de IA + control de "shadow AI" para PyMEs
- **Qué es:** política de 1-2 páginas + lista de herramientas aprobadas + taller de 1 h + checklist de datos que no se suben; versión template autoservicio.
- **Evidencia:** 81% de trabajadores usa herramientas de IA no aprobadas; 71% en Reino Unido; cuestionarios de renovación de ciber-seguros 2026 preguntan si hay una AUP de IA escrita ([dope.security](https://dope.security/post/ai-acceptable-use-policy), [ifeeltech](https://ifeeltech.com/blog/ai-acceptable-use-policy-small-business)) [ANECDÓTICO/CONFLICTO: vendedores de seguridad].
- **Cobro:** template USD 29-99 (pasivo); implementación + taller USD 200-800.
- **Ejecución:** Claude redacta; sin código. Adaptar a Ley 25.326 (AR) / RGPD (ES).
- **Tipo:** semi-pasivo (template) + activo (taller). 2-5 h/sem.
- **Capital:** < USD 50. **1er dólar:** 2-6 semanas.
- **Viabilidad AR:** media; la presión de aseguradoras es mayormente EE.UU./UK. En AR funciona como "gancho" de #4.
- **Riesgos:** abundan templates gratis; no es diferencial solo.
- **Ventana:** 2-3 años. **Score: 5/10** (6 como lead magnet de #4).

#### 8. Cumplimiento EU AI Act para PyMEs españolas (o LATAM que venden a la UE)
- **Evidencia:** blogs de "deadline agosto 2026" ([firstaimovers](https://radar.firstaimovers.com/eu-ai-act-august-2026-deadline-action-plan-smes)) **desactualizados**: el Omnibus movió alto riesgo a 2027-12-02 ([holisticai.com](https://www.holisticai.com/blog/eu-ai-acts-deadline-moved-2027)). Quedan vigentes obligaciones de transparencia (Art. 50: avisar al usuario que habla con una IA / contenido generado) — alcance exacto post-Omnibus **[NO VERIFICADO en detalle]**.
- **Cobro:** inventario de usos de IA + clasificación de riesgo USD 500-3.000 en España.
- **Ejecución:** documental, sin código; pero el cliente espera firma de abogado/DPO.
- **Tipo:** activo. **Capital:** bajo. **1er dólar:** 2-4 meses.
- **Viabilidad AR:** baja-media (vender a España sin presencia ni credencial legal).
- **Riesgos:** urgencia evaporada hasta fines de 2027; competencia de despachos y consultoras RGPD que ya tienen la cartera.
- **Ventana:** se reabre en 2027 (antes de 2027-12-02). **Score: 3/10.**

#### 9. Conectores MCP para sistemas argentinos (producto) o a medida (servicio)
- **Qué es:** servidores MCP que conectan Claude/ChatGPT con software local (Colppy, Xubio, Tango, Tiendanube, ARCA vía terceros) — que el contador o el comerciante "le pregunte a Claude" por sus datos.
- **Evidencia:** >10.000 servidores MCP indexados a inicios de 2026; freelancers cobran USD 5.000-15.000 por MCP a medida; MCP donado a la Agentic AI Foundation (Linux Foundation) en dic-2025 ([aibusiness.vc](https://aibusiness.vc/startups/mcp-servers-business-opportunity), [medium MCP](https://medium.com/mcp-server/the-rise-of-mcp-protocol-adoption-in-2026-and-emerging-monetization-models-cb03438e985c)) [ANECDÓTICO/CONFLICTO: cursos de MCP].
- **Cobro:** suscripción USD 10-40/mes por conector hosteado; a medida USD 500-3.000 en LATAM.
- **Ejecución:** **requiere código** (Claude Code lo escribe, pero mantenerlo, seguridad y credenciales de clientes son responsabilidad seria). Cloudflare (ya conectado) sirve de hosting.
- **Tipo:** semi-pasivo (producto). 3-6 h/sem.
- **Capital:** < USD 100. **1er dólar:** 2-4 meses.
- **Viabilidad AR:** buena (nadie localiza esto para software argentino) — **[evidencia de demanda local: débil, no verificada]**.
- **Riesgos:** los propios proveedores (Colppy, Tiendanube) sacan su MCP oficial y te borran; responsabilidad por manejo de credenciales y datos fiscales.
- **Ventana:** 6-18 meses antes de que los SaaS locales publiquen el suyo. **Score: 5/10** para un no-programador (7 si programara). Sinergia con stack de datos.

#### 10. "Catálogo listo para agentes": preparar tiendas Tiendanube / Mercado Libre para compras agénticas  ⭐
- **Qué es:** auditoría + limpieza de catálogo (títulos, atributos, stock sincronizado, políticas de envío/devolución estructuradas, medios de pago tokenizables) para que un agente (ChatGPT, asistente de Mercado Pago) pueda leer, comparar y comprar. Mantenimiento mensual.
- **Evidencia:** MODO + Frávega en ChatGPT 2026-09-23; pilotos Visa/Mastercard con 4 bancos AR; Tiendanube Lumi + Chat Nube ([iproup 2026-08-12](https://www.iproup.com/finanzas/70397-mercado-libre-tiendanube-y-tarjetas-ya-prueban-compras-agenticas-en-argentina.amp)); ya hay consultores ofreciéndolo con ese checklist ([diegoceredi.com 2026-09-25](https://www.diegoceredi.com/blog/pagos-agenticos-argentina-mercado-libre-tiendanube)). E-commerce AR 2025: ARS 15,1 billones (~USD 13.000M).
- **Cobro:** auditoría USD 100-400; limpieza de catálogo por SKU (USD 0,30-1/SKU) o paquete; mantenimiento USD 50-150/mes.
- **Ejecución:** sin código: exportar catálogo a planilla, Claude normaliza atributos y redacta, reimportar. Muy "ingeniería industrial" (maestro de artículos = orden operativo digital).
- **Tipo:** activo con componente recurrente. 5-15 h/sem.
- **Capital:** 0. **1er dólar:** 3-6 semanas.
- **Viabilidad AR:** alta, cliente local, cobro por Mercado Pago.
- **Riesgos:** **hype**: en EE.UU. el ACP tenía ~30 comercios vivos en feb-2026; las plataformas (Tiendanube, ML) pueden autocompletar atributos con su propia IA; el vendedor pyme no paga por algo que todavía no le trae ventas. Vender por el beneficio de hoy (mejor posicionamiento en ML/buscadores, menos devoluciones), no por "agentes".
- **Ventana:** 12-24 meses.
- **Sinergia:** directa con "Orden Operativo" (maestro de SKUs). **Score: 6,5/10.**

#### 11. Endpoints pagos por agentes (x402) — vender datos a agentes
- **Evidencia:** x402 160M+ transacciones, Stripe/Cloudflare/Vercel integrados, Google lo embebe en AP2; pero ~USD 28.000/día de volumen total (ver contexto macro).
- **Cobro:** micro-pagos USDC por llamada (USD 0,001-0,05).
- **Ejecución:** requiere código; ya está en el plan del stack de datos.
- **Tipo:** pasivo. **Capital:** bajo. **1er dólar:** meses; montos chicos.
- **Viabilidad AR:** cobro en USDC (cripto) → conversión vía exchange; legal pero con fricción.
- **Riesgos:** volumen ínfimo hoy; es apuesta de opción, no ingreso.
- **Ventana:** larga (2027+). **Score: 3/10 como idea separada** (mantener como "boca extra" del stack de datos, no más).

#### 12. Visibilidad en respuestas de IA (GEO) para negocios locales/profesionales hispanos
- **Evidencia:** "geo agency" búsquedas +2.300% interanual ([llmpulse.ai](https://llmpulse.ai/blog/geo-agency-guide/)) [CONFLICTO: vende herramienta GEO]; agencias USD 1.500-50.000/mes, herramientas USD 10-1.000/mes ([webfx.com](https://www.webfx.com/blog/ai/generative-engine-optimization-cost/)) [CONFLICTO: agencia].
- **Cobro LATAM:** auditoría "¿te recomienda ChatGPT?" USD 50-200; mensual USD 100-400.
- **Ejecución:** sin código: consultas sistemáticas a varios LLMs, ficha de Google Business, reseñas, páginas FAQ. Claude ayuda a redactar.
- **Tipo:** activo/recurrente. **Capital:** < USD 50/mes (herramienta de tracking). **1er dólar:** 1-2 meses.
- **Viabilidad AR:** media.
- **Riesgos:** medición difusa (respuestas no deterministas), solapa con el frente SEO/contenido, mucho "humo".
- **Ventana:** 2-3 años. **Score: 5/10.**

#### 13. "AI operations" remoto part-time para startups/agencias de EE.UU. (versión no técnica del FDE)
- **Qué es:** rol de operaciones que mantiene flujos con IA (Claude/ChatGPT/Zapier sin código), documenta procesos, hace QA.
- **Evidencia:** boom FDE (+729-1.000%), pero son ingenieros; la demanda no técnica aparece como "AI operations associate/specialist" en job boards [evidencia débil en esta sesión].
- **Cobro:** USD 15-35/h desde LATAM.
- **Ejecución:** sin código; inglés fluido.
- **Tipo:** activo (empleo encubierto). 20-40 h/sem.
- **Capital:** 0. **1er dólar:** 1-3 meses de búsqueda.
- **Viabilidad AR:** alta (contractor vía Deel/Payoneer).
- **Riesgos:** es empleo, no negocio; competencia de toda LATAM.
- **Ventana:** 2-4 años. **Score: 5/10.**

#### 14. Evaluación/QA de chatbots y agentes en español (evals para empresas que despliegan IA)
- **Qué es:** armar sets de prueba (100-300 casos), rubricas y reportes de fallas para chatbots/agentes en español de agencias o SaaS (EE.UU., España, LATAM); re-test mensual.
- **Evidencia:** Mercor paga a expertos para escribir rubricas y escenarios ("Supply Chain Expert": diseñar escenarios y rúbricas) → el mismo trabajo lo necesitan las empresas que despliegan agentes; boom de agentes de cobranza/recepción en español (Callbook YC S26, Colektia, Mozart, ver #24).
- **Cobro:** USD 300-1.500 por evaluación; USD 150-500/mes re-test.
- **Ejecución:** sin código (planillas + Claude para generar y puntuar casos).
- **Tipo:** activo, productizable. 5-10 h/sem.
- **Capital:** 0. **1er dólar:** 1-3 meses.
- **Viabilidad AR:** alta (arbitraje de idioma y cultura rioplatense/latina).
- **Riesgos:** herramientas de evals automáticas (LLM-as-judge) comprimen el valor; venta difícil (el cliente no sabe que lo necesita hasta que su bot falla en público). **[Demanda directa: evidencia débil]**.
- **Ventana:** 2-3 años. **Score: 6/10.**

#### 15. Diagnóstico "IA-ready" productizado (assessment de 1 semana a precio fijo)
- **Qué es:** relevamiento de procesos + mapa de oportunidades de IA + plan de 90 días, precio fijo.
- **Evidencia:** en EE.UU. los assessments básicos arrancan en USD 2.000 y la mayoría de las PyMEs gasta USD 10.000-50.000 en proyectos iniciales ([theaiconsultingnetwork](https://www.theaiconsultingnetwork.com/blog/ai-consulting-small-businesses-cost-how-it-works)) [CONFLICTO].
- **Cobro AR:** USD 200-600 por diagnóstico (descontable si contrata implementación).
- **Ejecución:** sin código; método de ingeniería industrial.
- **Tipo:** activo. **Capital:** 0. **1er dólar:** 1-2 meses.
- **Viabilidad AR:** alta. **Riesgos:** "diagnóstico gratis" de competidores; es el embudo de #4, no algo separado.
- **Ventana:** 2-4 años. **Score: 6/10** (ya cubierto por la ficha "Orden Operativo"; acá solo se confirma que el formato existe y se cobra).

#### 16. Limpieza y orden de datos para que la IA sirva ("AI-ready data") en PyMEs
- **Qué es:** ordenar Drive/planillas/maestros de clientes y productos para que Claude/Copilot los pueda usar (nomenclaturas, una sola fuente de verdad, plantillas).
- **Evidencia:** el checklist agéntico (catálogo limpio, stock sincronizado) y el pitch de Genio Contable ("la precisión depende de las herramientas alrededor del modelo") muestran que el cuello de botella son los datos, no el modelo. **[Demanda directa: evidencia débil en esta sesión]**.
- **Cobro:** USD 200-1.000 por proyecto.
- **Ejecución:** sin código (planillas + Claude). **Tipo:** activo. **Capital:** 0. **1er dólar:** 1-2 meses.
- **Viabilidad AR:** alta. **Riesgos:** difícil de vender como tal; venderlo dentro de #4/#10.
- **Ventana:** larga. **Score: 5,5/10** (6,5 dentro del paquete Orden Operativo).

### B. Verticales de nicho (LATAM / Argentina)

#### 17. IA para estudios contables argentinos (implementación + capacitación)  ⭐
- **Qué es:** configurar Claude (Projects con normativa vigente, Skills de papeles de trabajo, plantillas de mails a clientes, conciliaciones de planillas) en estudios de 1-10 personas; talleres para contadores.
- **Evidencia:** Genio Contable (startup AR, nota **2026-05-16**) promete -83% del trabajo operativo impositivo, reconciliando con ARCA/AGIP/ARBA; una empresa mediana argentina dedica ~311 h/año a cumplimiento fiscal, casi el doble que países desarrollados ([iprofesional.com](https://www.iprofesional.com/impuestos/454685-son-argentinos-y-crearon-una-ia-que-permite-liquidar-impuestos-facil-como-funciona)) [PRIMARIA, prensa]; Aconpy ofrece bots (login ARCA, alertas fiscales, APOC, monotributo) ([blogdelcontador](https://blogdelcontador.com.ar/news-46465-aconpy-el-primer-y-unico-sistema-contable-argentino-que-implemento-ia-en-sus-procesos)); Errepar prepara "Consultor IA" (nota **2026-08-06**) — la nota menciona **controversia en el sector por IA sin supervisión en temas impositivos** ([iprofesional](https://www.iprofesional.com/impuestos/461683-errepar-prepara-el-lanzamiento-de-consultor-ia-el-asistente-de-ia-para-contadores)).
- **Cobro:** implementación USD 200-600 por estudio; mensual USD 50-200; taller USD 15-40 por asistente (vía consejos profesionales o por cuenta propia).
- **Ejecución:** sin código (Projects/Skills); el valor está en conocer el flujo del estudio (relevamiento = ingeniería industrial).
- **Tipo:** activo + semi-pasivo (pack de Skills, ver #18). 8-15 h/sem.
- **Capital:** < USD 100. **1er dólar:** 1-2 meses.
- **Viabilidad AR:** alta; mercado grande y conocido; pago en ARS (inflación → indexar).
- **Riesgos:** Errepar/Tango/Colppy/Aconpy integran IA nativa con la normativa ya cargada → el estudio prefiere la herramienta de su proveedor; alucinaciones en temas fiscales = responsabilidad (posicionar como asistente con supervisión, nunca como "liquidador").
- **Ventana:** 12-24 meses antes de que el software contable lo traiga todo integrado. **Score: 7/10.**

#### 18. Pack de Skills/plantillas para contadores y monotributistas (producto digital)
- **Qué es:** paquete descargable de Skills/prompts estructurados para Claude (recategorización de monotributo, armado de papeles de trabajo, mails estándar a clientes, checklist de vencimientos).
- **Evidencia:** misma demanda que #17; formato Skills es texto (ver #5).
- **Cobro:** USD 15-60 por pack (Hotmart / Mercado Pago); actualización anual paga.
- **Ejecución:** sin código. **Tipo:** semi-pasivo; 2-4 h/sem (actualización normativa constante).
- **Capital:** < USD 50. **1er dólar:** 1-2 meses.
- **Viabilidad AR:** alta. **Riesgos:** linda frontera con "prompts" (descartado en el proyecto) — solo funciona como complemento de #17 con distribución propia; normativa cambia y el pack vence.
- **Ventana:** 12-24 meses. **Score: 5/10.**

#### 19. Licitaciones públicas: alertas + resumen de pliegos con IA para PyMEs proveedoras  ⭐
- **Qué es:** monitoreo de COMPR.AR, portales provinciales y municipales filtrado por rubro; resumen de pliego en 1 página (requisitos, garantías, fechas); opcional: armado del sobre/oferta.
- **Evidencia:** prototipos y SaaS de alertas con IA para facilitar a PyMEs el acceso a compras públicas (AR/LATAM), startup argentina usando IA sobre datos de licitaciones ([ecosistemastartup](https://ecosistemastartup.com/startup-argentina-usa-ia-contra-corrupcion-en-licitaciones-publicas/), [UBA](https://bibliotecadigital.economicas.uba.ar/bitstreams/0e7c6ce9-c183-4d7e-a986-26f551ce46b2/download)); ChileCompra licitó IA para compras públicas (2025-08) ([chilecompra.cl](https://www.chilecompra.cl/2025/08/chilecompra-lanza-licitacion-inedita-para-aplicar-inteligencia-artificial-en-compras-publicas-y-fortalecer-lucha-anticorrupcion/)). **[Competencia comercial existente en AR no relevada a fondo — hay servicios de alertas de licitaciones desde hace años; verificar antes de decidir.]**
- **Cobro:** alertas USD 15-60/mes por rubro; resumen de pliego USD 10-30 c/u; armado de oferta USD 100-500 o % de éxito.
- **Ejecución:** las alertas requieren scraping (Apify/actores existentes o Claude Code) → **semi-técnico**; el resumen de pliegos es sin código (Claude lee PDF).
- **Tipo:** semi-pasivo (alertas) + activo (ofertas). 3-8 h/sem.
- **Capital:** < USD 100. **1er dólar:** 1-3 meses.
- **Viabilidad AR:** alta; cliente local; cobro Mercado Pago.
- **Riesgos:** portales cambian/bloquean; competidores de alertas ya establecidos; el valor real está en el armado de la oferta (horas humanas).
- **Ventana:** larga (el Estado compra siempre); la parte "IA" se commoditiza en 1-2 años.
- **Sinergia:** fuerte con el stack de datos (scraping + alertas). **Score: 7/10.**

#### 20. IA para estudios jurídicos chicos (implementación)
- **Evidencia:** Enter (Brasil) USD 100M Serie B a USD 1.200M de valuación, primer unicornio IA de LATAM (mayo 2026) ([gtlaw.com](https://www.gtlaw.com/es/news/2026/05/press-releases/greenberg-traurig-represents-enter-in-$100m-series-b--creating-latin-americas-first-ai-unicorn)) [PRIMARIA]; Magnar (Chile) USD 8M Serie A con participación del estudio argentino Beccar Varela ([globallegalpost](https://www.globallegalpost.com/news/chilean-legal-ai-platform-start-up-magnar-raises-8m-in-series-a-funding-round-1219078957)) [PRIMARIA].
- **Cobro:** USD 200-800 implementación + USD 50-200/mes.
- **Ejecución:** sin código (Projects con modelos de escritos, revisión de contratos, resúmenes de expedientes).
- **Tipo:** activo. **Capital:** bajo. **1er dólar:** 2-3 meses.
- **Viabilidad AR:** media: abogados conservadores, secreto profesional, datos sensibles.
- **Riesgos:** Magnar/Enter y herramientas de editoriales jurídicas (La Ley/Thomson Reuters) ocupan el espacio; el usuario no es abogado → baja credibilidad.
- **Ventana:** 12-24 meses. **Score: 5/10.**

#### 21. Kit IA para inmobiliarias (descripciones, tasación comparativa, seguimiento de leads)
- **Evidencia:** CAMESI: 36% de inmobiliarias AR usaba IA en 2024 (10% en 2022) ([mercado.com.ar](https://mercado.com.ar/ruta-digital/la-adopcion-de-inteligencia-artificial-en-empresas-inmobiliarias-argentinas-alcanza-el-36-en-2024)); LIDZ.ai consolidando PropTech (compra de Leadnamics) ([revistaeconomia](https://www.revistaeconomia.com/redefinidiendo-la-venta-inmobiliaria-con-ia-lidz-ai-suma-a-argentina-y-llegaria-a-mas-paises-de-la-region/)); Zonaprop proyecta sumar IA ([mercado.com.ar](https://mercado.com.ar/ruta-digital/zonaprop-amplio-su-base-a-mas-de-11-000-clientes-en-una-decada)).
- **Cobro:** USD 50-200/mes o implementación USD 200-500.
- **Ejecución:** sin código (Skills de fichas y tasaciones; seguimiento por planilla/CRM).
- **Tipo:** activo/recurrente. **Capital:** bajo. **1er dólar:** 1-2 meses.
- **Viabilidad AR:** alta. **Riesgos:** Zonaprop/Argenprop/Tokko meten la IA en el producto; la parte de leads la cubre el frente "AI receptionist".
- **Ventana:** 12-18 meses. **Score: 5/10.**

#### 22. Back-office IA para consultorios (odontología, kinesiología): confirmaciones, seguimientos, autorizaciones de obras sociales
- **Evidencia:** EE.UU./Europa: Toothy AI (YC) — una clínica dental gasta 160+ h/mes en seguros; Linda AI €2,6M pre-seed (feb-2026); Dentio USD 2,3M (ene-2026); Rondah USD 1,8M ([ycombinator](https://ycombinator.com/companies/industry/Dental), [thesaasnews](https://www.thesaasnews.com/news/linda-ai-raises-2-6m-pre-seed/)) [PRIMARIA].
- **Equivalente AR:** autorizaciones de obras sociales/prepagas, recordatorios, seguimiento de tratamientos. **[Evidencia de demanda local: no relevada]**.
- **Cobro:** USD 50-200/mes por consultorio.
- **Ejecución:** parte sin código (plantillas/flujos), parte requiere integraciones (WhatsApp Business API, agendas) → semi-técnico.
- **Tipo:** semi-pasivo. **Capital:** USD 100-300. **1er dólar:** 2-3 meses.
- **Viabilidad AR:** media. **Riesgos:** datos de salud = sensibles (Ley 25.326); solapa con el frente "AI receptionist"; cada obra social tiene su portal.
- **Ventana:** 2-3 años. **Score: 5/10.**

#### 23. Asistente para productores asesores de seguros (PAS): comparativas de pólizas, propuestas, renovaciones
- **Evidencia:** Cara USD 8M seed, siete cifras de ARR en 7 meses, "90 minutos de trabajo manual → 2 minutos" en comparativas ([pulse2](https://pulse2.com/cara-8-million-raised-for-ai-insurance-brokerage-platform/amp/)); American Growth Insurance ~USD 70M (2026-07-27) ([fintech.global](https://fintech.global/2026/07/27/agi-secures-70m-to-scale-ai-native-insurance-brokerage-model/)); Panora USD 5M; Covera (agentes para brokers) ([dealroom](https://dealroom.co/just-founded/covera/)) [PRIMARIA].
- **Equivalente AR:** el PAS compara cotizaciones de varias aseguradoras, arma propuestas y persigue renovaciones/cobranzas — muy manual. **[Tamaño del mercado de PAS en AR: no relevado]**.
- **Cobro:** USD 30-100/mes por PAS (Skills + plantillas + flujo de renovaciones) o implementación USD 150-400.
- **Ejecución:** sin código para comparativas (Claude lee PDFs de cotización y arma tabla/propuesta); renovaciones con planilla + recordatorios.
- **Tipo:** activo → semi-pasivo. **Capital:** bajo. **1er dólar:** 1-3 meses.
- **Viabilidad AR:** buena; nicho grande, fragmentado y poco atendido por "consultores IA".
- **Riesgos:** cotizadores multicompañía existentes podrían sumar IA; regulación SSN sobre asesoramiento.
- **Ventana:** 18-36 meses. **Score: 6,5/10** — buen ejemplo de "traer al español lo que en EE.UU. ya funciona".

#### 24. Cobranzas asistidas por IA para PyMEs (secuencias WhatsApp/mail, sin voz)
- **Evidencia:** Callbook AI (Colombia) en YC S26; Colektia (Chile) USD 9M; Mozart (Uruguay) llegó a México ([noticiasrcn](https://www.noticiasrcn.com/economia/startup-colombiana-de-ia-para-cobranzas-entra-a-y-combinator-1033737), [forbesargentina](https://www.forbesargentina.com/innovacion/mozart-startup-uruguaya-quiere-reemplazar-call-centers-ia-llego-mexico-proyecta-region-n70956)) [PRIMARIA].
- **Cobro:** 5-15% de lo recuperado o fee mensual USD 50-200.
- **Ejecución:** semi-técnico (WhatsApp Business API + plantillas aprobadas por Meta); mensajes y tono sin código.
- **Tipo:** semi-pasivo. **Capital:** USD 100-300 (mensajería). **1er dólar:** 1-3 meses.
- **Viabilidad AR:** buena (morosidad alta en ciclos de crisis).
- **Riesgos:** legal (trato digno al deudor, Ley de Defensa del Consumidor, hostigamiento), baneo de números de WhatsApp, startups financiadas entrando a AR.
- **Ventana:** 2-3 años. **Score: 5/10.**

#### 25. Reclutamiento asistido por IA para PyMEs y consultoras chicas de RRHH
- **Evidencia:** Bumeran "Reclutamiento y Postulación Digital 2026" (2026-08-20): **46% de especialistas de RRHH en AR ya usa IA**; 55% para avisos, 50% para búsqueda y screening ([ecosistemastartup](https://ecosistemastartup.com/?p=100244)) [PRIMARIA vía prensa]; Selenios (Buenos Aires) USD 1,2M pre-seed ([mercado.com.ar](https://mercado.com.ar/innovacion/selenios-obtiene-us-12-millones-para-expandir-su-plataforma-de-reclutamiento-con-ia-en-latinoamerica)).
- **Cobro:** USD 100-400 por búsqueda (screening + shortlist + guía de entrevista) o fee por puesto cubierto.
- **Ejecución:** sin código (Claude lee CVs con criterios explícitos).
- **Tipo:** activo. **Capital:** 0. **1er dólar:** 1-2 meses.
- **Viabilidad AR:** media-alta. **Riesgos:** sesgo/discriminación (en la UE es alto riesgo, Anexo III); Bumeran/LinkedIn/Selenios integran IA; privacidad de CVs.
- **Ventana:** 12-24 meses. **Score: 5/10.**

#### 26. Comercio exterior: asistente de clasificación NCM + documentación para importadores pyme
- **Evidencia:** RG 5857/2026 actualizó criterios de clasificación NCM; existen herramientas tipo arancely.com (10.330 posiciones NCM con IA) ([arancely](https://www.arancely.com/blog/como-importar-argentina-guia-completa-2026)); OMA "Smart Customs Project" (mar-2025) ([cda.org.ar](https://cda.org.ar/detalle_noticia.php?id=42453)). Apertura importadora 2024-2026 = más importadores chicos nuevos **[dato de volumen no verificado]**.
- **Cobro:** consulta de pre-clasificación USD 10-30; acompañamiento de primera importación USD 100-300 (con despachante aliado).
- **Ejecución:** sin código (Claude + nomenclador + criterios).
- **Tipo:** activo. **Capital:** bajo. **1er dólar:** 1-2 meses.
- **Viabilidad AR:** buena, pero **la intervención del despachante es obligatoria** → modelo correcto: socio/derivador de despachantes, no reemplazo.
- **Riesgos:** error de clasificación = multas para el cliente → responsabilidad; competencia de herramientas existentes.
- **Ventana:** 2-3 años. **Score: 5/10.**

#### 27. Hotelería/cabañas: conversión de consultas a reserva directa + precios dinámicos simples
- **Evidencia:** WeSpeak (Córdoba): +400%, 30 hoteles, proyecta USD 2M en 2026 ([infonegocios](https://infonegocios.info/plus/wespeak-la-startup-que-convierte-chats-en-reservas-hoteleras-crece-400-y-ya-opera-en-30-hoteles-de-cordoba-pueblo-nativo-entre-ellos)); OEATUR: 83,3% de agencias de viaje AR usa IA ([innovaciondigital360](https://www.innovaciondigital360.com/software/erp/el-83-de-las-agencias-de-viajes-argentinas-ya-usa-ia-que-software-esta-transformando-el-turismo-en-2026/)).
- **Cobro:** USD 50-150/mes por complejo.
- **Ejecución:** parte de chat = frente "AI receptionist" (no profundizado); la parte de tarifas/ocupación es planilla + Claude.
- **Tipo:** semi-pasivo. **Capital:** bajo. **1er dólar:** 1-3 meses.
- **Viabilidad AR:** media (estacionalidad). **Riesgos:** WeSpeak y PMS con IA ya están; solapa con otro frente.
- **Ventana:** 18 meses. **Score: 4,5/10.**

#### 28. Construcción: cómputo y presupuesto asistido por IA para constructoras chicas y contratistas
- **Evidencia:** Bobyard USD 35M Serie A (takeoff automático hasta 70%); Attentive.ai USD 30,5M Serie B; Rudus (YC, hormigón); ServiceTitan 2026: 38% de contratistas ve impacto medible de IA (17% en 2025) ([businesswire](https://www.businesswire.com/news/home/20251210946193/en/), [lawnandlandscape](https://www.lawnandlandscape.com/news/attentive-ai-secures-30-million-series-b-funding), [inquirer 2026-08-11](https://www.inquirer.com/business/small-business/artificial-intelligence-small-business-contractors-construction-20260811.html)).
- **Cobro AR:** cómputo + presupuesto por obra USD 50-300; plantillas de presupuesto USD 20-50.
- **Ejecución:** sin código para presupuesto/análisis de precios; el takeoff desde planos con IA requiere herramientas pagas (en inglés).
- **Tipo:** activo. **Capital:** bajo. **1er dólar:** 1-2 meses.
- **Viabilidad AR:** media (inflación hace que actualizar presupuestos sea un dolor real). **[Demanda local no verificada]**.
- **Riesgos:** el usuario no es MMO/arquitecto → credibilidad; responsabilidad por errores de cómputo.
- **Ventana:** 2-3 años. **Score: 4,5/10.**

#### 29. Gastronomía: costeo de recetas, mermas y compras con IA
- **Qué es:** escandallos (costo por plato), control de mermas, sugerido de compras, actualización de precios de carta con inflación.
- **Evidencia:** **débil en esta sesión** (búsquedas agotadas); lógica: inflación AR + márgenes finos + es "orden operativo" puro.
- **Cobro:** implementación USD 150-400 + USD 30-80/mes.
- **Ejecución:** planillas + Claude; sin código.
- **Tipo:** activo/recurrente. **Capital:** 0. **1er dólar:** 1-2 meses.
- **Viabilidad AR:** alta (cliente abundante), pero ticket bajo y alta mortalidad de locales.
- **Riesgos:** software de gestión gastronómica (Fudo, etc.) ya trae costeo [NO VERIFICADO si con IA].
- **Ventana:** larga (problema estructural, no ola). **Score: 5,5/10** (como vertical de "Orden Operativo").

#### 30. Logística/distribuidoras chicas: ruteo, control de entregas y stock con IA
- **Evidencia:** **débil en esta sesión**; MELI anunció agentes IA + robots para logística (MELI Experience 2026) ([iproup](https://www.iproup.com/innovacion/71442-mercado-libre-ya-prueba-agentes-de-ia-y-robots-para-entregas)) — señal de la gran empresa, no de la pyme.
- **Cobro:** USD 200-800 por proyecto.
- **Ejecución:** herramientas de ruteo existentes + planillas + Claude.
- **Tipo:** activo. **Capital:** bajo. **1er dólar:** 1-3 meses.
- **Viabilidad AR:** buena; experiencia Sporting (logística) suma credibilidad.
- **Riesgos:** es la ficha "Orden Operativo" con otro nombre; no es "ola IA" sino problema eterno.
- **Ventana:** larga. **Score: 6/10** (por fit con la experiencia del usuario, no por ola).

#### 31. Capacitación IA para docentes de colegios privados + kit de planificación
- **Evidencia:** CABA formó 26.000+ docentes en IA (nota **2026-04-28**) e incorporó IA en todas las primarias públicas en 2026; Mendoza: 350+ docentes de gestión privada capacitados, diplomatura con UTN en preparación ([buenosaires.gob.ar](https://buenosaires.gob.ar/gcaba_historico/noticias/la-ciudad-ya-formo-mas-de-26000-docentes-en-inteligencia-artificial), [mendoza.gov.ar](https://www.mendoza.gov.ar/prensa/docentes-de-gestion-privada-se-capacitaron-en-inteligencia-artificial/)).
- **Cobro:** jornada institucional USD 150-600; kit de planificación USD 5-20 por docente.
- **Ejecución:** sin código. **Tipo:** activo + semi-pasivo. **Capital:** 0. **1er dólar:** 1-3 meses (calendario escolar: vender en nov-feb).
- **Viabilidad AR:** media: el Estado capacita gratis, presupuesto de colegios bajo.
- **Riesgos:** competencia gratuita estatal y de universidades; es "curso" (lo cubre otro frente).
- **Ventana:** 1-2 años. **Score: 4/10.**

#### 32. Municipios: atención al vecino con IA + digitalización de trámites
- **Evidencia:** Zárate designó a "ZARA" (chatbot) como funcionaria no humana (Decreto 532/25); Funes (Santa Fe) implementó chatbot; CAF impulsa "DesafIA Ciudades" ([palabrasdelderecho](https://www.palabrasdelderecho.com.ar/articulo/6390/ZARA-el-chatbot-que-sera-funcionaria-municipal-no-humana-en-Zarate), [lmneuquen](https://www.lmneuquen.com/neuquen/gaido-expuso-la-feria-del-libro-y-posiciono-neuquen-como-ciudad-lider-innovacion-inteligencia-artificial-n1236886)).
- **Cobro:** contratos USD 500-5.000 vía compras directas/licitación.
- **Ejecución:** requiere integraciones y soporte → no apto sin equipo técnico.
- **Tipo:** activo. **Capital:** bajo, pero ciclo de venta 6-12 meses y pago a 60-180 días.
- **Viabilidad AR:** baja para un individuo (relaciones políticas, garantías, inscripción como proveedor).
- **Riesgos:** cambio de gestión municipal, atraso de pagos.
- **Ventana:** 2-4 años. **Score: 3/10.**

#### 33. Subsidios y financiamiento PyME: monitoreo de convocatorias + redacción de postulaciones con IA
- **Qué es:** alertas de convocatorias (AR: CFI, programas provinciales, bancos públicos; ES: ayudas autonómicas, Kit Consulting) y redacción de la postulación con IA; cobro por éxito.
- **Evidencia:** **débil en esta sesión** (búsquedas agotadas). Lógica: mismo motor que #19 (monitoreo + documentos largos = fuerte de Claude).
- **Cobro:** fee fijo USD 100-400 + 3-8% del monto otorgado.
- **Ejecución:** sin código para redacción; alertas semi-técnicas.
- **Tipo:** activo con picos. **Capital:** 0. **1er dólar:** 2-6 meses (depende de calendarios de convocatoria).
- **Viabilidad AR:** media (oferta de programas en AR es irregular, 2024-2026 con recortes) **[NO VERIFICADO]**.
- **Riesgos:** dependencia de presupuesto público; cobro por éxito = ingreso volátil.
- **Ventana:** larga. **Score: 5/10** (fusionable con #19 como "radar de oportunidades públicas").

### C. Arbitrajes geográficos

#### 34. Implementación de IA en español para PyMEs hispanas de EE.UU.  ⭐
- **Qué es:** #4 + #5 vendidos a dueños hispanohablantes en EE.UU. (contratistas, limpieza, landscaping, talleres, restaurantes, inmobiliarios, preparadores de impuestos), en su idioma, con horarios compatibles desde AR.
- **Evidencia:** Intuit QuickBooks: 86% de dueños/decisores de PyMEs hispanas ya usa IA y 67% quiere usarla más — **dato de agosto 2023, viejo** ([quickbooks.intuit.com](https://quickbooks.intuit.com/r/small-business-data/hispanic-latino-ai/)); principales temores: privacidad, regulación, empleo; brecha idiomática en servicios (hipotecas con IA bilingüe, [Fortune 2025-09-05](https://www.fortune.com/2025/09/05/bilingual-ai-hispanic-homeownership-real-estate-mortgages)). Mercado hispano de EE.UU.: 60M+ personas (dato del pedido; no re-verificado acá).
- **Cobro:** USD 500-2.000 setup + USD 150-500/mes; facturable en USD.
- **Ejecución:** sin código; zoom + Claude. Necesita un canal de adquisición (grupos de Facebook/WhatsApp de emprendedores latinos, cámaras de comercio hispanas, referidos de contadores hispanos).
- **Tipo:** activo → semi-pasivo con productización. 10-20 h/sem.
- **Capital:** USD 50-300. **1er dólar:** 1-3 meses.
- **Viabilidad AR:** alta: cobro Payoneer/Stripe vía merchant of record; Factura E; ventaja horaria (AR = EE.UU. este +1/+2 h).
- **Riesgos:** adquisición en frío es lo difícil (tasas de respuesta bajas, ver ficha consultora); desconfianza a proveedores extranjeros; competencia de miles de "AI agencies" latinas en EE.UU.
- **Ventana:** 2-3 años. **Score: 7/10.**

#### 35. Subcontratista "white label" de implementación IA para agencias de EE.UU./España
- **Qué es:** vender horas de implementación/documentación/QA a agencias que ya tienen clientes (sobre todo los que necesitan entregables en español).
- **Evidencia:** demanda de skills de integración de IA en Upwork +178% (vía ruul.io) [ANECDÓTICO]; agencias GEO/IA cobran USD 1.500-50.000/mes y tercerizan [inferencia].
- **Cobro:** USD 15-40/h o por entregable.
- **Ejecución:** sin código para la mayoría de entregables (documentos, Skills, QA, prompts de sistema).
- **Tipo:** activo. **Capital:** 0. **1er dólar:** 1-2 meses.
- **Viabilidad AR:** alta (Payoneer/Deel). **Riesgos:** dependencia de 1-2 agencias; tarifas presionadas a la baja.
- **Ventana:** 2-3 años. **Score: 6/10.**

#### 36. Localizar al español rioplatense/latino un modelo que funciona en inglés (estrategia, no idea suelta)
- **Patrón:** Cara (seguros) → #23 para PAS; Toothy/Linda (dental) → #22 con obras sociales; Bobyard (construcción) → #28; Callbook/Colektia (cobranzas) → #24. El patrón es válido como **método de búsqueda de nicho**: tomar una startup de EE.UU. con funding 2026, verificar que el dolor existe en AR, ofrecerlo primero como servicio manual asistido por Claude (validación), productizar después.
- **Score:** n/a (meta-idea; aplicado en #22-#28).

#### 37. Verifactu (España): onboarding de autónomos a software de facturación adaptado
- **Qué es:** acompañar a autónomos/micro-pymes españolas a migrar a software que cumpla el reglamento de sistemas de facturación (Verifactu), + automatización de facturas recibidas con IA.
- **Evidencia:** la página de la AEAT ([sede.agenciatributaria.gob.es](https://sede.agenciatributaria.gob.es/Sede/iva/sistemas-informaticos-facturacion-verifactu.html)) referencia RD 1007/2023, RD 254/2025 y una **prórroga de plazos**; según conocimiento previo, la prórroga (fines de 2025) fijó **2027-01-01 para sociedades y 2027-07-01 para el resto** — **[NO VERIFICADO en esta sesión]**.
- **Cobro:** EUR 50-200 por alta/migración + comisiones de afiliado de software.
- **Ejecución:** sin código. **Tipo:** activo estacional. **Capital:** bajo. **1er dólar:** 1-3 meses.
- **Viabilidad AR:** baja-media (vender a España en remoto sin red; las gestorías ya lo cubren).
- **Riesgos:** ola de una sola vez, nuevas prórrogas posibles, competencia de gestorías.
- **Ventana:** hasta mediados de 2027 (si las fechas se confirman). **Score: 3/10.**

#### 38. Cohortes en español de "Claude/Cowork para profesionales" (variante educativa de #4)
- **Evidencia:** Cowork Academy (en inglés, 2026-07-06) y cursos en Francia (300+ alumnos) — no se encontró equivalente fuerte en español rioplatense **[búsqueda específica no realizada; verificar]**.
- **Cobro:** USD 30-150 por cohorte de 4 semanas; B2B in-company USD 300-1.500.
- **Ejecución:** sin código. **Tipo:** semi-pasivo (cohortes grabables). **Capital:** bajo. **1er dólar:** 1-2 meses si hay audiencia; sin audiencia, mucho más.
- **Riesgos:** es "curso" (otro frente), depende de audiencia; Anthropic Academy y YouTube gratuito.
- **Ventana:** 12-18 meses (hasta que el producto sea autoexplicativo). **Score: 5/10** (como canal de adquisición de #4, más que como negocio).

---

## 4. Top 5 del frente

| # | Idea | Por qué | Score |
|---|------|---------|-------|
| 4 | **Implementador de Claude/Cowork para equipos no técnicos** (+ #5 Skills como productización, + #15 diagnóstico como embudo) | Es el único "trabajo nuevo" donde no programar no es desventaja; Anthropic (Claude for Small Business 2026-05-13, Partner Network 2026-03) está creando la necesidad; fit directo con el método de ingeniería industrial y con la ficha Orden Operativo. | 8 |
| 1 | **Evaluador de modelos en español** (Mercor/Micro1/Turing) | Caja en USD en 2-6 semanas sin capital; 929 ofertas listadas para AR (2026-10-01). Puente para financiar lo demás — no negocio. Los roles de ing. industrial (USD 70-110/h) hoy exigen EE.UU. + 4 años. | 7 |
| 17 | **IA para estudios contables argentinos** | Dolor documentado (311 h/año de cumplimiento fiscal; startups locales prometiendo -83%), mercado grande y cercano; ventana de 12-24 meses antes de que el software contable lo integre. | 7 |
| 34 | **Implementación IA en español para PyMEs hispanas de EE.UU.** | Mismo servicio que #4 pero cobrando en USD y con ventaja de idioma/horario; Factura E + Payoneer resuelven el cobro. Lo difícil es la adquisición. | 7 |
| 19 | **Radar de licitaciones públicas (+ subsidios, #33) con resumen de pliegos** | Demanda estructural (el Estado compra siempre), cliente local, sinergia fuerte con el stack de datos; la IA resuelve lo más pesado (leer pliegos). Requiere algo de scraping. | 7 |

Mención: **#23 Asistente para productores de seguros (6,5)** y **#10 Catálogo listo para agentes (6,5)** — mejores ejemplos de "copiar lo que en EE.UU. tiene funding" y "subirse a la ola agéntica en AR", respectivamente. #10 encaja muy bien con Orden Operativo (maestro de SKUs).

**Lectura combinada:** #4 + #17 + #34 son el mismo motor (adopción de IA en equipos no técnicos con método de procesos) aplicado a tres mercados. Conviene elegir **un** mercado de arranque, no los tres.

## 5. Olas que se cierran rápido (entrar ya o no entrar)

| Ola | Por qué se cierra | Ventana estimada (desde 2026-10-01) |
|-----|-------------------|--------------------------------------|
| Configurar Claude/Cowork/ChatGPT para PyMEs (#4, #5, #38) | Anthropic sacó workflows listos (2026-05-13) y arma una red de partners con USD 100M; cada versión es más autoconfigurable. Sobrevive el que vende rediseño de procesos + adopción, no "setup". | 18-36 meses |
| Data labeling / evaluación generalista (#1 parte baja) | Ya colapsando: Outlier ~USD 50→20/h (dic-2025), DoorDash metiendo 8M couriers como evaluadores (mar-2026). Solo queda el segmento experto. | Ya cerrándose; experto 1-3 años |
| Catálogo "agent-ready" (#10) | Tiendanube/ML van a autocompletar atributos con su propia IA; hoy la demanda real es chica (ACP con ~30 comercios en EE.UU., feb-2026). | 12-24 meses |
| IA para contadores (#17, #18) | Errepar, Aconpy, Genio Contable, Colppy integran IA con normativa cargada. | 12-24 meses |
| Conectores MCP para SaaS locales (#9) | Los propios proveedores publican su MCP oficial. | 6-18 meses |
| EU AI Act (#8) | Ventana original (2026-08) se evaporó con el Omnibus; reabre antes de 2027-12-02. | Pausada hasta 2027 |
| Verifactu (#37) | Evento único con fecha (si se confirma: 2027-01-01 / 2027-07-01). | Hasta mediados de 2027 |

## 6. Trampas comunes (detectadas en esta investigación)

1. **Fechas regulatorias vencidas:** abundan blogs vendiendo "deadline EU AI Act agosto 2026" — se postergó (en vigor 2026-07-27). Verificar siempre la norma vigente antes de vender cumplimiento.
2. **Tarifas de EE.UU. aplicadas a LATAM:** "fractional CAIO USD 15.000-40.000/mes" o "MCP USD 5.000-15.000" no se trasladan a una PyME argentina; dividir por 3-10.
3. **Requisitos ocultos de las plataformas de datos:** el anuncio dice USD 110/h, pero la letra chica exige EE.UU., 4+ años y 20 h/sem (Mercor IE, leído 2026-10-01). Leer requisitos antes de entusiasmarse.
4. **Fuentes con conflicto de interés:** las cifras más espectaculares ("+2.300% búsquedas GEO", "LinkedIn +312%", "MCP es la oportunidad que nadie conoce") vienen de vendedores de herramientas/cursos o no son verificables.
5. **Funding ≠ demanda pagable acá:** que Cara o Toothy levanten millones en EE.UU. prueba el dolor allá; en AR hay que validar con 5-10 entrevistas y al menos 2 clientes pagos antes de construir nada.
6. **Competir contra el producto de la big tech o de la plataforma:** cualquier servicio que sea "configurar la herramienta" muere cuando la herramienta se configura sola. Anclar el valor en lo que la plataforma no puede hacer: relevar procesos, cambiar hábitos, medir resultados.
7. **Responsabilidad profesional:** impuestos (#17), clasificación aduanera (#26), salud (#22), seguros (#23), RRHH (#25) — un error de IA tiene costo legal para el cliente. Siempre "asistente con supervisión humana" y nunca firmar lo que corresponde a un matriculado.
8. **Volúmenes agénticos inflados:** "160M de transacciones x402" suena enorme; son ~USD 28.000/día. Medir en dólares, no en transacciones.
9. **Plataformas de trabajo que cambian las reglas:** recortes de tarifa, baneos automáticos y sequías sin aviso (Outlier, Scale). Nunca más del 50% del ingreso de una sola.
10. **Datos sensibles sin contrato:** subir datos de clientes de un estudio contable/jurídico/médico a una IA sin acuerdo de confidencialidad ni política de datos es un riesgo legal (Ley 25.326) y reputacional.

## 7. Fuentes principales (con fecha de consulta 2026-10-01)

- Mercor — ofertas "Industrial Engineers", "Spanish Linguistic Expert": work.mercor.com [PRIMARIA]
- aitrainer.work/jobs/argentina — 929 ofertas para AR al 2026-10-01 [ANECDÓTICO, agregador]
- breakingeven.online (newsletter 2026-04-08), herohunt.ai — estado del mercado de datos de IA [ANECDÓTICO]
- iProUP 2026-08-12 y diegoceredi.com 2026-09-25 — pagos agénticos en AR (MODO + Frávega en ChatGPT 2026-09-23) [PRIMARIA prensa / CONFLICTO consultor]
- iProfesional 2026-05-16 (Genio Contable) y 2026-08-06 (Errepar Consultor IA) [PRIMARIA prensa]
- ecosistemastartup.com 2026-08-20 (Bumeran: 46% RRHH AR usa IA) [PRIMARIA vía prensa]
- secureprivacy.ai / holisticai.com — Digital Omnibus AI Act (en vigor 2026-07-27) [ANECDÓTICO, coincidentes]
- kanerika.com / channelinsider.com — Claude Partner Network (mar-2026) [ANECDÓTICO]
- pasqualepillitteri.it — Claude for Small Business (2026-05-13) [ANECDÓTICO]
- accessnewswire 2026-07-06 — Cowork Academy [PRIMARIA, comunicado]
- gtlaw.com (Enter, mayo 2026), globallegalpost (Magnar) [PRIMARIA]
- pulse2 (Cara), fintech.global 2026-07-27 (AGI), dealroom (Covera) [PRIMARIA]
- ycombinator.com, thesaasnews (Linda AI feb-2026) — dental [PRIMARIA]
- noticiasrcn (Callbook YC S26), forbesargentina (Mozart), latamfintech (Colektia) [PRIMARIA]
- businesswire (Bobyard), lawnandlandscape (Attentive), inquirer 2026-08-11 (ServiceTitan) [PRIMARIA]
- mercado.com.ar (CAMESI 36%, Zonaprop, Selenios) [PRIMARIA prensa]
- infonegocios (WeSpeak), innovaciondigital360 (OEATUR 83,3%) [PRIMARIA prensa]
- buenosaires.gob.ar 2026-04-28, mendoza.gov.ar — docentes [PRIMARIA]
- palabrasdelderecho / lmneuquen — Zárate ZARA, DesafIA Ciudades [PRIMARIA prensa]
- bloomberry.com, algeriatech.news — FDE [ANECDÓTICO]
- hackerone.com — red teaming [PRIMARIA]
- kucoin/cointelegraph (a16z) — x402 volúmenes [ANECDÓTICO]
- quickbooks.intuit.com (2023), fortune.com 2025-09-05 — mercado hispano EE.UU. [PRIMARIA, dato viejo]
- Límite: búsquedas web agotadas a mitad de sesión; gastronomía, logística, subsidios, Verifactu y nearshoring quedaron con evidencia débil o [NO VERIFICADO].
