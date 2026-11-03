# EDU-5-3: app de profesores particulares como comisionista (indagación a fondo)

- **Fecha:** 2026-10-15
- **Para qué sirve:** decidir si EDU-5-3 va a "primeras" (para arrancar) o a "pendientes".
- **Convención (Regla N.º 1):** **DATO** = verificado, con fuente y fecha. **ESTIMACIÓN** = cálculo o supuesto mío, con el razonamiento. **OPINIÓN** = juicio mío. "No verificado" = no lo pude confirmar.
- **Límites de esta indagación (aviso honesto):**
  - Usé las 15 búsquedas web permitidas y unas 40 lecturas de páginas.
  - Me **bloquearon la lectura** (error 403) superprof.com.ar, tuquejasuma.com y las páginas de costos de Mercado Pago. Lo de esas fuentes sale de resúmenes del buscador o de fuentes secundarias, y está marcado.
  - **No encontré** datos de Argentina sobre cuántos alumnos toman clases particulares ni sobre cuánta plata pierden los profes por cancelaciones. Lo que hay en esos puntos son **estimaciones mías**.
  - No soy abogado ni contador. Las partes legales citan la norma oficial cuando pude abrirla. Lo demás es una lista de preguntas para un profesional.

---

## 1. Qué es exactamente

### 1.1 El problema (dos caras)

| Quién | Qué le duele | Qué tan comprobado está |
|---|---|---|
| **Alumno o padre** | Encontrar un profe bueno y confiable. No saber si va a venir. Pagar y que la clase salga mal. Si el alumno es menor, la seguridad. | **DATO parcial:** las quejas públicas contra Superprof hablan de profes que no responden, perfiles falsos y cobros de suscripción que no se esperaban (ver 3.2). |
| **Profesor** | Conseguir alumnos. Cancelaciones a último momento y alumnos que no vienen. Cobros atrasados. Organizar la agenda por WhatsApp. | **No verificado con datos de Argentina.** No encontré ninguna encuesta seria a profes particulares con tasas de cancelación o de plata perdida (ver 2.3). |

### 1.2 Quién paga

- **El alumno o el padre paga la clase.** Esto ya pasa hoy, con efectivo o transferencia.
- **La plataforma cobra una parte.** Hay tres formas, y las tres existen afuera:
  1. **Comisión por clase**, que se descuenta del pago al profe. Es lo que hacen Preply y Classgap (ver 3.1).
  2. **Suscripción del alumno para contactar profes.** Es lo que hace Superprof en Argentina.
  3. **Abono mensual del lado que ofrece** (el profe o la academia). Es lo que hace ATC con los clubes. Ojo: es el ejemplo que vos diste (ver 3.3).
- **Después:** publicidad (profes que pagan por aparecer primero) y suscripciones "Pro".

### 1.3 Qué hace la app: tu idea ordenada en módulos

Esto es tu pedido del 2026-10-14 bajado a piezas concretas. Al lado va qué hace quien ya lo tiene.

| Módulo | Qué hace | Quién lo hace afuera (DATO) |
|---|---|---|
| **Perfil verificado del profe** | DNI, foto, materias, precio, zona, modalidad (online, en casa, en un lugar público). Certificado de antecedentes penales para quien da clase a menores. | El certificado lo saca el propio profe online, entre $1.000 y $8.500 según la urgencia ([argentina.gob.ar](https://www.argentina.gob.ar/justicia/reincidencia/antecedentespenales), consulta 2026-10-15). |
| **Buscador** | Por materia, zona, precio, horario y puntaje. | Superprof, TusClasesParticulares, Classgap. |
| **Agenda y reserva** | El alumno elige un horario libre. El profe acepta o rechaza. Recordatorios automáticos. | TutorBird, TutorCruncher (software de gestión). |
| **Pago protegido** ("la app retiene hasta que la clase se da por concluida") | El alumno paga o deja la tarjeta en garantía al reservar. La plata **no pasa por la cuenta de la plataforma**. Ver 5.3. | Preply: la clase se confirma sola 72 h después si el alumno no la confirma antes (fuera de su aula virtual). Classgap: el profe cobra después de la clase. ATC: "tarjeta en garantía". |
| **Cierre y calificación** | Las dos partes confirman que la clase se dio. Si nadie dice nada, se confirma sola en un plazo fijo. Recién ahí se libera o se cobra. | Preply: confirmación automática ([Preply, consulta 2026-10-15](https://help.preply.com/en/articles/4171348-when-and-how-you-get-paid-for-lessons)). |
| **Política de cancelación** | Si el alumno cancela tarde o no viene, el profe cobra igual (todo o una parte). Si el profe no viene, se le devuelve todo al alumno. | Classgap: devolución total si el profe no aparece o si se cancela con 8 h o más de anticipación ([Classgap](https://www.classgap.com/en/info/bookings)). |
| **Reseñas y puntaje** | Solo de clases pagadas por la app, para que no haya reseñas falsas. | Todos los grandes. |
| **Chat interno** | Para coordinar sin pasarse el teléfono. | La investigación académica muestra que tener canal propio baja la "fuga" por fuera (ver 6.6). |
| **Bonos y paquetes** | Paquetes de 4 u 8 clases con el mismo profe, con descuento. | Classgap: packs de clases, 3% de ahorro en la renovación. |
| **Seguridad** | Antecedentes, reseñas, botón de denuncia. Si el alumno es menor, la cuenta es del padre. | Ver 5.4. |
| **"Instagram de profesores"** | Perfil con videos cortos y publicaciones del profe. | **OPINIÓN:** sirve como vidriera y para atraer gente. Pero una red social es otro negocio, más difícil. No lo pondría en la primera versión (ver 6.5). |
| **Publicidad y "Pro"** | El profe paga para aparecer primero o para tener herramientas extra. | Superprof tiene un servicio "Premium" para profes ([blog de Superprof México, 2026-05-14](https://www.superprof.mx/blog/profesores-particulares-superprof/)). |

### 1.4 Cómo entra la plata: cuenta de ejemplo (ESTIMACIÓN)

**Supuestos:**
- Clase de **ARS 40.000**: es un punto medio entre los valores base de $30.000 (estudiante universitario) y $45.000 (licenciado) de Cuánto Me Cuesta, de abril de 2026. Con la inflación desde entonces, hoy puede ser más.
- Comisión de la plataforma: **15%**.
- Costo de Mercado Pago con tarjeta de crédito y plata al instante: **6,49% + IVA (≈ 7,85%)**. **Es un dato de agosto de 2023** ([iProfesional, 2023-08-01](https://www.iprofesional.com/tecnologia/386153-mercado-pago-que-debes-saber-sobre-comisiones-plazos-y-montos)). La tarifa de hoy no la pude verificar (la página de costos de Mercado Pago me bloqueó).
- Tipo de cambio: unos ARS 1.500 por dólar, el que usa Cuánto Me Cuesta en abril de 2026. **No verifiqué el de hoy.**

| Concepto | ARS | Comentario |
|---|---|---|
| Paga el alumno | 40.000 | |
| Costo de Mercado Pago (crédito, al instante) | −3.140 | Con "dinero en cuenta" sería mucho menos: 0,8% + IVA (dato de 2023) |
| Comisión de la plataforma (15%) | −6.000 | ≈ USD 4 por clase |
| **Recibe el profe** | **≈ 30.860 (77%)** | Hoy, con transferencia o efectivo, recibe el 100% |

**Lo que tiene que pasar para que te sirva (ESTIMACIÓN):**
- Ganar **USD 1.000 por mes** exige unas **250 clases por mes** pagadas por la app, sin fuga. Por ejemplo, 60 alumnos con 1 clase por semana.
- Ganar **USD 5.000 por mes** exige unas **1.250 clases por mes**.

**OPINIÓN:** el profe pierde cerca de un cuarto de lo que cobra. Para que siga usando la app, tiene que recibir algo que valga más que eso: alumnos nuevos, cobro seguro y cero ausencias sin pagar. Si no, a la segunda clase se arregla por WhatsApp. Es **el** riesgo central (ver 6.6).

---

## 2. Mercado en Argentina

### 2.1 Datos verificados

| Dato | Valor | Fuente |
|---|---|---|
| Alumnos de secundaria (2024) | **4.062.601** | Anuario Estadístico 2024 del Ministerio de Capital Humano, citado por [Tiempo Argentino](https://www.tiempoar.com.ar/ta_article/caida-de-la-matricula-colegios-primaria-y-secundaria-argentina/). **Fuente secundaria:** no abrí el anuario. |
| Alumnos de primaria (2024) | **4.723.730** | Misma nota |
| Total de alumnos de todos los niveles antes de la universidad (2024) | **11.349.861** | Misma nota |
| Precio por hora (abril 2026, Buenos Aires) | Estudiante universitario: $15.000-40.000. Licenciado: $25.000-60.000. Con maestría: $50.000-120.000. Online: −15%. Interior: −25%. | [Cuánto Me Cuesta](https://cuantomecuesta.com/ar/clases-particulares/), consulta 2026-10-15 |
| Profes de Superprof en Argentina | **100.000**, "según la propia empresa". El dato es de **2019**. Llegó al país a fines de 2017. | [InfoNegocios, 2019-04-09](https://infonegocios.info/plus/superprof-profes-para-todo-en-un-solo-lugar-clases-de-cocina-portugues-canto-tenis-y-mas) |

**Ojo con el dato de precios que ya teníamos ("$45.000-120.000 por hora"):**
- Aparece como "rango mediano para secundaria y CBC" en el resumen del buscador de esa misma página.
- Pero la página **tiene contradicciones internas**. Por ejemplo, el promedio del licenciado figura como $60.000 en un lado y como $45.000 en la calculadora.
- Además **no explica cómo junta los datos**. Lo tomo como referencia gruesa, no como dato firme.

### 2.2 Tamaño del mercado (ESTIMACIÓN, sin dato oficial)

**No encontré** ninguna encuesta argentina que diga qué porcentaje de alumnos toma clases particulares. Busqué en informes del Ministerio ("La voz de los estudiantes 2022") y en Argentinos por la Educación, y no está. Hago un cálculo solo con secundaria y con supuestos explícitos:

| Escenario | % de alumnos de secundaria que toma clases en el año (supuesto) | Horas por año por alumno (supuesto) | Precio por hora (supuesto) | Gasto anual |
|---|---|---|---|---|
| Bajo | 10% | 10 | ARS 30.000 | ≈ ARS 122.000 M ≈ **USD 81 M** |
| Medio | 15% | 15 | ARS 40.000 | ≈ ARS 366.000 M ≈ **USD 244 M** |
| Alto | 25% | 20 | ARS 45.000 | ≈ ARS 914.000 M ≈ **USD 609 M** |

- **No incluye** primaria, universidad (ingresos, CBC, finales), idiomas, música ni adultos. Con todo eso, el total sería mayor.
- **OPINIÓN:** es un mercado de **cientos de millones de dólares por año**, pero **casi todo informal** (efectivo o transferencia, sin factura). Una plataforma nueva capturaría una parte chica. Con 15% de comisión sobre el 1% del escenario medio, serían unos USD 370.000 por año de ingresos. Es un negocio, pero no "algo grande" en Argentina sola.

### 2.3 Cuánto se pierde por cancelaciones y falta de pago

- **No lo pude verificar.** No hay encuestas serias a profes particulares, ni en Argentina ni afuera.
- Lo único que encontré es una cifra de una empresa que **vende software de recordatorios**: dice que "una de cada cinco" sesiones de tutoría termina en ausencia. No dice cómo lo midió y tiene interés en que el número sea alto ([Appointment Reminder](https://appointmentreminder.com/industries/education)). **No la uso como dato.**
- ATC dice, en su folleto de mayo de 2025, que en Latinoamérica "120 millones se pierden cada año por ausencias, superposiciones de turnos y cancelaciones" en canchas. **Según la propia empresa**, sin moneda clara ni método.
- **OPINIÓN:** este dolor hay que **medirlo vos** en las entrevistas (ver 8). Si los profes no recuerdan plata concreta perdida el último mes, el problema es más chico de lo que parece.

---

## 3. Qué existe (verificado)

### 3.1 Afuera

| Empresa | Qué hace | Cómo cobra (DATO) | Presencia en Argentina | Fuente |
|---|---|---|---|---|
| **Preply** | Clases online, sobre todo de idiomas | La **primera clase** de cada alumno nuevo se la queda **100%** Preply. Después cobra **entre 18% y 33%** según las horas que dio el profe. La clase se confirma sola ~15 min después en su aula virtual, o 72 h después fuera de ella. Recién ahí la plata pasa al saldo del profe. | Online. Funciona en todo el mundo (no verifiqué cifras de Argentina). | [Centro de ayuda de Preply](https://help.preply.com/en/articles/4171348-when-and-how-you-get-paid-for-lessons); [Sacra](https://sacra.com/research/preply) |
| | Escala | Más de 100.000 profes. Ingresos de **USD 50 M en 2021 (estimación de Sacra)**. Serie D de **USD 150 M en enero de 2026**, con valuación de USD 1.200 M (según Sacra). Más de USD 299 M levantados en total. | | [Sacra](https://sacra.com/research/preply) |
| **Classgap** (España) | Clases online, de los creadores de TusClasesParticulares | **10%** si el alumno llega por el link propio del profe. Si llega por Classgap: **25-30% la primera clase**, que baja a **10-15%** con más clases. Mínimo 1,25 € por hora. Paga a fin de mes (con un mínimo de 50 €). Devolución total si el profe no viene, si se cancela con 8 h de anticipación, o si el alumno no queda conforme dentro de las 24 h de la primera clase. | Online, en todo el mundo. Cuántos profes o alumnos de Argentina tiene: **no verificado**. | [Classgap, reservas](https://www.classgap.com/en/info/bookings). La tabla no aclara qué columna es de qué tipo de profe. |
| **TusClasesParticulares** (España, desde 2007) | Avisos de profes | Gratis para que el profe publique. Dice tener 4,09 M de avisos y 500.000 profes (**según la propia empresa**). | **No opera en Argentina**: su lista de países no la incluye. | [tusclasesparticulares.com](https://www.tusclasesparticulares.com/), consulta 2026-10-15 |
| **TutorBird** (Canadá) / **TutorCruncher** (Reino Unido) | Software de gestión para profes y agencias: agenda, facturación y cobro | Abono mensual (SaaS) | No verificado | Ficha del proyecto del 2026-10-13 (verificada en sus sitios ese día) |

### 3.2 En Argentina

| Empresa | Qué hace | Cómo cobra | Quejas y problemas | Fuente |
|---|---|---|---|---|
| **Superprof** (Francia, en Argentina desde fines de 2017) | El directorio de profes más grande | **El alumno paga el "Pase Alumno"**: una suscripción de 30 días que se renueva sola y le permite contactar a todos los profes. La clase se le paga aparte al profe. **El precio actual en pesos no lo pude verificar.** En México, si el profe no tiene "Premium", Superprof cobra **10%** sobre las clases pagadas por la plataforma. | En tuquejasuma.com: cobros recurrentes después de dar de baja, gente que no sabía que era mensual, problemas para cancelar. Un usuario dice que pagó 4 meses por usarlo una vez. Las respuestas de la empresa dicen que la renovación se avisa. | Resumen del buscador de [tuquejasuma.com](https://tuquejasuma.com/superprof-argentina) (**no pude abrir la página: 403**); [blog Superprof México](https://www.superprof.mx/blog/profesores-particulares-superprof/) |
| | | | Trustpilot (página "superprof.com.ar"): **3,9/5 con 51.553 reseñas**, 12% de 1 estrella. **Ojo:** las reseñas recientes hablan en libras y dólares, así que la página parece juntar varios países. | [Trustpilot](https://www.trustpilot.com/review/superprof.com.ar), consulta 2026-10-15 |
| **Busca Tu Clase** | Avisos clasificados de clases. Reseñas de alumnos. | No menciona cobro propio | Sin datos | [iProfesional](https://www.iprofesional.com/actualidad/219742-lanzan-sitio-para-buscar-clases-de-profesores-de-idiomas-y-computacion) (la fecha real de la nota no la pude ver; parece vieja) |
| **Profes independientes** | Instagram, grupos de Facebook y WhatsApp, boca en boca | Efectivo o transferencia | Es el competidor real (OPINIÓN) | — |

- **No encontré** una app argentina que junte buscador + reserva + cobro dentro de la app + reseñas para clases particulares. Busqué "Tutorea" y "Profe en Casa", que Cuánto Me Cuesta nombra como fuentes, y no aparecieron.
- **OPINIÓN:** que no haya nadie puede ser **un hueco** o puede ser **una señal** de que el modelo no cierra acá (ticket chico, informalidad, fuga). No tengo cómo distinguirlo sin probar.

**Relacionadas en el registro de ideas (Regla N.º 2):** DEP-5-4 (profe de deporte confiable cerca), DEP-5-1 (entrenadores) y EDU-2-1 (academias). Comparten el cliente. Si EDU-5-3 avanza, se pueden sumar como verticales, no como ideas nuevas.

### 3.3 ATC (Alquila Tu Cancha): tu ejemplo, verificado

| Qué | DATO | Fuente |
|---|---|---|
| Qué es | App para reservar canchas + **software de gestión para clubes** (turnos, caja, stock, reportes) | [Forbes Argentina, 2023-06-26](https://www.forbesargentina.com/negocios/crearon-una-app-alquilar-canchas-tienen-mas-350-clubes-200-mil-usuarios-pico-monaco-como-inversor-n36054); [atcsports.io](https://atcsports.io/) |
| **Cómo cobra hoy** | **Abono mensual al club: USD 50 (1-3 canchas), USD 80 (4-6) o USD 100 (7 o más).** Con descuento si se paga por año. Su página dice: "El único costo de ATC es el abono mensual". | [atcsports.io/software-gestion-deportiva](https://atcsports.io/software-gestion-deportiva), consulta 2026-10-15 |
| Lo que dice su folleto (mayo 2025) | Cuatro fuentes de ingreso: SaaS mensual, **comisión por transacciones online**, publicidad (ATC Ads) y servicios premium (torneos, tiendas, cobro en el local) | [One-pager ATC, mayo 2025, publicado en cancilleria.gob.ar](https://www.cancilleria.gob.ar/userfiles/ut/2025-05_-_one_pager_atc.pdf) |
| Cómo evita el "no vino" | **"Tarjeta en garantía":** el jugador deja la tarjeta y solo se le cobra si no se presenta o cancela fuera de plazo. Si cumple, paga el turno en el club. | [atcsports.io](https://atcsports.io/) |
| Tracción 2023 | 200.000 usuarios, 350 clubes, 40.000 reservas en enero, 7 países (**según la empresa**, vía Forbes) | Forbes, 2023-06-26 |
| Tracción 2025 | Más de 700 clubes en 9 países, más de 3.000 canchas, más de 800.000 usuarios registrados y 120.000 reservas por mes (**según la propia empresa**) | One-pager, mayo 2025 |
| Plata e historia | La idea es de 2014 según el fundador (2017 según otra nota). Fondo semilla público en 2016-2017. ~USD 135.000 en 2021-2022 (Pico Mónaco, Start-Up Chile, 500) + USD 270.000 en marzo de 2023. | Forbes, 2023-06-26 |

**ESTIMACIÓN (muy gruesa):** si los 700 clubes pagaran entre USD 40 y 100 por mes, ATC facturaría por abonos entre **USD 0,3 M y 0,8 M por año**. No sé cuántos pagan ni a qué precio.

**OPINIÓN, y es importante:** **ATC no es principalmente un comisionista.** Es software que paga el club (el lado que ofrece) más una app gratis para los jugadores. Y tardó entre 8 y 11 años, con inversión, en llegar a 700 clubes. Copiar ATC en clases particulares sería **"software para profes y academias + vidriera para alumnos"**, no "comisión por cada clase".

---

## 4. Cómo se construiría y cuánto costaría (ESTIMACIÓN)

### 4.1 Por etapas

| Etapa | Qué es | Cómo se hace | Costo en plata (ESTIMACIÓN) | Tiempo de Facu (ESTIMACIÓN) |
|---|---|---|---|---|
| **0. Prueba a mano ("concierge")** | Sin app. Vos hacés de plataforma: recibís pedidos, armás la cita y das seguimiento. | Landing gratis (Cloudflare Pages, que ya usás), formulario, grupo de WhatsApp Business, link de pago de Mercado Pago **del propio profe**. | USD 0-250 (dominio, algo de publicidad, carteles con QR) | 40-60 h en 30 días |
| **1. App mínima** | Web que se usa desde el celular: perfiles, búsqueda, agenda, cobro con split de Mercado Pago, confirmación y reseñas | Construida con Claude Code, como hiciste con CEMEVA. Es más difícil que CEMEVA porque tiene pagos, usuarios externos y seguridad. | Hosting y base de datos: USD 0-50/mes. Dominio: USD 10-20/año. Abogado para términos y condiciones: USD 200-600 (**sin fuente, orden de magnitud**). Monotributo categoría A: $49.527/mes (DATO, ARCA, vigente desde 2026-08-01). | 150-300 h (6-12 semanas a medio tiempo) |
| **2. App completa** | Apps de celular, chat interno, paquetes, panel para padres, publicidad | Equipo o socio técnico | USD 5.000-20.000+ (**sin fuente**) | — |

### 4.2 Lo técnico que ya está verificado (Mercado Pago)

- **Split de Pagos 1:1 (marketplace):** Argentina figura como país disponible. Está pensado para "servicios de PSP a vendedores en modelos de marketplace" ([Mercado Pago Developers](https://www.mercadopago.com.ar/developers/es/docs/split-payments/split-1-1/overview), consulta 2026-10-15).
- **Requisitos:** cuenta de vendedor con identificación nivel KYC 6. Cada profe tiene que vincular su cuenta de Mercado Pago a la plataforma por OAuth ([requisitos](https://www.mercadopago.com.ar/developers/es/docs/split-payments/split-1-1/prerequisites)).
- **Comisión de la plataforma:** se carga en `marketplace_fee` (Checkout Pro) o en `application_fee` (Checkout API). Textual: "primero se descuenta la comisión de Mercado Pago, y la comisión del marketplace se descuenta del saldo restante" ([integración](https://www.mercadopago.com.ar/developers/es/docs/split-payments/split-1-1/integration-configuration/integrate-marketplace)).
- **Devoluciones:** se reparten en proporción entre el profe y la plataforma. Si el profe no tiene saldo, la plataforma solo puede devolver su parte. El resto queda a cargo del vendedor (misma fuente).
- **Reserva de fondos en tarjeta (cobrar después):**
  - Con la Orders API, la reserva dura **5 días** desde que se crea; si no se captura, se cancela sola. Solo se puede capturar el total ([Orders API](https://www.mercadopago.com.ar/developers/es/docs/checkout-api-orders/payment-management/reserve-capture-cancel)).
  - La documentación de Bricks dice **7 días** ([Bricks](https://www.mercadopago.com.ar/developers/es/docs/checkout-bricks/additional-content/payment-management/make-value-reserve)). **Las dos páginas no coinciden.**
  - Los ejemplos son solo con **tarjeta de crédito**.
- **No verificado:**
  - si la reserva de fondos se puede combinar con el split (comisión automática para la plataforma);
  - si la plataforma puede decidir cuándo se libera la plata al profe según un evento (por ejemplo, "clase calificada").

---

## 5. Regulación y riesgos

### 5.1 Qué figura legal es un "comisionista" de clases

- **DATO (Código Civil y Comercial, [InfoLEG](http://servicios.infoleg.gob.ar/infolegInternet/anexos/235000-239999/235975/texact.htm), consulta 2026-10-15):**
  - **Art. 1345, corretaje:** el corredor media "en la negociación y conclusión de uno o varios negocios", sin relación de dependencia ni de representación con las partes.
  - **Art. 1347:** el corredor debe, entre otras cosas, **verificar la identidad y la capacidad legal** de quienes contratan e informar las circunstancias relevantes.
  - **Art. 1350:** si el negocio se concreta por su intervención, cobra la comisión pactada.
  - **Art. 1351:** si hay un solo corredor, le deben comisión las dos partes, salvo pacto en contrario.
  - **Art. 1346:** habla de corredor "habilitado profesionalmente". **No sé** si eso alcanza a una plataforma digital de clases. Es pregunta para el abogado.
- **OPINIÓN:** en la práctica, estas plataformas funcionan con un **contrato propio (términos y condiciones)**: la plataforma presta un servicio de intermediación y tecnología. El profe le da un mandato para cobrar por él, a través de un procesador de pagos. El encuadre exacto lo tiene que firmar un abogado.
- **Defensa del Consumidor (Ley 24.240, [InfoLEG](http://servicios.infoleg.gob.ar/infolegInternet/anexos/0-4999/638/texact.htm)):**
  - El **art. 40** hace responsables "solidariamente" al proveedor, al vendedor y a quien puso su marca cuando el daño viene del servicio.
  - **Riesgo:** que un juez considere a la plataforma parte de la cadena si una clase sale mal (o algo peor con un menor).
  - El **art. 10 ter** obliga a dejar dar de baja por el mismo medio por el que se contrató. Es justo lo que le reclaman a Superprof.
  - Investigaciones anteriores del proyecto encontraron fallos contra Mercado Libre por ventas de terceros ([iProfesional](https://www.iprofesional.com/legales/438359-fallo-justicia-argentino-contra-mercado-libre-por-no-entregar-2-aires-acondicionados), citado en `2026-10-08-L1-intermediario.md`; no lo reabrí hoy).

### 5.2 ¿Puede considerarse relación laboral con los profes?

- **DATO:** la **Ley 27.802 de Modernización Laboral** se publicó en el Boletín Oficial el **2026-03-06**.
  - Su art. 13 reemplazó el **art. 23 de la Ley de Contrato de Trabajo**. Ahora la presunción de contrato de trabajo **no se aplica** a contrataciones de servicios profesionales o de oficios cuando "se emitan los recibos o facturas correspondientes", o cuando el pago se hace por sistemas bancarios ([LCT en InfoLEG](http://servicios.infoleg.gob.ar/infolegInternet/anexos/25000-29999/25552/texact.htm), consulta 2026-10-15).
- **DATO:** esa misma ley creó un régimen de "prestadores independientes" de plataformas (Título XII, arts. 119-128). **Solo alcanza** a "servicios privados de movilidad de personas y reparto" ([Marval, 2026-03-18](https://www.marval.com/publicacion/se-regulan-los-servicios-de-plataformas-digitales-17528)). **No cubre las clases.**
- **No verificado:** si la ley tiene cuestionamientos judiciales.
- **OPINIÓN:** el riesgo laboral es **bajo** si:
  - el profe pone su precio y sus horarios;
  - acepta o rechaza alumnos;
  - puede trabajar en otras plataformas;
  - factura él.

  Sube si la plataforma fija precios, asigna alumnos, sanciona o exige exclusividad.

### 5.3 Retener el pago hasta que se califique la clase

- **DATO ([BCRA, Comunicación "A" 6859, 2020-01-09](https://www.bcra.gob.ar/Pdfs/comytexord/A6859.pdf)):**
  - Son PSP las personas jurídicas que, sin ser entidades financieras, cumplen al menos una función en un esquema de pagos minoristas, como ofrecer cuentas de pago.
  - El 100% de los fondos de los clientes tiene que estar, en todo momento, en cuentas a la vista en pesos en bancos del país.
  - Los incumplimientos se sancionan según los arts. 41 y 42 de la Ley de Entidades Financieras.
- **OPINIÓN, la regla práctica:** **la plataforma nunca tiene que tener la plata del alumno en su propia cuenta.** Tus mismas funciones se pueden armar de cuatro formas:

| Forma | Cómo funciona | Pros | Contras |
|---|---|---|---|
| **A. Reserva de fondos en la tarjeta** | Al reservar, se "congela" el monto en la tarjeta de crédito del alumno. Después de la clase confirmada, se cobra. Si el profe no vino, se cancela. | Es lo más parecido a tu idea. La plata no sale de la tarjeta del alumno hasta el final. | Dura **5-7 días**: solo sirve si se reserva poco antes de la clase. Solo crédito. Con split: **no verificado**. |
| **B. Cobro anticipado con split** | El alumno paga al reservar. La plata va a la cuenta de Mercado Pago **del profe** y la comisión, a la plataforma. Si hay problema, se devuelve. | Verificado y disponible en Argentina. La plataforma no custodia. | La plataforma no "retiene": el profe ya tiene la plata. Si el profe no devuelve, la plataforma solo devuelve su parte. |
| **C. Tarjeta en garantía (como ATC)** | No se cobra al reservar. Solo se cobra si el alumno no viene o cancela tarde. | Ataca justo el "nadie se clava". Lo usa tu propio ejemplo. | El pago de la clase sigue por fuera, salvo que se combine con B. |
| **D. Registrarse como PSP ante el BCRA** | La plataforma custodia la plata (como Preply con el saldo del profe) | Control total | Es para la etapa 2. Requisitos y costos actuales no verificados. |

- **No verificado y para el abogado:**
  1. Si una plataforma que cobra comisión por split queda alcanzada por alguna norma del BCRA para "agregadores" o "facilitadores".
  2. Si vender **paquetes o bonos** usables con cualquier profe (crédito guardado en la plataforma) se parece a custodiar fondos. **OPINIÓN:** evitarlo al principio. Los paquetes, siempre con un profe y pagados a su cuenta.

### 5.4 Alumnos menores de edad

- **DATO (Código Civil y Comercial, arts. 25-26):** menor es quien no cumplió 18 años, y "ejerce sus derechos a través de sus representantes legales". Consecuencia: **la cuenta, el contrato y el pago tienen que ser del padre, la madre o el tutor.**
- **Controles de antecedentes:**
  - **No encontré una ley nacional** que obligue a los profes particulares a presentar certificado de antecedentes.
  - Mendoza tiene una ley de "ficha limpia" (Ley 9606) para el personal de instituciones educativas. Lo vi en los resultados del buscador (Los Andes, 2025-01-10; gobierno de Mendoza), **no abrí la norma**.
  - Un caso de julio de 2026 en Mendoza (Sitio Andino) muestra que pedir el certificado no alcanza si nadie lee **qué** antecedente tiene. También lo vi solo en el resumen del buscador.
- **Datos personales:** aplica la Ley 25.326 de Protección de Datos Personales (conocimiento general; **no la abrí hoy**). Datos de menores, ubicación y horarios son información delicada.
- **OPINIÓN:** **un solo incidente con un menor puede matar la plataforma y dejar a los fundadores con un problema legal.** Para la primera etapa: **solo alumnos adultos** (ingreso a la facultad, CBC, finales, idiomas). Menores después, con cuenta del padre, certificado obligatorio y revisado, y la opción de clase online o en un lugar público.

### 5.5 Impuestos y facturación

- **DATO (Ley de IVA, art. 7, inciso h), apartado 3, [InfoLEG](http://servicios.infoleg.gob.ar/infolegInternet/anexos/40000-44999/42701/texact.htm)):** están exentas de IVA las "clases dadas a título particular sobre materias incluidas en los referidos planes de enseñanza oficial", dadas fuera de los establecimientos y sin depender de ellos.
- **DATO (ARCA, [categorías del monotributo](https://www.arca.gob.ar/monotributo/categorias.asp), vigentes desde 2026-08-01, servicios):**
  - Categoría A: hasta $12.009.410 por año, cuota de $49.527 por mes.
  - Categoría D: hasta $30.628.651 por año, cuota de $84.613 por mes.
- **Cómo factura cada uno (OPINIÓN, a confirmar con un contador):**
  - **El profe** le factura la clase al alumno (factura C si es monotributista).
  - **La plataforma** le factura su comisión al profe.
  - Ingresos Brutos de la plataforma: sobre su comisión.
  - Retenciones que pueda aplicar Mercado Pago a cada parte: **no verificado**.
- **OPINIÓN:** gran parte de los profes **no factura**. Exigir factura desde el día 1 achica la oferta. No exigirla expone a la plataforma. Hay que decidirlo con un contador antes de pasar de la prueba a mano a la app.

### 5.6 Resumen de riesgos

| Riesgo | Nivel (OPINIÓN) | Cómo se baja |
|---|---|---|
| **Fuga: alumno y profe se arreglan por fuera** | **Alto** | Ver 6.6. Es el riesgo que define si hay negocio. |
| Ticket chico (≈ USD 4 por clase) | Alto | Volumen, o cambiar a abono del profe o la academia (modelo ATC) |
| Incidente con un menor | Bajo de probabilidad, **catastrófico** de impacto | Empezar con adultos |
| Custodia de fondos (BCRA) | Bajo si nunca se toca la plata | Split o reserva de Mercado Pago |
| Responsabilidad como proveedor (Defensa del Consumidor) | Medio | Términos y condiciones bien hechos, verificación, resolución de disputas |
| Relación laboral | Bajo | Profe independiente que pone precio y horario |
| Superprof y Preply como competencia | Medio | Nicho local con cobro y cumplimiento, lo que Superprof no hace |
| Depender de Mercado Pago | Medio | Es el único procesador que verifiqué para split en Argentina. Otros: **no verificados** |

---

## 6. Respuestas a las dudas de Facu, una por una

**6.1 "Somos un comisionista, no sé qué legalidad hay en el medio."**
- Es legal intermediar y cobrar comisión. El Código Civil y Comercial regula el corretaje (arts. 1345-1355) y la libertad de contratar.
- Los tres puntos legales que importan son:
  1. **no custodiar plata** (BCRA, A 6859);
  2. **cuidar a los menores**;
  3. **términos y condiciones** que dejen claro que la plataforma intermedia y no da las clases.
- Ver 5.1 a 5.5. Antes de la app, una consulta con un abogado (ESTIMACIÓN: USD 100-300 la consulta, sin fuente).

**6.2 "Unimos alumnos con profesores y organizamos horarios."**
- **OPINIÓN:** "organizar horarios" es justo lo que **retiene** al profe. Es una herramienta que usa todos los días, aunque el alumno ya lo conozca.
- Es lo que venden TutorBird, TutorCruncher y ATC.
- La parte de "unir" solo genera plata en la **primera** clase de cada pareja.

**6.3 "Existe ATC en Argentina."**
- Verificado (ver 3.3). Pero ATC cobra sobre todo **un abono mensual a los clubes** (USD 50-100) y "el único costo de ATC es el abono mensual".
- Para el "no vino" usa la **tarjeta en garantía**.
- Tardó entre 8 y 11 años y necesitó inversión para llegar a 700 clubes.
- **OPINIÓN:** tu ejemplo confirma el rubro, pero **contradice un poco el modelo "comisionista puro".**

**6.4 "Los intermediarios siempre son los que más ganan (Amazon, Uber, Airbnb)."**
- **No estoy de acuerdo con el "siempre".** Ese razonamiento mira solo a los que sobrevivieron (sesgo de supervivencia).
- **DATO:** Homejoy (limpieza a domicilio) cerró. La literatura académica lo cita como caso de fuga de transacciones por fuera de la plataforma ([Gu, borrador, Boston College](https://mackinstitute.wharton.upenn.edu/wp-content/uploads/2021/03/Gu-Grace_Technology-and-Disintermediation-in-Online-Marketplaces.pdf)).
- Investigaciones anteriores del proyecto encontraron otros cierres de intermediarios: OLX Autos salió de Argentina en 2023, y Shypp.it cerró por el costo de cumplir la ley al retener plata de terceros (`2026-10-08-L1-intermediario.md`).
- **OPINIÓN:** los intermediarios ganan mucho **cuando son indispensables en cada transacción**:
  - Uber: el pasajero no vuelve a ver al mismo chofer.
  - Airbnb: viajes de una vez, con pagos internacionales y seguro.
  - Amazon: logística propia.

  En clases particulares la relación **se repite cada semana con la misma persona**, que es el peor caso para un comisionista.
- Preply lo resolvió así:
  - se queda con el **100% de la primera clase** y con **18-33%** de las siguientes;
  - da las clases **online dentro de su propia aula**;
  - levantó **más de USD 299 M**.

**6.5 "Que sea el Instagram de profesores particulares."**
- **OPINIÓN:** como **vidriera** (perfil con videos cortos, mostrar cómo explica el profe) es buena idea y barata, y ayuda a captar alumnos.
- Como **red social** (seguidores, contenido, tiempo de uso) es otro negocio. Compite por atención con Instagram y TikTok y no paga hasta tener millones de usuarios.
- Recomiendo dejarlo para la etapa 2. En la etapa 1, el valor está en **reservar, cobrar y que nadie se clave**.

**6.6 "Que nadie se clave con clases; la app retiene el pago hasta que todos den por concluida y puntuada la clase."**
- **Es viable sin custodiar plata.** Hay tres herramientas verificadas de Mercado Pago:
  1. reserva en tarjeta de crédito por 5-7 días;
  2. split con comisión;
  3. el modelo de tarjeta en garantía de ATC.

  Ver 5.3.
- **Cómo lo hacen los que funcionan (DATO):**
  - Preply confirma la clase sola a las 72 h si el alumno no la confirma (para que la plata no quede trabada).
  - Classgap devuelve todo si el profe no viene o si se cancela con 8 h de anticipación, y tiene garantía de 24 h para la primera clase.
- **El problema de la fuga (desintermediación), con fuentes:**
  - **Gu y Zhu (Management Science, 2021):**
    - hicieron un experimento en una plataforma de freelancers;
    - **más confianza** entre las partes mejora las contrataciones;
    - pero cuando la confianza es muy alta, **aumenta la fuga** y se come esa ganancia ([RePEc](https://ideas.repec.org/a/inm/ormnsc/v67y2021i2p794-807.html)).
    - Tus reseñas y puntajes son un arma de doble filo.
  - **Gu (borrador):**
    - cuando China bloqueó Skype, **bajó la fuga** en una plataforma de freelancers de EE.UU.;
    - la conclusión: tener canales de comunicación propios ayuda a retener las transacciones.
    - Ese mismo borrador cita una encuesta según la cual "cerca del 90%" de las transacciones se van por fuera después del primer contacto. **No verifiqué la fuente original; tomarlo con mucha cautela.**
  - **Contraejemplo: Astashkina, Bray, Momot y Salikhov (2023):**
    - midieron por GPS a 5.391 limpiadoras de una app y **no encontraron fuga** (como máximo 1 de cada 83 relaciones);
    - pero el 90% de las parejas limpiadora-casa tuvo **una sola limpieza** ([PDF, Kellogg](https://www.kellogg.northwestern.edu/faculty/bray/doc/disintermediation/disintermediation.pdf)).
    - **OPINIÓN:** en clases particulares pasa lo contrario (relación semanal), así que no nos salva.
- **Cómo la combaten los que funcionan (DATO de sus propias reglas):**
  - Preply cobra la primera clase entera (gana aunque después haya fuga).
  - Classgap cobra solo 10% cuando el profe trae su propio alumno, para que le convenga seguir usando la plataforma.
  - Superprof cobra al alumno **por contactar**, antes de que haya relación.
  - ATC cobra abono mensual al club.
  - **OPINIÓN:** las cuatro son formas de **no depender de la comisión de la clase número 10**.

**6.7 "Bonos, publicidad y suscripciones después."**
- **OPINIÓN:** es el orden correcto. Publicidad y "Pro" solo funcionan cuando hay muchos profes compitiendo por alumnos.
- Los **bonos o créditos de la plataforma** tienen riesgo regulatorio (ver 5.3). Mejor paquetes con un mismo profe.

**6.8 "Uber de logística B2B o B2C."**
- Lo investiga otro. Solo una nota: el mismo análisis de fuga (6.6) aplica allá. Los clientes que repiten con el mismo transportista son los que más se van por fuera.

---

## 7. Filtro final

| Filtro | Puntaje (1-5) | Por qué |
|---|---|---|
| **F1. Demanda comprobable en Argentina** | **3** | **A favor (DATO):** Superprof opera desde 2017 y la gente le paga una suscripción solo para contactar profes. Hay precios de mercado publicados. ATC muestra que en Argentina la gente reserva con tarjeta en garantía. **En contra:** no hay datos de cuántos alumnos toman clases ni de cuánto pierden los profes por cancelaciones. **No hay ninguna prueba** de que los profes acepten pagar 15-20% de comisión cuando hoy cobran el 100% por transferencia. |
| **F2. Producto automatizable y global** | **4** | Es el mismo producto para miles de profes, no es trabajo a medida. Funciona en cualquier país (Preply y Classgap lo demuestran). Lo que **no** se automatiza del todo: la verificación de profes, las disputas y "encender" cada ciudad y materia, que se hace a mano y de a una. |
| **F3. Validable rápido y barato (30 días, menos de USD 300)** | **4** | Una prueba a mano con WhatsApp, landing y links de pago de Mercado Pago se hace en 30 días por menos de USD 250 (ver 8). **OPINIÓN:** noviembre-diciembre es temporada de finales y exámenes, cuando más se buscan profes (conocimiento general del calendario, no verificado hoy). Resta un punto porque un marketplace necesita juntar a los dos lados a la vez, y 30 días es poco para medir la fuga. |
| **F4. Riesgo legal manejable (5 = bajo)** | **3** | Manejable **si** no se custodia plata y se arranca solo con adultos. Pesan la responsabilidad como proveedor (Defensa del Consumidor, art. 40), la informalidad fiscal de los profes y el riesgo con menores cuando se abra a secundaria. |
| **F5. Encaje con Facu** | **4** | **A favor:** te atrae el modelo de conectar dos partes; ya dirigiste una app real con Claude; el capital alcanza para la prueba; tenés 22 años y estás en la facultad, cerca de alumnos y de ayudantes que dan clases (OPINIÓN). **En contra:** ticket chico (≈ USD 4 por clase), que choca con tu regla de "no achicar ideas". Y el éxito depende de vender y conseguir usuarios más que de procesos, que es tu fuerte como ingeniero industrial. |
| **Total** | **18 / 25** | |

### Recomendación: **PRIMERA, pero como experimento acotado, no como "el Instagram de profesores".**

**Por qué PRIMERA:**
- Es de las más **baratas y rápidas de probar**.
- Te enseña lo que querés aprender para la etapa 2: **cómo funciona un marketplace por dentro** (conseguir los dos lados, fuga, cobro, confianza).
- La temporada de exámenes está empezando.
- Aunque falle, el aprendizaje sirve para cualquier otra app de "conectar dos partes" que tenés en la lista (enfermeros, repuestos, logística).

**Con tres condiciones (OPINIÓN):**
1. **Solo adultos** al principio: ingreso a la facultad, CBC, finales universitarios e idiomas.
2. **Sin tocar la plata.** El alumno le paga al profe por Mercado Pago y vos cobrás tu parte aparte, o se usa el split.
3. **La prueba tiene que medir la fuga y si el profe acepta pagar.** Si el profe no quiere pagar comisión pero sí un abono por la agenda y el cobro, el negocio es "ATC para profes" (software), no comisionista. **Las dos salidas sirven.**

**Por qué no es más que 18:** no hay evidencia de que la comisión por clase sobreviva a la segunda clase. Y lo grande del mercado es informal. Si la prueba sale mal en fuga, pasa a PENDIENTE sin culpa: habrá sido un fracaso barato y bien medido.

---

## 8. Primer experimento concreto

**Nombre de trabajo:** "Profes de finales con pago protegido". Es una prueba a mano, sin app.

| Punto | Detalle |
|---|---|
| **Qué** | Durante 30 días, vos hacés de plataforma para **un nicho**: materias de 1.º y 2.º año de tu facultad, o ingreso/CBC, en tu ciudad u online. Solo alumnos mayores de 18. |
| **Con quién (oferta)** | 8 a 10 profes: ayudantes de cátedra, alumnos avanzados y graduados que ya den clases. Cada uno pone su precio. Vos cobrás **15% de comisión**, o le ofrecés la alternativa de un **abono fijo de ARS 10.000-15.000 por mes** (para medir cuál prefiere). Pedido a cada profe: certificado de antecedentes (lo saca online por $1.000-8.500) y el compromiso de respetar la política de cancelación. |
| **Con quién (demanda) y cómo llegar** | Grupos de WhatsApp y de Instagram de cursos y comisiones, centro de estudiantes, carteles con QR en la facultad, una landing gratis en Cloudflare Pages con formulario. Opcional: USD 50-100 en publicidad de Instagram segmentada por edad y zona. |
| **Cómo funciona** | (1) El alumno pide por formulario o WhatsApp. (2) Vos le proponés 2-3 profes con horario. (3) **El alumno paga por adelantado con el link de Mercado Pago del profe** (la plata nunca pasa por vos). (4) Regla publicada: si el alumno cancela con menos de 12 h, el profe cobra igual; si el profe falta, se devuelve todo. (5) Después de la clase, los dos califican por formulario. (6) Cada semana le pasás al profe su resumen y le facturás tu comisión (monotributo). |
| **Semana 1** | 15 entrevistas a profes y 15 a alumnos con las preguntas de abajo. Reclutar profes. Armar la landing. |
| **Semanas 2-4** | Operar y medir todo en una planilla: pedidos, clases pagadas, cancelaciones, ausencias, segunda clase por el sistema o por fuera, comisiones cobradas. |
| **Costo** | Dominio USD 0-15. Publicidad USD 0-100. Impresiones USD 20. Monotributo si todavía no lo tenés: $49.527 por mes (≈ USD 33, con el tipo de cambio de abril de 2026). **Total: menos de USD 250.** |
| **Días** | 30 |
| **Número para SEGUIR** (propuesta mía, no es un estándar) | **Las cuatro a la vez:** (a) 30 o más clases pagadas por adelantado en 30 días; (b) 6 o más profes activos; (c) 50% o más de los alumnos que tomaron una clase reservaron la segunda **por el sistema**; (d) 70% o más de los profes pagaron la comisión o el abono sin pelear. |
| **Número para CORTAR** | **Cualquiera:** (a) menos de 10 clases pagadas; (b) menos de 30% de segundas clases por el sistema (la fuga gana); (c) más de la mitad de los profes se niega a pagar comisión **y** abono. |
| **Zona gris** | Entre los dos umbrales: repetir 30 días cambiando una sola cosa (por ejemplo, solo abono o solo tarjeta en garantía). |
| **Pérdida máxima** | **USD 250 + 60 h de tu tiempo.** Si se llega a eso antes del día 30, se corta igual. |
| **Qué aprendés aunque falle** | Cuánto se fuga una relación repetida, si el profe valora más conseguir alumnos o cobrar seguro, y cuánto cuesta conseguir cada lado. Sirve para todas tus ideas de "conectar dos partes". |

### Preguntas tipo The Mom Test

Preguntan por **hechos pasados**, no por opiniones sobre tu idea. **No cuentes la idea** hasta el final.

**Para profes:**
1. "Contame la última vez que un alumno te canceló a último momento o no vino. ¿Qué pasó y qué hiciste?"
2. "En el último mes, ¿cuántas clases se te cayeron y cuántas cobraste igual?"
3. "¿Cómo conseguiste a tus últimos tres alumnos?"
4. "¿Cómo te pagan hoy? ¿Alguien te quedó debiendo alguna vez? ¿Cuánto y cómo terminó?"
5. "¿Pagás o pagaste por algo para conseguir alumnos u organizarte (Superprof, avisos, alguna app)? ¿Cuánto? ¿Por qué lo seguís pagando, o por qué lo dejaste?"

**Para alumnos (o padres, cuando se abra a menores):**
1. "Contame cómo encontraste a tu último profe particular. ¿Dónde buscaste y cuánto tardaste?"
2. "Antes de la primera clase, ¿qué hiciste para saber si era bueno y confiable?" (Para padres: "La última vez que contrataste a alguien para tu hijo, ¿qué controlaste?")
3. "¿Alguna vez pagaste una clase que salió mal, o un profe no apareció? ¿Qué pasó con la plata?"
4. "¿Cómo le pagás hoy: antes o después de la clase? ¿Por qué así?"
5. "¿Pagaste alguna vez una plataforma para encontrar profe (Superprof u otra)? ¿Cuánto? ¿La volverías a pagar? ¿Por qué?"

---

## 9. Fuentes (todas consultadas el 2026-10-15, salvo que se indique otra cosa)

**Normas oficiales**
- BCRA, Comunicación "A" 6859 (2020-01-09): https://www.bcra.gob.ar/Pdfs/comytexord/A6859.pdf
- Ley de Contrato de Trabajo, art. 23 (texto vigente, modificado por la Ley 27.802): http://servicios.infoleg.gob.ar/infolegInternet/anexos/25000-29999/25552/texact.htm
- Código Civil y Comercial (arts. 25, 26, 30, 1345-1351): http://servicios.infoleg.gob.ar/infolegInternet/anexos/235000-239999/235975/texact.htm
- Ley 24.240 de Defensa del Consumidor (arts. 2, 10 ter, 40): http://servicios.infoleg.gob.ar/infolegInternet/anexos/0-4999/638/texact.htm
- Ley de IVA, art. 7, inciso h), apartado 3: http://servicios.infoleg.gob.ar/infolegInternet/anexos/40000-44999/42701/texact.htm
- ARCA, categorías del monotributo (vigentes desde 2026-08-01): https://www.arca.gob.ar/monotributo/categorias.asp
- Certificado de antecedentes penales: https://www.argentina.gob.ar/justicia/reincidencia/antecedentespenales

**Análisis legal (estudios de abogados)**
- Marval, régimen de plataformas de la Ley 27.802 (2026-03-18): https://www.marval.com/publicacion/se-regulan-los-servicios-de-plataformas-digitales-17528
- Ley 27.802, sanción y publicación: resumen del buscador de siap.blogdelcontador.com.ar y garciaalonso.com.ar (no abiertos)
- Mendoza, Ley 9606 "ficha limpia" y caso de julio de 2026: solo resúmenes del buscador (losandes.com.ar 2025-01-10; mendoza.gov.ar; sitioandino.com.ar). **No abiertos.**

**Mercado Pago**
- Split de Pagos 1:1, descripción: https://www.mercadopago.com.ar/developers/es/docs/split-payments/split-1-1/overview
- Requisitos: https://www.mercadopago.com.ar/developers/es/docs/split-payments/split-1-1/prerequisites
- Integración del marketplace: https://www.mercadopago.com.ar/developers/es/docs/split-payments/split-1-1/integration-configuration/integrate-marketplace
- Reservar, capturar y cancelar (Orders API): https://www.mercadopago.com.ar/developers/es/docs/checkout-api-orders/payment-management/reserve-capture-cancel
- Reserva de fondos (Bricks): https://www.mercadopago.com.ar/developers/es/docs/checkout-bricks/additional-content/payment-management/make-value-reserve
- Comisiones (datos de 2023-08-01): https://www.iprofesional.com/tecnologia/386153-mercado-pago-que-debes-saber-sobre-comisiones-plazos-y-montos

**Competidores y ejemplos**
- Superprof en Trustpilot: https://www.trustpilot.com/review/superprof.com.ar
- Superprof, reclamos (403; solo el resumen del buscador): https://tuquejasuma.com/superprof-argentina
- Superprof, blog de México (2026-05-14): https://www.superprof.mx/blog/profesores-particulares-superprof/
- Superprof en Argentina (2019-04-09): https://infonegocios.info/plus/superprof-profes-para-todo-en-un-solo-lugar-clases-de-cocina-portugues-canto-tenis-y-mas
- Forbes Argentina, cómo encontrar profes (2022-11-01, parece contenido de Superprof): https://www.forbesargentina.com/negocios/como-donde-encontrar-profesores-particulares-argentina-n24248
- Busca Tu Clase (iProfesional, fecha real no visible): https://www.iprofesional.com/actualidad/219742-lanzan-sitio-para-buscar-clases-de-profesores-de-idiomas-y-computacion
- Preply, cobro de las clases: https://help.preply.com/en/articles/4171348-when-and-how-you-get-paid-for-lessons
- Preply según Sacra: https://sacra.com/research/preply
- Classgap, reservas y comisiones: https://www.classgap.com/en/info/bookings
- TusClasesParticulares: https://www.tusclasesparticulares.com/
- ATC, Forbes Argentina (2023-06-26): https://www.forbesargentina.com/negocios/crearon-una-app-alquilar-canchas-tienen-mas-350-clubes-200-mil-usuarios-pico-monaco-como-inversor-n36054
- ATC, one-pager (mayo 2025): https://www.cancilleria.gob.ar/userfiles/ut/2025-05_-_one_pager_atc.pdf
- ATC, sitio y precios: https://atcsports.io/ y https://atcsports.io/software-gestion-deportiva

**Mercado**
- Precios de clases particulares (abril 2026): https://cuantomecuesta.com/ar/clases-particulares/
- Matrícula 2024 (fuente secundaria del Anuario 2024): https://www.tiempoar.com.ar/ta_article/caida-de-la-matricula-colegios-primaria-y-secundaria-argentina/
- Ministerio de Educación, "La voz de las y los estudiantes 2022" (revisado: no tiene datos de clases particulares): https://argentina.gob.ar/sites/default/files/la_voz_2022-informe.pdf
- Ausencias en tutorías (fuente con interés comercial, no usada como dato): https://appointmentreminder.com/industries/education

**Desintermediación (fuga)**
- Gu y Zhu, "Trust and Disintermediation", Management Science 67(2), 2021: https://ideas.repec.org/a/inm/ormnsc/v67y2021i2p794-807.html
- Gu, "Technology and Disintermediation in Online Marketplaces" (borrador): https://mackinstitute.wharton.upenn.edu/wp-content/uploads/2021/03/Gu-Grace_Technology-and-Disintermediation-in-Online-Marketplaces.pdf
- Astashkina, Bray, Momot y Salikhov, "A Disquieting Lack of Evidence for Disintermediation in a Home-Cleaning Platform" (2023-08-28): https://www.kellogg.northwestern.edu/faculty/bray/doc/disintermediation/disintermediation.pdf

**Del propio proyecto (no reabiertas hoy)**
- `research/fuentes/2026-10-08-L1-intermediario.md` (escrow, OLX Autos, Shypp.it, fallo contra Mercado Libre)
- `research/datos/2026-10-13-nichos/08-educacion.json` (TutorBird y TutorCruncher, verificados el 2026-10-13)
