# Indagación: "Ingeniería industrial productizada" (diagnóstico de stock + estudio de tiempos + productividad de depósito + calculadoras)

**Fecha:** 2026-10-15 · **Para:** Facu · **Etapa:** primera instancia (buscar, analizar, descartar) · **Ideas que integra:** L9 + L5, C34, C14, LOG-3-4

> **Cómo leer este informe (Regla N.º 1).**
> - **DATO** = verificado, con fuente [S#] o [R#] y fecha. "(resumen de búsqueda)" = lo vi en el resultado del buscador pero no pude abrir la página: es menos firme.
> - **ESTIMACIÓN** = número mío, con el razonamiento al lado.
> - **OPINIÓN** = mi juicio, separado de los datos.
> - **NO VERIFICADO** = lo busqué y no lo pude confirmar.
> - "según la propia empresa" = cifra que una empresa dice de sí misma.
>
> **Alcance real:** 15 búsquedas web (el tope) y unas 35 páginas abiertas el 2026-10-15. Además reutilizo datos de estudios anteriores del repo [R1–R3]; los marco como "dato del repo, no re-verificado hoy".
>
> **Regla N.º 2 (no repetir):** este informe **no agrega ideas nuevas al registro**. Todo lo nuevo son datos de ideas que ya estaban: L9, L5, C34, C14, LOG-3-4 y sus parecidas ya registradas (D38 calculadoras logísticas, P2 portfolio de calculadoras, A2 calculadora de índices + consultoría, C13 estudio de tiempos para talleres). El estudio del 2026-10-08 [R1] ya había cubierto parte de L9/L5; acá no lo repito: lo cito y sumo lo nuevo.

---

## Resumen en 10 líneas

1. **Afuera, el "diagnóstico de stock" existe y se usa como puerta de entrada a un software, no como negocio en sí.** Netstock regala un "Inventory Health Check" que valúa en USD 2.500 (o GBP 2.500) para venderte su software [S1]; EazyStock regala un "Stock Health Analysis" [S2]. Los dos piden conectarse al sistema de gestión (ERP) del cliente, no un Excel suelto.
2. **En Argentina no encontré a nadie que venda un diagnóstico de stock "empaquetado"** (precio fijo, entrega estándar) ni software local de reposición con IA para pymes. "No lo encontré" no es lo mismo que "no existe".
3. **No hay ningún dato de que una pyme argentina pague por esto.** Es el punto más débil de toda la bolsa (F1 = 2/5).
4. **Datos mínimos para el diagnóstico: 3 columnas por tabla** (ventas: código, fecha, cantidad; stock: código, cantidad; costo: código, costo). Con eso salen ABC, plata parada, quiebres y punto de pedido. Tango y Tiendanube exportan datos a planilla [S7, S9], pero **no pude confirmar** qué columnas trae cada exportación.
5. **Estudio de tiempos con video e IA:** hay jugadores con plata (Squint lanzó su agente el 2026-08-24 [S10]; Timer Pro dice tener 1.600+ empresas [S12]) y una herramienta gratis para marcar el video a mano (Iteros Lens [S11]). En Argentina no encontré oferta.
6. **¿Se puede hacer con Claude?** Claude **no recibe video**, solo imágenes (hasta 600 por pedido por API) [S16]. Gemini sí recibe video, pero por defecto toma **1 cuadro por segundo** y su propia documentación avisa que se pierden movimientos rápidos [S17]. Para tiempos de 2–5 segundos eso no alcanza sin revisión humana. Realista: **IA que propone, ingeniero que valida.**
7. **Productividad de operarios de depósito:** hay muchos productos afuera (Easy Metrics, Manhattan, Blue Yonder, Takt, Rebus, Deposco), todos para depósitos medianos y grandes, sin precio público [S18–S20]. En Argentina no encontré ninguno. Hay riesgo laboral y gremial.
8. **Calculadoras gratis:** casi toda la evidencia de que "traen clientes" viene de empresas que venden calculadoras (conflicto de interés) [S22]. HubSpot y Vorne usan herramientas gratis como imán, pero nunca publicaron cuántos clientes les trajeron [S23, S24].
9. **Propuesta (OPINIÓN):** entrar por **un solo módulo, el diagnóstico de stock, como servicio estandarizado**, apuntado al mismo cliente que la idea de piezas chicas (ferreterías, bulonerías, repuestos). El producto que escala no es el diagnóstico: es el **recálculo mensual conectado** (punto de pedido, alertas), y el diagnóstico es la forma de entrar.
10. **Filtro: 17/25 → PRIMERA, pero recortada:** solo el módulo de stock entra ya. Estudio de tiempos (C14) y productividad de depósito (LOG-3-4) quedan **PENDIENTES**.

---

## 1. Qué es exactamente (especificación integrada)

### 1.1 El hilo común (y su debilidad)
Las cuatro ideas tienen algo en común: **son ingeniería industrial clásica** (inventarios, estudio del trabajo, productividad) **hecha con un método fijo y herramientas, en vez de horas de consultor a medida**. Eso es lo que Facu llamó "darle la vuelta para automatizar y venderlo sin tener que estar atrás".

**OPINIÓN — la debilidad:** el hilo común es **la habilidad de Facu, no el cliente**. Cada módulo le vende a una persona distinta:

| Módulo | Idea | Problema | Quién lo sufre | Quién paga |
|---|---|---|---|---|
| **M1. Diagnóstico de stock** | L9 + L5 | Plata parada en mercadería que no rota, y faltantes de lo que sí se vende | Dueño de comercio o distribuidora con muchos artículos (ferretería, bulonería, repuestos, tienda online con 200+ productos) | El dueño |
| **M2. Estudio de tiempos por video** | C14 | No se sabe cuánto tarda cada tarea, ni dónde se pierde tiempo, ni cuánta gente hace falta | Jefe de planta o dueño de taller (confección, metalmecánica liviana, alimentos) | El dueño o el gerente de planta |
| **M3. Productividad en depósito** | LOG-3-4 | El sistema registra movimientos pero no cuánto rinde cada operario por tarea | Gerente de operaciones de un operador logístico (3PL) o de un centro de distribución | El gerente de operaciones |
| **M4. Calculadoras gratis** | C34 | (No es un problema: es un canal para conseguir clientes) | — | Nadie: es gratis |

Una marca puede tener los cuatro módulos, pero **para arrancar conviene un solo cliente y un solo módulo**. Ver §6 y §7.

### 1.2 Qué hace cada módulo

**M1 — Diagnóstico de stock (la puerta de entrada propuesta)**
- **Entrada:** el cliente manda 3 cosas de su sistema o de su Excel: ventas por artículo (12 meses), stock actual y costo (ver la lista exacta de columnas en §6.2, pregunta 2).
- **Salida (2 páginas, en lenguaje de dueño):**
  - **Plata parada:** "tenés $X en mercadería que no se vendió en 180 días" (unidades sin venta × costo).
  - **Clasificación ABC:** ordena los artículos por cuánto facturan. Los "A" son el ~20% que hace la mayor parte de la plata; los "C" son la cola larga. También ABC por margen (L5 entra acá, reconvertida: "¿qué productos te dejan plata?").
  - **Quiebres probables:** artículos cuyo stock no alcanza para cubrir la demanda mientras llega la reposición.
  - **Punto de pedido y stock de seguridad** para los artículos A. Punto de pedido = el nivel de stock en el que hay que volver a comprar. Stock de seguridad = colchón para cubrir días de venta más alta que lo normal.
  - **10 acciones** redactadas por IA **a partir de números calculados con fórmulas fijas** (la IA explica, no calcula; así no inventa números).
- **Después:** llamada 1:1 con Facu (30–60 min) y, si el cliente quiere, un servicio mensual.

**M2 — Estudio de tiempos remoto por video (C14)**
- El cliente recibe un **protocolo de filmación** (dónde poner el celular, cuántos ciclos filmar, qué no filmar).
- Se analiza el video: se corta cada ciclo en pasos ("elementos"), se mide cuánto dura cada uno, se separa lo que agrega valor de lo que es desperdicio, y se calcula el **tiempo estándar** (tiempo que debería llevar la tarea a ritmo normal, con tolerancias por fatiga y necesidades).
- **Salida:** tiempos por paso, desperdicios, y un gráfico de **balanceo** (Yamazumi = barras apiladas que muestran cuánto trabajo tiene cada puesto comparado con el **takt**, que es el ritmo al que hay que producir para cumplir con la demanda).

**M3 — Productividad de operarios de depósito (LOG-3-4)**
- **Entrada:** el registro de movimientos del sistema del depósito (quién movió qué y a qué hora), si existe. Si no existe, muestreo manual o planilla por turno.
- **Salida:** líneas o unidades por hora por tarea (picking = armar pedidos, recepción, guardado), comparación entre turnos, y cuánta gente hace falta por turno.

**M4 — Calculadoras gratis (C34)**
- Páginas con calculadoras de ingeniería industrial (punto de pedido, ABC, tiempo estándar, takt) que terminan en "¿querés esto con tus datos reales? Mandame tu archivo".

### 1.3 Cómo se conecta con la idea de piezas chicas (L14 / COM-3-5)
La investiga otro investigador; acá solo la conexión. **OPINIÓN:** el diagnóstico de stock (M1) es la **primera visita** de ese negocio: le muestra al dueño de una ferretería o bulonería cuánta plata tiene parada y qué le falta. La identificación de piezas por foto, el orden del depósito y el sistema de stock son **la implementación** que viene después. Mismo cliente, mismo problema, dos momentos. Por eso propongo que M1 apunte primero a ese rubro.

### 1.4 Cómo se cobra (todo ESTIMACIÓN a validar)
Tipo de cambio de referencia: dólar oficial venta $1.535 y blue venta $1.545 el 2026-10-15 a las 12:07 [S30].

| Nivel | Qué incluye | Precio a probar | Razonamiento |
|---|---|---|---|
| Gratis | Diagnóstico de 2 páginas (al principio hecho a mano) | 0 | Es el imán. Netstock regala el suyo y le pone un valor de USD 2.500 [S1] |
| Plan de acción | Limpieza de datos + plan de compras y liquidación + llamada | ARS 60.000 a 150.000 (≈ USD 39–98 al oficial) | Probar dos precios. El estudio del 2026-10-08 hablaba de USD 200–600 por proyecto [R1]; para comercios chicos argentinos lo veo alto (OPINIÓN), por eso arranco más abajo |
| Mensual | Recálculo de punto de pedido y alertas + 1 llamada | ARS 30.000 a 50.000/mes (≈ USD 20–33) | Referencia: un sistema de gestión completo como Contabilium cuesta $122.000–245.000 + IVA por mes (precios de sept-2026 [R1]) ≈ USD 79–160. Un agregado de análisis tiene que costar bastante menos que el sistema entero |
| Software (solo si se valida) | Autoservicio conectado, sin Facu | A definir | Prediko arranca en USD 49/mes en EE.UU. [R1] |

---

## 2. Mercado en Argentina

### 2.1 Datos (con fuente)
- **Universo de pymes:** 1.773.892 certificados MiPyME en abril de 2023; 95,9% micro; **24,1% comercio**, 12,9% industria (El Cronista, 2023-04-02) [R1]. *Dato del repo, no re-verificado hoy. No encontré un dato oficial más nuevo.*
- **Cuántas usan sistema de gestión:** 18% de las micro, 39% de las pequeñas, 58% de las medianas (CESSI, 2016) [R1]. *Tiene 10 años. Es el último dato nacional que se encontró.*
- **Tango (Axoft):** "lo usan más de 100.000 pymes" (según la propia empresa, 2023) [R1].
- **Uso de IA:** 42% de las empresas relevadas usa al menos una tecnología de IA, más de la mitad en etapa experimental (CEPE-UTDT/Fundar, 2026-05-01) [R1].
- **Contexto del sobrestock:** una nota de espacio pago (no editorial) en Revista Noticias, firmada por la consultora Identidad Financiera (2025-10-15), dice que muchas pymes usaron el sobrestock como defensa contra la inflación y que, con la baja de la inflación, ese capital inmovilizado pierde valor. **No trae ningún número** [S4]. Sirve como señal de que hay consultores usando ese mensaje, no como dato de mercado.
- **Planta industrial:** la UIA medía uso de capacidad instalada de 58–59% en mayo-junio de 2026 [R2]. *Dato del repo, no re-verificado hoy.* Importa para M2: vender "más capacidad" a una planta que usa el 60% de lo que tiene es difícil.
- **Depósitos y operadores logísticos:** existe CEDOL (Cámara Empresaria de Operadores Logísticos), que publica un índice de costos logísticos con la UTN [S21]. **No encontré** cuántos socios tiene, ni datos de metros cuadrados o empleados del sector.

### 2.2 Estimación del segmento para M1 (ESTIMACIÓN, muy gruesa)
- 1.773.892 × 24,1% ≈ **427.500 certificados de comercio** (2023).
- Supuesto mío, **sin fuente:** entre 5% y 10% tiene muchos artículos (300+) y datos de ventas digitales que se puedan exportar.
- Resultado: **≈ 21.000 a 43.000 comercios** posibles. Sirve solo para saber que el universo no es chico; no es un tamaño de mercado.
- Si 100 de ellos pagaran ARS 30.000–50.000 por mes: **≈ USD 2.000–3.300/mes** al oficial del 2026-10-15. Cálculo propio sobre precios que todavía nadie pagó.

### 2.3 Lo que falta (y no pude conseguir)
- Cuánto paga hoy una pyme argentina por consultoría de inventarios o por software de análisis. **No hay encuesta.**
- Cuántas pymes argentinas hicieron alguna vez un diagnóstico de stock.
- Volumen de búsquedas en Google de "punto de pedido", "análisis ABC" o "estudio de tiempos" en Argentina (no tengo herramientas de volumen con acceso).

---

## 3. Qué existe

### 3.1 Diagnóstico y analítica de inventario

**Afuera (verificado):**

| Quién | Qué ofrece | Precio | Datos | Fuente |
|---|---|---|---|---|
| **Netstock** | "Inventory Health Check": un especialista analiza tus datos y te presenta resultados en un taller online: exceso, stock obsoleto, riesgo de faltantes | **Gratis**, valuado en GBP 2.500 (Reino Unido) o USD 2.500 (versión NetSuite) | Exige llamada previa de calificación y un ERP conectado (Acumatica, NetSuite o Sage en la promoción del Reino Unido). "Pulls data only from your ERP". Sin obligación de comprar | [S1] |
| **EazyStock** (vía Innovia) | "Free Stock Health Analysis" que muestra el retorno que daría EazyStock | Gratis | Conectores para Microsoft Dynamics Business Central y NAV. No dice qué datos pide | [S2] |
| **Catalant** | "Inventory Optimization Diagnostic" hecho por consultores de su red: análisis de inventario + comparación con el sector + plan | No publica | Casos de empresas grandes (ej.: USD 85 millones de reducción de inventario en una de equipos industriales), según la propia empresa | [S3] |
| **Slimstock** | Software (Slim4) + proyectos | No publica | "1700+ customers", "75 countries", "200+ projects per year", según la propia empresa. Muestra que software y servicio conviven aun a escala | [S6] |
| **Datup** | Pronóstico de demanda y sugerencia de compras con IA "para equipos de Supply Chain en LATAM" | Suscripción mensual, sin precio público | Clientes en Colombia, México, Perú, Honduras, España y Ecuador (Grupo Bimbo, Juan Valdez, Colgate, entre otros, según la propia empresa). **No menciona Argentina** | [S5] |
| Prediko, Inventory Planner, Cogsy, Netstock (software), Cin7 | Software de inventario con IA | Prediko desde USD 49/mes; Netstock desde USD 900/mes | Ya relevados el 2026-10-08 | [R1] |

**Lo que muestran (OPINIÓN):** el diagnóstico se regala para vender otra cosa. Y siempre se hace **conectado al sistema del cliente**, porque así el paso siguiente (la suscripción) es natural. Nadie encontrado cobra por "subí tu Excel una vez".

**En Argentina:**
- **No encontré** consultoras que vendan un diagnóstico de stock con precio y entrega fijos (búsqueda del 2026-10-15). Los resultados fueron trabajos académicos: por ejemplo, un trabajo de campo de la UNT (2025) que propone indicadores de inventario como rotación, días de inventario, antigüedad e inmovilización [S31] (resumen de búsqueda).
- **No encontré** software argentino de sugerencia de compra o reposición con IA para pymes (búsqueda del 2026-10-15). Los sistemas de gestión locales (Tango, Xubio, Contabilium, Colppy) tienen reportes; **no verifiqué** si alguno tiene análisis de stock con IA [R1].
- Para vendedores de Mercado Libre existe Nubimetrics (argentina), que no muestra funciones de stock en su portada [R1].

### 3.2 Estudio de tiempos con video (con o sin IA)

**Afuera:**

| Herramienta | Qué hace | ¿IA automática? | Precio | Clientes / escala | Fuente |
|---|---|---|---|---|---|
| **Squint** — "Lean Manufacturing Agent" | Con un ciclo filmado con celular o cámara, etiqueta cada segundo como valor agregado, necesario o uno de los 7 desperdicios; arma Yamazumi contra el takt y propone cómo rebalancear | **Sí.** El cliente acepta, modifica o rechaza cada cambio | No publica ("Book a demo") | Lanzado el 2026-08-24. Nailor Industries como probador temprano (según Inc., citado por Let's Data Science, 2026-09-11). La nota aclara que **no es una validación independiente** | [S10] |
| **Iteros Lens** | Estudio de tiempos, balanceo de línea y flujo de proceso, en el navegador. "Film the line once, then mark each step on the video" | **No:** el ingeniero marca los pasos a mano. El video queda en la computadora del usuario | **Estudio de tiempos gratis para siempre**; balanceo y flujo, en prueba. No muestra precios de los planes pagos | Fundada en 2026. No da clientes. El fundador viene de "uno de los mayores fabricantes del Reino Unido" | [S11] |
| **Timer Pro** (ACSCO) | Módulo de estudio de tiempos por video "with millisecond accuracy", más "Timer Pro AI" | Parcial (no detalla qué hace la IA) | No publica; prueba gratis de 45 días | "Over 1600 companies worldwide", sobre todo automotriz (según la propia empresa) | [S12] |
| **Drishti** | Cámaras arriba de cada puesto de una línea de armado manual → tiempos de ciclo, cuellos de botella | Sí | No publica | Clientes citados: DENSO, Flex, Ford, Nissan. CB Insights dice que **Apple la compró en septiembre de 2023**: una sola fuente, **NO VERIFICADO** | [S13] (resumen de búsqueda) |
| **Retrocausal** | Asistente con visión por computadora para armado manual; socio de Siemens | Sí | No publica | Sus cifras de mejora no están verificadas | [S13] (resumen de búsqueda) |
| **Invisible AI** | Cámaras con procesamiento local (el video no sale de la planta) | Sí | No publica | Toyota (planta de Indiana), una docena de autopartistas y 4 terminales, según su CEO | [S13] (resumen de búsqueda) |
| **DeepHow + Yazaki** | Captura automática de tiempos de ciclo y clasificación de segmentos de trabajo | Sí | — | Comunicado de prensa del 2026-07-16 | [S14] (resumen de búsqueda) |
| Coats Digital GSD RealMotion; Khenda | Tiempos por video (Coats: confección) | Sí | — | Relevados el 2026-10-01; **no re-verificados hoy** | [R2] |
| Kaizen Copilot; WorkStudy+ | Aparecieron en la búsqueda | — | Un listado de terceros dice USD 59/mes para WorkStudy+, **NO VERIFICADO** | El sitio de Kaizen Copilot no cargó; la página de WorkStudy+ no muestra precio | — |

**OPINIÓN:** la herramienta para medir tiempos sobre un video **ya es gratis** (Iteros). La IA que lo hace sola apunta a plantas grandes (automotriz, alimentos) y viene con plata detrás. El hueco que queda para Facu no es la herramienta: es **el análisis y la propuesta de mejora para la planta chica que no tiene ingeniero**.

**En Argentina:** **no encontré** empresas que vendan estudio de tiempos como servicio (búsqueda del 2026-10-15); aparecieron solo programas de facultades (UNC, "Estudio del Trabajo") y trabajos de grado. Como antecedente, INTI + JICA asistieron a 100 pymes con el programa Kaizen TANGO, con 116 asesores (booklet INTI 2023) [R2]: hay consultores formados en mejora continua, aunque no los encontré vendiendo esto empaquetado.

### 3.3 Productividad de operarios de depósito

**Afuera:**

| Producto | Qué dice que hace | Para quién | Precio | Fuente |
|---|---|---|---|---|
| **Easy Metrics** | Une datos operativos, de mano de obra y financieros; estándares por tarea y pago por desempeño. Se conecta al sistema del depósito (WMS), al ERP y a RR.HH. | "Multi-site warehouse operations" | No publica | Según la propia empresa: "10% Labor Cost Reduction", "10:1 Average ROI", garantía de 4% de ahorro mínimo para empresas que califiquen. Logos: FedEx, Reyes Coca-Cola, McLane, GEODIS, Ferguson, American Tire Distributors [S18] |
| **ProGlove** | Escáner que se usa en la mano + software que convierte movimientos en indicadores de productividad | Grandes (Gap, BMW, DHL, según la empresa) | — | Relevado el 2026-10-13 [R3] |
| **Deposco, Takt.io, Rebus, Manhattan, Blue Yonder, Logiwa** | Gestión de mano de obra de depósito (en inglés, LMS) | De mediano a muy grande. Manhattan y Blue Yonder: implementaciones de varios años | No publican | Lista hecha por Deposco, que es competidor (2026-08-11) [S19] |
| **Blue Yonder, Softeon** | Suscripción por usuario o por sitio + implementación aparte | — | "Custom quoted" | Gartner Peer Insights [S20] (resumen de búsqueda) |

**En Argentina:** **no encontré** proveedores locales de software de productividad de operarios de depósito, ni el 2026-10-13 [R3] ni hoy. Tampoco pude confirmar qué sistemas de depósito (WMS) argentinos traen indicadores por operario.

**OPINIÓN:** este es el módulo más alejado de Facu como "producto". El que paga es un 3PL mediano o grande, que ya compra software global y exige integración con su sistema. Para una pyme sin WMS, medir productividad es trabajo de consultor (planillas y observación), no un producto.

### 3.4 Calculadoras gratis como imán
- Las calculadoras de una sola fórmula ya existen gratis en español (miniwebtool, The Retail Exec) y viven de publicidad [R1].
- **HubSpot Website Grader:** lanzado en febrero de 2007; había analizado "over 1 million" de sitios hacia 2009. HubSpot dice que lo hizo en parte para generar visitas y contactos, pero **no publica cuántos clientes trajo** [S23].
- **Vorne (oee.com):** regala guías y páginas para calcular OEE (indicador de eficiencia de máquinas) y desde ahí ofrece su equipo pago "XL" con prueba de 90 días [S24]. **No hay datos** de cuántas ventas vienen del sitio.
- **Datos de "las calculadoras convierten más":** vienen de empresas que venden calculadoras interactivas (Outgrow) o de agencias: VenturePact +28% de conversión en 2 semanas, BEMO "USD 4 millones en prospectos", "2,3 veces más que el contenido estático" atribuido a Demand Gen Report sin poder ver el estudio original [S22] (resumen de búsqueda). **Conflicto de interés: tomarlo como débil.**

---

## 4. Cómo se construiría y cuánto costaría (ESTIMACIÓN)

### 4.1 Qué parte es software y qué parte es servicio

| Pieza | Software hecho con Claude | Servicio (Facu) |
|---|---|---|
| M1 diagnóstico | Lectura del archivo, fórmulas fijas (ABC, plata parada, cobertura, punto de pedido), informe automático, texto de recomendaciones con IA | Limpiar archivos raros, la llamada 1:1, el plan de compras, la confianza |
| M1 mensual | Recálculo y alertas por mail o WhatsApp | Revisión mensual (al principio) |
| M2 tiempos | Extraer cuadros del video y pedirle a la IA que proponga cortes y clasifique pasos | Validar cada corte, calcular el tiempo estándar, proponer el método mejorado |
| M3 depósito | Leer el registro de movimientos y calcular líneas por hora | Definir estándares, hablar con supervisores y gremio |
| M4 calculadoras | Páginas simples | Escribir el contenido |

### 4.2 Versiones de M1 (escalera de servicio a producto)

| Versión | Qué es | Quién la hace | Tiempo | Costo |
|---|---|---|---|---|
| **V0 a mano** | Plantilla de Excel o Google Sheets con las fórmulas + Claude para limpiar y redactar | Facu | 1 semana para la plantilla; 1–2 h por diagnóstico al principio | USD 0–20 (dominio opcional) |
| **V1 plantilla de autoservicio** | La misma planilla, con instrucciones, para que el cliente pegue sus datos | Facu | +1 semana | USD 0 |
| **V2 web** | Página que lee el archivo **en el navegador del cliente** (los datos no se suben a ningún servidor), aplica las fórmulas y genera el informe | Facu dirigiendo a Claude Code (como hizo con la app de CEMEVA) | 3–6 semanas a tiempo parcial | Dominio ~USD 10–20/año (estimación); hosting en el plan gratis de Cloudflare (dato del repo, no re-verificado hoy) |
| **V3 conectada (software)** | Conexión a Tiendanube, Mercado Libre o el sistema de gestión; recálculo mensual automático | Facu + Claude Code; quizás un programador para las conexiones | 2–4 meses | No lo puedo estimar bien sin saber qué conexiones existen |

**Costo de IA por informe (ESTIMACIÓN):** si la IA solo redacta a partir de un resumen de ~10.000–20.000 tokens (unidades de texto que cobra la IA), con Claude Haiku 4.5 a USD 1 por millón de tokens de entrada [S16] son ~USD 0,01–0,02 de entrada por informe. No verifiqué el precio de salida; aun así, es del orden de centavos.

### 4.3 Costo de M2 con IA (ESTIMACIÓN, con precios de la documentación de Claude)
- Claude no acepta video: hay que sacar cuadros (fotos) del video. Una imagen de 1000×1000 píxeles son 1.296 tokens [S16].
- Un ciclo de 2 minutos a 2 cuadros por segundo = 240 imágenes ≈ 311.000 tokens → **≈ USD 0,31 con Haiku 4.5** o **≈ USD 1,24 con Opus 5.5** (USD 1 y USD 4 por millón de tokens de entrada, según la misma documentación) [S16]. Sin contar la respuesta.
- Límites: hasta 600 imágenes por pedido en la API y 32 MB por pedido [S16]. Hay que achicar las imágenes.
- **El costo no es el problema; la precisión sí** (ver §6.2, pregunta 4).

---

## 5. Regulación y riesgos

### 5.1 Legal
| Tema | Qué dice | Afecta a | Fuente |
|---|---|---|---|
| **Controles al trabajador (Ley de Contrato de Trabajo, arts. 70–72)** | Art. 70: los controles deben salvaguardar la dignidad del trabajador. Art. 71 (texto según Ley 27.322, 2016): los controles "relativos a la actividad del trabajador" deben ser conocidos por él. Art. 72: la autoridad de aplicación puede verificar que no afecten su dignidad de forma manifiesta y discriminatoria | M2 y M3 (filmar y medir operarios) | [S26] |
| **Datos personales (Ley 25.326) y cámaras (Disposición 10/2015 de la Dirección Nacional de Protección de Datos Personales)** | Marco general para filmar y tratar imágenes; carteles que avisen que hay cámaras. Córdoba tiene un protocolo de inspección de cámaras en lugares de trabajo | M2 y M3 | [S27] (resumen de búsqueda; **no abrí el texto de la disposición**) |
| **Filmaciones como prueba** | Los tribunales suelen descartar filmaciones sin certificación de escribano, según abogados consultados por la prensa | M2 (si alguien usa el video contra un operario) | [S27] (resumen de búsqueda) |
| **Gremios** | No encontré conflictos específicos por medir productividad en depósitos. En 2019, la cámara de transporte pidió revisar el convenio de Camioneros (CCT 40/89) "para mejorar la productividad" y el gremio se negó. **No pude confirmar** qué convenio cubre a un operario de depósito de un 3PL | M3 | [S28] (resumen de búsqueda) |
| **Reforma laboral 2026** | Un resumen de búsqueda menciona una Ley 27.802 y un Decreto 407/2026 con artículos suspendidos por un juzgado para el convenio de Camioneros. **NO VERIFICADO**, y no sé si cambia los arts. 70–72 | M2 y M3 | [S28] (resumen de búsqueda) |
| **Datos comerciales del cliente** | Ventas y costos por artículo no son datos personales; **sí lo son** si el archivo trae nombres de clientes personas | M1 | OPINIÓN sobre la Ley 25.326 |
| **Facturar** | Para cobrar hay que estar inscripto (por ejemplo, monotributo). **No verifiqué** categorías ni costos | Todos | — |

### 5.2 Riesgos de negocio
1. **Nadie paga** (F1 débil). Es lo primero que tiene que medir el experimento.
2. **Desconfianza a mandar datos:** Axoft (Tango) dijo ver "resistencia de las pymes a poner su información crítica en la nube" [R1]. Mitigación: procesar en el navegador, aceptar archivos sin descripciones ni nombres de clientes, cláusula de confidencialidad.
3. **Datos sucios:** el stock del sistema no coincide con el físico; códigos que cambian; devoluciones cargadas como ventas negativas; costos viejos (con inflación, el "costo" del sistema puede ser de hace meses). El informe tiene que decir qué supuso.
4. **"Lo hace ChatGPT gratis":** el 51% de los dueños de pymes de EE.UU. ya usa IA para analizar datos (U.S. Bank, 2026) [R1]. La defensa es método + formato + responsabilidad, no la fórmula.
5. **El sistema de gestión lo agrega gratis:** Tango, Tiendanube o Mercado Libre pueden sumar un "informe de stock" el día que quieran.
6. **Credibilidad junior:** sin casos, cuesta. Los primeros 5–10 diagnósticos gratis sirven para conseguir casos.
7. **M2 y M3: competencia con plata** (Squint, Easy Metrics) y **riesgo laboral** (§5.1).
8. **Responsabilidad:** un "comprá X unidades" que sale mal. Siempre como sugerencia, con supuestos escritos.

---

## 6. Respuestas a las dudas de Facu, una por una

### 6.1 Sobre tus comentarios del 2026-10-15

**"Podríamos unirlo con el 1 [piezas por foto / stock]."**
Sí, y es lo que recomiendo (OPINIÓN). El diagnóstico (M1) es la puerta; el orden del depósito y el sistema de piezas son la implementación. Mismo cliente: ferreterías, bulonerías, repuestos. Así la "bolsa top 1" tiene un solo cliente y no cuatro.

**"El Excel debería tener ciertos parámetros y estar armado con ciertos datos."**
Correcto. Son pocos (ver pregunta 2 abajo). La clave es no pedir "tu Excel" sino **una exportación concreta del sistema que ya usan**, y armar una plantilla para el que no tiene sistema.

**"Capaz podría ser parte de nuestra auditoría."**
Sí: es la fase 1 de cualquier auditoría de stock. Netstock hace exactamente eso: un diagnóstico gratis como primer paso [S1].

**"Es algo muy poco escalable, creo yo."**
Tenés razón **en la parte 1:1**. Deja de serlo si se cumplen dos condiciones: (a) que la entrada sea estándar (una exportación conocida, no un Excel distinto por cliente) y (b) que el resultado se use **todos los meses** (punto de pedido, alertas), no una sola vez. Los que cobran por software de inventario cobran por eso, no por el diagnóstico [S1, R1].

**"No sé si se hace mucho."**
Afuera sí, pero como **gancho de venta de software** (Netstock, EazyStock) o como consultoría para empresas grandes (Catalant) [S1–S3]. En Argentina **no encontré** a nadie que lo venda empaquetado, y **no hay datos** de cuánto pagaría una pyme. Puede ser un hueco o puede ser que no se pague: eso lo decide el experimento.

**"Dejalos integrados como servicio, pero dale la vuelta para automatizar y venderlo sin tener que estar atrás."**
La escalera está en §4.2: a mano → plantilla → web → conectado. Lo importante (OPINIÓN): **no saltar a la web antes de hacer 10–20 diagnósticos a mano.** Esos diagnósticos te dicen qué columnas traen de verdad los archivos y qué te piden los dueños.

**Sobre C14: "más de lo mismo, va con ing. ind., ahondemos, metámoslo en la misma bolsa como top 1 para saber dónde entrar."**
Lo metí en la bolsa, pero no coincido en que sea "más de lo mismo". Cambia el cliente (planta, no comercio), la competencia (Squint, Timer Pro, Iteros gratis) y el riesgo (filmar operarios, §5.1). Por eso lo dejo como **segundo módulo, PENDIENTE**. Si M1 funciona con talleres o pequeñas fábricas, M2 se le ofrece a los mismos clientes.

### 6.2 Las 7 preguntas obligatorias

**1. ¿Se hace mucho el diagnóstico de stock en pymes? ¿Quién lo vende y a qué precio?**
- **Argentina:** no encontré oferta empaquetada ni precios. Solo consultores que usan el mensaje del sobrestock (nota paga de Identidad Financiera, sin cifras) [S4] y material académico [S31]. Como referencia de lo que cuesta una hora de servicio profesional: el Consejo de Ciencias Económicas de CABA sugería en octubre de 2024 **$21.975 a $61.530 por hora** para contadores [S29]. Es de hace un año (con inflación de por medio) y es de otra profesión.
- **Afuera:** Netstock (gratis, valuado USD 2.500) [S1], EazyStock (gratis) [S2], Catalant (sin precio) [S3]. Software: Prediko desde USD 49/mes, Netstock desde USD 900/mes [R1]; Datup sin precio público [S5].

**2. ¿Qué columnas necesita el Excel? ¿Los sistemas argentinos las exportan?**

Columnas mínimas (fórmulas estándar de gestión de inventarios; no es un dato de mercado sino el método):

| Tabla | Columnas obligatorias | Opcionales que mejoran el resultado |
|---|---|---|
| Ventas (12 meses, idealmente 24) | Código del artículo · Fecha (o mes) · Cantidad vendida | Precio de venta · Cliente (sin nombre) · Sucursal |
| Stock actual | Código · Cantidad en stock | Ubicación · Fecha de última compra |
| Costos | Código · Costo unitario (mejor el último costo de compra que el histórico) | Proveedor · Plazo de reposición en días · Rubro o familia · Unidad de medida |

Qué necesita cada resultado:
- **ABC:** código + cantidad vendida + precio (o costo, si no hay precio).
- **Plata parada:** stock × costo + fecha de la última venta (sale de la tabla de ventas).
- **Quiebres:** venta promedio por día + stock + plazo de reposición (si falta, se supone uno y se avisa).
- **Punto de pedido y stock de seguridad:** ventas por mes o semana (para medir cuánto varían) + plazo de reposición. Con menos de 6 meses de historia el stock de seguridad no es confiable (OPINIÓN).
- **Margen por producto (L5):** precio + costo.

¿Lo exportan los sistemas?
- **Tango Gestión:** su centro de ayuda muestra exportación a Excel desde "Apertura > Excel > Exportar", pensada para actualizar registros (artículos, precios, pedidos), y una planilla de toma de inventario que trae "su saldo en el sistema" por artículo [S7]. **No pude confirmar** que el informe de ventas por artículo se exporte directo a Excel. Existe un complemento de terceros (TConnector) que lleva reportes de Ventas y Compras de Tango a Google Sheets [S8] (resumen de búsqueda).
- **Tiendanube:** exporta la lista de productos en CSV (**no** en el plan Inicial gratuito) y la lista de ventas en CSV con "el detalle de cada producto vendido por venta" [S9]. **No pude confirmar** si el CSV de productos trae costo y stock como columnas.
- **Mercado Libre, Xubio, Contabilium, Colppy, Bejerman:** **no lo verifiqué en esta sesión.**
- **Ojo:** según el dato de 2016, solo el 18% de las micro usa sistema de gestión [R1]. Muchos van a tener Excel o nada. Para ellos, la plantilla (V1).

**3. ¿Cómo se pasa de servicio a producto? Ejemplos reales.**
- **37signals → Basecamp:** empezó en 1999 como empresa de diseño web; en 2004 lanzó Basecamp, su primer producto; en 2005 dejó el trabajo para clientes y se dedicó solo a sus aplicaciones [S25]. Lección: el producto salió de una herramienta que usaban para su propio servicio.
- **Netstock y EazyStock:** al revés. Son software, pero usan un **diagnóstico hecho por una persona** como puerta de venta [S1, S2]. Lección: el servicio no desaparece, queda como gancho.
- **Slimstock:** software + 200+ proyectos por año + 1.700 clientes (según la propia empresa) [S6]. Lección: a escala, servicio y software conviven.
- **HubSpot Website Grader y Vorne:** herramienta o contenido gratis → producto pago [S23, S24]. No publican conversiones.
- **Lo que intenté verificar y no pude:** que Mailchimp y FreshBooks salieran de una agencia o consultora (se cuenta mucho, pero Wikipedia no lo dice). **No los uso como ejemplo.**
- **Patrón (OPINIÓN):** (1) hacer el servicio a mano con un método fijo, (2) escribir el método como plantilla, (3) automatizar la parte repetida, (4) cobrar por lo que se repite cada mes. El 1:1 queda como servicio premium opcional.

**4. Estudio de tiempos con video e IA: herramientas, Argentina y si es realista con Claude.**
- Herramientas: ver §3.2. En Argentina, no encontré oferta.
- **Claude:** acepta imágenes JPEG, PNG, GIF y WebP; **no video**. Hasta 600 imágenes por pedido por API (100 en modelos de 200.000 tokens de contexto) y 20 por mensaje en claude.ai. Su documentación advierte que la ubicación de cosas en la imagen es "approximate" y que el conteo puede fallar [S16].
- **Gemini:** acepta video. Por defecto toma 1 cuadro por segundo y su documentación dice que "fast action sequences might lose detail due to the 1 FPS sampling rate". Se puede pedir otra frecuencia de cuadros [S17].
- **Evidencia académica:** Gudlin y otros (Applied Sciences, 2024) probaron 27 modelos para cortar en pasos videos de un armado real (9 actividades, 4 personas, 3 productos). Reportan precisión de segmentación, **no error de tiempo contra cronómetro**. Mencionan que analizar video a mano lleva de 2 a 5 horas por hora de filmación [S15] (resumen de búsqueda). **No encontré ningún estudio con el error porcentual de la IA contra un cronometraje.**
- **ESTIMACIÓN de precisión:** a 2 cuadros por segundo, cada corte puede errarle hasta medio segundo. En un paso de 4 segundos, con dos cortes, el error puede llegar a ~25%. Para un estudio de tiempos formal eso no sirve sin revisión.
- **Veredicto (OPINIÓN):** realista como **"IA que propone, ingeniero que valida"**: la IA sugiere dónde empieza y termina cada paso y si es desperdicio; Facu lo corrige en una herramienta como Iteros (gratis, cuadro por cuadro) [S11]. **No realista hoy** como "subís el video y sale el tiempo estándar sin nadie atrás", y menos si el resultado se usa para pagar premios a los operarios.

**5. Productividad de operarios de depósito: productos, Argentina, quién paga.**
- Productos: ver §3.3. Todos para depósitos medianos y grandes, sin precio público, con integración al sistema del depósito.
- Argentina: no encontré proveedores locales. Existe la cámara CEDOL [S21], pero no conseguí cifras del sector.
- Quién paga: el gerente de operaciones del 3PL o centro de distribución [R3].
- **OPINIÓN:** es venta a empresas medianas y grandes, con ciclo largo y riesgo gremial. No encaja con USD 1.300 y con "empezar ya".

**6. ¿Las calculadoras gratis traen clientes?**
- **No encontré un dato confiable.** HubSpot y Vorne las usan, pero no publican resultados [S23, S24]. Las cifras de conversión vienen de quienes venden calculadoras [S22].
- El estudio del 2026-10-08 ya había visto que las calculadoras de una sola fórmula son un commodity y que los resúmenes de IA del buscador les sacan clics [R1].
- Facu no quiere aparecer en redes [perfil en MEMORY.md]; el buscador (SEO) es un canal que no necesita cara, pero tarda meses en rendir [R1].
- **OPINIÓN:** la mejor "calculadora" es **el diagnóstico mismo** (procesa tus datos reales, que ningún resumen de buscador tiene). Las calculadoras sueltas sirven como **material de venta** (un link para mandar en el primer contacto) y como apuesta de buscador a largo plazo, no como fuente de clientes para el primer mes.

**7. Propuesta integrada: ¿puerta de entrada servicio o producto? ¿Cómo se vuelve producto global?**
**OPINIÓN fundada:**
- **Puerta de entrada: servicio estandarizado (M1 a mano), no producto.** Razones: (a) no hay prueba de que alguien pague (F1); (b) no sabemos qué archivos tienen los clientes; (c) afuera, hasta los que venden software usan un diagnóstico humano como gancho [S1, S2].
- **Cliente inicial:** ferreterías, bulonerías y casas de repuestos (mismo cliente que la idea de piezas chicas), más un segundo grupo de prueba de tiendas Tiendanube con 200+ productos (porque su exportación es estándar [S9]).
- **Camino a producto:** a mano (10–20 casos) → plantilla → web que procesa en el navegador → conexión a Tiendanube o al sistema de gestión con recálculo mensual.
- **Global:** las fórmulas son iguales en cualquier país. El primer salto natural es América Latina en español: Tiendanube tiene centros de ayuda para Argentina, Colombia y México (se ve en sus direcciones web [S9]), y Datup muestra que hay empresas pagando por esto en la región [S5]. Pero **global recién después de que funcione en Argentina**; con inglés básico, venderle a EE.UU. hoy es cuesta arriba.
- **M2 (tiempos) y M3 (depósito):** módulos para más adelante, a clientes que ya confíen.

---

## 7. Filtro final

| Filtro | Puntaje (1–5) | Justificación |
|---|---|---|
| **F1. Demanda comprobable en Argentina** | **2** | No encontré oferta local, ni precios, ni encuestas de disposición a pagar. Solo hay señales indirectas: el mensaje del sobrestock [S4] y la cantidad de comercios [R1]. Afuera sí hay demanda comprobada (Netstock, Catalant, Datup), pero en empresas con ERP |
| **F2. Producto automatizable y global** | **3** | Las fórmulas de M1 se automatizan al 100%. Lo difícil es leer archivos desordenados y que el cliente vuelva todos los meses. M2 se automatiza solo en parte (la IA no alcanza la precisión, §6.2-4); M3 depende de integrarse con sistemas ajenos. Hay competidores globales con capital |
| **F3. Validable rápido y barato (30 días, < USD 300)** | **4** | M1 se valida a mano con Excel y Claude por menos de USD 150 (§8). No le pongo 5 porque depende de que Facu consiga 40 contactos en un mes y porque el "sí, pago" puede tardar más de 30 días |
| **F4. Riesgo legal manejable (5 = bajo)** | **4** | M1 tiene riesgo bajo (datos comerciales, con cuidado si hay nombres de clientes). M2 y M3 tienen riesgo medio (arts. 70–72 de la Ley de Contrato de Trabajo, imágenes como datos personales, gremios) [S26–S28]; por eso quedan para después |
| **F5. Encaje con Facu** | **4** | Ingeniería industrial, pasantía de stock en Sporting, ya dirigió una app real con Claude. Encaja con "automatizar procesos como producto". Le resto 1 porque Facu dijo que "no son al 100 mis favoritos" y porque no es tecnología del mundo físico ni una app que une dos partes |
| **Total** | **17/25** | |

### Recomendación: **PRIMERA, con alcance recortado**
- **Entra ya:** solo **M1, diagnóstico de stock**, como servicio a mano, apuntado al cliente de la idea de piezas chicas.
- **Quedan PENDIENTES:** **C14 (estudio de tiempos por video)** y **LOG-3-4 (productividad de depósito)**. Motivos: otro cliente, competencia con capital, riesgo laboral y, en LOG-3-4, venta a empresas grandes.
- **M4 (calculadoras):** no como negocio; como material de venta del M1, si sobra tiempo.
- **Por qué "primera" con un F1 de 2:** porque es la duda más barata de despejar de toda la bolsa. Con F3 alto y F1 desconocido, conviene medir antes de seguir discutiendo. Si el experimento da mal, se corta con poca pérdida y queda el aprendizaje (qué datos tienen de verdad los comercios), que sirve igual para la idea de piezas chicas.

---

## 8. Primer experimento concreto

**Qué:** "Diagnóstico de stock gratis en 48 horas", hecho a mano (V0). A cambio, el comercio manda su exportación de ventas, stock y costos. Después se ofrece un plan de acción pago.

**Con quién (dos grupos, 20 contactos cada uno):**
- **Grupo A — ferreterías, bulonerías, casas de repuestos:** visitas en persona en tu zona, con una hoja impresa que muestre un ejemplo de diagnóstico (armado con datos de ejemplo, **marcados claramente como ejemplo**); contactos de la red de CEMEVA, de Sporting y de la facultad; la cámara de ferreteros de tu zona (no verifiqué cuál es).
- **Grupo B — tiendas Tiendanube con 200+ productos:** grupos de vendedores en Facebook y WhatsApp, y mensaje directo a tiendas que se encuentren buscando en Google o en redes.

**Cómo, semana a semana (si arranca el 2026-10-20, el corte es el 2026-11-19):**
1. **Semana 1:** armar la plantilla con las fórmulas (ABC, plata parada, cobertura, punto de pedido, margen) y la hoja con la lista de columnas (§6.2-2). Probarla con datos de ejemplo. Escribir una cláusula de confidencialidad de un párrafo.
2. **Semanas 1–2:** los 40 contactos. Pedir **la exportación del sistema que ya usan**, no "un Excel". Aceptar archivos sin descripciones ni nombres de clientes.
3. **Semanas 2–3:** hacer cada diagnóstico, entregarlo en 2 páginas y tener una llamada o visita de 30 minutos.
4. **Semanas 3–4:** en esa llamada, ofrecer el plan de acción pago. Probar dos precios: ARS 60.000 a la mitad de los casos y ARS 150.000 a la otra mitad (≈ USD 39 y 98 al oficial del 2026-10-15 [S30]).

**Qué anotar en cada caso:** sistema que usa (Tango, Tiendanube, Excel, nada); si trajo las 3 columnas mínimas; minutos que llevó limpiar el archivo; plata parada encontrada; si el dueño se sorprendió (textual); objeciones textuales; si pagó y cuánto.

**Costo:** USD 0–150 (impresiones, viajes, dominio opcional). **Días:** 30.

**Número para "seguir":** de 40 contactos, **10 o más mandan su archivo**, y **2 o más pagan** el plan de acción (cualquiera de los dos precios). Además, mirar los minutos de limpieza: si el promedio es de más de 60 minutos por archivo, la automatización va a ser difícil (dato para la V2, no para cortar).

**Número para "cortar":** **menos de 5 archivos** de 40 contactos, **o** ningún pago después de 8 diagnósticos entregados. En ese caso: post-mortem escrito y se pasa a la siguiente idea de la lista.

**Pérdida máxima:** USD 150 y unas 50 horas de Facu.

**Lo que se aprende aunque falle:** qué datos tienen de verdad los comercios, en qué formato, y qué les duele. Es materia prima directa para la idea de piezas chicas y para la etapa 2.

**5 preguntas al estilo The Mom Test** (preguntan por lo que pasó, no por lo que harían; no mencionan la solución):
1. "¿Cuándo fue la última vez que un cliente te pidió algo y no lo tenías? ¿Qué hiciste?"
2. "¿Cómo decidiste lo que compraste la última vez? ¿Me mostrás cómo lo hiciste?"
3. "¿Tenés idea de cuánta mercadería tenés que no se movió en los últimos seis meses? ¿Cómo lo sabés?"
4. "¿Alguna vez le pagaste a alguien (contador, consultor, sistema) para ordenar el stock o las compras? ¿Cuánto pagaste y qué pasó?"
5. "¿Con qué sistema facturás? ¿Qué reportes sacás de ahí y cada cuánto? ¿Me mostrás el último?"

---

## 9. Fuentes

**[abierta]** = abrí la página el 2026-10-15. **[resumen de búsqueda]** = lo vi en el resultado del buscador sin abrir la página. Al lado, la fecha de publicación si se conoce.

- **[S1]** Netstock, "Inventory Health Check" [abierta]: https://www.netstock.com/inventory-health-check/ · versión de contenido: https://content.netstock.com/inventory-health-check
- **[S2]** Innovia, ficha de EazyStock ("Free Stock Health Analysis") [abierta]: https://www.innovia.com/isv-listing/eazystock
- **[S3]** Catalant, "Inventory Optimization Diagnostic" [abierta]: https://catalant.com/capability/inventory-optimization-diagnostic
- **[S4]** Revista Noticias (Perfil), espacio no editorial de Identidad Financiera, "Gestión de stock en pymes: un nuevo escenario exige eficiencia", 2025-10-15 [abierta]: https://noticias.perfil.com/noticias/espacio-no-editorial/gestion-de-stock-en-pymes-un-nuevo-escenario-exige-eficiencia.phtml
- **[S5]** Datup, portada [abierta]: https://www.datup.ai
- **[S6]** Slimstock, "About us" [abierta]: https://www.slimstock.com/about-us/
- **[S7]** Centro de Ayudas Axoft Tango: búsqueda "exportar excel" [abierta]: https://ayudas.axoft.com/26ar/?s=exportar+excel · "Exportación a Excel" [abierta]: https://ayudas.axoft.com/26ar/documentos/operacion/apertura_oper/excel_oper/excel_export_oper/ · "Toma de inventario masiva" (visto en la búsqueda del sitio): https://ayudas.axoft.com/26ar/ayudas/st/movimiento_carp_st/actstcolectora_carp_st/ajusteinventariocolectora_st/
- **[S8]** Google Workspace Marketplace, TConnector (conector Tango → Google Sheets, de terceros) [resumen de búsqueda]: https://workspace.google.com/marketplace/app/tconnector/1098297288560
- **[S9]** Tiendanube, "¿Cómo descargar la lista de productos?" [abierta]: https://ayuda.tiendanube.com/es_AR/como-descargar-la-lista-de-productos-de-mi-tiendanube · "¿Cómo exportar mi lista de ventas?" [abierta]: https://ayuda.tiendanube.com/es_AR/123338-exportar-lista-de-ventas/como-exportar-mi-lista-de-ventas · versiones para Colombia y México [resumen de búsqueda]: https://ayuda.tiendanube.com/es_CO/123338-exportar-lista-de-ventas/como-exportar-mi-lista-de-ventas · https://ayuda.tiendanube.com/es_MX/123338-exportar-lista-de-ventas/como-exportar-mi-lista-de-ventas
- **[S10]** Squint, portada [abierta]: https://www.squint.ai · Let's Data Science, "Squint applies video AI to factory workflows", 2026-09-11 [abierta]: https://letsdatascience.com/news/squint-applies-video-ai-to-factory-workflows-d66cd756
- **[S11]** Iteros, portada [abierta]: https://iteros.io · StartupHub, ficha de Iteros [abierta]: https://www.startuphub.ai/startups/iteros
- **[S12]** ACSCO, Timer Pro [abierta]: https://www.acsco.com/
- **[S13]** CB Insights, Drishti Technologies [resumen de búsqueda]: https://www.cbinsights.com/company/drishti-technologies · Siemens, blog de socios (Retrocausal) [resumen de búsqueda]: https://blogs.sw.siemens.com/partners/?p=1503 · Fox News, Invisible AI [resumen de búsqueda]: https://www.foxnews.com/auto/invisible-ais-intelligent-agent-cameras-see-autoworkers-machines-wrong.amp
- **[S14]** Business Wire, "DeepHow and Yazaki North America Drive Physical AI…", 2026-07-16 [resumen de búsqueda]: https://www.businesswire.com/news/home/20260716662554/en/ · Tech Mahindra, caso LineSense [resumen de búsqueda]: https://files.techmahindra.com/static/img/pdf/linesense-case-study.pdf
- **[S15]** Gudlin y otros, Applied Sciences 14(3):1185, 2024 [resumen de búsqueda; la página dio error 403]: https://www.mdpi.com/2076-3417/14/3/1185
- **[S16]** Documentación de Claude, "Vision" [abierta]: https://platform.claude.com/docs/en/build-with-claude/vision
- **[S17]** Documentación oficial de la API de Gemini, guía "Video understanding", secciones "Technical details about videos" y "Customize video processing" (consultada el 2026-10-15 con el buscador oficial de documentación de Gemini; no anoto la dirección web pública porque no la abrí)
- **[S18]** Easy Metrics, portada [abierta]: https://easymetrics.com/
- **[S19]** Deposco, "Easy Metrics LMS alternatives", 2026-08-11 (es competidor) [abierta]: https://deposco.com/blog/easymetrics-lms-alternatives/
- **[S20]** Gartner Peer Insights, Blue Yonder Warehouse Labor Management y Softeon [resumen de búsqueda]: https://www.gartner.com/reviews/product/blue-yonder-warehouse-labor-management · https://www.gartner.com/reviews/product/softeon-warehouse-labor-management
- **[S21]** CEDOL, portada [abierta]: https://www.cedol.org.ar/
- **[S22]** Outgrow, blog sobre calculadoras (vende calculadoras) [resumen de búsqueda]: https://outgrow.co/blog/interactive-calculators-lead-generation-conversion · Hauer Power (agencia) [resumen de búsqueda]: https://www.hauerpower.com/en/insights-posts/website-calculator-lead-generation
- **[S23]** HubSpot Blog, "Website Grader Evaluates Over 1 Million URLs", c. 2009 [abierta]: https://www.hubspot.com/blog/bid/4834/Website-Grader-Evaluates-Over-1-Million-URLs
- **[S24]** OEE.com (Vorne) [abierta]: https://www.oee.com/
- **[S25]** Wikipedia, "37signals" [abierta]: https://en.wikipedia.org/wiki/37signals · también abiertas, sin respaldo para el relato agencia → producto: https://en.wikipedia.org/wiki/Mailchimp · https://en.wikipedia.org/wiki/FreshBooks
- **[S26]** Infoleg, Ley 20.744 de Contrato de Trabajo, texto actualizado (arts. 70–72; art. 71 sustituido por Ley 27.322) [abierta]: https://servicios.infoleg.gob.ar/infolegInternet/anexos/25000-29999/25552/texact.htm
- **[S27]** Ministerio de Trabajo de Córdoba, resolución y anexo sobre cámaras de seguridad (2023) [resumen de búsqueda]: https://trabajo.cba.gov.ar/wp-content/uploads/2023/02/CONCURSOS-2023-RESOLUCION-CAMARAS-DE-SEGURIDAD.pdf · iProfesional, requisitos de las filmaciones como prueba [resumen de búsqueda]: https://www.iprofesional.com/notas/125705-Qu-requisitos-deben-cumplir-las-filmaciones-para-servir-como-prueba-en-un-juicio-laboral
- **[S28]** Blog del Contador, CCT 40/89 [resumen de búsqueda]: https://siap.blogdelcontador.com.ar/numero_convenio/40-89/ · BAE Negocios, paritaria de Camioneros 2019 [resumen de búsqueda]: https://www.baenegocios.com/amp/Camioneros-advierte-que-habra-conflicto-si-no-homologan-su-acuerdo-paritario-20190702-0077/
- **[S29]** Contadores en Red, honorarios sugeridos por jurisdicción, 2024-10-29 [abierta]: https://contadoresenred.com/honorarios-profesionales-cuanto-vale-la-hora-de-un-contador-publico-comparativo-por-jurisdiccion-y-encuesta/
- **[S30]** DolarHoy, cotizaciones del 2026-10-15 a las 12:07 [abierta]: https://dolarhoy.com/
- **[S31]** UNT, Facultad de Ciencias Económicas, trabajo de campo 2025 (indicadores de inventario) [resumen de búsqueda]: https://face.unt.edu.ar/web/iadmin/wp-content/uploads/sites/2/2026/02/47-Zelarayan-Evelyn-Nicolle-Trabajo-Campo-2025_compressed.pdf

**Documentos del repo (datos no re-verificados hoy):**
- **[R1]** `research/fuentes/2026-10-08-L5-L9-herramientas-analisis.md` (Prediko, Netstock, Contabilium, CESSI 2016, MiPyME 2023, Tango, adopción de IA, U.S. Bank, Nubimetrics, Axoft y la nube, calculadoras gratis, AI Overviews).
- **[R2]** `research/fuentes/2026-10-01-ideas-ingenieria-industrial-ops.md` (Coats GSD RealMotion, Khenda, INTI Kaizen TANGO, capacidad instalada UIA).
- **[R3]** `research/datos/2026-10-13-nichos/03-logistica.json`, problema LOG-3-4 (Easy Metrics, ProGlove, sin presencia en Argentina).

**Búsquedas sin resultado útil (para no repetirlas):** consultoras argentinas de diagnóstico de stock; software argentino de reposición con IA; consultoras argentinas de estudio de tiempos; WMS argentinos con productividad por operario; honorarios sugeridos para ingenieros industriales en 2026; error porcentual de la IA contra el cronómetro en estudios de tiempos.
