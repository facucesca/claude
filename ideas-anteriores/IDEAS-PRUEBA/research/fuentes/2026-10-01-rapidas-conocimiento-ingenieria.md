# Ideas rápidas (primer cobro en ≤ 7 días): monetizar conocimiento de ingeniería industrial, Excel y Claude

- **Fecha**: 2026-10-01
- **Frente**: trabajos chicos, cerrados y cobrables esta semana, basados en lo que el usuario ya sabe (ingeniería industrial, Excel, Claude/IA).
- **Perfil asumido**: argentino, no programa, usa Claude todos los días (Claude, Claude Code, Cowork, Claude en Excel), pasantía relevando un depósito (stock, picking, layout), capital < USD 300, cobra por Mercado Pago o transferencia.
- **Relación con el estudio anterior**: `research/2026-10-01-230-ideas-con-claude.md`, sección 4. Las ideas que son la **versión micro** de una ficha anterior llevan su código (ej. "micro-C2"). Las demás son nuevas.
- **Tipo de cambio de referencia**: ARS 1.535 por USD, oficial aproximado de septiembre de 2026 (Ceredi, 2026-09-09, [S4]). Los precios en ARS son de **octubre de 2026**. La inflación de agosto de 2026 fue 1,7% mensual y 33,5% interanual [S15], así que hay que actualizarlos cada mes.

---

## 0. Metodología y limitaciones

1. **Consultas**: 33 en total. Fueron 27 WebSearch, hasta que se agotó la cuota de la sesión (200/200), y 12 WebFetch sobre páginas primarias. Bing y DuckDuckGo no funcionaron: el primero devolvió resultados basura y el segundo rechazó la conexión.
2. **Bloqueos**: Superprof, Workana (listados y fichas de proyecto) y Fiverr (fichas) devolvieron **403**. Por eso los precios de esas plataformas salen de los fragmentos que muestra el buscador, no de la página. Están marcados [PARCIAL].
3. **Criterio de "primer cobro en 7 días"**: se cuenta como cobro una **seña del 50%** recibida por Mercado Pago dentro de los 7 días, aunque el trabajo se entregue después. Un "me interesa" no cuenta.
4. **Supuesto honesto sobre la probabilidad**: el usuario no tiene reseñas, portfolio ni marca. En 7 días solo se cobra por **contactos tibios** (familia, ex-compañeros, la empresa de la pasantía, comercios del barrio, grupos de la facultad). Las plataformas en frío (Fiverr/Workana) casi nunca dan un primer cobro en una semana.
5. **Score 1-10**: es un juicio que combina velocidad, probabilidad en 7 días, $/hora y puente hacia la consultoría "Orden Operativo + IA para PyMEs". No es una fórmula. Cuando $/hora y puente tiran en direcciones opuestas, se prioriza el puente: estas ideas sirven para hacer caja **y** juntar casos.
6. **Exclusiones** (ya acordadas): no se hacen exámenes, TPs ni tesis ajenos, y no se firma nada que requiera matrícula (contador, ingeniero matriculado, Higiene y Seguridad).

### Fuentes (consultadas el 2026-10-01)

| # | Fuente | Dato | Fecha del dato |
|---|---|---|---|
| S1 | [cuantomecuesta.com/ar/clases-particulares](https://cuantomecuesta.com/ar/clases-particulares/) | Estudiante universitario $15.000-40.000/h; licenciado $25.000-60.000/h; online -15%; interior -25%; grupal -50% | 2026-04 |
| S2 | [Tiempo de San Juan](https://www.tiempodesanjuan.com/economia/a-no-llevarse-materias-cuanto-cuestan-las-clases-de-apoyo-escolar-en-san-juan-pensando-en-los-proximos-examenes_1781396881/amp) | Consulta universitaria individual: $15.000-21.000; preparación de finales $190.000; plan de 12 h por $91.800 | 2026-06-16 |
| S3 | [UAI, Taller de Costos para Emprendedores 2026](https://uai.edu.ar/media/142543/taller-de-costos-para-emprendedores-2026.pdf) | 10 h virtual: matrícula $50.000 + $165.000 | 2026 (jun-jul) |
| S4 | [Diego Ceredi, precio de capacitación IA en Argentina](https://www.diegoceredi.com/blog/precio-capacitacion-ia-empresas-argentina) | Taller in-company de 8 h: ARS 3.900.000; implementación ARS 4,5-11 M; TC ~1.535 | 2026-09-09 |
| S5 | [the-decoder](https://the-decoder.com/anthropic-activates-claudes-excel-integration-for-all-pro-subscribers) / [support.claude.com](https://support.claude.com/es/articles/12650343-claude-en-excel) | Claude en Excel disponible en el plan Pro (USD 20/mes) | 2026-01-24 |
| S6 | [Premio Emprendimiento UP-Santander](https://www.palermo.edu/ingenieria/premio-emprendimiento-up-santander/) | Hasta $4.000.000 no reembolsable; **cierre 2026-10-15**; pide plan de negocios, flujo de 12 meses, presupuesto y video; el equipo debe incluir alumno o graduado UP | 2026-09-15 |
| S7 | [Concurso Emprendimiento Argentino 2026](https://argentina.gob.ar/concurso-emprendimiento-argentino) | Inscripción cerrada (2026-06-02 a 2026-07-31); instancias provinciales del 2026-08-31 al 2026-10-30 | 2026 |
| S8 | Fiverr, gigs de Gantt/MS Project (fragmento del buscador) [PARCIAL] | Rangos de hasta USD 50, 50-100, 100-200 y 400-600 | 2026-10-01 |
| S9 | Fiverr, process map/BPMN (fragmento del buscador) [PARCIAL] | USD 5-50; la mayoría arranca en USD 15-25 | 2026-10-01 |
| S10 | Fiverr, planillas de inventario (fragmento del buscador) [PARCIAL] | Gigs de ~USD 50 | 2026-10-01 |
| S11 | [Upwork, costo de freelancers de Google Sheets](https://www.upwork.com/hire/google-spreadsheet-freelancers/cost/) | USD 10-35/h | 2026 |
| S12 | Workana, proyectos "Optimización de planilla de Excel para presupuestos" (constructora de piletas) y "30 plantillas Excel con dashboards" [PARCIAL, 403] | Hay demanda de planillas a medida; no se ve el presupuesto | 2025-02-04 y 2026-02-02 |
| S13 | [Jaguar Sheet](https://jaguarsheet.com/es/blog/template-rentabilidad-mercado-libre) | Sincroniza Mercado Libre con Sheets desde ARS 12.000/mes (competidor/sustituto) | 2026 |
| S14 | Glassdoor AR, RGIS | Existe el servicio tercerizado de inventarios para retail grande en Argentina | varias |
| S15 | [iProUP, IPC de agosto](https://www.iproup.com/finanzas/71297-inflacion-agosto-dato-oficial-indec-confirma-cuanto-llego-ipc-acumulado-anual-precios-2026) | 1,7% mensual; 33,5% interanual; el IPC de septiembre sale el 2026-10-13 | 2026-09 |
| S16 | [iProfesional, Banco Nación](https://www.iprofesional.com/economia/277974-banco-central-empresa-hipotecario-Banco-Nacion-quiere-financiar-a-un-millon-de-emprendedores-cuanto-dinero-ofrece) / [Banco Provincia](https://www.iprofesional.com/finanzas/445858-banco-provincia-respalda-emprendedores-desde-18-anos-con-creditos-tasas-diferenciales) | Hay líneas activas de crédito para emprendedores en 2026 | 2026-06-27 / 2026-07-23 |
| S17 | [ADPList, guía](https://adplist.org/guides/best-mentorship-platforms) | ADPList es **gratis** (mentores voluntarios); MentorCruise cobra USD 100-450 | 2026 |
| S18 | [Clarity.fm, FAQ de expertos](https://clarity.fm/help/topics/5/expert-faqs) | Sigue operando; el experto fija su tarifa | 2026 |
| S19 | [INSPT-UTN, Seminario de Ingreso 2027](https://inspt.utn.edu.ar/wp-content/uploads/2026/05/Instructivo_Seminario_Ingreso_2027_Quimica-Informatica-Fisica-Matematica.pdf) / [UTN Santa Fe](https://www.ellitoral.com/educacion/utn-santa-fe-curso-anticipado-ingreso-2027-ingenieria-ahora-hoy_0_1kO6iKwMas.html) | Seminario de ingreso con cursada en **octubre 2026** o marzo 2027; Matemática y Física | 2026-05 |
| S20 | [Sitio Andino, Godoy Cruz](https://www.sitioandino.com.ar/departamentales/lanzan-godoy-cruz-un-curso-gratuito-excel-profesional-inteligencia-artificial-vecinos-del-departamento-n5722224) / [iProfesional, BA Emprende](https://www.iprofesional.com/management/440267-cursos-gratis-para-emprendedores-en-buenos-aires-como-anotarse-para-marketing-ia-y-mas) | Competencia **gratuita**: cursos de Excel + IA y de "agentes de IA para tu emprendimiento" que da el Estado | 2026-08-04 / 2025 |
| S21 | [Contadores en Red, honorarios](https://contadoresenred.com/honorarios-profesionales-cuanto-vale-la-hora-de-un-contador-publico-comparativo-por-jurisdiccion-y-encuesta/amp/) | Hora de contador sugerida en CABA: $21.975 / $43.950 / $61.530 (sirve de techo de referencia) | sin fecha visible [PARCIAL] |
| S22 | [Gumroad, mentoría de CV + LinkedIn](https://fioreintech.gumroad.com/l/mentoriacvlinkedin) / [Selar](https://selar.com/9w6121) | USD 499 (mentoría de 2 sesiones); USD 150 (perfil de LinkedIn) | 2026 |
| S23 | [ANB, Banco Patagonia Río Negro](https://www.anbariloche.com.ar/amp/noticias/2026/06/03/107594-banco-patagonia-abrio-la-inscripcion-para-su-programa-emprendedoras-y-emprendedores-de-rio-negro-2026) | Inscripción cerrada el 2026-06-30; final en octubre | 2026-06-03 |
| S24 | [Ecosistema Startup, San Juan](https://ecosistemastartup.com/san-juan-abre-convocatoria-para-startups-con-premio-de-5m/) | Concurso Innovación Startup: **cierra el 2026-10-05** | 2026-09 |
| S25 | Thumbtack/OC Design (EE.UU.) | Organización de garage: USD 695-895 por ~6 h (referencia de EE.UU., no de Argentina) | 2026 |
| S26 | [Ecosistema Startup, eCommerce Day](https://ecosistemastartup.com/ecommerce-day-argentina-2026-las-5-tecnologias-que-redefinen-el-retail/) | CACE/Kantar: el 71% de las empresas argentinas ya usa IA en algún proceso | 2026 |

**Vacío importante**: no se encontró ninguna tarifa argentina verificada de "planilla Excel a medida" ni de "organización de depósito en un día". Los precios de esas fichas se derivan de las horas estimadas, la hora universitaria (S1, S2) y la hora de contador como techo (S21). Están marcados [NO VERIFICADO].

---

## 1. Lista de ideas (37)

Formato por ficha: **Qué / Cliente** · **Evidencia** · **Precio y horas** · **Plan 7 días** · **Claude / Él** · **1er cobro y prob.** · **Puente** · **Riesgos** · **Score**.

### Bloque A — Planillas a medida en 48 h (remotas, se venden con un export o una charla de 20 min)

**1. Planilla de stock "mínimo viable" en 48 h** (micro-C2)
- *Qué / Cliente*: un Excel o Sheets con altas y bajas, stock actual, punto de reorden y alerta en rojo. Para ferretería, almacén, distribuidora chica, local de ropa o emprendimiento con depósito.
- *Evidencia*: Fiverr ofrece gigs de inventario de ~USD 50 [S10, PARCIAL]; en Workana hay demanda de planillas a medida [S12]. El precio local no está verificado.
- *Precio y horas*: ARS 60.000-100.000 (USD 40-65); 4-6 h.
- *Plan 7 días*: D1 arma un demo con datos ficticios (Claude en Excel). D1-2 escribe a 20 contactos tibios (familia, comercios del barrio, la empresa de la pasantía, ex-compañeros con negocio familiar) con un video de 60 s del demo. D3-4 visita 10 comercios a pie. Oferta: "en 48 h, 50% de seña, una revisión incluida".
- *Claude / Él*: Claude arma fórmulas, validaciones, formato condicional y el instructivo. Él releva el proceso (qué entra, qué sale, quién carga), define el punto de reorden y da la capacitación de 30 min.
- *1er cobro / prob.*: seña en 2-5 días; **media-alta**.
- *Puente*: **sí**. Es la puerta directa a "Stock Sano" y al Diagnóstico.
- *Riesgos*: que nadie cargue datos (la planilla muere); pedidos de "agregale facturación" (alcance que crece); comparación con apps gratis.
- **Score: 8**

**2. Cotizador/presupuestador para oficios**
- *Qué / Cliente*: una planilla que arma un presupuesto con materiales, mano de obra, margen y PDF. Para herreros, carpinteros, instaladores, piletas, durlock, imprentas.
- *Evidencia*: proyecto en Workana de una constructora de piletas pidiendo exactamente esto (2025-02-04) [S12, PARCIAL].
- *Precio y horas*: ARS 70.000-120.000; 5-7 h.
- *Plan 7 días*: buscar 15 oficios en Instagram o Google Maps de su zona más contactos personales. Mensaje: "¿Cuánto tardás en pasar un presupuesto? Te lo dejo en 5 minutos". Mostrar un demo genérico de herrería.
- *Claude / Él*: Claude hace la lógica y la plantilla de PDF. Él define el costeo de la mano de obra (horas × valor) y el margen.
- *1er cobro / prob.*: 3-6 días; **media**.
- *Puente*: **parcial** (costeo, entrada a pymes de servicios).
- *Riesgos*: precios de materiales que cambian cada mes (vender la actualización como abono); clientes que no responden mensajes.
- **Score: 7**

**3. Control de caja y gastos mensual para comercio chico**
- *Qué / Cliente*: ingresos por medio de pago (efectivo, MP, tarjeta), gastos fijos y variables, resultado del mes. Para kioscos, peluquerías, gimnasios, consultorios.
- *Evidencia*: [NO VERIFICADO]. Es un producto commodity: hay plantillas gratis por todos lados.
- *Precio y horas*: ARS 40.000-70.000; 3-4 h.
- *Plan 7 días*: igual que la #1, empaquetado como "sabé cuánto ganaste en octubre". Lo vende el mismo día que la #1, como combo.
- *Claude / Él*: Claude arma todo. Él adapta las categorías al negocio y explica cómo se carga.
- *1er cobro / prob.*: 2-5 días; **media**.
- *Puente*: **parcial** (llega al dueño, pero no es operaciones).
- *Riesgos*: cruce con el contador (aclarar que no es contabilidad ni impuestos); ticket bajo.
- **Score: 6**

**4. Costeo + precio de venta para emprendedor** (micro-C10/C12)
- *Qué / Cliente*: costo unitario por receta o producto (materia prima, merma, mano de obra, indirectos, comisión de MP/ML) y precio de venta con margen. Para emprendedores de alimentos, pastelería, textil, velas, cosmética o artesanías.
- *Evidencia*: la UAI cobra $215.000 por un **taller** de costos de 10 h para emprendedores (2026) [S3]. Hay demanda, pero el Estado ofrece cursos gratuitos de costos (Mendoza, Portal Empleo) [S20].
- *Precio y horas*: ARS 50.000-90.000 por hasta 10 productos; 3-5 h.
- *Plan 7 días*: entrar a 5 grupos de Facebook o WhatsApp de emprendedores de su ciudad y a ferias. Publicar un caso ("costeé una torta y estaba perdiendo 18%", con permiso o ficticio y aclarado). Escribir a 15 emprendedores conocidos. Oferta: "si no encontrás al menos un producto mal precio, no pagás el saldo".
- *Claude / Él*: Claude arma la planilla y calcula escenarios. Él hace la entrevista de 40 min sobre el proceso real (mermas, tiempos) y aporta el criterio de indirectos.
- *1er cobro / prob.*: 2-5 días; **media-alta** (es un dolor obvio con inflación).
- *Puente*: **sí** (el costeo es parte de Orden Operativo y sirve de caso para gastronomía).
- *Riesgos*: emprendedores con poca plata que regatean; competencia de cursos gratuitos; datos de costos incompletos.
- **Score: 8**

**5. Actualizador de lista de precios por inflación** (complemento de la #4)
- *Qué / Cliente*: una planilla que, cargando el % de aumento por proveedor o insumo, recalcula costos y lista de precios, y avisa qué productos quedaron bajo margen. Para comercios y distribuidoras con listas largas.
- *Evidencia*: inflación de 1,7% mensual y 33,5% interanual a 2026-09 [S15]. La necesidad es estructural. Precio [NO VERIFICADO].
- *Precio y horas*: ARS 40.000-80.000 + abono opcional de ARS 15.000/mes por actualización asistida; 3-4 h.
- *Plan 7 días*: ofrecerlo como upsell a cada cliente de la #1 y la #4, y a 10 comercios que trabajan con listas de proveedores (ferreterías, autopartes, librerías).
- *Claude / Él*: Claude hace las fórmulas y los formatos. Él mapea qué proveedor manda qué lista.
- *1er cobro / prob.*: 3-6 días; **media**.
- *Puente*: **sí** (gestión de compras y márgenes).
- *Riesgos*: listas de proveedores en PDF desordenados (consume horas); si la inflación baja, el dolor también.
- **Score: 7**

**6. Planilla de turnos, horas y francos (sin liquidar sueldos)**
- *Qué / Cliente*: grilla de turnos, horas trabajadas, extras y francos, que se exporta para el contador. Para gastronomía, comercios con 3-15 empleados, gimnasios.
- *Evidencia*: [NO VERIFICADO].
- *Precio y horas*: ARS 50.000-80.000; 4 h.
- *Plan 7 días*: 10 contactos de gastronomía y comercio. Se ofrece junto con la #3.
- *Claude / Él*: Claude arma la planilla. Él la adapta al convenio con lo que le pase el contador del cliente (**él no interpreta el convenio**).
- *1er cobro / prob.*: 4-7 días; **media-baja**.
- *Puente*: **parcial**.
- *Riesgos*: zona laboral y legal, que es terreno del contador (no liquidar sueldos ni opinar de convenios); datos personales de empleados.
- **Score: 5**

**7. Plan de producción semanal para taller o fábrica chica** (MRP light)
- *Qué / Cliente*: con los pedidos de la semana calcula qué producir, qué insumos comprar y la carga por día. Para fábrica de pastas o viandas, taller textil, carpintería, cervecería.
- *Evidencia*: [NO VERIFICADO].
- *Precio y horas*: ARS 100.000-180.000; 8-10 h (incluye 1 visita).
- *Plan 7 días*: 10 contactos de la pasantía, el entorno de la facultad y proveedores de su ex-empresa. Llamar en vez de escribir. Oferta: "en una visita y 72 h, sabés qué producir el lunes".
- *Claude / Él*: Claude arma la estructura BOM → necesidades. Él releva recetas, tiempos y capacidades: **es ingeniería industrial pura**.
- *1er cobro / prob.*: 5-7 días; **baja-media** (ciclo de venta más largo).
- *Puente*: **sí** (es el núcleo de Orden Operativo).
- *Riesgos*: alcance difuso; el dueño no tiene datos de tiempos.
- **Score: 6,5**

**8. "Rescate de planilla": arreglar el Excel que ya usan**
- *Qué / Cliente*: el negocio ya tiene un Excel roto, lento, con fórmulas que nadie entiende o con "#REF!". Él lo diagnostica, lo ordena, lo documenta y deja una hoja de instrucciones. Para cualquier pyme o profesional.
- *Evidencia*: en Workana aparece demanda de "optimización de planilla" [S12, PARCIAL]. Upwork paga USD 10-35/h por Google Sheets [S11].
- *Precio y horas*: precio fijo de ARS 30.000-60.000 por planilla chica; 2-3 h.
- *Plan 7 días*: post en LinkedIn y en sus estados de WhatsApp: "Mandame la planilla que te da dolores de cabeza; si en 15 min no te digo qué le pasa, no me debés nada". Escribir a 25 contactos. Es el producto **más fácil de decir que sí**.
- *Claude / Él*: Claude en Excel lee el libro, explica las dependencias y propone correcciones (es justo para lo que está hecho, S5). Él valida que el resultado tenga sentido para el negocio.
- *1er cobro / prob.*: 1-4 días; **alta**.
- *Puente*: **sí** (cada planilla rota muestra un proceso roto; abre la conversación del Diagnóstico).
- *Riesgos*: archivos con datos sensibles (pedir copia anonimizada y revisar la configuración de privacidad del plan de Claude); ticket bajo.
- **Score: 8,5**

**9. Reporte ABC "qué productos te dan plata"** (one-shot, micro-C2)
- *Qué / Cliente*: con un export de ventas del sistema de caja, Tiendanube o ML, entrega un PDF y un Excel con ABC por facturación y margen, productos muertos y sugerencias de compra. Para comercios con 200+ SKUs.
- *Evidencia*: [NO VERIFICADO] en Argentina. Las herramientas pagas para ML (Jaguar Sheet, ARS 12.000/mes) muestran que hay disposición a pagar por análisis de datos [S13].
- *Precio y horas*: ARS 60.000-100.000; 3-4 h.
- *Plan 7 días*: 20 contactos tibios con comercio y vendedores de ML del entorno. Oferta: "me pasás el Excel de ventas de 6 meses y en 48 h te digo qué 20% te deja el 80%".
- *Claude / Él*: Claude hace el análisis y los gráficos. Él lo interpreta con criterio de stock (cobertura, quiebres) y lo explica en una llamada de 30 min.
- *1er cobro / prob.*: 2-5 días; **media**.
- *Puente*: **sí** (es el entregable "gancho" de Stock Sano).
- *Riesgos*: exports sucios; clientes que no saben exportar (dar una guía paso a paso).
- **Score: 8**

**10. Calculadora de rentabilidad por publicación para vendedores de ML** (micro-C4)
- *Qué / Cliente*: precio, comisión por categoría, envío, cuotas, costo e impuestos → margen real por publicación. Para vendedores chicos de Mercado Libre.
- *Evidencia*: existen calculadoras gratuitas y Jaguar Sheet cobra un abono [S13], así que el producto genérico está saturado. El valor está en hacerla a medida con el costo real.
- *Precio y horas*: ARS 40.000-70.000; 3 h.
- *Plan 7 días*: grupos de vendedores de ML en Facebook o WhatsApp más conocidos.
- *Claude / Él*: Claude hace la lógica. Él verifica las comisiones vigentes de ML.
- *1er cobro / prob.*: 3-7 días; **media-baja**.
- *Puente*: **parcial** (puerta a "Ops para vendedores ML").
- *Riesgos*: ML cambia comisiones y la planilla queda vieja; competencia gratuita.
- **Score: 5,5**

**11. Control de vencimientos y FIFO para almacén, dietética o farmacia** (micro-C9)
- *Qué / Cliente*: alerta de vencimientos a 30, 15 y 7 días, rotación y mermas. Para dietéticas, almacenes, fiambrerías, veterinarias.
- *Evidencia*: [NO VERIFICADO].
- *Precio y horas*: ARS 50.000-80.000; 4 h.
- *Plan 7 días*: visita a pie a 10 comercios del rubro alimentos. La oferta se apoya en la merma: "¿cuánto tiraste el mes pasado?".
- *Claude / Él*: Claude arma la planilla. Él define la rutina de carga y el layout de góndola o depósito para FIFO.
- *1er cobro / prob.*: 4-7 días; **media-baja**.
- *Puente*: **sí**.
- *Riesgos*: carga manual por lote es pesada y la abandonan.
- **Score: 6**

**12. Tablero simple de ventas y operación** (micro-C24)
- *Qué / Cliente*: una hoja-tablero (Excel o Looker Studio) con 5-8 KPIs que se actualiza pegando el export semanal. Para pymes que ya tienen datos pero no los miran.
- *Evidencia*: commodity en Fiverr (ver estudio anterior, C24). Local [NO VERIFICADO].
- *Precio y horas*: ARS 80.000-150.000; 5-8 h.
- *Plan 7 días*: se vende como upsell de la #8 y la #9; no conviene salir a venderlo en frío.
- *Claude / Él*: Claude hace el armado. Él elige los KPIs que importan (merece criterio de ingeniería).
- *1er cobro / prob.*: 5-7 días; **baja-media**.
- *Puente*: **sí**.
- *Riesgos*: "lindo pero nadie lo abre"; atarlo a una reunión semanal.
- **Score: 6**

### Bloque B — Servicios presenciales de 1 día (ingeniería industrial "en el piso")

**13. Relevamiento express de 1 día con informe en 48 h** (micro-C1)
- *Qué / Cliente*: una mañana en el depósito o negocio (flujo, stock, layout, desperdicios). Entrega un informe de 5-8 páginas con 10 mejoras priorizadas y fotos. Para pyme de 5-50 personas, distribuidora, depósito, taller.
- *Evidencia*: [NO VERIFICADO] en Argentina. La versión de 1-2 meses (C1) tenía referencias de Upwork de ~USD 800.
- *Precio y horas*: ARS 150.000-250.000 (USD 100-160) **precio de lanzamiento por caso**; 4 h en el lugar + 4-6 h de informe.
- *Plan 7 días*: D1 arma un modelo de informe con un caso ficticio. D1-3 llama o escribe a la empresa de la pasantía (¿otra sede? ¿proveedores o clientes de ellos?), a 10 dueños del entorno familiar y a 5 contactos de LinkedIn. Oferta: "precio de lanzamiento a cambio de testimonio y permiso para usarlo como caso anónimo".
- *Claude / Él*: Claude convierte notas, fotos y audios en el informe, ayuda a priorizar con matriz impacto/esfuerzo y genera los gráficos. Él hace la observación, las preguntas y el criterio.
- *1er cobro / prob.*: 5-7 días; **media-baja** (hace falta confianza para que entres a la empresa).
- *Puente*: **sí, máximo** (es literalmente el producto de entrada a la consultora).
- *Riesgos*: regalarlo de más por ansiedad; prometer ahorros que no puede medir.
- **Score: 7,5**

**14. Conteo de inventario físico como servicio** (cierre de mes o de ejercicio)
- *Qué / Cliente*: planificar y ejecutar un conteo en un día (zonificación, planillas o celular, doble conteo ciego en ítems A) y entregar diferencias contra el sistema conciliadas en Excel. Para comercios y pymes con stock que cierran al 31/12, y para contadores que necesitan el inventario para el balance.
- *Evidencia*: el servicio tercerizado existe para retail grande (RGIS en Argentina [S14]). El cierre al 31/12 exige toma física. Precio pyme [NO VERIFICADO].
- *Precio y horas*: ARS 150.000-300.000 por jornada (él + 1-2 ayudantes pagos por hora); 6-10 h.
- *Plan 7 días*: escribir a 10 **contadores** del entorno (son los que sufren el inventario de cierre) y a comercios con stock. En los primeros 7 días el objetivo es **cerrar la seña** de un conteo de fin de octubre o de diciembre.
- *Claude / Él*: Claude arma el plan de conteo, las planillas y la conciliación. Él organiza en el lugar.
- *1er cobro / prob.*: seña en 5-7 días; **baja-media** (la temporada fuerte es diciembre).
- *Puente*: **sí** (después del conteo viene el "¿por qué no coincide?").
- *Riesgos*: responsabilidad sobre la cifra (aclarar que no certifica: el que firma el balance es el contador); necesita ayudantes; mal momento de calendario hasta diciembre.
- **Score: 6,5** (sube a 8 en noviembre-diciembre)

**15. Ordenar un depósito, trastienda o garage en 1 día** (micro-C3 / C19, "5S express")
- *Qué / Cliente*: clasificar, descartar, zonificar, rotular y dejar un plano simple con fotos de antes y después. Para trastiendas de comercio, depósitos chicos, talleres y garages de emprendedores que venden online.
- *Evidencia*: en EE.UU. la organización de garage cuesta USD 695-895 por ~6 h [S25] (referencia extranjera, no transferible). Argentina [NO VERIFICADO].
- *Precio y horas*: ARS 120.000-220.000 por jornada (+ insumos a cargo del cliente); 6-8 h + 1 h de informe.
- *Plan 7 días*: 15 contactos tibios de emprendedores con stock en casa o local. Publicar en estados y grupos de barrio. Las fotos de antes y después son el marketing para la semana siguiente.
- *Claude / Él*: Claude hace el plan de zonificación, las etiquetas y el informe. Él hace trabajo físico y criterio de layout (ABC por rotación cerca de la salida).
- *1er cobro / prob.*: 3-7 días; **media**.
- *Puente*: **sí** (5S y layout son parte de Orden Operativo).
- *Riesgos*: se confunde con "personal organizer" doméstico, que paga menos; es trabajo físico.
- **Score: 7**

**16. Layout de local comercial o gastronómico** (plano + propuesta)
- *Qué / Cliente*: un plano simple (draw.io o SketchUp Free) con la circulación y la ubicación de puestos, góndolas o heladeras, más una justificación. Para locales que abren o se reforman.
- *Evidencia*: [NO VERIFICADO].
- *Precio y horas*: ARS 80.000-150.000; 5-6 h.
- *Plan 7 días*: contactar a 5 arquitectos o maestros mayores de obra (como subcontratado) y a 10 comerciantes que estén abriendo (carteles de "próxima apertura").
- *Claude / Él*: Claude ordena el análisis de flujos y redacta la propuesta. Él mide y dibuja.
- *1er cobro / prob.*: 5-7 días; **baja**.
- *Puente*: **parcial**.
- *Riesgos*: pisa terreno de arquitectos (no presentar planos municipales ni firmar); bajo volumen.
- **Score: 5**

### Bloque C — Documentación técnica a precio fijo

**17. Manual o SOP de un puesto en 48 h** (micro-C22)
- *Qué / Cliente*: un procedimiento de un puesto (cajero, repositor, armado de pedidos, apertura y cierre) con pasos, fotos, checklist y errores típicos. Para pyme que incorpora gente o franquicia chica.
- *Evidencia*: entregable transversal (C22). Precio local [NO VERIFICADO].
- *Precio y horas*: ARS 80.000-140.000 por puesto; 4-6 h (1 h de entrevista o filmación + redacción).
- *Plan 7 días*: 15 contactos de comercio y gastronomía. Oferta: "grabo 30 min a tu mejor empleado haciendo la tarea y en 48 h tenés el manual para el próximo que entre".
- *Claude / Él*: Claude transcribe el audio o video y redacta el manual. Él observa y detecta pasos implícitos y riesgos.
- *1er cobro / prob.*: 4-7 días; **media**.
- *Puente*: **sí**.
- *Riesgos*: el dueño no lo ve urgente hasta que alguien renuncia; mejor venderlo junto a la #13.
- **Score: 7**

**18. Diagramas de procesos (BPMN) para pyme o consultor ISO**
- *Qué / Cliente*: 3-5 procesos diagramados en Bizagi o draw.io con su descripción. Para pyme que se va a certificar o **consultores ISO** que necesitan mano de obra.
- *Evidencia*: en Fiverr, mapas de procesos a USD 5-50, la mayoría USD 15-25 [S9, PARCIAL]: **muy comoditizado**. El valor está en el relevamiento local.
- *Precio y horas*: ARS 60.000-120.000 por paquete de 3-5 procesos; 5-8 h.
- *Plan 7 días*: escribir a 10 consultores ISO o de calidad en LinkedIn de su provincia ofreciéndose como subcontratado. Muestra: un BPMN de picking de su pasantía (anonimizado).
- *Claude / Él*: Claude genera la descripción y un primer diagrama a partir de texto. Él releva y valida con BPMN correcto.
- *1er cobro / prob.*: 5-7 días; **baja-media**.
- *Puente*: **parcial**.
- *Riesgos*: precio de Fiverr como ancla; dependencia del consultor.
- **Score: 5,5**

**19. Cronograma de obra o proyecto (Gantt) para contratistas y estudios**
- *Qué / Cliente*: Gantt en Excel o ProjectLibre con camino crítico, hitos y curva de inversión. Para maestros mayores de obra, arquitectos chicos, contratistas que presentan a un cliente o a un banco, organizadores de eventos.
- *Evidencia*: en Fiverr hay gigs de Gantt de hasta USD 50, 50-100 y 100-200, con premium de USD 400-600 [S8, PARCIAL].
- *Precio y horas*: ARS 60.000-120.000; 3-6 h.
- *Plan 7 días*: 10 contactos de arquitectura y construcción (ex-compañeros de civil o arquitectura, corralones, familia). Muestra: Gantt de una refacción de baño.
- *Claude / Él*: Claude hace la estructura de tareas (WBS), dependencias y formato. Él valida duraciones con el contratista.
- *1er cobro / prob.*: 4-7 días; **media-baja**.
- *Puente*: **parcial**.
- *Riesgos*: el contratista no lo valora; duraciones inventadas.
- **Score: 5,5**

**20. Presentación técnica o comercial de una pyme o profesional**
- *Qué / Cliente*: una presentación de 10-15 slides (propuesta comercial, informe para socios, pitch a banco) a partir de notas o un audio. Para pymes, profesionales, estudiantes de posgrado (solo diseño y estructura, **no contenido académico evaluable**).
- *Evidencia*: [NO VERIFICADO]. Es un servicio muy ofrecido.
- *Precio y horas*: ARS 40.000-80.000; 2-4 h.
- *Plan 7 días*: contactos tibios más un post en LinkedIn.
- *Claude / Él*: Claude genera estructura, texto y PPT (skill pptx o Cowork). Él define el mensaje y revisa.
- *1er cobro / prob.*: 2-5 días; **media**.
- *Puente*: **no o parcial**.
- *Riesgos*: se comoditiza; idas y vueltas de diseño.
- **Score: 5,5**

### Bloque D — Finanzas para emprendedores (sin firmar como contador)

**21. Carpeta para pedir crédito: flujo de fondos y proyección** (sin firma)
- *Qué / Cliente*: flujo de fondos de 12-24 meses, cuadro de usos y fuentes, escenarios y una nota del proyecto. Para emprendedores que van a Banco Nación, Banco Provincia, líneas para mujeres o fondos municipales.
- *Evidencia*: en 2026 hay líneas activas para emprendedores (Banco Nación, Banco Provincia) [S16]. Los requisitos documentales concretos [NO VERIFICADOS].
- *Precio y horas*: ARS 80.000-150.000; 5-8 h.
- *Plan 7 días*: 10 emprendedores conocidos más grupos de emprendedores; también ofrecerse a **contadores** como armador de la proyección (el contador firma lo que haga falta).
- *Claude / Él*: Claude arma el modelo y redacta. Él hace la entrevista y la coherencia de supuestos (ventas, costos, capacidad).
- *1er cobro / prob.*: 4-7 días; **media-baja**.
- *Puente*: **parcial**.
- *Riesgos*: **no firmar ni certificar estados contables**; responsabilidad si el crédito no sale (cobrar por el trabajo, no por el resultado).
- **Score: 6**

**22. Plan de negocios exprés para concursos con cierre en octubre de 2026** (micro-C31)
- *Qué / Cliente*: plan de negocios breve, presupuesto de uso de fondos, flujo de 12 meses y guion del video. Para emprendedores que se presentan a convocatorias abiertas.
- *Evidencia*: **Premio UP-Santander**: hasta $4.000.000, cierra el **2026-10-15**, pide justo plan de negocios, flujo de 12 meses, presupuesto, plan de marketing y video, pero el equipo debe incluir un alumno o graduado de la UP [S6]. **San Juan Startup** cierra el 2026-10-05 [S24], muy encima. Emprendimiento Argentino y Río Negro ya cerraron la inscripción [S7, S23].
- *Precio y horas*: ARS 120.000-220.000 (o fijo + bonus si gana; **nunca solo a éxito**); 8-12 h.
- *Plan 7 días*: D1 mensaje a centros de emprendedores o incubadoras de universidades de su zona y a grupos de la UP (LinkedIn: "alumnos UP emprendedores"). Oferta: "llegás al cierre del 15/10 con la carpeta completa".
- *Claude / Él*: Claude redacta, arma el flujo y el guion. Él define supuestos y revisa coherencia financiera y operativa.
- *1er cobro / prob.*: 3-7 días; **media-baja** (depende de encontrar a alguien que ya quiera presentarse).
- *Puente*: **parcial**.
- *Riesgos*: ventanas cortas; algunas bases pueden prohibir terceros redactores (leer las bases); calidad de la idea del cliente.
- **Score: 5,5**

**23. Estudio de factibilidad simple: "¿me conviene abrir X?"**
- *Qué / Cliente*: punto de equilibrio, inversión, recupero, 3 escenarios y riesgos operativos. Para quien quiere abrir un local, comprar una máquina o sumar una línea de producto.
- *Evidencia*: [NO VERIFICADO].
- *Precio y horas*: ARS 100.000-180.000; 6-8 h.
- *Plan 7 días*: contactos tibios. Oferta: "antes de poner USD 10.000, gastá ARS 120.000 en saber si cierra".
- *Claude / Él*: Claude modela y redacta. Él releva capacidad, costos y ritmo de ventas razonable.
- *1er cobro / prob.*: 5-7 días; **baja-media**.
- *Puente*: **parcial**.
- *Riesgos*: el cliente quiere que le digan que sí; no hacer proyecciones de mercado inventadas.
- **Score: 5,5**

### Bloque E — Enseñar: Claude, Excel e ingeniería

**24. Sesión 1:1 "Claude en Excel para tu negocio" (2 h, sobre SU planilla)** (micro-A10 / A38)
- *Qué / Cliente*: sesión con el dueño o administrativo sobre su propia planilla: instalar Claude en Excel, 5 tareas útiles (consultas, limpiar datos, armar resumen, detectar errores) y un "machete" PDF. Para dueños de pyme, administrativos, contadores chicos.
- *Evidencia*: Claude en Excel está disponible en el plan Pro (USD 20/mes) desde el 2026-01-24 [S5]. El 71% de las empresas argentinas ya usa IA en algún proceso [S26]. Ceredi cobra ARS 3,9 M por un día in-company [S4], lo que muestra el techo B2B. El 1:1 barato está [NO VERIFICADO].
- *Precio y horas*: ARS 40.000-70.000 por sesión de 2 h (+ el cliente paga su plan Pro); 3 h con preparación.
- *Plan 7 días*: post en LinkedIn con un video de 90 s ("le pedí a Claude que me explique esta planilla de stock"). Mensaje a 30 contactos (dueños, contadores, administrativos). Oferta: "si en la sesión no te ahorro 1 hora por semana, no pagás".
- *Claude / Él*: Claude genera el machete y los ejemplos. Él enseña con el caso real del cliente.
- *1er cobro / prob.*: 2-5 días; **media-alta**.
- *Puente*: **sí** (entra al negocio por la planilla y ve los procesos).
- *Riesgos*: el cliente no quiere pagar USD 20/mes; requiere Excel de escritorio o 365 compatible; la herramienta cambia rápido.
- **Score: 8**

**25. Taller grupal de 2 h "Claude/IA para tu negocio" en coworking, cámara o centro comercial** (micro-A1 / A21)
- *Qué / Cliente*: taller práctico con casos de comercio (presupuestos, respuestas a clientes, planillas). Para comerciantes y emprendedores de una cámara local, coworking o asociación.
- *Evidencia*: hay competencia **gratuita** del Estado (Godoy Cruz, Excel + IA, 2026-08-04; BA Emprende, "agentes de IA", 2025) [S20]. Taller IA en Colombia: cohorte de 4 sábados a ~COP 460-600 mil con 9 inscriptos [luma.com, 2026-07]. El precio por entrada en Argentina está [NO VERIFICADO].
- *Precio y horas*: ARS 15.000-25.000 por persona (objetivo de 10-15 personas) o fijo de ARS 200.000-350.000 a la institución; 6 h con preparación.
- *Plan 7 días*: D1-2 llama a 3 coworkings, 2 cámaras de comercio y 1 centro de estudiantes con propuesta de revenue share 70/30. D3-7 difusión. **El cobro realista es por preventa**, y el taller cae en la semana 2.
- *Claude / Él*: Claude hace material, ejercicios y certificado. Él da el taller (ensayado).
- *1er cobro / prob.*: preventa en 5-7 días; **baja-media**.
- *Puente*: **sí** (cada asistente es un lead para Diagnóstico).
- *Riesgos*: competir con talleres gratis; poca gente; miedo escénico; la institución tarda en decidir.
- **Score: 6**

**26. Taller in-company de 2 h para el equipo de una pyme conocida** (micro-A1)
- *Qué / Cliente*: lo mismo que la #25, cerrado para 5-15 empleados de una empresa (la de la pasantía, la de un familiar o un cliente de la #24).
- *Evidencia*: el techo de mercado es ARS 3,9 M por 8 h [S4]. Una versión de 2 h a ARS 300.000-500.000 queda 8-13 veces más barata por hora que ese techo.
- *Precio y horas*: ARS 300.000-500.000; 8 h con preparación.
- *Plan 7 días*: 5 llamados a dueños o gerentes conocidos.
- *Claude / Él*: igual que la #25, con casos de esa empresa.
- *1er cobro / prob.*: 5-7 días (seña); **baja-media**.
- *Puente*: **sí**.
- *Riesgos*: credibilidad de un junior frente al equipo; prometer de más.
- **Score: 6,5**

**27. Tutoría 1:1 de Investigación Operativa, Estadística, Costos y Simulación para estudiantes de ingeniería** (micro-A36, enfocada en finales)
- *Qué / Cliente*: clases para **aprender** (no resolver TPs ni exámenes) en la temporada de finales de noviembre-diciembre. Para estudiantes de ingeniería industrial y otras ingenierías.
- *Evidencia*: estudiante universitario como profesor: $15.000-40.000/h (2026-04) [S1]. En San Juan, consulta universitaria de $15.000-21.000 y preparación de finales de $190.000 (2026-06-16) [S2]. Matemática y física son las más pedidas.
- *Precio y horas*: ARS 15.000-25.000/h; pack de finales de 4 clases a ARS 70.000; 1 h por clase + preparación con Claude.
- *Plan 7 días*: D1 publica en grupos de WhatsApp o Telegram de su carrera y en el centro de estudiantes; mensaje a 20 conocidos de años inferiores. Primera clase de 20 min gratis para diagnosticar.
- *Claude / Él*: Claude genera ejercicios graduados, explicaciones alternativas y simulacros **propios**. Él enseña y corrige razonamiento.
- *1er cobro / prob.*: 1-4 días; **alta**.
- *Puente*: **no** (es caja, no consultoría), aunque arma red de futuros ingenieros.
- *Riesgos*: $/hora bajo; tentación de "resolveme el TP" (decir que no por escrito); estacionalidad.
- **Score: 7**

**28. Clases de Excel aplicado (estudiantes y profesionales)**
- *Qué / Cliente*: Excel de tablas dinámicas a funciones y modelado, con Claude como asistente. Para estudiantes, administrativos y quien busca empleo.
- *Evidencia*: el mismo rango de hora que S1. Hay cursos de Excel de Coderhouse desde ~USD 100 y competencia gratuita del Estado [S20].
- *Precio y horas*: ARS 15.000-25.000/h.
- *Plan 7 días*: el mismo canal que la #27, más el entorno familiar y LinkedIn.
- *Claude / Él*: Claude arma ejercicios con datos realistas. Él enseña.
- *1er cobro / prob.*: 2-5 días; **media-alta**.
- *Puente*: **parcial** (algún alumno puede ser dueño de pyme).
- *Riesgos*: mucha oferta; ticket bajo.
- **Score: 6,5**

**29. Apoyo para el Seminario de Ingreso a Ingeniería 2027 (Matemática y Física)**
- *Qué / Cliente*: clases grupales chicas (3-5 personas) para el ingreso. Para ingresantes a UTN u otras universidades nacionales con cursada en **octubre de 2026**.
- *Evidencia*: el seminario de ingreso 2027 se cursa en octubre de 2026 o marzo de 2027 (UTN INSPT, UTN Santa Fe) [S19]. La preparación del CBC UBA cuesta $1-4 M por 3 meses [S1].
- *Precio y horas*: ARS 10.000-15.000 por persona por clase grupal, o ARS 15.000-20.000/h individual.
- *Plan 7 días*: grupos de padres y ingresantes de su ciudad, colegios técnicos donde tenga conocidos, Facebook Marketplace o servicios locales.
- *Claude / Él*: Claude genera guías y simulacros propios. Él enseña.
- *1er cobro / prob.*: 2-5 días; **media-alta** (la temporada arranca justo ahora).
- *Puente*: **no**.
- *Riesgos*: menores de edad (consentimiento de padres; clases online o en lugar público); ventana estacional.
- **Score: 6,5**

**30. Taller grupal "Excel + Claude para estudiantes de ingeniería" en el centro de estudiantes**
- *Qué / Cliente*: 2 h con casos de IO y estadística (Solver, regresión, simulación Montecarlo), con IA como tutor y **no como copia**. Para estudiantes de 2º a 5º año.
- *Evidencia*: estudio anterior, A39 (demanda de Power BI + IA). Precio grupal [NO VERIFICADO]: grupal = -50% sobre la tarifa individual [S1].
- *Precio y horas*: ARS 8.000-15.000 por persona; 10-25 personas; 6 h con preparación.
- *Plan 7 días*: proponérselo al centro de estudiantes y a los ayudantes de cátedra; difundir por grupos de cursada; preventa por MP.
- *Claude / Él*: Claude hace material y datasets. Él da el taller.
- *1er cobro / prob.*: preventa en 5-7 días; **media**.
- *Puente*: **parcial** (red, contenido para LinkedIn, ensayo para los talleres a pymes).
- *Riesgos*: el centro de estudiantes no quiere actividades pagas; poca convocatoria en época de parciales.
- **Score: 6**

**31. Revisión de CV y LinkedIn para estudiantes y jóvenes ingenieros**
- *Qué / Cliente*: revisión asincrónica con Claude más 30 min de llamada; CV ATS-friendly. Para estudiantes avanzados de ingeniería que buscan pasantía.
- *Evidencia*: el extremo alto es USD 499 (mentoría de CV + LinkedIn) y USD 150 (perfil de LinkedIn) [S22], pero el bolsillo estudiantil argentino es mucho menor [NO VERIFICADO].
- *Precio y horas*: ARS 15.000-30.000; 1-1,5 h.
- *Plan 7 días*: grupos de la carrera más LinkedIn. Él mismo es "par" que consiguió pasantía.
- *Claude / Él*: Claude hace el borrador y el chequeo. Él aporta el criterio de qué buscan los reclutadores de industria y logística.
- *1er cobro / prob.*: 2-4 días; **media**.
- *Puente*: **no**.
- *Riesgos*: ticket mínimo; poca autoridad (no es reclutador).
- **Score: 4,5**

**32. "Office hours" pagas: consultá tu planilla o tu proceso (30 min)**
- *Qué / Cliente*: link de Calendly o turno manual más cobro previo por MP, 30 min por videollamada sobre un problema puntual. Para dueños y administrativos.
- *Evidencia*: [NO VERIFICADO]. Funciona solo con audiencia previa.
- *Precio y horas*: ARS 15.000-20.000 por 30 min.
- *Plan 7 días*: lo ofrece en cada post o mensaje como "escalón bajo" para quien no compra la #8 o la #24.
- *Claude / Él*: Claude prepara antes y resume después. Él da la llamada.
- *1er cobro / prob.*: 3-7 días; **baja-media**.
- *Puente*: **sí** (embudo).
- *Riesgos*: nadie compra sin confianza previa; funciona más como vía de entrada que como fuente de ingreso.
- **Score: 5**

### Bloque F — Subcontratación (que otro ya tiene los clientes)

**33. Asistente de Excel y operaciones para un estudio contable** (por horas)
- *Qué / Cliente*: conciliaciones, armado de planillas de clientes, inventario de bienes de uso y carga ordenada, sin firmar. Para estudios contables de 1-5 personas en temporada de cierre (octubre-diciembre).
- *Evidencia*: la hora sugerida de contador en CABA va de $21.975 a $61.530 [S21, PARCIAL], así que un asistente a $10.000-15.000/h les deja margen. Demanda [NO VERIFICADA].
- *Precio y horas*: ARS 10.000-15.000/h o por tarea cerrada; 10-20 h/semana.
- *Plan 7 días*: escribir a 10 contadores del entorno (el de su familia primero). Oferta: "te armo la planilla que hoy hacés a mano, cobro por tarea".
- *Claude / Él*: Claude automatiza las planillas. Él tiene el criterio de orden y verificación.
- *1er cobro / prob.*: 4-7 días (si pagan por tarea); **media**.
- *Puente*: **sí** (los contadores son el **mejor canal** de pymes para Orden Operativo; ver A2 y la #14).
- *Riesgos*: datos fiscales sensibles; trabajo a destajo de bajo valor; pagos a 30 días.
- **Score: 7**

**34. Mano de obra de relevamiento para estudios de Higiene y Seguridad** (micro-C26)
- *Qué / Cliente*: relevamiento con checklist y fotos, carga de mediciones y armado del borrador del informe en Word con Claude. **El matriculado firma.** Para licenciados o técnicos en HyS con muchas empresas cliente.
- *Evidencia*: hay búsquedas de consultores HyS monotributistas en Buenos Aires [búsqueda del 2026-10-01, PARCIAL]. Su cuello de botella es el papeleo (C26). La tarifa del asistente está [NO VERIFICADA].
- *Precio y horas*: ARS 10.000-15.000/h o ARS 30.000-60.000 por informe borrador.
- *Plan 7 días*: LinkedIn con 15 profesionales de HyS de su zona más el entorno de la facultad.
- *Claude / Él*: Claude convierte notas y fotos en un informe estructurado. Él releva y ordena la evidencia.
- *1er cobro / prob.*: 5-7 días; **baja-media**.
- *Puente*: **parcial** (entra a muchas pymes como acompañante).
- *Riesgos*: **nunca firmar ni opinar como profesional de HyS**; responsabilidad civil si un dato está mal; ART.
- **Score: 5,5**

**35. Subcontratado de un consultor o agencia de IA/automatización que ya tiene clientes**
- *Qué / Cliente*: ejecutar partes "de ingeniería" (relevar procesos, armar planillas, documentar SOPs) para un consultor que vende y no tiene tiempo. Para consultores pyme, agencias de automatización e implementadores de ERP o Tiendanube.
- *Evidencia*: [NO VERIFICADO]. Es una práctica común del sector servicios.
- *Precio y horas*: ARS 10.000-20.000/h o por entregable.
- *Plan 7 días*: buscar en LinkedIn a 20 consultores e implementadores argentinos que publiquen sobre IA para pymes; mensaje corto con una muestra (BPMN o planilla de stock).
- *Claude / Él*: lo mismo que su servicio propio.
- *1er cobro / prob.*: 5-7 días; **baja-media**.
- *Puente*: **sí** (aprende cómo vende un consultor y junta casos, aunque sean de otro).
- *Riesgos*: confidencialidad o no-competencia; precio bajo; no puede mostrar los casos.
- **Score: 6,5**

**36. Gigs de Excel y Sheets en Workana o Fiverr** (se superpone con freelance)
- *Qué / Cliente*: planillas e informes para clientes LATAM o globales.
- *Evidencia*: Google Sheets en Upwork: USD 10-35/h [S11]; Fiverr de inventario ~USD 50 [S10]; demanda en Workana [S12]. Plataformas bloqueadas a la consulta directa.
- *Precio y horas*: USD 30-80 por gig; 2-5 h.
- *Plan 7 días*: crear el perfil con 3 muestras de las ideas 1, 4 y 9, y mandar 30-50 propuestas en Workana.
- *Claude / Él*: Claude hace casi todo el trabajo técnico. Él atiende al cliente.
- *1er cobro / prob.*: 7-30 días (cold start, sin reseñas, más retención de pago de la plataforma); **baja**.
- *Puente*: **no o parcial** (clientes de otros países, no pymes locales).
- *Riesgos*: guerra de precios con India, Pakistán y Kenia; comisiones; Payoneer.
- **Score: 4**

**37. Mentorías en plataformas (ADPList, Clarity.fm, MentorCruise)**: **descartada para 7 días**
- *Evidencia*: **ADPList es gratis** (mentores voluntarios, sin tier pago) [S17]. Clarity.fm sigue operando con tarifa libre [S18], pero la demanda llega a expertos con trayectoria. MentorCruise cobra USD 100-450 por sesión [S17] y es para seniors.
- *Por qué no*: un estudiante o junior sin marca no recibe reservas en una semana. ADPList solo sirve para "construir reputación" gratis, y eso es otro objetivo.
- *Puente*: **no**.
- **Score: 2**

---

## 2. Top 5 para cobrar esta semana

| # | Idea | Por qué entra al Top 5 |
|---|---|---|
| 1 | **#8 Rescate de planilla** (ARS 30-60 mil, 2-3 h) | Es la oferta más fácil de aceptar ("mandame la planilla rota"). Claude en Excel hace justo esto. Abre la puerta al proceso. |
| 2 | **#1 Planilla de stock en 48 h** (ARS 60-100 mil) | Es su experiencia de pasantía convertida en producto. Es el puente directo a Stock Sano. |
| 3 | **#4 Costeo + precio de venta para emprendedor** (ARS 50-90 mil) | Es un dolor universal con inflación (33,5% interanual). La UAI cobra $215 mil por enseñarlo, y él lo entrega hecho. |
| 4 | **#24 Sesión 1:1 Claude en Excel** (ARS 40-70 mil) | Es su diferencial real (usa Claude todos los días). Es demostrable en 90 s de video. |
| 5 | **#27 Tutoría de IO, Estadística y Costos** (ARS 15-25 mil/h) | Es la **red de seguridad**: el cobro más probable de la semana, en temporada de finales. No da puente, pero da caja y práctica explicando. |

**Combo recomendado para la semana**: un solo mensaje a contactos tibios que ofrezca la #8 como gancho y la #1, la #4 y la #9 como siguiente paso, y en paralelo la #27 en los grupos de la facultad. **Meta concreta: 50 mensajes personalizados entre D1 y D3, 10 conversaciones, 2-3 señas.**

**Agenda de 7 días sugerida**

| Día | Tarea |
|---|---|
| D1 (jue 2026-10-01) | Armar con Claude 2 demos con datos ficticios (stock y costeo) más un video de 60-90 s. Crear el link de pago de MP. |
| D2 (vie 2026-10-02) | 25 mensajes personalizados (familia, empresa de la pasantía, comerciantes conocidos, contadores). Post en LinkedIn y estados de WhatsApp. Publicar la #27 en grupos de la carrera. |
| D3 (sáb 2026-10-03) | 25 mensajes más. Recorrer 10 comercios del barrio con el demo en el celular. |
| D4-D5 (dom-lun 2026-10-04/05) | Llamadas de 15-20 min con los interesados. Cerrar alcance por escrito y cobrar el 50% de seña. |
| D6-D7 (mar-mié 2026-10-06/07) | Entregar el primer trabajo y pedir testimonio y referido. Registrar horas reales (para recalibrar precios). |

---

## 3. Mensaje modelo (LinkedIn / WhatsApp a contactos)

**Versión WhatsApp (contacto tibio, dueño o comerciante):**

> Hola [Nombre], ¿cómo va? Te escribo por algo puntual: estoy arrancando con un servicio chico para negocios, armando y arreglando planillas de stock, costos y precios. Lo hago con lo que vi en mi pasantía en logística y con herramientas de IA que uso a diario.
>
> Esta semana tomo 3 casos a precio de lanzamiento:
> • **Arreglo tu planilla actual** (la que se rompe o nadie entiende): $40.000, lista en 48 h.
> • **Planilla de stock con alerta de reposición** o **costeo + precio de venta de tus productos**: desde $60.000.
>
> Si querés, mandame la planilla que más dolores de cabeza te da y en 15 minutos te digo qué le pasa, sin compromiso. ¿Te sirve?

**Versión LinkedIn (post + DM):**

> Durante mi pasantía relevé el depósito de una empresa: stock, picking y layout. Lo que más me sorprendió: la mitad de los problemas vivían en una planilla de Excel que nadie entendía.
>
> Hoy uso Claude dentro de Excel para auditar planillas en minutos: qué fórmula está mal, qué dato se duplica, qué producto quedó vendido por debajo del costo.
>
> Este mes tomo 5 casos de pymes y emprendedores a precio de lanzamiento: arreglo de planillas, planillas de stock y costeo de productos, entregado en 48 h. Si tenés "esa planilla" en tu negocio, escribime.

**DM a contador o consultor (subcontratación):**

> Hola [Nombre], soy [Nombre], estudiante/graduado de Ingeniería Industrial. Armo planillas de stock, costeo y conciliaciones en Excel con IA, rápido y documentado. Si en este cierre de año tenés tareas de planilla que te comen horas (inventarios de clientes, armado de proyecciones), me ofrezco por tarea cerrada. Te paso un ejemplo si te sirve.

**Reglas del mensaje**: personalizar la primera línea (nada de copy-paste masivo); un solo pedido concreto; precio visible; seña del 50% por MP antes de arrancar; alcance por escrito en 5 líneas (qué incluye, qué no, plazo, 1 revisión).

---

## 4. Trampas comunes

1. **Cobrar poco "para arrancar" y quedar atado**. Precio de lanzamiento sí, pero **por escrito y por tiempo limitado** ("primeros 5 casos"), a cambio de testimonio. Con 33,5% de inflación interanual [S15], hay que actualizar la lista cada mes.
2. **Alcance que se estira**: la planilla de stock se convierte en "y que facture, y que mande WhatsApp". Hay que dejar el alcance cerrado con 1 revisión y presupuestar el resto aparte.
3. **Arrancar sin seña**: 50% por MP antes de abrir el archivo. Sin seña, la probabilidad real de cobro cae fuerte.
4. **Pisar profesiones reguladas**: no liquidar sueldos, no certificar inventarios ni estados contables, no firmar informes de HyS ni planos. Decirlo en la propuesta convierte al profesional en aliado y canal (#14, #21, #33, #34).
5. **Integridad académica**: tutoría sí; resolver TPs, parciales o tesis, nunca. Aclararlo **por escrito** en la publicación evita el pedido y protege su reputación en la facultad.
6. **Datos del cliente en IA**: planillas con datos de ventas, sueldos o clientes. Pedir copias anonimizadas cuando se pueda, revisar la configuración de privacidad del plan de Claude y no compartir archivos de un cliente con otro.
7. **Competir con lo gratis**: el Estado da cursos gratuitos de Excel + IA y de costos [S20], y hay plantillas gratis en todos lados. Se gana **haciéndolo con los datos del cliente**, no enseñando lo genérico.
8. **Plataformas en frío para el corto plazo**: Fiverr y Workana no dan el primer cobro en 7 días a un perfil nuevo (#36). ADPList no paga (#37). Para esta semana sirven solo los contactos tibios.
9. **Facturación**: para cobrar a pymes de forma regular hace falta monotributo (las empresas piden factura). En la primera semana se puede cobrar a personas por MP, pero conviene **iniciar el trámite ya**. Las categorías y montos vigentes no se verificaron en esta sesión.
10. **Prometer ahorros**: "te ahorro 30%" sin medir es la trampa del gurú. Prometer entregables concretos (planilla, informe, sesión), no resultados.
11. **Dispersarse**: 37 ideas no son 37 negocios. Para la estrategia de fondo conviene que todo lo que se venda esta semana genere **un caso documentado** para Orden Operativo. La #27 (tutoría) es la excepción consciente: es caja.
12. **Convocatorias con letra chica**: el Premio UP-Santander exige un alumno o graduado UP en el equipo [S6], y San Juan cierra el 2026-10-05 [S24]. Leer las bases antes de vender la #22.
