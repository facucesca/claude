# Idea: Consultora de mejora de procesos + automatización con IA (2026-09-07)

**Origen:** se le ocurrió al usuario (Facu). Montar una empresa que audita empresas/PyMEs de cualquier rubro, detecta ineficiencias (cuellos de botella, tareas manuales, fallas) y las resuelve con automatización + metodologías de mejora continua (Lean, 5S, Six Sigma). Entrada de bajo costo tipo "auditoría de USD ~500" para mostrar cuánto se puede mejorar; clientela por mail frío en Argentina (Tucumán, Córdoba…) y España, después EEUU. Idea de arrancar como pasante para aprender mientras funda.

> ⚠️ **Choca con la tesis del repo.** Este proyecto es un *laboratorio de ingresos pasivos/semi-pasivos* (regla de oro: nada de vigilancia diaria, la compu trabaja sola). Una consultora es un **negocio de servicios**: intercambia horas por plata, con venta, reuniones y entrega a medida. No es pasivo y no lo va a ser al principio. Eso no la descarta — pero hay que evaluarla como lo que es, no como un ingreso pasivo. Ver "Reframe" abajo.

## Actualización 2026-09-07 (post-charla) — pivote de posicionamiento

> La advertencia de arriba quedó **superada**: el 2026-09-07 el usuario cambió el alcance del proyecto para aceptar ideas *activas*. Esta idea ya no "choca"; se evalúa como negocio de servicios. Además se corrige el enfoque de nicho (supera al punto 1 de "Qué haría distinto"):

- **El nicho NO es por industria, es por CAPACIDAD.** El usuario tiene razón: el ingeniero industrial es horizontal, no vive en un rubro. Pero "cualquier proceso de cualquier empresa" sigue siendo el error clásico (invisible, no vendible). La resolución: nichar por **problema**, no por industria. El problema que el usuario ya describió —y que es su verdadero producto— es el **ORDEN OPERATIVO**: control de stock, dónde va cada cosa (slotting/ABC), picking rápido, mermas/robos, layout de depósito. Aplica a *cualquiera con muchos SKUs* (retail, distribución, e-commerce, librería, repuestos, farmacia…). Eso **sí es un nicho**: filoso por capacidad, ancho por industria.
- **Posicionamiento propuesto:** *"Pongo orden en tu operación/depósito. Con números antes y después."* Diferencial claro vs scriptHouse (que vende software): el usuario vende **método de ingeniería industrial**; el software/hardware es herramienta, no el producto.
- **Activo de credibilidad #1 (ya lo tiene):** relevamiento del área de logística en **Sporting** (retail multimarca, AR) como pasantía. Es el caso de portfolio para escribir YA (anonimizado si hace falta): "relevé la logística de una multimarca, encontré X, propuse Y". Vuelve tibio el contacto frío.
- **Producto ≠ hardware (todavía).** El usuario baraja pick-to-light con Arduino / impresora 3D. Veredicto honesto: es un **upsell futuro**, no el producto de arranque. Empezar por hardware = meses construyendo antes de vender + convertirse en negocio de electrónica (inventario de componentes, instalación, soporte). El wedge es **método + herramientas digitales baratas** (análisis ABC, plan de slotting, punto de reorden, sistema de stock con QR) — costo ~0 y juega a la ventaja dev+IA. El pick-to-light se construye cuando un cliente con depósito grande lo pida y lo pague (y de paso sirve de demo con impacto visual).
- **Toolkit de referencia** (libros/métodos/métricas del nicho): `research/2026-09-07-orden-operativo-toolkit.md`.

---

## ¿Ya existe? Sí, y bastante saturado (competencia real)

**En Tucumán mismo:**
- **scriptHouse** — scripthouse.com.ar (verificado 2026-09-07). Dos ingenieros en computación de San Miguel de Tucumán. Ofrecen *automatización de procesos, software a medida, web y apps*. Gancho: **demo funcional en 72 h sin costo**, presupuesto cerrado por etapas, el código queda a nombre del cliente, trabajan para Caja Popular de Ahorros. **Es casi exactamente tu idea, ya en tu ciudad, con credibilidad de banco.** Competidor directo #1.
- **Berater** — beraterconsultora.com.ar. Consultora de RR.HH. en Tucumán (adyacente, no idéntica).

**Nacionales / regionales que pisan el mismo terreno:**
- **BPS Consultora** (bpsolutions.com.ar) — mejora de procesos con **Lean Six Sigma** adaptado a cada empresa.
- **Logsis** (logsis.com.ar) — optimización de procesos con simulación e IA.
- **Smartservices** (smartservices.com.ar) — automatización/RPA.
- **Crowe Argentina**, **EY**, **Schneider Electric** — el segmento medio/alto ya está tomado por firmas con marca.
- **revolucionatupyme.com** — el mismo pitch "automatizá tu pyme" empaquetado.

**El modelo "AI Automation Agency" (AAA)** explotó 2023-2025 empujado por gurús de YouTube que **venden el curso** de cómo armar la agencia (conflicto de interés clásico — la pala se la venden a vos, no al cliente). Está saturado en la base y con alta mortalidad (abajo).

**Conclusión:** la idea es válida pero **no es un océano azul**. Tu diferencial no puede ser "hago eficiencia para cualquier rubro" (eso ya lo ofrecen todos, incluido tu vecino de Tucumán). Tiene que ser un **nicho + prueba con números**.

---

## Los números honestos (mediana, no casos virales)

- **Mail frío B2B:** tasa de respuesta mediana **~3-5%**, y de esas respuestas solo una fracción agenda. Top decile llega a 10-25% *pero solo con targeting quirúrgico y personalización real*. (Belkins 2025-2026, Instantly). Traducción: para conseguir 3-4 reuniones vas a mandar **cientos** de mails bien hechos. La lista y el ángulo importan más que el volumen.
- **Proyectos de automatización/IA fracasan seguido:** Gartner proyecta que **>40% de los proyectos de "agentic AI" se cancelan para 2027**; MIT (2025) reportó que **~95% de los pilotos de IA generativa no mueven el P&L**; análisis de industria hablan de que la mayoría de los agentes no llegan a producción. El modo de falla típico es el salto **piloto→producción** (funciona en la demo, se rompe cuando cambia el proceso o la API). → Vender "outcome medido", no "una demo linda".
- **Ingreso de agencias de automatización (anécdotas, con survivorship bias):** un practicante dice **USD 8.200/mes a 25 h/semana** con n8n; un chico de 21 dice **USD 1.200/mes** automatizando gimnasios/dentistas/inmobiliarias. Son casos individuales autorreportados, no medianas. Lo estructural y creíble: **retainers de USD 500-3.000/cliente/mes** cuando vendés mantenimiento + resultados en lugar de un proyecto suelto. (Medium/LearnForge, consultado 2026-09-07).
- **Realidad del ticket "auditoría USD 500":** a un desconocido joven, en frío, una PyME no le suelta USD 500 fácil. El ticket bajo funciona **después** de tener 2-3 casos con testimonios. Al principio, tu instinto de "cobrar muy poco / equivocarme" es correcto, pero ordenalo (ver plan).

---

## Reframe: cómo esta idea SÍ encaja con el repo

No la evalúo solo como "negocio de servicios más". La versión fuerte es tratarla como el **motor de cash + distribución** que financia y alimenta el activo pasivo ("stack de datos") que ya está en marcha:

```
Consultoría (activo: TU TIEMPO)                Activo pasivo (repo actual)
─────────────────────────────────             ──────────────────────────
Automatizás un proceso para Cliente A   ──►    cada automatización = plantilla reutilizable
Automatizás el MISMO proceso para B,C,D ──►    después de N clientes de un nicho…
                                        ──►    …lo empaquetás en producto (SaaS / pack n8n)
Cobrás retainer mensual (cash ya)              Producto se vende solo (pasivo, idea #6 del estudio)
```

- La consultoría te da **plata rápida, casos reales y feedback de mercado** que la ruta pasiva tarda meses en darte.
- Cada trabajo a medida es un **ladrillo de un producto**. Después de automatizar "presupuestos por WhatsApp" para 5 ferreterías, tenés un producto de nicho, no 5 favores sueltos.
- Encaja con el stack: sos dev, tenés Claude Code, n8n (skills), Cloudflare, Gmail/GitHub por MCP. **Podés construir lo que vendés** — ese es tu diferencial real contra el consultor de Lean que solo hace PowerPoints.

**El costo a vigilar:** te come las 10-15 h/semana que hoy están asignadas a construir el activo pasivo. No podés hacer las dos a fondo. Es una decisión de foco, no de agenda.

---

## Scoring (7 criterios del CLAUDE.md, 1-10)

> El framework está calibrado para ingreso *pasivo*; por eso la automatización puntúa bajo por diseño. Doy también la lente "negocio de servicios".

| Criterio | Score | Nota |
|---|---|---|
| 1. Rentabilidad realista (mediana 6-12m) | **6** | USD 300-1.500/mes plausible con 3-6 clientes si vendés bien; techo alto con retainers. Todo gateado por tu capacidad de venta. |
| 2. Grado de automatización (pasividad) | **2** | Es entrega de servicio + venta. Productizable hasta ~4-5 con el tiempo; nunca pasivo al principio. |
| 3. Capital requerido | **9** | ~Cero: laptop, subs de IA, herramienta de mail. |
| 4. Tiempo al primer dólar | **7** | Semanas a un par de meses si empujás — más rápido que casi todo lo pasivo, pero gateado por cerrar 1 cliente. |
| 5. Riesgo | **6** | Bajo riesgo catastrófico (dueño de la relación, sin baneos de plataforma). Alto riesgo "nunca despega" (venta) y de sumidero de tiempo. Ojo IP/no-compete si sos pasante. |
| 6. Durabilidad 2026+ | **6** | La demanda (PyMEs necesitan eficiencia) es durable y crece con IA. Pero la base "AAA" se comoditiza rápido y la IA abarata que el cliente lo haga solo. Moat = nicho + relación + ROI medido. |
| 7. Fit con el stack | **8** | Excelente: dev + Claude Code + APIs + MCP. Podés *construir* lo que vendés. Tu ventaja genuina. |

**Score compuesto como "idea pasiva": ~5,5/10** (la pasividad la hunde).
**Como motor de cash + feeder del activo pasivo: ~8/10** (complemento estratégico fuerte).

---

## Qué haría distinto (mejoras al proceso)

1. **Matar el "cualquier rubro".** El error #1 del principiante. Horizontal = invisible e increíble. Elegí **UN nicho y UN proceso doloroso** (ej: automatizar presupuestos/seguimiento en inmobiliarias de Tucumán; o facturación ARCA + cobros en consultorios; o remitos/stock en distribuidoras). Convertite en "el que automatiza X para Y". Después expandís.
2. **Vender ROI medido, no "eficiencia".** El core de ingeniería industrial: medir el **antes** (tiempo/errores/costo del proceso actual) y el **después**. La mayoría de las PyMEs no mide nada — instrumentar la línea base ES la mitad del trabajo y tu mayor palanca de credibilidad. "Les ahorré 11 h/semana y USD X/mes" vende; "mejoro procesos" no.
3. **Reordenar el ticket bajo.** Primeros 1-3 clientes: gratis o casi, a cambio de **testimonio + permiso para publicar el caso con números**. Recién con 2-3 casos, lanzás la "auditoría diagnóstica" paga (USD 300-500) como gancho, y de ahí al retainer de implementación + mantenimiento (donde está la plata real).
4. **Usar la pasantía como laboratorio de casos, no como distracción.** Si es éticamente limpio (sin conflicto con el empleador ni con su competencia), automatizá algo *adentro* de esa empresa con permiso, medí el antes/después → ese es tu primer caso con credibilidad. La pasantía vale por aprendizaje + red + prueba social, no como fuente de clientes.
5. **Productizar desde el día 1.** Cada automatización, guardala como plantilla parametrizable. El objetivo silencioso: que el 4º cliente de un nicho se resuelva en horas, no días. Ahí nace el producto pasivo.
6. **Estudio de metodologías con criterio 70/30.** Para PyMEs, el 70% del valor es "encontrar el desperdicio obvio y automatizarlo"; el 30% es metodología formal como vocabulario/credibilidad. Ruta mínima útil: los **8 desperdicios (muda)**, **Value Stream Mapping**, **5S**, **trabajo estándar**, **Teoría de Restricciones** (tu "cuello de botella"), y **DMAIC** de Six Sigma por encima. No te trabes sacando un Black Belt antes de tener un cliente.

## Qué NO haría

- **No** cold-emailear a España desde el arranque. Empezá donde tenés contexto, idioma pleno y podés ir en persona/videollamada con confianza: Tucumán y NOA. España/EEUU cuando tengas casos y proceso repetible.
- **No** competir por precio contra scriptHouse ni contra AAAs. Competí por **nicho + ROI demostrado**.
- **No** prometer "demo en 72 h" como diferencial (scriptHouse ya lo hace). Tu diferencial es el **número de negocio**, no la velocidad de demo.
- **No** dejar caer el activo pasivo sin decidirlo a conciencia. Es una bifurcación de foco.

---

## Preguntas abiertas para decidir

1. ¿Esto **reemplaza** o **convive** con el stack de datos? (No entran las dos a fondo en 10-15 h/semana.)
2. ¿Cuál es el nicho #1 donde tenés algún contacto/contexto para conseguir el primer caso sin frío?
3. La pasantía: ¿hay cláusula de confidencialidad/no-compete? ¿Podés usar lo que aprendas/construís?
4. ¿Objetivo real a 6 meses: cash (entonces servicios gana) o activo vendible (entonces pasivo gana)?

## Fuentes (consultadas 2026-09-07)

- Competencia local/nacional: [scriptHouse](https://scripthouse.com.ar/) (verificado), [BPS](https://www.bpsolutions.com.ar/mejora-de-procesos/), [Logsis](https://logsis.com.ar/), [Smartservices](https://www.smartservices.com.ar/consultoria-automatizacion-procesos/), [Crowe AR](https://www.crowe.com/ar/services/advisory/procesos-y-sistemas-de-gestion-de-calidad), [Berater](https://www.beraterconsultora.com.ar/), [revolucionatupyme](https://revolucionatupyme.com/consultoria-procesos-y-automatizacion/).
- Mail frío B2B: [Belkins 2026](https://belkins.io/blog/cold-email-response-rates), [Instantly](https://instantly.ai/blog/cold-email-reply-rate-benchmarks/).
- Fracaso de proyectos IA/agénticos: [Gartner vía Automation Labs](https://medium.com/automation-labs/40-of-all-ai-agent-projects-will-fail-by-2027-and-why-even-n8n-wont-save-you-d5734b8ffb0e), [análisis 88% no llega a producción](https://www.digitalapplied.com/blog/88-percent-ai-agents-never-reach-production-failure-framework).
- Ingreso agencias n8n (anecdótico): [Medium/Ravindu](https://medium.com/write-a-catalyst/building-n8n-workflows-for-clients-8k-month-without-a-website-01f27d49f20b), [LearnForge](https://learnforge.dev/blog/n8n-automation-agency/).

*Nada de esto es consejo financiero. Números medianos, no casos virales. Re-verificar competidores y tarifas al momento de ejecutar.*
