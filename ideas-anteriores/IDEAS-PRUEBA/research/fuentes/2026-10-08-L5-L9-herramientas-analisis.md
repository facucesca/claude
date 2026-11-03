# L9 y L5: herramientas de análisis (calculadora de ingeniería + IA analista)

**Fecha:** 2026-10-08 · **Para:** Facu · **Tipo:** estudio de mercado de dos ideas emparentadas (etapa 1: negocio intermedio)

> **Cómo leer este informe (Regla N.º 1).** Cada afirmación lleva una marca:
> - **DATO** = verificado, con fuente [F#] y fecha. Si dice "(resumen de búsqueda)", lo vi en los resultados del buscador pero **no pude abrir la página**: tomalo como menos firme.
> - **ESTIMACIÓN** = número mío, con el razonamiento al lado.
> - **OPINIÓN** = mi juicio, separado de los datos.
> - **NO VERIFICADO** = lo busqué y no lo pude confirmar.
>
> **Alcance real:** 29 búsquedas web y unas 25 páginas abiertas (el 2026-10-08). Se agotó el cupo de búsquedas de la sesión, así que algunos huecos quedan marcados como tales (ver §11). No tuve acceso a herramientas de volumen de búsqueda (Ahrefs/Semrush con login), así que **no sé cuánta gente busca en Google "punto de pedido" o "análisis ABC" en español**.

---

## 0. Resumen en 10 líneas

1. **L9 no es una idea nueva dentro del proyecto:** es la suma de C34 (calculadoras gratis como imán, puntaje 4,5) y "Stock Sano" (diagnóstico de inventario, puntaje 7,5) del estudio del 2026-10-01 [F49]. Lo nuevo es la IA que explica y la derivación a Facu. La herramienta sola vale poco; **lo que vale es que le consiga clientes a Stock Sano.**
2. Las **calculadoras de fórmulas sueltas** (punto de pedido, stock de seguridad, EOQ) ya existen gratis en español y viven de publicidad (miniwebtool, Hacé Cuentas, The Retail Exec) [F21–F23]. No hay espacio para cobrar por eso.
3. El **software de inventario con IA** que sí cobra (Prediko USD 49/mes en adelante, Inventory Planner, Cogsy, Netstock USD 900/mes) cobra porque **se conecta a los datos del cliente y se usa todas las semanas**, no por las fórmulas [F1, F3, F5, F8].
4. **No encontré** una herramienta en español donde subís el Excel de ventas y stock y te devuelve ABC + plata parada + quiebres + punto de pedido explicado. "No lo encontré" no quiere decir que no exista.
5. **L5 (validador de ideas/rentabilidad con IA)** es una categoría saturada y que se volvió gratis: ValidatorAI es gratis y dice haber analizado ~288.000 ideas [F12]; IdeaProof vende paquetes desde €19,99 [F16]. El único caso con plata documentada (DimeADozen) facturó USD 58.000 en 5 meses **en 2023**, cuando la categoría era novedad [F14].
6. El riesgo de "lo hace ChatGPT gratis" es **alto para L5 y medio para L9**: el 51% de los dueños de pymes de EE.UU. ya usa IA generativa para analizar datos (U.S. Bank, 2026) [F33]; en Argentina, el 42% de las empresas relevadas usa al menos una tecnología de IA (CEPE-UTDT/Fundar, 2026) [F35].
7. Argentina: el universo es grande (1.773.892 certificados MiPyME en abril de 2023, 95,9% micro) [F37], pero la plata está escasa (IPA: más de 24.000 cierres de empresas entre dic-2023 y feb-2026) [F38] y **no encontré ninguna encuesta que mida cuánto pagaría una pyme argentina por software de análisis**.
8. **Diseño recomendado (OPINIÓN):** un solo producto, "diagnóstico de stock en 5 minutos" basado en L9. L5 entra después y cambiado: no "¿será rentable mi idea?" sino "¿qué productos o clientes de mi negocio dejan plata?", usando datos reales.
9. **Validación (2–4 semanas, menos de USD 200):** primero a mano ("concierge"), sin programar nada: ofrecer el diagnóstico gratis a 30 negocios a cambio de su archivo de ventas y stock, y medir cuántos lo mandan y cuántos pagan después.
10. **Veredicto:** L9 **6/10** como vehículo de etapa 1 (sirve si es la puerta a la consultoría, no como SaaS). L5 **3/10** como producto propio; conviene meterla adentro de L9.

---

## 1. Qué se evaluó y qué ya se había dicho

| Idea | Qué es | Antecedentes en el repo |
|---|---|---|
| **L9** (favorita) | Página con calculadoras de ingeniería industrial (stock, ABC, Pareto…) + IA que sugiere mejoras + derivación a un uno a uno pago con Facu | C34 "calculadoras tool-SEO como imán", **4,5/10** para perfil no programador; #2 "Stock Sano", **7,5/10**; P2 "portfolio de micro-herramientas SEO", 7/10 [F49] |
| **L5** | IA "analista de negocios": cargás tu negocio o idea con márgenes y, con fórmulas, te dice si va a ser rentable | No evaluada antes como tal |

**Corrección a un dato previo:** el estudio del 2026-10-01 citaba a Hacé Cuentas como sitio que "posiciona calculadoras en español". **Hoy (2026-10-08) la página de stock de seguridad de Hacé Cuentas devuelve HTTP 410 (borrada)** y su portada (600+ calculadoras, con AdSense) no muestra categorías de stock o logística [F21]. Por qué la sacaron: no lo sé. Sigue siendo un competidor en calculadoras generales, pero no en inventario.

---

## 2. Parecidos en el mundo

### 2.1 Calculadoras gratis (el "imán" de L9)

| Quién | Qué hace | Cómo gana plata | Datos |
|---|---|---|---|
| **miniwebtool (ES)** | Punto de pedido con stock de seguridad estadístico (Z × σ), más EOQ, rotación, stock de seguridad | Publicidad + Premium; **gratis hasta 3 usos/día** | DATO [F22], consultado 2026-10-08. No permite subir archivos. No vi un análisis ABC |
| **The Retail Exec (ES)** | Artículo-calculadora de punto de reorden | Registro obligatorio para leer todo; links a software (tiene página de "Affiliate Disclosure") y publicidad | DATO [F23] |
| **Hacé Cuentas (AR)** | 600+ calculadoras generales | AdSense | DATO [F21]. La de stock ya no está (410) |
| **Crehana** | Plantilla gratis de análisis ABC en Excel | Imán para sus cursos | Resumen de búsqueda [F24] |
| **Omni Calculator** | Miles de calculadoras en inglés | Publicidad | ~16,5 M de visitas en abril de 2026 (estimación de Semrush, −9,1% contra marzo); en julio de 2025, 52% de las visitas venían de Google orgánico [F26] (resumen de búsqueda) |
| **Vorne / OEE.com** | Desde 2005 regala guías, una planilla y una calculadora de OEE en oee.com | Vende el equipo XL de monitoreo de producción (USD 4.690 el modelo XL HD; dicen tener 45.000+ instalaciones) | [F25] (resumen de búsqueda). **Es el caso más parecido a L9 en espíritu: contenido de ingeniería gratis que lleva a un producto pago.** No encontré datos de cuántos clientes trae |

**OPINIÓN:** las calculadoras de una fórmula son un commodity. Viven de publicidad con mucho tráfico, y con el tráfico chico en español de un nicho B2B la publicidad no paga (esto ya lo marcaba el estudio del 2026-09-02 [F49]).

### 2.2 Software de inventario con IA para pymes (lo que hace L9 si se vuelve SaaS)

| Producto | Precio (USD) | Datos de escala / estado | Fuente |
|---|---|---|---|
| **Prediko** (Shopify) | **Desde 49/mes** para tiendas con menos de 100.000 de facturación anual; sube por tramo de facturación (12 tramos); prueba de 14 días | "2.500+ comerciantes de Shopify" (lo dice la empresa). Ronda semilla de USD 5 M en 2022 | Precios DATO [F1]; ronda de inversión (resumen de búsqueda) [F2] |
| **Inventory Planner by Sage** | Essentials 119,99/mes (Eightx, 2026-06-18); los planes superiores se estiman en 250–1.200+/mes | **Hoy la ficha en la Shopify App Store dice "no disponible actualmente"** [F4]. Eightx vende servicios de CFO (no es competidor directo) | [F3], [F4] |
| **Cogsy** | Desde 199/mes | Activo según fuentes de 2026 | Resumen de búsqueda [F8] |
| **Netstock** | **Desde 900/mes**, contrato anual; implementación de 6 a 10 semanas; se integra con 60+ ERP | ~2.400 clientes según una fuente secundaria (la web de precios no da el número) | DATO [F5]; cantidad de clientes NO VERIFICADA [F6] |
| **Cin7 Core** | 349 / 599 / 999 por mes | Compró a Inventoro (IA de pronóstico para pymes, checa) en 2024 | Resumen de búsqueda [F7], [F10] |
| **Stocky** (de Shopify) | Era gratis/incluida | **Shopify la cerró el 2026-08-31**; la sacó de la App Store el 2026-02-02 | [F9] (blog de inFlow, que vende un reemplazo) |
| **Forecastly** (Amazon) | Desde 49/mes | **Cerró el 2021-09-15** y su tecnología se integró a otra empresa | Resumen de búsqueda [F11] |

**Lo que muestra esta tabla (OPINIÓN, apoyada en los datos de arriba):**
- Todos los que cobran **se conectan solos a los datos del cliente** (Shopify, ERP) y **recalculan todo el tiempo**. Nadie cobra por "subí un Excel una vez".
- Están hechos para e-commerce en dólares (Shopify/Amazon) o para empresas medianas con ERP (Netstock). **Ninguno está pensado para el comercio argentino con Tango o Excel**; eso es un hueco, pero también puede ser señal de que es un mercado que paga poco.
- Hay movimiento de consolidación y cierres (Stocky, Inventoro, Forecastly). No es un mercado vacío: es un mercado con jugadores con plata.

### 2.3 Validadores de ideas y planes de negocio (lo que es L5)

| Producto | Precio | Escala / estado | Fuente |
|---|---|---|---|
| **ValidatorAI** | **Gratis** (puntaje de la idea, competencia, simulador de clientes) | Dice tener ~287.725 ideas analizadas / "300.000 founders" (números propios, no coinciden entre sí) | DATO [F12] |
| **DimeADozen** | 2023: USD 39 por informe (5 por 109; 20 por 189). Hoy: idea gratis, informes de USD 9 y 129 (según terceros) | **2023:** USD 58.000 de facturación y 32.000 de ganancia en 5 meses; 900+ pagos sobre 40.000+ usuarios gratis; puesto en venta a USD 160.000. 60% del tráfico vino de directorios de IA (FutureTools, There's An AI For That) | [F14] (artículo del 2023-09-21 con números del fundador); precio actual [F15] (resumen de búsqueda) |
| **IdeaProof** | 40 créditos gratis; paquetes de €19,99 / €49,99 / €99,99; validar una idea cuesta 40 créditos | Dice "10.000+ founders" | DATO [F16] |
| **LivePlan** | USD 15 y 30/mes pagando anual (en la página aparecen también 20 y 40) | "1,5 millones de negocios atendidos" (dato de la empresa, abarca todos sus productos y años) | DATO [F17] |
| **Upmetrics** | Desde USD 14/mes pagando anual | — | DATO [F18] |
| **Enloop** | Desde USD 19,95 | Sigue activo según Capterra (2026-02-08) | Resumen de búsqueda [F19] |
| **Fathom** (análisis financiero para contadores) | ~USD 50/mes | Se conecta a QuickBooks/Xero/MYOB; compara KPIs **entre los clientes del contador** | Resumen de búsqueda [F20] |

**Cálculo propio sobre los números de DimeADozen:** 900 pagos / 40.000 gratis ≈ **2,2% de conversión** a una compra de USD 39. Son números que dio el fundador y no se pueden auditar [F14].

**OPINIÓN:** L5 entra a un mercado donde (a) el líder en visibilidad es gratis, (b) los precios bajaron de USD 39 a USD 9 por informe entre 2023 y 2026, y (c) lo que hace la herramienta lo hace cualquier chat de IA con un buen pedido. El caso de éxito (DimeADozen) aprovechó una ventana de 2023 que ya se cerró.

---

## 3. El riesgo central: ¿por qué alguien pagaría si ChatGPT o Claude lo hacen gratis?

### 3.1 Qué tan cerca está el cliente de "hacerlo solo"
- **DATO:** en EE.UU., el 75% de los dueños de pymes usa IA generativa en su negocio y el **51% la usa para analizar datos** (encuesta de U.S. Bank publicada en ABA Banking Journal el 2026-07-09; no informa la muestra) [F33].
- **DATO (resumen de búsqueda):** en una encuesta de Bluehost a 350 pymes de EE.UU. (2026), el 73% usa ChatGPT [F34]. Ojo: Bluehost vende servicios para pymes.
- **DATO:** en Argentina, el 42% de las empresas relevadas usa al menos una tecnología de IA, y más de la mitad de esas está "en etapa experimental"; la barrera principal que citan es la **falta de gente capacitada**, más que el costo (CEPE-UTDT + Fundar, nota del 2026-05-01) [F35]. La encuesta Observatorio PyME/BID (nov–dic 2025, 402 empresas) da 36,4% [F36] (resumen de búsqueda).

**Lectura (OPINIÓN):** la barrera ya no es tener acceso a la IA. Es **saber qué preguntarle, preparar los datos y confiar en el resultado**. Eso juega a favor de L9 (resultado armado por un ingeniero, con un método fijo) y en contra de L5 (la pregunta "¿es rentable mi idea?" se la hace cualquiera a ChatGPT).

### 3.2 Qué hace que una herramienta así cobre (evidencia)
| Palanca | Evidencia | ¿L9 la puede tener? | ¿L5? |
|---|---|---|---|
| **Conexión a los datos del cliente** | Todos los que cobran se conectan: Prediko a Shopify, Netstock a 60+ ERP, Fathom a QuickBooks/Xero [F1, F5, F20] | Sí, empezando por un formato de exportación estándar (Mercado Libre / Tiendanube / Tango); a largo plazo, por API | No: una idea no tiene datos |
| **Uso repetido** (se vuelve a usar cada mes) | Todo el software de inventario se cobra por mes porque la reposición es continua [tabla 2.2] | Sí: el punto de pedido se recalcula todos los meses | No: se usa una vez por idea |
| **Especialización en un rubro** | Análisis de "wrappers" de IA (notas de opinión de 2025–2026, no datos duros): sobreviven los que tienen datos propios e integración en el flujo de trabajo, no los que solo dan acceso al modelo [F47] | Sí (un rubro primero) | Difícil |
| **Benchmarks** | Fathom compara entre los clientes del mismo contador [F20] | **A futuro:** con 50+ diagnósticos se puede decir "tu plata parada es X%, la mediana del rubro es Y%" (ESTIMACIÓN de umbral, sin fuente) | No |
| **Acompañamiento humano** | ValidatorAI ofrece una asesoría paga aparte de lo gratis (según BigIdeasDB, un competidor) [F13]; Vorne regala contenido y vende equipos [F25] | **Sí, es el modelo propuesto** | Poco creíble sin experiencia previa |

**Conclusión (OPINIÓN):** L9 puede tener 4 de las 5 palancas; L5 genérica, casi ninguna. Si L9 se queda en "calculadora de fórmulas", ChatGPT la reemplaza. Si es "subís tu archivo y en 5 minutos sabés cuánta plata tenés parada y qué comprar", es otra cosa.

---

## 4. Argentina y LATAM

### 4.1 Tamaño del universo
- **DATO:** 1.773.892 certificados MiPyME vigentes en abril de 2023 (incluye monotributistas y no empleadores); el 95,9% son micro; 50% servicios, **24,1% comercio**, **12,9% industria** (El Cronista, 2023-04-02) [F37]. No encontré un dato oficial de 2025 o 2026.
- **NO VERIFICADO:** el "Monitor de empresas" de Fundar citado por terceros pondría a los empleadores en ~488.000 (desde ~512.000 en dic-2023). No pude abrir la fuente original.
- **DATO:** el Observatorio IPA (industriales pymes) cuenta más de 24.000 cierres de empresas entre dic-2023 y feb-2026 y proyecta unos 40.000 a fin de 2026 (iProfesional, 2026-06-11) [F38]. Ojo: es una cámara empresaria y es una proyección.
- **DATO del repo, no re-verificado hoy:** 2,7 millones de emprendedores y pymes venden en Mercado Libre en Argentina (iProfesional, 2026-06-27) [F48].

### 4.2 ¿Cuántas usan sistema de gestión (y pueden exportar datos)?
- **DATO viejo:** uso de ERP según CESSI (2016): **18% de las micro, 39% de las pequeñas, 58% de las medianas** y 68% de las grandes [F39]. Tiene 10 años; no encontré nada más nuevo con alcance nacional.
- **DATO (dicho por la empresa):** Tango "lo usan más de 100.000 pymes" (nota del 2023-10-09) [F40]. Tango trae "Tango Tablero" para ver indicadores en tiempo real [F40]; **no encontré** que tenga análisis de stock con IA (la búsqueda trajo mucho ruido).
- **DATO (con interés comercial):** Develop Argentina (vende desarrollo de software) dice que desde 2025 ARCA exige factura electrónica a casi todos los contribuyentes, sin citar la norma (2026-06-25) [F42]. **No lo verifiqué con la norma.** Si es cierto, hay más datos digitales de ventas que antes.
- **Señal sin fecha (resumen de búsqueda):** Axoft (Tango) dijo que ve "resistencia de las pymes a poner su información crítica en la nube" [F50]. **Esto es un riesgo directo para "subí tu Excel".**

### 4.3 Precios de los sistemas de gestión locales (referencia de cuánto paga una pyme por software)
- **DATO (página de un competidor, SpomBridge, precios de septiembre de 2026):** Contabilium cobra **$122.000 a $245.000 + IVA por mes** según el plan (el Standard incluye 5.000 SKU); Xubio, Colppy y Tango no publican precio en esa comparativa [F41].
- **DATO (Develop Argentina, con interés comercial):** Tango en la nube desde ~$180.000/mes; Siigo $29.000–89.000/mes; Gestix desde $15.000/mes [F42].
- No pasé estos montos a dólares porque no verifiqué el tipo de cambio de hoy.

**Lectura (OPINIÓN):** la pyme argentina que tiene sistema ya paga una cifra relevante por él. Una herramienta extra de análisis compite por el mismo presupuesto, y los sistemas pueden sumar esta función el día que quieran. **El consultor (Facu) no compite con el sistema: lo usa como fuente de datos.**

### 4.4 Disposición a pagar
- **No encontré ninguna encuesta que pregunte cuánto pagaría una pyme argentina por un software o un informe de análisis.** Lo más cercano:
  - El 78,3% de las empresas no tiene una partida específica para IA (la mete en el presupuesto general); solo el 7,5% la tiene (resumen de búsqueda, Unidiversidad, encuesta Observatorio PyME/BID) [F36].
  - Chubb (2025): el 59% de las pymes se financia con plata de sus dueños [F43] (resumen de búsqueda).
  - ENAC, Radar Pyme del 3er trimestre de 2025 (379 empresas): el 40,4% reportó malas ventas (caída de más del 10% en unidades) [F44] (resumen de búsqueda).
  - IAE (jul–ago 2026, 221 dueños): mejora contra el 2º semestre de 2025, pero "todavía no se volvió inversión generalizada" [F45] (resumen de búsqueda).
- **OPINIÓN:** el contexto es bueno para el mensaje ("tenés plata parada en stock que no rota") y malo para el bolsillo. Hay que vender **ahorro medible** (plata que se libera), no "software".

### 4.5 Competidores locales en español
- Calculadoras de fórmulas: miniwebtool ES, The Retail Exec ES, plantillas de Crehana [F22–F24].
- Análisis para vendedores de Mercado Libre: **Nubimetrics** (argentina; mercado, competencia, "Mi negocio"; tiene un conector MCP; prueba gratis; **no muestra funciones de stock** en la portada) [F46]. Real Trends: no pude ver qué ofrece (la página no cargó el contenido).
- Sistemas de gestión con reportes: Tango (Tablero), Xubio, Contabilium, Colppy [F40–F42].
- Consultores de costos y contadores: existen, pero **no encontré** ofertas productizadas de "diagnóstico de stock" con una herramienta como imán (el estudio del 2026-10-01 tampoco las había encontrado) [F49].

---

## 5. El modelo "herramienta gratis + consultoría": casos y conversiones

| Caso | Qué regalaba | Qué vendía | Resultado conocido |
|---|---|---|---|
| **HubSpot Website Grader** | Nota gratis de tu sitio web (desde feb-2007) | Software de marketing de HubSpot | **1 millón** de URLs analizadas para 2009 [F27]; ~4 millones para 2011 y "hasta 2,5 millones de personas" según el VP de ventas (resumen de búsqueda) [F27]. **HubSpot nunca publicó cuántos clientes trajo** |
| **Ubersuggest → NP Digital** (Neil Patel) | Herramienta SEO gratis | Agencia | Patel dice tener ~300.000 usuarios diarios (en otra página dice 50.000) [F28]. **Sin datos de conversión a agencia** |
| **Vorne / OEE.com** | Guías y calculadora de OEE desde 2005 | Equipos XL | 45.000+ instalaciones (dato de la empresa); sin atribución al contenido [F25] |
| **DimeADozen** | Informe parcial gratis | Informe completo | ~2,2% de gratis → pago (cálculo propio con números del fundador) [F14] |

**Tasas de conversión de referencia (todas débiles):**
- De lead a cliente en B2B: **1–5%** o **0,67% en SaaS B2B** según tablas de agencias **sin metodología visible** [F30]. NO VERIFICADO como benchmark.
- De freemium a pago, en empresas que apuntan a pequeños negocios: **6–10% por mes**, según una encuesta de Databox a "decenas" de profesionales de SaaS (actualizada el 2025-07-10) [F29]. Muestra chica y autodeclarada.
- **No encontré ningún dato publicado de "herramienta gratis → contrato de consultoría".**

**ESTIMACIÓN (embudo de L9, todas son suposiciones mías para dimensionar, no datos):**
- 1.000 visitas/mes calificadas → 30% usa la herramienta (300) → 30% sube su archivo o deja el mail (90) → 7% pide la llamada (6) → 30% compra un diagnóstico pago (~2 clientes/mes).
- Con un ticket de USD 200–600 por proyecto (rango estimado en el estudio del 2026-10-01 [F49]) da **USD 400–1.200/mes**, **si** se llega a 1.000 visitas calificadas, cosa que en SEO de nicho en español puede tardar meses (el estudio del 2026-09-02 hablaba de 4–8 meses para que una herramienta SEO empiece a rendir; no lo re-verifiqué).
- **Consecuencia (OPINIÓN):** al principio la herramienta no sirve como imán de tráfico. Sirve como **excusa para la venta directa**: "te hago el diagnóstico de stock gratis en 24 horas, mandame tu Excel".

---

## 6. SEO y búsqueda con IA (2025–2026)

- **DATO:** el estudio más serio que encontré (Khosravi y Yoganarasimhan, arXiv, v1 del 2026-02-05) compara Wikipedia en inglés contra otros idiomas sin AI Overviews y mide **−15% de tráfico diario**; la caída es **mucho menor en artículos técnicos (STEM)** y mayor en cultura [F31]. **Ojo:** la página muestra una versión 2 retirada y no está confirmado que tenga revisión de pares.
- **DATO de segunda mano:** un análisis de Ahrefs (contado por MarTech Series en mayo de 2026) pone en **58%** la pérdida de clics de las páginas que están primeras cuando aparece un AI Overview [F32].
- **DATO (estimación de Semrush):** Omni Calculator mantiene entre 14 y 18 M de visitas por mes en feb–abr 2026; no se ve una caída clara [F26].
- **No encontré ningún estudio que mida el efecto de la IA solo en páginas de calculadoras.** La tesis del estudio del 2026-09-02 ("lo que se lee muere, lo que se usa sobrevive", Ahrefs 2026-07-16) sigue siendo la mejor que tenemos, pero es una tesis, no una medición [F49].

**OPINIÓN:**
- Una calculadora de una sola fórmula (punto de pedido = demanda × plazo + stock de seguridad) **es reemplazable**: el resumen de IA te da la fórmula y hasta el resultado si le pasás los números.
- Una herramienta que **procesa tu propio archivo** de 3.000 SKU no es reemplazable por un resumen del buscador. Sí puede reemplazarla un chat de IA con el archivo adjunto, y ahí el diferencial pasa a ser método, formato y confianza (§3).
- El SEO en español sirve como canal **secundario y lento**. No conviene basar la etapa 1 en él.

---

## 7. Diseño recomendado: cómo combinar L9 y L5

### 7.1 ¿Un producto o dos? (OPINIÓN)
**Uno solo, basado en L9.** L5 tal como está escrita ("¿mi idea será rentable?") apunta a gente **sin negocio y sin datos**, que es la que menos paga y la que mejor atiende ChatGPT gratis. Dentro de L9 tiene sentido una versión distinta de L5: **"rentabilidad de lo que ya vendés"** (margen de contribución por producto o cliente, punto de equilibrio, Pareto de margen). Usa los mismos datos que sube el cliente para el diagnóstico de stock.

### 7.2 Producto: "Diagnóstico de stock en 5 minutos" (nombre provisorio)
**Qué le pedís al usuario (lo mínimo, para que no abandone):**
1. Ventas de los últimos 12 meses por producto: código, descripción, fecha o mes, cantidad, precio (el export de su sistema, Mercado Libre o Tiendanube, o un Excel).
2. Stock actual por código.
3. Costo unitario por código.
4. *(Opcional)* Proveedor y plazo de entrega en días; rubro.

**Qué le devolvés (2 páginas, en lenguaje de dueño):**
- **Titular:** "Tenés aprox. $X en stock que no se vendió en 180 días" (plata parada = unidades sin movimiento × costo).
- **ABC** por facturación y **ABC por margen** (no siempre coinciden, y eso suele ser lo más revelador).
- **Cobertura en días** por producto y **quiebres probables** (stock menor a la demanda del plazo de entrega).
- **Punto de pedido y stock de seguridad** sugeridos para los productos A (con nivel de servicio que el usuario elige).
- **Top 10 acciones** redactadas por la IA a partir de los números ya calculados ("liquidar estos 15 productos C", "no te puede faltar este A"). **Importante (OPINIÓN):** los números los calculan fórmulas fijas, no la IA. La IA solo explica. Así se evitan errores de cálculo y el resultado se puede revisar.
- **Botón:** "Revisarlo con un ingeniero industrial (30 min)" → propuesta de Stock Sano.

**Cómo se cobra (propuesta; los precios son ESTIMACIONES a validar):**
| Nivel | Qué incluye | Precio tentativo |
|---|---|---|
| Gratis | Diagnóstico automático (o manual al principio) | 0 — es el imán |
| Proyecto | Stock Sano: limpieza de datos, conteo de verificación, plan de compras/liquidación, reunión | USD 200–600 (rango del estudio del 2026-10-01 [F49]) |
| Mensual | Recalcular el punto de pedido y alertas cada mes + 1 llamada | USD 50–150/mes (ídem) |
| SaaS (solo si se valida) | Autoservicio mensual | Referencia: Prediko arranca en USD 49/mes en EE.UU. [F1]; en Argentina, probablemente menos (OPINIÓN, sin dato) |

### 7.3 ¿Con qué rubro empezar? (OPINIÓN, con criterios)
Criterio clave: **que el archivo de exportación sea el mismo para todos**, así el programa lee un único formato y no hay que limpiar a mano cada caso.
| Opción | A favor | En contra |
|---|---|---|
| **Vendedores de Mercado Libre / Tiendanube con 200+ productos** | Exportación estándar; universo enorme (2,7 M en ML [F48]); venta 100% remota | Hay herramientas para ML (Nubimetrics) y la plataforma puede sumar la función; muchos son chicos y pagan poco |
| **Ferreterías, repuestos, distribuidoras (muchos SKU, con Tango u otro sistema)** | Mucho stock inmovilizado, la plata parada duele; ticket más alto | Exportaciones distintas según el sistema; desconfianza a subir datos [F50]; venta más presencial |
| **Rubro de la pasantía (artículos deportivos / retail)** | Facu conoce el problema de adentro | Depende de contactos que no conozco |

**Recomendación:** validar **dos** segmentos en paralelo durante la etapa a mano (ver §9) y quedarse con el que mande más archivos. No elegir de antemano.

### 7.4 Riesgos de diseño
- **Datos sucios:** el stock del sistema no coincide con el físico. Ya estaba marcado en Stock Sano [F49]. Para mitigarlo, el informe tiene que decir "esto supone que tu stock del sistema es real".
- **Confianza y privacidad:** subir ventas y costos a una web desconocida frena a cualquiera. Para mitigarlo: procesar el archivo en el navegador (no se sube a ningún servidor) o aceptar datos anonimizados (códigos sin descripción). **OPINIÓN:** al principio, el canal "me lo mandás por WhatsApp y te lo devuelvo yo" genera más confianza que una web anónima.
- **Responsabilidad:** un "comprá X unidades" que sale mal. Aclarar que es una sugerencia con supuestos.

---

## 8. MVP: equipo, costo y tiempo (todo ESTIMACIÓN)

| Versión | Qué es | Equipo | Tiempo | Costo |
|---|---|---|---|---|
| **V0, concierge** (sin programar) | Formulario (Tally o Google Forms) + Facu hace el análisis en Excel con Claude + informe en Docs | Solo Facu | 1 semana para armar la plantilla de análisis; 1–2 h por diagnóstico al principio | USD 0–20 (dominio opcional) |
| **V1, web simple** | Página que lee el Excel en el navegador, aplica las fórmulas fijas, muestra el informe y pide a la API de IA el texto de las recomendaciones | Facu (especificación, fórmulas, datos de prueba) + 1 amigo programador + Claude Code | 3–6 semanas a tiempo parcial; el amigo, ~20–40 h | Dominio ~USD 10–20/año; hosting en Cloudflare Pages en el plan gratis (Facu ya usa Cloudflare); la API se paga por uso, poco por informe (**verificar la tarifa vigente antes de lanzar**; no la consulté) |
| **V2, SaaS** (solo si V0/V1 dan señales) | Cuentas de usuario, conexión a Mercado Libre o Tiendanube por API, recálculo mensual, alertas | Programador con más dedicación | 2–4 meses | USD 1.000–5.000 si se le paga a un programador (rango grueso, sin fuente) |

**Factibilidad (OPINIÓN):** alta. Las fórmulas (ABC, cobertura, punto de pedido, stock de seguridad) son de primer año de ingeniería industrial, y Facu las domina. **Lo difícil no es la matemática: es leer archivos desordenados** (columnas con nombres distintos, fechas en mil formatos). Eso es trabajo del amigo programador y es la razón para arrancar con **un solo formato de exportación**. Con el amigo conviene definir antes de empezar: ¿se le paga, es socio o es un favor? Lo propongo como regla de la etapa 1.

---

## 9. Cómo validar en 2–4 semanas con menos de USD 200

**Hipótesis a probar (en orden):**
1. ¿Los dueños **mandan su archivo** de ventas y stock a cambio de un diagnóstico gratis? (confianza + fricción)
2. ¿El diagnóstico les **sorprende** (encuentra plata parada que no sabían que tenían)?
3. ¿Alguno **paga** por el paso siguiente (proyecto o seguimiento mensual)?

**Plan:**
| Semana | Acción | Costo |
|---|---|---|
| 1 | Armar la plantilla de análisis en Excel con Claude (ABC, plata parada, cobertura, punto de pedido) y probarla con datos de ejemplo. Página de una sola hoja + formulario (Tally gratis, o Carrd). Escribir el guion de contacto | USD 0–20 |
| 1–2 | **30 contactos directos** repartidos en 2 segmentos (por ej., 15 vendedores de ML/Tiendanube y 15 ferreterías o distribuidoras): LinkedIn, grupos de vendedores, conocidos, la red de la facultad y de la pasantía. Oferta: "diagnóstico de stock gratis en 48 h" | USD 0 |
| 2 | Prueba de anuncios chica (Meta o LinkedIn) hacia la página, para medir el costo por archivo recibido | USD 100–150 |
| 2–3 | Hacer cada diagnóstico a mano (V0), entregarlo en 2 páginas y una llamada de 30 min. Medir minutos por diagnóstico y % de archivos que hubo que limpiar | USD 0 |
| 3–4 | En la llamada, ofrecer el proyecto pago (USD 100–300 de entrada, para validar) y anotar objeciones textuales | USD 0 |
| | **Total** | **< USD 200** |

**Umbrales de decisión (propuesta para acordar con Facu antes de empezar):**
- **Corte 1 (semana 2):** de 30 contactos, **10 o más** mandan su archivo → la fricción de datos es manejable. Si son **menos de 5**, la herramienta "subí tu Excel" no es el camino: seguir con consultoría presencial y descartar la web.
- **Corte 2 (semana 4):** **2–3 o más** pagan algo o firman propuesta → construir V1. Si no paga nadie pero los diagnósticos gustaron → revisar precio y segmento, una sola iteración más.
- **Pérdida máxima:** USD 200 + ~40–60 h de Facu. Lo que se aprende aunque falle: qué datos tienen realmente las pymes, cómo los guardan y qué les duele (materia prima para la etapa 2).

**L5:** no recomiendo validarla por separado. Si Facu quiere probarla igual: una semana, una página "¿Es rentable tu producto? Calculadora de margen y punto de equilibrio", 3 publicaciones, y medir cuántos dejan el mail y cuántos pagarían USD 5–10 por un informe. Esperable (OPINIÓN): pocos, porque ValidatorAI es gratis [F12].

---

## 10. Veredicto por idea

### L9: calculadoras de ingeniería + IA + uno a uno con Facu → **6/10** (como vehículo de etapa 1)
| Criterio | Puntaje | Por qué (una línea) |
|---|---|---|
| Tamaño del problema | 6 | El stock parado y los quiebres duelen más con ventas en caída [F44], pero muchas micro no tienen datos ordenados [F39] |
| Disposición a pagar | 4 | Por la herramienta sola, baja (hay calculadoras gratis y ChatGPT); por la consultoría, posible pero **sin dato** de Argentina |
| Espacio frente a la competencia | 6 | No encontré "subí tu Excel → diagnóstico de stock" en español; el software de EE.UU. es caro y no está adaptado [F1, F5] |
| Ventaja de Facu | 6 | Ingeniería industrial + pasantía de logística; pero sin casos ni cartera de clientes todavía |
| Factibilidad | 8 | La V0 se hace a mano con Excel y Claude en una semana |
| Escalabilidad | 5 | Como imán + consultoría escala con las horas de Facu; el SaaS escalaría, pero contra jugadores con capital |
| Riesgo (10 = bajo) | 7 | Barato y acotado; los riesgos son que nadie mande archivos y los datos sucios |

### L5: IA analista de negocios / validador de rentabilidad → **3/10** (como producto independiente)
| Criterio | Puntaje | Por qué (una línea) |
|---|---|---|
| Tamaño del problema | 5 | Mucha gente con ideas, pero "¿será rentable?" no se responde con fórmulas sin datos reales |
| Disposición a pagar | 2 | El líder es gratis [F12]; los precios bajaron de USD 39 a 9 por informe entre 2023 y 2026 [F14, F15] |
| Espacio frente a la competencia | 2 | Categoría saturada (ValidatorAI, IdeaProof, DimeADozen, LivePlan, Upmetrics) y cualquier chat de IA hace lo mismo |
| Ventaja de Facu | 3 | Sabe costos, pero no tiene datos propios ni distribución que los demás no tengan |
| Factibilidad | 8 | Fácil de construir; ese es justamente el problema |
| Escalabilidad | 6 | Software puro, pero sin canal en español y con el precio en caída |
| Riesgo (10 = bajo) | 5 | Barato, pero lo más probable es que no facture nada; y riesgo de reputación si le dice "rentable" a alguien que después pierde plata |

### Opinión (marcada como tal)
Facu, mi lectura honesta: **L9 está bien como puerta de entrada y mal como negocio en sí.** La parte "calculadoras" es lo menos valioso de la idea: existe gratis, se copia en una tarde y la IA del buscador la vuelve innecesaria. Lo valioso son las otras dos partes: **que el cliente suba sus datos reales** y que **haya un ingeniero que se haga cargo** del resultado. Por eso propongo darla vuelta: no "una página de calculadoras que a veces deriva a Facu", sino **"Facu hace diagnósticos de stock; la herramienta es la forma barata de empezar la conversación y, más adelante, de hacer el trabajo repetitivo"**. Así encaja en la etapa 1: da plata relativamente rápido por consultoría, te mete adentro de pymes reales (aprendizaje para la etapa 2) y, si en 20–50 diagnósticos aparece un patrón que se repite, ahí puede estar el SaaS (con datos de referencia por rubro, que nadie más tiene en español).

L5 no la descartaría como pensamiento, pero sí como negocio aparte: **es la versión de la idea donde ChatGPT gana por goleada.** Su única versión con sentido es "rentabilidad de lo que ya vendés", como módulo de L9.

Dos puntos ciegos para no endulzar: (1) **no hay ningún dato** de que una pyme argentina pague por esto. Todo el modelo de cobro está en el aire hasta el corte 2 de la validación. (2) La desconfianza a compartir datos [F50] puede matar la versión web aunque el diagnóstico sea bueno. La validación a mano existe justamente para averiguarlo antes de gastar en programar.

---

## 11. Lo que NO pude verificar (para no repetirlo como dato)
- Volumen de búsqueda en Google de "punto de pedido", "análisis ABC", "stock de seguridad" en español y en Argentina.
- Cuántas pymes argentinas usan hoy un sistema de gestión (el último dato nacional es de 2016).
- Cuántos empleadores hay hoy en Argentina (el dato de Fundar llegó de segunda mano).
- Disposición a pagar software o consultoría de análisis en Argentina (no hay encuesta).
- Conversión real de "herramienta gratis → cliente de consultoría" (nadie la publica, ni HubSpot).
- Si DimeADozen se vendió y por cuánto (un sitio dice USD 150.000 en oct-2023, sin segunda fuente).
- Si Tango, Xubio o Contabilium ya tienen análisis de stock con IA.
- La norma exacta de factura electrónica obligatoria desde 2025.
- Tarifas vigentes de la API de IA (para costear el MVP; se verifican antes de construir).
- Qué ofrece Real Trends y quién es el dueño.

---

## Fuentes (consultadas el 2026-10-08)

**[abierta]** = abrí la página. **[resumen de búsqueda]** = lo vi en el resultado del buscador sin poder abrirla. Al lado va la fecha de publicación si se conoce.

- **[F1]** Prediko, Pricing [abierta]: https://prediko.io/pricing
- **[F2]** TechCrunch, "With Prediko, online brands should never run out of stock", 2022-09-14 [resumen de búsqueda]: https://techcrunch.com/2022/09/14/with-prediko-online-brands-should-never-run-out-of-stock/
- **[F3]** Eightx, "How much does Inventory Planner cost", 2026-06-18 [abierta]: https://eightx.co/blog/compare/how-much-does-inventory-planner-cost
- **[F4]** Shopify App Store, Inventory Planner by Sage ("no disponible actualmente") [abierta]: https://apps.shopify.com/inventory-planner
- **[F5]** Netstock, Pricing [abierta]: https://www.netstock.com/pricing/
- **[F6]** CFO Shortlist, Netstock [resumen de búsqueda]: https://www.cfoshortlist.com/vendors/netstock
- **[F7]** Capterra, Cin7 Core Pricing 2026 [resumen de búsqueda]: https://www.capterra.com/p/133038/Cin7-Core/pricing/ · Eightx: https://eightx.co/blog/compare/how-much-does-cin7-cost
- **[F8]** Eightx, Inventory Planner vs Cogsy [resumen de búsqueda]: https://eightx.co/blog/inventory-planner-vs-cogsy-forecasting
- **[F9]** inFlow, "Stocky Shopify app sunsetting" (vende un reemplazo) [abierta]: https://www.inflowinventory.com/blog/stocky-shopify-app-sunsetting/
- **[F10]** Vestbee, "Cin7 acquires Inventoro" [resumen de búsqueda]: https://vestbee.com/insights/articles/cin7-acquires-inventoro
- **[F11]** Jungle Scout, Q&A Forecastly (cierre 2021-09-15) [resumen de búsqueda]: https://www.junglescout.com/?p=94986
- **[F12]** ValidatorAI, portada [abierta]: https://validatorai.com/
- **[F13]** BigIdeasDB, "ValidatorAI alternative" (es un competidor; error 429 al abrir) [resumen de búsqueda]: https://bigideasdb.com/validatorai-alternative
- **[F14]** AI Pursuits, caso DimeADozen, 2023-09-21 [abierta]: https://ai-pursuits.beehiiv.com/p/how-this-bootstrapped-ai-startup-validated-900-business-ideas-and-made-32k-profit-in-just-5-months · Indie Hackers (error 403 al abrir): https://www.indiehackers.com/post/case-study-ai-business-idea-validator-makes-8k-m-profit-in-5-months-8306a4dd08
- **[F15]** Stork.ai, DimeADozen [resumen de búsqueda]: https://www.stork.ai/en/dimeadozen-ai · Indexator: https://dev.indexator.ai/companies/dimeadozen
- **[F16]** IdeaProof, Pricing [abierta]: https://ideaproof.io/pricing
- **[F17]** LivePlan, Pricing [abierta]: https://www.liveplan.com/pricing
- **[F18]** Upmetrics, Pricing [abierta]: https://upmetrics.co/pricing
- **[F19]** Capterra, Enloop (actualizada 2026-02-08) [resumen de búsqueda]: https://www.capterra.com/p/145820/Enloop/
- **[F20]** Capterra UK, Fathom [resumen de búsqueda]: https://www.capterra.co.uk/software/136476/fathom · GetApp: https://www.getapp.com/reporting-software/a/fathom
- **[F21]** Hacé Cuentas, portada [abierta]: https://hacecuentas.com/ · página de stock (HTTP 410 el 2026-10-08): https://hacecuentas.com/calculadora-stock-seguridad-punto-reposicion
- **[F22]** miniwebtool, Calculadora de punto de pedido [abierta]: https://miniwebtool.com/es/calculadora-de-punto-de-pedido/
- **[F23]** The Retail Exec (ES), Calculadora punto de reorden [abierta]: https://theretailexec.com/es/logistica-2/calculadora-punto-reorden/
- **[F24]** Crehana, Plantilla análisis ABC [resumen de búsqueda]: https://www.crehana.com/business/descargables/plantilla-analisis-abc/
- **[F25]** Vorne, portada [resumen de búsqueda]: https://vorne.com/ · PFFC, "Online lean resource" (lanzamiento de oee.com, 2005) [resumen de búsqueda]: https://pffc-online.com/ar/4018-online-lean-resource-121405
- **[F26]** Semrush, omnicalculator.com overview (actualizada 2026-05-13 y 2025-08-11) [resumen de búsqueda]: https://www.semrush.com/website/omnicalculator.com/overview/ · https://cw.semrush.com/website/omnicalculator.com/overview
- **[F27]** HubSpot Blog, "Website Grader Evaluates Over 1 Million URLs", c. jun-2009 [abierta]: https://www.hubspot.com/blog/bid/4834/Website-Grader-Evaluates-Over-1-Million-URLs · Demand Gen Report [resumen de búsqueda]: https://www.demandgenreport.com/?p=20329 · Sramana Mitra (entrevista a Mark Roberge) [resumen de búsqueda]: https://www.sramanamitra.com/tag/consultative-sales/
- **[F28]** Neil Patel, About [resumen de búsqueda]: https://neilpatel.com/about/
- **[F29]** Databox, "Freemium conversion rate", actualizada 2025-07-10 [abierta]: https://databox.com/freemium-conversion-rate
- **[F30]** Focus Digital, "Lead magnet conversion rate by industry" [resumen de búsqueda]: https://focus-digital.co/?p=4052
- **[F31]** Khosravi y Yoganarasimhan, "Impact of AI Search Summaries on Website Traffic", arXiv v1 del 2026-02-05 [abierta]: https://arxiv.org/abs/2602.18455v1
- **[F32]** The ATDB, "Google's AI Overviews now cost websites 58% of their clicks" (reproduce datos de Ahrefs vía MarTech Series) [resumen de búsqueda]: https://www.theatdb.com/news/new-research-googles-ai-overviews-now-cost-websites-58-of-their-clicks
- **[F33]** ABA Banking Journal, encuesta de U.S. Bank, 2026-07-09 [abierta]: https://bankingjournal.aba.com/2026/07/bank-survey-small-business-growth-continues-amid-economic-uncertainty/
- **[F34]** Bluehost, "State of Small Business AI Confidence 2026" (vende servicios) [resumen de búsqueda]: https://www.bluehost.com/state-of-small-business-ai-confidence
- **[F35]** Revista Mercado, "Una encuesta nacional midió la adopción de IA en PyMEs argentinas" (CEPE-UTDT/Fundar), 2026-05-01 [abierta]: https://mercado.com.ar/ruta-digital/una-encuesta-nacional-midio-la-adopcion-de-inteligencia-artificial-en-pymes-argentinas
- **[F36]** Unidiversidad, "Cuatro de cada diez pymes argentinas ya usan IA…" (Observatorio PyME/BID) [resumen de búsqueda]: https://www.unidiversidad.com.ar/cuatro-de-cada-diez-pymes-argentinas-ya-usan-ia-y-la-mayoria-no-redujo-puestos-de-trabajo
- **[F37]** El Cronista, "MiPyMEs: la nueva categoría…", 2023-04-02 [abierta]: https://www.cronista.com/economia-politica/mipymes-la-nueva-categoria-representa-un-alivio-fiscal-para-18-millones-de-empresas/
- **[F38]** iProfesional, "Advierten por cierres de empresas…" (Observatorio IPA), 2026-06-11 [abierta]: https://www.iprofesional.com/economia/457004-advierten-por-cierres-de-empresas-el-pais-podria-perder-500000-empleos-formales
- **[F39]** Revista Mercado, "La apuesta es a 2017" (CESSI, sept-2016) [abierta]: https://mercado.com.ar/revista/2016-septiembre-no1184/la-apuesta-es-a-2017/
- **[F40]** Contadores en Red, "Tango Delta…", 2023-10-09 [abierta]: https://contadoresenred.com/tango-delta-la-nueva-version-del-software-de-gestion-lider-para-administrar-pymes/
- **[F41]** SpomBridge, "Alternativas a Contabilium" (competidor; precios de sept-2026) [abierta]: https://app.spomsolutions.com/comparar/alternativas-a-contabilium
- **[F42]** Develop Argentina, "Sistemas de gestión comercial en Argentina 2026", 2026-06-25 (vende desarrollo) [abierta]: https://developargentina.com/blog/sistemas-gestion-comercial-argentina-2026
- **[F43]** Chubb, Barómetro Pymes Argentina 2025 [resumen de búsqueda]: https://www.chubb.com/content/dam/chubb-sites/chubb-com/ar-es/empresas/recursos/estudio-barometro-pymes-arg-v2.pdf
- **[F44]** ENAC, Radar Pyme del 3er trimestre de 2025 [resumen de búsqueda]: https://enac.org.ar/download/multimedia.archivo.a8c1b21b4c725722.YXJjaGl2by5wZGY%3D.pdf
- **[F45]** Revista Mercado, "Encuesta del IAE: las PyME se recuperan…" (jul–ago 2026) [resumen de búsqueda]: https://mercado.com.ar/tendencias/encuesta-del-iae-las-pyme-se-recuperan-pero-sostienen-cautela-en-empleo-e-inversion
- **[F46]** Nubimetrics, portada [abierta]: https://www.nubimetrics.com/
- **[F47]** Notas de opinión sobre "AI wrappers" (2025–2026; análisis, no datos) [resumen de búsqueda]: https://hatchworks.com/blog/gen-ai/ai-wrapper-product-strategy/ · https://jacar.es/en/llm-wrappers-when-they-are-a-business-and-when-they-are-not/
- **[F48]** iProfesional, Mercado Libre en Argentina, 2026-06-27 (citada en el repo el 2026-10-01; no re-verificada hoy): https://www.iprofesional.com/negocios/450528-mercado-libre-cambia-logistica-argentina-inversion-record-miles-empleos
- **[F49]** Documentos internos: `research/2026-09-02-estudio-mercado-ingresos-pasivos-ia.md` (idea 2, tool-SEO) y `research/fuentes/2026-10-01-ideas-ingenieria-industrial-ops.md` (ideas #2 Stock Sano y #34 calculadoras).
- **[F50]** ITSitio, "Un tango entre la tierra y la nube" (Axoft, sin fecha visible) [resumen de búsqueda]: https://www.itsitio.com/?p=2899
