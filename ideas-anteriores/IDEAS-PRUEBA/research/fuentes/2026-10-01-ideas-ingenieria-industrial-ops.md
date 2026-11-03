# Ideas de ingresos — Frente: Ingeniería industrial, operaciones y consultoría para PyMEs (potenciada con IA)

- **Fecha del informe:** 2026-10-01
- **Autor:** agente de investigación (Claude) para el laboratorio IDEAS-PRUEBA
- **Perfil asumido del usuario (según el encargo de 2026-10-01):** argentino; formación/pasantía en ingeniería industrial (relevó logística de un depósito: stock, picking, layout); trabaja con Claude / Claude Code pero **no sabe programar**; presupuesto < USD 500-1.000; acepta pasivos, semi-pasivos y activos; cobra desde Argentina (Payoneer, Mercado Pago, merchant of record tipo Lemon Squeezy/Paddle/Hotmart).
- **Relación con ideas existentes:** la idea propia **"Orden Operativo"** (consultoría de stock/slotting/picking/mermas/layout de depósito; ficha en `ideas/2026-09-07-consultora-mejora-procesos.md`) es el núcleo de este frente. Cada idea abajo marca su **superposición** con ella: `TOTAL` (es Orden Operativo o un módulo suyo), `PARCIAL` (expansión/variante/sinergia) o `NINGUNA`.

> Nota de coherencia: `MEMORY.md` describe al usuario como "técnico, puede construir software asistido por IA". El encargo de hoy dice que **no sabe programar**. Este informe toma la versión de hoy: todas las ejecuciones propuestas son **no-code** (Claude chat/Projects, Claude en Excel/Sheets, Google Forms/Sheets, AppSheet, Looker Studio, Canva, herramientas SaaS con plan gratis). Conviene actualizar `MEMORY.md`.

---

## Metodología

1. **30 búsquedas web** (WebSearch, modo estándar) + **8 lecturas directas** (WebFetch) el 2026-10-01. El presupuesto de búsquedas de la sesión se agotó en la búsqueda 31 (límite compartido con otros agentes), por lo que algunos datos quedaron **sin verificar** y están marcados como tales.
2. Prioridad a fuentes 2025-2026. Para Argentina: UIA (Monitor de Desempeño Industrial), Di Tella/Fundar (adopción de IA en PyMEs), INTI (Kaizen TANGO), GCBA (Expertos PyME), FAQYA (honorarios H&S), La Capital (gastronomía Rosario), iProfesional (Mercado Libre).
3. Criterio para que algo entre como "idea": **oferta concreta + cliente concreto + alguien haciéndolo hoy** (con link). No categorías vagas.
4. **Score 1-10 "realista para ESTE usuario"**: pondera los 7 criterios del `CLAUDE.md` pero con tres penalizaciones explícitas del perfil: (a) junior sin casos → credibilidad baja, (b) no programa → nada que dependa de construir software, (c) presupuesto bajo → nada con hardware/inventario. Para ideas activas no se castiga la falta de pasividad (nota 2026-09-07 del `CLAUDE.md`).
5. Escepticismo: medianas sobre casos virales; se señalan conflictos de interés (vendedores de software que publican "guías de costos", consultores que publican sus propias tarifas, gurús de agencias).

### Contexto macro que condiciona TODO el frente (leer primero)

- **La industria argentina está en contracción.** El Monitor de Desempeño Industrial de la UIA dio **36,5 puntos en enero 2026** (umbral de expansión = 50; relevamiento 2026-02-02 a 2026-02-16, 644 empresas con ADIMRA y FISFE) y las PyMEs fueron las más afectadas ([Tiempo de San Juan, 2026](https://www.tiempodesanjuan.com/politica/la-industria-inicio-2026-caida-generalizada-y-el-indice-desempeno-zona-contraccion-n424599); [Canal 26, 2026-03-05](https://www.canal26.com/economia/2026/03/05/la-uia-informo-que-cayeron-la-produccion-y-las-ventas-en-mas-del-50-de-las-fabricas/)). Uso de capacidad instalada **58,4% en mayo 2026** y **59,1% en junio 2026** ("cuatro de cada diez máquinas paradas"); se reportan **>3.500 empresas industriales perdidas desde fines de 2023** (mismas fuentes; cifra de la UIA, organismo con interés gremial).
  - **Implicancia:** vender "más productividad/más capacidad" a una fábrica con 40% de máquinas paradas es difícil. Lo que se vende hoy en AR es **bajar costos, reducir capital inmovilizado en stock, mermas y horas extra**. Para "productividad pura" el mercado está afuera (remoto, USD).
- **Adopción de IA en PyMEs AR:** **42%** usa al menos una tecnología de IA, más de la mitad en fase experimental; barrera #1 = **falta de talento**, luego infraestructura digital insuficiente y falta de gobernanza (CEPE-UTDT + Fundar, con Observatorio PyME y BID; publicado 2026-05-01, [Mercado](https://mercado.com.ar/ruta-digital/una-encuesta-nacional-midio-la-adopcion-de-inteligencia-artificial-en-pymes-argentinas)). → Hay hueco para "el que baja la IA a tierra en operaciones", pero la PyME "opera a la defensiva".
- **Programas de subsidio a consultoría: mayormente dormidos.** PAC (ANR 70%, modalidad Kaizen) aparece en fuentes de años anteriores, sin convocatoria 2025-2026 verificada; **Expertos PyME (GCBA)** tuvo convocatoria 2025-03-01 a 2025-03-31 y hoy figura "no hay convocatorias vigentes" (consultado 2026-10-01, [GCBA](https://buenosaires.gob.ar/desarrolloeconomico/ba-pyme/expertos-pyme)). No armar un modelo de negocio que dependa de subsidios.

---

## Lista de ideas (34)

Formato de cada ficha: **Qué es** · **Quién lo hace / señal de auge** · **Cobro y precio** · **Ejecución con Claude (no-code)** · **Tipo y h/sem en régimen; productización** · **Capital y tiempo al 1er dólar** · **Viabilidad AR** · **Riesgos/escepticismo** · **Superposición con Orden Operativo** · **Score**.

---

### BLOQUE A — Diagnósticos productizados (la puerta de entrada)

#### 1. "Diagnóstico Express de Operación" a precio fijo (1 día en sitio + informe con cuellos de botella costeados)
- **Qué es:** visita de un día a una PyME (depósito, taller, cocina, local), seguir pedidos reales de punta a punta, mapear el estado actual (VSM simplificado), y entregar a los 7-10 días un informe con los 3-5 cuellos de botella **valorizados en horas y pesos**, más un plan priorizado. Precio fijo acordado antes.
- **Quién lo hace / señal:** Osher Digital (Australia) vende exactamente esto: "one-day onsite study" con fee fijo, informe 7-10 días después con mapeo del estado actual, cuellos de botella cuantificados y plan de implementación cotizado aparte ([Osher](https://osher.com.au/help/working-with-osher-digital/what-is-a-process-audit/), consultado 2026-10-01). En Upwork hay "business process audit" productizados desde ~USD 800 ([Upwork](https://www.upwork.com/services/product/consulting-hr-a-business-process-audit-to-optimize-processes-for-efficient-growth-1741212274255642624)). El modelo "productized consulting" (alcance y precio fijos como puerta a tiers superiores) está documentado como tendencia ([ManyRequests](https://manyrequests.com/blog/productized-consulting-how-it-works-why-its-worth-it)).
- **Cobro y precio:** fijo. Afuera USD 800-3.000. En AR (estimación propia, no verificada): USD 150-400 equivalentes al arranque; los primeros 2-3 gratis/bonificados a cambio de caso publicable con números.
- **Ejecución con Claude:** checklist de relevamiento armada con Claude; fotos + audios del día → Claude transcribe y estructura; planilla de tiempos en Sheets; Claude redacta informe y arma el VSM (diagrama en Canva/Mermaid exportado). Plantilla de informe reusable.
- **Tipo:** activo; ~6-10 h por diagnóstico (1 día + 1 día de informe). Productizable: plantilla de informe + checklist → cada diagnóstico más rápido; vender el "kit de autodiagnóstico" como producto digital más adelante.
- **Capital / 1er dólar:** ~USD 0-50 (transporte, impresión). 1er dólar: 1-3 meses (depende de cerrar el primer pago tras 1-2 casos gratis).
- **Viabilidad AR:** venta presencial en tu ciudad; cobro por transferencia/Mercado Pago, factura como monotributista. Viable.
- **Riesgos:** junior + "diagnóstico" = la PyME espera que sea gratis (todos los vendedores de software regalan diagnósticos). El valor del informe depende de que tenga **números**; sin línea base no hay venta de implementación. Ciclo de venta corto si es en persona.
- **Superposición:** PARCIAL — es el **producto de entrada natural** de Orden Operativo.
- **Score: 7/10.**

#### 2. "Stock Sano": auditoría de inventario + ABC + punto de reorden para comercios con muchos SKUs
- **Qué es:** el cliente exporta ventas y stock (de su sistema o Excel); se entrega: clasificación ABC/XYZ, stock inmovilizado (plata parada), quiebres, punto de reorden y stock de seguridad por SKU, lista de "qué liquidar" y "qué no puede faltar". Opcional: conteo cíclico.
- **Quién lo hace / señal:** consultores de inventario en Upwork venden forecasts/planes productizados (USD 50-200 por paquete) ([Upwork](https://www.upwork.com/services/product/admin-customer-support-inventory-forecasting-for-amazon-fba-1747312553979592704)); software como Forecastly cobra desde USD 49/mes ([Novadata](https://novadata.io/resources/best-amazon-seller-tools/forecastly)). En AR, proveedores de software (Base) publican guías de "stock óptimo en contexto inflacionario" ([Base](https://base.com/es-AR/blog/stock-en-argentina/)) — señal de dolor, con conflicto de interés (venden el software).
- **Cobro y precio:** proyecto fijo (estimado AR: USD 200-600) + mantenimiento mensual opcional (USD 50-150/mes) para recalcular reorden.
- **Ejecución con Claude:** Claude en Excel/Sheets hace el ABC, rotaciones y fórmulas de reorden; Claude explica cada resultado en lenguaje de dueño; informe en Docs.
- **Tipo:** activo → semi-pasivo (el recálculo mensual es casi mecánico). Régimen: 1-2 h/cliente/mes.
- **Capital / 1er dólar:** ~USD 0. 1-2 meses.
- **Viabilidad AR:** alta — con inflación el stock inmovilizado duele; se puede vender **remoto** a todo el país (y LATAM) porque solo requiere exportar datos.
- **Riesgos:** datos sucios (sistemas sin stock real); la "auditoría" pierde valor si el stock del sistema no coincide con el físico → hace falta conteo (presencial). La IA puede equivocarse en fórmulas: revisar.
- **Superposición:** TOTAL — es el núcleo de Orden Operativo.
- **Score: 7,5/10.**

#### 3. Re-slotting y layout de depósito chico (proyecto de alcance fijo)
- **Qué es:** reubicar SKUs por rotación (A adelante y a la altura de la mano), zonificar rápidos/lentos, rediseñar recorridos de picking, señalización. Medir antes/después (metros recorridos, minutos por pedido).
- **Quién lo hace / señal:** proveedores de slotting (Optioryx) publican en 2026 que el slotting bien hecho reduce **15-30% la distancia de picking** y mejora 20-40% el uso de capacidad ([Optioryx 2026](https://www.optioryx.com/blog/warehouse-slotting)) — fuente con conflicto de interés (venden software). Un caso académico de ABC en dos etapas reportó **27,62%** menos distancia ([Omni Online](https://omnionlinestrategies.com/blog/abc-slotting-analysis)).
- **Cobro y precio:** fijo por proyecto (estimado AR: USD 300-1.000 según tamaño), idealmente con un componente variable atado al ahorro medido.
- **Ejecución con Claude:** plano en Sheets/Canva, ABC con Claude, plan de reubicación por etapas, cartelería con QR (Canva), medición con cronómetro y planilla.
- **Tipo:** activo, presencial. 10-30 h por proyecto.
- **Capital / 1er dólar:** USD 0-100 (etiquetas). 1-3 meses.
- **Viabilidad AR:** buena en distribuidoras, repuestos, ferreterías, e-commerce con depósito propio.
- **Riesgos:** el cliente no deja "mover todo" sin confianza; implementación física la hace su personal (si no la sostienen, se desordena en 3 meses → vender seguimiento 5S). El caso de Sporting es la palanca de credibilidad.
- **Superposición:** TOTAL.
- **Score: 7/10.**

#### 4. Operaciones para vendedores de Mercado Libre (Flex/Full/depósito propio, picking y preparación)
- **Qué es:** paquete para sellers medianos de ML: decidir qué SKUs mandar a Full vs. despachar con Flex/colecta, ordenar el depósito propio para picking rápido, estandarizar el armado de paquetes (SOP), reducir errores de envío y reclamos, planificar reposición a Full.
- **Quién lo hace / señal:** ML concentra **>2,7 millones de emprendedores y PyMEs en Argentina; para el 49% es su ingreso principal**; en 2026 ML planea invertir USD 3.400 M en AR y construye su mayor centro de distribución local (USD 115 M) ([iProfesional, 2026-06-27](https://www.iprofesional.com/negocios/450528-mercado-libre-cambia-logistica-argentina-inversion-record-miles-empleos)). Herramientas de terceros (Nubimetrics academia) enseñan Full ([Nubimetrics](https://academia.nubimetrics.com/mercado-envios-full)). No encontré (por límite de búsquedas) un consultor de ops específicamente para sellers ML — **hueco probable, no verificado**.
- **Cobro y precio:** diagnóstico fijo (estimado USD 100-300) + retainer de reposición/planificación (USD 100-300/mes). Alternativa: curso/taller grupal.
- **Ejecución con Claude:** Claude analiza el reporte de ventas de ML (export Excel) → ABC, candidatos a Full, punto de reorden a Full; SOP de armado con fotos; checklist diaria en Google Forms.
- **Tipo:** activo → semi-pasivo (reposición mensual es mecanizable). 1-3 h/cliente/mes en régimen.
- **Capital / 1er dólar:** USD 0. 1-2 meses (comunidades de sellers, grupos de Facebook/WhatsApp, LinkedIn).
- **Viabilidad AR:** muy alta; venta 100% remota a todo el país; mismo producto exportable a MX/BR/CL (ML regional).
- **Riesgos:** ML cambia reglas de Full/Flex seguido (dependencia de plataforma); sellers chicos no pagan; competencia de agencias de "gestión de cuentas ML" que podrían sumar ops.
- **Superposición:** PARCIAL — es Orden Operativo **verticalizado en e-commerce**, la expansión más natural.
- **Score: 7,5/10.**

#### 5. Consultor de fulfillment / selección de 3PL para marcas Shopify (remoto, en USD)
- **Qué es:** para marcas DTC de EE.UU./España: auditar costos de fulfillment, comparar 3PLs, preparar RFP, checklist de integración y piloto.
- **Quién lo hace / señal:** eHub describe el rol "3PL consultant" (evaluar operación, recomendar 3PL, negociar, reducir costos); algunos cobran por hora/proyecto y otros cobran comisión de las redes de fulfillment ([eHub](https://ehub.com/blog/3pl-consultants)) — ojo, conflicto de interés en los "gratis". Guías de selección de 3PL para Shopify ([SKUSavvy](https://skusavvy.com/blog/how-to-find-the-right-3pl-for-your-shopify-store)).
- **Cobro y precio:** proyecto fijo (rango típico estimado USD 1.000-5.000; no verificado) o comisión de referidos de 3PL.
- **Ejecución con Claude:** Claude arma la matriz de comparación, el RFP y analiza facturas del 3PL actual; llamadas por Zoom.
- **Tipo:** activo remoto. 5-15 h por proyecto.
- **Capital / 1er dólar:** USD 0-100 (LinkedIn Premium opcional). 3-6 meses (venta en frío al exterior, sin casos = lento).
- **Viabilidad AR:** cobro vía Payoneer/Wise/Upwork; contrato en USD. Viable pero la venta es la barrera.
- **Riesgos:** cero credibilidad en el mercado de EE.UU. sin casos; nunca pisó un 3PL; inglés de negocios necesario; consultores con 10+ años compiten.
- **Superposición:** PARCIAL (misma capacidad, mercado exterior).
- **Score: 4/10** (bueno en papel, pésimo fit de credibilidad hoy; reconsiderar con 5+ casos locales).

---

### BLOQUE B — Stock, compras, forecast y reparto

#### 6. Forecast + plan de reposición para sellers de Amazon FBA (gig remoto)
- **Qué es:** a partir del reporte de ventas, entregar forecast por SKU, fecha y cantidad de envío a FBA para no pagar sobrestock ni quebrar.
- **Quién lo hace / señal:** gig productizado en Upwork: USD 50 / 100 / 200 por paquete, por un consultor con 5+ años en supply chain ([Upwork](https://www.upwork.com/services/product/admin-customer-support-inventory-forecasting-for-amazon-fba-1747312553979592704)); en 2025 Amazon reestructuró fees y castiga el sobrestock con storage charges ([SmartScout](https://www.smartscout.com/blog/how-to-navigate-amazons-new-fee-structure-in-2025); [Seller Labs](https://www.sellerlabs.com/blog/10-amazon-fba-mistakes-to-avoid-2025)).
- **Cobro y precio:** USD 50-200 por entrega; retainer mensual USD 100-300 si se fideliza.
- **Ejecución con Claude:** Claude en Excel/Sheets (estacionalidad simple, promedio móvil, stock de seguridad); plantilla de entrega estándar.
- **Tipo:** activo, muy productizable (misma plantilla para todos). 1-2 h por entrega en régimen.
- **Capital / 1er dólar:** USD 0 (cuenta Upwork; los "connects" cuestan poco). 1-3 meses (las primeras reseñas en Upwork son lo difícil).
- **Viabilidad AR:** cobro por Upwork → Payoneer. Viable.
- **Riesgos:** precio bajo y competencia global (India/Pakistán/Filipinas); software barato (Forecastly USD 49/mes) reemplaza el gig; ticket chico.
- **Superposición:** PARCIAL (misma matemática que Stock Sano).
- **Score: 5,5/10.**

#### 7. Forecast de demanda y compras con "Claude en Excel" para distribuidoras/mayoristas locales
- **Qué es:** sistema de compras mensual: forecast por familia, sugerido de compra, alertas de quiebre, todo en la planilla que el cliente ya usa.
- **Quién lo hace / señal:** ya hay cursos de "Claude AI in Excel for operations analytics" (forecast, error de pronóstico, planificación) en Udemy ([Udemy](https://www.udemy.com/course/claude-ai-in-excel-for-operations-analytics/)); guías para pequeños comercios de forecast con IA sin software caro ([Jeff Bullas](https://www.jeffbullas.com/thread/can-small-shops-use-ai-to-forecast-inventory-demand-practical-steps-for-beginners/)). Señal de que la herramienta existe y está bajando a no-programadores.
- **Cobro y precio:** setup fijo (estimado USD 200-500) + mantenimiento USD 50-150/mes.
- **Ejecución con Claude:** justamente lo que Claude en Excel hace bien sin programar; documentar fórmulas para que el cliente entienda.
- **Tipo:** activo → semi-pasivo. 1-2 h/cliente/mes.
- **Capital / 1er dólar:** USD 0-20/mes (suscripción Claude). 1-3 meses.
- **Viabilidad AR:** buena; con inflación y lead times erráticos, el forecast "puro" es menos confiable → vender **reglas de compra** más que precisión estadística.
- **Riesgos:** si la herramienta es tan fácil, el cliente "lo hace solo" con ChatGPT; vender criterio + seguimiento, no la planilla. Forecast malo = el cliente culpa al consultor.
- **Superposición:** PARCIAL (módulo de compras de Orden Operativo).
- **Score: 6,5/10.**

#### 8. Ruteo de reparto / última milla para distribuidoras, viandas y comercios con delivery propio
- **Qué es:** rediseñar zonas y días de reparto, configurar un ruteador SaaS, medir km y paradas por hora antes/después.
- **Quién lo hace / señal:** Routific tiene plan gratis hasta 100 pedidos/mes y pagos desde USD 150/mes; Circuit desde USD 100/mes (500 paradas) o USD 20/conductor/mes ([Toolradar](https://toolradar.com/tools/routific/pricing); [Upper](https://www.upperinc.com/comparison/circuit-vs-routific.txt)). Los vendedores de estas herramientas hacen el "consultor" gratis → el valor del consultor está en el **rediseño de zonas/frecuencias**, no en el setup.
- **Cobro y precio:** proyecto fijo (estimado USD 200-600) + success fee sobre ahorro de combustible/horas.
- **Ejecución con Claude:** Claude analiza la planilla de pedidos/direcciones, propone zonas; setup del SaaS (no-code); Google My Maps para visualizar.
- **Tipo:** activo. 10-20 h por proyecto.
- **Capital / 1er dólar:** USD 0. 2-3 meses.
- **Viabilidad AR:** buena en distribuidoras de bebidas/alimentos del interior; el ahorro de combustible es tangible.
- **Riesgos:** la resistencia del chofer/repartidor; datos de direcciones malos; sin hardware/GPS el "después" es difícil de medir.
- **Superposición:** PARCIAL (logística, expansión aguas abajo).
- **Score: 5,5/10.**

#### 9. Gestión de mermas y vencimientos para almacenes, dietéticas, minisúper y farmacias chicas
- **Qué es:** sistema de control de vencimientos (FEFO), conteos sorpresa por categoría de alto riesgo, registro de mermas por causa (vencido, roto, faltante), tablero mensual.
- **Quién lo hace / señal:** a nivel global, empresas como Afresh y Winnow venden IA para medir desperdicio ([NewsNation](https://www.newsnationnow.com/business/tech/artificial-intelligence-technology-tracks-us-food-waste/amp/)). **Sin dato verificado de mermas en retail argentino** (se agotó el presupuesto de búsquedas) — verificar antes de usar cifras.
- **Cobro y precio:** setup fijo + mensual chico (estimado USD 50-100/mes).
- **Ejecución con Claude:** Google Form de registro de mermas → Sheets → resumen mensual redactado por Claude; checklist de FEFO.
- **Tipo:** semi-pasivo una vez instalado (el cliente carga, el reporte sale solo). 1 h/cliente/mes.
- **Capital / 1er dólar:** USD 0. 1-2 meses.
- **Viabilidad AR:** buena, cliente abundante; ticket bajo.
- **Riesgos:** ticket chico + clientes que dejan de cargar datos a las 3 semanas; difícil demostrar ahorro sin línea base.
- **Superposición:** TOTAL (módulo "mermas" de Orden Operativo).
- **Score: 6/10.**

---

### BLOQUE C — Gastronomía y costeo

#### 10. Costeo de recetas + control de mermas + ingeniería de menú para restaurantes/cafeterías
- **Qué es:** recetas estándar con gramaje, factor de corrección/rendimiento, food cost por plato, matriz de ingeniería de menú (qué plato empujar/sacar), registro de desperdicio, actualización de costos ante aumentos.
- **Quién lo hace / señal:** en Rosario la rentabilidad gastronómica cayó de 20-25% histórico a **5-10%** (≈8% típico); los locales pasaron de ~1.700 a ~1.500 y la supervivencia media de un emprendimiento nuevo es ~2 años; los propios dueños citan recetas estándar con control de peso, factor de corrección y control de desperdicio como estrategia (La Capital, 2026-07-28, voces de AEHGAR y restauranteros) ([La Capital](https://www.lacapital.com.ar/negocios/gastronomia-rosarina-modo-supervivencia-menos-rentabilidad-mas-costos-y-una-receta-no-cerrar-n10270966.html)). Afuera: Leanpath desplegó su sistema IA de desperdicio en 14 sitios de Elior North America (noviembre 2025); Winnow ofrece versión "solo tablet" para cocinas chicas ([Verdict](https://www.verdict.co.uk/smart-bin-restaurants/); [CB Insights](https://www.cbinsights.com/company/leanpath)).
- **Cobro y precio:** proyecto fijo (estimado AR: USD 150-500) + actualización mensual de costos (USD 40-100/mes).
- **Ejecución con Claude:** Claude en Sheets arma la plantilla de escandallo; fotos de facturas de proveedores → Claude extrae precios; informe mensual "tus 5 platos que pierden plata".
- **Tipo:** activo → semi-pasivo (la actualización mensual es casi mecánica). 1-2 h/cliente/mes.
- **Capital / 1er dólar:** USD 0. 1-2 meses (dolor agudo y visible).
- **Viabilidad AR:** alta. Clientes: restaurantes, cafeterías, rotiserías, dark kitchens. Cámaras gastronómicas locales como canal.
- **Riesgos:** el gastronómico promedio no tiene tiempo ni disciplina para pesar; alta mortalidad de clientes (si cierran, se pierde el retainer); competencia de software (MarketMan, Apicbase, sistemas POS con costeo) y de contadores. Es un nicho con mucho "consultor gastronómico" (chefs) — el diferencial es el método de ingeniería, no la cocina.
- **Superposición:** PARCIAL (mermas + stock aplicados a cocina).
- **Score: 7/10.**

#### 11. Planilla de costeo y precios para gastronomía/emprendedores (producto digital en español)
- **Qué es:** plantilla Google Sheets/Excel de escandallo + precio de venta + punto de equilibrio, con video tutorial. Versión "pro" con actualización por inflación.
- **Quién lo hace / señal:** existen calculadoras gratuitas en español (Hacé Cuentas: "costo de receta y precio por porción") que capturan búsquedas ([Hacé Cuentas](https://hacecuentas.com/calculadora-costo-receta-precio-por-porcion)); plantillas de ops se venden en Gumroad a ~€12 y en Flevy a ~USD 30 ([Gumroad OEE](https://devls.gumroad.com/l/oee_calc) — link listado el 2026-10-01 pero devolvió 404 al abrirlo; [Flevy](https://flevy.com/browse/marketplace/oee-production-dashboard-and-loss-analyst-12206)).
- **Cobro y precio:** USD 10-30 (Hotmart / Lemon Squeezy / Mercado Pago).
- **Ejecución con Claude:** Claude diseña fórmulas y la guía; Canva para mockups; landing con Hotmart.
- **Tipo:** pasivo/semi-pasivo; 1-3 h/sem (soporte + contenido).
- **Capital / 1er dólar:** USD 0-50. 1-3 meses, pero ventas bajas sin audiencia.
- **Viabilidad AR:** Hotmart cobra en ARS/USD; Mercado Pago local.
- **Riesgos:** competencia gratuita (calculadoras web, plantillas gratis de proveedores de software); sin distribución vende ~0. Estudio de 2026-09-02 ya mostró que plantillas sin audiencia rinden poco.
- **Superposición:** PARCIAL (subproducto del #10).
- **Score: 5/10.**

#### 12. Costeo industrial y lista de precios para talleres/PyMEs productoras con inflación
- **Qué es:** costo estándar por producto (materiales + mano de obra por tiempos + gastos indirectos), margen real por producto/cliente, regla de actualización de lista de precios.
- **Quién lo hace / señal:** dolor documentado: fijar precio "a ojo" es causa de cierre temprano (Hacé Cuentas, 2026) y la industria opera con capacidad ociosa y márgenes comprimidos (UIA 2026, arriba). En AR lo hacen típicamente contadores y consultores de costos; no se verificaron ofertas productizadas específicas.
- **Cobro y precio:** proyecto fijo (estimado USD 300-800) + actualización mensual.
- **Ejecución con Claude:** Claude en Excel arma el modelo de costos y la sensibilidad; tiempos tomados con video (ver #13).
- **Tipo:** activo; 15-30 h por proyecto, 1-2 h/mes después.
- **Capital / 1er dólar:** USD 0. 2-4 meses.
- **Viabilidad AR:** buena; ojo, el contador del cliente es competidor/aliado.
- **Riesgos:** requiere entender contabilidad de costos con solidez; error de costeo = decisiones de precio equivocadas con responsabilidad reputacional.
- **Superposición:** NINGUNA directa (complementa: el stock inmovilizado entra en el costo).
- **Score: 6/10.**

---

### BLOQUE D — Planta: tiempos, balanceo, OEE, mantenimiento, calidad

#### 13. Estudio de tiempos y métodos con video + IA ("time study express") para talleres
- **Qué es:** filmar ciclos con el celular, cronometrar elementos con software de video, separar valor agregado / desperdicio (7 mudas), proponer método mejorado y tiempo estándar.
- **Quién lo hace / señal (auge fuerte 2026):** **Squint** lanzó su "Lean Manufacturing Agent" el **2026-08-24**: con un ciclo filmado con celular clasifica cada segundo en valor agregado/desperdicio y arma Yamazumi contra takt ([Let's Data Science](https://letsdatascience.com/news/squint-applies-video-ai-to-factory-workflows-d66cd756)); clientes citados: Pepsi y Carolina Handling (PYMNTS, 2026-09-11, [PYMNTS](https://www.pymnts.com/?p=4178078)). **Iteros Lens** (fundada 2026-06-10) ofrece estudio de tiempos por video en el navegador con **plan gratis** y export a Excel ([StartupHub](https://www.startuphub.ai/startups/iteros.md)). **Coats Digital GSD RealMotion** (confección) lanzado 2026-08-19 ([IMARC](https://www.imarcengineering.com/news/coats-digital-gsd-realmotion-ai-time-motion-studies)). **Khenda** (SaaS de time study con IA) ([Crunchbase](https://crunchbase.com/organization/khenda)).
- **Cobro y precio:** por estación/proceso estudiado (estimado AR: USD 150-400 por proceso) o paquete.
- **Ejecución con Claude:** Iteros (gratis) para marcar elementos; Claude analiza la planilla, identifica mudas, redacta método propuesto y hoja de trabajo estándar.
- **Tipo:** activo; 5-10 h por proceso.
- **Capital / 1er dólar:** USD 0-100 (trípode). 2-4 meses.
- **Viabilidad AR:** confección (textil), metalmecánica liviana, alimentos. Pero con capacidad ociosa ~41% el argumento debe ser **costo por unidad** (horas extra, premios), no capacidad.
- **Riesgos:** el software se vuelve autoservicio (Squint apunta justo a reemplazar parte de este trabajo); en AR los gremios/operarios pueden resistir ser filmados (relaciones laborales sensibles); credibilidad junior frente al jefe de planta.
- **Superposición:** NINGUNA (planta, no depósito) — mismo método de "medir antes/después".
- **Score: 6/10.**

#### 14. "Time study as a service" remoto: el cliente filma, vos analizás (exportable)
- **Qué es:** variante remota del #13 para plantas de cualquier país: reciben un protocolo de filmación, suben videos, reciben análisis, Yamazumi y propuesta.
- **Quién lo hace / señal:** las mismas herramientas (Squint/Iteros) muestran que el flujo "filmar con celular → análisis" ya es aceptado (2026). Oferta de consultor remoto específica: **no verificada**.
- **Cobro y precio:** USD 100-300 por proceso (estimado), Payoneer/Upwork.
- **Ejecución con Claude:** igual que #13 + traducción/redacción en inglés con Claude.
- **Tipo:** activo remoto, muy productizable (protocolo + plantilla de entrega).
- **Capital / 1er dólar:** USD 0. 3-6 meses.
- **Viabilidad AR:** cobro vía Upwork/Payoneer OK.
- **Riesgos:** competir con un SaaS que hace lo mismo más barato; confidencialidad de videos de planta; sin casos no hay confianza.
- **Superposición:** NINGUNA.
- **Score: 4,5/10.**

#### 15. Balanceo de línea / Yamazumi para confección y armado
- **Qué es:** con tiempos por operación, rebalancear la línea contra el takt, reasignar tareas, reducir cuello de botella.
- **Quién lo hace / señal:** es la función núcleo que Squint y Coats GSD automatizan (agosto 2026, ver #13); el sector confección es el blanco explícito de Coats.
- **Cobro y precio:** proyecto (estimado USD 300-800).
- **Ejecución con Claude:** Claude en Excel arma el Yamazumi y prueba combinaciones.
- **Tipo:** activo, presencial.
- **Capital / 1er dólar:** USD 0. 3-6 meses.
- **Viabilidad AR:** textil argentino en caída fuerte (UIA 2026) → mercado reducido.
- **Riesgos:** sector en crisis; se superpone con #13 (venderlos juntos).
- **Superposición:** NINGUNA.
- **Score: 4,5/10.**

#### 16. OEE "light" con planilla/Forms + tablero para PyMEs metalmecánicas y de alimentos
- **Qué es:** registrar paradas, velocidad y scrap por turno (Google Forms en tablet), calcular OEE, Pareto de pérdidas, reunión semanal de 15 min.
- **Quién lo hace / señal:** plantillas OEE se venden a €12 (Gumroad) y USD 30 (Flevy) ([Flevy](https://flevy.com/browse/marketplace/oee-production-dashboard-and-loss-analyst-12206)); Teeptrak publica plantillas gratis para captar ([Teeptrak](https://teeptrak.com/fr/?p=88127)) — conflicto de interés: venden sensores.
- **Cobro y precio:** setup fijo (USD 200-500) + acompañamiento mensual (USD 100-200).
- **Ejecución con Claude:** Forms + Sheets + Looker Studio; Claude escribe el resumen semanal de pérdidas.
- **Tipo:** activo → semi-pasivo.
- **Capital / 1er dólar:** USD 0-150 (tablet usada opcional). 2-4 meses.
- **Viabilidad AR:** media; el OEE vende "capacidad" en un contexto de 41% capacidad ociosa → reformular como "costo por pieza y scrap".
- **Riesgos:** registro manual se abandona; jefes de planta suelen saber de OEE más que un junior.
- **Superposición:** NINGUNA.
- **Score: 5/10.**

#### 17. Plan de mantenimiento preventivo + CMMS liviano (setup MaintainX/UpKeep)
- **Qué es:** inventario de activos, plan de preventivo, órdenes de trabajo en el celular, KPIs (MTBF/MTTR), con un CMMS de plan gratuito.
- **Quién lo hace / señal:** MaintainX tiene plan gratis (solo órdenes) y pago desde USD 16/usuario/mes; UpKeep apunta a fabricantes chicos ([Oxmaint 2025](https://oxmaint.com/article/best-cmms-software-comparison-2025); [Inzonex](https://inzonex.co.uk/ai/tools/upkeep)). Verdantix publicó Green Quadrant CMMS 2025 (categoría madura) ([Verdantix](https://www.verdantix.com/report/green-quadrant-industrial-computerized-maintenance-management-systems-cmms-2025)).
- **Cobro y precio:** setup fijo (estimado USD 300-800).
- **Ejecución con Claude:** Claude arma planes de mantenimiento desde manuales de máquinas (PDF) y la carga masiva en Excel.
- **Tipo:** activo; proyecto de 15-30 h.
- **Capital / 1er dólar:** USD 0. 3-6 meses.
- **Viabilidad AR:** media (plantas con menos producción postergan gasto).
- **Riesgos:** requiere conocimiento de mantenimiento industrial que un junior no tiene; el técnico de mantenimiento del cliente desconfía.
- **Superposición:** NINGUNA.
- **Score: 4,5/10.**

#### 18. Control de calidad visual con IA (prototipo de inspección con cámara)
- **Qué es:** detectar defectos con una cámara y un modelo entrenado en plataforma no-code.
- **Quién lo hace / señal:** Landing AI vende inspección visual a manufactura con plan "Explore" pay-as-you-go ([PricingSaaS](https://pricingsaas.com/companies/landing)); guías de costo de sistemas de visión (SmartDev) ([SmartDev](https://smartdev.com/fr/computer-vision-cost-manufacturing-complete-cv-system-pricing-breakdown/)).
- **Cobro y precio:** proyectos de miles de USD.
- **Ejecución con Claude:** limitada sin programar; requiere iluminación, cámara, integración.
- **Tipo:** activo técnico.
- **Capital / 1er dólar:** USD 200-1.000+ en hardware. 6+ meses.
- **Viabilidad AR:** baja para este perfil.
- **Riesgos:** hardware, integración, falsos positivos, responsabilidad sobre calidad. No encaja con "no programa + bajo presupuesto".
- **Superposición:** NINGUNA.
- **Score: 2,5/10.**

#### 19. Kit 5S + gestión visual + auditoría mensual con fotos e IA (talleres y depósitos)
- **Qué es:** implementación 5S en un sector piloto en 2-4 semanas; auditoría mensual: el cliente sube fotos, Claude puntúa contra checklist y devuelve informe con acciones.
- **Quién lo hace / señal:** INTI + JICA ("Kaizen TANGO") asistió a **100 PyMEs y 27 organizaciones** con 116 asesores; el PAC Kaizen financió **>280 empresas** (programas de años previos) ([INTI booklet 2023](https://web2.inti.gob.ar/www/assets/uploads/files/tecnologia-de-gestion/2023/BOOKLET-2023.pdf); [INTI guía](https://www.inti.gob.ar/assets/uploads/files/tecnologia-de-gestion/guia-tg-kt-2019.pdf)) → hay una base de PyMEs ya "educadas" en Kaizen, y una red de consultores formados (competencia).
- **Cobro y precio:** implementación fija (USD 200-600) + auditoría mensual por fotos (USD 30-80/mes).
- **Ejecución con Claude:** checklist 5S en Forms; Claude analiza fotos (visión) y redacta; cartelería en Canva.
- **Tipo:** semi-pasivo en la parte de auditoría (asíncrona). 0,5 h/cliente/mes.
- **Capital / 1er dólar:** USD 50-150 (etiquetas, cinta de piso). 1-3 meses.
- **Viabilidad AR:** buena; 5S es barato y visible (antes/después en fotos = marketing).
- **Riesgos:** 5S "de cartel" que se cae en 2 meses; la auditoría mensual se percibe como prescindible.
- **Superposición:** PARCIAL (sostenimiento del orden de depósito de Orden Operativo; es el "mantenimiento" que evita la recaída).
- **Score: 6,5/10.**

#### 20. Coaching de mejora continua / Kaizen mensual (retainer)
- **Qué es:** 2 sesiones/mes con el equipo de la PyME para resolver un problema por mes (A3/PDCA), con tablero de seguimiento.
- **Quién lo hace / señal:** la red INTI de tecnologías de gestión y los ex-asesores Kaizen TANGO hacen esto (ver #19). Oferta productizada privada: no verificada.
- **Cobro y precio:** retainer estimado USD 150-400/mes.
- **Ejecución con Claude:** plantillas A3, minutas automáticas (Claude resume audio de la reunión), seguimiento en Sheets.
- **Tipo:** activo; 4-6 h/cliente/mes.
- **Capital / 1er dólar:** USD 0. 3-6 meses.
- **Viabilidad AR:** media.
- **Riesgos:** "coach" junior sin canas = baja credibilidad; competencia de asesores INTI con años.
- **Superposición:** PARCIAL (retainer posterior a Orden Operativo).
- **Score: 5/10.**

#### 21. Auditoría de energía por facturas y consumo para PyMEs (post-tarifazo)
- **Qué es:** analizar 12 meses de facturas de luz/gas: potencia contratada, penalidades por factor de potencia, cambio de categoría tarifaria, horarios; quick wins sin inversión; derivar inversiones (LED, capacitores, solar) a instaladores con comisión.
- **Quién lo hace / señal:** en 2026 hubo reclamos de PyMEs por aumentos tarifarios (Diputados pidió suspender cuadro de Naturgy BAN; empresarios hablan de "mortandad de pymes") ([HCDN](https://rest.hcdn.gob.ar/web/proyectos/292446/adjuntos/106156); [LM Neuquén](https://mase.lmneuquen.com/economia/empresarios-alertan-que-el-tarifazo-lleva-mortandad-pymes-n1100249)); Grant Thornton publica sobre "energía más cara: cómo bajar costos" ([El Economista](https://eleconomista.com.ar/energia/energia-mas-cara-decisiones-urgentes-como-bajar-costos-avanzar-transicion-renovable-argentina-n91404)); existe línea BNA para equipos eficientes (misma fuente).
- **Cobro y precio:** fijo bajo (USD 100-300) o **success fee** (% del ahorro del primer año).
- **Ejecución con Claude:** fotos/PDF de facturas → Claude extrae datos y arma tabla; reglas tarifarias de la distribuidora local.
- **Tipo:** activo, muy productizable (las facturas tienen formato fijo por distribuidora). 3-6 h por cliente.
- **Capital / 1er dólar:** USD 0. 1-3 meses.
- **Viabilidad AR:** buena; ahorro "plata en mano" vende más que productividad. Las comisiones de instaladores solares son ingreso adicional.
- **Riesgos:** cuadros tarifarios cambian seguido y varían por provincia; mediciones eléctricas reales requieren matrícula/instrumental; competencia de instaladores que hacen el análisis gratis para vender paneles.
- **Superposición:** NINGUNA.
- **Score: 6/10.**

---

### BLOQUE E — Documentación, digitalización, tableros, normas

#### 22. SOPs y manuales de procesos con IA (del video del operario al procedimiento + checklist)
- **Qué es:** filmar/grabar al que sabe hacer la tarea → procedimiento estándar escrito con fotos, checklist y quiz de capacitación. "Capturar el conocimiento que está en la cabeza de la gente."
- **Quién lo hace / señal:** gigs de SOPs en Upwork a USD 75 / 175 / 350 (y otros a 30/65/120) ([Upwork](https://www.upwork.com/services/product/admin-customer-support-professional-sops-and-process-documentation-that-streamline-your-operations-2026230545925501764)); agencias proponen "SOP generator service" con suscripción por volumen (Ciela, 2026-02-25, [Ciela](https://ciela.ai/blogs/ai-sop-generator-service-for-clients) — vende la herramienta, conflicto de interés). El CEO de Squint resume la tesis: "mucho estaba en la cabeza de la gente y nunca se documentó" (PYMNTS, 2026-09-11).
- **Cobro y precio:** por SOP (USD 30-150 afuera; estimado AR USD 20-60) o paquete "manual de operaciones" (USD 300-1.000).
- **Ejecución con Claude:** Claude transcribe el audio/video, estructura el SOP, genera checklist y quiz; Canva/Docs para formato; Scribe/Guidde (planes gratis) para tareas de computadora.
- **Tipo:** activo pero muy productizable; régimen 3-6 h por manual chico. Puede venderse remoto.
- **Capital / 1er dólar:** USD 0. 1-2 meses.
- **Viabilidad AR:** buena local (franquicias, gastronomía, depósitos, clínicas) + remota en USD (Upwork).
- **Riesgos:** commodity global en Upwork (precio a la baja por IA); el valor se defiende con **método** (trabajo estándar, puntos clave de calidad/seguridad) y con nicho (ops/depósito), no con "escribo bien".
- **Superposición:** PARCIAL (entregable natural de Orden Operativo: SOP de picking, recepción, conteo).
- **Score: 7/10.**

#### 23. Digitalización de procesos en papel con AppSheet / Google Forms (remitos, partes, checklists)
- **Qué es:** reemplazar planillas de papel (partes de producción, checklists de camión, recepción de mercadería, órdenes de trabajo) por apps no-code en el celular con datos en Sheets.
- **Quién lo hace / señal:** "Gemini en AppSheet" permite describir el proceso en palabras y genera la app ([Google Workspace Marketplace](https://workspace.google.com/marketplace/app/gemini_in_appsheet/1035879554174?hl=ar)); agencias locales publican guías de transformación digital PyME 2026 ([Develop Argentina, 2026-06-25](https://www.developargentina.com/blog/transformacion-digital-pymes-argentina-por-donde-empezar-2026)); gigs en Fiverr de "sistemas de control para negocios" en AppSheet ([Fiverr](https://fiverr.com/daniloruizg/control-systems-for-businesses)). El estudio Di Tella/Fundar 2026 marca "infraestructura digital insuficiente" como barrera a la IA → digitalizar es el paso previo.
- **Cobro y precio:** por app (estimado AR USD 150-500) + soporte mensual (USD 30-100).
- **Ejecución con Claude:** AppSheet es no-code; Claude guía la estructura de datos y redacta fórmulas.
- **Tipo:** activo → semi-pasivo (apps estables requieren poco soporte). 1 h/cliente/mes.
- **Capital / 1er dólar:** USD 0 (AppSheet gratis para prototipos; el cliente paga licencias Workspace si escala). 1-2 meses.
- **Viabilidad AR:** buena.
- **Riesgos:** competencia de "automatizadores" (ver scriptHouse en la ficha del 2026-09-07); dependencia de Google; si el proceso de papel estaba mal diseñado, digitalizarlo solo acelera el desorden (vender rediseño + app).
- **Superposición:** PARCIAL (herramienta de implementación de Orden Operativo: app de stock con QR, conteo cíclico).
- **Score: 6,5/10.**

#### 24. Tableros de KPIs operativos (Looker Studio) para PyMEs
- **Qué es:** tablero semanal de ventas, stock, quiebres, mermas, productividad, conectado a Sheets/exports del sistema.
- **Quién lo hace / señal:** Fiverr lista **~555 servicios de Looker Studio** entre USD 10 y 595 ([The Bricks, 2025-10-21](https://www.thebricks.com/resources/guide-does-looker-studio-cost-money); [Fiverr](https://block.fiverr.com/gigs/looker-studio)) → mercado global saturado y barato. Looker Studio es gratis; el costo está en conectores (USD 50+/mes).
- **Cobro y precio:** local estimado USD 150-400 por tablero + USD 30-80/mes de mantenimiento.
- **Ejecución con Claude:** Looker Studio es no-code; Claude define KPIs y fórmulas calculadas.
- **Tipo:** semi-pasivo una vez armado.
- **Capital / 1er dólar:** USD 0. 1-2 meses.
- **Viabilidad AR:** media; vender como **parte** de un proyecto, no suelto.
- **Riesgos:** commodity; "tablero que nadie mira" si no hay rutina de gestión detrás.
- **Superposición:** PARCIAL (el "después medido" de Orden Operativo).
- **Score: 5/10** suelto; suma mucho como componente.

#### 25. Documentación ISO 9001 asistida por IA para PyMEs proveedoras (gap analysis + manual + procedimientos)
- **Qué es:** preparar a una PyME que necesita ISO 9001 porque un cliente grande se lo exige: análisis de brechas, mapa de procesos, procedimientos, registros, auditoría interna. La certificación la da un organismo aparte.
- **Quién lo hace / señal:** Core Business Solutions vende ISO 9001 "en ~4 meses" con precio fijo **USD 6.000-15.000** según alcance; costo total típico para una PyME de 1-50 empleados **USD 5.000-15.000**, con gap analysis USD 100-3.000 y documentación USD 1.500-3.000 ([The Core Solution](https://www.thecoresolution.com/iso-9001-certification-cost); [9001 Simplified](https://www.9001simplified.com/learn/iso-9001-certification-cost.php)) — fuentes que venden el servicio (conflicto de interés).
- **Cobro y precio:** gap analysis fijo + documentación por etapas. AR: estimado USD 800-3.000 por proyecto completo (no verificado).
- **Ejecución con Claude:** Claude es muy bueno redactando procedimientos y matrices; Claude Projects con la norma (el texto ISO es pago y con copyright — el usuario debe comprarlo, no "pedírselo" a la IA).
- **Tipo:** activo; 40-80 h por proyecto.
- **Capital / 1er dólar:** USD 50-150 (compra de la norma; curso de auditor interno recomendable, costo aparte). 4-8 meses.
- **Viabilidad AR:** media; hay mercado en proveedores de automotrices/petroleras/alimenticias, pero muchos consultores ISO con trayectoria.
- **Riesgos:** sin credencial (auditor interno/líder) es difícil; si el cliente no certifica, el consultor queda mal; la IA genera documentación "de manual" que el auditor detecta si no refleja la práctica real.
- **Superposición:** NINGUNA.
- **Score: 4,5/10.**

#### 26. Back-office documental con IA para profesionales de Higiene y Seguridad (white-label)
- **Qué es:** **no** prestar el servicio de H&S (requiere matrícula), sino trabajar **para** los técnicos/licenciados/ingenieros en H&S matriculados que atienden 10-40 PyMEs cada uno: redactar relevamientos, programas de capacitación, informes mensuales, matrices de riesgo, registros, a partir de sus fotos y notas de visita.
- **Quién lo hace / señal:** honorarios mínimos éticos sugeridos para dirección técnica de un servicio de H&S para empresas de **hasta 5 trabajadores: ARS 156.800/mes desde 2026-07-01 y ARS 163.100/mes desde 2026-09-01** (Federación Química Argentina / Consejo, [PDF 2026-09](https://quimica.org.ar/wp-content/uploads/2026/09/VALORES-MINIMOS-SUGERIDOS-A-PARTIR-DEL-01092026.pdf)) → cada profesional factura por cliente un monto recurrente y su cuello de botella es el papeleo. El servicio externo de H&S es obligatorio para empleadores (Ley 19.587 y decretos; no re-verificado en esta sesión). Oferta de "back-office para H&S con IA" en AR: **no verificada** (hueco probable).
- **Cobro y precio:** por informe (estimado ARS 10.000-30.000) o mensual por profesional atendido.
- **Ejecución con Claude:** Claude Projects con plantillas del profesional; fotos de visita → borrador de informe; checklist por rubro.
- **Tipo:** semi-pasivo con 3-5 profesionales clientes; ~1 h por informe al inicio, menos después.
- **Capital / 1er dólar:** USD 0. 1-2 meses (pocos clientes B2B, se venden por recomendación).
- **Viabilidad AR:** alta en venta (profesionales independientes, decisión rápida); cobro local en ARS (indexar).
- **Riesgos:** **responsabilidad legal**: el informe lo firma el matriculado, que debe revisarlo — si el profesional firma sin leer, hay riesgo ético/legal; datos de trabajadores (privacidad); el profesional puede aprender a usar Claude solo (el moat es la plantilla + velocidad + volumen).
- **Superposición:** NINGUNA.
- **Score: 6,5/10.**

#### 27. Process mining "light" (análisis de registros del ERP/Excel con Claude) para PyMEs medianas
- **Qué es:** tomar exports de pedidos/facturas/órdenes con timestamps y reconstruir el flujo real (dónde se demoran los pedidos, retrabajos, desvíos).
- **Quién lo hace / señal:** Celonis es "solo accesible para grandes empresas" según reviews de usuarios ([PeerSpot](https://www.peerspot.com/product_reviews/celonis-review-3876800-by-gul-ansari)); la startup alemana Logatik vende implementación de Celonis a empresas "más chicas" (USD 100M-1.000M de facturación) ([Acceleration Economy](https://accelerationeconomy.com/?p=33487)) — o sea, "chico" para process mining sigue siendo grande. Alternativas: Power Automate Process Mining, Bizagi.
- **Cobro y precio:** proyecto USD 1.000+ (afuera).
- **Ejecución con Claude:** limitada a análisis exploratorio en Excel con timestamps; sin herramienta real de process mining el resultado es básico.
- **Tipo:** activo técnico.
- **Capital / 1er dólar:** USD 0-500. 6+ meses.
- **Viabilidad AR:** baja (PyMEs AR raramente tienen logs limpios).
- **Riesgos:** mercado de empresas grandes; requiere datos y skills de datos.
- **Superposición:** NINGUNA.
- **Score: 3/10.**

#### 28. "Diagnóstico de IA y automatización operativa" (AI readiness con base en procesos)
- **Qué es:** relevar procesos, identificar 3-5 tareas donde IA/no-code ahorran horas, priorizar por ROI, y entregar plan + 1 quick win implementado.
- **Quién lo hace / señal:** 42% de PyMEs AR usa IA, mayoría experimentando; barrera #1 falta de talento (UTDT/Fundar, 2026-05-01). 54% de PyMEs en las Américas usa IA (encuesta Microsoft 2025, [Microsoft LATAM](https://news.microsoft.com/source/latam/noticias-de-microsoft/encuesta-pymes-2025-54-de-las-pymes-en-las-americas-usa-ia/)). Contraejemplo de cautela: Gartner proyecta >40% de proyectos de IA agéntica cancelados a 2027 (citado en ficha 2026-09-07).
- **Cobro y precio:** fijo (estimado AR USD 150-500) + implementación aparte.
- **Ejecución con Claude:** Claude mismo es la demo; quick wins en Gmail/Sheets/Forms.
- **Tipo:** activo.
- **Capital / 1er dólar:** USD 0. 1-3 meses.
- **Viabilidad AR:** buena demanda, **altísima competencia** (agencias de automatización, scriptHouse, AAA).
- **Riesgos:** saturado por gurús de "AI Automation Agency" (conflicto de interés: venden el curso); un no-programador compite en desventaja contra devs que construyen. Diferenciarse anclando en **procesos** (ingeniería) y no en "IA".
- **Superposición:** PARCIAL (es la consultora original del 2026-09-07 antes del pivote a Orden Operativo).
- **Score: 5,5/10.**

---

### BLOQUE F — Roles a tiempo parcial y remoto

#### 29. Jefe de operaciones a tiempo parcial (fractional ops manager) para PyMEs locales
- **Qué es:** 1 día/semana fijo en una PyME de 10-50 empleados: indicadores, reuniones de operación, compras, stock, mejoras.
- **Quién lo hace / señal:** en EE.UU. un fractional COO cobra **USD 3.000-15.000/mes** (o USD 200-500/h) para empresas de USD 1-15 M de facturación ([Kamyar Shah](https://kamyarshah.com/fractional-coo-rates-cost-breakdown/) — consultor que vende el servicio, conflicto de interés). En LATAM: 128 M de trabajadores independientes, crecimiento proyectado 30% en 2025 (Landa, informe 2025, [Substack](https://landaclub1.substack.com/p/new-report-fractional-work-and-the)); Argentina #2 en densidad de freelancers (misma fuente, no auditada).
- **Cobro y precio:** retainer mensual. Para un junior en AR: estimado USD 300-700/mes por 1 día/semana (no verificado) — es "jefe de operaciones part-time", **no COO**.
- **Ejecución con Claude:** Claude como "segundo cerebro": minutas, tableros, análisis de datos, redacción de procedimientos.
- **Tipo:** activo; 8-10 h/sem por cliente.
- **Capital / 1er dólar:** USD 0. 2-4 meses.
- **Viabilidad AR:** buena si sale de la red de contactos o como continuidad de un proyecto Orden Operativo exitoso.
- **Riesgos:** "fractional COO" está inflado por coaches en LinkedIn; un junior no puede venderse como C-level; riesgo de convertirse en empleado sin beneficios.
- **Superposición:** PARCIAL (retainer natural post-proyecto de Orden Operativo).
- **Score: 6/10.**

#### 30. Ops manager remoto para e-commerce/agencias de EE.UU. (contractor LATAM)
- **Qué es:** trabajar remoto como coordinador/gerente de operaciones (inventario, proveedores, 3PL, SOPs) para una marca DTC o agencia de EE.UU.
- **Quién lo hace / señal:** agencias de staffing LATAM ubican perfiles argentinos a ~USD 2.000/mes (ej. marketing specialist vs ~USD 5.800 en EE.UU.) ([Hire in South](https://www.hireinsouth.com/post/hire-a-latam-marketing-specialist-for-2-000-month)); hay avisos de "E-commerce Operations Manager — Remote LATAM" ([Remowork](https://remowork.life/jobs/6a7da6bf413a2a759fa984d0/e-commerce-operations-manager-remote-or-latam)).
- **Cobro y precio:** USD 1.200-2.500/mes (rango estimado para junior-semi senior; no verificado).
- **Ejecución con Claude:** productividad personal (análisis, SOPs, reportes) — Claude como multiplicador.
- **Tipo:** activo (empleo/contractor); 20-40 h/sem.
- **Capital / 1er dólar:** USD 0. 1-3 meses (proceso de selección).
- **Viabilidad AR:** cobro vía Deel/Payoneer; muy común.
- **Riesgos:** es un **empleo**, no un negocio; inglés fluido; competencia de toda LATAM. Pero es la vía de **ingreso en USD más probable a corto plazo** y genera experiencia/casos reales.
- **Superposición:** PARCIAL (misma capacidad, como empleado).
- **Score: 6/10** (como ingreso; 3/10 como "negocio").

#### 31. Armador de proyectos para programas de apoyo (PAC / Expertos PyME / provinciales)
- **Qué es:** preparar la presentación de PyMEs a programas que financian asistencia técnica (ANR) y luego ejecutar la asistencia.
- **Quién lo hace / señal:** PAC financiaba 70% con ANR, con modalidad Kaizen 4.0 ([A24](https://www.a24.com/pymes/el-gobierno-lanza-el-pac-mejorar-la-competitividad-las-pymes-n822844)); Expertos PyME CABA tuvo convocatoria 2025-03 y hoy **no tiene convocatoria vigente** (consultado 2026-10-01); algunas provincias lanzan programas de reactivación ([Diario Jornada](https://diariojornada.com.ar/283377/magazine/provincia_convoca_a_pymes_para_el_programa_de_reactivacion_productiva)).
- **Cobro y precio:** % del ANR o fee por presentación.
- **Ejecución con Claude:** redacción de formularios y planes.
- **Tipo:** activo, estacional.
- **Capital / 1er dólar:** USD 0. Incierto (depende de convocatorias).
- **Viabilidad AR:** baja hoy (programas nacionales recortados desde 2024).
- **Riesgos:** dependencia total de políticas públicas; requisitos de registro de expertos; pagos estatales lentos.
- **Superposición:** PARCIAL (vía de financiar al cliente de Orden Operativo — **vigilar convocatorias provinciales**, no depender).
- **Score: 3/10.**

---

### BLOQUE G — Productos digitales y educación para el nicho

#### 32. Pack de plantillas de ingeniería industrial en español (ABC, punto de reorden, OEE, balanceo, VSM, 5S)
- **Qué es:** 8-12 plantillas Excel/Sheets en español con instrucciones y ejemplos resueltos.
- **Quién lo hace / señal:** Systems2win vende 150+ plantillas lean (5S, FMEA, OEE, VSM, A3) ([AME](https://www.ame.org/node/37203)); Flevy vende plantilla OEE a USD 30; Gumroad €12 (ver #11). En español la oferta es menor (no verificado cuantitativamente).
- **Cobro y precio:** USD 15-49 el pack (Hotmart/Lemon Squeezy).
- **Ejecución con Claude:** Claude en Excel construye y testea; videos con Loom.
- **Tipo:** pasivo/semi-pasivo; 1-2 h/sem.
- **Capital / 1er dólar:** USD 0-50. 1-3 meses (ventas bajas sin audiencia).
- **Viabilidad AR:** cobro vía Hotmart/Lemon Squeezy → Payoneer. Clientes: estudiantes de ingeniería industrial LATAM, jefes de depósito.
- **Riesgos:** plantillas gratis abundan; estudiantes pagan poco; el estudio del 2026-09-02 mostró que productos digitales sin audiencia rinden mediana muy baja.
- **Superposición:** PARCIAL (empaqueta las herramientas de Orden Operativo; sirve de lead magnet).
- **Score: 5/10.**

#### 33. Curso/taller "Claude en Excel para logística y operaciones" en español (Hotmart / en vivo)
- **Qué es:** curso práctico para jefes de depósito/compras/producción: ABC, reorden, forecast, tableros, SOPs usando Claude sin programar.
- **Quién lo hace / señal:** existe en inglés ("Claude AI in Excel for Operations Analytics", Udemy) ([Udemy](https://www.udemy.com/course/claude-ai-in-excel-for-operations-analytics/)); en España se venden cursos de Excel para logística (UNO Logística: "Excel avanzado para optimizar la operativa de logística", mayo 2026; "Excel intermedio sector logístico", febrero 2026) ([UNO](https://unologistica.org/wp-content/uploads/2025/12/ID-149-PROGRAMA-Excel-avanzado-para-optimizar-.pdf)); curso "Excel avanzado para ingenieros" a €195 ([Educaweb](https://www.educaweb.com/curso/training-excel-avanzado-ingenieros-on-line-389734/)).
- **Cobro y precio:** USD 30-150 grabado; talleres en vivo para empresas USD 300-1.000.
- **Ejecución con Claude:** guión, ejercicios y datasets armados con Claude; grabación con OBS/Loom.
- **Tipo:** semi-pasivo (grabado) / activo (en vivo).
- **Capital / 1er dólar:** USD 0-100. 2-4 meses.
- **Viabilidad AR:** Hotmart funciona en AR; venta corporativa local por factura.
- **Riesgos:** **conflicto de interés propio**: enseñar algo que todavía no aplicaste en clientes = el clásico gurú. Hacerlo **después** de 3-5 casos reales. La interfaz de Claude cambia rápido → el curso envejece.
- **Superposición:** PARCIAL (convierte el método de Orden Operativo en producto).
- **Score: 5,5/10** (sube a 7 con casos).

#### 34. Calculadoras/simuladores web gratuitos de ingeniería industrial (tool-SEO) como imán de clientes
- **Qué es:** calculadoras de punto de reorden, EOQ, OEE, takt time, costo por plato, en español, gratis, que capturan búsquedas y derivan a consultoría/plantillas.
- **Quién lo hace / señal:** Hacé Cuentas posiciona calculadoras en español (ej. costo de receta, costo laboral) ([Hacé Cuentas](https://hacecuentas.com/calculadora-costo-laboral-empleado)). El estudio del 2026-09-02 ya rankeó "micro-herramientas web + MCP (tool-SEO)" con 7/10 como más resistente a AI Overviews.
- **Cobro y precio:** indirecto (leads); eventualmente AdSense/afiliados (estos últimos ya descartados en el repo).
- **Ejecución con Claude:** Claude Code puede generar HTML/JS simple, pero **requiere** algo de manejo técnico para publicar (Cloudflare Pages). Para un no-programador: hacerlo en Sheets publicados o Notion.
- **Tipo:** pasivo; 1 h/sem.
- **Capital / 1er dólar:** USD 0-15 (dominio). 4-8 meses.
- **Viabilidad AR:** sin problema.
- **Riesgos:** lento; tráfico incierto; competencia de calculadoras genéricas.
- **Superposición:** PARCIAL con Orden Operativo (lead magnet) y **con el proyecto stack-de-datos** (idea #2 del estudio 2026-09-02).
- **Score: 4,5/10** (para este perfil no-programador).

---

## Tabla resumen

| # | Idea | Tipo | Superposición O.O. | Score |
|---|---|---|---|---|
| 1 | Diagnóstico Express precio fijo | Activo | PARCIAL (entrada) | 7 |
| 2 | Stock Sano (ABC + reorden) | Activo→semi | TOTAL | 7,5 |
| 3 | Re-slotting/layout depósito | Activo | TOTAL | 7 |
| 4 | Ops para sellers Mercado Libre | Activo→semi | PARCIAL | 7,5 |
| 5 | Consultor 3PL Shopify (USD) | Activo remoto | PARCIAL | 4 |
| 6 | Forecast Amazon FBA (Upwork) | Activo productizado | PARCIAL | 5,5 |
| 7 | Forecast/compras con Claude en Excel | Activo→semi | PARCIAL | 6,5 |
| 8 | Ruteo de reparto | Activo | PARCIAL | 5,5 |
| 9 | Mermas y vencimientos retail chico | Semi | TOTAL | 6 |
| 10 | Costeo de recetas + mermas gastronomía | Activo→semi | PARCIAL | 7 |
| 11 | Planilla costeo gastronomía (digital) | Pasivo | PARCIAL | 5 |
| 12 | Costeo industrial y precios | Activo | NINGUNA | 6 |
| 13 | Tiempos y métodos con video+IA | Activo | NINGUNA | 6 |
| 14 | Time study remoto (exportable) | Activo remoto | NINGUNA | 4,5 |
| 15 | Balanceo de línea/Yamazumi | Activo | NINGUNA | 4,5 |
| 16 | OEE light | Activo→semi | NINGUNA | 5 |
| 17 | CMMS liviano/preventivo | Activo | NINGUNA | 4,5 |
| 18 | Calidad visual con IA | Activo técnico | NINGUNA | 2,5 |
| 19 | Kit 5S + auditoría por fotos | Semi | PARCIAL | 6,5 |
| 20 | Coaching Kaizen mensual | Activo | PARCIAL | 5 |
| 21 | Auditoría de energía por facturas | Activo | NINGUNA | 6 |
| 22 | SOPs con IA | Activo productizado | PARCIAL | 7 |
| 23 | Digitalización papel → AppSheet | Activo→semi | PARCIAL | 6,5 |
| 24 | Tableros KPI Looker Studio | Semi | PARCIAL | 5 |
| 25 | ISO 9001 asistida por IA | Activo | NINGUNA | 4,5 |
| 26 | Back-office IA para H&S | Semi | NINGUNA | 6,5 |
| 27 | Process mining light | Activo técnico | NINGUNA | 3 |
| 28 | Diagnóstico IA/automatización | Activo | PARCIAL | 5,5 |
| 29 | Jefe de ops part-time | Activo | PARCIAL | 6 |
| 30 | Ops manager remoto EE.UU. | Empleo/contractor | PARCIAL | 6 |
| 31 | Armador de proyectos ANR | Activo | PARCIAL | 3 |
| 32 | Pack plantillas IE en español | Pasivo | PARCIAL | 5 |
| 33 | Curso Claude en Excel para ops | Semi | PARCIAL | 5,5 |
| 34 | Calculadoras IE (tool-SEO) | Pasivo | PARCIAL (+stack) | 4,5 |

---

## Top 5 de este frente

1. **Stock Sano + Ops para sellers de Mercado Libre (#2 + #4), 7,5.** Es Orden Operativo con la **cartera más grande y accesible del país** (2,7 M de vendedores/PyMEs en ML, 49% dependen de ML; iProfesional 2026-06-27) y se vende **remoto** porque el insumo es un export de ventas/stock. Claude en Excel hace el trabajo pesado sin programar. Ruta a semi-pasivo: reposición mensual mecanizada.
2. **Diagnóstico Express a precio fijo (#1), 7.** Es la puerta de entrada que convierte todo lo demás. Modelo probado afuera (Osher: 1 día + informe en 7-10 días; Upwork ~USD 800). Los primeros 2-3 casos a cambio de testimonio con números; después cobrar.
3. **Costeo de recetas + mermas en gastronomía (#10), 7.** Dolor agudo y fechado: márgenes de 5-10% (antes 20-25%) y ~200 locales menos en Rosario (de ~1.700 a ~1.500) (La Capital 2026-07-28). Mantenimiento mensual casi mecánico (actualización de costos por facturas con Claude).
4. **SOPs con IA (#22), 7.** Entregable que todos los demás proyectos producen igual (picking, recepción, conteo, armado de paquetes); vendible solo, local y remoto; capitaliza la tesis 2026 de "capturar conocimiento tácito" (Squint, PYMNTS 2026-09-11). Commodity en Upwork → venderlo anclado al nicho ops.
5. **Back-office IA para profesionales de Higiene y Seguridad (#26), 6,5** — o **Kit 5S + auditoría por fotos (#19), 6,5** como alternativa más cercana a Orden Operativo. El #26 es la idea "no obvia": B2B2B, clientes que ya facturan mensual (mínimo FAQYA ARS 163.100/mes por empresa chica desde 2026-09-01) y cuyo cuello de botella es el papeleo; pocos clientes = poca venta. Validar con 3 profesionales antes de cualquier cosa.

**Combinación recomendada para validar (no es decisión, es hipótesis):** ofrecer un único paquete **"Orden Operativo"** = Diagnóstico Express (#1) → Stock Sano (#2) → SOPs (#22) → mantenimiento mensual (reorden + auditoría 5S por fotos, #19), con dos verticales de venta: **sellers de ML** (remoto) y **gastronomía** (local). Todo lo demás (OEE, tiempos, CMMS, ISO) queda como upsell cuando haya casos.

**Vía de cash en USD en paralelo, si se necesita:** #30 (ops manager remoto) es la forma más probable de cobrar en dólares en 1-3 meses, pero es un empleo — compite por las mismas horas.

---

## Trampas comunes de este frente

1. **"Productividad" no se vende en una industria con 40% de máquinas paradas.** UIA: MDI 36,5 (enero 2026), capacidad instalada 58-59% (mayo-junio 2026). Vender **ahorro de costo, plata parada en stock y mermas**, no "capacidad".
2. **El diagnóstico gratis es la norma del mercado.** Vendedores de software (ruteo, CMMS, solar, WMS) regalan "diagnósticos" para vender licencias. Un diagnóstico pago tiene que entregar **números en pesos** que el cliente no podía sacar solo.
3. **Credibilidad junior.** "Fractional COO", "consultor ISO", "coach Kaizen" son roles que el cliente asocia a canas. Venderse como *"ordeno tu depósito/cocina y te muestro el antes y después"*, con el caso Sporting y 2-3 casos más, no con títulos.
4. **Las fuentes de precios suelen tener conflicto de interés.** Los rangos de fractional COO los publican fractional COOs; los de ISO, consultoras ISO; los ahorros de slotting, vendedores de software de slotting. Usarlos como techo, no como mediana.
5. **El software te come el servicio por abajo.** Squint (2026-08-24), Iteros (plan gratis, 2026), Coats GSD (2026-08-19) automatizan tiempos y balanceo; Routific/Circuit hacen ruteo; Forecastly forecast a USD 49/mes. Lo defendible es **criterio + implementación en el piso + seguimiento**, no el cálculo.
6. **Commodity global en Upwork/Fiverr.** ~555 gigs de Looker Studio desde USD 10; SOPs desde USD 30. Competir por precio contra el mundo es perder; usar estas plataformas solo para casos/reseñas iniciales o con nicho muy filoso.
7. **Subsidios como modelo de negocio.** PAC/Expertos PyME están sin convocatoria verificada (2026-10-01). Bonus si aparecen; nunca la base.
8. **Matrícula y responsabilidad.** Higiene y seguridad, mediciones eléctricas, firmas de planos y algunas certificaciones requieren profesional matriculado. Trabajar *para* matriculados, no *en lugar de* ellos.
9. **Cobrar en pesos sin indexar.** Retainers en ARS se licúan; fijar en USD o con actualización mensual pactada (IPC o tipo de cambio).
10. **La IA inventa números.** Claude en Excel es potente, pero toda fórmula de reorden, costo o forecast se revisa a mano en 3-5 SKUs antes de entregarla. Un error de costeo frente a un cliente destruye la credibilidad que es todo el negocio.
11. **Confidencialidad.** Ventas, costos, videos de planta y datos de trabajadores no se suben a herramientas sin permiso explícito del cliente; poner cláusula simple en el presupuesto.
12. **Enseñar antes de hacer.** Cursos/plantillas (#32, #33) antes de tener casos = convertirse en el gurú que el propio repo critica. Primero 3-5 clientes, después producto.
13. **Clientes que abandonan la disciplina.** 5S, registro de mermas, OEE manual: el cliente deja de cargar datos a las 3-6 semanas. Diseñar todo para **mínima carga** (un Form de 30 segundos) y cobrar el seguimiento que lo sostiene.

---

## Fuentes (consultadas 2026-10-01)

**Argentina / LATAM**
- UIA, Monitor de Desempeño Industrial y capacidad instalada 2026: [Tiempo de San Juan](https://www.tiempodesanjuan.com/politica/la-industria-inicio-2026-caida-generalizada-y-el-indice-desempeno-zona-contraccion-n424599) · [Canal 26 (2026-03-05)](https://www.canal26.com/economia/2026/03/05/la-uia-informo-que-cayeron-la-produccion-y-las-ventas-en-mas-del-50-de-las-fabricas/) · [El Litoral](https://www.ellitoral.com/economia/industria-capacidadociosa-automotrices-textiles-fiel-patentamientos-coyuntura-semestre-refinacion_0_iX3xj1i6rc.html)
- Adopción de IA en PyMEs AR (CEPE-UTDT + Fundar, 2026-05-01): [Mercado](https://mercado.com.ar/ruta-digital/una-encuesta-nacional-midio-la-adopcion-de-inteligencia-artificial-en-pymes-argentinas) · Microsoft PyMEs Américas 2025: [Microsoft](https://news.microsoft.com/source/latam/noticias-de-microsoft/encuesta-pymes-2025-54-de-las-pymes-en-las-americas-usa-ia/)
- Mercado Libre en AR (2026-06-27): [iProfesional](https://www.iprofesional.com/negocios/450528-mercado-libre-cambia-logistica-argentina-inversion-record-miles-empleos) · [Nubimetrics Full](https://academia.nubimetrics.com/mercado-envios-full)
- Gastronomía Rosario (2026-07-28): [La Capital](https://www.lacapital.com.ar/negocios/gastronomia-rosarina-modo-supervivencia-menos-rentabilidad-mas-costos-y-una-receta-no-cerrar-n10270966.html)
- Honorarios H&S FAQYA (2026-07 y 2026-09): [PDF septiembre](https://quimica.org.ar/wp-content/uploads/2026/09/VALORES-MINIMOS-SUGERIDOS-A-PARTIR-DEL-01092026.pdf) · [PDF julio](https://quimica.org.ar/wp-content/uploads/2026/07/VALORES-MINIMOS-SUGERIDOS-A-PARTIR-DEL-01072026.pdf)
- Honorarios de consultoría profesional por jurisdicción (referencia contable, no ingeniería): [Contadores en Red](https://contadoresenred.com/honorarios-profesionales-cuanto-vale-la-hora-de-un-contador-publico-comparativo-por-jurisdiccion-y-encuesta/amp/)
- Programas: [Expertos PyME GCBA](https://buenosaires.gob.ar/desarrolloeconomico/ba-pyme/expertos-pyme) · [PAC (A24)](https://www.a24.com/pymes/el-gobierno-lanza-el-pac-mejorar-la-competitividad-las-pymes-n822844) · [INTI Kaizen TANGO booklet 2023](https://web2.inti.gob.ar/www/assets/uploads/files/tecnologia-de-gestion/2023/BOOKLET-2023.pdf) · [Programa provincial reactivación](https://diariojornada.com.ar/283377/magazine/provincia_convoca_a_pymes_para_el_programa_de_reactivacion_productiva)
- Energía/tarifas 2026: [HCDN](https://rest.hcdn.gob.ar/web/proyectos/292446/adjuntos/106156) · [El Economista / Grant Thornton](https://eleconomista.com.ar/energia/energia-mas-cara-decisiones-urgentes-como-bajar-costos-avanzar-transicion-renovable-argentina-n91404) · [LM Neuquén](https://mase.lmneuquen.com/economia/empresarios-alertan-que-el-tarifazo-lleva-mortandad-pymes-n1100249)
- Digitalización PyME 2026: [Develop Argentina](https://www.developargentina.com/blog/transformacion-digital-pymes-argentina-por-donde-empezar-2026) · Stock con inflación: [Base](https://base.com/es-AR/blog/stock-en-argentina/) · Calculadoras: [Hacé Cuentas](https://hacecuentas.com/calculadora-costo-receta-precio-por-porcion)
- Trabajo fractional LATAM: [Landa 2025](https://landaclub1.substack.com/p/new-report-fractional-work-and-the) · [Hire in South](https://www.hireinsouth.com/post/hire-a-latam-marketing-specialist-for-2-000-month) · [Remowork](https://remowork.life/jobs/6a7da6bf413a2a759fa984d0/e-commerce-operations-manager-remote-or-latam)

**Global — herramientas y tendencias**
- Video time study con IA: [Squint (Let's Data Science, 2026-08-24)](https://letsdatascience.com/news/squint-applies-video-ai-to-factory-workflows-d66cd756) · [Squint (PYMNTS, 2026-09-11)](https://www.pymnts.com/?p=4178078) · [Iteros](https://www.startuphub.ai/startups/iteros.md) · [Coats GSD RealMotion (2026-08-19)](https://www.imarcengineering.com/news/coats-digital-gsd-realmotion-ai-time-motion-studies) · [Khenda](https://crunchbase.com/organization/khenda)
- Process audit productizado: [Osher Digital](https://osher.com.au/help/working-with-osher-digital/what-is-a-process-audit/) · [ManyRequests](https://manyrequests.com/blog/productized-consulting-how-it-works-why-its-worth-it) · [Upwork process audit](https://www.upwork.com/services/product/consulting-hr-a-business-process-audit-to-optimize-processes-for-efficient-growth-1741212274255642624)
- Fractional COO: [Kamyar Shah](https://kamyarshah.com/fractional-coo-rates-cost-breakdown/)
- SOPs: [Upwork SOP gig](https://www.upwork.com/services/product/admin-customer-support-professional-sops-and-process-documentation-that-streamline-your-operations-2026230545925501764) · [Ciela (2026-02-25)](https://ciela.ai/blogs/ai-sop-generator-service-for-clients) · [Guidde](https://www.guidde.com/knowledge-hub/sop-writing-ai-assistance-complete-guide)
- Inventario/forecast: [Upwork FBA forecast](https://www.upwork.com/services/product/admin-customer-support-inventory-forecasting-for-amazon-fba-1747312553979592704) · [Forecastly (Novadata)](https://novadata.io/resources/best-amazon-seller-tools/forecastly) · [Udemy Claude en Excel ops](https://www.udemy.com/course/claude-ai-in-excel-for-operations-analytics/) · [Jeff Bullas](https://www.jeffbullas.com/thread/can-small-shops-use-ai-to-forecast-inventory-demand-practical-steps-for-beginners/) · [SmartScout fees 2025](https://www.smartscout.com/blog/how-to-navigate-amazons-new-fee-structure-in-2025)
- Slotting: [Optioryx 2026](https://www.optioryx.com/blog/warehouse-slotting) · [Omni Online ABC](https://omnionlinestrategies.com/blog/abc-slotting-analysis)
- Ruteo: [Toolradar Routific](https://toolradar.com/tools/routific/pricing) · [Upper Circuit vs Routific](https://www.upperinc.com/comparison/circuit-vs-routific.txt)
- 3PL: [eHub](https://ehub.com/blog/3pl-consultants) · [SKUSavvy](https://skusavvy.com/blog/how-to-find-the-right-3pl-for-your-shopify-store)
- Desperdicio de alimentos: [Verdict](https://www.verdict.co.uk/smart-bin-restaurants/) · [CB Insights Leanpath](https://www.cbinsights.com/company/leanpath) · [NewsNation](https://www.newsnationnow.com/business/tech/artificial-intelligence-technology-tracks-us-food-waste/amp/)
- Plantillas: [Flevy OEE](https://flevy.com/browse/marketplace/oee-production-dashboard-and-loss-analyst-12206) · [AME / Systems2win](https://www.ame.org/node/37203) · [Teeptrak](https://teeptrak.com/fr/?p=88127)
- Dashboards: [The Bricks (2025-10-21)](https://www.thebricks.com/resources/guide-does-looker-studio-cost-money) · [Fiverr Looker Studio](https://block.fiverr.com/gigs/looker-studio)
- CMMS: [Oxmaint 2025](https://oxmaint.com/article/best-cmms-software-comparison-2025) · [Verdantix 2025](https://www.verdantix.com/report/green-quadrant-industrial-computerized-maintenance-management-systems-cmms-2025)
- Visión artificial: [PricingSaaS Landing AI](https://pricingsaas.com/companies/landing) · [SmartDev](https://smartdev.com/fr/computer-vision-cost-manufacturing-complete-cv-system-pricing-breakdown/)
- ISO 9001: [The Core Solution](https://www.thecoresolution.com/iso-9001-certification-cost) · [9001 Simplified](https://www.9001simplified.com/learn/iso-9001-certification-cost.php)
- Process mining: [PeerSpot Celonis](https://www.peerspot.com/product_reviews/celonis-review-3876800-by-gul-ansari) · [Acceleration Economy (Logatik)](https://accelerationeconomy.com/?p=33487)
- AppSheet: [Gemini en AppSheet](https://workspace.google.com/marketplace/app/gemini_in_appsheet/1035879554174?hl=ar)
- Cursos Excel logística: [UNO Logística](https://unologistica.org/wp-content/uploads/2025/12/ID-149-PROGRAMA-Excel-avanzado-para-optimizar-.pdf) · [Educaweb](https://www.educaweb.com/curso/training-excel-avanzado-ingenieros-on-line-389734/)

### Pendientes de verificación (no se pudo por límite de búsquedas)
- Tasas de merma en retail/supermercados argentinos (para #9).
- Existencia/precios de consultores de operaciones específicos para sellers de ML (#4) y back-office para H&S (#26) — se presumen huecos, **confirmar con búsqueda y con 3-5 entrevistas**.
- Honorarios reales de consultores de ingeniería industrial en AR (Consejos Profesionales de Ingeniería provinciales).
- Precios de Guidewheel/sensores OEE para PyMEs; retainers de consultoría gastronómica en AR.

*Nada de esto es consejo financiero. Rangos de precios marcados "estimado" son juicio del investigador, no dato de mercado. Re-verificar al momento de ejecutar.*
