# L2 (app de precios del súper) y L7 (app de huella de carbono): investigación de mercado

**Fecha:** 2026-10-08 · **Para:** Facu · **Regla N.º 1 aplicada:** cada dato lleva su fuente (lista al final con URL y fecha).

## Cómo leer este informe

- **DATO**: afirmación con fuente. Entre corchetes, el número de la fuente de la lista final.
- **ESTIMACIÓN**: cálculo o razonamiento mío, marcado con la palabra "ESTIMACIÓN".
- **OPINIÓN**: juicio mío, marcado con la palabra "OPINIÓN".
- **Nivel de verificación de cada fuente:** en la lista final, **[A]** = abrí la página y leí el contenido; **[B]** = la vi solo a través del resumen del buscador, sin abrirla. Las [B] valen menos: conviene abrirlas antes de usar un número en algo importante.
- **Límite de esta investigación:** hice 15 búsquedas para L2 y 17 para L7, más 20 lecturas directas de páginas. En la mitad de L7 **se agotó el cupo de búsquedas web de la sesión**. Por eso quedaron **sin buscar**: startups argentinas de software de huella de carbono, encuestas de disposición a pagar por apps de carbono y el estado del acuerdo UE-Mercosur. Quedan anotados en "Pendientes".

---

## Resumen ejecutivo

| Idea | Puntaje global (OPINIÓN) | Veredicto corto |
|---|---|---|
| **L2: app para sacar fotos a los precios y saber cuánto llevás** | **3/10** | Ya existe gratis, de varias formas, y la plata está en la publicidad o en vender datos, que exige millones de usuarios. Como negocio, no. Como ejercicio de aprendizaje barato, puede ser. |
| **L7a: app de huella de carbono para personas (suscripción)** | **2/10** | Hay evidencia fuerte de que las personas no pagan. Klima (Berlín) se vendió y se cerró en 2025. Joro pasó a llamarse Commons y declaró el seguimiento "gratis para siempre". Descartar. |
| **L7b: servicio o herramienta de huella y trazabilidad para empresas y exportadores** | **4/10** | Es el único ángulo con alguien que paga por obligación (EUDR desde 2026-12-30, Mendoza obliga a reportar, CNV pide indicadores). Pero hay jugadores gratuitos o sectoriales (VISEC), consultoras y un mercado global en consolidación, y la regulación cambia seguido. Vale validarlo con entrevistas, sin construir nada todavía. |

---

# PARTE 1 — L2: app para sacar fotos a los precios del súper y saber cuánto llevás

## 1.1 Qué ya existe en Argentina

**El Estado ya publica los precios gratis**
- DATO: Precios Claros se alimenta del SEPA (Sistema Electrónico de Publicidad de Precios Argentinos, creado en 2016). En agosto de 2024, la Disposición 494/2024 abrió el acceso público y gratuito a unos **12 millones de precios diarios de 3.600 supermercados**, para empresas, emprendedores, académicos y medios [L2-1][L2-2].
- DATO: El 2026-10-08 el sitio preciosclaros.gob.ar responde. Permite buscar por producto o categoría, comparar hasta 4 comercios cercanos a una dirección y armar una lista de compras. Según sus preguntas frecuentes, los precios se actualizan todos los días. No vi un escáner por cámara ni una descarga de datos en la página principal. Algunos campos aparecían sin completar ("actualizados al {{ fecha }}"), así que no pude confirmar que funcione del todo [L2-3].

**Comparadores privados (todos gratis para el usuario)**
- DATO: **Ratoneando** es un sitio gratuito con app para Android, creado por Matías Bontempo, que ordena los productos por precio por unidad [L2-4][L2-5]. Al abrir ratoneando.ar solo vi el eslogan, así que no pude ver cómo gana plata ni cuántos usuarios tiene [L2-6].
- DATO: **Mirá Precios** fue creada por tres egresados del ITBA. En agosto de 2024 tenía **unos 15.000 usuarios desde su lanzamiento en abril y unos 500 activos por día**. Ya facturaba algo, pero estaba "lejos" de escala. No planeaban cobrar suscripción y veían valor en los datos de los carritos. Usa códigos de barras (EAN) y permite exportar el carrito a la web de las cadenas [L2-7]. En agosto de 2025 se la describía escaneando códigos de barras con IA [L2-8].
- DATO: **Pricely** (actualización diaria, escaneo de producto, gráficos de evolución de precios) y **Precialo** (historial de precios y alertas) aparecen en una nota de agosto de 2025 [L2-8].
- DATO: **PrecioYa** compara precios de La Anónima, Carrefour, Disco, Jumbo, Vea y ChangoMás, con lista de compras y promociones bancarias. La nota no tiene fecha visible [L2-9]. **Tu Changuito** (de Neuquén) permite escanear el código de barras en la góndola para ver si otro comercio lo tiene más barato. Tampoco tiene fecha visible [L2-10].
- No encontré cifras de descargas de PrecioYa, Ratoneando ni Tu Changuito.

**Lo que pide Facu ("ir sumando cuánto llevo") ya existe**
- DATO: Una búsqueda en Google Play Argentina del 2026-10-08 ("calculadora supermercado escanear precio") devuelve, entre otras: "Calculadora de compras" (MLZ, 4,8 estrellas), "Shopping Calculator" (LemonClip, 4,0), "**SuperJusto: Escaneá precios**" (4,8, con voseo, probablemente argentina), "Escáner de supermercado", "Calculadora para ir de compras" y "Escaner de precios" [L2-11]. No abrí cada ficha, así que no verifiqué cuántas descargas tiene cada una ni si leen la etiqueta con la cámara o solo el código de barras.
- DATO: La app oficial de **Carrefour Argentina** permite escanear el código de barras del producto para ver su precio [L2-12]. Otra nota dice que su app se diseñó a partir de una encuesta a más de 15.000 clientes e incluye escáner de precios en tienda y tickets digitales [L2-13]. Una nota sobre retail en Argentina menciona "calculadoras de compras" dentro de apps de supermercados, con total en tiempo real y promociones incluidas, pero no nombra la cadena ni tiene fecha visible [L2-42].
- DATO: **Carrefour Flash** (Pilar, 50 m², unos 500 productos) cobra en forma automática al salir, sin escanear nada [L2-14].

## 1.2 Afuera: Scan & Go y listas de compras

- DATO: Carrefour tiene "Scan and Go" en algunas tiendas de España, atado a su tarjeta de fidelidad [L2-15]. En Brasil estaba en 40 tiendas en 2021 [L2-16]. No encontré evidencia de que exista en Argentina con ese nombre.
- DATO: **Walmart canceló su Scan & Go en EE.UU. en mayo de 2018.** La empresa lo atribuyó a la baja adopción y a la "fricción" (controles de ticket, pesar verduras, embolsar) [L2-17]. Un ex directivo dijo después que el motivo principal fue el robo. Walmart no lo confirmó [L2-18]. En Sam's Club, en cambio, siguió funcionando [L2-17].
- DATO: **Listonic** (Polonia) dice tener más de 15 millones de descargas y ser rentable "desde hace años", sin dar cifras ni fechas (es material propio) [L2-19]. Es gratis con publicidad, y el plan premium sirve sobre todo para sacar los anuncios: 4,99 zł por mes o 29,99 zł por año en la App Store de Polonia (ficha sin fecha) [L2-20].
- DATO: **Bring!** (Suiza) es gratis para el usuario y gana plata con **publicidad de marcas de consumo masivo y cadenas** dentro de la lista: productos patrocinados, ofertas y recetas [L2-21]. En febrero de 2025 informó **3,6 millones de usuarios activos por mes** en Alemania, Austria y Suiza, y **más de 150 anunciantes** [L2-22]. Informó crecimientos de facturación del +69 % (2020), más del +90 % (2021) y alrededor del +30 % (2022), siempre sin montos absolutos [L2-23]. Según el resumen del buscador, el Correo Suizo compró la mayoría en 2021 [L2-21].
- No encontré datos de ingresos de OurGroceries ni de AnyList.

## 1.3 ¿Cómo ganan plata estas apps? Datos de ingresos

- DATO (RevenueCat, informe 2026 con datos de más de 115.000 apps): **solo el 17 % de las apps de suscripción llega a USD 1.000 por mes de ingreso recurrente en sus primeros dos años, y el 4,6 % llega a USD 10.000.** Un año después del lanzamiento, el ingreso mensual típico ronda los USD 72, y la mitad del medio de las apps está entre USD 16 y USD 429 por mes. La conversión de descarga a pago al día 35 es del 11 % con muro de pago duro y del 2 % con modelo gratuito más premium (freemium) [L2-24].
- DATO: En el mismo informe, el valor anual por cliente que paga es de USD 32 en Norteamérica, USD 25 en Europa Occidental, USD 14 en India y el Sudeste Asiático, y USD 23 de mediana global. **No hay dato de Latinoamérica** [L2-24].
- DATO (informe 2025): la mediana de ingreso por instalación a los 60 días fue de USD 0,31 [L2-25].
- **Disposición a pagar en Argentina: no encontré ninguna encuesta directa sobre apps.** Lo más cercano:
  - DATO: según Sherlock Communications, 7 de cada 10 argentinos dicen que pagar más de un streaming "se volvió muy caro" [L2-26].
  - DATO: en 2022, en apps de citas los argentinos gastaron USD 780.000, contra más de USD 3 millones en México y USD 5,2 millones en Brasil (data.ai) [L2-27].
  - DATO: el Banco Central midió más de USD 1.000 millones en suscripciones digitales en un año. Incluye streaming, IA y software y no separa las tiendas de apps. La nota no tiene fecha visible [L2-28].
- ESTIMACIÓN: una app de consumo para Argentina, con el modelo gratuito más premium que exige el mercado (todo lo comparable es gratis), probablemente quede por debajo de la mediana de RevenueCat. El valor por cliente de las regiones de menores ingresos (USD 14) es bastante menor que el de Norteamérica (USD 32), y el argentino es sensible al precio.

## 1.4 El ángulo B2B: vender los datos de precios

- DATO: **Basket** (EE.UU.) juntaba precios de góndola fotografiados por usuarios y los vendía a cadenas y marcas. Recaudó unos USD 18 millones [L2-29]. En 2022, Fobi AI firmó una carta de intención para comprar sus activos y su propiedad intelectual [L2-30]. CB Insights da información contradictoria sobre si la operación se cerró [L2-31].
- DATO: **mySupermarket** (comparador del Reino Unido) cerró [L2-32]. **Shooper** (Indonesia), que vende datos de tickets por suscripción, levantó apenas USD 130.000 [L2-33]. **Snapstar/OurCart** contó con el respaldo de Nielsen [L2-34].
- **Los jugadores que ya existen en Argentina:**
  - DATO: **Scentia** publica informes mensuales de consumo masivo con datos de más de 8.000 puntos de venta [L2-35]. Su director dijo que trabajan con "cientos de millones de tickets de compra" [L2-36]. En un estudio de 2020, según el resumen del buscador, midieron por seguimiento de cajas el 95 % de las cadenas y mayoristas, más de mil supermercados chinos y una muestra de almacenes [B, **no identifiqué con certeza la URL de este dato; no usarlo sin verificar**].
  - DATO: **Kantar Worldpanel** tiene un panel de hogares en Argentina, ampliado a 5.200 hogares en 2017 [L2-37].
  - DATO: **Rocketpin** (Chile, en Argentina desde 2018) vende relevamientos de precios y auditorías hechos con una red de personas con smartphone que cobran por "misión" [L2-38]. Es exactamente el modelo de "usuarios que sacan fotos y alguien paga por los datos".
- OPINIÓN: el ángulo B2B es el más interesante de L2, pero también el más difícil. (1) Los precios de las cadenas ya son públicos y gratis por SEPA, así que no valen nada nuevo. (2) Lo que queda (almacenes, chinos, interior) ya lo cubren Scentia y Rocketpin. (3) Para que los datos de los usuarios valgan, hace falta cobertura masiva y constante, y eso exige muchísimos usuarios o pagar por cada foto. Basket levantó USD 18 millones y terminó vendiendo sus activos.

## 1.5 Contexto argentino 2026

- DATO: según Scentia, el consumo masivo **cayó 1,5 % interanual en agosto de 2026 y acumula −2,7 % en enero–agosto**. Los supermercados de cadena cayeron 3,3 % y el comercio electrónico creció 36,9 % interanual [L2-39]. En junio de 2026 la caída fue de −2,7 % interanual [L2-40].
- DATO: la inflación (INDEC) de **agosto de 2026 fue de 33,5 % interanual y 21,3 % acumulada en el año** [L2-41]. La de julio fue de 2,1 % mensual y 33,8 % interanual [L2-41]. El dato de septiembre se publica el 2026-10-13 [L2-43].
- OPINIÓN: un consumidor que compra menos y compara más es una señal a favor del problema ("quiero controlar cuánto gasto"). Pero ese mismo consumidor es el que menos va a pagar por una app. Con inflación en baja (comparada con 2023–2024), además, la urgencia de comparar precios es menor que hace dos años.

## 1.6 Veredicto L2 (OPINIÓN, con razonamiento)

| Criterio | Puntaje | Una línea |
|---|---|---|
| Tamaño del problema | 4 | El problema existe (no pasarse del presupuesto), pero es chico: lo resuelven la calculadora del celular, la app del súper o ir anotando. |
| Disposición a pagar | 2 | Todo lo comparable es gratis. Mirá Precios ni siquiera planea cobrar. Argentina paga poco por apps. |
| Espacio frente a la competencia | 3 | Ya hay al menos 5 apps en Google Play que hacen "escanear y sumar", además de Carrefour, los comparadores y Precios Claros. |
| Ventaja de Facu | 2 | No tiene datos propios, distribución, contactos en retail ni una tecnología diferencial. Ser ingeniero industrial no pesa acá. |
| Factibilidad | 7 | Técnicamente es sencillo (foto, lectura del precio con IA, suma), aunque las promos ("2x1", "2da al 70 %") complican la lectura. |
| Escalabilidad | 4 | El software escala, pero el negocio (publicidad o datos) exige millones de usuarios: Bring! tiene 3,6 millones activos por mes después de unos 10 años. |
| Riesgo (10 = bajo) | 6 | Se pierde poca plata. El riesgo real es construir algo que nadie use. |

**Puntaje global: 3/10.** No lo recomiendo como negocio. Si Facu quiere usarlo para **aprender a lanzar una app y medir uso real**, que sea con pérdida máxima y fecha de corte definidas.

**Versión chica para validar (2–4 semanas, menos de USD 200)**
1. **Semana 1, entrevistas (USD 0):** 15 entrevistas cortas a la salida de 2 o 3 supermercados, o en grupos de ahorro de Facebook o WhatsApp. Pregunta central: "¿Cómo controlás hoy cuánto llevás? ¿Te pasó de llegar a la caja y que te alcance menos de lo que pensabas?". Ver si ya usan la calculadora del celular o la app del súper.
2. **Semanas 1–2, prototipo "Mago de Oz" (USD 0–20):** que manden por WhatsApp la foto de la etiqueta y reciban el total acumulado. Al principio lo responde Facu a mano, o una app web mínima hecha con Claude Code que lea la foto con un modelo de visión. El costo por foto hay que verificarlo en la página de precios del proveedor; no lo verifiqué.
3. **Semanas 2–4, uso real (USD 50–150 en anuncios o regalos):** 30 personas. Medir qué porcentaje lo usa en 2 o más compras distintas, cuánto acierta la lectura de precios y si alguien acepta pagar por adelantado una versión premium (por ejemplo, alertas de presupuesto).
4. **Gate (umbral para seguir, ESTIMACIÓN mía, ajustable):** 40 % o más vuelve a usarlo y al menos 5 personas pagan por adelantado. Si no se cumple, se cierra y se escribe el post-mortem. **Pérdida máxima: USD 200. Fecha de corte: 4 semanas desde el inicio.**

---

# PARTE 2 — L7: app de huella de carbono para personas y empresas

## 2.1 Apps para personas: ¿quién sigue vivo y quién paga?

- DATO: **Klima** (Berlín, 2019) calculaba la huella con un cuestionario y vendía compensación por suscripción. **En mayo de 2025, Wren compró la app y pasó a sus suscriptores a sus propios programas.** Sus miembros habían compensado más de 100.000 t de CO₂e desde 2019 [L7-1]. Dealroom fecha la compra el 2025-04-30 y dice que klima.com quedó como una página de cierre [L7-2]. No encontré un comunicado oficial.
- DATO: **Joro** (EE.UU., abril de 2020) estimaba emisiones a partir de los gastos con tarjeta [L7-3]. Levantó USD 3,5 millones y lanzó una suscripción para compensar [L7-4]. Según Princeton Alumni Weekly, en 2023 cambió de marca a **Commons** [L7-5]. Hoy Commons dice: "Tracking your carbon emissions is free, and always will be" ("el seguimiento de tus emisiones es gratis y siempre lo va a ser"). Ofrece recompensas de "50K brands" ("50.000 marcas") y no dice cómo gana plata [L7-6]. Bloomberg (2024-08-11) la describe con reintegros por compras sustentables [L7-7].
- DATO: **Earth Hero** es gratuita en la App Store [L7-8]. El Boston Globe la probó en septiembre de 2025 [L7-9].
- DATO: **Capture** (Singapur) figura como "cerrada" en Dealroom, pero la ficha está marcada como hecha con IA, así que es una fuente débil [L7-10]. **CarbonCancel** (Ámsterdam) cerró. No verifiqué la fecha [L7-11].
- **Disposición a pagar de consumidores:** no pude buscar encuestas porque se agotó el cupo. La evidencia indirecta es fuerte y va toda en la misma dirección. OPINIÓN: el más conocido de Europa (Klima) se vendió y se cerró, y el más conocido de EE.UU. (Joro/Commons) dejó de cobrar el seguimiento. **No encontré ninguna app de huella personal que viva de suscripciones.**

## 2.2 Software B2B de contabilidad de carbono: mucha plata invertida, ahora en consolidación

- DATO: **Watershed** levantó USD 70 millones con una valuación de USD 1.000 millones en febrero de 2022 [L7-12] y USD 100 millones en su Serie C en febrero de 2024 [L7-13]. Preqin estima esa valuación en unos USD 1.800 millones [L7-49]. No encontré facturación confiable: las cifras que circulan se contradicen.
- DATO: **Persefoni** levantó USD 50 millones en agosto de 2023 [L7-14] y USD 23 millones en marzo de 2025 (USD 179 millones en total). Su CEO apuntaba a ser rentable desde la segunda mitad de 2025 [L7-15]. No encontré si lo logró. Su cofundador dijo que el mercado está "in consolidation phase, big time" ("en plena fase de consolidación") [L7-16]. No verifiqué la fecha de esa entrevista.
- DATO (ESG Today, 2026-09-11): **Greenly (París) compra Normative (Estocolmo).** Juntas atienden a **más de 4.000 empresas en más de 30 países**. Tienen **ARR (ingreso anual recurrente) combinado de €30 millones** y quieren llegar a €50 millones en 3 años. La operación se valora en unos €64 millones. Greenly levantó €75 millones en total y Normative más de €40 millones. La propia Greenly describe el mercado como "fragmentado y saturado". **Otras compras de 2026:** Optera (por Green Project Technologies), Minimum (por Novisto) y **Plan A (por Diginex)** [L7-17].
- ESTIMACIÓN: €30 millones de ARR / 4.000 clientes = **unos €7.500 por cliente por año** en promedio. No es una mediana: los clientes grandes suben el promedio. Además, Normative levantó más de €40 millones y la operación conjunta se valoró en unos €64 millones. OPINIÓN: para los inversores, el sector dejó de ser un negocio de "crecer a cualquier costo".
- No encontré precios publicados de Watershed, Sweep, Greenly ni Plan A. Un comparador ubica a Watershed como la opción "premium" para grandes empresas, por encima de Normative y Sweep [L7-18]. Es una fuente débil.

## 2.3 Regulación que empuja (o dejó de empujar) la demanda

**Unión Europea: el "Ómnibus" recortó la CSRD (directiva de reporte de sostenibilidad)**
- DATO: la **Directiva (UE) 2026/470** se publicó el 2026-02-26 y rige desde el 2026-03-18. Ahora la CSRD obliga solo a las empresas con **más de 1.000 empleados y más de €450 millones de facturación**, desde el ejercicio 2027 (primer reporte en 2028). Para grupos de fuera de la UE, el umbral es más de €450 millones facturados en la UE y una filial o sucursal con más de €200 millones. Las empresas más chicas de la cadena **pueden negarse a dar datos** que excedan el estándar voluntario. La directiva de debida diligencia (CSDDD) quedó para empresas con más de 5.000 empleados y €1.500 millones, desde julio de 2029 [L7-19][L7-20]. Según distintas fuentes, entre el 80 % y el 90 % de las empresas que estaban alcanzadas quedan afuera [L7-20].
- OPINIÓN: esto **reduce la presión de los clientes europeos** para pedirle datos de emisiones (alcance 3) a un proveedor argentino chico. Es una mala noticia para la idea.

**EE.UU.**
- DATO: la SEC dejó de defender su norma climática en marzo de 2025 [L7-21][L7-22]. El 2026-05-07 envió a revisión una propuesta para derogarla [L7-23].
- DATO: la ley de California **SB 253** obliga a las empresas con más de USD 1.000 millones de facturación que operan en California a reportar sus alcances 1 y 2 desde 2026 y el alcance 3 desde 2027. El regulador (CARB) pasó el primer vencimiento al **2026-11-10**, sujeto a que se apruebe su reglamento [L7-24][L7-25].

**CBAM (ajuste en frontera por carbono de la UE)**
- DATO: el período definitivo empezó el **2026-01-01**. Los certificados se compran **desde el 2027-02-01** y la primera declaración anual, que cubre 2026, vence el **2027-09-30** [L7-26]. Cubre hierro y acero, aluminio, cemento, fertilizantes, hidrógeno y electricidad (unos 570 códigos de producto). La extensión a productos derivados desde 2028 todavía no está aprobada [L7-26].
- DATO: el acuerdo de simplificación (2025-06-18) fijó un **mínimo de 50 toneladas por importador por año**. Con eso queda exento el 90 % de los importadores y se mantiene cubierto el 99 % de las emisiones [L7-27].
- DATO: según consultoras, el precio de referencia del primer trimestre de 2026 fue de €75,36 por tonelada de CO₂e [B, L7-26]. No lo verifiqué en una fuente oficial.
- **Argentina y el CBAM:** DATO: según PwC Argentina (mayo de 2024), el complejo siderúrgico exportó USD 1.103 millones en 2023, sobre todo a EE.UU., México y Canadá. El del aluminio exportó USD 885 millones, sobre todo al Mercosur. **La UE no figura entre los destinos principales** [L7-28]. En 2024, Aluar exportó USD 530 millones a EE.UU. [B, L7-29].
- OPINIÓN: **la exposición directa de Argentina al CBAM es chica.** Las obligaciones recaen sobre el importador europeo (el "declarante autorizado"), que le va a pedir datos de emisiones de planta al productor. Pocas empresas argentinas, y grandes (Aluar, Ternium, Acindar), tienen equipos o consultoras grandes para eso. Que el CBAM exija verificación por un organismo acreditado es conocimiento mío y no lo verifiqué en esta búsqueda.

**EUDR (reglamento europeo de deforestación)**
- DATO: el **Reglamento (UE) 2025/2650** (publicado el 2025-12-23) volvió a postergar la aplicación: **2026-12-30 para operadores medianos y grandes, y 2027-06-30 para micro y pequeños**. También simplificó trámites para los operadores que están más abajo en la cadena [L7-30][L7-31]. El 2026-05-04 la Comisión publicó su revisión de simplificación y **decidió no cambiar de nuevo el texto de base**. Estima que las simplificaciones bajan un 75 % los costos de cumplimiento [L7-32].
- DATO: los productos argentinos afectados son la **harina de soja, la carne vacuna (cuota Hilton y no Hilton) y los cueros**. El maíz podría sumarse en la campaña 2027/28. Argentina figura como país de **riesgo "estándar"**, así que no aplica la excepción para microempresas de países de riesgo bajo [L7-33].
- DATO: exportaciones argentinas a la UE (FECOI, julio de 2025): **harina de soja USD 628 millones (22 % del total exportado a la UE) y carne bovina USD 479 millones (49.000 t)**. La UE es el tercer socio comercial de Argentina (12 % del comercio en 2024) [L7-34].
- DATO: **VISEC** es la plataforma sectorial argentina, impulsada por la cámara aceitera (CIARA-CEC). Verifica con polígonos del campo (RENSPA) e imágenes satelitales que no haya deforestación desde diciembre de 2020 y emite una certificación. **La adhesión es voluntaria y gratuita para productores, acopios y exportadores** [L7-33]. Si se mezcla mercadería adherida con no adherida, hay que separarla físicamente, y eso genera sobrecostos [L7-33]. Otra fuente dice que el exportador paga el sistema y que al menos el 50 % de la producción anual ya está adentro [L7-47; B, no identifiqué cuál de las dos URL lo dice]: hay una contradicción sobre quién paga. **VISEC Carne** la financian el IPCVA y el Consorcio ABC. Los productores ganaderos debían inscribirse antes de junio de 2026 [L7-34].
- DATO: **Ucrop.it** (Argentina, 2018) traza cultivos y tiene una calculadora de huella. Es gratis para productores y pagan las empresas compradoras (exportadores, semilleras, bancos). Hizo un piloto con NASA Harvest sobre 10.000 ha [L7-35][L7-36]. No encontré sus precios.
- DATO: entre los proveedores globales de monitoreo satelital para la EUDR están LiveEO (TradeAware), osapiens, EOSDA, Cropin y SatSure [L7-48].
- OPINIÓN: en soja y carne, **el hueco ya lo está llenando un sistema sectorial gratuito (VISEC), respaldado por las cámaras.** Competir contra eso sin contactos es casi imposible. El espacio posible, a verificar, está en los **márgenes**: curtiembres (no encontré cómo las cubre VISEC), productores o frigoríficos chicos que no se adhirieron, y empresas que necesitan ayuda para cargar sus datos. Son hipótesis: no tengo evidencia de que alguien pague por eso.

**Normas técnicas y obligaciones en Argentina**
- **GHG Protocol** e **ISO 14064-1** miden emisiones de una organización. **ISO 14067** mide la huella de un producto. Esto es la definición general de las normas; no lo verifiqué contra el texto de ISO en esta búsqueda. Un estudio del INTA sobre té argentino usó ISO 14067, 14040 y 14044 con SimaPro, un software de análisis de ciclo de vida [L7-37].
- DATO: **CNV, RG 1115/2026** (desde el 2026-03-02): la Memoria Anual de las empresas que cotizan debe incluir un apartado de política ambiental y de sostenibilidad, con indicadores, bajo el principio de "cumplir o explicar" [L7-38]. **No pude verificar si obliga a reportar gases de efecto invernadero (GEI).**
- DATO: **Mendoza (Decreto 758/2025, 2025-04-16)** obliga a medir y reportar **cada año los alcances 1 y 2** a las actividades medianas y grandes de industria, energía, transporte, agro, servicios y residuos. El alcance 3 es optativo. También exige **planes de reducción**, con metodologías como IPCC, GHG Protocol o ISO 14064 [L7-39]. El Decreto 1338/2026 (agosto de 2026) redefinió quiénes reportan: las fuentes fijas registradas o las que designe la autoridad, "con independencia de su tamaño" [L7-40].
- DATO: **Neuquén, Resolución 258/2025**: el reporte de emisiones pasa a ser obligatorio para el sector de hidrocarburos [L7-41].
- OPINIÓN: **Mendoza es la demanda regulatoria local más concreta que encontré.** Hay empresas medianas obligadas a medir y presentar planes todos los años. Hay que verificar cuántas son y si el reporte requiere un profesional matriculado.

## 2.4 ¿Cuánto se cobra hoy en Argentina?

- DATO: un presupuesto de 2024 de la cooperativa Regenera cobra **USD 1.350 por una huella corporativa (IRAM-ISO 14064-1:2020)**, con un plazo aproximado de un mes y pago de 70 % al inicio y 30 % al final. Aparte va el visado del Colegio de Especialistas, de unos ARS 175.000 en agosto de 2024 [L7-42]. **Este dato lo vi solo en el resumen del buscador. Intenté abrir el documento y no se pudo leer, así que no está confirmado.**
- DATO: la UIA, con PAGE y ONUDI, lanzó una metodología para que las pymes midan su huella. Sus programas Ruta X y Ruta Verde asistieron a más de 300 empresas [L7-43]. La Universidad Nacional de La Plata anunció una certificación propia y un registro de profesionales [L7-44].
- DATO: en España, el precio medio de un certificado de huella ronda los €3.000 más IVA (comparador español) [L7-45]. No es comparable con Argentina.
- DATO: la UTN Bahía Blanca dicta un programa de posgrado sobre huella de carbono [L7-46]. Existe formación local.

## 2.5 Veredicto L7 (OPINIÓN, con razonamiento)

### L7a: app de huella para personas, con suscripción

| Criterio | Puntaje | Una línea |
|---|---|---|
| Tamaño del problema | 2 | Para la mayoría de la gente no es un dolor sentido, es una preocupación abstracta. |
| Disposición a pagar | 1 | Klima se vendió y se cerró, Commons dejó el seguimiento gratis y Earth Hero es gratis. No encontré casos que vivan de suscripciones. |
| Espacio frente a la competencia | 3 | Hay varias apps gratuitas y sostenidas por fundaciones o capital de riesgo. |
| Ventaja de Facu | 2 | No tiene audiencia, datos ni marca en el tema. |
| Factibilidad | 7 | Una calculadora es fácil de construir. |
| Escalabilidad | 3 | Escala técnicamente, pero no tiene con qué monetizar. |
| Riesgo (10 = bajo) | 5 | Se pierde poca plata, pero lo más probable es facturar cero. |

**Puntaje global: 2/10. Descartar.** Versión chica, solo si Facu quiere confirmarlo él mismo: una página con 2 planes (gratis o pago) y USD 50–100 en anuncios. Medir cuántos hacen clic en "pagar". **Gate:** si menos del 2 % de las visitas hace clic en el plan pago, se cierra. Mi recomendación es no gastar ni eso: la evidencia ya es bastante clara.

### L7b: servicio o herramienta para empresas y exportadores

| Criterio | Puntaje | Una línea |
|---|---|---|
| Tamaño del problema | 5 | Hay obligación real (EUDR desde 2026-12-30, Mendoza, CNV), pero el Ómnibus achicó el pedido europeo, el CBAM toca poco a Argentina y VISEC ya cubre soja y carne. |
| Disposición a pagar | 5 | Se paga por obligación: unos USD 1.350 por huella corporativa (dato a confirmar) y unos €7.500 por cliente por año en software europeo (ESTIMACIÓN). Las pymes argentinas pagan poco. |
| Espacio frente a la competencia | 3 | VISEC (gratis), Ucrop.it, consultoras grandes, cooperativas, UIA y UNLP, más proveedores satelitales globales. Greenly dice que el mercado está "saturado". |
| Ventaja de Facu | 4 | Ingeniería industrial (balances de energía y materiales, procesos) sirve para inventarios de GEI, pero no tiene experiencia, matrícula específica ni contactos. Con inglés básico, venderle a importadores europeos es difícil. |
| Factibilidad | 5 | Como servicio es posible con una capacitación (ISO 14064 o 14067) y la alianza con un profesional que firme. Como software, compite contra empresas con decenas de millones de euros. |
| Escalabilidad | 4 | Al principio es un servicio que vende horas. Se puede productizar (plantillas y una herramienta para un nicho como Mendoza o curtiembres), pero el techo es local. |
| Riesgo (10 = bajo) | 4 | La regulación cambia todo el tiempo: el Ómnibus, la SEC, la EUDR postergada dos veces, el CBAM simplificado. Un cambio de reglas puede borrar la demanda. |

**Puntaje global: 4/10.** No construir nada todavía: **validar con entrevistas.** OPINIÓN: encaja mejor como **módulo de la consultora de mejora de procesos** (ficha `ideas/2026-09-07-consultora-mejora-procesos.md`) que como empresa aparte. Medir energía y materiales para bajar costos y medir emisiones son casi el mismo trabajo, y la reducción de emisiones vende mejor cuando también baja costos. Esto es una hipótesis, sin evidencia todavía.

**Versión chica para validar (2–4 semanas, menos de USD 200, casi todo es tiempo)**
1. **Semana 1, leer los textos oficiales (USD 0):** el Decreto 758/2025 y el 1338/2026 de Mendoza, con la Resolución 1/2026 (¿quién está obligado?, ¿cuántos son?, ¿hace falta un profesional matriculado?), la RG CNV 1115/2026 y la guía de VISEC (¿qué pasa con los cueros?, ¿quién paga?).
2. **Semanas 1–3, 20 entrevistas (USD 0–50):** a 3 segmentos:
   (a) empresas medianas de Mendoza alcanzadas por el decreto. Bodegas, agroindustria y metalurgia son una hipótesis mía de rubros, sin verificar;
   (b) curtiembres y frigoríficos chicos que exportan a la UE;
   (c) pymes proveedoras de clientes europeos.
   Preguntas clave: "¿En los últimos 12 meses les pidieron datos de emisiones o de trazabilidad? ¿Quién lo resolvió? ¿Cuánto pagaron o les presupuestaron? ¿Qué les dolió?". Canales: LinkedIn, cámaras sectoriales, la Coordinación de Sostenibilidad de Mendoza y los talleres gratuitos que organiza la provincia.
3. **Semanas 3–4, oferta concreta:** a quien haya mostrado dolor, ofrecerle un "diagnóstico de alcances 1 y 2" chico, gratis o a precio simbólico, como piloto, junto con un profesional que firme.
4. **Gate:** al menos 5 de 20 empresas con un pedido real (del cliente o del regulador) y al menos 1 que acepte pagar algo, o un piloto con compromiso de pago. Si se cumple, recién ahí pagar una capacitación formal en ISO 14064. Si no, cerrar y escribir el post-mortem. **Pérdida máxima: USD 200. Fecha de corte: 4 semanas.**

---

## Pendientes (no pude buscarlos porque se agotó el cupo de búsquedas)

1. Startups o software argentinos de huella de carbono para empresas (competencia local directa).
2. Encuestas de disposición a pagar por apps de huella personal.
3. Estado del acuerdo UE-Mercosur (cambia la importancia de exportar a la UE).
4. Descargas de Ratoneando, PrecioYa, "Calculadora de compras", "SuperJusto" y otras (hay que abrir cada ficha de Google Play).
5. Confirmar el presupuesto de Regenera (USD 1.350) en la fuente original.
6. Cuántas empresas están alcanzadas por el decreto de Mendoza y si exige un profesional matriculado.

---

## Fuentes

[A] = la abrí y la leí. [B] = la vi solo en el resumen del buscador. Todas fueron consultadas el 2026-10-08. La fecha indicada es la de publicación, cuando se conoce.

### L2
- [L2-1] [B] Perfil, "El Gobierno difundirá 12 millones de precios diarios de supermercados" (agosto de 2024): https://www.perfil.com/noticias/economia/el-gobierno-difundira-12-millones-de-precios-diarios-de-supermercados-como-funciona-el-sistema.phtml
- [L2-2] [B] El Economista, "Precios SEPA: el Gobierno habilitó plataforma…" (agosto de 2024): https://eleconomista.com.ar/economia/precios-sepa-gobierno-habilito-plataforma-conocer-12-millones-precios-n76774
- [L2-3] [A] Precios Claros (sitio oficial), consultado el 2026-10-08: https://www.preciosclaros.gob.ar/
- [L2-4] [B] iProfesional, nota sobre Ratoneando (cobertura de abril de 2024): https://www.iprofesional.com/economia/403514-supermercados-como-funciona-web-para-comparar-precios-ahorrar
- [L2-5] [B] Río Negro, "¿Querés encontrar los mejores precios…? Ratoneando…": https://www.rionegro.com.ar/?p=3387552
- [L2-6] [A] Ratoneando, sitio, consultado el 2026-10-08: https://ratoneando.ar/
- [L2-7] [A] iProfesional, "Argentinos crearon app para ahorrar en el supermercado" (2024-08-31): https://www.iprofesional.com/tecnologia/412128-argentinos-crearon-app-ahorrar-supermercado-como-funciona
- [L2-8] [A] Canal 26, "Tecnología al servicio del ahorro: las apps para comparar precios…" (2025-08-20): https://www.canal26.com/economia/2025/08/20/tecnologia-al-servicio-del-ahorro-las-apps-para-comparar-precios-que-estan-revolucionando-el-bolsillo/
- [L2-9] [B] InfoNegocios, "PrecioYa, la app que compara precios de supermercados…" (sin fecha visible): https://infonegocios.info/plus/precioya-la-app-que-compara-precios-de-supermercados-en-tiempo-real-con-diferencias-de-hasta-81-por-el-mismo-producto
- [L2-10] [B] LM Neuquén, "Una app cipoleña que ayuda a ahorrar en el súper" (sin fecha visible): https://www.lmneuquen.com/una-app-cipolena-que-ayuda-ahorrar-el-super-n674887
- [L2-11] [A] Google Play Argentina, búsqueda "calculadora supermercado escanear precio", consultada el 2026-10-08: https://play.google.com/store/search?q=calculadora%20supermercado%20escanear%20precio&c=apps&hl=es_AR&gl=AR
- [L2-12] [B] App Store Argentina, "Carrefour Argentina": https://apps.apple.com/ar/app/carrefour-argentina/id6472512419
- [L2-13] [B] Revista Mercado, "Carrefour presenta una App de ahorro creada por sus propios clientes": https://mercado.com.ar/protagonistas/carrefour-presenta-una-app-de-ahorro-creada-por-sus-propios-clientes
- [L2-14] [B] Perfil, "Argentina ya tiene su primer supermercado inteligente sin sector de cajas": https://www.perfil.com/noticias/modo-fontevecchia/argentina-ya-tiene-su-primer-supermercado-inteligente-sin-sector-de-cajas-modof.phtml
- [L2-15] [B] App Store España, "Scan and Go" (Carrefour): https://apps.apple.com/es/app/id1503326363
- [L2-16] [B] Mercado & Consumo, "Carrefour abre lojas tecnológicas sem atendentes" (2021-03-26): https://mercadoeconsumo.com.br/2021/03/26/carrefour-abre-lojas-tecnologicas-sem-atendentes/
- [L2-17] [B] Chain Store Age, "Walmart pulls the plug on self-checkout app" (2018): https://chainstoreage.com/technology/walmart-reportedly-pulling-the-plug-on-self-checkout-app/
- [L2-18] [B] NFCW, "Walmart cancelled in-aisle self-checkout project due to high levels of shopper theft" (2019): https://www.nfcw.com/?p=61650
- [L2-19] [B] Listonic, "Listonic case" (página de la empresa, sin fecha): https://dev.listonic.com/listonic-case
- [L2-20] [B] App Store Polonia, "Lista zakupów - Listonic" (sin fecha): https://apps.apple.com/pl/app/lista-zakup%C3%B3w-listonic/id331302745?l=pl
- [L2-21] [B] Dealroom, Bring!: https://app.dealroom.co/companies/bring_
- [L2-22] [A] Horizont, "Bilanz und Ausblick: Bring! Labs…" (2025-02-04): https://www.horizont.net/schweiz/nachrichten/bilanz-und-ausblick-bring-labs-startet-mit-positiver-jahresbilanz-in-zehnjaehriges-firmenjubilaeum-225608
- [L2-23] [B] Bring!, "Successful business year for Bring! Labs AG" y "Shopping app Bring! continues its course for growth in 2021": https://getbring.com/magazin/successful-business-year-for-bring-labs-ag ; https://getbring.com/magazin/shopping-app-bring-continues-its-course-for-growth-in-2021
- [L2-24] [A] RevenueCat, State of Subscription Apps 2026, página de hallazgos (aprox. marzo de 2026): https://revenuecat.com/sosa-26-insights/
- [L2-25] [B] RevenueCat, State of Subscription Apps 2025 (marzo de 2025): https://revenuecat.com/state-of-subscription-apps-2025
- [L2-26] [B] Revista Mercado, "Streaming: cada vez más argentinos comparten suscripciones o se dan de baja": https://mercado.com.ar/protagonistas/streaming-cada-vez-mas-argentinos-comparten-suscripciones-o-se-dan-de-baja
- [L2-27] [B] Diario Panorama, "Argentinos gastaron 780.000 dólares en aplicaciones para buscar citas durante 2022": https://www.diariopanorama.com/noticia/442137/argentinos-gastaron-780000-dolares-aplicaciones-para-buscar-citas-durante-2022
- [L2-28] [B] Contexto Tucumán, "En apps, Netflix y Spotify los argentinos gastaron US$1.000 millones…" (sin fecha visible): https://www.contextotucuman.com/nota/405966/en-apps-netflix-y-spotify-los-argentinos-gastaron-u$s-1-000-millones-durante-este-ano.html
- [L2-29] [B] FoodNavigator-USA, "Waze for groceries? Basket app…" (2019-01-04): https://www.foodnavigator-usa.com/Article/2019/01/04/Waze-for-groceries-Basket-app-deploys-crowdsourcing-for-real-time-pricing-info
- [L2-30] [B] ARLnow, Fobi adquiere Basket (2022): https://www.arlnow.com/?p=270001
- [L2-31] [B] CB Insights, Basket: https://www.cbinsights.com/company/basket-1 ; https://www.cbinsights.com/company/basket-savings
- [L2-32] [B] Better Retailing, "mySupermarket grocery price comparison closes": https://betterretailing.com/mysupermarket-grocery-price-comparison-closes
- [L2-33] [B] Digital in Asia, "Retail Tech Consumer Analytics Startup Shooper Raises US$130k": https://digitalinasia.com/retail-tech-consumer-analytics-startup-shooper-raises-us130k/
- [L2-34] [B] MarTech, "Nielsen-backed OurCart startup launches Snapstar app…": https://martech.org/nielsen-backed-ourcart-startup-launches-snapstar-app-incentivize-brand-loyalty-grocery-shoppers/
- [L2-35] [B] Tiempo Argentino, "El consumo no reacciona: cayó 1,5% en agosto" (septiembre de 2026): https://www.tiempoar.com.ar/ta_article/el-consumo-no-reacciona-cayo-15-en-agosto/
- [L2-36] [B] Ámbito, "Equifax se alía con Scentia para potenciar soluciones retail" (2016-03-22): https://www.ambito.com/ambito-biz/equifax-se-alia-scentia-potenciar-soluciones-retail-n3932276
- [L2-37] [B] Kantar Worldpanel, "Kantar Worldpanel expands its consumer panel in Argentina" (2017): https://kantarworldpanel.com/global/News/Kantar-Worldpanel-expands-its-consumer-panel-in-Argentina
- [L2-38] [A] Diario Estrategia (Chile), "Startup chilena se consolida en Argentina" (Rocketpin, 2019-04-22): https://www.diarioestrategia.cl/texto-diario/mostrar/1393539/startup-chilena-consolida-argentina
- [L2-39] [B] Tiempo Argentino (igual que L2-35), datos de Scentia de agosto de 2026.
- [L2-40] [B] Infobae, "El consumo masivo cayó 2,7% en junio…" (2026-07-23): https://www.infobae.com/economia/2026/07/23/el-consumo-masivo-cayo-27-en-junio-y-acumula-una-baja-de-casi-3-en-2026/
- [L2-41] [B] iProUP, "Inflación de agosto: dato oficial INDEC…" (septiembre de 2026): https://www.iproup.com/finanzas/71297-inflacion-agosto-dato-oficial-indec-confirma-cuanto-llego-ipc-acumulado-anual-precios-2026
- [L2-42] [B] América Retail, "La nueva herramienta digital que redefine la experiencia en supermercados en Argentina" (sin fecha visible): https://americaretail-malls.com/paises/argentina/la-nueva-herramienta-digital-que-redefine-la-experiencia-en-supermercados-en-argentina/
- [L2-43] [B] Richify, calculadora de inflación (cita el calendario del INDEC): https://www.richify.ai/ar/calculadora-inflacion

### L7
- [L7-1] [A] Sustainable Jungle, "Best carbon offset programs" (menciona la compra de Klima por Wren en mayo de 2025): https://www.sustainablejungle.com/best-carbon-offset-programs
- [L7-2] [B] Dealroom, Klima: https://dealroom.co/companies/klima/
- [L7-3] [B] TIME, Joro (2022): https://time.com/collection-post/6159458/joro
- [L7-4] [B] Crunchbase News, Sanchali Pal / Joro: https://news.crunchbase.com/news/sanchali-pal-joro-something-ventured-2
- [L7-5] [B] Princeton Alumni Weekly, "Sanchali Pal '12…": https://paw.princeton.edu/article/sanchali-pal-12-helping-consumers-live-more-sustainably
- [L7-6] [A] Commons, "Guide to Carbon Footprint Tracking" (2023-03-06; pie de página de 2025): https://www.thecommons.earth/blog/carbon-footprint-tracking
- [L7-7] [B] Bloomberg, "Want to track your carbon footprint? There are apps for that" (2024-08-11): https://www.bloomberg.com/news/articles/2024-08-11/want-to-track-your-carbon-footprint-there-are-apps-for-that
- [L7-8] [B] App Store, Earth Hero: https://apps.apple.com/app/id1458057746
- [L7-9] [B] Boston Globe, "Climate tracking apps measure carbon footprint" (2025-09-09): https://www.bostonglobe.com/2025/09/09/science/climate-tracking-apps-measure-carbon-footprint/
- [L7-10] [B] Dealroom, Capture: https://app.dealroom.co/companies/capture_1
- [L7-11] [B] Silicon Canals, "CarbonCancel shuts shop": https://siliconcanals.com/carboncancel-shuts-shop/
- [L7-12] [B] ESG Today, "Watershed raises $70 million, reaching $1 billion valuation" (febrero de 2022): https://www.esgtoday.com/climate-solutions-platform-watershed-raises-70-million-reaching-1-billion-valuation/
- [L7-13] [B] ESG Today, "Corporate Climate Platform Watershed Raises $100 Million" (febrero de 2024): https://www.esgtoday.com/corporate-climate-platform-watershed-raises-100-million/
- [L7-14] [B] Axios Pro, "Persefoni raises $50M led by TPG" (2023-08-11): https://www.axios.com/pro/climate-deals/2023/08/11/persefoni-raises-50m-led-by-tpg-kentaro-kawamori
- [L7-15] [B] The SaaS News, "Persefoni raises $23M in Series C extension" (marzo de 2025): https://www.thesaasnews.com/news/persefoni-raises-23m-in-series-c-extension/
- [L7-16] [B] Responsible Investor, "Carbon accounting market 'in consolidation phase, big time'" (fecha no verificada): https://www.responsible-investor.com/carbon-accounting-market-in-consolidation-phase-big-time-says-persefoni-co-founder/
- [L7-17] [A] ESG Today, "Greenly Acquires Normative as Carbon Accounting Consolidation Accelerates" (2026-09-11): https://esgtoday.com/greenly-acquires-normative-as-carbon-accounting-consolidation-accelerates
- [L7-18] [B] rfp.wiki, Watershed vs Normative: https://www.rfp.wiki/sustainability-esg/carbon-accounting-and-management-software/watershed/normative
- [L7-19] [B] Herbert Smith Freehills Kramer, "Omnibus I update: CSRD and CSDDD amendment directive published in the Official Journal" (2026): https://www.hsfkramer.com/notes/esg/2026-posts/omnibus-i-update-csrd-and-csddd-amendment-directive-published-in-the-official-journal
- [L7-20] [B] Morrison Foerster, "EU Sustainability Omnibus I – Detailed Omnibus Adopted" (2025-12-22): https://mofo.com/resources/insights/251222-eu-sustainability-omnibus-i-detailed-omnibus ; PwC Luxemburgo: https://www.pwc.lu/en/sustainable-finance/eu-finalises-agreement-on-omnibus.html
- [L7-21] [B] CATF, "SEC abandons defense of climate-related disclosure rules" (marzo de 2025): https://www.catf.us/2025/03/sec-abandons-defense-of-climate-related-disclosure-rules-reducing-investor-access-to-material-information/
- [L7-22] [B] Cahill, "SEC Abandons Climate Disclosure Rules" (2025-04-10): https://www.cahill.com/publications/client-alerts/2025-04-10-sec-abandons-climate-disclosure-rules
- [L7-23] [B] TheCorporateCounsel.net, "SEC submits climate disclosure rulemaking to OIRA" (2026-05-06): https://www.thecorporatecounsel.net/blog/2026/05/but-wait-theres-more-sec-submits-climate-disclosure-rulemaking-to-oira.html
- [L7-24] [B] Sidley, "SB 253 Update: CARB Delays Reporting Deadline to November 2026" (2026-06-30): https://environmentalhealthsafetybrief.sidley.com/2026/06/30/sb-253-update-carb-delays-reporting-deadline-to-november-2026-and-proposes-to-clarify-requirements/
- [L7-25] [B] Linklaters, "California SB 253: CARB defers first-year reporting deadline to November 10": https://sustainablefutures.linklaters.com/post/102n6f5/california-sb-253-carb-defers-first-year-reporting-deadline-to-november-10
- [L7-26] [B] Tanso, "CBAM 2026: who is affected, 50-tonne threshold, costs, obligations" y PwC Suiza, "CBAM in focus": https://www.tanso.de/en/blog/cbam-2026-who-is-affected-50-tonne-threshold-costs-obligations ; https://www.pwc.ch/en/insights/cbam-in-focus-preparing-for-the-definitive-regime.html
- [L7-27] [A] Parlamento Europeo, "CBAM: Deal with Council to simplify EU carbon leakage instrument" (2025-06-18): https://www.europarl.europa.eu/news/en/press-room/20250613IPR28918/cbam-deal-with-council-to-simplify-eu-carbon-leakage-instrument
- [L7-28] [A] Economía Sustentable, "Alertan que los exportadores argentinos deberán adaptarse al ajuste de carbono de la UE" (análisis de PwC Strategy&, sin fecha visible; el informe de PwC es de mayo de 2024): https://economiasustentable.com/noticias/alertan-que-los-exportadores-argentinos-deberan-adaptarse-al-ajuste-de-carbono-de-la-ue-para-evitar-sanciones/amp/ ; informe original (no pude abrirlo, error 403): https://www.strategyand.pwc.com/ar/es/publicaciones/mecanismo-ajuste-fronterizo-carbono.html
- [L7-29] [B] Infobae, "Acero y aluminio en alerta…" (2025-06-06): https://www.infobae.com/economia/2025/06/06/acero-y-aluminio-en-alerta-la-suba-de-aranceles-de-eeuu-paralizan-ventas-y-las-empresas-esperan-un-gesto-del-gobierno/
- [L7-30] [B] EY Tax News, "EU Deforestation Regulation application postponed to 30 December 2026" (2026-01-20): https://taxnews.ey.com/news/2026-0237-eu-deforestation-regulation-application-postponed-to-30-december-2026
- [L7-31] [B] Comisión Europea (Access2Markets), "Delay until December 2026 and other developments in the implementation of the EUDR Regulation": https://trade.ec.europa.eu/access-to-markets/en/news/delay-until-december-2026-and-other-developments-implementation-eudr-regulation
- [L7-32] [B] Baker McKenzie, "EU Commission publishes simplification review of EUDR" (mayo de 2026): https://www.bakermckenzie.com/en/insight/publications/2026/05/eu-commission-publishes-simplification-review-of-eudr ; ESG Today: https://www.esgtoday.com/?p=23495
- [L7-33] [A] Bichos de Campo, "Preocupación de los exportadores por la entrada en vigencia del reglamento antideforestación…" (2025-10-23): https://bichosdecampo.com/preocupacion-de-los-exportadores-por-la-entrada-en-vigencia-del-reglamento-antideforestacion-en-europa-en-los-proximos-dias-invitaran-a-los-productores-a-sumarse-gratuitamente-al-visec/
- [L7-34] [A] Innovación Digital 360, "EUDR: trazabilidad en la cadena cárnica argentina…" (2026-05-07; cita datos de FECOI de julio de 2025): https://www.innovaciondigital360.com/agrotech/agrotech-eudr-trazabilidad-cadena-carnica-argentina-exportacion-europa/
- [L7-35] [B] Forbes Argentina, "La startup argentina que certifica sustentabilidad de cultivos…" (enero de 2024): https://www.forbesargentina.com/money/la-startup-argentina-certifica-sustentabilidad-cultivos-tecnologia-blockchain-hoy-opera-9-paises-n46590
- [L7-36] [B] AgFunderNews, "Argentine ag blockchain platform ucrop.it raises seed funding": https://agfundernews.com/ucrop-it-argentine-food-traceability-blockchain-platform-raises-seed-funding
- [L7-37] [B] INTA, "Huella de carbono del té certificado en Argentina": https://repositorio.inta.gob.ar/handle/20.500.12123/14735
- [L7-38] [B] Revista Mercado, "La CNV exige reportes de sostenibilidad y gobierno corporativo en la Memoria Anual" (2026): https://mercado.com.ar/gestion-sustentable/la-cnv-exige-reportes-de-sostenibilidad-y-gobierno-corporativo-en-la-memoria-anual
- [L7-39] [A] Gobierno de Mendoza, "Mendoza establece la obligatoriedad de medir y reportar la huella de carbono para grandes generadores" (2025-04-16): https://www.mendoza.gov.ar/prensa/mendoza-establece-la-obligatoriedad-de-medir-y-reportar-la-huella-de-carbono-para-grandes-generadores/
- [L7-40] [B] Marval O'Farrell Mairal, "Mendoza: reporte de emisiones de Gases de Efecto Invernadero" (agosto de 2026): https://www.marval.com/Publicacion/mendoza-reporte-de-emisiones-de-gases-de-efecto-invernadero-17723
- [L7-41] [B] Marval O'Farrell Mairal, "Neuquén: programa de monitoreo de emisiones en hidrocarburos": https://www.marval.com/Publicacion/neuquen-programa-de-monitoreo-de-emisiones-en-hidrocarburos-17174
- [L7-42] [B, no confirmado] Google Docs, "SERVICIO DE HUELLA DE CARBONO" (presupuesto de la cooperativa Regenera, 2024). Intenté abrirlo y no se pudo leer: https://docs.google.com/document/d/1zLFS0O-Zat4bwdH_L6deO0aLL0n3vW73/
- [L7-43] [B] Ámbito, "Producción sostenible: lo que era visto como un costo…": https://www.ambito.com/negocios/produccion-sostenible-lo-que-era-visto-como-un-costo-las-empresas-ahora-es-una-forma-ganar-competitividad-n6268063
- [L7-44] [B] Bichos de Campo, "La Universidad Nacional de La Plata se lanza a competir con las certificadoras privadas de la huella de carbono": https://bichosdecampo.com/con-ganas-de-impulsar-el-mercado-local-de-bonos-la-universidad-nacional-de-la-plata-se-lanza-a-competir-con-las-certificadoras-privadas-de-la-huella-de-carbono
- [L7-45] [B] Certicalia (España), "Certificado huella de carbono en Ávila": https://www.certicalia.com/certificado-huella-de-carbono/avila
- [L7-46] [B] UTN Facultad Regional Bahía Blanca, programa de huella de carbono (posgrado): https://www.frbb.utn.edu.ar/frbb/info/secretarias/academica/carreras/posgrado/mia/programas/programa_huella_carbono.pdf
- [L7-47] [B] Datamar News, "From field to port: Argentina, Chile, Paraguay, and Uruguay building EUDR compliance": https://datamarnews.com/?p=72281 ; AL-INVEST Verde, "AL-INVEST green introduces VISEC traceability system…": https://alinvest-verde.eu/en_gb/al-invest-verde-presenta-el-sistema-de-trazabilidad-visec-para-verificar-el-comercio-de-productos-libres-de-deforestacion/
- [L7-48] [B] osapiens, "Evaluación del riesgo de deforestación de EUDR mediante análisis satelital": https://osapiens.com/es/gestion-de-riesgos-de-eudr-satellite ; EOSDA, "El EUDR impulsa la demanda de datos satelitales": https://eos.com/es/blog/el-eudr-impulsa-la-demanda-de-datos-satelitales/ ; Cropin, "EUDR compliance solution": https://cropin.com/intelligent-agriculture-cloud/solutions/eudr-compliance-solution
- [L7-49] [B] Preqin, Watershed Technology Inc.: https://www.preqin.com/data/profile/asset/watershed-technology-inc-/468065
