# Ideas rápidas (≤ 7 días al primer dólar): freelance, gigs y microtrabajo cobrando en USD

- **Fecha:** 2026-10-01 (jueves). Ventana analizada: 2026-10-01 → 2026-10-07.
- **Frente:** plataformas internacionales de freelance, entrenamiento de IA, testeo y microtrabajo, aceleradas con Claude.
- **Perfil asumido:** argentino, no programa, usa Claude a diario, formación en ingeniería industrial (relevó la logística de un depósito), capital menor a USD 300, tiene Higgsfield. Cobra con Payoneer, Mercado Pago, PayPal (limitado) y USDT (Binance P2P). Wise solo a veces.
- **Complementa a:** `research/2026-10-01-230-ideas-con-claude.md`. No repite las fichas de ese estudio: cuando una idea ya existía (B35, F1, F14, C22), acá aparece solo su **versión "cobrar esta semana"** y se aclara.

---

## 0. Metodología y la verdad incómoda

**Cómo se hizo.** Hice unas 32 búsquedas web hasta agotar la cuota de la sesión, más WebFetch sobre páginas primarias: ayuda de Contra, aitrainer.work y listados de Workana. Workana, Upwork y Fiverr devolvieron 403 al pedido directo, así que sus datos salen de fuentes secundarias fechadas en 2026. Lo que no pude confirmar está marcado **[NO VERIFICADO]**.

**La verdad incómoda (leer antes que las ideas).** La consigna mide plata **cobrada y disponible**, no "ganada". Con esa vara, **casi ninguna plataforma deja cobrar en 7 días a una cuenta nueva**:

- **Fiverr:** 14 días de clearing para vendedores nuevos, más hasta 3 días hasta que la orden se completa sola. Son ≥ 17 días aunque la venta entre hoy, y la primera venta orgánica tarda típicamente entre 4 y 10 semanas.
- **Freelancer.com:** el primer retiro tiene 15 días de clearance.
- **Workana:** con el plan gratuito se retira solo entre el 1 y el 5 de cada mes. Lo que se libere después del 2026-09-30 recién se retira del 2026-11-01 al 2026-11-05. Los planes pagos tienen retiro semanal.
- **Upwork por hora:** la semana se factura el lunes, siguen 5 días de revisión y se retira el miércoles siguiente. Si trabaja del 2026-10-01 al 2026-10-04, recién retira el **2026-10-14**.
- **Upwork precio fijo:** es lo más rápido. Después de que el cliente aprueba el hito hay 5 días de seguridad. Si consigue contrato el día 1-2 y le aprueban el día 2-3, cobra el **día 7-8**. Es justo, pero posible.
- **Entrenamiento de IA:** pagan por semana, pero el onboarding tarda de 3 a 14 días y es común la "empty queue" (cuenta aprobada sin tareas).
- **Microtareas:** en Clickworker/UHRS el saldo tarda **39 días** en ser pagable.

**Conclusión de método:** el cobro en ≤ 7 días sale por **clientes directos que pagan por rieles rápidos**: solicitud de pago de Payoneer, factura de Contra (que paga a Payoneer o PayPal en 30 minutos), PayPal o USDT. Las plataformas sirven para **sembrar ahora y cobrar en 2-5 semanas**. La lista lo refleja sin endulzarlo.

**Score (1-10):** velocidad al cobro × probabilidad de cobrar en 7 días × USD/hora realista, **para este usuario** (no programa; nivel de inglés a confirmar).

**Requisito transversal que no pude verificar:** su nivel de inglés escrito y oral. Casi todo lo que paga en USD lo pide. Donde es crítico, lo marco con **(EN)**.

---

## 1. Rieles de cobro (definen todo lo demás)

| Riel | Velocidad real | Costo | Nota AR |
|---|---|---|---|
| Payoneer (desde Upwork) | Minutos u horas | Comisión de conversión 0,75% al retirar en AR (fuente: jonatanalmeira.com, 2026) | Hay acuerdo Payoneer–Santander AR para retirar a una cuenta en USD |
| Payoneer "solicitud de pago" a un cliente directo | 1-3 días según cómo pague el cliente | Si paga con tarjeta, ~3-4% [NO VERIFICADO] | Sirve para clientes fuera de plataforma |
| Contra (factura a cliente propio) | PayPal/Payoneer: **30 min (rápido)** o 4 días hábiles (estándar, con 4 días de "safety-clearance"). Si el cliente paga por ACH: +3-5 días hábiles | 0% de comisión al freelancer; tope de USD 3 por retiro a Payoneer | Lo mejor para cobrar rápido a un cliente propio |
| PayPal | Inmediato en saldo; retiro a CBU en 24-72 h hábiles, **en pesos** | 5,4% + USD 0,30 por cobro internacional | No entrega USD físicos |
| USDT (Binance Pay / transferencia) | Minutos | Casi 0 | Solo clientes cripto-nativos; ojo con estafas |
| Mercado Pago | Inmediato (pesos) | — | No recibe SWIFT. Del exterior solo por Western Union o vía PayPal/Airtm |

Fuentes: [Contra – plazos de payout](https://help.contra.com/en/articles/10008642-payout-timelines-for-freelancers-on-contra) (consultado 2026-10-01); [Contra – métodos](https://help.contra.com/en/articles/10008642-payout-methods-on-contra); [Calculadora PayPal AR](https://www.jonatanalmeira.com/calculadora-paypal-argentina/) (2026); [Payoneer–Santander AR](https://www.payoneer.com/es/resources/business/payoneer-y-santander-argentina/); [Recibir del exterior en Mercado Pago (2026)](https://www.jonatanalmeira.com/?p=65154).

---

## 2. Lista de ideas (39)

> Formato compacto. **Plan 7d** = qué hacer cada día. **1er cobro** = días hasta tener la plata disponible (no "ganada") y probabilidad de lograrlo en 7 días.

### Bloque A — Cliente directo con riel rápido (lo único que cobra en 7 días con probabilidad razonable)

**1. "Arreglo tu planilla en 48 h" a precio fijo, vendido por red y LinkedIn y cobrado por Contra o Payoneer**
- **Qué es:** arreglar o armar una planilla de Excel/Google Sheets (fórmulas, tablas dinámicas, un tablero simple, control de stock) a precio fijo, para dueños hispanohablantes de EE.UU., España o LATAM que pagan en USD.
- **Demanda:** en Upwork, la categoría "AI Integration & Automation" creció ~90% y la de preparación de datos crece fuerte ([Upwork In-Demand Skills 2026](https://investors.upwork.com/news-releases/news-release-details/upworks-demand-skills-2026-demand-top-ai-skills-more-doubles-ai)). Excel es la tarea chica más pedida en todas las plataformas [conteo NO VERIFICADO: 403 al listar].
- **Precio:** USD 40-150 por arreglo.
- **Plan 7d:**
  - D1: arma un perfil de Contra con 3 ejemplos hechos con Claude (inventario, ABC, flujo de caja) y anota 40 contactos cálidos (exjefes, conocidos con negocio en el exterior, familiares emigrados).
  - D2: manda 40 mensajes personales con oferta cerrada ("USD 60, entrego en 48 h, pagás al aprobar").
  - D3: manda 30 mensajes más en LinkedIn y en grupos de emprendedores hispanos de EE.UU. y España.
  - D4-D5: entrega a los primeros 1-2 clientes.
  - D6: factura por Contra con payout rápido a Payoneer.
  - D7: pide testimonio y referido.
- **Claude / él:** Claude escribe fórmulas, Apps Script y el tutorial de uso. Él diagnostica, testea cada fórmula con datos reales, habla con el cliente y garantiza el resultado.
- **Capital:** USD 0.
- **1er cobro:** 3-6 días. Probabilidad: **media**. Depende 100% de su red.
- **Techo y puente:** es la puerta directa a "Orden Operativo"/Stock Sano. El mejor puente del informe.
- **Riesgos:** su red puede ser chica. Una fórmula mal hecha con IA quema el contacto. Si el cliente paga por ACH, se suman 3-5 días.
- **Score: 7**

**2. Documentar 3 procesos (SOP) en 72 h para una PyME hispana, con cobro directo**
- **Qué es:** versión rápida de C22: un paquete fijo de "3 SOPs + checklist + diagrama" para negocios de servicios (limpieza, construcción, logística) de dueños hispanos en EE.UU.
- **Demanda:** la documentación de procesos para PyMEs se contrata en Upwork, aunque no pude abrir los listados [NO VERIFICADO].
- **Precio:** USD 120-300 el paquete.
- **Plan 7d:**
  - D1: hace un SOP de ejemplo con su relevamiento del depósito (anonimizado).
  - D2-D3: ofrece el paquete por red y LinkedIn, a 50 personas.
  - D4: hace una llamada de relevamiento de 45 min (Claude transcribe y estructura).
  - D5: entrega.
  - D6: factura por Contra.
- **Claude / él:** Claude estructura y redacta. Él hace la entrevista, valida contra la realidad y cuida el formato.
- **Capital:** 0.
- **1er cobro:** 5-8 días. Probabilidad: **media-baja**. El ticket es más alto y el ciclo de venta más largo.
- **Techo y puente:** máximo, es el corazón de la consultora.
- **Riesgos:** el cliente posterga la entrevista.
- **Score: 6,5**

**3. Traducción y localización EN↔ES con post-edición, para contactos y agencias chicas**
- **Qué es:** traducir y localizar textos cortos (web, mails, formularios, menús, fichas de producto) con borrador de Claude y post-edición humana.
- **Demanda:** en Workana hay proyectos de traducción ES↔EN, con presupuestos muy dispares, desde USD 0,02/palabra ([listado de Workana](https://www.workana.com/job/spanish-to-english-translation-and-editing-projects-1), consultado 2026-10-01).
- **Precio:** USD 0,03-0,08/palabra directo; lo típico son USD 30-120 por pedido.
- **Plan 7d:**
  - D1: arma una tarifa cerrada ("hasta 1.000 palabras, USD 50, 24 h").
  - D2-D3: ofrece a 30 contactos y a 10 agencias de marketing hispanas (mail frío corto).
  - D4-D6: entrega.
  - D6-D7: cobra por PayPal o Contra.
- **Claude / él:** Claude traduce. Él post-edita frase por frase y adapta al país.
- **Capital:** 0.
- **1er cobro:** 4-7 días. Probabilidad: **media-baja**.
- **Techo:** bajo. Es un commodity que paga cada vez menos. Puente al de fondo: débil.
- **Riesgos:** **(EN)** obligatorio para EN→ES de calidad. Si el cliente no sabe que se usó IA, hay que avisarle (ética y contrato).
- **Score: 5,5**

**4. Pedidos chicos de Reddit (r/forhire, r/HireaWriter, r/slavelabour) cobrados por PayPal**
- **Qué es:** responder pedidos chicos de data entry, investigación, edición o transcripción cobrados por PayPal. Son los "dólares más rápidos" que existen, pero mal pagos.
- **Demanda:** hilos diarios de [Hiring] en esos subreddits [volumen NO VERIFICADO en esta sesión]. r/slavelabour tiene pedidos de USD 5-50.
- **Precio:** USD 5-80 por tarea.
- **Plan 7d:**
  - D1: arma una cuenta de Reddit con historial genuino, aunque una cuenta nueva genera desconfianza.
  - D1-D7: responde 5-10 posts por día.
  - Pide el pago por PayPal "goods & services" y solo por tareas chicas, para cortar pérdidas.
- **Claude / él:** Claude hace el borrador. Él verifica y entrega.
- **Capital:** 0.
- **1er cobro:** 2-6 días. Probabilidad: **media**, por montos chicos (USD 10-50).
- **Techo:** muy bajo. Puente: casi nulo.
- **Riesgos:** estafas (trabajo entregado sin pago, cheques falsos, "pagame un fee"), 5,4% + USD 0,30 de PayPal, **pedidos de tareas académicas (rechazarlos, excluidos por ética)**.
- **Score: 5**

**5. Moderación y community management en español para comunidades de Discord/Telegram, cobrado en USDT**
- **Qué es:** moderar en turnos y responder FAQs en español para comunidades de software o juegos que se expanden a LATAM.
- **Demanda:** [NO VERIFICADO en esta sesión]. Es un pedido recurrente en servidores de "jobs" de Discord.
- **Precio:** USD 3-8/h o USD 150-400/mes.
- **Plan 7d:**
  - D1-D2: lista proyectos con comunidad hispana creciente que **no** sean tokens especulativos.
  - D3: escribe a los community managers.
  - D4-D7: hace un turno de prueba pago semanal.
- **Claude / él:** Claude arma la base de FAQs y los borradores. Él modera en vivo.
- **Capital:** 0.
- **1er cobro:** 5-10 días. Probabilidad: **baja**.
- **Techo:** bajo. Puente: nulo.
- **Riesgos:** **la mayoría de las ofertas pagas en USDT vienen de proyectos cripto especulativos o directamente estafas, que están excluidos**. Es un trabajo atado al reloj.
- **Score: 3**

**6. Cobro directo a negocios hispanos de EE.UU. para traducir formularios, cartelería y web al español**
- **Qué es:** una variante nicho de la #3, con oferta cerrada para negocios de EE.UU. que atienden a clientes hispanos.
- **Precio:** USD 50-200.
- **Plan 7d:**
  - D1: Claude arma una lista de 100 negocios desde Google Maps con datos públicos.
  - D2-D4: les escribe por mail o formulario de contacto.
  - D5-D7: entrega y cobra con solicitud de pago de Payoneer.
- **Claude / él:** Claude arma la lista y los borradores. Él hace la post-edición y el contacto.
- **Capital:** 0.
- **1er cobro:** 5-9 días. Probabilidad: **baja**, porque la conversión en frío es del 0,5-2%.
- **Techo:** medio. Puente al de fondo: medio (F34 en el estudio anterior).
- **Riesgos:** reglas anti-spam (CAN-SPAM), baja tasa de respuesta.
- **Score: 4,5**

### Bloque B — Upwork (la plataforma más rápida para cobrar; el plazo real es de 7-14 días)

Datos comunes a todo el bloque:
- **Connects:** USD 0,15 cada uno; una propuesta cuesta entre 2 y 16+. Las cuentas nuevas reciben unos 60 iniciales (fuentes no oficiales; [unilink 2026](https://www.unilink.us/blog/upwork-connects-explained-2026)). Hay una bonificación de 18 Connects si gasta 54.
- **Plazos:** el precio fijo tiene 5 días de seguridad después de la aprobación; si el cliente no hace nada, se libera solo a los 14 días. Por hora: se factura el lunes y se retira el miércoles siguiente ([gigradar](https://gigradar.io/blog/how-to-get-paid-on-upwork), [aiproposer](https://aiproposer.com/guides/upwork-strategy/upwork-payment-methods), 2026).
- **Aprobación del perfil:** puede ser rechazado si las skills son "genéricas y ya cubiertas". La verificación de identidad incluye una videollamada ([websitebuilderinsider](https://www.websitebuilderinsider.com/why-is-upwork-not-approving-my-profile/)).
- **Comisión:** ~10-15% variable [NO VERIFICADO 2026].
- **Regla de ToS:** prohibido llevarse fuera de Upwork a un cliente que conoció ahí.
- **Presupuesto sugerido:** USD 15-30 en Connects.
- **Cuello de botella:** aunque todo salga perfecto, el primer cobro de Upwork cae entre el **día 7 y el 9** si el contrato es de precio fijo y se firma el día 1-2. Por hora, el primer retiro es el **2026-10-14**.

**7. Upwork: arreglos de Excel/Google Sheets a precio fijo**
- **Demanda:** "AI Data Annotation & Labeling" creció 154% interanual y la preparación de datos está entre las skills de mayor crecimiento ([Upwork 2026](https://investors.upwork.com/news-releases/news-release-details/upworks-demand-skills-2026-demand-top-ai-skills-more-doubles-ai)).
- **Precio:** USD 30-150.
- **Plan 7d:**
  - D1: arma el perfil enfocado en "Excel/Sheets para operaciones e inventario" y un portfolio de 3 planillas.
  - D1-D3: manda 10-15 propuestas por día a trabajos de menos de 24 h con presupuesto de USD 30-100, siempre con una muestra del arreglo hecha en la propuesta (Claude la arma).
  - D3-D4: entrega en el día.
  - D4: pide la aprobación del hito.
  - D9: cobra.
- **1er cobro:** 7-10 días. Probabilidad: **media-baja**.
- **Techo y puente:** alto como puente. Los clientes de inventario son el embudo natural de la consultora.
- **Riesgos:** rechazo del perfil, competencia de Asia a USD 5-10/h, fórmulas mal hechas.
- **Score: 6**

**8. Upwork: limpieza y normalización de datos (CSV, CRM, catálogos de SKUs)**
- **Qué es:** deduplicar, normalizar y separar columnas. Versión rápida de D5 del estudio anterior.
- **Precio:** USD 25-120 por lote.
- **Plan 7d:** igual que la #7, apuntando a "data cleaning" y "CRM cleanup".
- **Claude / él:** Claude propone las reglas y fórmulas. Él verifica una muestra del 100% de las filas críticas.
- **1er cobro:** 7-10 días. Probabilidad: **media-baja**.
- **Puente:** alto (datos maestros = Orden Operativo).
- **Riesgos:** datos personales de terceros (no subirlos a herramientas no autorizadas por el cliente).
- **Score: 5,5**

**9. Upwork: post-edición y proofreading de contenido en español generado por IA**
- **Qué es:** corregir estilo, regionalismos y errores de contenido IA en español.
- **Ética:** se vende como **edición de calidad, no como "esquivar detectores"**. Los pedidos de "hacer indetectable una tarea o tesis" se rechazan.
- **Precio:** USD 0,01-0,03/palabra o USD 15-25/h.
- **Plan 7d:** igual que la #7, con 3 muestras antes/después.
- **1er cobro:** 7-10 días. Probabilidad: **media-baja**.
- **Techo:** bajo. Puente: bajo.
- **Riesgos:** demanda en baja porque los modelos escriben mejor en español cada año. Muchos pedidos son académicos (excluidos).
- **Score: 4,5**

**10. Upwork: traducción EN↔ES**
- **Qué es:** la #3, pero dentro de la plataforma.
- **Precio:** USD 0,02-0,08/palabra.
- **1er cobro:** 7-10 días. Probabilidad: **baja-media**, por la enorme competencia de nativos.
- **Score: 4,5**

**11. Upwork: subtítulos SRT en español (transcripción automática + corrección humana)**
- **Precio:** USD 1-3 por minuto de video.
- **Plan 7d:** perfil y propuestas a trabajos de "Spanish subtitles". Entrega en 24 h.
- **Claude / él:** Whisper o herramientas gratis hacen el borrador. Claude corrige la terminología. Él sincroniza y revisa.
- **1er cobro:** 7-10 días. Probabilidad: **baja-media**.
- **Riesgos:** YouTube y las plataformas lo automatizan (ver E16 del estudio anterior).
- **Score: 4**

**12. Upwork: lead lists e investigación web B2B (LATAM y España)**
- **Qué es:** listas de empresas con decisor, web y datos públicos, verificadas a mano.
- **Precio:** USD 50-200 por lista de 100-300 filas.
- **1er cobro:** 7-10 días. Probabilidad: **baja-media**.
- **Puente:** bajo-medio (aprende a prospectar, que le sirve después).
- **Riesgos:** GDPR y datos personales en España, scraping contra ToS de LinkedIn (**no scrapear LinkedIn**), clientes que la usan para spam.
- **Score: 4,5**

**13. Upwork: presentaciones en Google Slides/PowerPoint a partir de contenido del cliente**
- **Precio:** USD 50-150.
- **Claude / él:** Claude arma la estructura y el .pptx. Él cuida el diseño y la coherencia.
- **1er cobro:** 7-10 días. Probabilidad: **baja-media**.
- **Riesgos:** Gamma, Canva y Copilot lo hacen solo (E10 del estudio anterior, score 4).
- **Score: 4**

**14. Upwork: setup de Claude Projects, Skills o un GPT para un negocio chico**
- **Qué es:** versión rápida de B35/D3: un micro-gig de "te dejo armado tu Claude Project con tus documentos y 10 prompts en 48 h".
- **Demanda:** en Upwork, las menciones de Claude crecieron 372% y las de Claude Code 8.162% entre el 1er semestre de 2025 y el 1er semestre de 2026 ([UpHunt, state of AI on Upwork 2026](https://uphunt.io/blog/state-of-ai-on-upwork-2026)). Hay gigs equivalentes publicados en [Fiverr](https://fiverr.com/josh_d4v/do-claude-ai-setup-automation-and-workflow-configuration-for-business).
- **Precio:** USD 75-250.
- **1er cobro:** 7-10 días. Probabilidad: **baja-media**, porque compite con devs y le falta portfolio.
- **Techo y puente:** alto (F4 del estudio anterior, score 8).
- **Riesgos:** **(EN)**, prometer integraciones que requieren código.
- **Score: 5,5**

**15. Upwork: QA y testing de chatbots en español**
- **Qué es:** versión rápida de F14: "pruebo tu bot con 100 casos en español y te entrego un informe".
- **Precio:** USD 50-200.
- **1er cobro:** 7-10 días. Probabilidad: **baja**, porque hay pocos pedidos públicos [NO VERIFICADO].
- **Puente:** medio.
- **Score: 4**

**16. Upwork: carga de catálogo y descripciones de producto en español (Shopify/WooCommerce)**
- **Precio:** USD 0,5-3 por producto (lotes de USD 50-150).
- **Claude / él:** Claude redacta las fichas desde una planilla. Él carga y revisa.
- **1er cobro:** 7-10 días. Probabilidad: **baja-media**.
- **Puente:** bajo-medio (E6 y F10 del estudio anterior).
- **Score: 4,5**

**17. Upwork: asistente virtual o soporte al cliente por chat bilingüe, por hora**
- **Precio:** USD 5-12/h.
- **1er cobro:** **13+ días** (ciclo semanal por hora: primer retiro el 2026-10-14). Probabilidad en 7 días: **muy baja**.
- **Puente:** bajo. Es casi un empleo atado al reloj.
- **Score: 3**

### Bloque C — Workana, Fiverr, Freelancer, PeoplePerHour, Malt, 99designs (sembrar, no cobrar esta semana)

**18. Workana: Excel, redacción o transcripción para clientes de LATAM en español**
- **Demanda:** hay proyectos en español de traducción, transcripción y redacción ([ejemplo de transcripción](https://www.workana.com/job/transcripcion-de-videos-20), [ejemplo de traducción](https://www.workana.com/es/job/redactor-y-traductor-bilingue-textos-claros-y-bien-escritos), consultados 2026-10-01). Las tarifas son muy bajas, por ejemplo USD 0,02/palabra o USD 6/h.
- **Comisión:** arranca en 20% y puede bajar hasta 5%.
- **Plan gratis:** pocas propuestas por semana ([ARQ](https://www.arqfinance.com/es-AR/blog/freelancer-tips/flexjobs-vs-workana), [Xolo 2026](https://blog.xolo.io/es/7-mejores-plataformas-para-trabajos-freelance-espanol-2026)).
- **Retiro:** con el plan gratis, solo del 1 al 5 de cada mes [parcialmente verificado vía global66; NO VERIFICADO en la ayuda oficial].
- **1er cobro:** **~31-35 días** (ventana del 2026-11-01 al 2026-11-05). Probabilidad en 7 días: **muy baja**, salvo que pague un plan con retiro semanal [precio NO VERIFICADO].
- **Puente:** medio, porque hay clientes PyME de LATAM.
- **Riesgos:** **estafas de "presupuesto USD 4.000, 10 vacantes"** ([ejemplo de patrón](https://www.workana.com/job/freelancers-needed-for-typing-and-translation-job-budget-4000-10-slots-available-no-scammers-needed-please-1)) y pedidos académicos con normas APA, **excluidos** ([ejemplo](https://www.workana.com/es/job/mileidy-rosario-redaccion-de-texto-utilizando-normas-apa)).
- **Score: 3,5** (sembrar ahora)

**19. Fiverr: gig de "Claude/Excel para operaciones en español"**
- **Datos de la plataforma:** 20% fijo de comisión. 14 días de clearing para vendedores nuevos (7 en nivel 1-2). La primera orden orgánica tarda típicamente 4-10 semanas. Retiro a Payoneer con USD 1 de costo ([vaultleap 2026](https://vaultleap.com/blog/fiverr-fees-explained-2026), [conductatlas – ToS](https://conductatlas.com/platform/fiverr/fiverr-terms-of-service/payment-clearance-period-14-day-hold/), [walletgrower 2026](https://walletgrower.com/blog/fiverr-review-2026)).
- **1er cobro:** **≥ 17 días** en el mejor caso; realista, 5-10 semanas. Probabilidad en 7 días: **nula**.
- **Recomendación:** publicar el gig igual el día 1 (cuesta 2 h) como opción a 1-2 meses.
- **Score: 2,5**

**20. Freelancer.com: concursos y proyectos chicos**
- **Datos:** el primer retiro tiene 15 días de clearance, aunque el retiro "Express" en pesos está disponible para AR ([soporte de Freelancer](https://www.freelancer.com.au/support/Payments/express-withdrawals)).
- **1er cobro:** ≥ 16 días. Probabilidad en 7 días: **nula**.
- **Riesgos:** reputación de lowballing y de cuentas falsas.
- **Score: 2**

**21. PeoplePerHour y Malt**
- **Qué son:** clientes del Reino Unido y Europa. Malt está muy orientado a residentes de la UE.
- **1er cobro:** PeoplePerHour [plazos NO VERIFICADO]. Probabilidad en 7 días: **muy baja**, porque hay aprobación de perfil y poco volumen en español.
- **Score: 2**

**22. 99designs y concursos de diseño con Higgsfield**
- **1er cobro:** [NO VERIFICADO] Además de ganar el concurso, hay que pasar el traspaso de archivos y el período de liberación.
- **Riesgos:** las políticas sobre diseños generados por IA en concursos están [NO VERIFICADO; probablemente restringidos] y los derechos de imagen son poco claros. Sin oficio de diseño, la tasa de éxito es muy baja.
- **Score: 1,5**

**23. Contra como marketplace (no como facturador)**
- **Qué es:** publicar servicios en Contra para que lleguen clientes. La factura a clientes propios ya está en la #1.
- **Datos:** 0% de comisión. Payout a Payoneer o PayPal en 30 minutos con la opción rápida, o 4 días ([ayuda de Contra](https://help.contra.com/en/articles/10008642-payout-timelines-for-freelancers-on-contra)).
- **Probabilidad:** baja. El tráfico orgánico de clientes es bajo y está sesgado a diseño y desarrollo.
- **Score: 3** (como marketplace) / **parte esencial de la #1** (como facturador)

### Bloque D — Entrenamiento y evaluación de IA (alto USD/h, onboarding lento: una lotería en 7 días)

Contexto: el estudio anterior ya puntuó 7 al rol de evaluador en español (F1). Acá solo cuenta la **velocidad**.

**24. Alignerr (Labelbox)**
- **Datos:** el onboarding "suele dar resultado en el mismo día". Paga por semana vía Deel. Es global salvo ~2 docenas de países bloqueados ([aitrainer.work, 2026-10-01](https://aitrainer.work/guides/best-ai-training-platforms-reviewed)). Para AR hay roles de USD 20-40/h ([aitrainer.work/jobs/argentina](https://aitrainer.work/jobs/argentina)).
- **Plan 7d:** D1 aplica a 3-5 roles (generalista en español, operaciones/logística si existe). D2-D3 hace las evaluaciones. D4-D7 hace tareas si se las asignan.
- **1er cobro:** 7-14 días. Probabilidad en 7 días: **baja**.
- **Puente:** bajo, pero da caja en USD.
- **Riesgos:** usar Claude para resolver las tareas suele **violar las reglas del proyecto** y es causa de baneo. Volumen de tareas irregular.
- **Score: 4,5**

**25. Outlier (Scale AI)**
- **Datos:** disponible en AR. Paga los martes por PayPal o **Airtm**, a ~USD 20/h ([raenest 2026](https://www.raenest.com/es-ar/blog/outlier-ai-vs-handshake-ai)). El onboarding tarda 3-14 días y es común quedar semanas en "onboarding" o con "empty queue".
- **Contexto de la empresa:** la tarifa efectiva cayó de ~USD 50/h a ~USD 20/h en 2025-12. Google y OpenAI cortaron contratos con Scale después del deal con Meta, y Scale pivotea a defensa ([breakingeven](https://breakingeven.online/platforms/outlier), [aitrainer.work news](https://aitrainer.work/news/scale-ai-fallout-surge-ai-hyper-growth)).
- **1er cobro:** 7-21+ días. Probabilidad en 7 días: **baja**.
- **Score: 3,5**

**26. Mercor: evaluador bilingüe o experto lingüístico en español**
- **Datos:** hay roles de USD 25-35/h ("Internet-Native Bilingual Evaluator, Spanish LATAM") y de USD 40-60/h ("Spanish Linguistic Expert", publicado ~2026-09-10). Paga por semana vía Stripe o Wise. El proceso es una entrevista con IA ([aitrainer.work](https://aitrainer.work/jobs/argentina)).
- **1er cobro:** 10-30 días. Probabilidad en 7 días: **baja**.
- **Riesgos:** el payout a AR por Wise no siempre funciona [método AR NO VERIFICADO].
- **Score: 4**

**27. Micro1**
- **Datos:** mediana de USD 67,50/h. Pagos cada 2 semanas por Deel. Entrevista con IA ("Zara") y **hasta 30 días** de revisión ([aitrainer.work](https://aitrainer.work/guides/best-ai-training-platforms-reviewed)).
- **1er cobro:** 3-6 semanas. Probabilidad en 7 días: **muy baja**.
- **Score: 2,5**

**28. Meridial: experto en español rioplatense o en dialectos (cordobés, litoraleño)**
- **Datos:** roles de USD 6-70/h para AR y Uruguay, publicados hace ~52 días (alrededor del 2026-08-10) ([aitrainer.work/jobs/argentina](https://aitrainer.work/jobs/argentina)).
- **Ventaja:** que sea argentino es justamente el requisito.
- **1er cobro:** [NO VERIFICADO]. Probabilidad en 7 días: **baja**.
- **Score: 3,5** (aplicar sí o sí: 30 min)

**29. AfterQuery: contribuidor de audio bilingüe ES/EN**
- **Datos:** USD 40-60/h según el listado ([aitrainer.work](https://aitrainer.work/jobs/argentina)). Pagos [NO VERIFICADO].
- **Probabilidad en 7 días:** **baja**. **(EN oral)**
- **Score: 3**

**30. TELUS Digital AI Community: evaluador de búsquedas y QA rater**
- **Datos:** USD 9/h en México y EUR 18/h en España. Pide **5 años de residencia en el país** del rol, y los roles para AR están [NO VERIFICADO]. Paga mensual [NO VERIFICADO] ([workingnomads](https://www.workingnomads.com/jobs/quality-assurance-rater-spanish-spain-telus-digital)).
- **1er cobro:** 4-8 semanas. Probabilidad en 7 días: **nula**.
- **Score: 2**

**31. OneForma (Centific) y tareas UHRS**
- **Datos:** ciclo mensual del 26 al 25, pago mensual por Payoneer. PayPal tiene tope de USD 300/año ([OneForma](https://www.oneforma.com/help-center/project-help/how-to-set-up-payoneer-payment-method-on-oneforma/)).
- **1er cobro:** ≥ 4-8 semanas (ciclo del 2026-09-26 al 2026-10-25 y pago posterior). Probabilidad en 7 días: **nula**.
- **Score: 2**

> **Excluida: DataAnnotation.** Solo acepta EE.UU., Reino Unido, Canadá, Australia, Nueva Zelanda e Irlanda, y usar VPN se banea ([aitrainer.work](https://aitrainer.work/guides/is-dataannotation-legit-review)).
>
> **Remotasks:** obsoleta; la empresa la reemplazó por Outlier.
>
> **Handshake AI:** solo EE.UU.

### Bloque E — Testeo de usabilidad, crowdtesting e investigación paga

**32. Trymata (ex TryMyUI)**
- **Datos:** USD 5-30 por test (típico USD 10). Paga **los viernes por PayPal**, incluidos los tests de esa misma semana ([sidehusl](https://sidehusl.com/trymata/), [thebudgetdiet](https://www.thebudgetdiet.com/trymyui-review)).
- **Plan 7d:** D1 se registra y hace el test de calificación. D2-D7 entra a diario a buscar tests. Le pagan el viernes 2026-10-09.
- **1er cobro:** 8-9 días. Probabilidad en 7 días: **baja-media**, y el monto es chico (USD 10-30).
- **Riesgos:** **(EN oral)**, poca oferta de tests para AR [NO VERIFICADO], 5,4% de PayPal.
- **Score: 4,5**

**33. Userfeel**
- **Datos:** USD 10 por un test de 20 min (USD 3-30 según duración). Acredita a la billetera ~1 semana después y de ahí se pasa a PayPal cuando quiera ([sidehusl](https://sidehusl.com/userfeel/)). Hay tests en varios idiomas, español incluido [NO VERIFICADO].
- **1er cobro:** 7-10 días. Probabilidad en 7 días: **baja-media**.
- **Score: 4,5**

**34. Userlytics**
- **Datos:** USD 5-90 por test. Paga por PayPal cada 2 semanas o hasta 30 días después. Disponible donde opere PayPal (AR sí) ([moneypantry](https://moneypantry.com/sites-like-usertesting/), [Userlytics, países](https://remove.userlytics.com/helpcenter/testers/what-countries-are-supported-for-testers/)).
- **1er cobro:** 14-30 días. Probabilidad en 7 días: **muy baja**.
- **Score: 3**

**35. UserTesting**
- **Datos:** PayPal **~14 días después** del test ([ayuda de UserTesting](https://help.usertesting.com/hc/en-us/articles/11880240002845)).
- **1er cobro:** ≥ 14 días. Probabilidad en 7 días: **nula**.
- **Score: 2,5** (sembrar)

**36. Crowdtesting: uTest y Test IO**
- **Datos:** uTest paga ~USD 5 por bug y USD 5-50 por caso, los días **15 y último de cada mes**, por PayPal o Payoneer ([selfmadesuccess, 2026-08-24](https://selfmadesuccess.com/utest-review/)). Test IO paga en más de 100 países ([Trolley](https://trolley.com/success-stories/test-io-global-payouts/)).
- **1er cobro:** el 2026-10-15 en el mejor caso. Probabilidad en 7 días: **nula**. En 15 días: baja.
- **Puente:** bajo, aunque el testing metódico encaja con su perfil.
- **Score: 2,5**

**37. Respondent: entrevistas pagas B2B como "profesional de logística u operaciones"**
- **Datos:** incentivo promedio de ~USD 100 por estudio (rango USD 5-1.000). El pago se procesa en 5-10 días hábiles con tarjeta Visa virtual; PayPal se habría eliminado ([sidehusl](https://sidehusl.com/respondent/), [joingerald](https://joingerald.com/learn/work--income/respondent-io-reviews-legit)). **No pude verificar la elegibilidad para AR.**
- **Ventaja:** su perfil de ingeniería industrial y depósito califica para estudios de software de WMS y supply chain. Es el **mejor USD/h del bloque**.
- **1er cobro:** 10-20 días. Probabilidad en 7 días: **muy baja**.
- **Score: 3,5**

> **Prolific:** no pude verificar si AR está entre los países aceptados (la búsqueda devolvió un resultado espurio) → **[NO VERIFICADO]**. Igual paga poco (~USD 8-12/h) y requiere PayPal.

### Bloque F — Transcripción, traducción en plataforma y microtareas

**38. GoTranscript: transcripción en español**
- **Datos:** paga **los viernes por PayPal o Payoneer**. Rango de USD 0,60-1,00 por minuto de audio; español "hasta" USD 1,75/min. Ingreso con quiz más una transcripción de prueba ([GoTranscript, empleo en español](https://gotranscript.com/spanish-transcription-job), [lilachbullock](https://www.lilachbullock.com/how-transcription-jobs-gotranscript-work/)).
- **Ingreso real:** USD 2-5/h, porque 1 minuto de audio lleva 4-6 minutos de trabajo [estimación].
- **1er cobro:** 9-16 días (viernes 2026-10-09 o 2026-10-16 si aprueba rápido). Probabilidad en 7 días: **baja**.
- **Riesgos:** **usar transcripción automática y subirla como propia probablemente viole sus reglas** [NO VERIFICADO], con baneo y pérdida del saldo.
- **Score: 3**

**39. Gengo y Clickworker/UHRS (juntas: no sirven para esta semana)**
- **Gengo:** paga USD 0,03-0,12/palabra. La revisión del test tarda ~7 días y los payouts son los días 10 y 25 → primer cobro el **2026-10-25** en el mejor caso ([realwaystoearnmoneyonline](https://realwaystoearnmoneyonline.com/become-translator-for-mygengo/)). Entregar traducción automática como humana viola sus reglas.
- **Clickworker/UHRS:** el saldo se vuelve pagable **a los 39 días** y se cierran registros por país ([soporte de Clickworker](https://support-workplace.clickworker.com/support/solutions/articles/80000672346-how-do-i-get-paid-for-my-work-)).
- **Microworkers y Picoworkers:** pagan centavos por tarea.
- **Score: 1,5**

---

## 3. Top 5 para cobrar esta semana (2026-10-01 → 2026-10-07)

La estrategia es **hacer en paralelo** una cosa que cobra rápido (cliente directo) y varias que siembran (plataformas), porque la plata "en 7 días" depende de rieles directos.

1. **#1 Arreglo de planilla en 48 h vendido a la red, con factura de Contra** (score 7).
   - Es la única vía con probabilidad *media* de tener USD disponibles en 7 días.
   - Meta: 70+ mensajes personales entre el jueves 1 y el sábado 3.
2. **#7 Upwork, Excel/Sheets a precio fijo** (score 6).
   - Arrancar **hoy**, porque cada día de demora corre el cobro un día (5 días de seguridad después de la aprobación).
   - Usar solo contratos de precio fijo chicos con entrega en el día. Presupuesto: USD 15-30 en Connects.
3. **#2 Paquete de 3 SOPs** (score 6,5).
   - El mismo esfuerzo de prospección que la #1, con ticket más alto.
   - Probablemente cobre en el día 8-12, pero es el mejor puente a la consultora.
4. **#4 Pedidos chicos de Reddit pagados por PayPal** (score 5).
   - Para garantizar *algún* dólar cobrado el día 7, aunque sean USD 20-50.
   - Solo tareas legítimas y chicas.
5. **#24 Alignerr + #28 Meridial + #26 Mercor, aplicando el día 1** (score 3,5-4,5).
   - 2-3 horas en total. Es una lotería de USD 20-60/h que puede pagar en la semana 2-3.

**Expectativa honesta:** si ejecuta bien las 5, lo más probable al **2026-10-07** es tener **USD 0-150 disponibles** y **USD 100-400 "en tránsito"**, que se liberan entre el 2026-10-08 y el 2026-10-20. Cobrar más de USD 300 disponible en la primera semana es improbable sin una red de contactos que ya pague en USD.

**Fuera de este frente, pero hay que decirlo:** el peso más rápido es un cliente **local** que paga por Mercado Pago en el día (ver C1/D5 del estudio anterior). Si el objetivo es "plata esta semana" más que "dólares esta semana", rinde más.

---

## 4. Trampas y estafas comunes

1. **Ofertas "presupuesto USD 4.000, 10 vacantes, no scammers"** en Workana y Freelancer. Es un patrón clásico de captación para estafas (piden un "fee de capacitación", sacan datos o pasan la charla a Telegram) ([ejemplo en Workana](https://www.workana.com/job/freelancers-needed-for-typing-and-translation-job-budget-4000-10-slots-available-no-scammers-needed-please-1)).
2. **"Pasemos a Telegram o WhatsApp y te pago fuera de la plataforma."** Viola el ToS (Upwork banea la circunvención) y es el vector número 1 de estafas: cheques falsos, "comprá equipo y te reembolso", trabajo gratis.
3. **Test pagos que en realidad son trabajo gratis:** "traducí 2.000 palabras como prueba".
4. **Tareas académicas disfrazadas** ("redacción con normas APA", "parafraseo indetectable") → **excluidas por ética**. Además, son causa frecuente de reportes.
5. **Plataformas de "tareas de IA" con depósito previo o "activá tu cuenta con USDT":** estafa al 100%. Ninguna plataforma legítima cobra para trabajar.
6. **Ofertas de moderación o "ambassador" pagadas en tokens** de proyectos cripto nuevos: suelen ser especulativas o pump-and-dump (excluidas).
7. **VPN o cuentas a nombre de terceros** para entrar a DataAnnotation, Prolific o Handshake desde AR: baneo y pérdida del saldo, además de violar el ToS (excluido).
8. **Usar Claude para resolver tareas de entrenamiento de IA o transcripciones "humanas"** donde está prohibido: es la causa más citada de baneos en Outlier y similares. Claude se usa para lo que el cliente compra (Excel, SOPs, borradores declarados), no para fingir trabajo humano.
9. **Gurús que venden "cursos para ganar USD 1.000 en Fiverr la primera semana":** el clearing de 14 días lo hace matemáticamente imposible.
10. **Comisiones escondidas en AR:** 5,4% + USD 0,30 de PayPal, mínimo de USD 50 para retirar de Workana a Payoneer [según fuentes secundarias], USD 30 por wire de Upwork. Hay que calcular el neto antes de aceptar un precio.

---

## 5. Tiempos reales de cobro por plataforma (cuenta nueva, desde AR)

| Plataforma | Onboarding real | Retención / liberación | Frecuencia de pago | Método AR | Día más temprano con dinero **disponible** (empezando el 2026-10-01) | ¿≤ 7 días? |
|---|---|---|---|---|---|---|
| Cliente directo + **Contra** | Horas | 0 (rápido) o 4 días (estándar); +3-5 días hábiles si el cliente paga por ACH | Por factura | Payoneer/PayPal en 30 min | Día 3-6 | **Sí (media)** |
| Cliente directo + **solicitud de Payoneer** | Horas | 1-3 días según medio [NO VERIFICADO] | Por solicitud | Payoneer | Día 4-7 | **Sí (media-baja)** |
| Cliente directo + **PayPal** | Horas | Inmediato en saldo | — | PayPal → CBU en pesos, 24-72 h | Día 2-6 | Sí (montos chicos) |
| **Upwork precio fijo** | 1-3 días (aprobación del perfil, ID con videollamada) | 5 días después de la aprobación del hito; 14 días si el cliente no actúa | Al liberarse | Payoneer (horas) | **Día 7-9** | Límite (baja-media) |
| **Upwork por hora** | Igual | Facturación lunes + 5 días de revisión → miércoles | Semanal | Payoneer | **2026-10-14** | No |
| **Workana** (plan gratis) | 1-2 días | Al liberar el cliente; retiro **del 1 al 5 de cada mes** [parcialmente NO VERIFICADO] | Mensual (semanal en planes pagos) | Payoneer (mínimo USD 50), PayPal, banco AR | **2026-11-01 al 05** | No |
| **Fiverr** | 1 día (pero primera venta en 4-10 semanas) | 14 días de clearing (nuevos) + ~3 de autocompletado | Al liberarse | Payoneer (USD 1) | ≥ 2026-10-18, realista 5-10 semanas | No |
| **Freelancer.com** | 1 día | 15 días en el primer retiro | — | Express en pesos (AR) | ≥ 2026-10-16 | No |
| **Contra** (marketplace) | 1 día | 0-4 días | Por proyecto | Payoneer/PayPal | Depende de conseguir cliente (poco tráfico) | Improbable |
| **Alignerr** | "Resultado en el mismo día" | — | Semanal (Deel) | Deel → ¿? [NO VERIFICADO para AR] | Día 7-14 | Improbable |
| **Outlier** | 3-14 días + "empty queue" | — | Semanal (martes) | PayPal / Airtm | Martes 2026-10-06 si trabaja antes del lunes (improbable); realista 2026-10-13 o después | Improbable |
| **Mercor** | Entrevista con IA; días a semanas | — | Semanal (Stripe/Wise) | [NO VERIFICADO para AR] | 2-4 semanas | No |
| **Micro1** | Hasta 30 días de revisión | — | Quincenal (Deel) | Deel | 4-6 semanas | No |
| **TELUS Digital** | Semanas (exige 5 años de residencia en el país del rol) | — | Mensual [NO VERIFICADO] | — | 4-8 semanas | No |
| **OneForma / UHRS** | Días a semanas | Ciclo del 26 al 25 | Mensual | Payoneer (PayPal hasta USD 300/año) | Fines de 2026-10 o 2026-11 | No |
| **Clickworker (UHRS)** | Días | **39 días** | Semanal después de los 39 días | PayPal/Payoneer | ~2026-11-10 | No |
| **Trymata** | 1-2 días (test de calificación) | — | Viernes (tests de esa semana) | PayPal | **Viernes 2026-10-09** | Límite |
| **Userfeel** | 1-2 días | ~1 semana a la billetera | A pedido | PayPal | Día 8-10 | Límite |
| **Userlytics** | 1 día | — | Quincenal o hasta 30 días | PayPal | 2-4 semanas | No |
| **UserTesting** | 1-3 días | ~14 días después del test | — | PayPal | ≥ 2026-10-15 | No |
| **uTest** | Días (perfil y cursos) | Aprobación del bug | Los días 15 y último del mes | PayPal/Payoneer | 2026-10-15 (optimista) | No |
| **Respondent** | Días (perfil y screener; elegibilidad AR [NO VERIFICADO]) | 5-10 días hábiles | Por estudio | Visa virtual | 2-3 semanas | No |
| **GoTranscript** | 2-7 días (quiz + prueba) | — | Viernes | PayPal/Payoneer | 2026-10-09 (optimista) o 2026-10-16 | Improbable |
| **Gengo** | ~7 días de revisión del test | — | Días 10 y 25 | PayPal/Payoneer | 2026-10-25 | No |
| **DataAnnotation** | — | — | — | — | **No disponible en AR** | — |

---

## 6. Fuentes (consultadas el 2026-10-01)

- Upwork, pagos y plazos: [gigradar](https://gigradar.io/blog/how-to-get-paid-on-upwork) · [aiproposer – métodos de pago](https://aiproposer.com/guides/upwork-strategy/upwork-payment-methods) · [Upwork – protección de pagos](https://www.upwork.com/resources/understanding-freelancer-payment-protection)
- Upwork, Connects: [unilink 2026](https://www.unilink.us/blog/upwork-connects-explained-2026) · [snipework 2026](https://snipework.com/blog/upwork-connects-strategy-2026)
- Upwork, aprobación de perfil e ID: [websitebuilderinsider](https://www.websitebuilderinsider.com/why-is-upwork-not-approving-my-profile/) · [comunidad Upwork – ID](https://community.upwork.com/t5/Support-Forum/Identity-ID-verification/m-p/1291369)
- Upwork, demanda IA 2026: [Upwork In-Demand Skills 2026](https://investors.upwork.com/news-releases/news-release-details/upworks-demand-skills-2026-demand-top-ai-skills-more-doubles-ai) · [UpHunt – State of AI on Upwork 2026](https://uphunt.io/blog/state-of-ai-on-upwork-2026) · [PYMNTS 2026](https://pymnts.com/earnings/2026/upwork-navigates-cross-currents-as-ai-reshapes-freelance-demand)
- Fiverr: [vaultleap – comisiones 2026](https://vaultleap.com/blog/fiverr-fees-explained-2026) · [conductatlas – ToS, clearing de 14 días](https://conductatlas.com/platform/fiverr/fiverr-terms-of-service/payment-clearance-period-14-day-hold/) · [walletgrower 2026](https://walletgrower.com/blog/fiverr-review-2026) · [Fiverr – retiros (ES)](https://help.fiverr.com/hc/es/articles/360010530058-Retirar-tus-ganancias-y-administrar-tus-m%C3%A9todos-de-retiro)
- Workana: [listados públicos](https://www.workana.com/job/spanish-to-english-translation-and-editing-projects-1) · [ARQ – Workana](https://www.arqfinance.com/es-AR/blog/freelancer-tips/flexjobs-vs-workana) · [Xolo 2026](https://blog.xolo.io/es/7-mejores-plataformas-para-trabajos-freelance-espanol-2026) · global66 (fechas de retiro; snippet, página con 403)
- Freelancer.com: [Express Withdrawals](https://www.freelancer.com.au/support/Payments/express-withdrawals)
- Contra: [plazos de payout](https://help.contra.com/en/articles/10008642-payout-timelines-for-freelancers-on-contra)
- Entrenamiento de IA: [aitrainer.work – comparativa (2026-10-01)](https://aitrainer.work/guides/best-ai-training-platforms-reviewed) · [aitrainer.work – empleos AR](https://aitrainer.work/jobs/argentina) · [raenest – Outlier 2026](https://www.raenest.com/es-ar/blog/outlier-ai-vs-handshake-ai) · [breakingeven – Outlier](https://breakingeven.online/platforms/outlier) · [aitrainer.work – fallout de Scale](https://aitrainer.work/news/scale-ai-fallout-surge-ai-hyper-growth) · [DataAnnotation, países](https://aitrainer.work/guides/is-dataannotation-legit-review) · [TELUS QA rater](https://www.workingnomads.com/jobs/quality-assurance-rater-spanish-spain-telus-digital) · [OneForma – Payoneer](https://www.oneforma.com/help-center/project-help/how-to-set-up-payoneer-payment-method-on-oneforma/)
- Testeo: [UserTesting – compensación](https://help.usertesting.com/hc/en-us/articles/11880240002845) · [Userlytics – países](https://remove.userlytics.com/helpcenter/testers/what-countries-are-supported-for-testers/) · [Trymata](https://sidehusl.com/trymata/) · [Userfeel](https://sidehusl.com/userfeel/) · [uTest review 2026-08-24](https://selfmadesuccess.com/utest-review/) · [Respondent](https://sidehusl.com/respondent/)
- Transcripción y traducción: [GoTranscript – español](https://gotranscript.com/spanish-transcription-job) · [Gengo](https://realwaystoearnmoneyonline.com/become-translator-for-mygengo/)
- Microtareas: [Clickworker – pagos](https://support-workplace.clickworker.com/support/solutions/articles/80000672346-how-do-i-get-paid-for-my-work-)
- Cobro en AR: [PayPal AR – iProfesional 2026-06-19](https://www.iprofesional.com/finanzas/403093-pay-pal-argentina-como-cobrar-en-dolares) · [calculadora PayPal AR](https://www.jonatanalmeira.com/calculadora-paypal-argentina/) · [Mercado Pago, recibir del exterior](https://www.jonatanalmeira.com/?p=65154) · [Payoneer–Santander AR](https://www.payoneer.com/es/resources/business/payoneer-y-santander-argentina/)

## 7. Pendientes de verificar

- Si Prolific acepta participantes de Argentina, y si Respondent lo hace.
- Fechas exactas de retiro de Workana por plan y precio de los planes con retiro semanal (página oficial con 403).
- Comisión vigente de Upwork al freelancer en 2026 (¿variable 0-15%?).
- Cómo cobra en AR Alignerr (Deel) y Mercor (¿Stripe/Wise?), y si Deel deja retirar a Payoneer o a USDT.
- Política de GoTranscript y Gengo sobre el uso de transcripción y traducción automática.
- Política de 99designs sobre diseños hechos con IA.
- Nivel de inglés del usuario: define si entran las ideas marcadas (EN).
