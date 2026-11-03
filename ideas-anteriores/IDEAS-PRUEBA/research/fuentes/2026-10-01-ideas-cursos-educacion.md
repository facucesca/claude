# Frente: cursos, educación e infoproductos — 40 ideas concretas

- **Fecha:** 2026-10-01
- **Autor:** agente investigador (Claude) para IDEAS-PRUEBA
- **Perfil asumido:** argentino, no programa (usa Claude/Claude Code), formación/pasantía en ingeniería industrial (relevamiento logístico de depósito en Sporting), presupuesto < USD 500-1.000, acepta pasivo/semi-pasivo/activo.
- **Excluidas por estar ya descartadas en el proyecto:** trading bots retail, TikTok Rewards, afiliados desde cero, música IA, KDP low-content, POD, prompts genéricos, GPT Store, Shorts AdSense.

## Metodología

1. 40 búsquedas web (WebSearch) entre 2026-09-30 y 2026-10-01 + 8 verificaciones directas (WebFetch) de las fuentes más citadas. El presupuesto de búsquedas de la sesión se agotó al final; algunos datos quedaron **sin verificar** y están marcados así.
2. Prioridad a fuentes 2025-2026. Cada dato numérico lleva fuente y fecha de publicación o de consulta.
3. **Alerta metodológica importante:** una parte grande de lo que aparece en buscadores sobre "cómo ganar plata con cursos/IA" es contenido SEO generado con IA y con cifras inventadas. Ejemplo detectado: varias páginas afirman que "Anthropic lanzó un Claude Skills Marketplace en mayo 2026 con 15% de comisión y USD 48M en Q1". Al verificar la fuente citada (agent37.com, consultada 2026-10-01) dice lo contrario: **no existe un marketplace oficial** de skills. Toda cifra que no pude rastrear hasta una fuente primaria está marcada como *no verificada*.
4. Los ingresos de comunidades Skool que circulan son **estimaciones precio × miembros** (techo teórico, no facturación real). profitable.app lo aclara explícitamente.
5. Score 1-10 = potencial realista **para este usuario** (no para el mercado en general), ponderando: credibilidad que puede construir, fit con Claude sin programar, cobro desde AR, tiempo al primer dólar, saturación.

### Datos de contexto del frente (base para varias ideas)

| Dato | Valor | Fuente / fecha |
|---|---|---|
| Creadores Kajabi que ganan < USD 1.000/año | 46% | Kajabi Creator Report 2025, citado por voxbooster/biztoolkit (2026) — *cifra secundaria* |
| Mediana creador en plataforma propia | USD 2.000-10.000/año solo cursos | biztoolkit.co, 2026 — *secundaria* |
| Comunidades Skool rastreadas / % pagas | 48.100 / 32,6% pagas | [profitable.app/skool/stats](https://profitable.app/skool/stats), datos 2026-09-02 |
| Mediana MRR estimado comunidad paga Skool | ~USD 1.200/mes (techo: precio × miembros) | ídem |
| Precio mediano Skool (pagas) | USD 29/mes (profitable) – USD 39/mes (trending, revenuegeeks) | profitable.app 2026-09-02; [revenuegeeks](https://revenuegeeks.com/software/skool/statistics) 2026-09-05 |
| Techo típico comunidad drip USD 19-39 | ~USD 5K MRR (churn 6-9%/mes) | [communipass](https://communipass.com/?p=20194), 2026 |
| Completion cohorte vs self-paced | 53-64% vs 42-48%; marketplaces/MOOCs 3-15% | [Ruzuku](https://www.ruzuku.com/learn/articles/cohort-vs-self-paced-completion-study), 2026 |
| Maven | +500 expertos, "~USD 20.000 por cohorte promedio" | Maven (fuente con conflicto de interés: es su marketing) |
| Hotmart: cursos de IA | > R$ 140M movidos en 2025, 340.000 compradores, +326% vs 2023 | startups.com.br, 2026 |
| PyMEs argentinas e IA | 46% valora/exige IA al contratar; solo 36% capacita; 11% tiene programa formal; 28% planea uno en 12 meses | Trendsity para Deel, [Mercado](https://mercado.com.ar/talento-y-liderazgo/pymes-argentinas-crece-la-exigencia-de-habilidades-de-ia-pero-falta-capacitacion-interna), 2026 |
| Udemy: revenue share suscripción | 15% desde 2026-01 (era 25%); 37% venta orgánica | [teach.udemy.com](https://teach.udemy.com/enabling-investment-subscription-terms-update/) |
| Substack | USD 450M brutos a escritores en 2025; 5M suscripciones pagas Q1 2026 | everything-pr.com, 2026 |

### Cobro desde Argentina (aplica a todas)

- **Hotmart:** retiro vía Payoneer / PayPal / Tarjeta Hotmart; mínimo USD 50, fee USD 1 por retiro; plazo D+2 para 90% (fuera de Brasil). Fuente: bit4learn.com, 2026. ✅ viable.
- **Lemon Squeezy (MoR, de Stripe):** Argentina soportada para payouts bancarios y PayPal ([docs Lemon Squeezy](https://docs.lemonsqueezy.com/help/getting-started/supported-countries), consultado 2026-10-01). ✅ viable. Ojo: Stripe Managed Payments en preview desde 2026-02; LS sigue standalone (fungies.io, 2026-04).
- **Gumroad:** paga vía PayPal a AR (conocido; no re-verificado hoy).
- **Skool / Maven / Circle:** cobran con Stripe; Argentina no es país Stripe. **No verificado** si Skool/Maven pagan a AR → asumir que NO hasta confirmar; workaround = cobrar por Hotmart/Lemon Squeezy y dar acceso manual/automatizado.
- **Clientes locales (talleres, PyMEs):** Mercado Pago + factura de monotributo. Para clientes del exterior: exportación de servicios (factura E) con Payoneer/Wise según disponibilidad.

---

## Las 40 ideas

> Formato por idea: **Qué es** · **Ejemplo y señal** · **Cobro y precio** · **Ejecución con Claude** · **Tipo / h-sem en régimen** · **Capital / 1er dólar** · **Cobro AR** · **Riesgos** · **Score**

### Bloque A — Capacitación en IA por profesión o sector

#### 1. Talleres in-company "IA práctica para PyMEs" (medio día / jornada)
- **Qué es:** taller presencial u online de 3-4 h para equipos de una PyME: Claude/ChatGPT/Copilot aplicados a sus tareas reales (mails, planillas, procedimientos, atención).
- **Ejemplo y señal:** Andreas Lopez cobra USD 1.950 por medio día on-site (cal.com/andreaslopez, 2026); Design for Online desde £850 hasta 12 personas ([designforonline.com](https://designforonline.com/training-and-resources/ai-training-workshops/), 2026). En AR: 46% de PyMEs exige IA pero solo 11% tiene programa formal y 28% planea uno en 12 meses (Trendsity/Deel, 2026).
- **Cobro y precio:** por taller. AR realista: USD 300-800 por taller PyME; USD 1.000-2.000 empresa mediana.
- **Ejecución con Claude:** Claude arma diagnóstico previo (formulario), guía del facilitador, ejercicios con datos del rubro del cliente, handout y certificado. Él vende (LinkedIn, cámaras de comercio, contactos), da el taller y adapta ejemplos.
- **Tipo / h-sem:** activo. 4-8 h por taller (prep + dictado).
- **Capital / 1er dólar:** < USD 100 / 3-8 semanas (primer taller piloto con descuento).
- **Cobro AR:** ✅ Mercado Pago + factura monotributo.
- **Riesgos:** commodity rápido (todos dan "taller de ChatGPT"); necesita diferencial (rubro u operaciones). No escala sin él. Clientes PyME AR con presupuesto chico.
- **Score: 7/10**

#### 2. IA para estudios contables argentinos (ARCA, monotributo, liquidaciones)
- **Qué es:** cohorte online corta (4 encuentros) + kit de prompts/skills para contadores y sus empleados.
- **Ejemplo y señal:** Universidad de Belgrano lanzó posgrado "IA Práctica para Contadores" ciclo 2026 ([ub.edu.ar](https://ub.edu.ar/sites/default/files/ia_practica_para_contadores_final.pdf)); ICAEW cobra £825 + VAT por su curso 2026 ([events.icaew.com](https://events.icaew.com/pd/31977/2026-generative-ai-for-accountants-learn-it-use-it-apply-it)).
- **Cobro y precio:** USD 80-200 por persona (AR); in-company para estudios USD 400-1.000.
- **Ejecución con Claude:** Claude produce casos con datos ficticios, plantillas Excel, skills de Claude para conciliaciones/resúmenes; él necesita un **socio contador** que valide y co-firme.
- **Tipo / h-sem:** semi-pasivo (curso grabado + 1 cohorte/trimestre). 4-6 h.
- **Capital / 1er dólar:** < USD 200 / 6-10 semanas.
- **Cobro AR:** ✅ Mercado Pago / Hotmart.
- **Riesgos:** credibilidad (no es contador → socio obligatorio); universidades y consejos profesionales compiten con aval; riesgo de que la IA dé respuestas impositivas erróneas (responsabilidad).
- **Score: 6/10**

#### 3. IA para estudios jurídicos
- **Qué es:** taller/cohorte de uso de IA para escritos, revisión de contratos, gestión del estudio.
- **Ejemplo y señal:** UCA abrió posgrado "Práctica legal con IA generativa" (2026-05-19 a 2026-07-14) ([abogados.com.ar](https://abogados.com.ar/la-facultad-de-derecho-de-la-uca-abrio-la-inscripcion-al-posgrado-practica-legal-con-ia-generativa/38899)); Thomson Reuters "LegalTech: Tecno abogad@s 2026" desde 2026-06-29 (mercado.com.ar).
- **Cobro y precio:** USD 100-300 por persona.
- **Ejecución con Claude:** igual que #2, con socio abogado.
- **Tipo / h-sem:** semi-pasivo, 4-6 h.
- **Capital / 1er dólar:** < USD 200 / 2-3 meses.
- **Cobro AR:** ✅.
- **Riesgos:** jugadores institucionales fuertes (UCA, Thomson Reuters); credibilidad nula sin abogado; alucinaciones de jurisprudencia = riesgo reputacional.
- **Score: 4/10**

#### 4. IA para la administración de consultorios/clínicas (no clínica)
- **Qué es:** taller para secretarias/administración de consultorios: turnos, recordatorios, facturación a obras sociales, respuestas por WhatsApp.
- **Ejemplo y señal:** el mercado "IA para médicos" está dominado por cursos clínicos caros: Harvard Medical School USD 1.900 (22,5 créditos CME) ([learn.hms.harvard.edu](https://learn.hms.harvard.edu/ai-clinical-medicine/agenda)); MIT xPRO USD 2.650 (2026). El hueco es lo administrativo.
- **Cobro y precio:** USD 50-150 por persona o USD 300-500 por clínica.
- **Ejecución con Claude:** Claude arma flujos y guiones; él dicta.
- **Tipo / h-sem:** activo, 3-5 h.
- **Capital / 1er dólar:** < USD 100 / 2-3 meses.
- **Cobro AR:** ✅.
- **Riesgos:** datos de salud (Ley 25.326 de datos personales) → no puede enseñar a cargar historias clínicas en chatbots; poca disposición a pagar.
- **Score: 4/10**

#### 5. Cursos de IA para docentes con puntaje (Argentina)
- **Qué es:** curso asincrónico/sincrónico con puntaje docente (requiere aval de una institución).
- **Ejemplo y señal:** CABA ya formó +26.000 docentes en IA (buenosaires.gob.ar, 2026-04-28); Tucumán capacitará 25.000 con puntaje (iprofesional, 2026-06-13); Universidad FASTA obtuvo puntaje en Mendoza (2026).
- **Cobro y precio:** ARS bajo (USD 15-40) o pago institucional.
- **Ejecución con Claude:** Claude escribe el material; él necesita un instituto que avale ante la DGCyE/ministerio.
- **Tipo / h-sem:** semi-pasivo, 3-5 h.
- **Capital / 1er dólar:** bajo / 4-6 meses (trámite de aval).
- **Cobro AR:** ✅ pero en pesos.
- **Riesgos:** el Estado lo da gratis a escala; trámite burocrático; ticket muy bajo.
- **Score: 3/10**

#### 6. IA para inmobiliarias / corredores
- **Qué es:** comunidad o cohorte para agentes: descripciones, tasaciones asistidas, seguimiento de leads.
- **Ejemplo y señal:** Empowered Agent AI (Skool) USD 97/mes ([skool.com/empoweredagent](https://www.skool.com/empoweredagent)); AI Real Estate Academy (Skool) 282 miembros, gratis (2026). Asociaciones de REALTORS en EE.UU. dan cursos de IA en 2026 (kcrar.com, gcar.net).
- **Cobro y precio:** USD 50-150 curso; comunidad USD 20-50/mes.
- **Ejecución con Claude:** Claude produce plantillas de avisos, guiones, skill de redacción; él vende a colegios de martilleros/inmobiliarias.
- **Tipo / h-sem:** semi-pasivo, 3-5 h.
- **Capital / 1er dólar:** < USD 200 / 2-3 meses.
- **Cobro AR:** ✅.
- **Riesgos:** comunidades de EE.UU. con poca tracción (282 miembros gratis); no tiene red en el rubro.
- **Score: 4/10**

#### 7. IA para RRHH y reclutadores
- **Qué es:** cohorte de 2 días para armar agentes de screening, descripciones de puesto, onboarding.
- **Ejemplo y señal:** "The AI-Native HR Leader", 2 días (2026-09-18/19), USD 995 con 30 cupos fundadores (skillscouter, 2026); HR AI Bootcamp 4 semanas (2026-06-15 a 07-19).
- **Cobro y precio:** USD 300-1.000 en EE.UU.; LATAM USD 100-300.
- **Ejecución con Claude:** Claude arma contenido; él necesita experiencia de RRHH que no tiene.
- **Tipo / h-sem:** activo/semi, 4-6 h.
- **Capital / 1er dólar:** bajo / 3+ meses.
- **Cobro AR:** ✅.
- **Riesgos:** falta de credibilidad de dominio; sesgo/discriminación algorítmica en selección (riesgo legal).
- **Score: 3/10**

#### 8. IA aplicada a logística y depósitos (en español) ⭐
- **Qué es:** curso/cohorte + taller in-company: control de stock, ABC/slotting, pronóstico simple, análisis de mermas, procedimientos de picking, usando Claude + Excel/Sheets, sin programar.
- **Ejemplo y señal:** Georgia Tech "Generative AI Application for Supply Chain Professionals" (2026-03-23/25 virtual; 2026-04-20/22 presencial USD 1.500) ([scl.gatech.edu](https://www.scl.gatech.edu/education/professional-education/course/gaiascp)); MIT CTL "AI-Driven Supply Chain" (2026-07-20/24); programas ejecutivos de "AI-Driven Warehousing" (2026-08-03/05). **Casi no hay oferta práctica en español para PyMEs/depósitos** (no encontré ninguna en las búsquedas → señal de hueco, pero también puede ser señal de baja demanda; validar).
- **Cobro y precio:** curso grabado USD 49-149; cohorte USD 150-400; in-company USD 500-2.000.
- **Ejecución con Claude:** Claude genera datasets de depósito ficticios, planillas con fórmulas ABC/punto de pedido, guiones de clase, ejercicios y skills reutilizables. Él aporta el **caso Sporting** (relevamiento real), da las clases y vende. Sinergia directa con la idea "Orden Operativo" (el curso es el embudo de la consultoría).
- **Tipo / h-sem:** semi-pasivo (grabado) + activo (in-company). 4-8 h.
- **Capital / 1er dólar:** < USD 300 / 6-12 semanas.
- **Cobro AR:** ✅ Hotmart (LATAM) + Mercado Pago (local).
- **Riesgos:** nicho chico; compradores (jefes de depósito/logística) menos digitales; credibilidad junior (mitigar con casos reales y piloto gratis).
- **Score: 8/10**

#### 9. Lean / mejora continua + IA
- **Qué es:** curso para practicantes de mejora continua: IA en DMAIC, 5 porqués, VSM, documentación de procesos.
- **Ejemplo y señal:** Loyola University Chicago "Lean and Artificial Intelligence" (2026-09-09/30), USD 750 ([luc.edu](https://www.luc.edu/executiveeducation/forindividuals/leanandartificialintelligence/)); SUTD Singapur 2 días; Udemy "Generative AI for Lean Six Sigma Experts"; especialización en Coursera (Packt).
- **Cobro y precio:** USD 50-300.
- **Ejecución con Claude:** Claude arma plantillas (A3, VSM, SIPOC) con prompts; él valida con su formación de industrial.
- **Tipo / h-sem:** semi-pasivo, 3-5 h.
- **Capital / 1er dólar:** < USD 200 / 2-3 meses.
- **Cobro AR:** ✅.
- **Riesgos:** sin certificación (Green/Black Belt) su autoridad es limitada; mejor como módulo de #8 que como producto aparte.
- **Score: 6/10**

#### 10. Excel + IA (Claude for Excel / Copilot) para operaciones y PyMEs ⭐
- **Qué es:** curso práctico de planillas con IA para no-financieros: stock, costos, reportes, limpieza de datos.
- **Ejemplo y señal:** Miss Excel (Kat Norton) facturó USD 2,9M en 2024 sin inversión externa (getlatka; foundry, 2025) y lanzó curso de Copilot a USD 299 para 2026 ([miss-excel.com](https://www.miss-excel.com/courses/copilot-with-miss-excel)). Anthropic lanzó **Claude for Excel** en beta (2026-05, [anthropic.com](https://www.anthropic.com/news/advancing-claude-for-financial-services)); en Maven ya hubo "AI-Powered Excel for Finance Professionals" (2026-06-11). Ola nueva = ventana para contenido en español.
- **Cobro y precio:** USD 29-149 curso; plantillas USD 10-40.
- **Ejecución con Claude:** Claude diseña las planillas y ejercicios; él graba pantalla (sin cara si quiere) y publica clips cortos como marketing.
- **Tipo / h-sem:** semi-pasivo, 3-5 h.
- **Capital / 1er dólar:** < USD 200 / 6-10 semanas.
- **Cobro AR:** ✅ Hotmart / Lemon Squeezy.
- **Riesgos:** Miss Excel es survivorship puro (contenido viral con baile, 2M seguidores); el nicho "Excel" está muy saturado en español; diferenciarse por "Excel para depósito/operaciones". Las features de IA cambian cada mes → mantenimiento.
- **Score: 7/10**

#### 11. Capacitador de adopción Microsoft 365 Copilot (subcontratado)
- **Qué es:** dar capacitaciones de Copilot a empleados de corporativos, como freelance para partners de Microsoft.
- **Ejemplo y señal:** múltiples búsquedas laborales de "Copilot Trainer" en UK/EE.UU. con contratos hasta 2026-12 (itjobswatch, insightglobal, 2026).
- **Cobro y precio:** USD 25-60/h en LATAM (estimación propia, *no verificada*).
- **Ejecución con Claude:** Claude prepara labs y guías; él necesita certificaciones Microsoft (MS-4005 o similar) y licencia de prueba.
- **Tipo / h-sem:** activo, 10-20 h (es casi un empleo).
- **Capital / 1er dólar:** USD 0-200 / 2-4 meses.
- **Cobro AR:** ✅ como exportación de servicios.
- **Riesgos:** es trabajar para otro; requiere inglés y certificación; demanda en LATAM no medida.
- **Score: 4/10**

#### 12. AI literacy corporativa para empresas de habla hispana (empuje EU AI Act art. 4)
- **Qué es:** módulo e-learning (SCORM) de alfabetización en IA vendible a empresas españolas o multinacionales con filiales en LATAM.
- **Ejemplo y señal:** el art. 4 del AI Act exige alfabetización en IA desde 2025-02-02, con supervisión/enforcement desde 2026-08 ([KnowBe4 blog](https://blog.knowbe4.com/ai-literacy-training-from-best-practice-to-legal-requirement-under-the-new-eu-ai-act)); 78% de organizaciones sin pasos significativos (epcgroup, 2026 — *dato de proveedor, conflicto de interés*). Ya venden esto Kubicle, KnowBe4, NAVEX.
- **Cobro y precio:** licencia por empleado USD 5-30 o paquete USD 500-3.000.
- **Ejecución con Claude:** Claude escribe guion, quizzes y adapta a SCORM con herramientas no-code (ej. iSpring/Articulate trial, o H5P).
- **Tipo / h-sem:** semi-pasivo, 3-5 h + ventas.
- **Capital / 1er dólar:** USD 200-500 / 3-6 meses (ciclo de venta B2B largo).
- **Cobro AR:** ✅ exportación de servicios.
- **Riesgos:** competencia con proveedores de compliance consolidados; venderle a Europa desde AR sin red es difícil.
- **Score: 4/10**

#### 13. Talleres de IA para adultos mayores
- **Qué es:** clases grupales para jubilados (ChatGPT/Claude para trámites, salud, comunicación).
- **Ejemplo y señal:** OpenAI Academy + Senior Planet (AARP) hacen "AI Skills Jam" **gratuitos y bilingües** (2026-09-16) con 12 meses de ChatGPT Plus regalados ([academy.openai.com](https://academy.openai.com/public/events/ai-skills-jam-for-older-adults-or-jornada-de-habilidades-de-ia-para-adultos-mayores-fresno-ca-c9yguf4sjb)); municipios y centros comunitarios ofrecen gratis (active.com, 2026).
- **Cobro y precio:** USD 5-20 por clase o contrato con municipio/PAMI/centros de jubilados.
- **Ejecución con Claude:** material simple; él dicta.
- **Tipo / h-sem:** activo, 3-6 h.
- **Capital / 1er dólar:** ~0 / 1-2 meses.
- **Cobro AR:** ✅ en pesos.
- **Riesgos:** OpenAI lo regala; baja disposición a pagar; más impacto social que negocio.
- **Score: 3/10**

#### 14. Bootcamp de IA para chicos y adolescentes (vacaciones de invierno/verano)
- **Qué es:** semana de proyectos con IA (crear un juego, una app, un video) para 12-17 años.
- **Ejemplo y señal:** iD Tech AI Experimentation Lab virtual desde USD 449/semana; camps presenciales desde USD 1.199/semana; AI Explorers Camp USD 399 (2026-07) ([codakid.com](https://codakid.com/blog/kids-coding-camps/best-ai-summer-camps-for-teens/), 2026).
- **Cobro y precio:** AR realista USD 60-150 por semana por chico.
- **Ejecución con Claude:** Claude diseña proyectos guiados; él coordina y dicta.
- **Tipo / h-sem:** activo, estacional (10-20 h las semanas de camp).
- **Capital / 1er dólar:** < USD 200 / próximas vacaciones (2026-12/2027-01).
- **Cobro AR:** ✅.
- **Riesgos:** trabajo con menores (seguros, protección de datos, cuentas de IA requieren 13/18+ años); estacional; competencia de academias de programación para chicos.
- **Score: 4/10**

#### 15. Taller "búsqueda laboral con IA" (CV, LinkedIn, entrevistas)
- **Qué es:** cohorte corta para profesionales que buscan trabajo.
- **Ejemplo y señal:** Leland "AI-Powered Job Search Bootcamp" USD 799, 6 sesiones (al 2026-10-01 **sin cohortes abiertas** — [joinleland.com](https://www.joinleland.com/live-programs/ai-powered-job-search-bootcamp)); Penn State Great Valley 3 sesiones USD 150-200 (2026).
- **Cobro y precio:** AR USD 20-60; LATAM remoto USD 50-150.
- **Ejecución con Claude:** Claude arma plantillas de CV, prompts y simulador de entrevista con un Project de Claude; él dicta.
- **Tipo / h-sem:** semi-pasivo, 3-4 h.
- **Capital / 1er dólar:** ~0 / 3-6 semanas.
- **Cobro AR:** ✅.
- **Riesgos:** público con poca plata (desempleado); muy saturado de contenido gratis; la cohorte cerrada de Leland sugiere demanda irregular.
- **Score: 4/10**

### Bloque B — Educación sobre Claude, vibe-coding y automatización

#### 16. Claude Code para no programadores, en español ("aprendé conmigo")
- **Qué es:** curso/cohorte para profesionales no técnicos que quieren construir herramientas con Claude Code; él lo enseña como alguien que aprendió sin programar.
- **Ejemplo y señal:** Maven "Claude Code Workshop: Build your first app in 4 hours" USD 299 ([maven.com/no-code-ai](https://maven.com/no-code-ai/claude-code-workshop)); "Claude Code for Beginners: 2 Day Launchpad" (Maven, 2026). En español: Imperio Digital (Benjamín Cordero) en Skool, USD 67/mes (subía a 77 el 2026-04-30), 836+ miembros, 102K suscriptores YouTube a 2026-04 ([aifunnelinsider](https://aifunnelinsider.com/imperio-digital-review-2026/) — *reseña con links de afiliado*).
- **Cobro y precio:** workshop USD 49-149 (LATAM); comunidad USD 20-40/mes.
- **Ejecución con Claude:** documenta en público sus propios proyectos del laboratorio (stack de datos, etc.) → eso es el contenido; Claude estructura el curso.
- **Tipo / h-sem:** semi-pasivo, 5-8 h (contenido continuo).
- **Capital / 1er dólar:** < USD 200 / 2-4 meses.
- **Cobro AR:** ✅ Hotmart.
- **Riesgos:** **credibilidad**: no sabe programar y compite con creadores que sí; el contenido caduca cada 1-3 meses (cambios de Claude Code); Anthropic publica cursos gratis (Anthropic Academy) y Vanderbilt tiene especialización en Coursera.
- **Score: 5/10**

#### 17. Claude Cowork para profesionales hispanos (sin terminal) ⭐
- **Qué es:** curso + packs de "personas"/carpetas listos para usar Claude Cowork (modo de trabajo de la app de escritorio) en tareas de oficina.
- **Ejemplo y señal:** Cowork Academy abrió admisión temprana en 2026-07 con packs por profesión (marketing, consultoría, inmobiliaria, contabilidad) ([accessnewswire](https://www.accessnewswire.com/newsroom/en/business-and-professional-services/cowork-academy-guided-claude-cowork-training-early-admission-now-1186878)); cursos en Udemy/Learn Formula/Varsity Tutors USD 129-199 (fast.io, 2026); Anthropic Academy tiene "Introduction to Claude Cowork". Producto muy nuevo → poca oferta en español.
- **Cobro y precio:** USD 29-99 curso; pack de plantillas USD 19-49.
- **Ejecución con Claude:** él usa Cowork en su propio trabajo; Claude escribe las instrucciones/skills de cada pack y los guiones.
- **Tipo / h-sem:** semi-pasivo, 3-5 h.
- **Capital / 1er dólar:** < USD 150 / 4-8 semanas.
- **Cobro AR:** ✅ Hotmart / Lemon Squeezy.
- **Riesgos:** ventana corta (en 6-12 meses habrá mucha oferta y Anthropic educa gratis); dependencia total de un producto de un tercero; requiere plan pago de Claude del alumno.
- **Score: 7/10**

#### 18. Curso/comunidad de n8n en español
- **Qué es:** enseñar automatizaciones con n8n.
- **Ejemplo y señal:** saturación visible: en Udemy hay decenas de cursos 2026 de n8n con 98-822 alumnos ([udemy.com](https://www.udemy.com/course/master-n8n-in-7-days/)); "AI Automation (A-Z)" en Skool con ~164.700 miembros a USD 7/mes (revenuegeeks, 2026-09-05); NoCode Startup dice +10.000 alumnos.
- **Cobro y precio:** USD 7-50/mes o USD 30-100 curso.
- **Ejecución con Claude:** Claude (con skills n8n) arma los flujos; él explica.
- **Tipo / h-sem:** semi-pasivo, 5 h.
- **Capital / 1er dólar:** bajo / 2-4 meses.
- **Cobro AR:** ✅.
- **Riesgos:** océano rojo; precios a la baja (USD 7/mes del líder); él no domina n8n.
- **Score: 3/10**

#### 19. Comunidad paga de nicho en Skool (IA para un oficio) 
- **Qué es:** comunidad con cursos + llamadas semanales para un nicho (ej. "IA para operaciones/depósitos").
- **Ejemplo y señal:** mediana de comunidades pagas ~USD 1.200/mes estimado (techo) y precio mediano USD 29 (profitable.app, 2026-09-02); 205 miembros × USD 27 es el "ganador mediano" según communipass (2026). Ojo: casos como "AI Agency Arbitrage" (USD 500/mes × 8.900 miembros) son estimaciones de precio × miembros, no facturación.
- **Cobro y precio:** USD 19-49/mes.
- **Ejecución con Claude:** Claude produce contenido semanal, resúmenes, onboarding; él anima la comunidad y da 1 llamada/semana.
- **Tipo / h-sem:** semi-pasivo con piso de trabajo (5-8 h; la comunidad muere sin anfitrión).
- **Capital / 1er dólar:** USD 9-99/mes Skool / 2-4 meses (requiere audiencia previa).
- **Cobro AR:** ⚠️ Skool paga vía Stripe → **no verificado para AR**; usar Hotmart para cobrar y Skool gratis para la comunidad.
- **Riesgos:** churn 6-9%/mes → techo ~USD 5K MRR; 67% de comunidades Skool son gratis; sin audiencia previa no arranca.
- **Score: 5/10**

#### 20. Cohorte "vibe coding para fundadores no técnicos"
- **Qué es:** enseñar a validar y construir un MVP con Lovable/Replit/Claude.
- **Ejemplo y señal:** DataCamp posiciona "Vibe Coding with Replit" para no técnicos (2026); casos citados: Plinq USD 456K ARR en 45 días con Lovable, Creator Buddy USD 300K ARR (iamjohnellison substack, 2026 — **survivorship bias puro**).
- **Cobro y precio:** USD 99-499.
- **Ejecución con Claude:** él construye en público.
- **Tipo / h-sem:** activo/semi, 5-8 h.
- **Capital / 1er dólar:** bajo / 2-4 meses.
- **Cobro AR:** ✅.
- **Riesgos:** vende sueños de startup (zona gurú); él aún no tiene un producto exitoso que mostrar; plataformas regalan tutoriales.
- **Score: 4/10**

#### 21. Workshops de 1 día / "lightning lessons" en Maven o Luma
- **Qué es:** formato corto en vivo (2-4 h) para validar un tema antes de un curso largo.
- **Ejemplo y señal:** Maven ofrece "Free Lightning Lessons" para "construir lista, validar demanda" y workshops de 1 día ([maven.com/start](https://maven.com/start?token=blog)); afirma ~USD 20K por cohorte promedio (**dato de marketing de Maven, conflicto de interés**). Ejemplos 2026: "Claude for Finance: 5-Hour Hands-On Workshop" en Luma.
- **Cobro y precio:** USD 0 (gratis para lista) a USD 49-299.
- **Ejecución con Claude:** Claude arma landing, guion, ejercicios y secuencia de mails; él dicta.
- **Tipo / h-sem:** activo, 3-6 h por workshop.
- **Capital / 1er dólar:** ~0 / 3-6 semanas.
- **Cobro AR:** ⚠️ Maven paga con Stripe (no verificado para AR); Luma igual. Alternativa: Zoom + Hotmart/Mercado Pago.
- **Riesgos:** Maven trae poco tráfico propio para principiantes; es una táctica de validación más que un negocio.
- **Score: 5/10** (como herramienta de validación de #8/#10/#17)

### Bloque C — Infoproductos, kits y plantillas

#### 22. Claude Skills empaquetadas por profesión (pack + video de instalación) ⭐
- **Qué es:** paquetes de 10-30 skills/instrucciones de Claude listas para un oficio (ej. "pack jefe de depósito", "pack estudio contable AR"), con guía de instalación y actualizaciones.
- **Ejemplo y señal:** Ryan Dozer (consultor de marketing, no técnico) vendió 25 skills a USD 99 en su web → ~USD 3.000 en 45 días sin ads ([aiblewmymind substack](https://aiblewmymind.substack.com/p/sell-claude-skills), 2026 — **la autora vende suscripción con skills: conflicto**). En Gumroad: "Master Marketing Claude Skills Bundle" 167 skills a USD 167. **Aviso:** NO existe marketplace oficial de Anthropic (verificado en agent37.com 2026-10-01); las cifras de "USD 48M en Q1 2026" que circulan son falsas o no rastreables.
- **Cobro y precio:** USD 19-99 único; o USD 9-19/mes con actualizaciones.
- **Ejecución con Claude:** Claude escribe y prueba las skills (es literalmente lo que mejor hace); él aporta el conocimiento del oficio y los casos de prueba, graba la instalación.
- **Tipo / h-sem:** semi-pasivo, 2-4 h.
- **Capital / 1er dólar:** < USD 100 / 3-6 semanas.
- **Cobro AR:** ✅ Lemon Squeezy / Gumroad / Hotmart.
- **Riesgos:** copiable al instante (son archivos de texto); "skill genérica" ≈ prompt pack (descartado) → solo funciona si es de nicho y con criterio experto; Anthropic puede lanzar skills oficiales gratis para el mismo caso.
- **Score: 7/10**

#### 23. Plantillas Excel/Sheets de inventario y stock para comercios y PyMEs
- **Qué es:** planillas listas (stock, punto de pedido, ABC, valuación, mermas) vendidas en Etsy/Hotmart/web propia.
- **Ejemplo y señal:** trackers de inventario se venden a USD 8-20 y plantillas B2B de finanzas a USD 25-75 (fungies.io; craftybase, 2026). *Sin datos de volumen verificados.*
- **Cobro y precio:** USD 9-49.
- **Ejecución con Claude:** Claude diseña fórmulas, validaciones y manual; él define la lógica de ingeniería industrial y prueba.
- **Tipo / h-sem:** pasivo-semi, 1-3 h.
- **Capital / 1er dólar:** USD 0-50 (fee Etsy USD 0,20/listing) / 1-3 meses.
- **Cobro AR:** ✅ Etsy paga a AR vía Payoneer (*no re-verificado 2026*); Hotmart ✅.
- **Riesgos:** mercado de plantillas saturado y de ticket bajo; Claude for Excel/Copilot reducen el valor de una planilla hecha. Mejor como lead magnet de #8.
- **Score: 5/10**

#### 24. Kit ISO 9001 / procedimientos (SOPs) en español para PyMEs
- **Qué es:** set de manual, procedimientos y registros editables + guía para adaptarlo con IA.
- **Ejemplo y señal:** Qlause ISO 9001 Documentation Toolkit (50 documentos) a USD 99; kits de SOP en Payhip; servicios en Fiverr de documentación ISO (2026) ([riskprofs.com](https://riskprofs.com/templates)).
- **Cobro y precio:** USD 49-199 kit; + servicio de adaptación USD 300-1.000.
- **Ejecución con Claude:** Claude redacta el sistema documental coherente; él lo revisa con criterio de gestión de calidad.
- **Tipo / h-sem:** semi-pasivo, 2-3 h.
- **Capital / 1er dólar:** < USD 100 / 2-3 meses.
- **Cobro AR:** ✅.
- **Riesgos:** consultoras ISO y Advisera dominan; un kit mal hecho daña la certificación del cliente; requiere conocer la norma (no tiene auditor).
- **Score: 5/10**

#### 25. Toolkit "Orden operativo de depósito" (5S + ABC + layout + KPIs) con mini-curso ⭐
- **Qué es:** producto digital de entrada de la consultora: plantillas + checklists de relevamiento + videos cortos, para que un dueño ordene su depósito solo.
- **Ejemplo y señal:** misma señal que #8 y #23 (hueco en español; demanda de inventario en plantillas). *Sin ejemplo directo idéntico encontrado.*
- **Cobro y precio:** USD 29-79; upsell a diagnóstico pago.
- **Ejecución con Claude:** Claude convierte su relevamiento de Sporting en método replicable (plantillas, guías, videos con guion).
- **Tipo / h-sem:** semi-pasivo, 2-3 h.
- **Capital / 1er dólar:** < USD 100 / 1-2 meses.
- **Cobro AR:** ✅.
- **Riesgos:** el dueño de PyME rara vez compra infoproductos; funciona sobre todo como embudo, no como ingreso principal.
- **Score: 7/10**

#### 26. Plantillas Notion
- **Qué es:** sistemas Notion (planner, CRM, gestión de proyectos).
- **Ejemplo y señal:** Thomas Frank > USD 2,5M; Easlo > USD 500K en 2 años (fungies.io, 2026 — sitio de un MoR con interés en promover la venta de plantillas).
- **Cobro y precio:** USD 19-79.
- **Ejecución con Claude:** Claude diseña estructura; él arma en Notion.
- **Tipo / h-sem:** pasivo, 1-2 h.
- **Capital / 1er dólar:** 0 / 2-6 meses.
- **Cobro AR:** ✅ Gumroad/Lemon.
- **Riesgos:** saturado desde 2022; Notion AI genera plantillas solo; ejemplos son survivorship.
- **Score: 2/10**

#### 27. Membresía de recursos IA para docentes (prompts, planificaciones, rúbricas)
- **Qué es:** suscripción mensual con recursos curados para docentes.
- **Ejemplo y señal:** "AI in Education Membership" de Class Tech Tips (Monica Burns) ([classtechtips.com](https://classtechtips.com/ai-for-educators-membership/)); newsletter paga "AI School Librarian" en Substack con biblioteca de prompts (2026).
- **Cobro y precio:** USD 5-15/mes.
- **Ejecución con Claude:** Claude produce material semanal; él cura y distribuye.
- **Tipo / h-sem:** semi-pasivo, 3-4 h.
- **Capital / 1er dólar:** ~0 / 3-6 meses.
- **Cobro AR:** ✅.
- **Riesgos:** docentes argentinos con sueldos bajos; Estado y Google/Microsoft regalan recursos; él no es docente.
- **Score: 3/10**

### Bloque D — Newsletters y audiencias

#### 28. Newsletter paga de nicho "IA para operaciones/PyMEs" en español
- **Qué es:** newsletter semanal con casos, herramientas y plantillas; free + plan pago.
- **Ejemplo y señal:** Substack pagó USD 450M a escritores en 2025 (vs 375M en 2024) y tenía 5M suscripciones pagas en Q1 2026 (everything-pr, 2026); conversión free→paid típica 2-5% el primer año (vantaige.io, 2026 — *secundaria*).
- **Cobro y precio:** USD 5-10/mes.
- **Ejecución con Claude:** Claude investiga y redacta borradores; él edita y agrega criterio.
- **Tipo / h-sem:** semi-pasivo, 3-5 h (cadencia obligatoria).
- **Capital / 1er dólar:** 0 / 3-9 meses.
- **Cobro AR:** ⚠️ Substack paga vía Stripe (no AR); usar Beehiiv/Ghost con cobro por Lemon Squeezy o Hotmart.
- **Riesgos:** 1.000 suscriptores gratis → 20-50 pagos (USD 100-500/mes); newsletters de IA saturadísimas en inglés; texto escrito por IA sin criterio no retiene.
- **Score: 5/10**

#### 29. Newsletter gratuita B2B con sponsors (nicho logística/PyMEs LATAM)
- **Qué es:** newsletter gratis monetizada con patrocinadores del rubro (software de inventario, transportes).
- **Ejemplo y señal:** Beehiiv distribuye > USD 1M/mes a su red de publishers (vantaige.io, 2026 — *no verificado en fuente primaria*). Sin datos de CPM hispano verificados (presupuesto de búsqueda agotado).
- **Cobro y precio:** USD 50-500 por envío según lista.
- **Ejecución con Claude:** igual que #28.
- **Tipo / h-sem:** semi-pasivo, 3-5 h.
- **Capital / 1er dólar:** 0 / 6-12 meses (necesita ~2.000-5.000 suscriptores).
- **Cobro AR:** ✅ factura E a sponsors.
- **Riesgos:** lento; sponsors hispanos escasos.
- **Score: 4/10**

### Bloque E — Plataformas de terceros

#### 30. Curso en Udemy (español)
- **Qué es:** subir curso grabado al marketplace.
- **Ejemplo y señal:** revenue share de suscripción bajó a 15% en 2026-01; 37% en ventas orgánicas, 97% con cupón propio ([teach.udemy.com](https://teach.udemy.com/enabling-investment-subscription-terms-update/)); la porción de ingresos a instructores bajó de 40% (2019) a ~24% (2024) (classcentral).
- **Cobro y precio:** USD 10-20 efectivo por venta (descuentos permanentes).
- **Ejecución con Claude:** Claude estructura; él graba.
- **Tipo / h-sem:** pasivo, 1 h.
- **Capital / 1er dólar:** 0 / 1-2 meses.
- **Cobro AR:** ✅ Payoneer/PayPal.
- **Riesgos:** ingresos marginales; plataforma recorta márgenes año a año. Útil solo como vitrina/credibilidad.
- **Score: 3/10**

#### 31. Docente/autor en plataformas hispanas (Coderhouse, Crehana, Platzi, Domestika)
- **Qué es:** ser profesor contratado (por hora o por regalías) en una plataforma con tráfico propio.
- **Ejemplo y señal:** Coderhouse vende cursos de IA/automatización a ~USD 150/mes por alumno en Buenos Aires (coderhouse.com, 2026). **No encontré datos de pago a instructores** (búsqueda sin resultados útiles) → *no verificado*.
- **Cobro y precio:** por hora de clase o regalías.
- **Ejecución con Claude:** preparación de clases.
- **Tipo / h-sem:** activo, 4-8 h.
- **Capital / 1er dólar:** 0 / 1-3 meses (proceso de selección).
- **Cobro AR:** ✅ (empresas argentinas o con pago local).
- **Riesgos:** requieren experiencia demostrable; poca autonomía; sirve como credencial y práctica docente.
- **Score: 5/10**

#### 32. Infoproducto en Hotmart (curso de IA aplicada a un oficio, mercado LATAM)
- **Qué es:** curso grabado vendido en Hotmart con su red de afiliados.
- **Ejemplo y señal:** cursos de IA movieron > R$ 140M en Hotmart en 2025, 340.000 compradores, +326% vs 2023 (startups.com.br, 2026); Hotmart lanzó Launchpad y agentes de venta IA en FIRE 26 (2026-09-10/12) con ~6.000 creadores usando el agente (dplnews, 2026).
- **Cobro y precio:** USD 20-100; comisión Hotmart ~9,9% + fee; afiliados 30-60%.
- **Ejecución con Claude:** Claude escribe curso, página de venta, mails y material para afiliados.
- **Tipo / h-sem:** semi-pasivo, 2-5 h.
- **Capital / 1er dólar:** USD 100-500 (ads de prueba) / 1-3 meses.
- **Cobro AR:** ✅ Payoneer, mínimo USD 50.
- **Riesgos:** Hotmart está lleno de "fórmula de lanzamiento" y gurús; reembolsos de 7 días; el dato de R$ 140M es mayormente Brasil; sin audiencia, dependés de ads o afiliados.
- **Score: 6/10** (es el canal de cobro recomendado para #8/#10/#17)

### Bloque F — Servicios educativos (activos)

#### 33. Diseño instruccional con IA para capacitación interna de empresas
- **Qué es:** convertir el conocimiento interno de una empresa (procedimientos, inducción, seguridad) en cursos cortos, quizzes y manuales usando IA.
- **Ejemplo y señal:** producción tradicional "hecha para vos" cuesta USD 2.000-4.000 por hora de video terminado (problemio.com, 2026); herramientas IA (Synthesia desde USD 22/mes, HeyGen) bajan el costo radicalmente (schoolmaker, 2026).
- **Cobro y precio:** USD 500-3.000 por módulo (LATAM: USD 300-1.500).
- **Ejecución con Claude:** Claude transforma documentos en guion, evaluaciones y estructura; avatar/voz con HeyGen o Higgsfield (ya conectado); él releva con el cliente (habilidad de ingeniero industrial: relevar procesos).
- **Tipo / h-sem:** activo, 8-15 h por proyecto.
- **Capital / 1er dólar:** USD 30-100/mes herramientas / 1-2 meses.
- **Cobro AR:** ✅ local y exportación.
- **Riesgos:** venta B2B lenta; competencia de agencias de e-learning; él no tiene portfolio (hacer 1-2 gratis/baratos).
- **Score: 6/10**

#### 34. Producción "llave en mano" de cursos para expertos (ghost course creator)
- **Qué es:** a un experto (contador, kinesiólogo, chef) le armás el curso completo: estructura, guiones, edición, plataforma, página de venta.
- **Ejemplo y señal:** misma referencia de precio de #33; proliferan herramientas IA de creación de cursos (CourseAI USD 29-79/mes, Tichr USD 49-99/mes — Capterra, 2026).
- **Cobro y precio:** USD 500-2.000 fijo + % de ventas opcional.
- **Ejecución con Claude:** Claude hace el 70% del trabajo de producción; él gestiona al experto y la calidad.
- **Tipo / h-sem:** activo, 10-15 h por proyecto.
- **Capital / 1er dólar:** bajo / 1-3 meses.
- **Cobro AR:** ✅.
- **Riesgos:** el experto promedio no vende → esquemas de % suelen dar 0; cobrar fijo por adelantado.
- **Score: 5/10**

#### 35. Localización/doblaje de cursos al español con IA
- **Qué es:** traducir y doblar cursos en inglés al español (o viceversa) con lip-sync IA y revisión humana.
- **Ejemplo y señal:** doblaje tradicional USD 50-150 por minuto terminado; Coursera usa HeyGen para versiones en español, francés, alemán (heygen.com); educación es la categoría #1 en Perso Dubbing: 10,8% de 316.856 proyectos (2025-01 a 2026-04) (perso.ai, 2026 — *proveedor, conflicto*).
- **Cobro y precio:** USD 5-20 por minuto (vs 50-150 tradicional).
- **Ejecución con Claude:** Claude traduce/adapta guiones y glosario; HeyGen/Higgsfield dobla; él revisa (nativo español) y entrega.
- **Tipo / h-sem:** activo, 5-10 h según volumen.
- **Capital / 1er dólar:** USD 30-100/mes herramientas / 1-2 meses.
- **Cobro AR:** ✅ exportación (Payoneer).
- **Riesgos:** las plataformas lo están automatizando ellas mismas (Coursera, Udemy) → el intermediario desaparece; precio a la baja.
- **Score: 5/10**

#### 36. Clases particulares para estudiantes de ingeniería (Investigación Operativa, Estadística, Excel) con IA
- **Qué es:** tutoría online para estudiantes de UTN/UBA/etc.; IA para generar ejercicios y explicaciones.
- **Ejemplo y señal:** mercado global de tutoría ~USD 115-120 mil millones y crecimiento 12% anual (aibusiness.vc; wise.live, 2026 — *secundarias*); la demanda se desplaza a "acompañamiento + IA".
- **Cobro y precio:** AR USD 8-20/h; grupales USD 5/h por alumno.
- **Ejecución con Claude:** Claude genera bancos de ejercicios resueltos y explicaciones; él dicta.
- **Tipo / h-sem:** activo, 5-10 h.
- **Capital / 1er dólar:** 0 / 1-3 semanas (el más rápido de la lista).
- **Cobro AR:** ✅ Mercado Pago.
- **Riesgos:** ingreso por hora bajo; los alumnos usan IA gratis; estacional (finales).
- **Score: 5/10** (cash rápido + produce material para cursos)

#### 37. Preparación para certificaciones con bancos de preguntas generados con IA
- **Qué es:** simuladores de examen y guías para certificaciones (ej. Lean Six Sigma Yellow Belt, APICS, certificaciones de IA de Microsoft) en español.
- **Ejemplo y señal:** en Udemy ya hay "AB-730 AI Business Professional — 5 practice tests 2026" con 655 preguntas ([udemy.com](https://www.udemy.com/course/ab-730-ai-business-professional-5-practice-tests-2026/)).
- **Cobro y precio:** USD 10-40.
- **Ejecución con Claude:** Claude genera y verifica preguntas; él revisa.
- **Tipo / h-sem:** pasivo, 1-2 h.
- **Capital / 1er dólar:** 0 / 1-2 meses.
- **Cobro AR:** ✅.
- **Riesgos:** derechos de las entidades certificadoras (no copiar preguntas reales); preguntas generadas con IA con errores → reseñas malas; Udemy saturado de "practice tests".
- **Score: 4/10**

#### 38. Coaching 1:1 de implementación de IA para dueños de PyME (programa de 4-8 semanas)
- **Qué es:** acompañamiento semanal al dueño para implementar 3-5 automatizaciones/usos de IA en su negocio.
- **Ejemplo y señal:** consultoría IA para small business en EE.UU.: USD 80-600/h y retainers USD 4.000-8.000/mes (unio.digital, 2026).
- **Cobro y precio:** AR USD 300-800 por programa; exterior USD 1.000-3.000.
- **Ejecución con Claude:** Claude prepara diagnóstico, plan y materiales; él acompaña. Es casi la consultora "Orden operativo" en versión educativa.
- **Tipo / h-sem:** activo, 2-3 h por cliente/semana.
- **Capital / 1er dólar:** 0 / 3-6 semanas.
- **Cobro AR:** ✅.
- **Riesgos:** solapa con la consultora ya en evaluación (no es idea nueva, es formato); requiere resultados demostrables.
- **Score: 6/10**

#### 39. Cohorte "IA para ingenieros industriales y estudiantes" (Argentina/LATAM)
- **Qué es:** curso para estudiantes/graduados recientes de ingeniería industrial: IA en relevamientos, layout, simulación simple, informes, Power BI.
- **Ejemplo y señal:** UTN Rosario dicta Power BI (cursos 2025-03, 2025-08, 2026-06) ([seuvt.frro.utn.edu.ar](https://seuvt.frro.utn.edu.ar/gestor/frm-cursos/folletos/folletoCurso_Curso%20Power%20BI%20Junio%202026.pdf)); U. de Chile "Power BI con IA – Avanzado" (2026-08-24 a 09-09); Néstor Adrianzen (Quipu Analytics) con 24K+ alumnos de Power BI/Excel en 150 países a 2025-12 (Udemy).
- **Cobro y precio:** USD 30-120.
- **Ejecución con Claude:** él es "uno de ellos" (credibilidad de par); Claude arma casos.
- **Tipo / h-sem:** semi-pasivo, 3-5 h.
- **Capital / 1er dólar:** < USD 100 / 1-3 meses (centros de estudiantes, grupos de WhatsApp de la facultad).
- **Cobro AR:** ✅.
- **Riesgos:** estudiantes con poco presupuesto; competencia con cursos de extensión universitaria baratos.
- **Score: 6/10**

#### 40. ⚠️ Programas "montá tu agencia de IA / vendé automatizaciones" (meta-gurú)
- **Qué es:** cursos/comunidades que enseñan a vender servicios de IA (AAA, "AI arbitrage").
- **Ejemplo y señal:** es la categoría que más factura en Skool (estimaciones) pero con quejas: AI Arbitrage Agency criticada en Trustpilot por "sobre-prometer" y demoras en reembolsos; la FTC demandó a Air AI por afirmaciones engañosas de ingresos (~USD 19M) (cfodive.com, 2025). Se incluye para dejarla **explícitamente descartada**.
- **Cobro y precio:** USD 97-500/mes.
- **Ejecución con Claude:** técnicamente fácil; éticamente y reputacionalmente mala.
- **Tipo / h-sem:** activo.
- **Capital / 1er dólar:** —
- **Cobro AR:** —
- **Riesgos:** **conflicto de interés estructural** (gana vendiendo el sueño, no haciendo agencia); riesgo legal por promesas de ingresos; él no tiene resultados propios.
- **Score: 1/10**

---

## Top 5 de este frente (para ESTE usuario)

1. **#8 IA aplicada a logística y depósitos (+ #25 toolkit como producto de entrada)** — 8/10. Es el único lugar donde tiene ventaja real (ingeniería industrial + caso Sporting), hay oferta en inglés a USD 750-1.500 (Georgia Tech, MIT, Loyola) y casi nada práctico en español. Además alimenta directamente la consultora "Orden operativo" (curso = embudo; toolkit = producto barato; in-company = cash).
2. **#1 Talleres in-company de IA para PyMEs argentinas** — 7/10. Cash más rápido de la lista con ticket decente; la brecha está medida (46% exige IA, 11% capacita formalmente — Trendsity/Deel 2026). Diferenciarse dando el taller "con foco en operaciones" (conecta con #8).
3. **#22 Claude Skills empaquetadas por oficio** — 7/10. Lo que mejor sabe hacer Claude es escribir skills; él aporta el criterio de oficio. Semi-pasivo, capital casi nulo, cobro desde AR resuelto (Lemon Squeezy/Gumroad). Debe ser de nicho (sino es "prompt pack", descartado).
4. **#10 Excel + IA (Claude for Excel/Copilot) para operaciones** — 7/10. Ola fresca (Claude for Excel beta 2026-05), demanda probada (Miss Excel USD 2,9M en 2024, aunque es survivorship); en español y con foco operaciones evita el océano rojo de "Excel genérico".
5. **#17 Claude Cowork para profesionales hispanos** — 7/10. Ventana nueva (Cowork Academy arrancó 2026-07, cursos USD 129-199 en inglés) y él usa la herramienta todos los días. Ventana corta: si se hace, hacerlo en los próximos 3-6 meses.

**Combinación sugerida (a validar):** un solo "sistema" — contenido corto de Excel/Claude aplicado a depósitos (#10) → toolkit USD 29-79 (#25) + pack de skills (#22) en Hotmart/Lemon → cohorte/taller (#8/#1) → consultoría Orden Operativo. Validar primero con 1-2 talleres piloto (#1) y una lightning lesson gratuita (#21) antes de grabar nada.

## Trampas comunes del frente

1. **Gurús que venden "cómo vender cursos" o "cómo montar tu agencia de IA".** Ganan con el curso, no con el método. Mayor categoría por facturación estimada en Skool y la más denunciada (Trustpilot, FTC vs Air AI). Si la fuente vende un curso sobre el tema, sus cifras no cuentan.
2. **Cifras inventadas por contenido SEO hecho con IA.** Caso detectado: el "marketplace oficial de Claude Skills con USD 48M en Q1 2026" no existe. Regla: si no se rastrea a fuente primaria, no se usa.
3. **"Revenue" de Skool = precio × miembros.** Es un techo teórico (profitable.app lo dice). Mediana real de una comunidad paga: ~USD 1.200/mes como máximo; 67% de las comunidades son gratis.
4. **Survivorship bias en los casos famosos** (Miss Excel, Thomas Frank, Easlo, Plinq). Contra eso: 46% de creadores Kajabi gana < USD 1.000/año; mediana en plataforma propia USD 2-10K/año.
5. **Credibilidad de dominio.** Vender "IA para abogados/médicos/contadores" sin serlo no funciona sin socio del oficio. Su ventaja real es ingeniería industrial/logística y "aprender Claude sin programar".
6. **Caducidad del contenido.** Cursos sobre herramientas (Claude Code, Cowork, n8n, Copilot) quedan viejos en 1-3 meses; el costo de mantenimiento es alto. Enseñar *método* (procesos, criterio) + herramienta como ejemplo.
7. **Las plataformas comen margen o no pagan a Argentina.** Udemy bajó a 15% en suscripción (2026); Skool/Maven/Substack pagan vía Stripe (no AR, no verificado en contrario). Cobrar con Hotmart, Lemon Squeezy o Mercado Pago y usar las otras solo como herramientas.
8. **Competencia gratuita de los dueños de la herramienta.** Anthropic Academy, OpenAI Academy (talleres gratis para adultos mayores con ChatGPT Plus de regalo), Microsoft y gobiernos (CABA formó +26.000 docentes) educan gratis. Solo se cobra lo aplicado a un nicho y con resultado concreto.
9. **Completion rates bajísimos en cursos grabados** (3-15% en marketplaces) → reembolsos, malas reseñas y poca recomendación. Cohortes chicas (11-25 personas) completan ~65%.
10. **Ticket en pesos vs costo en dólares.** Herramientas y ads en USD, ventas locales en ARS: priorizar B2B (empresas pagan más) y mercado LATAM/exterior en USD vía Hotmart.

## Fuentes principales (consultadas 2026-09-30 / 2026-10-01)

- Skool: [profitable.app/skool/stats](https://profitable.app/skool/stats) · [revenuegeeks.com](https://revenuegeeks.com/software/skool/statistics) · [communipass.com](https://communipass.com/?p=20194)
- Claude Skills: [agent37.com](https://www.agent37.com/blog/claude-skills-marketplace) · [aiblewmymind.substack.com](https://aiblewmymind.substack.com/p/sell-claude-skills)
- Claude for Excel: [anthropic.com/news/advancing-claude-for-financial-services](https://www.anthropic.com/news/advancing-claude-for-financial-services)
- Maven: [maven.com/no-code-ai/claude-code-workshop](https://maven.com/no-code-ai/claude-code-workshop) · [maven.com/start](https://maven.com/start?token=blog)
- Cowork: [accessnewswire.com](https://www.accessnewswire.com/newsroom/en/business-and-professional-services/cowork-academy-guided-claude-cowork-training-early-admission-now-1186878)
- Imperio Digital: [aifunnelinsider.com](https://aifunnelinsider.com/imperio-digital-review-2026/)
- PyMEs AR: [mercado.com.ar](https://mercado.com.ar/talento-y-liderazgo/pymes-argentinas-crece-la-exigencia-de-habilidades-de-ia-pero-falta-capacitacion-interna)
- Contadores/abogados AR: [ub.edu.ar](https://ub.edu.ar/sites/default/files/ia_practica_para_contadores_final.pdf) · [abogados.com.ar](https://abogados.com.ar/la-facultad-de-derecho-de-la-uca-abrio-la-inscripcion-al-posgrado-practica-legal-con-ia-generativa/38899) · [events.icaew.com](https://events.icaew.com/pd/31977/2026-generative-ai-for-accountants-learn-it-use-it-apply-it)
- Supply chain / Lean: [scl.gatech.edu](https://www.scl.gatech.edu/education/professional-education/course/gaiascp) · [luc.edu](https://www.luc.edu/executiveeducation/forindividuals/leanandartificialintelligence/)
- Miss Excel: [miss-excel.com](https://www.miss-excel.com/courses/copilot-with-miss-excel) · getlatka.com/companies/miss-excel
- Udemy: [teach.udemy.com](https://teach.udemy.com/enabling-investment-subscription-terms-update/)
- Hotmart: startups.com.br (IA en Hotmart 2025) · dplnews.com (FIRE 26) · bit4learn.com (retiros)
- Lemon Squeezy AR: [docs.lemonsqueezy.com](https://docs.lemonsqueezy.com/help/getting-started/supported-countries)
- Completion: [ruzuku.com](https://www.ruzuku.com/learn/articles/cohort-vs-self-paced-completion-study)
- Talleres: designforonline.com · cal.com/andreaslopez · unio.digital
- EU AI Act art. 4: [blog.knowbe4.com](https://blog.knowbe4.com/ai-literacy-training-from-best-practice-to-legal-requirement-under-the-new-eu-ai-act)
- Adultos mayores: [academy.openai.com](https://academy.openai.com/public/events/ai-skills-jam-for-older-adults-or-jornada-de-habilidades-de-ia-para-adultos-mayores-fresno-ca-c9yguf4sjb)
- Kids camps: [codakid.com](https://codakid.com/blog/kids-coding-camps/best-ai-summer-camps-for-teens/)
- Job search: [joinleland.com](https://www.joinleland.com/live-programs/ai-powered-job-search-bootcamp)
- Doblaje: perso.ai · heygen.com (caso Coursera)
- ISO 9001: [riskprofs.com](https://riskprofs.com/templates)
- Docentes AR: buenosaires.gob.ar (2026-04-28) · iprofesional.com (2026-06-13)
- Agencias IA / FTC: cfodive.com (Air AI) · trustpilot.com (aiarbitrageagency.com)

## Pendientes de verificación (no se pudo por límite de búsquedas)

- Si Skool y Maven pagan a cuentas argentinas (asumido NO).
- CPM/sponsors de newsletters hispanas B2B.
- Pago a instructores en Coderhouse/Crehana/Platzi/Domestika.
- Demanda real (volumen de búsqueda) de "IA para logística/depósito" en español — validar con Google Trends/Keyword Planner antes de producir.
