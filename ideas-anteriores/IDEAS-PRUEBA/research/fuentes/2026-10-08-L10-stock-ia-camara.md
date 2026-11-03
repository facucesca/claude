# L10 — Stock con IA y cámara para supermercados y almacenes (2026-10-08)

> Informe del agente de investigación. Fecha de corte: **2026-10-08**. Pensado para Facu: 22 años, por recibirse de ingeniero industrial (pasantía de relevamiento logístico, sabe de stock, ABC e inventarios), no programa (tiene amigos programadores y usa Claude Code), ahorros de ~USD 1.300, inglés básico. Quiere empresa propia y, más adelante, una startup grande.
>
> **La idea, en palabras de Facu:** "Un sistema novedoso en Argentina, con inteligencia artificial, para supermercados, almacenes, etc., que tenga el stock con IA y descuente simplemente lo que se lleva (el cliente) o no. Si se llegara a ver la forma de tener algún sistema de IA con cámara, desarrollarlo acá y poder venderlo a todos los súper, sería una ideaza tener esa tecnología."

---

## 0. Metodología, marcas y limitaciones

- Hice **~35 búsquedas web** y **~17 lecturas de páginas** (WebFetch), todas el **2026-10-08**. Después **se agotó el cupo de búsquedas de la sesión** (límite compartido entre agentes), así que algunos huecos quedaron sin cubrir. Están listados en la sección 10.
- Marcas que uso:
  - **[DATO]**: viene de una fuente con URL. Indico la fecha de publicación cuando la conozco.
  - **[DATO-EMPRESA]**: lo dice la propia empresa (comunicado, blog o FAQ). Tiene conflicto de interés: sirve como techo, no como mediana.
  - **[ESTIMACIÓN]**: cálculo mío, con el razonamiento a la vista.
  - **[OPINIÓN]**: juicio mío.
  - **[NO VERIFICADO]**: no lo pude confirmar.
- Muchos datos de la industria salen de **prensa especializada que reproduce comunicados** (Retail Dive, Grocery Dive, The Spoon, Pulse 2.0). Lo marco cuando la cifra es de la empresa.
- Varios sitios argentinos (iProfesional, Mercado, Perfil) muestran **la fecha del día en el encabezado** y no la de publicación. Usé la fecha que figura en el cuerpo de la nota o en la URL.

---

## 1. Resumen ejecutivo

1. **El "Amazon Go" está en retirada en todo el mundo.** Amazon sacó Just Walk Out de sus Amazon Fresh de EE.UU. en abril de 2024. El **27 de enero de 2026 anunció el cierre de todas sus tiendas físicas Amazon Go y Amazon Fresh**, porque no encontró "el modelo económico correcto" para escalar [DATO, TechCrunch 2026-01-27]. Grabango, el competidor más conocido, **cerró en octubre de 2024** después de levantar más de USD 73-93 M [DATO]. Standard AI, que llegó a valer ~USD 1.000 M, **abandonó el checkout autónomo en 2024** y pasó a vender analítica con cámaras [DATO].
2. **En Argentina no sería "lo primero".** Go2Future/MiniGo abrió una tienda autónoma en Colegiales en mayo de 2022 (inversión reportada de ~USD 900.000), y Carrefour abrió en Pilar "Carrefour Flash" en febrero de 2023, con 20 cámaras y unos 200 sensores [DATO]. Además, **Sensify**, startup argentina fundada en 2019, ya usa cámaras con IA en heladeras del canal tradicional y tiene inversión de Kamay Ventures (Arcor, Coca-Cola, Bimbo) y de Arca Continental [DATO].
3. **Lo que sí sobrevive y crece es "ver la góndola" y no "cobrar sin cajero":** robots (Simbe, USD 50 M en 2024), cámaras fijas (Focal Systems, Walmart Canadá), carritos inteligentes (Caper/Instacart triplicó tiendas en 2025) y, sobre todo, **reconocimiento de imágenes por foto de celular para marcas de consumo masivo** (Trax, cuya unidad de reconocimiento de imágenes se vendió a Gemspring en febrero de 2026; Ailet; Involves; Teamcore) [DATO].
4. **El mercado argentino que importa es el canal tradicional.** Según NielsenIQ (junio de 2026), almacenes y autoservicios independientes explican **~35% del consumo masivo**, y su análisis abarcó **más de 194.700 puntos de venta independientes** [DATO]. Ahí casi no hay tecnología, y el que pierde plata con los faltantes es **la marca o el distribuidor**, no solo el comercio.
5. **Técnicamente, hoy se puede** detectar huecos en la góndola, verificar la presencia de una lista corta de productos, leer precios y fechas en una foto de celular, a un costo de **USD 0,0005 a 0,006 por foto** con APIs de modelos multimodales [ESTIMACIÓN con precios oficiales]. **No se puede**, sin entrenamiento propio, contar unidades exactas en góndolas densas ni distinguir con fiabilidad miles de variantes de producto. En un benchmark de conteo con fotos reales, el mejor modelo acertó el **42,9%**, y apenas el **13,9%** con más de 50 objetos [DATO, CountQA 2025].
6. **Veredicto [OPINIÓN]:** el "Amazon Go argentino" **no tiene sentido** para Facu, y tampoco, por ahora, para nadie en Argentina. La versión que sí podría tenerlo es **"auditoría de góndola y faltantes por foto de celular + IA para el canal tradicional"**, que pagan **distribuidoras y marcas medianas**. Arranca como servicio concierge (casi sin código) y, si se valida, se convierte en software y en una red de datos de góndola. Es más una **idea de etapa 2 (startup)** con un posible **puente de etapa 1 (servicio)**. La disposición a pagar está **sin verificar** y es lo primero que hay que testear.

---

## 2. Las variantes tecnológicas y quién las hace

### 2a) Tiendas sin cajero ("agarrás y te vas")

| Empresa | Año / plata | Clientes | Estado a 2026-10 | Fuente |
|---|---|---|---|---|
| **Amazon Just Walk Out** (Amazon Go / Fresh) | Interno de Amazon. Un análisis de terceros estima que el hardware de la primera Amazon Go superó **USD 1 M** [ESTIMACIÓN de terceros, no de Amazon] | Tiendas propias y terceros (estadios, aeropuertos) | **2024-04-03:** lo saca de los Amazon Fresh de EE.UU. y lo reemplaza por Dash Carts. RetailWire informó que eran 27 de 44 locales. **2023:** cierra 8 Amazon Go. **2026-01-27:** anuncia el cierre de **todas** las Amazon Go y Amazon Fresh físicas. Sigue vendiendo JWO a terceros: Amazon dice tener **más de 360 ubicaciones de terceros en 5 países** [DATO-EMPRESA, citado por fuentes secundarias] | Retail Dive 2024-04-03; RetailWire; TechCrunch 2026-01-27; Wikipedia "Amazon Go" |
| **Grabango** (EE.UU., visión pura sin sensores en estante) | Fundada en 2016 por Will Glaser (cofundador de Pandora). Levantó **más de USD 93 M** (The Spoon) o **~USD 73 M** (CNBC vía CSP): las cifras no coinciden | ALDI (ALDIgo), Giant Eagle, 7-Eleven, Circle K | **Cerró el 2024-10-09** por no conseguir financiamiento | The Spoon 2024-10-09; CSP Daily News |
| **Standard AI** (ex Standard Cognition) | Serie C de **USD 150 M** en 2021 (liderada por SoftBank Vision Fund 2); total de **USD 236 M**; valuación reportada de ~USD 1.000 M | Circle K, Compass y otros | **Pivot en marzo de 2024** a "VISION" (analítica con cámaras). El CTO dijo (2024-10-07) que "ni compradores ni retailers están listos" para el checkout autónomo masivo y que procesar en el local "es una gran inversión de capital". Compró Skip (2023) y Pathr.ai (ene-2026, según el resumen de búsqueda) | Pulse 2.0 2024-10-07; The Spoon; Axios 2023-02-02 |
| **Zippin** (EE.UU.) | Serie A de USD 12 M; Serie B de USD 30 M (total > USD 45 M) | Arena de los Sacramento Kings; **Lojas Americanas (Brasil)**, contrato de 18 meses | **[NO VERIFICADO]** a 2025-2026. Su meta de "miles de tiendas para 2025" no encontré que se haya cumplido | Retail Dive; PYMNTS |
| **AiFi** (EE.UU.) | Ronda de USD 65 M; total ~USD 80 M | Aldi Süd (Londres), Rewe | **[NO VERIFICADO]** a 2025-2026 | Retail Dive |
| **Trigo** (Israel) | Serie B de USD 60 M; total de USD 94 M | Tesco, Rewe, Aldi Nord (piloto) | **[NO VERIFICADO]** a 2025-2026 | The Spoon; Retail Dive |
| **Go2Future / MiniGo** (Argentina) | Idea de 2019; inversión reportada de **~USD 900.000** | Tienda propia en Colegiales (mayo de 2022); **Carrefour Flash Pilar** (2023-02-10): 50 m², 20 cámaras HD, ~200 sensores en góndola, pago automático al salir | **[NO VERIFICADO]** si siguen operando. No encontré expansión posterior | Perfil 2023-02-10; Economía Sustentable; iProfesional |

**Sobre los revisores humanos de Amazon (las dos versiones):**
- **Versión The Information** (periodista Theo Wayt; difundida en abril de 2024 y citada por KUOW y otros. Algunas fuentes secundarias la fechan en 2023 y no pude leer el original por el muro de pago): unas **1.000 personas en India** revisaban compras. Según una fuente anónima, en 2022 **~700 de cada 1.000** transacciones necesitaban revisión humana, contra una meta interna de 50 de cada 1.000.
- **Versión Amazon:** calificó los reportes de "engañosos e inexactos". El vocero Nathan Strauss dijo que "la caracterización de que Just Walk Out depende de revisores humanos es inexacta" y que el rol principal de su equipo es **anotar imágenes de video para entrenar el modelo**. Otra vocera dijo que validan "una pequeña porción de visitas revisando clips grabados". **Amazon no negó que haya humanos en el proceso.** Dijo que intervienen en una minoría de casos de baja confianza y que esas revisiones bajan año a año (sin cifras).
- **[OPINIÓN]:** con cualquiera de las dos versiones, la conclusión práctica es la misma. Incluso con los recursos de Amazon, el sistema necesitó personas para etiquetar y revisar, y un emprendedor chico no puede pagar esa capa.

### 2b) Monitoreo de góndola por cámara o robot (quiebres de stock)

| Empresa | Año / plata | Clientes | Estado | Fuente |
|---|---|---|---|---|
| **Trax** (Singapur/Israel) | Serie E de **USD 640 M** (abril de 2021; SoftBank VF2 y BlackRock). Valuación reportada de USD 2.000-3.000+ M según la fuente. Solo ~USD 300 M fueron dinero nuevo; el resto compró acciones existentes | Coca-Cola Hellenic (caso: auditorías hasta 9 veces más rápidas, 97% de reconocimiento de SKU [DATO-EMPRESA]) y grandes marcas | Despidos en 2020 (~120, 10%), 2021 y 2022 (>100, ~12%, y otra tanda de 70-80). Deuda de USD 50 M con Deutsche Bank (ene-2024). **Feb-2026: vendió su negocio de reconocimiento de imágenes a una afiliada de Gemspring Capital**, que lo fusionó con FORM (GoSpotCheck). Trax se quedó con Shopkick, Survey y LenzTech | Bloomberg; Globes; Calcalist; Lincoln International; nota de prensa 2026-02-12 |
| **Focal Systems** (EE.UU.) | Serie B de USD 25,8 M (dic-2021/ene-2022, Point72); total de ~USD 37-40 M | **Walmart Canadá** (piloto en 70 tiendas y luego toda la cadena) | Activa (presente en NRF 2025). Modelo: **fee de instalación + fee mensual**, "IA como servicio". **Cada cámara cubre ~8 pies (2,4 m) de góndola y un súper de 30.000 ft² (~2.800 m²) necesita ~400 cámaras** [DATO-EMPRESA, FAQ]. No publica precios | focal.systems/faqs; Retail Dive; CDO Magazine |
| **Simbe Robotics** (robot Tally) | Serie C de **USD 50 M** (2024-10-24, Goldman Sachs); total de más de USD 100 M; ~75 empleados | 29 marcas de retail en 2024 (más de la mitad con contrato y el resto en piloto); Schnucks en todas sus tiendas; BJ's; Albertsons | Activa. Cobra un **fee mensual por tienda** en suscripción anual y además **comparte ingresos por vender los datos a los proveedores (marcas)**. Dice ahorrarle al retailer 4-6 veces lo que cuesta [DATO-EMPRESA]. Nov-2025: opera en 10 países con "casi cinco docenas" de clientes [DATO-EMPRESA] | Fortune 2024-10-24; simberobotics.com |
| **Bossa Nova Robotics** | — | Walmart (~500 tiendas) | **Walmart cortó el contrato en nov-2020**: encontró soluciones "más simples" e igual de útiles. Bossa Nova despidió al 50%. Según su exCEO en Fortune (2024), la empresa no logró nuevos clientes y **cerró** | Grocery Dive / Retail Dive 2020; Fortune 2024-10-24 |
| **Shelfie** | — | — | **[NO VERIFICADO]**: no llegué a investigarla | — |

### 2c) Carritos inteligentes

| Empresa | Datos | Estado | Fuente |
|---|---|---|---|
| **Caper (Instacart)** | Instacart no publica el costo por carrito, que "varía según el retailer" y suele venderse junto con otros productos. El NY Post reportó **hasta USD 10.000 por carrito** [DATO de prensa, sin método] | **Nov-2025: triplicó la cantidad de tiendas respecto de 2024.** Está en 100 ciudades de 15 estados y más de una docena de cadenas (ShopRite/Wakefern ~20% de sus tiendas, Sprouts, Schnucks, Wegmans), además de Coles (Australia) y Morrisons (Reino Unido). El negocio es **publicidad dentro del carrito** y datos | Modern Retail / Digiday 2025-11-28; AOL/NY Post |
| **Amazon Dash Cart** | Reemplazó a Just Walk Out en Fresh (2024) | Con el cierre de Fresh (2026), su estado es **[NO VERIFICADO]** | Retail Dive 2024-04-03 |
| **Veeve** | — | **[NO VERIFICADO]** | — |

### 2d) Cajas de autoservicio con visión

| Empresa | Datos | Estado | Fuente |
|---|---|---|---|
| **Mashgin** (EE.UU.) | Serie B de USD 62,5 M (mayo de 2022, NEA); valuación de **USD 1.500 M**; total de USD 74,7 M. Más de 800 ubicaciones (estadios, convenience) y se declaraba "ya rentable" [DATO-EMPRESA] | No encontré rondas nuevas en 2025 **[NO VERIFICADO]** | Retail Dive / Grocery Dive 2022; PYMNTS |

[OPINIÓN] Es la variante de visión más "sana" en cuanto a negocio: un kiosco con catálogo acotado (comida de estadio, cafetería) reconoce lo que el cliente apoya sobre la bandeja. No sirve para un almacén con miles de productos.

### 2e) Soluciones con celular (foto de la góndola → IA)

| Empresa | Datos | Fuente |
|---|---|---|
| **Trax / FORM** (unidad de reconocimiento de imágenes) | Fotos tomadas por los repositores de la marca, que la IA convierte en KPIs: presencia, quiebre, planograma, share of shelf | ver 2b |
| **ParallelDots ShelfWatch** | Mide planograma, share of shelf, material POP, precios y disponibilidad. **Precio: "contactar al proveedor"** | Capterra |
| **Ailet** | Se expande en LATAM: nombró director comercial regional y organizó eventos en México con Grupo Modelo (AB InBev) | Merca2.0 |
| **Involves (Brasil)** | Agile Promoter (gestión de repositores) más "Involves Stage" (reconocimiento de imágenes, tecnología comprada a la startup Stringhini a fines de 2018). Dice tener **más de 90% de precisión** [DATO-EMPRESA] y equipos en **Argentina**, México, Chile, Perú y Colombia [DATO-EMPRESA] | Baguete 2019-01-22; ABES; Capterra |
| **Teamcore (Chile)** | Disponibilidad en góndola y alertas para repositores con machine learning. Accel-KKR tomó la mayoría en agosto de 2022; compró Tech-K (Chile), Pabis (México) y Grupo BIT (Colombia, 2024). Clientes: 3M, Coca-Cola, Unilever, Colgate, L'Oréal [DATO-EMPRESA]. **Su presencia en Argentina no está clara** (una nota vieja dice que sí y Forbes Chile 2024 no la menciona) | Accel-KKR; Forbes Chile 2024-05-16 |
| **Shelfpix (Brasil)** | App + red neuronal "YODDA", lanzada en Berlín en 2018. Estado actual **[NO VERIFICADO]** | Mercado & Consumo 2018-05-14 |

### 2f) Variante LATAM específica: cámaras en heladeras del canal tradicional

| Empresa | Datos | Fuente |
|---|---|---|
| **Sensify (Argentina)** | Fundada en **2019** por Matías Cottone y los hermanos Eugenio y Federico Harraca. Gestiona heladeras de marcas de bebidas y alimentos en comercios, con sensores y **módulos de visión que reconocen marcas** ("Cooler Eye": cámara que mira el interior y el exterior de la heladera). Dice monitorear "más de un millón de heladeras cada 15 minutos" (Ámbito 2023, [DATO-EMPRESA]). Clientes en México, Colombia, Uruguay, Chile, Bolivia y Argentina. **Pre-seed (dic-2023) con Kamay Ventures**, el fondo de Arcor, Coca-Cola y Bimbo. **Seed con AC Ventures (Arca Continental, 2025-04-14)**, monto no informado. iProUP reporta una ronda de **USD 2 M** (fecha no confirmada) | Arca Continental 2025-04-14; Ámbito 2023-12-26; iProUP; El Financiero 2025-04-16 |

**[OPINIÓN] Esta es la señal más importante del informe.** En el canal tradicional latinoamericano ya hay una startup argentina con cámaras e IA, y **los que ponen la plata son las marcas y las embotelladoras**, no los almaceneros. Es a la vez evidencia de demanda y un competidor directo en la parte de heladeras.

### 2g) Pariente low-tech: mercaditos autónomos en edificios (Brasil)

- **Market4u**: ~2.100 tiendas autónomas dentro de condominios residenciales y comerciales (1er semestre de 2023), con 406 franquiciados. En marzo de 2026 la empresa declaró **más de 2.500** y lideró el ranking ABF de microfranquicias [DATO-EMPRESA]. Proyectaba 50.000 tiendas para 2028, muy lejos de lo real. Una proyección de 2021 del sector hablaba de ~110.000 tiendas para 2025, tampoco cumplida.
- No son tiendas de visión artificial al estilo Amazon: son **autoservicio con monitoreo**. En 2023 decían estar desarrollando "detección de robos" con una inversión de "siete dígitos".
- **[OPINIÓN]:** muestra que en LATAM "sin cajero" prospera cuando es **barato y en un entorno de confianza** (edificio cerrado), no cuando apuesta a la tecnología cara.

---

## 3. Por qué fracasó o se frenó la tecnología cashierless

| Causa | Evidencia | Tipo |
|---|---|---|
| **Costo de hardware e instalación** | Hardware estimado en más de USD 1 M para la primera Amazon Go. Morgan Stanley estimó USD 0,5-3.000 M para 3.000 tiendas, o sea **~USD 170.000 a 1 M por tienda** (mi cuenta sobre su rango) | [ESTIMACIÓN de terceros] digitalcenter.org; Harvard D3 |
| **Repago largo** | Con un cajero menos 24 horas (~USD 131.000/año en EE.UU.), una inversión de USD 1 M **tarda ~8 años en repagarse**. Con dos cajeros a USD 18/h, unos 3 años | [ESTIMACIÓN de terceros] Harvard D3 |
| **Mantenimiento y cómputo** | "Cargas de cómputo pesadas en el local, una gran inversión de capital" (CTO de Standard AI). Técnicos para reparar sensores | [DATO] Pulse 2.0 2024-10-07 |
| **Precisión y revisión humana** | ~1.000 revisores en India y ~70% de transacciones revisadas en 2022 (The Information, **negado** por Amazon). Casos difíciles: devolver a la góndola, carritos compartidos, productos tapados | [DATO en disputa] |
| **Catálogo grande** | Cada producto debía pesarse y registrarse de antemano: inviable con decenas de miles de SKUs de un súper grande | [DATO de análisis secundario] iads.org / Modern Retail 2024-04-04 |
| **Margen bajo del súper** | "Los costos de equipar y mantener no se compensaron con más ventas o eficiencia en un negocio de margen bajo" | análisis secundario |
| **El personal no desaparece** | Igual hace falta gente para reponer, preparar frescos e inventariar | análisis secundario |
| **Experiencia y confianza del cliente** | Amazon dijo que los clientes preferían el Dash Cart porque ven cuánto gastan mientras compran. Hubo errores en tickets y quejas de privacidad | Retail Dive 2024-04-03 |
| **Clientes y compradores "no listos"** | Standard AI: "ni compradores ni retailers están listos a escala masiva" | Pulse 2.0 |
| **Financiamiento** | Grabango no consiguió la siguiente ronda y cerró | The Spoon 2024-10-09 |
| **Economía de la tienda** | Amazon cerró Go y Fresh en 2026: "no creamos… el modelo económico correcto para una expansión a gran escala" | TechCrunch 2026-01-27 |

**Robo:** no encontré datos duros que muestren que el robo haya sido la causa principal del abandono. **[NO VERIFICADO]**

**[ESTIMACIÓN / OPINIÓN] Por qué en Argentina es peor:** el ahorro de un cashierless es sueldo de cajero. Si el costo laboral argentino en dólares es menor que en EE.UU. (no verifiqué salarios de cajero en Argentina hoy) y el hardware importado no es más barato, el repago se estira todavía más que los 3-8 años calculados para EE.UU. Además, los súper argentinos venían de caer 5,2% en volumen en 2025 (Scentia), lo que no favorece grandes inversiones.

---

## 4. Argentina y LATAM

### 4.1 Estructura del mercado

| Dato | Valor | Fuente / fecha |
|---|---|---|
| Peso del canal tradicional + autoservicios independientes | **35%** de las ventas de consumo masivo | [DATO] NielsenIQ vía Mercado, **2026-06-08** |
| Puntos de venta independientes analizados por NIQ | **más de 194.700** | [DATO] mismo |
| Reparto por formato (NIQ, nota de 2025-26, fecha exacta no verificada) | Almacenes/canal tradicional 34%, cadenas 31%, kioscos/minimercados 15%, autoservicios independientes 14%, farmacias 5%. **Ojo:** no cierra del todo con el 35% de arriba; la metodología no está explicada | [DATO] Mercado.com.ar |
| Consumo masivo 2025 (Scentia) | +2% en 2025 después de **-13,9% en 2024**. Almacenes y kioscos +9,1%, e-commerce +14,1%, **supermercados -5,2%**, mayoristas -5%, autoservicios +0,1% | [DATO] Infobae 2026-01-22 |
| 2026 | En abril de 2026, almacenes y kioscos cayeron 4,8% interanual. En agosto volvieron a caer todos los canales | [DATO] Scentia vía prensa |
| Supermercados "chinos" (autoservicios asiáticos) | ~**13.000** locales (cámara CEDEAPSA, 2025). Es el mismo número que se repetía en 2020, así que **probablemente no se actualiza**. Hubo cierres en la pandemia (~2.500) y después | [DATO de gremio] iProfesional; Ámbito |
| Kioscos | De ~112.000 a ~96.000 en un año (UKRA, gremio) | [DATO de gremio] La Voz de San Justo |
| Cantidad de almacenes de barrio | **No encontré un censo.** La referencia más cercana es el >194.700 de NIQ | [NO VERIFICADO] |
| Cantidad de bocas de supermercados de cadena | **[NO VERIFICADO]** (no llegué a buscarlo) | — |

### 4.2 Qué sistemas de stock y caja usan hoy

- **No encontré datos de qué porcentaje de almacenes usa un sistema de stock.** [NO VERIFICADO]
- Ejemplos de oferta local: **Ventar** (ventas + stock + facturación ARCA) figura en GetApp con "precio inicial **25.000 por mes**", **sin aclarar la moneda**, y 40 días de prueba gratis. **Zoo Logic Dragonfish** (stock, caja, etiquetas) no publica precio. **Lider Gestión** se vende con licencia propia, sin abono, según reseñas.
- [ESTIMACIÓN] Si los 25.000 son pesos, el ticket de software para un comercio chico ronda las **decenas de dólares por mes** (no convertí porque no verifiqué el tipo de cambio de hoy). Es una referencia del techo de precio que un almacén acepta pagar por software.
- [OPINIÓN, importante para la idea] **"Descontar lo que se lleva el cliente" ya lo resuelve cualquier punto de venta con lector de código de barras.** El problema real del stock en un almacén no está en las salidas: está en que **no se cargan las entradas** (compras, remitos), no se ajusta el inventario y no se repone a tiempo. La cámara agrega valor donde **no hay cajero** o donde **nadie mira la góndola** (cadenas con varias sucursales, dueño ausente, o la marca que no está en el local).

### 4.3 Faltantes en góndola (Argentina e internacional)

| Dato | Valor | Fuente |
|---|---|---|
| Faltante en góndola en Argentina (GS1/EAN, series viejas) | 13,8% (2008); 7,61% (2010); 14,88% (2011); 19,47% (2014); 3,89% → 4,77% (fines de 2017 → 1T-2018); otro estudio de EAN, 17,15% (fecha no confirmada). **No son comparables entre sí.** No hay dato 2024-2026 | [DATO viejo] Mercado; The Logistics World; iProfesional |
| Causas del faltante (GS1, marzo de 2018) | **48,09% mercadería que está en el local pero no se repuso en góndola**, 23,61% inventario no ajustado, 16,65% proveedor que no entregó | [DATO] mismo |
| Reacción del consumidor (GS1 2018) | ~40% no compra ante el faltante | [DATO] mismo |
| Internacional | Faltante promedio de **8,3%** en tiendas físicas; **~4% de ventas perdidas**; ante el faltante, 45% sustituye, 31% va a otra tienda y ~14% no vuelve a comprarlo; **las pérdidas se reparten: retailer ~31%, marcas ~33%** | [DATO, vía fuentes secundarias] Gruen, Corsten y Bharadwaj 2002; GMA 2018 |

**[OPINIÓN, con lente de ingeniero industrial]:** en el súper, casi la mitad del faltante es **un problema de proceso de reposición dentro del local**, no de abastecimiento. La cámara solo **detecta**; el valor está en cerrar el ciclo (alerta → repositor → verificación). Ahí Facu tiene ventaja de oficio.

### 4.4 Merma y robo

| Dato | Valor | Fuente |
|---|---|---|
| Merma operativa en súper y autoservicios de Argentina (BID) | **4,76% de las ventas (2019)**; **3,32% (2020)** | [DATO] BID, "Desperdicio de alimentos en supermercados y autoservicios de Argentina" (vía resumen de búsqueda; no pude abrir el PDF, devolvió 403) |
| Porción "desconocida" de la merma | 48,1% del total | [DATO] mismo |
| Dentro de la merma conocida | devoluciones 20,2%, no clasificadas 15,4%, desperdicio 6,5%, **vencimiento 4,3%**, rotura 3,0%, **robo identificado 0,1%** | [DATO] mismo |
| Grandes cadenas (2012) | Pérdidas de 1,70% de las ventas; ~25% por hurto externo y 15% por hurto interno | [DATO viejo] censo de Hasar |
| Chile (referencia) | Merma desconocida de 55% en supermercados; de ella, 49,4% robo externo y 28,2% hurto interno | [DATO] Cámara de Comercio de Santiago |

### 4.5 Startups locales o latinoamericanas de visión para retail

- **Argentina:** Go2Future/MiniGo (tienda autónoma, 2022-2023) y **Sensify** (heladeras, desde 2019, con inversión de Kamay y de Arca). **No encontré** una startup argentina de reconocimiento de góndola por foto. Eso no prueba que no exista: se cortó el cupo de búsquedas.
- **LATAM:** Involves (Brasil), Teamcore (Chile), Shelfpix (Brasil, estado desconocido), y Ailet y Trax/FORM entrando por México.
- **Interés estratégico:** el fondo de Arcor, Coca-Cola y Bimbo (Kamay) y el de Arca Continental (AC Ventures) **ya invierten en tecnología para el canal tradicional** [DATO]. Es un posible canal de salida o de inversión para una etapa 2.

### 4.6 Poder de compra y hardware importado

- El poder de compra del canal es frágil: consumo masivo -13,9% en 2024 y +2% en 2025, y cierre de kioscos y de chinos [DATO, ver arriba].
- **Costo y aranceles del hardware importado (cámaras, sensores): [NO VERIFICADO].** No llegué a buscarlo antes de que se agotara el cupo.
- [ESTIMACIÓN ilustrativa, no dato] Focal habla de **~400 cámaras para un súper de ~2.800 m²**. Si cada cámara costara entre USD 30 y 100 (supuesto mío, no verificado), serían **USD 12.000-40.000 solo en cámaras por tienda**, sin instalación, conectividad ni mantenimiento. Es inviable para Facu y difícil de vender a un súper argentino.

---

## 5. Ángulos más chicos y realistas, y qué es técnicamente factible hoy

### 5.1 Qué dice la evidencia sobre la precisión

| Tarea | Evidencia | Lectura |
|---|---|---|
| **Contar objetos** con modelos multimodales generales | **CountQA** (arXiv 2508.06585, ago/sep-2025): fotos reales densas, 15 modelos; **el mejor acierta 42,9%**. Por resumen secundario: Gemini 2.5 Pro llega a 60,3% con 1-5 objetos, 44% con 6-10, 39,3% con 11-20 y **13,9% el mejor modelo con más de 50 objetos** | Contar unidades exactas en una góndola **no** es confiable con APIs generales |
| Lo que dicen los propios proveedores | Anthropic: Claude da "conteos aproximados… especialmente con muchos objetos chicos". Gemini: devuelve cajas delimitadoras (detección) y segmentación | Coincide: sirven para aproximar y localizar, no para contar con exactitud |
| **Detección densa en góndola** con modelos especializados | SKU-110K (CVPR 2019): el mejor método de entonces llega a **AP 0,492**; leaderboards posteriores, ~0,59 (métrica estricta) | Incluso los modelos entrenados para esto sufren con góndolas muy densas |
| **Detección entrenada y en producción** | 7-Eleven Taiwán: sistema de cumplimiento de planograma en **más de 7.000 tiendas**, con detector de productos de **95,7% mAP@50** (Scientific Reports, dic-2025) | **Con datos propios y entrenamiento, funciona a escala.** Es lo que hacen Trax y sus competidores, y requiere inversión en datos |
| **Distinguir SKUs parecidos** | Estudio de 190 VLMs open-source (arXiv 2605.18029, 2026): **94,5% Recall@5**, pero el Recall@1 cae 17,5 puntos | Los modelos aciertan la categoría o la marca y fallan en la variante exacta (tamaño, sabor) |
| Proveedores comerciales | Trax dice 97% de reconocimiento de SKU (caso Coca-Cola Hellenic); Involves, más de 90% [DATO-EMPRESA] | Son cifras de marketing; sirven de techo |

### 5.2 Factible hoy y no factible (para un MVP con APIs, sin entrenar modelos)

**Factible con buena probabilidad** [ESTIMACIÓN basada en lo anterior; **hay que medirlo con fotos reales**]:
- Detectar **huecos o espacios vacíos** en la góndola y marcarlos con cajas.
- Verificar **si está o no está** una lista corta de productos o marcas objetivo (por ejemplo, los 20 SKUs de una marca en un almacén).
- **Leer precios** de etiquetas y carteles, y **fechas de vencimiento** cuando la foto es de cerca.
- Clasificar el contenido de una heladera ("¿hay productos de otra marca en la heladera de la marca X?"), aunque eso ya lo hace Sensify.
- Leer **fotos de facturas o remitos** para cargar compras al stock (documentos, no góndola; es la tarea en que estos modelos son más fuertes, según mi experiencia, sin benchmark citado).

**No factible o poco confiable sin entrenamiento propio:**
- Contar unidades exactas (sobre todo en profundidad: lo que está detrás no se ve).
- Distinguir con fiabilidad miles de SKUs y variantes en un catálogo argentino.
- Seguir a cada cliente por la tienda y saber qué se llevó (cashierless). Es lo que no le cerró ni a Amazon.

### 5.3 Costo por imagen (precios oficiales consultados el 2026-10-08)

| Modelo | Precio (USD por millón de tokens, entrada / salida) | Tokens por foto | Costo por foto [ESTIMACIÓN] | Por 1.000 fotos |
|---|---|---|---|---|
| Gemini 2.5 Flash-Lite | 0,10 / 0,40 | Foto de ~1600×1200: 4 tiles de 258 = ~1.030 tokens de imagen + ~500 de instrucciones; respuesta de ~800 tokens | ~USD 0,0005 | **~USD 0,50** |
| Gemini 3.1 Flash-Lite | 0,25 / 1,50 | 1.120 tokens por imagen (resolución por defecto) + 500; respuesta de ~800 | ~USD 0,0016 | **~USD 1,60** |
| Claude Haiku 4.5 | 1 / 5 | Imagen de 1000×1000: 1.296 tokens + 500; respuesta de ~800 | ~USD 0,006 | **~USD 6** |

- Supuestos míos: ~500 tokens de instrucciones y ~800 de respuesta (lista de productos o huecos en JSON). **Si el modelo "piensa"**, la salida puede crecer varias veces. Anthropic ofrece 50% de descuento en lote (batch).
- [ESTIMACIÓN] Un almacén con **100 fotos por semana** (~430 por mes) costaría entre **USD 0,20 y 2,60 por mes** en API. **El costo de la IA no es la barrera; la precisión y la disposición a pagar, sí.**
- **Riesgo de precio:** la página de Google anuncia que `gemini-3.8-flash` pasa de USD 0,75/3,75 a **USD 1,50/7,50 desde el 2027-01-01**. Los precios de API cambian, y conviene diseñar el sistema para poder cambiar de proveedor.

### 5.4 Los ángulos, comparados

| # | Ángulo | Usuario | Quién paga | Hardware | Comentario [OPINIÓN] |
|---|---|---|---|---|---|
| A | **Amazon Go argentino** (cobrar sin cajero) | Cliente del súper | Súper | Decenas o cientos de cámaras y sensores | Descartado (ver sección 3) |
| B | Cámaras fijas en góndola para quiebres (tipo Focal) | Repositor del súper | Súper o cadena | ~400 cámaras por tienda mediana | Capital intensivo, venta larga a cadenas; no es para Facu hoy |
| C | **Cámaras baratas + foto cada hora** en autoservicios con varias sucursales | Dueño o encargado | Autoservicio o cadena chica | 2-6 cámaras Wi-Fi por local (precio **[NO VERIFICADO]**) | Interesante para dueños ausentes y cadenas chicas; disposición a pagar desconocida |
| D | **Auditoría de góndola por foto de celular para marcas o distribuidoras** (Trax barato para el canal tradicional) | Repositor, preventista o promotor de la marca o distribuidora | **Marca mediana o distribuidora** | Ninguno (el celular que ya tienen) | **Mi favorito.** Ellos pierden plata con el faltante (~33% de la pérdida es de la marca); ya pagan repositores que sacan fotos. Competidores fuertes en Tier 1; el hueco posible está en marcas PyME y distribuidoras **[NO VERIFICADO]** |
| E | **Pedido sugerido por foto** para preventistas de distribuidoras | Preventista | Distribuidora o mayorista | Ninguno | Variante de D muy ligada al saber logístico de Facu: foto → faltantes → pedido sugerido |
| F | **Stock por foto para el almacenero** (entradas por foto de factura o remito, salidas por la caja, faltantes por foto) | Almacenero | Almacén | Celular | Resuelve el problema real del stock (cargar entradas), pero el ticket es bajo, la cobranza difícil y la competencia son los puntos de venta locales |
| G | Control de vencimientos por foto | Almacén o súper | Almacén o súper | Celular | El vencimiento es 4,3% de la merma conocida (BID). Mejor como función de F (cargar el vencimiento al recibir) que como producto suelto |

---

## 6. Quién paga y cuánto

| Pagador | ¿Paga hoy por algo parecido? | ¿Cuánto? | Fuente |
|---|---|---|---|
| **Supermercado o cadena grande** | Sí, en EE.UU.: Simbe (fee mensual por tienda + reparto de datos), Focal (instalación + fee mensual), Caper (carritos) | **No publicado** en ningún caso. Carritos: "hasta USD 10.000" por unidad (prensa) | Fortune 2024; focal.systems; NY Post |
| **Autoservicio o almacén** | Paga software de punto de venta y stock | Ventar: "25.000 por mes" (moneda no aclarada); otros, licencia única | GetApp |
| **Marca de consumo masivo** | Sí: repositores y promotores propios o tercerizados, más software de reconocimiento de imágenes (Trax, Ailet, Involves, ShelfWatch). Las embotelladoras invierten en startups (Arca → Sensify) | **Precios no publicados.** Involves figura en Capterra con un "inicial de 30 BRL", sin claridad sobre qué incluye | Capterra; Arca Continental 2025 |
| **Distribuidora o mayorista** | Paga preventistas y repositores. Gasto en tecnología de góndola: **[NO VERIFICADO]** | **[NO VERIFICADO]** | — |
| **Agencias de trade marketing** | Venden visitas de auditoría o reposición a las marcas. En los avisos de empleo argentinos, los repositores ya sacan fotos y colocan material POP | **Tarifa por visita en Argentina: [NO VERIFICADO]** (no hay precios públicos) | Avisos de Computrabajo |

**[OPINIÓN]** El patrón internacional es claro: **la tecnología de góndola se financia cuando paga quien pierde con el faltante y tiene presupuesto** (marcas y embotelladoras) o cuando el dato se puede revender. El modelo de Simbe, que cobra al retailer y además comparte ingresos por vender datos a las marcas, muestra que un mismo dato puede cobrarse dos veces.

---

## 7. MVP: equipo, costo y tiempo (todo [ESTIMACIÓN])

| Nivel | Qué es | Equipo | Costo | Tiempo | ¿Factible para Facu? |
|---|---|---|---|---|---|
| **0. Concierge** | Facu (o el repositor del cliente) saca fotos, las pasa por Gemini o Claude desde el navegador, revisa a mano y entrega un reporte de faltantes en Google Sheets o PDF | Solo Facu | < USD 200 | 2-4 semanas | **Sí.** No requiere programar |
| **1. MVP software** | App web o PWA de captura de fotos + backend + llamada a la API + panel con faltantes por punto de venta + revisión humana de dudas | 1 amigo programador part-time + Facu (producto, ventas, operación) | USD 0 (si es socio con equity) a ~USD 3.000-8.000 (si se le paga). API de USD 10-50/mes; hosting de USD 20-50/mes | 6-10 semanas | **Sí, con un socio técnico** |
| **2. Modelo propio** | Detector entrenado con miles de fotos etiquetadas de productos argentinos (lo que hacen Trax o 7-Eleven) | Ingeniero de ML + etiquetado | Decenas de miles de USD | 3-6+ meses | **No por ahora.** Solo si el nivel 1 vende |
| **3. Cámaras fijas** (ángulo C) | 2-6 cámaras por local + capturas periódicas | Técnico de instalación + software | Hardware **[NO VERIFICADO]** + instalación | 2-3 meses | Solo después de validar D o F |
| **4. Cashierless** | Tienda sin cajero | Equipo grande + hardware | Go2Future reportó **~USD 900.000** para su tienda | Años | **No** |

---

## 8. Riesgos

| Riesgo | Detalle | Severidad [OPINIÓN] |
|---|---|---|
| **Precisión** | Los modelos generales fallan contando y distinguiendo variantes (CountQA, estudio de 190 VLMs). Si el reporte se equivoca, el cliente deja de confiar | Alta: es el riesgo técnico central. Mitigación: lista corta de SKUs objetivo, revisión humana y medición antes de vender |
| **Disposición a pagar** | Nada de lo que encontré prueba que marcas medianas o distribuidoras argentinas paguen por esto | **Alta: es lo primero a validar** |
| **Competencia de gigantes y de regionales** | Trax/FORM, Ailet, Involves, Teamcore y Sensify ya venden a las marcas grandes. "Ser el primero" no está disponible | Media-alta. El hueco posible está en el segmento chico, con precio bajo y foco en Argentina |
| **Privacidad (Ley 25.326)** | La Disposición 10/2015 (DNPDP, hoy AAIP) considera la imagen de una persona identificable un **dato personal**, y un archivo de filmaciones una **base de datos sujeta a la ley**. Dentro del propio local no hace falta consentimiento, pero sí **cartel informativo** (nuevo modelo por Resolución AAIP 38/2024, 2024-02-02), finalidad declarada, registro de la base y un manual de tratamiento. Un cashierless que **sigue personas** y las vincula a su medio de pago es un tratamiento mucho más intenso | Baja para el ángulo D (fotos de góndola, conviene **difuminar caras** de quien pase). Alta para el cashierless. **Consultar con un abogado antes de cámaras fijas con personas** |
| **Hardware** | Importación, instalación, roturas, conectividad. Costo y aranceles **[NO VERIFICADO]** | Alta para A, B y C. Nula para D, E y F |
| **Dependencia de APIs** | Cambios de precio (Gemini 3.8 Flash duplica precio en 2027) o de comportamiento del modelo | Media. Mitigación: poder cambiar de proveedor |
| **Mercado frágil** | Consumo masivo -13,9% en 2024; cierres de kioscos y chinos | Media |
| **Ciclo de venta B2B** | Las marcas grandes compran con pilotos largos (Simbe: casi la mitad de sus 29 clientes seguía en piloto en 2024) | Media. Las distribuidoras y marcas PyME deciden más rápido (hipótesis **[NO VERIFICADO]**) |
| **Capital de Facu** | ~USD 1.300 | Solo alcanza para D, E o F en versión concierge |

---

## 9. Cómo validar en 2-4 semanas con menos de USD 200

**Pérdida máxima:** USD 200 y 4 semanas. **Fecha de corte:** 4 semanas después de arrancar.

**Semana 1: entrevistas (USD 0-40 en viajes).** Seguir el método "The Mom Test": preguntar por el pasado y por plata, no por la idea.
- **5 almaceneros o encargados de autoservicio:** ¿cómo controlan hoy el stock?, ¿cargan las compras?, ¿cuánto pagan por su sistema?, ¿qué les costó el último faltante?
- **5 preventistas o dueños de distribuidoras:** ¿cómo arman el pedido sugerido?, ¿cuánto tiempo pasan en cada comercio?, ¿pierden ventas por faltantes en el almacén?
- **3-5 personas de trade marketing de marcas medianas** (alimentos, bebidas, limpieza; vía LinkedIn o contactos de la facultad): ¿cómo auditan la góndola del canal tradicional?, ¿usan Trax, Ailet o Involves?, ¿cuánto pagan por visita de auditoría?
- **Pregunta clave para todos:** "¿Cuánto gastaste el año pasado en resolver esto?"

**Semanas 1-2: prueba técnica (USD 5-20 en API).**
- Con permiso del comercio, sacar **100 fotos de góndola** en 5 almacenes y 2 autoservicios.
- Contar a mano lo que hay (la "verdad"). Pasarlas por Gemini Flash y Claude Haiku desde la consola web (Google AI Studio o la consola de Anthropic, sin programar) con 3 tareas: (1) huecos visibles, (2) presencia de 20 SKUs de una marca elegida, (3) precios y vencimientos legibles.
- **Medir:** porcentaje de aciertos por tarea, falsos positivos y tiempo de revisión humana por foto.
- **Gate técnico:** al menos **90% de acierto** en presencia o ausencia de los SKUs objetivo y en detección de huecos. Si no se llega, el ángulo D necesita un modelo entrenado (nivel 2) y no es para ahora.

**Semanas 2-4: concierge con precio (USD 50-150).**
- Ofrecer a **1-2 distribuidoras o marcas medianas** un **reporte semanal de faltantes y exhibición de 20 puntos de venta**, hecho por Facu con fotos + IA + revisión.
- Cobrar un precio simbólico o pedir **una carta de intención con precio** para la versión continua (el monto a proponer sale de las entrevistas).
- **Gate comercial:** al menos **3 de 10 prospectos B2B** aceptan un piloto pago o firman una carta de intención con precio. Del lado del almacén, al menos **5 de 15 almaceneros** dicen que pagarían un monto concreto (y no solo "está bueno").

**Decisión al cierre:** si se cumplen ambos gates, armar el nivel 1 (MVP software con socio técnico). Si se cumple solo el técnico, probar otro pagador. Si no se cumple ninguno, cerrar y escribir el post-mortem (regla del proyecto).

---

## 10. Veredicto

### 10.1 Puntajes (1-10; en riesgo, 10 = bajo riesgo) [OPINIÓN fundada en los datos de arriba]

| Criterio | A. Amazon Go argentino | B. Cámaras fijas en súper | **D/E. Foto de celular B2B (marcas y distribuidoras)** | F. Stock por foto para el almacenero |
|---|---|---|---|---|
| **Tamaño del problema** | 4: ahorro de cajeros, menor en Argentina que en EE.UU. | 7: faltante histórico de 4-19% y ~4% de ventas perdidas | **7**: canal tradicional con ~35% del consumo masivo y más de 194.700 puntos de venta; las marcas cargan ~33% de la pérdida por faltante | 6: stock desordenado y merma de 3-5% de las ventas, pero cada comercio es chico |
| **Disposición a pagar** | 2: ni Amazon logró que cerrara la cuenta | 4: en EE.UU. pagan; en Argentina, sin evidencia | **5**: las marcas ya pagan repositores y software, y Kamay y Arca invierten en el canal; falta verificar marcas PyME y distribuidoras | 3: ticket bajo y comercios cerrando |
| **Espacio frente a la competencia** | 2: global en retirada y local ya intentado (Go2Future) | 3: Focal, Simbe, Trax/FORM | **4**: Trax/FORM, Ailet, Involves, Teamcore y Sensify; posible hueco en el segmento chico y en distribuidoras | 5: muchos puntos de venta, pocos con IA (no verificado) |
| **Ventaja de Facu** | 1: nada | 2: sabe de inventarios, sin capital ni red | **4**: ingeniero industrial con práctica en logística (reposición, ABC), pero sin red en consumo masivo ni ML | 5: entiende el stock y puede hacer trabajo de campo |
| **Factibilidad con sus recursos** | 1: hace falta ~USD 900.000 | 2: hardware y capital | **6**: concierge sin código y MVP con un socio técnico | 6: similar |
| **Escalabilidad** | 3: hardware por tienda | 5: software + hardware | **7**: software puro, replicable en LATAM, con datos acumulables | 5: muchos clientes chicos, costo de adquisición y abandono altos |
| **Riesgo (10 = bajo)** | 1: capital, técnico, privacidad | 3 | **5**: riesgo técnico medible barato y competencia fuerte | 5 |
| **Promedio simple** | **2,0** | **3,7** | **5,4** | **5,0** |

*El promedio simple es una ayuda, no un veredicto: los criterios no pesan igual. Para Facu, la disposición a pagar y la factibilidad pesan más.*

### 10.2 Opinión (marcada como tal)

**[OPINIÓN]** El "Amazon Go argentino" no tiene sentido, ni para Facu ni, hoy, para nadie en Argentina. Amazon gastó lo que quiso, necesitó personas revisando y etiquetando, y el 27 de enero de 2026 cerró sus propias tiendas. Grabango murió y Standard AI pivotó. En Argentina ya lo intentaron Go2Future y Carrefour en 2022-2023, y no encontré evidencia de que haya escalado. El cajero argentino cuesta menos en dólares que el estadounidense y el súper argentino viene de vender menos, así que el repago sería peor que en EE.UU. Además, la parte de "descontar lo que se lleva el cliente" ya la resuelve el lector de código de barras de cualquier caja. **El problema de stock no está en las salidas, está en las entradas, en la reposición y en que nadie mira la góndola.**

La versión que sí puede tener sentido es usar la IA como **ojos baratos en el canal tradicional**: fotos de celular que ya sacan repositores, preventistas o el propio almacenero, procesadas con modelos multimodales por fracciones de centavo, con revisión humana donde haya duda, y vendidas a quien pierde plata con el faltante y tiene presupuesto (**distribuidoras y marcas medianas**). Para la etapa 1 puede arrancar como **servicio de auditoría de góndola con IA** (concierge, casi sin capital), lo que daría ingresos y aprendizaje. Si se valida, el activo de etapa 2 sería una **red de datos de qué hay y qué falta en decenas de miles de almacenes**, algo que hoy solo tienen a medias las marcas grandes y que fondos como Kamay y AC Ventures ya mostraron estar dispuestos a financiar. Dos advertencias honestas: **(1)** no sería "el primero" (Sensify, Involves y Trax ya están), así que la ventaja tiene que salir de foco, precio y ejecución; y **(2)** la disposición a pagar de marcas PyME y distribuidoras es **la gran incógnita**. Si las entrevistas no la muestran, esta idea no debería avanzar, por linda que sea la tecnología.

---

## 11. Lo que no pude verificar (huecos para una próxima sesión)

1. El estado actual (2025-2026) de Zippin, AiFi, Trigo, Mashgin, Veeve, Shelfie, Go2Future/MiniGo y Carrefour Flash Pilar.
2. Precios reales de Trax/FORM, Ailet, Involves Stage, ShelfWatch, Focal y Simbe (ninguno los publica).
3. La tarifa por visita de auditoría o reposición en Argentina.
4. El costo y los aranceles de cámaras IP importadas en Argentina en 2026.
5. Cantidad de almacenes y de bocas de supermercados de cadena en Argentina, y qué porcentaje usa software de stock.
6. Un dato reciente (2024-2026) de faltante en góndola en Argentina (lo último es GS1 2018).
7. El documento original de The Information sobre los revisores de Amazon (con muro de pago) y la cifra exacta de tiendas cerradas en 2026.
8. Si existe una startup argentina de reconocimiento de góndola por foto (no la encontré, pero la búsqueda quedó cortada por el límite).
9. El precio y los límites del nivel gratuito de Google AI Studio para la prueba técnica.
10. Los salarios de cajeros en Argentina, para hacer el cálculo de repago de un cashierless local.

---

## 12. Fuentes (todas consultadas el 2026-10-08)

**Cashierless y Amazon**
- Retail Dive, "Amazon removes Just Walk Out tech from Amazon Fresh stores, adds Dash Carts", 2024-04-03: https://www.retaildive.com/news/amazon-removes-just-walk-out-tech-amazon-fresh-stores-dash-carts/712150
- RetailWire, Dash Cart en Amazon Fresh (27 de 44 tiendas), 2024: https://retailwire.com/?p=230660
- TechCrunch, "Amazon is closing its physical Amazon Go and Amazon Fresh stores", 2026-01-27: https://techcrunch.com/2026/01/27/amazon-is-closing-its-physical-amazon-go-and-amazon-fresh-stores
- Wikipedia, "Amazon Go" (dato de más de 360 ubicaciones de terceros citado del blog de Amazon): https://en.wikipedia.org/wiki/Amazon_Go
- Cross-Border Magazine, cierre de 8 Amazon Go (2023): https://cross-border-magazine.com/amazon-go-will-close-8-stores/
- KUOW, "Is Amazon's 'Just Walk Out' technology powered by AI or by hundreds of underpaid workers in India?", 2024: https://thankyou.kuow.org/stories/is-amazon-s-just-walk-out-technology-powered-by-ai-or-by-hundreds-of-underpaid-workers-in-india
- ITC.ua, resumen del reporte de The Information, 2024: https://itc.ua/en/news/amazon-closes-cash-registers-just-walk-out-ai-triumph-was-the-result-of-thousands-of-indian-workers
- Modern Retail, "Why Just Walk Out wasn't the right fit for grocery", 2024-04-04: https://www.modernretail.co/technology/amazon-briefing-why-just-walk-out-wasnt-the-right-fit-for-grocery/
- IADS, "Why Amazon's Just Walk Out tech failed": https://www.iads.org/member/articles-reports/why-amazon-s-just-walk-out-tech-failed
- Digital Center, "How far can cashier-less stores go?" (estimaciones de costo): https://www.digitalcenter.org/columns/cashierless-stores/
- Harvard D3 (análisis de estudiantes, repago de 8 años): https://d3.harvard.edu/platform-rctom/wp-json/wp/v2/hck-submission/37013
- The Spoon, "Cashierless checkout pioneer Grabango shuts down…", 2024-10-09: https://thespoon.tech/cashierless-checkout-pioneer-grabango-shuts-down-after-failing-to-secure-additional-funding/
- CSP Daily News, Grabango (cifra de CNBC, ~USD 73 M): https://cspdailynews.com/technologyservices/checkout-free-technology-provider-grabango-shuts-down
- Pulse 2.0, entrevista con el CTO de Standard AI, 2024-10-07: https://pulse2.com/standard-ai-profile-david-woollard-interview/
- The Spoon, Serie C de Standard Cognition (USD 150 M): https://thespoon.tech/standard-cognition-raises-150m-series-for-its-cashierless-checkout
- Axios, Standard AI compra Skip, 2023-02-02: https://www.axios.com/pro/retail-deals/2023/02/02/autonomous-tech-standard-ai-acquires-self-checkout-skip
- Retail Dive, Zippin levanta USD 12 M: https://www.retaildive.com/news/zippin-raises-12m-to-introduce-cashierless-checkout-to-more-stores/569095/
- PYMNTS, Zippin USD 30 M: https://www.pymnts.com/?p=1144825
- Retail Dive, AiFi levanta USD 65 M: https://www.retaildive.com/news/aifi-raises-65m-as-retailers-sharpen-focus-on-computer-vision/620506
- The Spoon, Trigo levanta USD 60 M: https://thespoon.tech/cashierless-checkout-startup-trigo-raises-60m
- Perfil, "Argentina ya tiene su primer supermercado inteligente sin sector de cajas", 2023-02-10: https://www.perfil.com/noticias/modo-fontevecchia/argentina-ya-tiene-su-primer-supermercado-inteligente-sin-sector-de-cajas-modof.phtml
- Economía Sustentable, Carrefour y Go2Future/MiniGo: https://economiasustentable.com/noticias/sin-filas-ni-cajeros-asi-funciona-la-nueva-tienda-inteligente-que-abrio-una-importante-cadena-de-supermercados-en-argentina/
- Forbes Argentina, Carrefour con locales autónomos: https://www.forbesargentina.com/innovacion/carrefour-incorpora-inteligencia-artificial-apuesta-locales-autonomos-e-inteligentes-n29663/amp

**Góndola, robots, carritos y cajas**
- Bloomberg (vía BloombergQuint), Trax USD 640 M, abril de 2021: https://www.bloombergquint.com/markets/softbank-blackrock-lead-640-million-funding-for-startup-trax
- Global Venturing, Trax Serie E, 2021-04-08: https://globalventuring.com/blog/2021/04/08/trax-traps-640m-in-series-e-round/
- Globes, despidos en Trax (2022): https://en.globes.co.il/en/article-1001415644
- Calcalist, despidos en Trax (2020): https://www.calcalistech.com/ctech/articles/0,7340,L-3815332,00.html
- Lincoln International, Gemspring adquiere FORM y el segmento de reconocimiento de imágenes de Trax (2026): https://www.lincolninternational.com/transactions/gemspring-has-acquired-form-and-the-image-recognition-segment-of-trax-retail/
- Nota de prensa sobre la desinversión de Trax, 2026-02-12: https://www.benningtonbanner.com/online_features/press_releases/trax-limited-divests-image-recognition-business-to-gemspring-capital-remaining-trax-ltd-businesses-poised-for/article_ab072e9f-bd96-5551-bb88-f709325e2e8d.html
- Best Practice AI, caso Coca-Cola Hellenic con Trax: https://bestpractice.ai/ai-use-cases/case-studies/consumer-retail/coca-cola-hellenic-covers-3-6x-more-stores-by-automating-in-store-inventory-audits-using-image-recognition
- Focal Systems, FAQ (precio, cámaras por tienda): https://focal.systems/faqs
- Retail Dive, Walmart Canadá con Focal: https://www.retaildive.com/news/walmart-canada-automated-ai-solution-curbs-out-of-stocks/632029
- CDO Magazine, Focal Serie B USD 25,8 M: https://www.cdomagazine.tech/events-announcements/focal-systems-raises-us25-8-million-in-series-b-funding-to-automate-retail-globally
- Fortune, Simbe Serie C, 2024-10-24: https://www.fortune.com/2024/10/24/goldman-sachs-simbe-series-c-robot-business
- Simbe, "10 años de Tally" (nov-2025): https://www.simberobotics.com/about/newsroom/simbe-marks-10-years-of-tally-the-robot
- Robotics 24/7, Tally en Theisen's (abril de 2025): https://www.robotics247.com/article/simbe-tally-inventory-amr-deployed-for-theisens/supply_chain
- Grocery Dive, Walmart deja los robots de Bossa Nova (2020): https://www.grocerydive.com/news/walmart-nixes-plans-to-use-aisle-scanning-robots/588302/
- Fierce Electronics, Bossa Nova tras Walmart (2020): https://www.fierceelectronics.com/electronics/walmart-fires-store-robots-but-bossa-nova-remains-bullish
- Digiday / Modern Retail, "Instacart tripled its smart cart store count this year", 2025-11-28: https://digiday.com/media-buying/instacart-tripled-its-smart-cart-store-count-this-year/
- AOL / NY Post, Caper Carts hasta USD 10.000: https://www.aol.com/future-shopping-instacart-debuts-ai-162906440.html
- Retail Dive, Mashgin USD 62,5 M (2022): https://www.retaildive.com/news/self-checkout-tech-maker-mashgin-raises-625m/623508/
- PYMNTS, Mashgin valuada en USD 1.500 M: https://www.pymnts.com/?p=1301239

**LATAM: reconocimiento de imágenes, trade marketing y heladeras**
- Arca Continental, inversión en Sensify, 2025-04-14: https://www.arcacontal.com/en/noticia/financial/arca-continental-invests-startup-enhance-traditional-channel-ai-cooling-equipment
- El Financiero, 2025-04-16: https://www.elfinanciero.com.mx/monterrey/2025/04/16/invierte-en-la-modernizacion-de-equipos-de-refrigeracion-con-ia/
- Ámbito, "Startup nacional Sensify recibe inversión del fondo de Arcor y Coca-Cola", 2023-12-26: https://www.ambito.com/startup-nacional-sensify-recibe-inversion-del-fondo-arcor-y-coca-cola-n5907197
- iProUP, "Argentinos crean una IA para expendedoras de bebidas y levantan USD 2 millones" (fecha no confirmada): https://www.iproup.com/startups/61717-argentinos-crean-una-ia-para-expendedoras-de-bebidas-y-levantan-usd-2-millones
- Abogados.com.ar, ronda SAFE de Sensify: https://abogados.com.ar/tca-tanoira-cassagne-asesora-a-sensify-en-su-ronda-de-inversion-safe/38751
- Baguete, "Involves adquire startup Stringhini", 2019-01-22: https://www.baguete.com.br/noticias/22/01/2019/involves-adquire-startup-stringhini
- ABES, Involves exportada a varios países: https://abes.com.br/en/?p=2256
- Capterra, Agile Promoter: https://www.capterra.es/software/171231/agile-promoter
- Merca2.0, Ailet en LATAM: https://www.merca20.com/?p=12420125
- Mercado & Consumo, Shelfpix, 2018-05-14: https://mercadoeconsumo.com.br/14/05/2018/noticias/startup-brasileira-lanca-plataforma-de-monitoramento-de-gondolas-na-alemanha/
- Accel-KKR, inversión en Teamcore, 2022-08-30: https://www.accel-kkr.com/accel-kkr-makes-majority-growth-investment-in-teamcore-a-leading-retail-execution-platform-for-cpgs-and-retailers-in-latin-america/
- Forbes Chile, Teamcore compra Grupo BIT, 2024-05-16: https://forbes.cl/negocios/2024-05-16/plataforma-tecnologica-de-origen-chileno-teamcore-adquiere-colombiana-grupo-bit/
- Capterra, ShelfWatch (precio "contactar"): https://www.capterra.com/p/201366/ShelfWatch/
- Portal do Franchising, Market4u con más de 400 franquiciados y 2.100 tiendas, 2023-10-02: https://www.portaldofranchising.com.br/noticias/market4u-tem-mais-de-400-franqueados/
- Portal do Franchising, Market4u, mayor microfranquicia: https://www.portaldofranchising.com.br/noticias/maior-microfranquia-pelo-3-ano/

**Argentina: mercado, merma, faltantes y software**
- Mercado, "NielsenIQ: el canal tradicional ya explica 35% de las ventas de consumo masivo", 2026-06-08: https://mercado.com.ar/negocios/nielseniq-el-canal-tradicional-ya-explica-35-de-las-ventas-de-consumo-masivo
- Mercado, "Autoservicios y almacenes ganan tracción en el consumo masivo durante 2025": https://mercado.com.ar/tendencias/autoservicios-y-almacenes-ganan-traccion-en-el-consumo-masivo-durante-2025
- Infobae, "El consumo masivo cerró el 2025 con subas…", 2026-01-22: https://www.infobae.com/economia/2026/01/22/el-consumo-masivo-cerro-el-2025-con-subas-pero-aun-no-recupero-el-terreno-perdido-durante-2024/
- iProfesional, supermercados chinos y Carrefour Express: https://www.iprofesional.com/negocios/434942-supermercados-chinos-revelaron-plan-para-quedarse-con-supermercado-carrefour-argentina
- Ámbito, cierres de chinos en la cuarentena (2020): https://www.ambito.com/informacion-general/supermercados/en-cuarentena-cerraron-200-chinos-las-ventas-cayeron-25-n5137863
- La Voz de San Justo, kioscos (UKRA): https://www.lavozdesanjusto.com.ar/el-kiosco-de-barrio-en-crisis-16000-locales-cerrados-y-un-simbolo-que-se-pierde
- BID, "Desperdicio de alimentos en supermercados y autoservicios de Argentina: causas y estimaciones" (no pude abrirlo, error 403; datos vía resumen): https://publications.iadb.org/en/node/29756 y https://publications.iadb.org/publications/spanish/document/Desperdicio-de-alimentos-en-supermercados-y-autoservicios-de-Argentina-causas-y-estimaciones-informacion-operativa-2020.pdf
- Chócale, mermas en el retail de Chile (CCS), 2023-06: https://chocale.cl/2023/06/mermas-robos-comercio-perdidas-supermercados-retail-estudio-ccs-alto-uai/
- Mercado, "Faltantes de mercadería en góndola" (GS1): https://mercado.com.ar/revista/numero-1030/faltantes-de-mercaderia-en-gondola/
- The Logistics World, "Se incrementó en 5,8 el faltante de mercadería en góndola": https://thelogisticsworld.com/historico/se-incremento-en-5-8-el-faltante-de-mercaderia-en-gondola
- iProfesional, faltantes en góndolas: https://www.iprofesional.com/marketing/268984-ahora-se-registran-mas-faltantes-en-las-gondolas-de-supermercados-de-todo-el-pais
- Wikipedia, "Stockout" (cita a Gruen y Corsten): https://en.wikipedia.org/wiki/Stockout
- SciELO / RBGN, estudio brasileño sobre faltantes (cita a Gruen, Corsten y Bharadwaj): https://scielo.br/j/rbgn/a/G3PcfMjvCKtmPqMm5PJgnFm/?lang=en
- Supermarket News, estudio GMA 2018: https://www.supermarketnews.com/grocery-trends-data/reducing-online-out-of-stocks-critical-for-retailers-says-gma-study
- GetApp, Ventar: https://www.getapp.com/all-software/a/ventar/
- GetApp, Lider Gestión: https://www.getapp.co.uk/software/2080119/lider-gestion
- Messe Frankfurt, Zoo Logic: https://texpertisenetwork.messefrankfurt.com/frankfurt/en/market-directory.detail.html/EMITEX/zoo-logic-sa.html
- Computrabajo, aviso de repositor/merchandiser (La Plata): https://ar.computrabajo.com/ofertas-de-trabajo/oferta-de-trabajo-de-repositormerchandiser-con-experiencia-en-la-plata-8C8619964C4666E761373E686DCF3405
- Coderhouse, IA para retail físico en Argentina (blog de una empresa que vende cursos; débil como fuente): https://www.coderhouse.com/coderlibrary/ia-para-retail-fisico-argentina-supermercados-tiendas

**Legal (Argentina)**
- Disposición 10/2015 (DNPDP), texto: https://www.argentina.gob.ar/normativa/nacional/243335/texto
- AAIP, videovigilancia: https://www.argentina.gob.ar/aaip/datospersonales/responsables/videovigilancia
- Marval O'Farrell Mairal, "Regulación sobre video vigilancia": https://www.marval.com/publicacion/regulacion-sobre-video-vigilancia-12624
- Beccar Varela, nuevo cartel (Resolución AAIP 38/2024), 2024-02-02: https://beccarvarela.com/novedades/recoleccion-de-imagenes-digitales-nuevo-cartel/
- Microjuris, Disposición 10/2015, 2015-02-27: https://aldiaargentina.microjuris.com/2015/02/27/se-establecen-las-condiciones-de-licitud-para-las-actividades-de-recoleccion-y-posterior-tratamiento-de-imagenes-digitales-de-personas-con-fines-de-seguridad/

**Técnica: precisión y costo de modelos de visión**
- Tamarapalli et al., "CountQA: How Well Do MLLMs Count in the Wild?", arXiv 2508.06585 (2025-08-08, v2 2025-09-09): https://arxiv.org/abs/2508.06585
- "Object Counting with GPT-4o and GPT-5: A Comparative Study", arXiv 2512.03233: https://arxiv.org/html/2512.03233v1
- Goldman et al., "Precise Detection in Densely Packed Scenes" (SKU-110K), CVPR 2019: https://arxiv.org/pdf/1904.00853
- Leaderboard SKU-110K (hyper.ai): https://vercel.hyper.ai/en/sota/tasks/dense-object-detection/benchmark/dense-object-detection-on-sku-110k
- Maminta y Atienza, "What Matters for Grocery Product Retrieval with Open Source Vision Language Models", arXiv 2605.18029 (2026): https://arxiv.org/pdf/2605.18029
- Scientific Reports (dic-2025), planogramas en 7-Eleven Taiwán: https://doaj.org/article/ab8a602260bc47d2a15fbdffb8eb2507
- Google, precios de la API de Gemini (página actualizada el 2026-10-07): https://ai.google.dev/gemini-api/docs/pricing
- Google, comprensión de imágenes en Gemini (tokens por imagen, detección): https://ai.google.dev/gemini-api/docs/image-understanding
- Google, resolución de medios en Gemini 3: https://ai.google.dev/gemini-api/docs/media-resolution
- Anthropic, visión de Claude (tokens por imagen, limitaciones de conteo): https://platform.claude.com/docs/en/build-with-claude/vision
- Anthropic, precios: https://claude.com/pricing
