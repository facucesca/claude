# L6 — "Uber de la logística" como comisionista (B2B y B2C): indagación a fondo

**Fecha:** 2026-10-15
**Idea (Facu, 2026-10-08):** app o empresa que une en todo el país a quienes necesitan transporte con transportistas.
**Comentario de Facu (2026-10-15):** "el comisionista es un gran rubro [...] los intermediarios siempre son los que más ganan como Amazon, Uber, Airbnb [...] también se me ocurrió por eso el Uber de logística B2B o B2C".
**Base:** este informe actualiza y profundiza `research/fuentes/2026-10-08-L6-logistica.md`. No repito lo que ya está ahí. Cuando uso un dato de ese informe, lo marco "(informe 2026-10-08)".
**Método:** 15 búsquedas web (tope) y unas 35 lecturas directas de páginas (sitios de empresas, Boletín Oficial, InfoLEG, ARCA, notas de prensa).

**Convenciones (Regla N.º 1):**
- **DATO** = tiene fuente y fecha. Si la fuente es interesada (la propia empresa, un gremio, un vendedor), lo aclaro.
- **ESTIMACIÓN** = cálculo mío, con el razonamiento a la vista.
- **OPINIÓN** = mi juicio.
- **"No verificado"** = no lo pude confirmar.
- Tipo de cambio supuesto para pasar pesos a dólares: **≈ $ 1.400 por dólar** (es el implícito en las tarifas de abril de 2026 del informe 2026-10-08). **No verifiqué el de octubre de 2026.** Todas las conversiones a dólares son ESTIMACIÓN.

**Regla N.º 2 (no repetir):** no propongo ideas nuevas. Profundizo L6. En el registro (`research/datos/registro-de-ideas.csv`) ya figuran como parte de L6 o parecidas: LOG-1-1 (camiones que vuelven vacíos) y AGR-3-2 (conseguir camiones en cosecha), marcadas como repetidas de L6; MUD-1-4 (mano de obra para mudanzas), COM-3-4 (entregas urgentes a obra sin fleteros) e I18 (plan de mudanza con comparación de fletes), parecidas. LOG-1-4 (pedidos de flete por WhatsApp cargados a mano, nivel "Indagar ya") toca el mismo circuito, pero desde el lado del software. Las nombro solo como referencia.

---

## 0. Resumen en 12 líneas

1. **Hay intermediarios de fletes en Argentina y cobran.** Según un dirigente de transportistas de Río Cuarto (abril de 2026), cobran **"hasta un 10% a 12%"**. Entre lo que paga el productor y lo que recibe el camionero hay una brecha de **"hasta el 20%"**, y la asociación de transportistas retiene un **3%** (LV16, 2026-04-13). Es una fuente interesada que se queja de ellos, pero es el primer dato local de comisión que encontré.
2. **Las apps nuevas de cargas van hacia comisión 0%.** Tracción Argentina (0%), Carga GO (sin comisión por viaje, con suscripción) y FletArg y Flets en fletes chicos ("sin comisiones") lo dicen en sus sitios (2025-2026). **OPINIÓN:** conectar a dos partes, por sí solo, se está volviendo gratis.
3. **Avancargo sigue viva y ya no se presenta como marketplace:** vende software (TMS), torre de control (4PL) y su red de camiones (3PL a demanda). No publica precios. Dice tener +125.000 camiones fiscalizados y +2.000 dadores (su web, 2026-10-15).
4. **El RUTA está eliminado** (Decreto 1109/2024, Boletín Oficial del 2024-12-19) y **no hay un registro que lo reemplace.** Queda vigente la Ley 24.653: libertad de contratación y precios libres, carta de porte o remito, y **seguro sobre la carga** (art. 10).
5. **Para Facu, la figura legal más segura es la de "corredor"** (Código Civil y Comercial, arts. 1345-1355): media entre las partes y cobra comisión, pero **no transporta ni vende el viaje a su nombre.** Si vende el viaje a su nombre, pasa a ser responsable como transportista (arts. 1280-1287).
6. **Capital de trabajo:** en EE.UU. los brokers pagan antes con plata propia, con líneas de crédito o con factoring (1-5% del valor de la factura cada 30 días; FreightWaves, 2026-02-17). En Argentina existen la Factura de Crédito Electrónica MiPyME y el descuento de cheques electrónicos (e-cheq), pero no encontré ninguna fintech que adelante fletes a camioneros. Humber anunció adelantos "en 72 horas" (fecha no confirmada, ~2022).
7. **B2C (fletes chicos y mudanzas): hay muchas apps chicas, pero ninguna dominante.** Fletalo, FletArg, Flets, MiFlete y Weflet, más Uber Envíos para paquetes. **No encontré a Lalamove en Argentina.** El hueco no es la falta de oferta: falta un ganador. Ganar esa carrera cuesta plata en marketing y en densidad, y Facu no la tiene.
8. **En B2C el riesgo legal sube:** la Ley de Defensa del Consumidor (art. 40) puede hacer responsable a la plataforma. Así se lo aplicaron a Booking en 2023 (Cámara Comercial, Sala D, según Derecho en Zapatillas, 2026).
9. **Lo que cambió para Facu desde el 2026-10-08:** antes se dijo que "no tiene red en transporte". Hoy sabemos que **CEMEVA trabaja con fleteros tercerizados y Facu ya tiene una herramienta de seguimiento de esos fleteros.** Eso le da un acceso que el informe anterior no consideró. Pero Facu dijo (2026-10-13) que los granos "no es el rubro que más le gusta" y que no quiere ir 100% por ahí.
10. **Números (ESTIMACIÓN):** como corredor transparente, con una comisión del 3-5% sobre un viaje de US$ 800-1.500, cada viaje deja US$ 25-75. **Para ganar US$ 1.000 por mes hacen falta 13-40 viajes por mes.** Es un negocio chico, salvo que escale mucho.
11. **Filtro: 15/25 → PENDIENTE.** El experimento es baratísimo y se puede hacer en cualquier momento por el acceso que da CEMEVA. Pero no es un producto global, tiene márgenes finos y cae en el rubro que Facu dijo no querer como destino.
12. **Si Facu igual quiere probarlo:** 30 días, menos de US$ 200, con los fleteros de CEMEVA y dadores vecinos, centrado en el viaje de vuelta y los viajes extra (sección 8). **Antes, hablarlo con su papá:** hay un posible conflicto de interés con CEMEVA.

---

## 1. Qué es exactamente (especificación integrada)

Hay tres formas de ser "comisionista de fletes". Son negocios distintos: cambian quién toca la plata, cuánto capital hace falta y quién responde si se pierde la carga.

### 1.1 B2B (empresas, productores, acopios ↔ transportistas)

| Variante | Qué hace Facu | Quién le paga a quién | Cómo cobra Facu | Capital de trabajo | Responsabilidad por la carga |
|---|---|---|---|---|---|
| **A. Corredor puro** (lo que recomiendo para empezar) | Consigue el camión para el dador, o la carga para el camionero. Verifica la documentación y coordina | El dador le paga **directo** al transportista | Comisión fija o porcentaje, facturada aparte, idealmente **al confirmar el viaje** | **Cero** | La tiene el transportista (Ley 24.653, art. 10; CCyC, art. 1286). Facu, como corredor, tiene los deberes del art. 1347 (verificar identidad, informar bien) |
| **B. Gestor "cobra y paga"** (como hacen algunos centros de transportistas, que retienen un %) | Lo mismo que A, más el cobro al dador y el pago al transportista **cuando el dador paga** | Dador → Facu → transportista | Retiene su % al pasar la plata | Bajo, si paga recién cuando cobra. Pero **maneja plata de terceros** (riesgos impositivo y de confianza) | Zona gris. Depende de quién figura como contratante. **Consultar abogado** |
| **C. Broker principal** (el modelo de Convoy, Uber Freight y Kobo360) | Le "vende" el viaje al dador a su nombre y se lo "compra" a un fletero | Dador → Facu (a 30-60 días); Facu → fletero (antes) | Diferencia entre lo que cobra y lo que paga | **Alto.** Ver sección 4.3 | **Facu responde como transportista** frente al dador. La Ley 24.653 (art. 4 h) define al **fletero** como el que trabaja "por cuenta de otro que actúa como principal". El principal sería Facu |

### 1.2 B2C (particulares y comercios chicos ↔ fleteros con camioneta o camión chico)

| Elemento | Cómo funciona hoy en las apps argentinas (DATO, según sus sitios) |
|---|---|
| Quién pide | Un particular (mudanza, un mueble) o un comercio (repartos, materiales) |
| Cómo se fija el precio | Lo **cotiza el fletero** (FletArg, Flets) o lo **calcula un algoritmo** (Fletalo, MiFlete) |
| Quién paga a quién | En general, **directo al fletero** (efectivo o transferencia). MiFlete dice: "Cobro directo o a través de la plataforma" |
| Cómo cobra la app | Casi todas dicen **"sin comisiones"** (FletArg, Flets) y no explican de qué viven. Kargho (2020) cobraba un "honorario" calculado por un algoritmo y sumado al precio del fletero. **No encontré la comisión de Fletalo** |
| Referencia afuera | Porter (India): comisión de hasta 30% (informe 2026-10-08). Lalamove en China: 14-18% (informe 2026-10-08). **Lalamove Brasil bajó la comisión de los viajes en moto de hasta 10 km de 15,99% a 5,99%** (Mercado & Consumo, 2026-02-10) |

**OPINIÓN — la diferencia clave entre B2B y B2C:**
- En **B2B** los viajes se repiten (mismo dador, mismo corredor, cada semana). Eso es bueno para el volumen, pero **facilita que las partes se arreglen directo** sin el intermediario.
- En **B2C** el cliente se muda una vez cada varios años. Casi no hay riesgo de que te salteen, pero **hay que conseguir cada cliente de nuevo** (marketing caro). Además, la ley del consumidor pone más responsabilidad sobre la plataforma.

---

## 2. Mercado en Argentina

### 2.1 Datos nuevos (2026)

| Indicador | Valor | Fuente y comentario |
|---|---|---|
| **Comisión de los intermediarios informales en fletes de granos** | **"Hasta un 10% a 12%"**. Brecha de **"hasta el 20%"** entre lo que paga el productor y lo que recibe el camionero. La asociación de transportistas de Río Cuarto se queda con un **3%** | LV16 Río Cuarto, 2026-04-13. Habla Miguel Targhetta, presidente del Centro de Transportistas Rurales de Río Cuarto. **Fuente interesada:** se queja de los intermediarios ("no tienen camiones, no saben de números, no están inscriptos"). Es una sola zona (sur de Córdoba) |
| **Digitalización (IDT 2026, 4.ª edición, Avancargo)** | 378 empresas encuestadas. **86,5% asigna los viajes sin un software logístico**; 13,5% usa un TMS; 4,2% integró inteligencia artificial | Post de LinkedIn del CEO de Avancargo y Prensa Mercosur (2026-06-28). **Lo tomé del resumen del buscador** (la nota no cargó). **Fuente interesada:** Avancargo vende ese software |
| **Tarifas de referencia** | En abril de 2026 el Ministerio de Economía dijo que la mesa de tarifa de referencia "fue eliminada" por "poco funcional". Las tarifas "son determinadas libremente a partir del acuerdo entre partes" | Bichos de Campo, 2026-04-10. Hubo bloqueos en los puertos de Bahía Blanca y Quequén en abril de 2026 |
| **Conflicto de tarifas en Córdoba** | Los transportistas pidieron +20% sobre la tarifa de Fecotac; los dadores ofrecieron +12% | LV16, 2026-04-13 |
| **Costo del gasoil** | Gasoil grado 3: $ 2.351 por litro en octubre de 2026, +46,8% desde enero de 2026 (≈ US$ 1,68/l, ESTIMACIÓN) | Sitio de TCARGO, consultado el 2026-10-15. **No verificado:** es el monitor de precios de una app, no un dato oficial |
| **Costos del transporte** | +41% interanual (FADEEAC, septiembre de 2026) | Informe 2026-10-08 (Agrofy, 2026-10-06). No re-verificado hoy |

### 2.2 Datos estructurales (del informe 2026-10-08, no repetidos en detalle)
- ~91% de la carga va en camión (BCR, 2018). ~2 camiones por empresa (UNTREF, 2019). Granos por camión: ~137 Mt en 2014 (IAT, citado por la BCR en 2018).

### 2.3 Tamaño (ESTIMACIÓN gruesa, solo para tener una escala)
- **Fletes de granos por camión:** 137 Mt (dato de 2014) × US$ 20-50 por tonelada (supuesto mío: la tarifa orientativa a 400 km era US$ 53,7/t en abril de 2026, y muchos viajes son más cortos) ≈ **US$ 2.700-6.900 millones por año** en fletes de granos.
- **No encontré** cuánto de eso pasa por intermediarios, ni un dato del mercado B2C de fletes y mudanzas. **No invento esos números.**
- **OPINIÓN:** el mercado es enorme. El problema nunca fue el tamaño: es que el margen por viaje es fino y la plata está repartida entre muchísimos actores chicos.

### 2.4 Cómo se mueve la plata en granos (DATOS, con fechas)
- **Quién paga el flete:** el transportista negocia con el dador (productor o acopio), pero "luego el pago lo hace el comprador de esa mercadería" (Bichos de Campo, **2018-10-22**).
- **Plazos:** en 2018 los transportistas reclamaban cobrar a no más de 30 días: "Nos dan un cheque a 60 días pero tenemos un costo financiero del 10,5% mensual" (misma nota de 2018). **Ojo: el buscador la muestra como actual, pero es de 2018.** No encontré un dato de plazos de 2026.
- **Desvíos:** en 2021, Fetra denunció que a los productores se les cobraba "el flete completo a Rosario" y "al transportista le pagan mucho menos" (Bichos de Campo, 2021-09-03).
- **Centros de transportistas:** "en la mayoría de los pueblos del interior productivo hay una relación directa" entre los dadores y los centros de transportistas, que acuerdan tarifas por región (misma nota de 2021, según el resumen del buscador). **OPINIÓN:** en granos, el intermediario "natural" ya existe. Es el centro o la cooperativa de transportistas del pueblo.

---

## 3. Qué existe en Argentina y afuera (verificado) y qué cambió desde el 2026-10-08

### 3.1 B2B en Argentina (estado al 2026-10-15)

| Nombre | Qué hace | Cómo cobra | Tracción (fuente y fecha) | Estado |
|---|---|---|---|---|
| **Avancargo** | TMS en la nube, Control Tower 4PL, 3PL a demanda (su red de camiones) y una app de tareas de campo | **No publica precios ni comisiones** en su web | Web (2026-10-15): "+125.000 camiones fiscalizados", "+2.000 dadores", AR, CL y UY. **Según la propia empresa.** Getlatka **estima** ingresos de US$ 4,4 M (2023), muy por debajo de la meta de US$ 20 M que publicó Forbes en 2023: estimación de terceros, poco confiable. Premios 2026 (Galicia-LA NACION, Acciones Positivas) | **Vivo.** No encontré facturación de 2025-2026 |
| **Humber** | Camiones a demanda para dadores, gestión de flota y app para camioneros. Minería, petróleo, carga general y agro | Según Estación Vial (fecha no confirmada, ~2022): **comisión por viaje que paga el transportista** (sin %). Además, financiación de combustible y "anticipos de liquidaciones en 72 horas" | Más del 70% de sus usuarios llegaron por recomendación (misma nota). La web muestra una "Tarjeta Humber" sin detalles. Hay titulares de prensa de ~2022 sobre "20.000" choferes y "US$ 10 M" de facturación, **que no pude confirmar que sean de Humber** | **Sitio activo** (2026-10-15) |
| **MuvinApp** | Turnos y programación de camiones para agro, por WhatsApp, panel web y app | No publica | Logos de clientes: YPF, Bunge, Glencore, Profertil. Sin cifras | Activo. La web dice "BCR Servicios Digitales", lo que es coherente con la compra por la Bolsa de Comercio de Rosario |
| **Circular** | Turnos de descarga en puertos | **Paga la terminal portuaria.** Gratis para el camionero | 390.000 turnos en 2021 (Estación Vial) | Estado 2026: no verificado |
| **DeTransporte.com** | Bolsa de cargas | Hay que registrarse para ver los contactos. "Suscripción anual" según el resumen del buscador; **la página no muestra precios** | "© 2009 - 2026". El listado muestra 121.838 resultados (no está claro si son activos) | **Activo** desde ~2009 |
| **Rutazo** (Rutazo S.A.S.) | TMS para transportistas + red de cargas | "Gastos de servicio" solo cuando se completa un viaje (según el resumen del buscador de su web; **la página que leí no lo mostraba**) | Sin cifras | Activo (© 2026) |
| **Tracción Argentina** | App para que el camión "no vuelva vacío" | **"0%" de comisión**. Planea planes pagos Base y Pro: "Todavía no publicamos precios" | Sin cifras. No identifica a la empresa que la opera | Activo (© 2026) |
| **Carga GO** | App que conecta camioneros con cargas | "No pagás comisiones por viaje". Habla de una suscripción mensual, pero en otra parte dice "Suscripción gratuita" (contradictorio) | Sin cifras | © 2024 |
| **TCARGO** | Cargas completas, seguimiento. Mendoza e Itajaí (Brasil) | Tiene un enlace a "Precios y Comisiones", pero no muestra las tarifas | Dice tener "7500+" usuarios activos y "10K+" envíos, pero también dice "Recién arrancamos": **cifras inconsistentes, no confiables** | © 2024, con datos de octubre de 2026 |
| **Kargho** | Fletes (2018-2020) | Honorario por algoritmo (2020) | — | **No verificado:** el dominio kargho.com hoy muestra "MatchFreight.AI" |
| **Intermediarios informales y centros de transportistas** | Reparten viajes, cobran y retienen | **10-12%** (intermediarios) y **3%** (asociación, Río Cuarto) | LV16, 2026-04-13 | El "competidor" real en granos |
| **Grupos de WhatsApp y Facebook** | Bolsa informal | — | **No medido** (sigue pendiente) | — |

### 3.2 B2C en Argentina (fletes chicos y mudanzas)

| Nombre | Dónde | Modelo | Tracción (fuente y fecha) |
|---|---|---|---|
| **Fletalo** | AMBA, Córdoba, Rosario | Cotización por algoritmo; división B2B desde 2022. **Comisión no encontrada** | Fundada en 2020; Endeavor HIT 2024; meta de US$ 450.000 para 2024 (Descubre, 2024-06; iProUP tituló "$450 M" sin aclarar la moneda); en Córdoba, "más de 30 vehículos de carga registrados" (Punto a Punto, 2024-02-29) |
| **FletArg** | Nació en Comodoro Rivadavia, alcance nacional | Los transportistas ponen su precio; "sin intermediarios ni comisiones ocultas" | "Más de 150 transportistas registrados" (ADNSUR, 2025-10-16) |
| **Flets** | Patagonia (Neuquén) | Ofertas de fleteros verificados; "Sin comisiones por viaje" | Android "Próximamente" (sitio, 2026-10-15) |
| **MiFlete** | Argentina | Precio estimado automático; pago en efectivo, transferencia, Mercado Pago o cripto | Sin cifras (© 2026) |
| **Weflet** | AMBA, hasta 1.500 kg | Cotiza en la web y se pide desde la app | Solo el resumen del buscador (el sitio no cargó). No verificado |
| **Uber Envíos / Flash** | Ciudades donde opera Uber | Paquetes que entren en un UberX | No sirve para mudanzas. Según Derecho en Zapatillas (2026), sus términos ponen un tope de 20 kg y ~US$ 100 de valor, y no aseguran el contenido |
| **Lalamove** | **No la encontré en Argentina** | En Brasil desde 2019, en 8 ciudades. Dice tener "2 milhões de motoristas parceiros ativos mensalmente" (según la propia empresa) | Mercado & Consumo, 2025-11-06 y 2026-02-10 |

### 3.3 Afuera: lo nuevo que suma a la tabla del 2026-10-08
- **Cómo financian los brokers de EE.UU. el pago anticipado** (FreightWaves, 2026-02-17, nota con contenido promocional de un socio): factoring con adelanto del **80-95%** de la factura y un costo de **"roughly 1%-5% of invoice value per 30 days"**. Con recurso: si el cliente no paga en 60-90 días, el broker tiene que devolver la plata. El **"quick pay"** (pagarle al camionero en 1-3 días a cambio de un descuento) cuesta **1-3% del viaje, 2% lo más común**, según blogs de factoring y despacho (otrucking y otros, 2026; **fuentes interesadas, tomadas del resumen del buscador**).
- **Brasil:** no hay un tope legal a la comisión del "agenciador de cargas". Las cámaras de camioneros denuncian que la intermediación se queda con el 40% del flete (CNTA, 2021) y hasta con el 50-70% en los viajes de retorno a puertos (Aprosoja-MT). **Son fuentes muy interesadas y las tomé del resumen del buscador.** Hubo una propuesta de tope del 10% que no encontré convertida en norma.
- **Moving Truck (Delpa Tecnología):** cobra "una comisión por el uso de la infraestructura" y "la gestión de pagos queda a cargo de Delpa" (blog de Delpa, 2026-10-07). Por el teléfono y la dirección, parece ser de **Chile** (inferencia mía).

### 3.4 Qué cambió desde el informe del 2026-10-08
1. **Primer dato local de comisión:** intermediarios al 10-12% y asociación al 3% (2026-04-13). Antes no había ninguno.
2. **Nuevos jugadores B2B** (Rutazo, Tracción Argentina, Carga GO, TCARGO, DeTransporte.com) y **nuevos B2C** (FletArg, Flets, MiFlete, Weflet). **Tendencia (OPINIÓN):** la mayoría anuncia comisión 0% y vive (o planea vivir) de suscripciones o software.
3. **Avancargo:** sin cambios de modelo visibles. Publicó el IDT 2026 y ganó premios en 2026. Sigue sin precios públicos ni facturación conocida de 2025-2026.
4. **RUTA:** se confirmó leyendo el decreto que **está eliminado y no tiene reemplazo** (pendiente n.º 8 del informe anterior, resuelto).
5. **Marco legal del corredor** (CCyC, arts. 1345-1355): nuevo en este informe.
6. **Sindicato de Camioneros:** no encontré ninguna postura pública de 2025-2026 contra las apps de fletes. Lo más cercano es su conflicto con Mercado Libre por el encuadre de sus trabajadores de depósito (resumen del buscador). El riesgo sigue sin verificar, pero no apareció nada nuevo.
7. **Frutas y verduras:** con una 2.ª búsqueda, **sigue sin aparecer ninguna startup** de logística frutihortícola en Argentina. Que no aparezca no prueba que no exista.
8. **Corrección importante:** el informe anterior puso "Ventaja de Facu: 3/10, sin red en transporte". **Eso quedó viejo:** desde el 2026-10-13 sabemos que CEMEVA trabaja con fleteros tercerizados y que Facu hizo una app que les sigue los viajes y les reclama las facturas (MEMORY.md). Por eso propongo cambiar el corredor del experimento: **del Mercado Central a la red de CEMEVA** (sección 8).

---

## 4. Cómo se construiría y cuánto costaría (todo ESTIMACIÓN salvo que diga DATO)

### 4.1 Por etapas

| Etapa | Qué es | Costo | Tiempo | ¿Puede Facu? |
|---|---|---|---|---|
| **0. Corredor manual (concierge)** | WhatsApp Business + planilla (camiones, documentos, rutas habituales, días libres; cargas disponibles) + un mensaje modelo que aclare "conecto, no transporto" | US$ 0-50 + monotributo si no lo tiene (categoría A: $ 49.527 por mes desde el 2026-08-01 según ARCA ≈ US$ 35) | 1 semana | **Sí** |
| **1. Herramienta propia simple** | Facu ya llevó a producción una app con Claude (CEMEVA). Podría armar un bot de WhatsApp o un panel web: alta de camiones, avisos de cargas por zona, registro de comisiones | US$ 0-50 por mes de hosting y herramientas. **No verifiqué** el costo actual de la API de WhatsApp Business | 3-6 semanas | **Sí, si la etapa 0 funcionó** |
| **2. Marketplace con pagos** | La app cobra al dador y le paga al transportista, con validación de documentos, seguimiento y calificaciones | US$ 15.000-50.000 si se paga a mercado (informe 2026-10-08) + capital de trabajo (4.3) + procesador de pagos habilitado | 3-6 meses | **No con US$ 1.300** |

### 4.2 Cuánto deja (variante A, corredor)
- **Valor del viaje:** US$ 800-1.500 (supuesto). La tarifa orientativa de granos a 400 km daba unos US$ 1.500 por camión de 28 t en abril de 2026 (informe 2026-10-08). Pero **lo pagado real suele estar por debajo de la orientativa** (Bichos de Campo, 2023-04-21, para aquel momento).
- **Comisión posible:** un recién llegado que se presenta como transparente difícilmente cobre el 10-12% que critican los transportistas. Supongo un **3-5%**, cerca del 3% de la asociación (OPINIÓN).

| Comisión por viaje | US$ 1.000/mes | US$ 3.000/mes | US$ 5.000/mes |
|---|---|---|---|
| US$ 25 (3% de US$ 800) | 40 viajes | 120 viajes | 200 viajes |
| US$ 45 (3% de US$ 1.500) | 22 viajes | 67 viajes | 111 viajes |
| US$ 75 (5% de US$ 1.500) | 13 viajes | 40 viajes | 67 viajes |

- Es **margen bruto**: no descuenta el tiempo de Facu, el teléfono, la nafta ni las comisiones que no se cobran.
- **OPINIÓN:** para que sea un negocio que justifique dedicarse en serio, hay que mover **más de 60-100 viajes por mes**. Eso es una operación de varias personas, con guardias en cosecha.

### 4.3 El capital de trabajo (variante C), con los números actualizados
- **Cálculo del informe 2026-10-08 (sigue valiendo):** si se le paga al camionero a los 7 días y se le cobra al dador a los 60, cada viaje deja US$ 1.350 atados ~53 días. Con 20 viajes por mes, eso son **~US$ 47.700 en la calle.**
- **Si se financia con factoring** a un 3% cada 30 días (punto medio del rango 1-5% de EE.UU.; **no encontré tasas argentinas de 2026**): 53 días cuestan **~5,3% del viaje.** Con un margen del 10%, **la mitad se va en financiación.**
- **Herramientas argentinas que existen (DATO):**
  - **Factura de Crédito Electrónica MiPyME:** obligatoria cuando una MiPyME le factura a una gran empresa **$ 5.549.862 o más** (desde el 2026-04-14; ≈ US$ 3.960). Una vez aceptada, se puede negociar en el Mercado Argentino de Valores (MAV) o con bancos. El plazo para aceptarla o rechazarla es de **21 días corridos** hasta el **2026-10-31** (Resolución SPyME 219/2025). **No sé qué pasa después del 2026-10-31:** no encontré una nueva prórroga. Ojo: un solo viaje de US$ 1.500 está por debajo del mínimo. Habría que facturar por mes (ESTIMACIÓN).
  - **Cheques de pago diferido y e-cheq:** se descuentan en el MAV o en bancos. **No verifiqué las tasas de 2026.**
  - **Humber** anunció "anticipos de liquidaciones en 72 horas" y financiación de combustible (Estación Vial, ~2022). No sé si sigue.
- **Conclusión (OPINIÓN):** con US$ 1.300, **la variante C está descartada.** La variante B ("cobra y paga") solo si paga *después* de cobrar, y con un contador al lado.

---

## 5. Regulación y riesgos

### 5.1 Normas (fuentes oficiales)

| Tema | Qué dice | Fuente |
|---|---|---|
| **Libertad de contratación** | El sistema opera "con precios libres" y con "plena libertad de contratación" para quien cumpla la ley | Ley 24.653, art. 1 (texto actualizado, argentina.gob.ar) |
| **Qué es un fletero** | "transportista que presta el servicio por cuenta de otro que actúa como principal" | Ley 24.653, art. 4 h |
| **Requisitos del transportista** | Persona física: inscripta "en la matrícula de comerciante" y en los organismos previsionales e impositivos. Sociedad: con el transporte en su objeto social | Ley 24.653, art. 8 |
| **Documentos** | En servicios entre jurisdicciones: "carta de porte o un contrato de ejecución continuada". Toda mercadería va con esos documentos o con un remito | Ley 24.653, art. 9 |
| **Seguros** | Obligatorios: responsabilidad civil hacia terceros y **seguro sobre la carga** "únicamente mediando contrato de transporte". Lo contrata el remitente; si no, el transportista, con cargo al dador | Ley 24.653, art. 10 |
| **Corresponsabilidad** | El transportista responde por las infracciones; el dador es solidario si tiene relación con el hecho o si falta documentación | Ley 24.653, art. 12 |
| **RUTA** | **Eliminado.** El Decreto 1109/2024 deroga los arts. 9 a 17 bis (y otros) del Anexo I del Decreto 1035/2002, donde estaba el registro. No crea otro. Las multas pasan a medirse en unidades equivalentes a 100 litros de gasoil (máximo 1.000 por falta) | Decreto 1109/2024, BO 2024-12-19 |
| **Contrato de transporte** | El transportista se libera solo "probando la causa ajena" (art. 1286). Si hay varios transportistas en un solo contrato, o no se sabe dónde ocurrió el daño, **responden todos solidariamente** (art. 1287) | CCyC (InfoLEG) |
| **Corretaje** (la figura para Facu) | El corredor "se obliga ante otra, a mediar en la negociación y conclusión" de negocios, sin relación de dependencia ni de representación (art. 1345). Tiene que verificar la identidad de las partes e informar con exactitud (art. 1347). Cobra la comisión "si el negocio se celebra como resultado de su intervención" (art. 1350). Si no se pactó, rige la de los usos del lugar (art. 1350). Si interviene un solo corredor, **le deben comisión todas las partes**, salvo pacto en contrario (art. 1351) | CCyC (InfoLEG) |
| **Corredor no habilitado** | El art. 1346 habla del corredor "habilitado para el ejercicio profesional". **No verifiqué** qué cambia para un corredor sin matrícula. **OPINIÓN:** dejar todo por escrito (con WhatsApp alcanza para empezar) y consultarlo con un abogado | CCyC, art. 1346 |
| **B2C: Defensa del Consumidor** | El art. 40 de la Ley 24.240 hace responsables solidarios a todos los de la cadena. "el transportista responderá por los daños ocasionados a la cosa". En 2023 la Cámara Comercial (Sala D) trató a Booking como parte de la cadena y no como "mero intermediario tecnológico". El art. 37 tiene por "no convenidas" las cláusulas que limitan la responsabilidad | Derecho en Zapatillas (2026), comentando la ley y el fallo. **Es un blog**, no el fallo original |
| **Facturación** | **Corredor:** factura solo su comisión (monotributo). **Principal:** factura el flete entero. El tope del monotributo más alto (categoría K) es de **$ 126.610.838,75 por año** desde el 2026-08-01 (ARCA) ≈ US$ 90.000. A US$ 1.500 por viaje, son ~60 viajes por año (ESTIMACIÓN). Después hay que pasar a Responsable Inscripto | ARCA, tabla del monotributo |
| **Granos: carta de porte electrónica** | Obligatoria (RGC 5017/2021, modificada por la RGC 5821/2026) | Informe 2026-10-08. **No verifiqué** si la CPe tiene un campo para el intermediario del flete. **Facu lo puede ver en las cartas de porte de CEMEVA** |

### 5.2 Riesgos (actualizados)

| Riesgo | Detalle | Severidad (OPINIÓN) |
|---|---|---|
| **Que las partes se arreglen directo** | En granos, con dadores y fleteros que se repiten, es el riesgo n.º 1. Las apps gratis lo agravan: el camionero tiene alternativas sin comisión | **Alta** |
| **Responsabilidad por la carga** | Baja si Facu es corredor puro. **Alta** si vende el viaje a su nombre (CCyC, arts. 1286-1287; Ley 24.653, art. 4 h) | Media |
| **Conflicto de interés con CEMEVA** | Si Facu les consigue viajes a terceros a los fleteros de CEMEVA, en cosecha pueden faltarle camiones a CEMEVA. Además, Facu conoce las tarifas de CEMEVA (información confidencial) | **Media-Alta** (hay que hablarlo antes) |
| **Mala imagen del intermediario** | Los transportistas acusan a los intermediarios de quedarse con una parte sin transparencia (2021, 2026). Entrar como "un intermediario más" puede generar rechazo | Media |
| **Conflictos de tarifas y paros** | Abril de 2026: bloqueos en Bahía Blanca y Quequén, paros en el sur de Córdoba, mesa de tarifas eliminada | Media |
| **Plata de terceros** (variante B) | Manejar cobros y pagos de terceros tiene implicancias impositivas y de confianza. **No lo verifiqué en detalle** | Media |
| **B2C: consumidor** | La plataforma puede responder por roturas o pérdidas (art. 40) | **Alta** para B2C |
| **Sindicato** | Sin evidencia nueva de conflicto con apps (2025-2026). En el transporte con dueños de camión, el sindicato pesa menos (OPINIÓN) | Baja-Media (no verificado) |

---

## 6. Respuestas a las dudas de Facu

**"Los intermediarios siempre son los que más ganan (Amazon, Uber, Airbnb)."**
- **No estoy de acuerdo del todo, y lo digo con datos.** En fletes, el intermediario digital más famoso, **Uber Freight, sigue perdiendo plata**: pérdida operativa de US$ 24 M sobre US$ 1.583 M facturados en el 2T-2026 (informe 2026-10-08; no re-verificado hoy). **Convoy cerró** en 2023. **Porter** (India) gana plata, pero con un margen EBITDA del 1,94% en su año fiscal 2025 (informe 2026-10-08).
- **OPINIÓN:** el intermediario gana mucho cuando se cumplen tres cosas. (1) Es el dueño de la demanda y cada usuario nuevo atrae a otros (efecto red). (2) Hay muchísimas transacciones chicas y frecuentes. (3) A las partes les cuesta saltearlo. En fletes B2B falla la (3) y el margen es fino. En B2C urbano se cumplen la (1) y la (2), pero solo con mucha densidad en una ciudad, y eso cuesta mucho capital.
- **Sí es cierto a escala chica:** en granos hay intermediarios informales que cobran 10-12% (2026-04-13). Pero lo hacen con relaciones de años, a veces sin transparencia, y no son empresas escalables.

**1. Bolsas de cargas y apps de fletes en 2026.** Ver tablas 3.1 y 3.2. Resumen: Avancargo pasó a software y servicios. En granos están Humber, MuvinApp (BCR) y Circular. Aparecieron varias apps nuevas al 0%. En B2C hay muchas apps chicas regionales y Fletalo es la más establecida. **Casi ninguna publica cuánto cobra.**

**2. Comisión típica.**
- **Argentina:** 10-12% (intermediarios informales en granos) y 3% (asociación de transportistas), los dos de LV16 (2026-04-13, fuente interesada).
- **Región y afuera:** Lalamove Brasil cobró 15,99% en motos y lo bajó a 5,99% (2026-02-10). Brokers de EE.UU.: margen bruto del 12-16%. BlackBuck: 6-8%. Porter: hasta 30% (informe 2026-10-08).
- **No hay un porcentaje legal:** el CCyC dice que, si no se pacta, rige el uso del lugar (art. 1350).

**3. Capital de trabajo.**
- Los que funcionan afuera lo financian con plata propia, líneas de crédito o factoring (1-5% cada 30 días), y le cobran al camionero el pago rápido (1-3%).
- En Argentina existen la FCE MiPyME y el descuento de e-cheq, pero **no encontré ninguna fintech que adelante fletes a camioneros.**
- **Lo que recomiendo:** no tocar la plata (variante A).

**4. Regulación.**
- No hay registro nacional (el RUTA se eliminó).
- Rigen la Ley 24.653 (carta de porte o remito, seguro de carga) y el CCyC (corretaje y transporte).
- Como corredor, Facu factura solo su comisión. Como principal, responde por la carga y se va rápido del monotributo.
- **Antes del primer viaje: una consulta con un abogado y un contador** (quizás el de CEMEVA).

**5. B2C: ¿hay hueco?**
- **OPINIÓN:** hay hueco de **ganador**, no de oferta. Hay al menos 6 apps y casi todas dicen no cobrar comisión, lo que sugiere que todavía nadie encontró cómo cobrar.
- Para ganar hacen falta densidad en una ciudad y marketing (cada mudanza es un cliente nuevo), además de asumir más riesgo legal (ley del consumidor).
- **Con US$ 1.300, no es para Facu ahora.** El B2C que se repite (comercios y corralones con repartos semanales) se parece a COM-3-4 del registro. No lo investigué como idea nueva (Regla N.º 2).

**6. ¿Dónde tiene ventaja Facu? (OPINIÓN fundada)**
- **Ventajas reales:**
  - **Acceso:** fleteros que ya trabajan con CEMEVA, conocimiento de cartas de porte, liquidaciones y reclamos de facturas, y una app que ya sigue viajes y facturas de fleteros.
  - **Credibilidad:** "soy de CEMEVA" abre puertas con fleteros y con acopios vecinos.
  - **Herramientas:** sabe llevar software a producción con Claude.
- **Dónde las usaría:** como **corredor transparente** para (a) **viajes de vuelta o viajes extra** de los fleteros de CEMEVA, con cargas de otros dadores de la zona (insumos, fertilizantes, otros acopios), y (b) **picos de cosecha** en los que a CEMEVA o a sus vecinos les faltan camiones. Hay una anécdota de 2023: un chofer volvía de Rosario con fertilizantes para pagar el viaje, y en la sequía casi siempre volvía vacío (La Nación, 2023-05-08, según el resumen del buscador).
- **Lo que juega en contra:**
  - Facu dijo (2026-10-13) que los granos no son su rubro favorito y que no quiere ir 100% por ahí.
  - Quiere algo **global y de producto** (2026-10-14), y un corredor es servicio local.
  - El conflicto de interés con CEMEVA.
- **Lo más valioso que puede sacar (OPINIÓN):** las entrevistas con los fleteros pueden mostrar si el dolor real está en **cobrar** (plazos, cheques, facturas reclamadas) más que en conseguir carga. La evidencia mundial apunta a que la plata está en servirle al camionero (informe 2026-10-08). Eso es una **hipótesis**, no un dato.

---

## 7. Filtro final

| Criterio | Puntaje (1-5) | Justificación |
|---|---|---|
| **F1. Demanda comprobable en Argentina** | **3** | El flete se paga siempre y hay intermediarios cobrando 10-12% y asociaciones cobrando 3% (LV16, 2026-04-13). Pero la fuente es interesada y de una sola zona, no sé cuántos viajes pasan por intermediarios, y la ola de apps al 0% muestra que "solo conectar" ya no se paga |
| **F2. Producto automatizable y global** | **2** | Como corredor es un servicio local, de relaciones y con guardias en cosecha. El marketplace sí es software, pero su liquidez es por corredor y por ciudad; afuera fracasó con cientos de millones (Convoy, Kobo360) y los que sobreviven giraron a software y servicios (Avancargo, Transfix) |
| **F3. Validable rápido y barato (30 días, < US$ 300)** | **4** | Con los fleteros de CEMEVA, las entrevistas y los primeros viajes cuestan menos de US$ 200. No es un 5 porque cerrar viajes reales en 30 días depende de la época de cosecha y del permiso de CEMEVA |
| **F4. Riesgo legal manejable (5 = bajo)** | **3** | Como corredor puro y sin tocar plata, es manejable. Hay zona gris si se lo ve como principal (CCyC 1287, Ley 24.653 art. 4 h), conflictos de tarifas y la CPe. En B2C el riesgo es mayor (Ley 24.240, art. 40) |
| **F5. Encaje con Facu** | **3** | El acceso y el conocimiento son altos (CEMEVA). Pero choca con dos preferencias que él expresó: no ir 100% por granos y buscar algo global de producto. Además, el conflicto de interés familiar |
| **Total** | **15/25** | |

**Recomendación: PENDIENTE.**

**Por qué (OPINIÓN):**
- Como **negocio principal**, no reúne lo que Facu pidió: no es global, es de margen fino (hacen falta más de 60-100 viajes por mes para que valga la pena) y está en el rubro que él no quiere como destino.
- Al mismo tiempo, **el experimento es de los más baratos de toda la lista** gracias a CEMEVA, y se puede hacer en cualquier momento.
- Por eso lo dejaría **como candidato a "experimento chico en paralelo"** (CLAUDE.md permite uno) cuando ya esté elegido el negocio principal. No lo pondría como primero.
- **Si Facu decide arrancar igual,** que sea con la variante A (corredor puro, sin tocar plata) y con las reglas de la sección 8.

---

## 8. Primer experimento concreto (para cuando Facu lo active)

**Qué:** "corredor transparente" de viajes de vuelta y viajes extra para fleteros de la red de CEMEVA. Comisión fija conocida por las dos partes. El dador le paga directo al transportista.

**Paso 0 (antes del día 1, obligatorio):**
- Hablar con su papá: ¿le sirve o le perjudica a CEMEVA? ¿Qué información de CEMEVA no se puede usar (tarifas, clientes)?
- Una consulta corta con el contador (¿monotributo? ¿cómo se factura la comisión?) y, si se puede, con un abogado (el texto de "conecto, no transporto").

**Con quién y cómo llegar:**
- **8 fleteros** que ya trabajan con CEMEVA. Facu los tiene en su app de seguimiento y en la planilla de cargas. Llamarlos o encontrarlos en la planta, sin pedirles nada al principio: solo preguntar.
- **4-5 dadores de la zona:** acopios vecinos, agronomías o distribuidores de fertilizantes, productores medianos. Llegar a ellos por contactos de CEMEVA o yendo en persona.
- **1-2 centros o cooperativas de transportistas de la zona:** para entender cómo reparten viajes y cuánto retienen. Son competencia o posibles aliados.

**Cronograma:**

| Días | Qué | Costo (ESTIMACIÓN) |
|---|---|---|
| 1-10 | 13-15 entrevistas (preguntas abajo). Anotar todo en una planilla | US$ 40-80 (nafta y cafés) |
| 11-14 | Si al menos 5 de los 8 fleteros dan ejemplos concretos de vueltas vacías: armar el grupo o lista de WhatsApp Business y la planilla de camiones y cargas, y pedirles cargas a los dadores | US$ 0-20 |
| 15-30 | Intentar cerrar viajes. Comisión fija acordada antes, cobrada al confirmar el viaje. Pago directo del dador al transportista. Seguir cada viaje y preguntar después si lo repetirían a través de Facu | US$ 20-50 + monotributo (≈ US$ 35/mes si no lo tiene) |

- **Costo total:** US$ 100-185 (ESTIMACIÓN).
- **Pérdida máxima:** **US$ 200 de plata + ~50 horas.**
- **Días:** 30.

**Números para decidir (definirlos con Facu antes de empezar):**
- **Seguir** si en 30 días se cumplen las tres cosas:
  - ≥ 5 de 8 fleteros cuentan **al menos 2 viajes vacíos o días parados en el último mes**, con fechas y lugares;
  - ≥ 3 viajes cerrados con comisión **cobrada** (≥ US$ 25 cada una);
  - ≥ 1 dador o fletero que **vuelve a pedir a través de Facu**.
- **Cortar** si pasa alguna de estas:
  - menos de 2 viajes cerrados;
  - nadie repite a través de Facu;
  - los dadores solo aceptan si Facu adelanta el pago al camionero;
  - CEMEVA se ve perjudicada.
- **Hallazgo valioso aunque se corte:** si los fleteros dicen que su dolor más grande es **cobrar** (y no conseguir carga), anotarlo como dato de esta idea. Puede reorientar todo hacia servirle al camionero. Se anota como dato de L6 y como referencia de LOG-1-2 (no como idea nueva, por la Regla N.º 2).
- **Al cierre:** post-mortem escrito (qué se aprendió del sector), aunque haya funcionado.

**5 preguntas al estilo The Mom Test** (libro de Rob Fitzpatrick: preguntar por hechos pasados y concretos, no por opiniones ni por "¿usarías...?"):
1. (Fletero) "Contame **la última vez** que volviste vacío: ¿cuándo fue, desde dónde, y qué hiciste para conseguir carga de vuelta?"
2. (Fletero) "¿De dónde salieron tus **últimos tres viajes** que no fueron de CEMEVA? ¿Quién te los pasó y **cuánto se quedó** esa persona?"
3. (Fletero) "¿Cuánto tardaste en **cobrar tu último viaje** y cómo te lo pagaron? ¿Tuviste que descontar algún cheque? ¿A qué costo?"
4. (Dador) "**La última vez que te faltó un camión**, ¿qué hiciste, a cuántos llamaste, cuánto tardaste y cuánto terminaste pagando?"
5. (Los dos) "¿Usaste alguna vez una app o un grupo para fletes (Avancargo, Humber, DeTransporte, grupos de WhatsApp)? **¿Por qué la seguís usando o por qué la dejaste?**"

---

## 9. Fuentes

Todas consultadas el **2026-10-15**. La fecha entre paréntesis es la de publicación según la fuente ("s/f" = sin fecha visible). "(resumen)" = lo tomé del resumen del buscador porque no pude leer la página o porque la página no mostraba ese dato.

**Normas (fuentes oficiales)**
- Boletín Oficial — Decreto 1109/2024 (2024-12-19): https://www.boletinoficial.gob.ar/detalleAviso/primera/318417/20241219
- argentina.gob.ar — Ley 24.653, texto actualizado: https://www.argentina.gob.ar/normativa/nacional/37871/actualizacion
- InfoLEG — Código Civil y Comercial de la Nación (arts. 1280-1287, 1309-1311, 1345-1353): https://servicios.infoleg.gob.ar/infolegInternet/anexos/235000-239999/235975/norma.htm
- ARCA — Categorías del monotributo, valores desde el 2026-08-01: https://www.afip.gob.ar/monotributo/categorias.asp

**Factura de Crédito Electrónica MiPyME**
- Contadores en Red — "FCE MiPyME: monto mínimo a partir de abril 2026" (2026-04-10): https://contadoresenred.com/factura-de-credito-electronica-mipyme-monto-minimo-a-partir-de-abril-2026/
- Blog del Contador — "El Gobierno prorroga hasta octubre de 2026 los plazos del régimen de FCE MiPyMEs" (Res. 219/2025; 2025-10-28): https://siap.blogdelcontador.com.ar/novedades/el-gobierno-prorroga-hasta-octubre-de-2026-los-plazos-del-regimen-de-factura-de-credito-electronica-mipymes/
- MAV — "Negociación Factura de Crédito Electrónica MiPyMEs" (s/f; resumen): https://www.mav-sa.com.ar/uploads/tx_sbdownloader/Negociacion_Factura_de_Credito_Electronica_MiPyMES.pdf

**Comisiones, tarifas y plata en el sector (Argentina)**
- LV16 Río Cuarto — "Tras el paro, camioneros denuncian 'comisiones oscuras' en los fletes" (2026-04-13): https://www.lv16.com.ar/sg/nota-213803/tras-el-paro-camioneros-denuncian-comisiones-oscuras-en-los-fletes
- Bichos de Campo — conflicto de tarifas y bloqueos en puertos bonaerenses (2026-04-10): https://bichosdecampo.com/conflicto-por-las-tarifas-de-fletes-sigue-el-bloqueo-de-transportistas-en-accesos-portuarios-bonaerenses-y-piden-garantizar-la-libre-circulacion/
- Bichos de Campo — "Se viene un paro: el transporte de cargas no quiere que lo sigan caminando" (2018-10-22): https://bichosdecampo.com/se-viene-un-paro-el-transporte-de-cargas-no-quiere-que-lo-sigan-caminando
- Bichos de Campo — sistema de alerta por desvíos entre tarifas pagadas y acordadas (2021-09-03): https://bichosdecampo.com/adelanto-el-ministerio-de-transporte-disenara-un-sistema-de-alerta-para-detectar-desvios-entre-las-tarifas-de-fletes-abonadas-y-acordadas
- Bichos de Campo — mesa contra el abuso de posición dominante en la contratación de fletes (2023-04-21): https://bichosdecampo.com/el-ministerio-de-transporte-creo-una-mesa-de-trabajo-para-erradicar-situaciones-de-abuso-de-posicion-dominante-en-la-contratacion-de-fletes
- Bichos de Campo / Valor Soja — "Sigue la batalla silenciosa de las aplicaciones digitales de logística" (2021-07-15): https://bichosdecampo.com/sigue-la-batalla-silenciosa-de-las-aplicaciones-digitales-de-logistica-para-cerrar-acuerdos-con-dadores-de-carga
- Estación Vial — "Las aplicaciones digitales se disputan la asistencia logística del transporte de cargas" (fecha no confirmada, ~2022): https://estacionvial.com.ar/nota/2590/las-aplicaciones-digitales-se-disputan-la-asistencia-logistica-del-transporte-de-cargas/
- La Nación — "En el polo agroexportador más moderno del mundo se viven imágenes inéditas por la sequía" (2023-05-08; resumen): https://www.lanacion.com.ar/economia/campo/en-el-polo-agroexportador-mas-moderno-del-mundo-se-viven-imagenes-ineditas-por-la-sequia-nid08052023/

**Plataformas B2B (Argentina y región)**
- Avancargo — sitio oficial (fuente de la empresa): https://www.avancargo.com/
- Prensa Mercosur — "Analógicos: casi el 87% del transporte de cargas en Argentina opera sin sistemas digitales" (2026-06-28; resumen, la página no cargó): https://prensamercosur.org/2026/06/28/analogicos-casi-el-87-del-transporte-de-cargas-en-argentina-opera-sin-sistemas-digitales/
- Descubre.vc — "Avancargo lanza primer Índice de Digitalización del Transporte de Cargas" (2025-11-29; resumen): https://www.descubre.vc/noticia/avancargo-lanza-primer-ndice-de-digitalizaci-n-del-transporte-de-cargas-2025-11-29
- Getlatka — Avancargo (s/f; estimación de terceros; resumen): https://www.getlatka.com/companies/avancargo
- Humber — sitio oficial: https://www.humber.com.ar/
- MuvinApp — sitio oficial: https://www.muvinapp.com/
- DeTransporte.com — sitio oficial: https://detransporte.com/
- Rutazo — página para transportistas (fees: resumen): https://www.rutazo.com/para-transportistas ; guía: https://www.rutazo.com/guia-transporte-carga
- Tracción Argentina — sitio oficial: https://traccionargentina.com/
- Carga GO — página para camioneros: https://cargago.com.ar/soluciones/camioneros/
- TCARGO — sitio oficial: https://tcargo.app/
- Kargho — dominio (hoy muestra "MatchFreight.AI"): https://www.kargho.com/
- Delpa Tecnología — "Plataforma de licitaciones de transporte y bolsa de carga" (2026-10-07): https://www.delpatecnologia.com/es/blog/licitaciones-transporte-bolsa-de-carga/

**Plataformas B2C (Argentina y región)**
- Punto a Punto Mendoza — "Cómo funciona Fletalo, la app de mudanzas BtoB" (2024-02-29): https://mendoza.puntoapunto.com.ar/como-funciona-fletalo-la-app-de-mudanzas-btob-que-ya-opera-en-argentina-y-suma-empleados/
- iProUP — "Fletalo planea facturar $450 M en 2024" (2024; solo el título): https://www.iproup.com/innovacion/47915-fletalo-startup-fletes-online-planea-facturar-450-m-en-2024
- Globalports — "Fletalo expuso su caso en la Universidad de San Andrés" (2023-04-12): https://www.globalports.com.ar/fletalo-la-startup-de-mudanzas-y-fletes-expuso-su-caso-en-la-universidad-de-san-andres/
- Fletalo — sitio oficial (no muestra contenido sin JavaScript): https://www.fletalo.com.ar/
- ADNSUR — "FletArg: la app que revoluciona la forma de conseguir fletes..." (2025-10-16): https://www.adnsur.com.ar/empresarias/fletarg--la-app-que-revoluciona-la-forma-de-conseguir-fletes--mudanzas--envios-de-materiales-y-auxilios-mecanicos-en-toda-la-argentina_a68f0df974e662ee67c3ccbdc
- Flets — sitio oficial: https://flets.com.ar/
- MiFlete — sitio oficial: https://miflete.ar/
- Weflet — sitio oficial (no cargó; resumen): https://weflet.com/
- Perfil — "En Argentina los fletes también tienen su propia aplicación" (Kargho, 2020-10-26): https://www.perfil.com/noticias/tecnologia/fletes-tambien-tienen-su-propia-aplicacion-argentina-app.phtml
- Derecho en Zapatillas — "Uber Flash y paquete perdido: quién responde y cómo reclamar" (2026): https://www.derechoenzapatillas.com/2026/uber-flash-y-paquete-perdido-quien-responde-y-como-reclamar/
- Mercado & Consumo — "Lalamove reduz comissão para corridas de moto de até 10 km" (2026-02-10): https://mercadoeconsumo.com.br/10/02/2026/logistica/lalamove-reduz-comissao-para-corridas-de-moto-de-ate-10-km/
- Mercado & Consumo — "Lalamove amplia operação no Brasil..." (2025-11-06): https://mercadoeconsumo.com.br/06/11/2025/logistica/lalamove-amplia-operacao-no-brasil-com-foco-em-personalizacao-e-novos-perfis-de-clientes/amp/

**Capital de trabajo y comisiones afuera**
- FreightWaves — "What Is Freight Broker Factoring? How It Works, Costs, & Types" (2026-02-17; con contenido promocional): https://www.freightwaves.com/checkpoint/freight-broker-factoring/
- otrucking — "Quickpay rates by broker" (s/f; fuente interesada; resumen): https://otrucking.com/resources/guides/quickpay-rates-by-broker/
- Canal Rural — "Frete: limitar margem do agenciador de carga pode ser solução" (s/f; error 403; resumen): https://www.canalrural.com.br/programas/direto-ao-ponto/frete-limitar-margem-do-agenciador-de-carga-pode-ser-solucao/

**Sindicato**
- iProfesional — Galperin y Moyano (2025; resumen): https://www.iprofesional.com/politica/434956-ceo-mercado-libre-marcos-galperin-cuestiono-a-moyano-por-uso-camiones-autonomos
- iProUP — "Apps de transporte de carga: qué son y cómo funcionan" (2020; resumen): https://www.iproup.com/innovacion/18656-apps-de-transporte-de-carga-que-son-y-como-funcionan

**Contexto interno (no son fuentes de mercado)**
- `research/fuentes/2026-10-08-L6-logistica.md` (informe anterior; sus fuentes no se repiten acá)
- `MEMORY.md` del proyecto (entradas del 2026-10-13 y 2026-10-14 sobre CEMEVA y las preferencias de Facu)
- `C:\FACU\CEMEVA\CONTEXT.md` (qué hace CEMEVA y su app; lectura sin cambios)

**Nota de método:**
- (1) Varias páginas muestran la fecha del día como si fuera la de la nota. Revisé la firma de cada nota: así detecté que la cita de "cheques a 60 días" es de **2018** y no actual.
- (2) Casi ninguna app publica su comisión. Los "0%" y "sin comisiones" son **lo que dicen las propias empresas.**
- (3) No pude abrir las fuentes primarias del IDT 2026, de Getlatka ni de los datos de Brasil (Aprosoja, CNTA). Están marcadas como resumen.
- (4) No verifiqué: tipo de cambio de octubre de 2026, tasas de descuento de e-cheq y factoring en Argentina, qué pasa con la FCE después del 2026-10-31, comisión de Fletalo, estado de Kargho y Circular, si la CPe tiene un rol para el intermediario del flete, ni los grupos de WhatsApp de transportistas.
