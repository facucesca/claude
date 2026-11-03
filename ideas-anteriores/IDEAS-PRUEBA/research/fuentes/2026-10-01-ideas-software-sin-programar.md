# Informe fuente: Software y productos tecnológicos que un NO-programador puede construir con Claude (2026-10-01)

> Informe crudo del frente "software sin saber programar / vibe coding". Fecha de corte: **2026-10-01**.
> Marcas de confianza: **[PRIMARIA]** = dato oficial, reporte con metodología o revenue verificado por API (TrustMRR); **[SECUNDARIA]** = prensa/analistas; **[ANECDÓTICO]** = blog, self-report o vendedor; **[COI]** = conflicto de interés (vende curso, plataforma o la herramienta que recomienda); **[SIN DATO 2026]** = idea plausible pero sin evidencia fresca verificada en esta sesión.

---

## 0. Encabezado y contexto del usuario

- Argentino; cobra vía Payoneer, Mercado Pago o merchant of record (Polar, Lemon Squeezy/Stripe Managed Payments, Paddle, Hotmart). Stripe directo no.
- Usa Claude / Claude Code pero **no sabe programar** y le preocupa vender software que no entiende (bugs, seguridad, mantenimiento). Esta es la restricción dominante del informe: la pregunta no es "¿se puede construir?" (casi todo se puede) sino "¿puede **sostenerlo y responder por él** sin entender el código?".
- Tiene Cloudflare, GitHub y Higgsfield conectados. Presupuesto < USD 500-1.000. Acepta activos, semi-pasivos y pasivos.
- Activo diferencial ya identificado en el proyecto: **ingeniería industrial / "Orden Operativo"** (stock, ABC, picking, mermas, layout) — ver `ideas/2026-09-07-consultora-mejora-procesos.md`.

## 1. Metodología

- ~37 búsquedas web + ~22 lecturas de páginas (WebFetch) el 2026-10-01. **La cuota de búsquedas de la sesión se agotó** antes de cubrir algunas verticales (Glide/AppSheet pricing 2026, Apify PPE oct-2026, talleres corporativos), por lo que esas ideas quedan marcadas [SIN DATO 2026] y deben verificarse antes de decidir.
- Fuentes priorizadas: TrustMRR (revenue verificado por API de Stripe — el mejor antídoto contra capturas falsas), reportes con metodología (Symbiotic Security, Wiz, Fiverr Business Trends Index), prensa tech (The Register, TechCrunch, The Next Web, The Decoder), documentación oficial (Shopify, Polar, Tiendanube).
- Se descartó como evidencia todo número que solo aparece en blogs generados por SEO sin fuente primaria (ver "Trampas comunes", punto 4: ejemplo concreto de un dato inventado sobre un "marketplace oficial de Claude Skills").
- Score 1-10 = **para ESTE usuario** (no-programador, AR, presupuesto bajo, perfil ing. industrial), integrando los 7 criterios del CLAUDE.md. Para ideas activas el criterio de automatización pesa menos (nota 2026-09-07).
- Dificultad para no-programador 1-5: 1 = configurar herramientas sin código; 3 = Claude escribe código pero en un entorno gestionado y acotado; 5 = requiere poder leer y depurar código en producción.

---

## 2. Contexto de mercado: el auge del vibe coding (datos duros)

### 2.1 Las plataformas crecen como nada en la historia del SaaS
| Plataforma | Dato | Fecha | Fuente |
|---|---|---|---|
| Lovable | USD 200M ARR | 2025-11 | [TechDogs](https://www.techdogs.com/tech-news/td-newsdesk/lovable-hits-400m-arr-in-february-adds-100m-in-a-month-with-146-employees) [SECUNDARIA] |
| Lovable | USD 400M ARR (sumó ~100M en un mes, 146 empleados) | 2026-02 | ídem |
| Lovable | ~USD 600M run-rate; Serie C USD 400M a valuación USD 13,3B | 2026-08 | [Ecosistema Startup](https://ecosistemastartup.com/lovable-cruza-us600m-arr-y-consolida-el-vibe-coding/), [Northeast Times 2026-08-13](https://northeasttimes.com/2026/08/13/lovable-the-app-building-startup-just-doubled-its-value-to-13-3-billion/) [SECUNDARIA] |
| Replit | USD 300M ARR fin 2025 → USD 525M abr-2026; objetivo USD 1B fin 2026; valuación USD 9B | 2026-04 | [Sacra](https://sacra.com/research/replit-passes-500m-year/), [Startbase](https://www.startbase.com/news/replit-erreicht-9-milliarden-bewertung-und-will-vibe-coding-neu-definieren/) [SECUNDARIA] |
| Bolt.new (StackBlitz) | USD 40M ARR en ~6 meses (mar-2025); 7M usuarios (dic-2025) | 2025 | [Sacra](https://sacra.com/research/bolt-new), [Morph](https://www.morphllm.com/bolt-vibe-coding) [SECUNDARIA] |
| Fiverr | +938% demanda de "especialistas en Claude Code" (búsquedas nov-2025 → abr-2026); vibe coding y agentes de voz como prioridades | 2026 (BTI) | [Fiverr Business Trends Index vía Longbridge](https://longbridge.com/news/289193258.md) [PRIMARIA, pero % sobre base chica] |
| App Store | 557.000 apps nuevas en 2025; +84% de envíos en un trimestre; revisión pasó de 24-48 h a 7-30+ días (mar-2026) | 2026 | [The Next Web](https://thenextweb.com/news/vibe-coding-apple-app-store-surge-crackdown) [SECUNDARIA] |

**Lectura:** el dinero grande del vibe coding lo capturan **las plataformas** (Lovable, Replit, Bolt) y los que ya tienen distribución. La oferta de software se multiplicó (App Store duplicándose), lo que **abarata el software genérico** y vuelve más valiosos (a) la distribución, (b) el conocimiento de dominio y (c) la confianza/responsabilidad humana.

### 2.2 Evidencia de "no-programadores que facturan" — con sus sesgos
- ShiftNex (staffing de salud, Lovable): USD 1M ARR en ~5 meses; Lumoo (moda, Lovable): ~€700k ARR; Qconcursos (Brasil, Lovable): USD 3M en 48 h — **pero tenía 500k alumnos previos** (la distribución hizo el trabajo). Fuente: [Sorceress, 2026](https://sorceress.games/blog/real-vibe-coding-apps-what-indies-built-in-2026) [ANECDÓTICO].
- Alex Finn (Creator Buddy) USD 300k ARR — **vende la "Vibe Coding Academy"** [COI]; Vibed Agents USD 9k MRR (el fundador no sabía hacer `git commit` 9 meses antes). Fuente: [John Ellison, ene-2026](https://iamjohnellison.substack.com/p/the-vibe-coding-wave-is-here-5-builders) — el propio autor nota que 4 de 5 casos venden cursos [COI].
- "~70% de los primeros builds vibe-coded requieren al menos un reinicio completo" ([Questera, 2026-05-30](https://www.questera.ai/blogs/vibe-coding-statistics-2026)) [ANECDÓTICO, metodología no publicada].
- **Mediana real (base del proyecto):** app de suscripción al año de lanzada ≈ USD 72/mes (RevenueCat 2026, ya documentado en `2026-09-02-microsaas-productos-dev.md`).

### 2.3 Seguridad: el riesgo que define este frente
| Caso | Qué pasó | Fecha | Fuente |
|---|---|---|---|
| EnrichLead | SaaS "100% hecho con Cursor, cero código a mano": API keys en el frontend, sin auth, sin rate limit. Atacado a los 2 días del post viral; la IA "rompía otras partes" al intentar arreglar; cerró en una semana | 2025-03 | [Vibe Graveyard](https://vibegraveyard.ai/story/enrichlead-vibe-coded-saas-shutdown/) [SECUNDARIA] |
| Base44 (Wix) | Bypass de autenticación con solo el `app_id` público: acceso a apps privadas de empresas (RRHH, PII). Parche en 24 h | 2025-07-09 | [Wiz](https://www.wiz.io/blog/critical-vulnerability-base44), [The Hacker News](https://thehackernews.com/2025/07/wiz-uncovers-critical-access-bypass.html) [PRIMARIA] |
| App educativa en Lovable | 16 vulnerabilidades (6 críticas), lógica de auth invertida, 18.697 registros expuestos (alumnos de UC Berkeley, K-12). Causa: RLS/roles de Supabase mal implementados | 2026-02-27 | [The Register](https://www.theregister.com/2026/02/27/lovable_app_vulnerabilities) [SECUNDARIA] |
| Lovable (plataforma) | BOLA: cualquier cuenta gratis podía leer código, credenciales de DB y chats de proyectos creados antes de nov-2025; reporte HackerOne abierto 48 días; Lovable primero negó la brecha | 2026-04 | [The Register 2026-04-20](https://www.theregister.com/2026/04/20/lovable_denies_data_leak/), [Computing](https://www.computing.co.uk/news/2026/security/lovable-flaw-exposed-source-code-credentials-and-ai-chats) [SECUNDARIA] |
| Estudio 1.072 apps (Lovable, v0, Bolt, Replit, Windsurf + Supabase) | 98% con ≥1 falla; 16% críticas; 172 sitios permitían **borrar** tablas sin autenticación | 2026-06-02 | [Symbiotic Security](https://www.symbioticsec.ai/blog/we-scanned-1-072-vibe-coded-apps-98-had-security-flaws) [PRIMARIA, COI: venden escáner] |
| GitGuardian 2026 / OX Security | Commits asistidos por IA filtran credenciales ~2x más; 62% del código IA con ≥1 vulnerabilidad | 2026 | citado en [Exitbid](https://exitbid.io/blog/sell-vibe-coded-app) [SECUNDARIA] |
| Due diligence | FE International: riesgos técnicos de IA restan 15-30% al múltiplo de venta; "secretos en el repo" = señal #1 para matar un deal | 2026 | ídem |

**Lectura para este usuario:** su miedo es racional y está respaldado por datos. Ni siquiera la plataforma (Lovable) es garantía. La conclusión operativa del informe es: **vender resultados sobre stacks gestionados donde él no es responsable del perímetro de seguridad, o vender conocimiento/configuración, no software propio con datos de terceros.**

### 2.4 Mercado de MCP / Skills / apps en asistentes
- MCP: 12.000+ servidores públicos (mar-2026), **< 5% monetizados** ([Medium/MCP, 2026](https://medium.com/mcp-server/the-rise-of-mcp-protocol-adoption-in-2026-and-emerging-monetization-models-cb03438e985c)) [ANECDÓTICO]. Marketplaces con cobro: MCPize (85% al creador), Smithery, Apify (pagó USD 560k a creadores en sep-2025). El caso "21st.dev USD 10k MRR en 6 semanas" es de un dev experto con producto de UI, no replicable por un no-programador.
- Claude Skills: **no existe un store oficial pago de Anthropic** a jul-2026; lo oficial es el sistema de **plugins/marketplaces de Claude Code** (un repo de GitHub con config se vuelve marketplace). Hay marketplaces pagos incipientes de terceros (Agensi, Agent37, SkillHQ) sin datos públicos de ventas de creadores ([Ryan Doser, jul-2026](https://ryandoser.com/claude-skills-marketplace/); [Agent37](https://www.agent37.com/blog/claude-skills-marketplace) [COI]). Caso anecdótico: consultor de marketing vendió 25 skills a USD 99 → USD 3.000 en 45 días ([AI Blew My Mind](https://aiblewmymind.substack.com/p/sell-claude-skills)) [ANECDÓTICO]: vendió a **su audiencia**, no a un marketplace.
- ChatGPT App Directory: abrió dic-2025 sobre Apps SDK (MCP); el checkout nativo es para bienes físicos en EE.UU.; el resto monetiza con redirección externa ([WebFX](https://www.webfx.com/blog/ai/chatgpt-apps/), [OpenAI](https://openai.com/index/introducing-apps-in-chatgpt/)) [SECUNDARIA].

### 2.5 Señal de saturación más dura del informe (TrustMRR, revenue verificado por API al 2026-10-01)
| Producto | Qué es | MRR verificado | Fuente |
|---|---|---|---|
| Vibe App Scanner | Escáner de seguridad para apps hechas con IA (USD 19-39/mes), **hecho por 2 ingenieros de seguridad**, 281k impresiones en Google/30 días | **USD 942** (38 suscripciones; fundado 2025-12-21) | [TrustMRR](https://trustmrr.com/startup/vibe-app-scanner.md) [PRIMARIA] |
| SecureMyVibes | Auditoría web automática (€15 reporte / €19 mes) | **USD 21** (USD 153 histórico; fundado 2026-02) | [TrustMRR](https://trustmrr.com/startup/securemyvibes?metric=mrr) [PRIMARIA] |
| VibeFix | "Forense" de código IA + parches | **USD 0** | [TrustMRR](https://trustmrr.com/startup/vibefix.md) [PRIMARIA] |

Aun el nicho "más obvio" del momento (seguridad para vibe coders), con demanda real y fundadores expertos, rinde de USD 0 a USD 942/mes. **El cuello de botella es distribución + confianza, no construir.**

### 2.6 Cobro desde Argentina (transversal)
- **Polar**: merchant of record, paga a Argentina vía Stripe Connect Express ([docs Polar](https://polar.sh/docs/merchant-of-record/supported-countries)); subió su tarifa ~25% en 2026 [SECUNDARIA].
- **Lemon Squeezy** se está absorbiendo en **Stripe Managed Payments** (3,5% + fees Stripe ≈ 6,4% + USD 0,30) ([Alex Cloudstar](https://alexcloudstar.com/blog/merchant-of-record-indie-saas-2026/)) — verificar si Managed Payments acepta vendedores AR antes de depender de él.
- Clientes argentinos (servicios/PyMEs): **Mercado Pago / transferencia en pesos + factura (monotributo)** — sin fricción, pero con riesgo cambiario; cotizar en USD o ajustar mensualmente.
- Hotmart: cobra en LATAM con medios locales, apto para plantillas/cursos.

---

## 3. Ideas — lista numerada

> Formato por idea: **Qué es** · **Ejemplo/señal** · **Cobro y precio** · **Stack con Claude + dificultad (1-5)** · **Tipo y h/sem en régimen** · **Capital y tiempo al 1er dólar** · **Cobro desde AR** · **Riesgos** · **Score**.

### Bloque A — Servicios (activos) donde el software es el medio, no el producto

**1. "Kit Orden Operativo": app de stock/depósito sobre Google Sheets + AppSheet/Glide, implementada en PyMEs**
- Qué es: control de stock, clasificación ABC, conteo cíclico, punto de pedido y tablero de mermas, armado sobre planillas + app móvil no-code, vendido junto con el método de ing. industrial (relevamiento → rediseño → herramienta → capacitación).
- Señal: el software de inventario para PyMEs AR cuesta ARS 5k-15k/mes (básico) a 15k-50k/mes (multi-sucursal, integración ML/Tiendanube); Gestar Pyme desde ARS 49.000/mes ([Yo Facturo](https://yo-facturo.com/blog/sistema-de-inventario-y-facturacion-pyme/), [Diario de Cuyo](https://www.diariodecuyo.com.ar/espaciodemarca/desarrollo-local-con-vision-de-futuro-gestar-pyme-integra-ia-para-que-los-comercios-sanjuaninos-disparen-su-rentabilidad-1798956.html), 2026) [SECUNDARIA]. El hueco: el software existe, **el orden operativo no** — la PyME compra el sistema y sigue con stock fantasma.
- Cobro: proyecto USD 400-1.500 (relevamiento + implementación) + abono USD 50-150/mes de soporte/ajustes. [estimación, validar con 3-5 clientes]
- Stack: Google Sheets (fórmulas + Apps Script generado por Claude) + AppSheet o Glide para la app de conteo/escaneo de códigos; Looker Studio para el tablero. Dificultad **2**. Los datos quedan en la cuenta Google **del cliente** (él no custodia nada).
- Tipo: activo → semi-pasivo (las plantillas se reutilizan). Régimen 3-6 h/sem por cartera de 5-10 abonos.
- Capital: ~USD 0-100. Primer dólar: 4-8 semanas (con el caso Sporting como credencial).
- AR: perfecto (Mercado Pago/transferencia + factura).
- Riesgos: depende de vender (es consultoría); AppSheet/Glide cambian precios [SIN DATO 2026: verificar planes vigentes]; fórmulas frágiles si el cliente las toca (mitigar: hojas protegidas + versión).
- **Score: 8/10** — máximo fit (dominio propio + cero custodia de datos + stack que él puede entender).

**2. Herramientas internas a medida para PyMEs (sobre stack gestionado)**
- Qué es: "apps a medida" chicas — carga de pedidos, ABM de clientes, órdenes de trabajo, checklist de calidad, cotizador — reemplazando planillas sueltas. Construidas con Lovable/Claude **solo si** el backend es gestionado y el alcance no toca pagos ni datos sensibles.
- Señal: agencias que construyen herramientas internas con Lovable (propuestas, dashboards operativos) ([LowCode Agency, 2026-09-03](https://www.lowcode.agency/blog/lovable-for-agencies)) [COI: agencia]; la misma fuente advierte que "un developer debe auditar RLS y auth antes de salir en vivo; no es opcional" y que "cuando el proyecto toca el techo de Lovable, las horas de developer no presupuestadas son problema de la agencia".
- Cobro: USD 500-3.000 por herramienta + mantenimiento USD 50-200/mes.
- Stack: preferir Google Workspace (Sheets + AppSheet + Apps Script) o Airtable/Softr/Glide (auth y permisos los resuelve la plataforma). Lovable + Supabase solo para uso interno detrás de login de Google y sin PII. Dificultad **2-3**.
- Tipo: activo. 5-10 h/sem con 3-5 clientes.
- Capital: USD 0-50/mes (planes de plataforma, a veces los paga el cliente). Primer dólar: 4-10 semanas.
- AR: fácil.
- Riesgos: responsabilidad por bugs; "scope creep"; cliente que pide "solo un cambito" eterno (contrato con alcance y horas). Lock-in a la plataforma no-code.
- **Score: 7,5/10**.

**3. Migración "de Excel caótico a datos maestros limpios" (SKUs, proveedores, listas de precio)**
- Qué es: limpieza y normalización de maestros de artículos (duplicados, unidades, códigos, categorías) — prerrequisito de cualquier sistema. Claude hace el 80% del trabajo de normalización.
- Señal: [SIN DATO 2026] específico; es el paso previo que todo ERP/Tango/Xubio necesita y que los integradores cobran como servicio de implementación ([Guía de Software](https://www.guiadesoftware.com/blog/mejor-erp-pymes-argentina)).
- Cobro: USD 200-800 por proyecto según volumen.
- Stack: Claude (análisis de CSV) + Sheets. Dificultad **1-2**.
- Tipo: activo, por proyecto; puerta de entrada a la idea 1.
- Capital: 0. Primer dólar: 2-6 semanas.
- AR: fácil. Riesgos: confidencialidad de listas de precios (NDA simple); bajo ticket.
- **Score: 7/10** — como "producto de entrada", no como negocio aislado.

**4. Tableros de KPIs operativos como abono (Looker Studio + Sheets)**
- Qué es: tablero semanal de stock, rotación, quiebres, mermas y fill-rate conectado a las planillas/exports del sistema del cliente, + 1 revisión mensual.
- Señal: [SIN DATO 2026] de precio local; categoría madura en consultoría BI.
- Cobro: USD 80-250/mes por cliente.
- Stack: Looker Studio (gratis) + Sheets + Apps Script para importar exports. Dificultad **2**.
- Tipo: semi-pasivo (una vez armado, se actualiza solo). 1 h/cliente/mes.
- Capital: 0. Primer dólar: 4-8 semanas (upsell de 1-3).
- AR: fácil. Riesgos: churn si no se usa; depende de que el cliente exporte datos (automatizar).
- **Score: 7/10**.

**5. Setup de Claude para equipos de PyME: Skills/Proyectos a medida + capacitación**
- Qué es: empaquetar procedimientos internos (cómo cotizar, cómo responder reclamos, cómo hacer el conteo, plantillas de informes) como **Skills de Claude** (carpetas de instrucciones en texto + plantillas) y entrenar al equipo para usarlas. No es software ejecutable: es conocimiento estructurado.
- Señal: Fiverr BTI 2026: +938% demanda de especialistas en Claude Code y "vibe coding" como prioridad de empresas ([Longbridge/Fiverr](https://longbridge.com/news/289193258.md)) [PRIMARIA, base chica]. Skills son "carpetas con instrucciones, scripts y recursos" portables entre apps de Claude, Claude Code y API ([The Decoder](https://the-decoder.com/anthropic-launches-skills-so-claude-can-automatically-pick-prompts-for-specialized-tasks/)).
- Cobro: USD 300-1.500 por setup (5-10 skills + 2 sesiones de capacitación) + abono opcional de mantenimiento de skills.
- Stack: Claude (Team/Pro del cliente) + skills en markdown + plugin marketplace privado en GitHub si usan Claude Code. Dificultad **1-2**.
- Tipo: activo, productizable (biblioteca de skills reutilizable por rubro).
- Capital: 0. Primer dólar: 3-8 semanas.
- AR: fácil (local) y exportable (Payoneer).
- Riesgos: Anthropic puede volver trivial lo que hoy se cobra; el cliente tiene que pagar Claude; competencia creciente de "consultores IA". Riesgo técnico bajo (no hay datos custodiados por él).
- **Score: 7/10**.

**6. Automatizaciones Google Apps Script / Sheets para PyMEs (alertas, reportes, mails automáticos)**
- Qué es: alerta de stock bajo por mail/Telegram, reporte semanal automático, importador de ventas de ML/Tiendanube a una planilla.
- Señal: Fiverr: pedidos de "arreglar WordPress" +712% y de mantenimiento web x4 entre oct-2024 y mar-2025 — la PyME paga por que "algo funcione" ([KUOW/CodeConductor](https://codeconductor.ai/blog/vibe-coding-cleanup-specialists/)) [SECUNDARIA]. Precio de Apps Script en Workana [SIN DATO 2026].
- Cobro: USD 100-500 por automatización.
- Stack: Apps Script escrito por Claude, corre en la cuenta Google del cliente. Dificultad **2** (scripts cortos, auditables línea por línea pidiéndole a Claude que explique).
- Tipo: activo, tickets chicos. Capital 0. Primer dólar 2-4 semanas.
- AR: fácil. Riesgos: cuotas de Apps Script; mantenimiento cuando cambia una API externa.
- **Score: 6,5/10**.

**7. Implementador/revendedor de bots de WhatsApp (turnos, pedidos, FAQ) sobre plataforma gestionada**
- Qué es: configurar bots de WhatsApp para consultorios, restaurantes, inmobiliarias usando plataformas existentes (Botmaker, Whaticket, Cliengo, ManyChat, Treble) — no construir el bot de cero.
- Señal: costo mensual típico de una PyME AR con ~1.000 conversaciones: ARS 60.000-150.000 ([Yo Facturo, 2026](https://yo-facturo.com/blog/bot-whatsapp-argentina-ia/)); turnos con recordatorios bajaron ausentismo >40% (caso citado en [Develop Argentina, 2026-06-25](https://developargentina.com/blog/chatbot-whatsapp-argentina-implementar-empresa-2026)) [ANECDÓTICO]; tiers LATAM USD 15-50 / 50-300 / 500+ por mes ([AsisteClick](https://asisteclick.com/en/blog/chatbot-whatsapp-precio-empresas/)) [COI: vendedor]. **Meta reintroduce tarifa por mensaje de servicio desde 2026-10-01** ([SendPulse](https://sendpulse.com/latam/blog/cambios-en-el-precio-de-los-mensajes-de-servicio-de-whatsapp-en-octubre)).
- Cobro: implementación USD 150-600 + abono USD 30-100/mes (o comisión de partner de la plataforma).
- Stack: plataforma no-code + Claude para diseñar flujos y base de conocimiento. Dificultad **1-2**.
- Tipo: activo → semi-pasivo con cartera. 2-4 h/sem con 10 clientes.
- Capital: 0-50. Primer dólar: 3-6 semanas.
- AR: fácil.
- Riesgos: **saturación alta** (muchas agencias), cambios de precio de Meta, baneos de números, el cliente puede ir directo a la plataforma.
- **Score: 6,5/10**.

**8. Partner/integrador de SaaS existentes con comisión recurrente (Tiendanube Partners, ERPs locales)**
- Qué es: en vez de construir software, implementar y referir el de otros (Tiendanube, Xubio, Gestar, Pago Nube/Envío Nube) cobrando implementación + comisión recurrente del programa de partners.
- Señal: Tiendanube Partners: 600+ partners en 5 países; programa de agencias con 5 niveles y **comisiones recurrentes** (actualizado 2026-07-21) ([Tiendanube](https://www.tiendanube.com/blog/tiendanube-partners/), [Ayuda Tiendanube](https://ayuda.tiendanube.com/socios-especialistas/como-se-calculan-las-comisiones-en-el-partners-program-agencies-de-tiendanube)) [PRIMARIA].
- Cobro: setup USD 200-800 + comisión recurrente (porcentajes por nivel; verificar tabla vigente).
- Stack: ninguno propio; Claude para documentación y migración de catálogos. Dificultad **1**.
- Tipo: activo con cola pasiva (comisión). 
- Capital: 0. Primer dólar: 4-8 semanas.
- AR: nativo.
- Riesgos: depende de las reglas del programa; ticket bajo; no construye activo propio.
- **Score: 6/10** — buena "bolsa de clientes" para las ideas 1 y 4.

**9. MCP servers a medida para PyMEs (conectar su ERP/planillas a Claude)**
- Qué es: construir un MCP que deje a Claude consultar el stock, ventas o tickets de la empresa.
- Señal: proliferan "agencias de MCP" enterprise (RaftLabs, Simform, etc.) ([RaftLabs, ago-2026](https://www.raftlabs.com/blog/top-mcp-server-development-companies)) [COI]; "la habilidad rara es escribir definiciones de herramientas que un agente lea sin adivinar parámetros". Precios no publicados.
- Cobro: USD 1.000-5.000 por servidor (rango de agencias, [SIN DATO 2026] para AR).
- Stack: Cloudflare Workers + McpAgent (tiene la skill `cloudflare:build-mcp`). Dificultad **4**: maneja credenciales del cliente, auth OAuth, permisos de escritura.
- Tipo: activo. Capital bajo. Primer dólar 2-4 meses.
- AR: Payoneer/local.
- Riesgos: **alto** — un MCP con permisos de escritura mal hecho = el agente borra o filtra datos (prompt injection). Solo en modo **solo-lectura** y con un dev revisor.
- **Score: 4/10** (sube a 6 si se limita a solo-lectura sobre Sheets).

**10. Agencia de recepcionista de voz IA white-label para negocios locales**
- Qué es: revender agentes de voz (atención telefónica, turnos) de plataformas white-label.
- Señal: Trillet USD 299/mes plan agencia; Synthflow white-label USD 2.000/mes; My AI Front Desk: revendedores cobran USD 250-500/mes por recepcionista; "márgenes 70-90%" ([Trillet](https://trillet.ai/blogs/best-white-label-ai-receptionist-for-agencies-2026), [Dupple](https://dupple.com/learn/best-ai-receptionists)) [COI: los vendedores publican "playbooks de $0 a $50K MRR"].
- Cobro: USD 100-300/mes por cliente en AR (estimado; el mercado local paga menos que EE.UU.).
- Stack: Retell/Vapi/Trillet + Claude para prompts. Dificultad **2-3**.
- Tipo: activo/semi-pasivo. Capital USD 300+/mes de plataforma antes de tener clientes.
- AR: posible, pero las voces en rioplatense y el uso de teléfono en PyMEs AR (WhatsApp domina) bajan la demanda.
- Riesgos: el canal real en AR es WhatsApp, no la llamada; costo fijo de plataforma; saturación de "AI agencies".
- **Score: 4/10**.

**11. Servicio "vibe coding para no técnicos" (construir MVPs a emprendedores)**
- Qué es: armar MVPs con Lovable/Claude para otros emprendedores.
- Señal: Prajwal Tomar (AI MVP Builders) 45+ MVPs ([Ellison, ene-2026](https://iamjohnellison.substack.com/p/the-vibe-coding-wave-is-here-5-builders)) [COI: vende formación]; Lovable promociona "cómo arrancar una agencia Lovable" ([Lovable](https://lovable.dev/video/how-to-start-a-lovable-agency-build-mvps-find-clients-and-launch-your-portfolio)) [COI].
- Cobro: USD 1.500-8.000 por MVP (mercado global).
- Stack: Lovable + Supabase. Dificultad **3-4** (el MVP tiene usuarios reales, auth y datos).
- Riesgos: **justamente lo que el usuario teme**: responde por código que no entiende, con usuarios finales y datos personales (caso 18.697 registros). Competencia global con devs reales usando las mismas herramientas.
- **Score: 3,5/10**.

**12. Rescate de apps vibe-coded que se rompieron**
- Señal: demanda real ("20-30 contratos grandes en cola" según un dev en [KUOW, 2025-10-01](https://kuow.org/stories/the-human-coders-hired-to-mop-up-ai-slop)); "gig más barato USD 299, factura promedio ~USD 7.200" ([CodeConductor](https://codeconductor.ai/blog/vibe-coding-cleanup-specialists/)) [ANECDÓTICO]. Contra-análisis: no hay casos públicos de rentabilidad; el cliente típico tenía < USD 2.000 de presupuesto y un rescate competente requiere USD 10-15k ([Rentier Digital](https://rentierdigital.xyz/blog/vibe-code-rescue-market-analysis)) [ANECDÓTICO].
- Dificultad **5** — requiere leer y refactorizar código ajeno.
- **Score: 1,5/10** para este usuario (incompatible con su perfil).

**13. Auditoría de seguridad de apps vibe-coded (como servicio)**
- Señal: precios USD 199 (Valletta), USD 497 (High Velocity Club), USD 750 (VIBE/CHECK), hardening USD 2-5k (Beesoul) ([Valletta](https://vallettasoftware.com/blog/post/vibe-coding-audit), [SecurityWall](https://securitywall.co/blog/vibe-coding-security-audit-guide)) [COI].
- Dificultad **5**: vender seguridad sin saber seguridad = riesgo legal y reputacional.
- **Score: 1,5/10**.

### Bloque B — Productos digitales semi-pasivos de bajo riesgo técnico

**14. Plantillas Google Sheets "con superpoderes" (Apps Script) para PyMEs en español**
- Qué es: control de stock con ABC y punto de pedido, cotizador, costeo de producto/receta, control de caja; vendidas como plantilla con video tutorial.
- Señal: Google Sheets add-ons/plantillas monetizan bien en nichos: Sync2Sheets USD 9k MRR, 400+ clientes ([Starter Story, 2024-05-07](https://www.starterstory.com/stories/sync2sheets-give-notion-the-superpowers-of-google-sheets)); BudgetSheet USD 1,6k MRR tras ~2 años ([Indie Hackers, 2022](https://www.indiehackers.com/post/how-i-built-a-google-sheets-extension-making-1-6k-mrr-b42d845e6a)) — ambos **founders técnicos** y datos viejos [ANECDÓTICO].
- Cobro: USD 15-60 pago único (Hotmart/Mercado Pago/Gumroad); bundles USD 80-150.
- Stack: Sheets + Apps Script generado por Claude; landing en Cloudflare Pages. Dificultad **1-2**.
- Tipo: pasivo/semi-pasivo; 1-3 h/sem soporte.
- Capital: 0-50. Primer dólar: 4-10 semanas (depende de distribución).
- AR: Hotmart/Mercado Pago sin fricción.
- Riesgos: copia trivial; plantillas gratis abundan; necesita canal (YouTube/TikTok vía Higgsfield, o derivación desde la consultoría).
- **Score: 6,5/10** — sinergia directa con idea 1 (la consultoría genera las plantillas y la credibilidad).

**15. Template apps no-code revendibles (AppSheet/Glide "App de Inventario lista")**
- Qué es: igual que 14 pero como app móvil copiable (escaneo de código de barras, conteo, recepción).
- Señal: [SIN DATO 2026] de ventas; marketplaces de plantillas de Glide/AppSheet existen.
- Cobro: USD 30-150 + setup opcional USD 100-300.
- Dificultad **1-2**. Riesgo: dependencia de precios de la plataforma.
- **Score: 6/10**.

**16. Biblioteca de Claude Skills en español por rubro (venta directa)**
- Qué es: paquetes de Skills (ej. "Skills para depósito y logística", "Skills para estudio contable AR: monotributo, ARCA, liquidaciones") distribuidos como plugin de Claude Code o carpeta para Claude.ai.
- Señal: no hay store oficial pago; marketplaces de terceros sin datos de venta; caso USD 3.000 en 45 días vendiendo a audiencia propia ([AI Blew My Mind](https://aiblewmymind.substack.com/p/sell-claude-skills)) [ANECDÓTICO]; Ryan Doser vende "AI Skills Stack" sin cifras ([Ryan Doser, jul-2026](https://ryandoser.com/claude-skills-marketplace/)).
- Cobro: USD 29-99 pago único; o suscripción USD 9-19/mes con actualizaciones.
- Stack: markdown + GitHub privado + Polar/Hotmart con entrega de acceso. Dificultad **1**.
- Tipo: pasivo. Capital 0. Primer dólar: 1-3 meses.
- AR: Polar/Hotmart.
- Riesgos: **copia trivial** (son archivos de texto); Anthropic puede lanzar equivalentes; demanda no probada en español.
- **Score: 5,5/10** (como subproducto de la idea 5, no standalone).

**17. Curso/comunidad "vibe coding y Claude para no programadores en español" (build in public)**
- Qué es: documentar su propio recorrido (el no-programador que construye) y monetizar con comunidad/curso.
- Señal: 4 de 5 "casos de éxito" de vibe coding monetizan enseñando ([Ellison](https://iamjohnellison.substack.com/p/the-vibe-coding-wave-is-here-5-builders)) — lo que es a la vez señal de demanda y de COI. Libros/cursos en español ya existen ([Ecosistema Startup](https://ecosistemastartup.com/?p=67479), [Inflearn](https://www.inflearn.com/en/course/how-a-non-major-can?cid=341078)).
- Cobro: comunidad USD 10-30/mes; curso USD 50-200.
- Stack: Higgsfield para video corto, Hotmart. Dificultad **1**.
- Tipo: semi-pasivo, pero la audiencia exige constancia (contradice la regla de no-vigilancia).
- Riesgos: credibilidad (enseñar lo que aún no domina), saturación de gurús, ética (no vender humo).
- **Score: 4,5/10** — mejor como canal de distribución de las otras ideas que como producto.

**18. Plantillas Notion/Airtable para gestión de PyMEs**
- Señal: "creador promedio exitoso USD 2-5k/mes" ([Fungies, 2026](https://fungies.io/sell-notion-templates/)) [COI: Fungies es plataforma de cobro; número sin metodología]. Notion Marketplace cobra 10%.
- Dificultad **1**. Saturación muy alta en inglés; PyMEs AR usan más Excel/Sheets que Notion.
- **Score: 4/10**.

### Bloque C — Software propio (micro-SaaS, extensiones, apps): mayor riesgo para un no-programador

**19. App para la tienda de Tiendanube (ej. alertas de stock, reposición, etiquetas, costeo)**
- Qué es: app del App Store de Tiendanube para merchants AR/BR/MX.
- Señal: 600+ partners tecnológicos en 5 países; **NubeSDK obligatorio para instalaciones nuevas desde 2026-08-30**, validación SDK en homologación desde 2026-06-05 ([Tiendanube Partners](https://www.tiendanube.com/socios/tecnologicos), [dev Tiendanube](https://dev.tiendanube.com/en/docs/applications/overview)) [PRIMARIA]. Mucho menos competida que Shopify; cobro en moneda local.
- Cobro: USD 5-30/mes por tienda.
- Stack: Cloudflare Workers + D1 + OAuth de Tiendanube + NubeSDK. Dificultad **4** (OAuth, webhooks, datos de pedidos de compradores = PII).
- Tipo: semi-pasivo. 2-5 h/sem soporte.
- Capital: bajo. Primer dólar: 3-6 meses (homologación incluida).
- AR: nativo (Tiendanube cobra al merchant).
- Riesgos: PII de compradores (Ley 25.326), homologación, soporte en horario comercial.
- **Score: 5/10** (6 si la app solo lee stock/productos, sin datos de compradores).

**20. Herramientas para vendedores de Mercado Libre (calculadora de márgenes/comisiones, alertas de precio de competencia, reposición)**
- Señal: incumbente local Real Trends (2014, AR/MX/BR; planes por volumen de ventas) ([Cronista](https://www.cronista.com/infotechnology/internet/si-vendes-en-mercadolibre-este-servicio-busca-mejorar-tu-desempeno/)); calculadoras gratuitas ya existen ([SPOM](https://app.spomsolutions.com/herramientas/calculadora-comisiones-mercadolibre)) [PRIMARIA del producto]. ML Argentina ~6.000 tiendas integradas (dato api2cart) [ANECDÓTICO].
- Cobro: freemium; USD 5-20/mes.
- Stack: versión **sin login a ML** (calculadora pública + planilla) dificultad **2**; versión con OAuth de ML dificultad **4**.
- Riesgos: ML cambia API y reglas; incumbentes; datos de ventas sensibles.
- **Score: 5,5/10** (la calculadora pública entra en la cartera "micro-herramientas web").

**21. Add-on de Google Sheets en Workspace Marketplace (nicho operativo: ABC, pronóstico simple, conteo)**
- Señal: el Marketplace fue el canal #1 de BudgetSheet y Sync2Sheets (ver idea 14); Google Sheets tools en Starter Story con ingresos altos pero muestra sesgada ([Starter Story ideas](https://www.starterstory.com/ideas/google-sheets-tool)) [ANECDÓTICO, survivorship].
- Cobro: USD 5-15/mes.
- Stack: Apps Script + Polar/ExtensionPay-like licencias. Dificultad **3** (publicación requiere verificación OAuth de Google; scopes amplios pueden exigir auditoría de seguridad — [SIN DATO 2026]: confirmar requisitos vigentes y usar scopes mínimos tipo "solo esta hoja").
- **Score: 5/10**.

**22. Agente IA empaquetado "comprador/reposición" para PyMEs (sugiere pedidos a proveedores)**
- Qué es: lee ventas y stock (planilla), sugiere pedido óptimo y redacta el mail al proveedor; el humano aprueba.
- Señal: [SIN DATO 2026] específico; se solapa con el micro-SaaS de monitoreo ya en cartera.
- Stack: Cloudflare Agents SDK o Apps Script + API Claude. Dificultad **3-4**.
- Riesgos: si escribe/envía solo → errores caros; diseñar con aprobación humana.
- **Score: 5,5/10** — mejor como feature del Kit Orden Operativo (idea 1) que como SaaS.

**23. Wrapper vertical de IA en español (ej. descripciones de producto para ML/Tiendanube; presupuestos para oficios)**
- Señal: casos de wrappers de USD 40k-64k MRR ([Jack's newsletter, 2026-02](https://jacks-newsletter-0adf2e.beehiiv.com/p/how-an-ai-wrapper-hit-40k-mrr-and-what-it-means-for-our-tools-126a)) [ANECDÓTICO, survivorship]; "esperar USD 1-12k MRR en un primer año sólido a ~30 h/sem" ([IdeaProof](https://ideaproof.io/business-ideas/ai-wrapper)) [ANECDÓTICO]. Bain usa vibe coding para replicar productos en due diligence y un fondo abandonó una compra porque era replicable ([The Decoder, 2026-06-22](https://the-decoder.com/vibecoding-is-becoming-a-deal-breaker-test-for-software-acquisitions/)) → los wrappers son **lo más fácil de copiar**.
- Stack: Lovable/Workers + API Claude + Polar. Dificultad **3** (costos de API por abuso si no hay rate limit — caso EnrichLead).
- **Score: 4/10**.

**24. Directorio de nicho con IA (ej. proveedores logísticos y depósitos en AR; herramientas IA en español)**
- Señal: OpenAlternative ~USD 6.500/mes (65% ads + featured USD 197/mes); SaaSHub USD 10k+ MRR ([Dirstarter, 2026-07-15](https://dirstarter.com/blog/directory-website-examples)) [COI: Dirstarter vende boilerplate de directorios]. Fees de listing USD 29-497 ([OrangeBot](https://orangebot.ai/blog/where-to-submit-your-ai-tool-2026)).
- Stack: Cloudflare Pages + D1 o un boilerplate; contenido enriquecido con Claude. Dificultad **2-3**.
- Tipo: pasivo lento (SEO 6-12 meses). Capital < USD 100.
- Riesgos: AI Overviews comen clics (ya documentado en el proyecto: -34/61% CTR); directorios de IA saturados; el de nicho logístico AR es chico pero sin competencia [SIN DATO 2026].
- **Score: 4,5/10** (el directorio de proveedores logísticos AR sube a 5 por sinergia de leads para la consultoría).

**25. Micro-SaaS vertical construido con Lovable para un rubro AR (ej. turnos + recordatorios para talleres; órdenes de trabajo para service técnico)**
- Señal: ShiftNex USD 1M ARR con Lovable (staffing de salud) [ANECDÓTICO]; mediana RevenueCat USD 72/mes [PRIMARIA].
- Stack: Lovable + Supabase (RLS obligatoria) + Mercado Pago suscripciones. Dificultad **4** (multi-tenant + auth + datos de clientes de clientes).
- Riesgos: exactamente el patrón de las brechas de 2026 (Supabase sin RLS); soporte diario.
- **Score: 4/10** — solo después de 6+ meses de experiencia y con revisión de un dev.

**26. Plugin de WordPress**
- Señal: Freemius cobra ~10,5% efectivo; casos solo-dev existen ([Freemius](https://freemius.com/blog/how-wordpress-plugin-developers-make-money/)) [COI].
- Dificultad **4**: los plugins son el vector principal de hackeo de WordPress; soporte de compatibilidad infinito.
- **Score: 2,5/10**.

**27. App de Shopify**
- Señal: 0% de rev share hasta USD 1M (límite de por vida desde 2025) ([Shopify docs](https://shopify.dev/docs/apps/launch/distribution/revenue-share)) [PRIMARIA]; apps en venta: revenue trailing mediano USD 85k, múltiplo 3,9x ([BigIdeasDB](https://bigideasdb.com/how-to-sell-a-shopify-app)) [ANECDÓTICO, muestra sesgada a apps que llegaron a venderse].
- Dificultad **4-5** (review estricto, GDPR webhooks, Polaris, billing API). Mercado ultra competido.
- **Score: 3/10**.

**28. App móvil simple (iOS/Android) vibe-coded**
- Señal: Stoppr USD 12k MRR en mes 5 con TikTok ads ([Sorceress](https://sorceress.games/blog/real-vibe-coding-apps-what-indies-built-in-2026)) [ANECDÓTICO]; Apple endureció enforcement (2.5.2), retiró "Anything" el 2026-03-30, revisiones de 7-30+ días ([TNW](https://thenextweb.com/news/vibe-coding-apple-app-store-surge-crackdown)); mediana RevenueCat USD 72/mes.
- Dificultad **4**; cuenta de dev Apple USD 99/año; suscripciones in-app cobran bien desde AR (Apple/Google pagan), pero la distribución depende de ads pagos.
- **Score: 3/10**.

**29. App en el ChatGPT App Directory / conector para asistentes**
- Señal: directorio abierto dic-2025; monetización vía redirección externa salvo bienes físicos en EE.UU. ([WebFX](https://www.webfx.com/blog/ai/chatgpt-apps/)) [SECUNDARIA]. Es descubrimiento, no cobro.
- Dificultad **4** (MCP + UI + review de OpenAI).
- **Score: 3/10** (útil como canal si ya existe un producto; el proyecto descartó GPT Store).

**30. Plugin de Claude Code / marketplace propio en GitHub (vertical)**
- Señal: sistema oficial de plugins vía repos de GitHub; sin cobro nativo ([Ryan Doser](https://ryandoser.com/claude-skills-marketplace/)).
- Monetización indirecta (lead-gen para servicio). Dificultad **2**.
- **Score: 4/10** standalone; como vitrina de la idea 5, útil.

**31. MCP server pago en marketplaces (MCPize/Smithery/Apify)**
- Señal: < 5% de 12.000+ MCPs monetizados; MCPize 85% al creador; Apify USD 560k a creadores en sep-2025 ([Medium MCP 2026](https://medium.com/mcp-server/the-rise-of-mcp-protocol-adoption-in-2026-and-emerging-monetization-models-cb03438e985c)) [ANECDÓTICO].
- Dificultad **3** si es solo lectura de datos públicos (Workers). Ya cubierto por "micro-herramientas web + MCP" y "Apify" en cartera.
- **Score: 5/10** (sin cambios vs cartera).

**32. Telegram Mini App con Stars**
- Señal: Stars solo se retiran vía TON; una compra de USD 2,40 puede dejar ~USD 1,30 al dev ([Merge Rocks](https://merge.rocks/blog/telegram-mini-apps-2026-monetization-guide-how-to-earn-from-telegram-mini-apps), [The Block](https://www.theblock.co/post/303217/telegram-mini-app-developers-can-now-use-stars-to-get-ton-rewards-or-ad-discounts)) [SECUNDARIA]. Mercado dominado por juegos/cripto.
- **Score: 2,5/10**.

**33. Escáner SaaS de seguridad para apps vibe-coded (producto)**
- Señal: ver tabla TrustMRR (USD 0 / 21 / 942 MRR) — nicho obvio, saturado, construido por expertos.
- **Score: 1,5/10**.

**34. Boilerplates/"starters seguros" de Lovable/Claude Code para vender a otros no-programadores**
- Riesgo: vender "seguridad" que él no puede verificar; los boilerplates compiten con los gratuitos de las plataformas.
- **Score: 2/10**.

**35. Reventa/flip de apps vibe-coded (construir y vender en Microns/Flippa/Acquire)**
- Señal: apps pre-revenue se venden USD 100-5.000 (deals documentados: USD 500, 1.000, 4.500) ([Exitbid, 2026-07-31](https://exitbid.io/blog/how-much-is-a-vibe-coded-app-worth)) [ANECDÓTICO]; con MRR se valúan por múltiplo, pero con descuento de 15-30% por riesgo de código IA.
- Dificultad **3**; el comprador hace due diligence de seguridad.
- **Score: 3/10**.

**36. Generador de informes de relevamiento con IA (fotos + checklist de depósito → informe PDF con hallazgos y quick-wins)**
- Qué es: herramienta interna para la consultoría Orden Operativo que, madura, se vende a otros consultores/encargados de depósito.
- Señal: [SIN DATO 2026] — idea derivada del perfil; el valor está en el método, no en el código.
- Stack: Claude (visión) + plantilla de informe + Apps Script/Docs. Dificultad **2** (uso interno primero, sin usuarios externos).
- Tipo: herramienta de productividad propia → semi-pasivo después.
- **Score: 6,5/10** (como apalancamiento de la idea 1).

**37. Portal de pedidos B2B por WhatsApp para distribuidoras chicas (catálogo + pedido + lista de precios)**
- Qué es: catálogo web con lista de precios por cliente que arma el pedido y lo manda por WhatsApp al vendedor; sin cobro online.
- Señal: [SIN DATO 2026] específico en AR; competidores probables (Tiendanube B2B, catálogos WhatsApp Business gratis).
- Stack: Sheets como backend + página estática en Cloudflare Pages (sin login de compradores, sin pagos). Dificultad **2-3**.
- Cobro: setup USD 200-500 + USD 20-50/mes.
- **Score: 5,5/10** (interesante por bajo riesgo: no hay pagos ni cuentas).

**38. Herramientas web gratuitas de cálculo logístico/operativo monetizadas (EOQ, punto de pedido, cubicaje, costo de almacenamiento)**
- Variante temática de "micro-herramientas web" (en cartera) con sesgo a su dominio; capta leads para la consultoría además de ads.
- Dificultad **2** (Cloudflare Pages, sin datos de usuario).
- **Score: 6/10** (como imán de leads, no por AdSense).

---

## 4. Ya en cartera (datos actualizados breves, no se re-evalúan)

| Idea en cartera | Score previo | Novedad 2026-10-01 |
|---|---|---|
| Actores Apify LATAM | 8 | Apify pagó USD 560k a creadores en sep-2025; Apify aparece como canal de monetización de MCP. La migración a pay-per-event de oct-2026 **no pudo re-verificarse** (cuota de búsqueda agotada) → verificar en consola Apify. |
| Micro-herramientas web + MCP | 7 | < 5% de 12k+ MCPs monetizan; MCPize da 85% al creador. Refuerza: MCP como canal, no como negocio. Idea 38 es su variante de nicho logístico. |
| Micro-SaaS monitoreo B2B | 7 | Bain/The Decoder (2026-06-22): software replicable pierde valor en M&A → el moat es el dato/nicho, no el código. Ideas 22 y 37 son variantes con menor riesgo. |
| Bots Telegram utilitarios | 6 | Mini Apps con Stars poco atractivas (idea 32). Sin cambios. |
| Templates n8n hispanos | 6 | Sin datos nuevos. |
| Extensión Chrome B2B | 6 | 178.299 extensiones activas; **mediana 18 usuarios**; solo 2,63% supera 10k usuarios (mar-2026) ([Konabayev](https://konabayev.com/blog/extension-monetization-statistics-2026/)) — dato que empeora la expectativa. |

Descartados que siguen descartados: GPT Store (el App Directory de ChatGPT no cambia el problema de cobro), RapidAPI, trading bots.

---

## 5. Top 5 del frente (para ESTE usuario)

1. **Kit Orden Operativo (Sheets + AppSheet/Glide + método) — 8/10.** Une su único diferencial real (ing. industrial, caso Sporting) con un stack que puede entender y donde **los datos viven en la cuenta del cliente**. Es la idea de consultoría ya en evaluación, con una capa de producto que la vuelve semi-pasiva (plantillas reutilizables + abonos de tablero).
2. **Herramientas internas a medida sobre stack gestionado — 7,5/10.** Demanda real de PyMEs con procesos en planillas; precio USD 500-3.000; riesgo acotado si se respeta la regla "sin pagos, sin PII, auth de la plataforma".
3. **Setup de Claude (Skills + capacitación) para equipos de PyME — 7/10.** Vende conocimiento estructurado, no código; demanda creciente (Fiverr +938%); productizable como biblioteca por rubro (idea 16 como subproducto).
4. **Tableros KPI como abono + limpieza de datos maestros (ideas 3 y 4) — 7/10.** Puerta de entrada de ticket bajo y la parte más "pasiva" de la línea de servicios.
5. **Plantillas Sheets/Apps Script en español (idea 14) + calculadoras logísticas gratis (idea 38) — 6,5/10.** El brazo semi-pasivo: se alimenta de lo que se construye para clientes y genera leads para el resto.

**Patrón del Top 5:** todo gira alrededor de **un mismo activo** (método de orden operativo + stack Google/no-code) con varias bocas de cobro, igual que la lógica del "stack de datos". Ninguna del Top 5 obliga a custodiar datos personales, cobrar pagos online ni operar un backend propio expuesto a internet.

**Lo que NO recomendamos aún** (aunque sea "lo de moda"): rescate de apps, auditoría de seguridad, MVPs para terceros, Shopify/WordPress, apps móviles, escáneres de seguridad. Todas requieren entender código en producción o competir con expertos — y los datos verificados (TrustMRR) muestran que incluso los expertos facturan poco ahí.

---

## 6. Trampas comunes

1. **Survivorship bias industrializado:** 4 de 5 "casos de vibe coding exitoso" venden cursos ([Ellison, ene-2026](https://iamjohnellison.substack.com/p/the-vibe-coding-wave-is-here-5-builders)). Qconcursos facturó USD 3M en 48 h porque ya tenía 500k alumnos. El dato a usar es la mediana (USD 72/mes, RevenueCat).
2. **MRR de captura de pantalla:** existe TrustMRR justamente porque los screenshots se falsifican. Regla: solo creer revenue verificado por API o reportes públicos.
3. **Vendedores que publican "playbooks":** plataformas de voz IA ("de $0 a $50K MRR"), Fungies (plantillas Notion), Dirstarter (directorios), agencias Lovable: todos venden la pala. Sus números son marketing.
4. **Estadísticas inventadas por blogs SEO generados con IA:** ej. un blog afirma que "Anthropic lanzó el Claude Skills Marketplace en mayo 2026 y facturó USD 48M en Q1"; fuentes más cuidadosas (Ryan Doser, jul-2026) confirman que **no existe store oficial pago**. Si un dato no tiene fuente primaria, no entra en la decisión.
5. **"Lo construí en un fin de semana" ≠ "lo puedo sostener":** ~70% de los primeros builds requieren reinicio completo; EnrichLead murió en una semana porque la IA rompía otras partes al arreglar. El costo real está en mantener, no en construir.
6. **La plataforma tampoco te cubre:** Lovable tuvo su propia brecha (BOLA, 48 días) y su "escaneo de seguridad gratuito" no evitó la app con 18.697 registros expuestos. La responsabilidad legal frente al cliente es tuya.
7. **Copia trivial:** si se construye en un fin de semana con IA, cualquiera lo copia en un fin de semana (Bain lo usa para tumbar valuaciones). Moat = dominio, datos, relación y distribución.
8. **Dependencia de tienda/plataforma:** Apple retiró apps sin aviso (2026-03-30) y las revisiones tardan 7-30 días; Tiendanube cambió a NubeSDK obligatorio (2026-08-30); Meta cambia tarifas de WhatsApp (2026-10-01).
9. **Costos de API sin techo:** un wrapper sin rate limit ni auth puede generar una factura de API mayor que todo lo facturado (EnrichLead: "maxearon las API keys").
10. **Cobrar en pesos sin cláusula de ajuste:** abonos locales deben cotizarse en USD o ajustarse mensualmente.

---

## 7. Reglas de seguridad mínimas para vender software sin saber programar

**Regla 0 — Elegí el perímetro antes que la idea.** Si el producto necesita (a) cobrar pagos online, (b) guardar datos personales de terceros (DNI, salud, menores, datos financieros), o (c) tener cuentas de usuario propias expuestas a internet, **no lo hagas solo**: o usás una plataforma que lo resuelve, o contratás revisión de un dev, o no lo hacés.

**Diseño**
1. **Los datos del cliente viven en la cuenta del cliente** (su Google Workspace, su Airtable, su Tiendanube). Vos tenés acceso delegado y revocable, nunca una copia propia.
2. **Pagos siempre por merchant of record o link de pago** (Polar, Hotmart, Mercado Pago). Nunca procesar tarjetas ni guardar datos de pago.
3. **Login siempre de un tercero** (Google, la plataforma no-code, Cloudflare Access). Nunca auth hecha a mano.
4. **Solo-lectura por defecto.** Cualquier automatización o agente que escribe, borra o envía mails necesita aprobación humana y un log.
5. **Alcance chico y por escrito:** qué hace, qué no hace, cuántas horas de cambios incluye el abono.

**Construcción con Claude**
6. **Cero secretos en el código o el repo:** API keys en variables de entorno/secretos de Cloudflare o Script Properties de Apps Script; repo privado; `.env` en `.gitignore`. Rotar cualquier clave que se haya pegado en un chat o commit.
7. **Si usás Supabase: RLS activada en todas las tablas** y probada con un usuario de prueba que intenta leer/borrar datos ajenos (el 98% de fallas del estudio de 2026-06-02 eran de este tipo).
8. **Rate limit y tope de gasto** en toda API paga (límite mensual en la consola de Anthropic/OpenAI; Cloudflare rate limiting).
9. **Pedirle a Claude revisión de seguridad en cada entrega** (ej. el comando `/security-review` de Claude Code) y que explique en castellano qué hace cada archivo; si no podés entender la explicación, el alcance es demasiado grande.
10. **Para cualquier cosa con usuarios externos o PII: revisión de un dev humano pago** antes de salir (presupuestar USD 100-300 por revisión acotada) — es más barato que un incidente.

**Operación**
11. **Backups automáticos** (versión de Sheets, export semanal de la base) y probá restaurar una vez.
12. **Monitoreo con alerta** (uptime + errores a Telegram/mail) — coherente con la regla de oro alert-driven.
13. **Actualizaciones:** congelar versiones de dependencias y no actualizar en producción sin probar en copia.

**Legal y comercial**
14. **Contrato simple** con: limitación de responsabilidad al monto cobrado, el cliente es responsable de sus datos y accesos, alcance y SLA "best effort", confidencialidad.
15. **Ley 25.326 (datos personales AR):** si igualmente tocás PII, el responsable de la base es el cliente; documentalo y no la copies.
16. **Transparencia:** decir que la herramienta se construye con asistencia de IA y está revisada; nunca vender "seguridad" o "auditorías" que no podés firmar.
17. **Salida definida:** entregar documentación y accesos para que el cliente pueda seguir sin vos (reduce el miedo a "lock-in" y es argumento de venta).

---

## 8. Fuentes principales (fechas de consulta 2026-10-01)

- Lovable ARR/valuación: [Ecosistema Startup](https://ecosistemastartup.com/lovable-cruza-us600m-arr-y-consolida-el-vibe-coding/) · [TechDogs](https://www.techdogs.com/tech-news/td-newsdesk/lovable-hits-400m-arr-in-february-adds-100m-in-a-month-with-146-employees) · [Northeast Times 2026-08-13](https://northeasttimes.com/2026/08/13/lovable-the-app-building-startup-just-doubled-its-value-to-13-3-billion/)
- Replit: [Sacra](https://sacra.com/research/replit-passes-500m-year/) · [Startbase](https://www.startbase.com/news/replit-erreicht-9-milliarden-bewertung-und-will-vibe-coding-neu-definieren/)
- Bolt: [Sacra](https://sacra.com/research/bolt-new) · [Morph](https://www.morphllm.com/bolt-vibe-coding)
- Fiverr BTI 2026: [Longbridge](https://longbridge.com/news/289193258.md)
- Seguridad: [Symbiotic 2026-06-02](https://www.symbioticsec.ai/blog/we-scanned-1-072-vibe-coded-apps-98-had-security-flaws) · [The Register 2026-02-27](https://www.theregister.com/2026/02/27/lovable_app_vulnerabilities) · [The Register 2026-04-20](https://www.theregister.com/2026/04/20/lovable_denies_data_leak/) · [Bastion](https://bastion.tech/blog/lovable-april-2026-data-breach) · [Wiz Base44](https://www.wiz.io/blog/critical-vulnerability-base44) · [Vibe Graveyard EnrichLead](https://vibegraveyard.ai/story/enrichlead-vibe-coded-saas-shutdown/)
- Rescate/auditoría: [KUOW 2025-10-01](https://kuow.org/stories/the-human-coders-hired-to-mop-up-ai-slop) · [CodeConductor](https://codeconductor.ai/blog/vibe-coding-cleanup-specialists/) · [Rentier Digital](https://rentierdigital.xyz/blog/vibe-code-rescue-market-analysis) · [Valletta](https://vallettasoftware.com/blog/post/vibe-coding-audit) · [SecurityWall](https://securitywall.co/blog/vibe-coding-security-audit-guide)
- TrustMRR: [Vibe App Scanner](https://trustmrr.com/startup/vibe-app-scanner.md) · [SecureMyVibes](https://trustmrr.com/startup/securemyvibes?metric=mrr) · [VibeFix](https://trustmrr.com/startup/vibefix.md)
- Venta de apps: [Exitbid](https://exitbid.io/blog/how-much-is-a-vibe-coded-app-worth) · [The Decoder 2026-06-22](https://the-decoder.com/vibecoding-is-becoming-a-deal-breaker-test-for-software-acquisitions/)
- MCP/Skills/ChatGPT apps: [Medium MCP](https://medium.com/mcp-server/the-rise-of-mcp-protocol-adoption-in-2026-and-emerging-monetization-models-cb03438e985c) · [Ryan Doser](https://ryandoser.com/claude-skills-marketplace/) · [Agent37](https://www.agent37.com/blog/claude-skills-marketplace) · [AI Blew My Mind](https://aiblewmymind.substack.com/p/sell-claude-skills) · [WebFX](https://www.webfx.com/blog/ai/chatgpt-apps/) · [RaftLabs](https://www.raftlabs.com/blog/top-mcp-server-development-companies)
- Apple: [The Next Web](https://thenextweb.com/news/vibe-coding-apple-app-store-surge-crackdown)
- Casos: [Sorceress](https://sorceress.games/blog/real-vibe-coding-apps-what-indies-built-in-2026) · [Ellison](https://iamjohnellison.substack.com/p/the-vibe-coding-wave-is-here-5-builders) · [Starter Story Sync2Sheets](https://www.starterstory.com/stories/sync2sheets-give-notion-the-superpowers-of-google-sheets) · [Indie Hackers BudgetSheet](https://www.indiehackers.com/post/how-i-built-a-google-sheets-extension-making-1-6k-mrr-b42d845e6a)
- Argentina: [Tiendanube Partners](https://www.tiendanube.com/blog/tiendanube-partners/) · [dev Tiendanube](https://dev.tiendanube.com/en/docs/applications/overview) · [Yo Facturo bots](https://yo-facturo.com/blog/bot-whatsapp-argentina-ia/) · [Yo Facturo inventario](https://yo-facturo.com/blog/sistema-de-inventario-y-facturacion-pyme/) · [Develop Argentina](https://developargentina.com/blog/chatbot-whatsapp-argentina-implementar-empresa-2026) · [Cronista/Real Trends](https://www.cronista.com/infotechnology/internet/si-vendes-en-mercadolibre-este-servicio-busca-mejorar-tu-desempeno/) · [SendPulse Meta oct-2026](https://sendpulse.com/latam/blog/cambios-en-el-precio-de-los-mensajes-de-servicio-de-whatsapp-en-octubre)
- Cobro: [Polar países](https://polar.sh/docs/merchant-of-record/supported-countries) · [Alex Cloudstar MoR 2026](https://alexcloudstar.com/blog/merchant-of-record-indie-saas-2026/) · [Shopify rev share](https://shopify.dev/docs/apps/launch/distribution/revenue-share)
- Otros: [Konabayev extensiones](https://konabayev.com/blog/extension-monetization-statistics-2026/) · [Dirstarter](https://dirstarter.com/blog/directory-website-examples) · [Trillet](https://trillet.ai/blogs/best-white-label-ai-receptionist-for-agencies-2026) · [LowCode Agency](https://www.lowcode.agency/blog/lovable-for-agencies)

## 9. Pendientes de verificación (cuota de búsqueda agotada)

- Precios vigentes 2026 de AppSheet y Glide (claves para ideas 1, 2, 15).
- Requisitos actuales de verificación OAuth / auditoría de seguridad para add-ons de Google Workspace (idea 21).
- Estado real de la migración Apify a pay-per-event (oct-2026) para la cartera.
- Si Stripe Managed Payments acepta vendedores con residencia argentina.
- Precio de mercado en AR (Workana/LinkedIn) de automatizaciones Apps Script y tableros Looker Studio — validar con 5 entrevistas a PyMEs antes de fijar precios.
