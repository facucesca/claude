# Indagación a fondo: "Stock de piezas chicas" (L14 + COM-3-5 + X1d + K11) (2026-10-15)

> Informe del investigador de mercado para Facu. Fecha de corte: **2026-10-15**.
> Tema: la parte física de la "idea integral de ingeniería industrial". Junta L14 (stock de piezas chicas, anti-robo, "¿por peso?"), COM-3-5 (identificar una pieza por foto, sobre una regla, y saber dónde está), X1d (pick-to-light) y K11 (vencimientos y FIFO).
>
> **Marcas que uso en todo el documento:**
> - **[DATO]**: viene de una fuente con URL (lista en la sección 9). Pongo la fecha de publicación cuando la conozco.
> - **[DATO-EMPRESA]**: lo dice la propia empresa sobre sí misma. Tiene conflicto de interés.
> - **[ESTIMACIÓN]**: cálculo mío, con el razonamiento a la vista.
> - **[OPINIÓN]**: juicio mío.
> - **[NO VERIFICADO]**: no lo pude confirmar.
>
> **Método:** 15 búsquedas web (el tope) y unas 45 lecturas de páginas, todas el 2026-10-15. El buscador está pensado para EE.UU. y devolvió poco sobre Argentina. Por eso "no encontré" **no** quiere decir "no existe". Mercado Libre bloqueó las consultas, así que no tengo precios locales de balanzas ni de sensores.

---

## Resumen en 8 líneas

1. **El problema existe y está documentado:** la cámara del sector (CAFARA) dice que una ferretería promedio maneja **20.000 artículos o más**, y que muchos clientes llegan "sin saber siquiera el nombre" de lo que buscan [DATO, gacetilla de ExpoFerretera, julio de 2023].
2. **El mercado:** CAFARA estima **unas 15.000 ferreterías** en el país, aunque aclara que no hay registro oficial. En los datos oficiales del CEP XXI hay **4.562 empresas con empleados** en venta minorista de ferretería y materiales eléctricos, y **4.304** en repuestos de autos (octubre de 2023) [DATO].
3. **Los sistemas argentinos que revisé** (Tango, Flexxus, Zoo Logic, Dux, YoFacturo) cubren facturación, stock y precios. **En las páginas que leí, ninguno ofrece búsqueda por foto, ubicación de cada pieza en el cajón ni pick-to-light** [DATO sobre esas páginas]. Ahí hay un hueco, o falta de demanda. Todavía no sé cuál de las dos.
4. **Afuera, la tecnología existe y la pagan empresas grandes:** foto → pieza (nyris, Partium, con clientes como IKEA, Hornbach y The Home Depot), cajones que pesan y piden reposición solos (Bossard SmartBin, TeDaLoS), pick-to-light (ekko, Lightning Pick) y cámaras con IA contra robo (Veesion). No encontré a nadie que lo junte para la ferretería de barrio.
5. **El RFID no sirve para tornillos sueltos.** Con piezas metálicas chicas y juntas, la lectura falla sea cual sea la etiqueta [DATO, RFID Journal]. **Contar por foto tampoco anda bien.** **El peso sí funciona para contar**, con límites conocidos.
6. **[OPINIÓN] Lo difícil no es la IA, son los datos:** sin un catálogo con foto, ubicación y peso unitario de cada artículo, el buscador por foto no tiene contra qué comparar. Cargar eso en un comercio con 20.000 artículos es mucho trabajo. Por eso conviene arrancar como **servicio + software**.
7. **Filtro: 16/25.** Recomendación: **PRIMERA, pero acotada** al núcleo de software (buscador por foto y por nombre + ubicaciones) en **tornillería de ferreterías y bulonerías**. El hardware (peso en estantes, luces, cámaras) queda **PENDIENTE**.
8. **Primer experimento:** 30 días, hasta USD 300. Se hacen 15 entrevistas, un catálogo piloto de 200 piezas en un comercio, una prueba a ciegas con 50 piezas y una oferta de piloto pago.

---

## 1. Qué es exactamente (especificación integrada)

### 1.1 El problema

- Los comercios de piezas chicas tienen **miles de artículos casi iguales**: el mismo tornillo en 10 largos, 3 roscas y 2 materiales. CAFARA habla de **20.000 o más artículos** en una ferretería promedio [DATO].
- El cliente llega con la pieza en la mano, con una foto o con una descripción vaga. CAFARA lo cuenta con humor: "el coso de la mochila del baño" era un flotador [DATO, Diario Jornada, 2023-09-02]. Encontrar el código depende de la memoria del ferretero.
- **El stock del sistema no coincide con el del cajón.** No encontré un dato argentino. En EE.UU., un estudio de casi 370.000 registros de inventario de 37 locales de un minorista encontró que **el 65% estaba mal** [DATO, DeHoratius y Raman, *Management Science*, 2008]. Es otro rubro y otro país: sirve como referencia, no como dato de ferreterías.
- Las piezas chicas **se pierden, se roban o se mezclan**, y el faltante se descubre recién cuando un cliente pide la pieza.
- Contar a mano miles de piezas es lento. Ese problema ya está en el registro como K14 / COM-3-3 (repetida). Acá aparece como un módulo, no como idea nueva.

### 1.2 Quién lo sufre y quién paga

| Rol | Qué sufre | ¿Paga? |
|---|---|---|
| Vendedor de mostrador | Pierde tiempo buscando y depende de la memoria. Si es nuevo, no encuentra nada | No |
| Dueño o encargado | Ventas perdidas, faltantes, robo hormiga, horas de conteo, depende de empleados "que saben" | **Sí: es el comprador** |
| Cliente (plomero, electricista, particular) | Espera, o se va sin la pieza | No |
| Distribuidor o mayorista de bulones | Si su cliente tiene faltantes, le compra menos o le compra a otro | **Variante posible: podría pagarlo para dárselo a sus clientes** (es lo que hacen Bossard o Würth con la industria) [OPINIÓN] |

### 1.3 Qué hace (los módulos)

**Antes de seguir, lo que NO es [OPINIÓN]:** no es un sistema de gestión. No factura ni reemplaza a Tango, Flexxus o el sistema que ya tenga el comercio. Es una **capa física del stock** que se conecta con ese sistema, primero por Excel y después por integración. Pelear contra los sistemas de gestión con facturación ante ARCA es otra guerra, y ya tiene muchos jugadores.

| # | Módulo | Qué hace | Idea de origen | Tipo | Prioridad [OPINIÓN] |
|---|---|---|---|---|---|
| M1 | **Catálogo vivo con ubicaciones** | Cada artículo con foto, medidas, sinónimos, ubicación (pasillo, estante, cajón) y peso unitario. Etiqueta QR por cajón. Permite altas y bajas rápidas porque "las piezas van variando" (comentario de Facu) | L14, X1 | Software + servicio de carga | **Base de todo** |
| M2 | **Buscador por foto y por nombre** | Foto de la pieza sobre un tapete impreso con regla o cuadrícula: la IA propone 3 a 5 candidatos del catálogo **de ese comercio**, con su ubicación. Búsqueda por nombre que entiende la jerga ("el cosito de la mochila"). Facu pidió que no sea solo para bulonerías | COM-3-5 | Software | **Primero** |
| M3 | **Conteo por peso** | Balanza cuentapiezas conectada: se escanea el QR del cajón, se pesa y el sistema calcula la cantidad. Sirve para inventario y para despachar | L14 ("¿por peso?") | Hardware comprado + software | Segundo |
| M4 | **Cajones que avisan** | Sensores de peso bajo los cajones de los artículos más importantes: avisan faltantes y retiros sin venta registrada | L14 (anti-robo) | Hardware + software | Pendiente |
| M5 | **Pick-to-light** | Se prende una luz en el cajón de lo que se busca o se arma | X1d | Hardware + instalación | Pendiente (sirve más en depósitos y mayoristas) |
| M6 | **Anti-robo con cámaras** | IA que mira las cámaras existentes y avisa gestos de robo | L14 | Mejor como alianza con quien ya lo hace | Pendiente / no construir |
| M7 | **Vencimientos y FIFO** | Para lo que vence: adhesivos, selladores, pinturas, pilas | K11 | Software | Menor en este nicho |
| S | **Servicio de puesta en orden** | Relevamiento, análisis ABC, nuevo orden de cajones, codificación, fotos y etiquetas | X1 / ing. industrial | Servicio | **Puerta de entrada** |

### 1.4 Cómo se cobraría [ESTIMACIÓN / OPINIÓN]

- **Instalación (pago único):** el servicio de orden y carga del catálogo, cobrado por cantidad de artículos o de cajones.
- **Suscripción mensual** por el software (M1, M2, M3, M7). Referencia local: los sistemas de gestión cuestan desde **ARS 20.000 por mes + IVA** (YoFacturo) y **ARS 43.699 a 57.621 por usuario por mes** (Flexxus) [DATO-EMPRESA]. Al dólar oficial de venta de hoy (ARS 1.535, según dolarapi.com), eso es **unos USD 13 a 38**. Un módulo complementario difícilmente cobre más que el sistema principal. **Rango razonable para testear: USD 15 a 40 por mes por comercio** [ESTIMACIÓN].
- **Hardware** (balanza, sensores, luces): reventa con margen, o alquiler incluido en el abono.
- **[ESTIMACIÓN] Lo que implica:** con USD 30 por mes, ganar USD 2.000 por mes en abonos exige **unos 67 comercios**, y cada uno requiere una instalación. Con solo el software en Argentina es un negocio chico o mediano. Para que sea grande tiene que pasar a otros países o reducir mucho el costo de instalación (ver la variante del catálogo compartido, en 6.6).

---

## 2. Mercado en Argentina

### 2.1 Datos oficiales: empresas con empleados por actividad (CEP XXI)

Fuente: dataset "Cantidad de empleadores que declararon trabajadores, por sector de actividad", del CEP XXI (Ministerio de Economía), con datos de AFIP/SIPA. El archivo por CLAE de 6 dígitos tiene datos mensuales **hasta 2023-10-01**, el último mes del archivo cuando lo leí el 2026-10-15. La página del dataset dice "última actualización 2022-04-07", pero el archivo llega a 2023.

| Código CLAE | Actividad (nombre oficial) | Empresas con empleados (2023-10) |
|---|---|---|
| 475230 | Venta al por menor de artículos de ferretería y materiales eléctricos | **4.562** |
| 466330 | Venta al por mayor de artículos de ferretería y materiales eléctricos | **1.209** |
| 475250 | Venta al por menor de artículos para plomería e instalación de gas | 474 |
| 453291 | Venta al por menor de partes, piezas y accesorios nuevos n.c.p. (automotor) | **4.304** |
| 453100 | Venta al por mayor de partes, piezas y accesorios de vehículos automotores | 1.663 |
| 454010 | Venta de motocicletas y de sus partes, piezas y accesorios | 1.043 |
| 475110 | Venta al por menor de hilados, tejidos y artículos de mercería | 689 |
| 464112 | Venta al por mayor de artículos de mercería | 116 |
| 471900 | Venta al por menor en comercios no especializados, sin predominio de alimentos y bebidas | 331 |

**Cómo leer esta tabla:**
- Cuenta **empresas (CUIT) privadas que declararon al menos un empleado**. **Deja afuera a los comercios sin empleados**, por ejemplo un monotributista que atiende solo, y una empresa con 3 locales cuenta una sola vez.
- Cada empresa figura en su actividad principal. **No existe un código para "bulonería".** Una bulonería minorista probablemente esté en 475230, y una mayorista en 466330. Esto último es inferencia mía [NO VERIFICADO].
- Los valores los leí en el CSV oficial en dos lecturas separadas, que coincidieron. Septiembre de 2023 da casi lo mismo: 4.564 en ferretería minorista y 4.298 en repuestos.

### 2.2 Dato de la cámara del sector (CAFARA)

- **"En Argentina, existen más de 15.000 ferreterías, lo que representa cerca de una cada 3000 habitantes. De estas, solo el 20% se dedican a comercio industrial, y el 80%** están destinadas a la venta para el consumidor final" [DATO, gacetilla de ExpoFerretera de julio de 2023, con declaraciones del presidente de CAFARA].
- La misma cifra de **unas 15.000** aparece en Diario Jornada (2023-09-02), que aclara que **no hay registros oficiales**, porque los rubros vecinos (sanitarios, electricidad, pinturerías) se mezclan [DATO].
- **"Una ferretería promedio tiene alrededor de 20.000 o más artículos"** [DATO, misma gacetilla]. Es la frase que mejor justifica el problema.
- La misma gacetilla dice que el software de gestión es un aporte de las nuevas generaciones [DATO]. Esto sugiere que la adopción es despareja, pero no da porcentajes.
- **CAFARA existe y está activa:** se presenta como la "única cámara empresarial que representa a las ferreterías de toda la Argentina a nivel nacional", dice trabajar desde 1905, edita la revista mensual *Ferreteros* y organiza ExpoFerretera (ya promociona la edición 2027 en La Rural) y "Espacio CAFARA Rosario 2026" [DATO-EMPRESA, cafara.org.ar].

### 2.3 Estimaciones (marcadas)

- **[ESTIMACIÓN] Universo total de ferreterías:** unas 15.000 (CAFARA) contra 4.562 empresas con empleados. Hay **unas 3,3 ferreterías por cada empresa con empleados**. La diferencia son comercios sin empleados registrados y sucursales.
- **[ESTIMACIÓN, confianza baja] Otros rubros con la misma proporción:** repuestos, 4.304 × 3,3 ≈ **14.000**; mercerías e hilados, 689 × 3,3 ≈ **2.300**. Es una regla de tres con un supuesto fuerte: que cada rubro tenga la misma proporción de comercios sin empleados que las ferreterías. No lo verifiqué.
- **[ESTIMACIÓN] Clientes con más chance de pagar:** las ferreterías y bulonerías **con empleados** (unas 4.562 minoristas y parte de las 1.209 mayoristas), porque tienen más artículos, rotación de personal y un dueño que no está en todos los cajones.
- **[ESTIMACIÓN] Techo de ingresos del software solo en Argentina:** 5.771 empresas (minoristas + mayoristas de ferretería) × USD 30 × 12 ≈ **USD 2,1 M por año si el 100% lo comprara**, cosa que no pasa. Con un 2-5% de adopción en 2-3 años: **USD 40.000 a 100.000 por año**. Sirve como piso económico y para aprender, pero no es una startup grande si se queda en Argentina y en un solo rubro.

### 2.4 Cuánto pierden por desorden, faltantes o robo

- **Argentina: no encontré ningún dato** de merma ni de pérdidas por desorden en ferreterías, ni en el comercio minorista argentino en general (búsqueda del 2026-10-15). No digo que no exista: no lo encontré.
- **EE.UU.:** la merma promedio del comercio minorista fue **1,6% de las ventas** en el año fiscal 2022 (USD 112.100 M), contra 1,4% en 2021 [DATO, NRF, 2023-09-26]. No separa ferreterías.
- **Chile:** la merma fue **1,43% de las ventas** en 2023 (1,14% en 2022). Supermercados 2,7%, farmacias 1%, multitiendas 0,8%. No hay datos de ferreterías [DATO, estudio de la CCS y la UAI, citado por The Clinic, 2024-08-08].
- **Desorden de registros:** **65%** de casi 370.000 registros de inventario estaban mal en 37 locales de un minorista de EE.UU. [DATO, DeHoratius y Raman, 2008].
- **[ESTIMACIÓN ilustrativa, no es dato]:** si una ferretería tuviera una merma parecida a la chilena o la estadounidense (1,4-1,6%), por cada ARS 10 millones vendidos por mes perdería unos **ARS 140.000-160.000** (unos USD 90-105 al oficial de hoy). Eso alcanzaría para pagar un abono de USD 15-40, **si** el sistema redujera la merma de forma visible. No sé cuánto venden las ferreterías ni cuál es su merma real: hay que preguntarlo en las entrevistas.

---

## 3. Qué existe

### 3.1 Afuera (empresas reales, verificadas en su web)

**a) Identificar piezas por foto**

| Empresa / producto | Qué hace | Clientes / tamaño | Precio | Nota |
|---|---|---|---|---|
| **nyris** (Berlín, Alemania) | Búsqueda visual de repuestos y productos a partir de una imagen | Logos y testimonios de IKEA, Volkswagen, Hornbach, Bühler, Trumpf, Schindler, Renault y otros; "más de 50 países" [DATO-EMPRESA] | No publicado ("contact us") | Dice ser "3,3 veces más rápido y 51% más preciso" que buscar por palabras, según un comunicado de 2022 [DATO-EMPRESA] |
| **Partium** | IA para equipos de repuestos industriales: "identify the part from a photo, a label or a few words" | The Home Depot, Deutsche Bahn, Walmart, Liebherr, ÖBB y otros [DATO-EMPRESA] | No publicado | Apunta a mantenimiento industrial y grandes cuentas. En lo que leí, su web no muestra la sede |
| **Screw Identifier - Bolt ID** (app de iPhone) | Identifica tornillos, bulones, tuercas y arandelas por foto, **usando una moneda o una regla como referencia de escala**. Estima largo, diámetro y paso de rosca | 3,5 de 5 estrellas con 23 calificaciones [DATO, App Store] | Gratis, con compras desde USD 4,99 por semana o USD 29,99-39,99 por año | **Es casi literal la idea de la regla de Facu**, pero para el consumidor final: no sabe qué tiene el comercio ni dónde está |
| **Magica, "AI Screw Identifier"** (web) | Analiza tipo de cabeza, encastre y rosca a partir de una foto | Sin datos | No visible | Reconoce que **el tamaño solo lo "estima"** y recomienda calibre o peine de roscas para medir exacto [DATO-EMPRESA] |

**b) Contar y controlar por peso**

| Empresa / producto | Qué hace | Precio |
|---|---|---|
| **Bossard SmartBin** (Suiza, distribuidor de bulonería industrial) | Cajones con "sensores de peso" que registran cada retiro, actualizan el stock en la nube (plataforma ARIMS) y **disparan el pedido de reposición solos** al llegar al punto de pedido. Pensado para piezas "B y C" en plantas de producción [DATO-EMPRESA] | No publicado |
| **TeDaLoS** (Austria) | Sensor universal de peso, inalámbrico y retrofit, para cajones de 12×17 cm a 30×40 cm, con nube propia y sin integración informática local [DATO, Fastener + Fixing, 2021-05-05] | No publicado |
| **Balanzas cuentapiezas** (KERN, PCE y otras) | Pesan una muestra de 20 a 50 piezas y calculan la cantidad | Una PCE-BSH 6000 figuraba a **€278,18** en una tienda de España, según el resumen del buscador. **No pude abrir la página** [NO VERIFICADO] |

**c) Pick-to-light (luces en los estantes)**

| Empresa | Qué vende | Precio |
|---|---|---|
| **ekko** (Alemania) | Pick-to-light inalámbrico, e-kanban y localización | Según su propio artículo del 2026-09-23: **€10 a €250 por posición** según el tipo de pantalla. El cableado agrega **€50-150 por posición**. En un ejemplo de 200 posiciones: **unos €8.000 inalámbrico contra unos €55.000 cableado** [DATO-EMPRESA, con conflicto de interés: vende el inalámbrico] |
| **Lightning Pick** (parte de Pyramid, del grupo Duravant) | Pick-to-light, put-to-light, carros con luces | No publicado [DATO-EMPRESA] |

**d) Cámaras con IA contra robo**

| Empresa | Qué hace | Tamaño | Precio |
|---|---|---|---|
| **Veesion** (Francia) | IA sobre las cámaras que ya existen: detecta gestos previos a un robo y manda un aviso con video al celular. Dice no usar reconocimiento facial | "6.000+ tiendas" [DATO-EMPRESA]. En mayo de 2025 levantó **€38 M** y tenía "más de 5.000 tiendas en 25 países" [DATO, FrenchWeb, 2025-05-21] | Sin lista pública. NBC Boston (2024-03-20) dice que a una vinería le cuesta "**a couple hundred dollars a month**" [DATO de prensa]. Entre sus rubros nombra "Home Improvement" |

**e) Inventario con fotos para comercios chicos (genérico)**

- **Sortly** (EE.UU.): inventario con fotos, etiquetas QR y alertas de stock bajo. El plan Premium cuesta **USD 149 por mes** (con 50% de descuento el primer año) y admite **5.000 artículos**. Para más de 10.000 artículos hay que pedir cotización [DATO-EMPRESA]. Una ferretería con 20.000 artículos no entra en sus planes estándar, y además Sortly no busca por foto de la pieza ni está en castellano rioplatense.

**[OPINIÓN] Lectura de conjunto:** cada pieza del rompecabezas existe y tiene clientes que pagan, pero en **empresas grandes** (IKEA, Home Depot, plantas industriales) y con precios "a cotizar". **No encontré** a nadie que junte catálogo con ubicaciones, búsqueda por foto y por nombre y conteo por peso para el **comercio chico de piezas**. Eso no prueba que no exista.

### 3.2 En Argentina (verificados)

| Sistema | Empresa | Qué dice de sí misma | Precio publicado | ¿Foto, ubicación en cajón o pick-to-light? |
|---|---|---|---|---|
| **Tango** (incluye Tango Punto de Venta) | Axoft | "Más de 60.000 empresas" y, en otra parte de la misma página, "más de 79.800" (la página se contradice) [DATO-EMPRESA] | No publicado | No figura en la página principal |
| **Flexxus** (Order Gestión / Enterprise) | Flexxus | "+5.000 empresas". Página para **ferreterías** con "más de 60 implementaciones exitosas" y clientes como Rossi Ferreterías, Hiper Ferretero y Ferretería Butrón. También tiene páginas para autopartes, corralones y electricidad [DATO-EMPRESA] | Desde **ARS 22.500 por mes** (facturación). Starter ARS 43.699, Pro ARS 50.660 y Advanced ARS 57.621, por usuario y por mes | En las páginas de ferreterías y de repuestos: actualización de precios desde Excel, alertas de stock mínimo, multi-depósito. **No menciona** ubicación en estante, búsqueda por foto, código de barras, balanzas ni pick-to-light |
| **Dragonfish / Pantera / Lince** | Zoo Logic | "+5.500 empresas" y "+22.000" instalaciones. Tiene un rubro "Ferretería, Pinturería y Corralón" [DATO-EMPRESA] | No publicado | No lo vi |
| **Dux Software** | Dux (Córdoba, fundada en 2015) | Atiende indumentaria, **ferretería**, dietéticas y tecnología [DATO, CB Insights] | Su web me bloqueó (error 403) | No lo pude ver |
| **YoFacturo** | YoFacturo | "200+ empresas". Facturación ante ARCA, stock y punto de venta [DATO-EMPRESA] | "Planes desde $20.000/mes + IVA" | **Sí toca el tema del peso:** un artículo de su blog (2026-09-05) explica cómo conectar balanzas contadoras (Toledo, CAS, Systel, Kretz) para tornillería en ferreterías. Es el antecedente local más cercano al módulo M3 |

**Qué les falta a estos sistemas, según lo que pude ver:**
- **Dónde está la pieza:** Flexxus habla de "múltiples sucursales y depósitos", no de estante ni de cajón [DATO sobre su página].
- **Buscar sin código:** en ninguna página vi búsqueda por foto ni por descripción vaga.
- **Orden físico:** ninguno ofrece el servicio de ordenar y etiquetar cajones, ni pick-to-light.
- **Lo que sí resuelven:** facturación, precios y compras. La actualización de precios por inflación ya está cubierta por Flexxus y figura en el registro como K5, así que no la propongo.

**No encontré** en Argentina un producto de búsqueda de piezas por foto para comercios, ni proveedores locales de pick-to-light. Esto último no lo busqué a fondo porque se terminó el cupo de búsquedas.

---

## 4. Cómo se construiría y cuánto costaría (todo es ESTIMACIÓN salvo donde dice DATO)

### 4.1 Software (lo hace Facu dirigiendo a Claude)

- **Forma:** una web que se usa desde el celular y la PC del mostrador (las llamadas PWA, que se instalan como una app sin pasar por tiendas). Base de datos de artículos, fotos y ubicaciones. Facu ya tiene Cloudflare conectado.
- **Carga inicial:** importar el Excel que exporta el sistema de gestión del comercio (código, descripción, precio). Después se completan fotos, ubicación y peso unitario.
- **Buscador por nombre:** un modelo de lenguaje traduce la jerga ("el coso de la mochila") a términos del catálogo, más una lista de sinónimos que aprende de cada búsqueda.
- **Buscador por foto (cómo funcionaría) [OPINIÓN técnica]:**
  1. La foto se saca sobre un **tapete impreso con regla y cuadrícula**, que da la escala.
  2. Un modelo de IA que entiende imágenes extrae atributos: tipo de pieza, cabeza, encastre, largo y diámetro aproximados.
  3. Se filtra el catálogo **del comercio** y se ordena por parecido visual contra las fotos cargadas. Esto último usa vectores de imagen ("embeddings"), que permiten sumar artículos nuevos con 2 o 3 fotos, sin reentrenar nada. Responde así a "las piezas van variando".
  4. Muestra 3 a 5 candidatos con foto y ubicación. **El vendedor confirma**, y si hace falta usa calibre o peine de roscas.
- **Por qué no prometer el 100% por foto:** el paso de rosca casi no se ve en una foto. La propia Magica dice que el tamaño solo se "estima" [DATO-EMPRESA]. Además, contar objetos en fotos es flojo: en una prueba con fotos reales (CountQA, 2025), el mejor modelo acertó el 42,9% de las veces, y el 13,9% con más de 50 objetos. Este dato viene del informe L10 del 2026-10-08 y no lo volví a verificar hoy. **Conclusión: la foto sirve para identificar y el peso para contar.**
- **Costo de la IA por foto:** entre **USD 0,0005 y 0,006** con modelos comerciales, según los precios oficiales que se calcularon en el informe L10 (2026-10-08, sin recalcular hoy). Mil búsquedas por mes cuestan menos de USD 6.
- **Hosting:** entre USD 0 y 25 por mes en la etapa piloto [ESTIMACIÓN].
- **Tiempo de construcción del prototipo:** 2 a 4 semanas de trabajo parcial con Claude Code. Facu ya dirigió una app de escritorio real en producción (CEMEVA) [ESTIMACIÓN].

### 4.2 Hardware

| Componente | Costo | Comentario |
|---|---|---|
| Balanza cuentapiezas comercial | ~€278 en España (PCE-BSH 6000) [NO VERIFICADO: lo vi solo en el resumen del buscador] | **Comprar, no fabricar.** No conseguí precios en Argentina porque Mercado Libre bloqueó la consulta. Ojo: muchas balanzas de mostrador ya traen función contadora (blog de YoFacturo) |
| Sensor de peso casero por cajón (celda de carga + amplificador HX711 + microcontrolador) | El amplificador HX711 cuesta **USD 4,95** en SparkFun [DATO]. Con la celda y el microcontrolador: **USD 10-25 por cajón en componentes** [ESTIMACIÓN], sin carcasa, instalación ni soporte | Sirve solo para prototipos. Vender hardware casero implica dar garantía, soporte y posiblemente homologaciones (sección 5) |
| Pick-to-light comercial | **€10-250 por posición**, más cableado de €50-150 por posición si no es inalámbrico [DATO-EMPRESA, ekko] | Para una bulonería mayorista con 500 posiciones, aun en el rango bajo son miles de euros [ESTIMACIÓN] |
| Pick-to-light casero (idea X1d) | Pocos dólares por posición en componentes [ESTIMACIÓN, sin fuente] | Facu no programa firmware a mano. El soporte en campo es el costo real |
| Etiquetas QR y tapete impreso | Menos de USD 20 por comercio [ESTIMACIÓN] | Lo más barato y de mayor impacto inicial |

### 4.3 Servicio (la parte que no escala sola)

- **[ESTIMACIÓN] Cargar el catálogo:** a 1-2 minutos por artículo (foto, ubicación, verificación y peso de una muestra), **2.000 artículos de tornillería llevan entre 33 y 67 horas**. Una ferretería completa de 20.000 artículos llevaría entre 330 y 670 horas. **Por eso se empieza solo con la tornillería** y con los artículos A del análisis ABC (los que más venden).
- **Cómo se reduce:** con un **catálogo compartido** de piezas normalizadas. Un bulón métrico normalizado es el mismo en todas las ferreterías, así que su foto, medidas y peso por cada 1.000 piezas se cargan una sola vez y se reutilizan. Que los catálogos de bulonería publiquen el peso por 1.000 piezas es conocimiento general de ingeniería que no verifiqué hoy. El comercio solo agrega la ubicación. Ver 6.6.

---

## 5. Regulación y riesgos

### 5.1 Regulación

- **Balanzas (metrología legal):** la página oficial de Metrología Legal dice que los instrumentos de medición reglamentados deben cumplir la **Ley 19.511/72** y la **Resolución 611/19**, y tiene una sección de "instrumentos con aprobación de modelo" [DATO, argentina.gob.ar]. **No pude abrir el texto de la ley**, así que no verifiqué si una balanza cuentapiezas que se usa **solo para control interno de stock** está alcanzada. **[OPINIÓN]** Si la balanza se usa para cobrar al cliente, hay que usar balanzas aprobadas y compradas, nunca caseras. Para contar stock adentro, el riesgo parece bajo, pero hay que confirmarlo.
- **Cámaras y datos personales:** las imágenes de personas son datos personales (Ley 25.326). La página de obligaciones de la AAIP dice que ciertas bases de datos deben inscribirse en el Registro Nacional de Bases de Datos Personales y que la información a los titulares "debe ser exhibida en un sitio visible" [DATO, argentina.gob.ar]. **No pude abrir** la norma específica sobre videovigilancia. Sé que existe una disposición de 2015, pero no la verifiqué hoy en fuente oficial. **[OPINIÓN]** Es otra razón para no construir el módulo de cámaras y, si hace falta, aliarse con quien ya lo resuelve.
- **Equipos inalámbricos (luces o sensores con Wi-Fi o Bluetooth):** en Argentina, los equipos de radio requieren homologación de ENACOM. **No lo pude verificar** porque la página oficial dio error. Comprar módulos ya homologados o equipos terminados reduce este riesgo.
- **Facturación:** como el producto **no factura**, no necesita integrarse con ARCA. Es una ventaja de ser una "capa" y no un sistema de gestión [OPINIÓN].

### 5.2 Riesgos del negocio [OPINIÓN]

1. **Que no quieran pagar:** es el riesgo principal. El ferretero tradicional valora el trato y "conocer el barrio" (CAFARA), y puede ver esto como un gasto. No tengo ningún dato de disposición a pagar.
2. **Que no escale:** cada cliente necesita carga de catálogo y orden físico. Si eso no se reduce (catálogo compartido, carga por foto), es una consultora con software, no un producto.
3. **Integraciones:** hay muchos sistemas de gestión distintos (Tango, Flexxus, Zoo Logic, Dux, YoFacturo y otros). Empezar con importación de Excel evita el problema al principio.
4. **Que lo copien:** Flexxus, Tango o YoFacturo pueden sumar "búsqueda por foto" si ven demanda. YoFacturo ya integra balanzas. La defensa es el **catálogo de fotos y ubicaciones cargado** y el servicio, no el algoritmo.
5. **Precisión con piezas casi iguales:** hay que medirla con piezas reales antes de prometer nada (es el corazón del experimento de la sección 8).
6. **Hardware:** las fallas en campo, el soporte y la importación consumen la plata y el tiempo de un emprendedor solo. Por eso queda pendiente.
7. **Moneda:** se cobra en pesos con costos de IA en dólares, aunque el costo de IA por cliente es bajo (sección 4.1).

---

## 6. Respuestas a las dudas de Facu, una por una

### 6.1 "¿Por peso? ¿Cómo?"
Hay dos formas reales, y las dos existen afuera:
- **Balanza cuentapiezas (para contar y despachar):** se pesa una muestra de 20 a 50 piezas, la balanza calcula el peso unitario y después cuenta pesando. Límites [DATO, blog de YoFacturo, 2026-09-05]: cuanto más liviana la pieza, más fina tiene que ser la balanza. Si en un mismo lote hay piezas de tamaños distintos, el cálculo pierde precisión. En pedidos grandes conviene verificar con un conteo parcial.
- **Cajones con sensor de peso (para vigilar todo el tiempo):** Bossard SmartBin y TeDaLoS lo venden para la industria. El cajón "sabe" cuánto queda y pide reposición solo [DATO-EMPRESA].
- **[OPINIÓN] Qué conviene:** la balanza cuentapiezas desde el día 1, porque es barata, se compra hecha y ahorra horas de conteo. Los cajones con sensor, solo para los pocos artículos de valor alto o mucha rotación, y recién cuando un cliente lo pague.

### 6.2 "Hay sistemas pero ninguno definitivo ni dominante"
- **Lo que vi:** hay varios sistemas de gestión fuertes (Tango dice tener más de 60.000 empresas, Flexxus y Zoo Logic más de 5.000 cada uno) y algunos tienen página para ferreterías. **Ninguno de los que revisé** maneja la parte física: dónde está la pieza, cómo encontrarla sin código y cómo contarla rápido.
- **[OPINIÓN]** La intuición de Facu se sostiene para la **parte física del stock**, no para el sistema de gestión en general. "Definitivo" no se logra compitiendo con Tango. Se logra siendo la mejor capa física que se conecta con cualquier sistema.

### 6.3 "Que evite robos y controle todo"
- **Lo que se puede hacer:** (a) comparar lo que salió del cajón (por peso o por conteo) contra lo vendido: si falta y no hubo venta, hay alerta. Eso **detecta**, no **previene**. (b) Usar cámaras con IA tipo Veesion, que ya existen, cuestan un par de cientos de dólares por mes en EE.UU. según la prensa, y nombran el rubro "home improvement".
- **[OPINIÓN]** Con un tornillo de pocos pesos, **el control puede costar más que lo que se pierde**. El anti-robo conviene para artículos caros (herramientas, consumibles de valor) y como alianza, no como desarrollo propio. No encontré datos de merma en ferreterías (ver 2.4).

### 6.4 "Foto de la pieza sobre una regla"
- **Funciona como idea, y ya existe para el consumidor final:** la app "Screw Identifier" usa "una moneda o una regla como referencia" [DATO]. Lo que **no** existe, o no encontré, es la versión **para el comercio**, que cruza la foto con **su** catálogo y le dice al vendedor en qué cajón está.
- **El límite:** el paso de rosca no se ve bien en una foto. La foto achica la búsqueda a 3-5 candidatos, y el peine de roscas o el calibre confirman.

### 6.5 "Buscar por foto y por nombre, no solo para bulonerías"
- **Por nombre:** es lo más barato y quizás lo más útil. El mostrador vive de descripciones vagas, como el ejemplo de CAFARA. Un modelo de lenguaje con sinónimos del comercio lo resuelve sin hardware.
- **No solo bulonerías:** la base técnica sirve igual para una mercería (botones, cierres), una casa de repuestos o una de electricidad. **[OPINIÓN]** Conviene diseñarla así, pero **venderla primero a un solo rubro** (ver 6.7).

### 6.6 "Las piezas van variando": catálogo vivo y compartido
- El buscador por parecido visual (embeddings) permite **dar de alta una pieza nueva con 2 o 3 fotos**, sin reentrenar nada [OPINIÓN técnica].
- **Variante mejor del mismo problema [OPINIÓN]: "catálogo visual compartido de tornillería normalizada".** Se arma una vez (con fotos propias y datos de distribuidores) y se reutiliza en todos los comercios. Cada comercio solo agrega sus ubicaciones y sus artículos raros. Esto **baja mucho el costo de instalación** (mejora F2), y además es un **activo propio** que crece con cada cliente y sirve en cualquier país que use bulonería métrica normalizada.
- **Otra variante para probar en las entrevistas:** que **pague el distribuidor de bulones** y se lo dé a sus ferreterías clientes, como hacen Bossard o Würth con la industria. No verifiqué que algún distribuidor argentino haga algo así; la web de Würth Argentina no lo menciona.

### 6.7 "¿Stock entero multinicho o centrarse en uno?"
**[OPINIÓN fundada]: un solo nicho para empezar: tornillería de ferreterías y bulonerías.** Razones:
1. Es el rubro con **más comercios medibles**: 4.562 minoristas y 1.209 mayoristas con empleados, y unas 15.000 ferreterías según CAFARA.
2. Tiene **más artículos casi iguales**, más de 20.000 por local, que es justo donde duele.
3. Tiene **un canal para llegar**: CAFARA, la revista *Ferreteros*, ExpoFerretera y Espacio CAFARA Rosario.
4. Las piezas son **normalizadas**, y eso hace posible el catálogo compartido.
5. **Repuestos de autos** es otro problema: ahí se busca por vehículo y código del fabricante, y es probable que ya existan catálogos del rubro. No lo verifiqué. **Mercerías** es un mercado chico (689 empresas con empleados, sumando hilados y tejidos) y de ticket bajo [OPINIÓN].

El modelo de datos (artículo, ubicación, foto, peso) se diseña genérico para cumplir el "adaptable a cualquier comercio" de Facu, **sin salir a vender a todos a la vez**.

### 6.8 "¿Producto de software, servicio de instalación más software, o las dos cosas?"
**[OPINIÓN fundada]: las dos, en este orden y con fecha de corte:**
- **Primero, servicio + software:** el servicio de "orden de la tornillería" (análisis ABC, re-layout, etiquetas, fotos y carga) es la puerta de entrada, porque **sin datos el software no funciona** y porque es donde Facu tiene ventaja como ingeniero industrial. Además, se cobra antes.
- **Después, solo software:** a medida que el catálogo compartido crece, la instalación se achica y el producto se vende sin que Facu esté en cada local.
- **El hardware se compra y se revende, no se fabrica**, hasta que haya clientes pagando y un problema que solo el hardware resuelva.
- **Señal de alarma:** si después de 10 clientes cada instalación sigue llevando más de 20 horas, es una consultora y hay que decidirlo conscientemente.

### 6.9 "Brindar un servicio de pick-to-light"
- **[OPINIÓN]** Sirve donde **se arman pedidos de muchas líneas**: bulonerías mayoristas, distribuidoras, depósitos. En el mostrador de una ferretería chica, una etiqueta QR más "ubicación en pantalla" da casi lo mismo por mucho menos.
- **Costos reales afuera:** de €10 a €250 por posición más instalación (ekko, que tiene conflicto de interés). Para un primer cliente, conviene un piloto de 20 a 50 posiciones en un mayorista, y solo si lo pide y lo paga.
- **Queda PENDIENTE** hasta validar el núcleo.

### 6.10 "RFID con piezas metálicas, ¿funciona?" (lo pidió el briefing)
- **Para tornillos sueltos en un cajón: no.** RFID Journal responde que si son "piezas metálicas chicas apretadas en una caja" puede costar leerlas "no importa qué tipo de etiqueta o lector uses". El metal desafina la antena de la etiqueta y bloquea la señal [DATO, RFID Journal, 2009 y c. 2020].
- **Existen etiquetas especiales para metal**, con un separador de espuma, pero son para **una pieza grande con una etiqueta**, no para mil tornillos [DATO].
- **[OPINIÓN]** Poner RFID en el **cajón** dice dónde está el cajón, no cuánto tiene. Para cantidad, el peso le gana al RFID en este rubro.

### 6.11 "Vencimientos y FIFO (K11), donde aplique"
- **[OPINIÓN]** En ferreterías aplica a pocas familias: adhesivos, selladores, siliconas, algunas pinturas y pilas. Va como **campo opcional** del catálogo (fecha de vencimiento al recibir), no como producto aparte. **No encontré datos** sobre cuánto pierden las ferreterías por vencimientos.

---

## 7. Filtro final

| Criterio | Puntaje (1-5) | Justificación |
|---|---|---|
| **F1** Demanda comprobable en Argentina | **2** | El problema está documentado (CAFARA: más de 20.000 artículos, clientes que no saben el nombre). **No hay ninguna evidencia de que paguen** por esta solución, y no encontré competidores locales que lo cobren, lo que puede ser hueco o falta de demanda |
| **F2** Producto automatizable y global | **2** | El buscador es software escalable, y las piezas normalizadas son iguales en todo el mundo. Pero hoy cada cliente necesita carga de catálogo y orden físico. Sube a 3-4 solo si funciona el catálogo compartido |
| **F3** Validable rápido y barato (30 días, menos de USD 300) | **4** | Con entrevistas, un catálogo piloto de 200 piezas y una prueba a ciegas alcanza, por unos USD 150. Lo que más tarda es conseguir que paguen |
| **F4** Riesgo legal manejable (5 = bajo) | **4** | Sin facturar ni usar cámaras, el riesgo es bajo. Hay dudas menores: metrología si una balanza se usa para cobrar, y ENACOM si se fabrica hardware inalámbrico. Las cámaras lo empeorarían (datos personales) |
| **F5** Encaje con Facu | **4** | Es su interés más constante desde septiembre (Orden Operativo, Sporting, pick-to-light, L9, L10, COM-3-5). Junta ingeniería industrial, stock y tecnología física. Ya dirigió software real con Claude. Le falta red de contactos en ferreterías, hasta donde sé |
| **Total** | **16/25** | |

**Recomendación: PRIMERA (acotada).** Se arranca **solo con el núcleo de software, en tornillería de ferreterías y bulonerías**: catálogo con ubicaciones y buscador por foto y por nombre, con el servicio de orden como entrada. **El hardware (cajones con peso, pick-to-light, cámaras, RFID) queda PENDIENTE.**

**Por qué [OPINIÓN]:** no es PRIMERA porque la demanda esté probada (F1 = 2), sino porque **el test es barato y responde justo esa duda**, el encaje con Facu es el más alto y lo que se aprende sirve aunque falle: vender a comercios, ordenar stock real y usar IA con imágenes. **Advertencia honesta:** si las otras indagaciones de esta ronda traen ideas con F1 de 4 o más, deberían ir antes que esta.

---

## 8. Primer experimento concreto

**Nombre:** "Tornillería encontrable", 30 días.

**Hipótesis a probar:**
1. Los ferreteros pierden ventas o tiempo **de forma frecuente y reciente** buscando piezas sin código o descubriendo faltantes tarde.
2. Con una foto sobre un tapete con regla, el sistema pone la pieza correcta **entre los 3 primeros candidatos** en la mayoría de los casos.
3. Al menos algunos comercios **ponen plata** por un piloto.

**Qué hacer, día por día:**

| Días | Tarea |
|---|---|
| 1-3 | Armar una lista de 30 ferreterías y bulonerías de la zona de Facu (Google Maps, o el dataset oficial "Distribución geográfica de los establecimientos productivos" del CEP XXI, que trae locales por departamento y actividad). Imprimir el tapete con regla y cuadrícula. Preparar la guía de preguntas |
| 4-14 | **15 entrevistas** en persona, en horarios de poca gente, sin vender nada (estilo The Mom Test). En 2 comercios, **1 hora de observación en el mostrador**, contando las consultas "sin código" y cuánto tarda cada una |
| 8-20 | **Piloto de datos** en 1 comercio que acepte: fotografiar **200 artículos de tornillería** sobre el tapete y anotar código, ubicación y peso de 20 piezas. Prototipo con Claude: planilla más una página web que busca por foto y por nombre |
| 20-25 | **Prueba a ciegas:** el comercio elige 50 piezas al azar y el sistema las busca por foto. Se mide en cuántas acierta entre los 3 primeros, y cuánto tarda contra la búsqueda manual |
| 25-30 | **Oferta concreta** a los 15 entrevistados: "Ordeno y cargo tu tornillería, con buscador por foto y nombre, por $X de instalación + $Y por mes". Se registra cuántos ponen un anticipo o firman un piloto pago con fecha |

**Cómo llegar:** caminando, local por local, presentándose como lo que es: un ingeniero industrial que está por recibirse e investiga cómo manejan el stock de piezas chicas. Si sale bien, en una segunda vuelta se puede contactar a CAFARA (info@cafara.org.ar) para pedir acceso a socios o a la revista. Conviene sumar 2 o 3 **distribuidores de bulonería** para probar la variante "paga el distribuidor".

**Costo [ESTIMACIÓN]:**
- Impresiones (tapetes, etiquetas QR): unos USD 20.
- Viáticos: unos USD 60.
- IA (APIs): menos de USD 10.
- Balanza de precisión de 0,01 g, si el comercio no tiene una: USD 30-50 (no verifiqué el precio).
- **Total: unos USD 150. Pérdida máxima fija: USD 300 y 60 horas de Facu.**

**Números de decisión (se fijan antes de empezar):**
- **SEGUIR** si se cumplen las tres:
  - (a) **8 o más de 15** cuentan un caso concreto **de los últimos 30 días** de pieza no encontrada, código desconocido o faltante descubierto tarde;
  - (b) la pieza correcta aparece **entre los 3 primeros en el 80% o más** de las 50 piezas;
  - (c) **2 o más comercios** ponen un anticipo o firman un piloto pago con monto y fecha.
- **CORTAR** si pasa cualquiera de estas:
  - menos de 4 de 15 cuentan casos concretos recientes;
  - **ningún** comercio pone plata;
  - menos del 60% de acierto entre los 3 primeros después de 2 rondas de ajuste.
- **Zona gris** (entre una cosa y la otra): una sola ronda más, probando **otro comprador**: bulonerías mayoristas, con pick-to-light, o distribuidores que lo regalen a sus clientes. Si tampoco funciona, se corta y se escribe el post-mortem.

**5 preguntas estilo The Mom Test (sobre hechos pasados, no "¿lo usarías?"):**
1. "La última vez que un cliente trajo una pieza o una foto y no sabían qué era o dónde estaba, ¿qué pasó? ¿Cuánto tardaron? ¿Se terminó vendiendo?"
2. "¿Cuándo fue la última vez que contaron la tornillería? ¿Quién lo hizo, cuántas horas les llevó y qué hicieron con las diferencias?"
3. "En los últimos tres meses, ¿cuántas veces se dieron cuenta de que no tenían algo recién cuando lo pidió un cliente? ¿Me cuenta la última?"
4. "¿Qué sistema usan hoy para el stock, cuánto pagan por mes y qué le pidieron alguna vez al proveedor del sistema que no les resolvió?"
5. "¿Alguna vez le pagaron a alguien, o pusieron horas de un empleado, para ordenar, etiquetar o recontar el local o el depósito? ¿Cuánto costó y cómo quedó a los seis meses?"

---

## 9. Fuentes (todas consultadas el 2026-10-15)

**Mercado y datos oficiales**
- CEP XXI, dataset "Cantidad de empleadores que declararon trabajadores, por sector de actividad": https://datos.produccion.gob.ar/dataset/cantidad-de-empleadores-que-declararon-trabajadores-por-sector-de-actividad
- CSV por CLAE 6 (datos hasta 2023-10-01): https://cdn.produccion.gob.ar/cdn-cep/datos-por-actividad/empleadoras/empleadoras_privadas_por_clae6.csv
- Diccionario de códigos CLAE: https://datos.produccion.gob.ar/dataset/dd219131-47eb-431d-81e7-ab475914337d/resource/19375a1a-68fa-48f6-9b81-de1d29d51ced/download/clae_diccionario.csv
- CEP XXI, "Distribución geográfica de los establecimientos productivos" (para armar listas por zona): https://datos.produccion.gob.ar/dataset/distribucion-geografica-de-los-establecimientos-productivos
- Gacetilla de ExpoFerretera / CAFARA, "Cambio generacional: un factor clave para el futuro del sector ferretero" (julio de 2023): https://expoferretera.ar.messefrankfurt.com/content/dam/messefrankfurt-argentina/expoferretera/press-releases/2023/02EF2023_JUL2023_Cambio_generacional-sector_ferretero.pdf
- Diario Jornada, "Día de los Ferreteros…" (2023-09-02): https://www.diariojornada.com.ar/353795/magazine/dia_de_los_ferreteros_el_cosito_del_coso_y_me_muestra_la_lija_otras_galimatias_de_un_oficio_centenario
- CAFARA (sitio oficial): https://www.cafara.org.ar/
- Cotización del dólar oficial, venta ARS 1.535 (agregador privado, no es el BCRA): https://dolarapi.com/v1/dolares

**Sistemas argentinos**
- Axoft / Tango: https://www.axoft.com/
- Flexxus (inicio y precios): https://www.flexxus.com.ar/
- Flexxus para ferreterías: https://flexxus.com.ar/software-de-gestion-erp-para-ferreterias/
- Flexxus para repuestos: https://flexxus.com.ar/software-y-sistemas-de-gestion-para-venta-de-repuestos-y-autopartes/
- Zoo Logic: https://www.zoologic.com.ar/
- Dux Software (ficha de CB Insights): https://www.cbinsights.com/compare/bondarea-vs-dux-software
- YoFacturo: https://yo-facturo.com/
- YoFacturo, blog "Balanza contadora para ferretería y tornillería" (2026-09-05): https://yo-facturo.com/blog/balanza-contadora-para-ferreteria-y-tornilleria/
- Würth Argentina: https://www.wurth.com.ar/

**Tecnología afuera**
- nyris: https://www.nyris.io/
- Partium: https://www.partium.io/
- App Screw Identifier - Bolt ID: https://apps.apple.com/us/app/id6759244718
- Magica, AI Screw Identifier: https://magica.com/features/ai-screw-identifier
- Bossard SmartBin: https://americas.bossard.com/smart-bins-for-cloud-based-inventory-management/
- Fastener + Fixing, "Smart bins in small part warehouses" (TeDaLoS, 2021-05-05): https://fastenerandfixing.com/management-systems/smart-bins-in-small-part-warehouses
- ekko, costos de pick-to-light (2026-09-23): https://www.ekko.io/en/wissen/pick-to-light-cost
- Lightning Pick: https://www.lightningpick.com/
- SparkFun, amplificador de celda de carga HX711: https://www.sparkfun.com/sparkfun-load-cell-amplifier-hx711.html
- Sortly, precios: https://www.sortly.com/pricing/
- Veesion: https://veesion.io/en/
- NBC Boston sobre Veesion (2024-03-20): https://nbcboston.com/investigations/consumer/ai-is-helping-small-businesses-stop-shoplifting-in-their-stores/3314063
- FrenchWeb sobre la ronda de Veesion (2025-05-21): https://www.frenchweb.fr/retail-sous-surveillance-veesion-leve-38-millions-deuros-pour-imposer-son-ia-anti-vol-a-lechelle-mondiale/454661
- RFID Journal, "Can RFID Inventory Tagged Parts Within a Cage?" (2009-11-04): https://www.rfidjournal.com/?p=176733
- RFID Journal, "Can I Use an RFID Tag on a Metal Surface?" (sin fecha visible, c. 2020): https://www.rfidjournal.com/?p=212966
- Precio de la PCE-BSH 6000, visto solo en el resumen del buscador (la página dio error 403): https://www.carrefour.es/balanza-cuentapiezas-pce-bsh-6000/4250348700605/p

**Pérdidas (merma, desorden, robo)**
- NRF, National Retail Security Survey 2023 (2023-09-26): https://nrf.com/research/national-retail-security-survey-2023
- The Clinic, estudio de la Cámara de Comercio de Santiago y la UAI sobre mermas en Chile (2024-08-08): https://www.theclinic.cl/2024/08/08/perdidas-de-mil-millones-en-el-retail-de-chile-por-robo/
- DeHoratius y Raman (2008), "Inventory Record Inaccuracy: An Empirical Analysis", *Management Science* 54(4): https://ideas.repec.org/a/inm/ormnsc/v54y2008i4p627-641.html

**Regulación**
- Metrología Legal (argentina.gob.ar): https://www.argentina.gob.ar/produccion/metrologia-legal
- AAIP, obligaciones de los responsables de bases de datos: https://www.argentina.gob.ar/aaip/datospersonales/responsables/obligaciones
- No pude abrir: el texto de la Ley 19.511 en InfoLeg, la norma de videovigilancia de la AAIP y la página de homologación de ENACOM (todas dieron error).

**Documentos internos del proyecto que uso**
- `research/fuentes/2026-10-08-L10-stock-ia-camara.md`: costo de la IA por foto y prueba de conteo CountQA. No lo re-verifiqué hoy.
- `research/2026-10-14-marcas-de-facu-nichos.md`: origen de L14, COM-3-5 y sus comentarios.
