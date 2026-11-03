# L6 — "Uber de la logística empresarial": investigación de mercado

**Fecha:** 2026-10-08
**Idea (palabras de Facu):** "Aplicación o empresa intermediaria de logística: une en todo el país a personas que necesitan un transporte, por ejemplo para frutas, verduras y todo, con transportistas. Sería como un Uber, pero en logística empresarial."
**Método:** ~31 búsquedas web + ~20 lecturas directas de fuentes (notas, PDFs de la Bolsa de Comercio de Rosario y de la UNTREF, sitios de empresas). **El presupuesto de búsquedas se agotó antes de terminar**: quedaron huecos marcados como "no verificado" (ver sección 12).

**Convenciones (Regla N.º 1):**
- **DATO** = tiene fuente (URL) y fecha de publicación. Si la fuente es interesada (la propia empresa, un gremio, una nota de prensa sin datos duros), lo marco.
- **ESTIMACIÓN** = cálculo mío, con el razonamiento a la vista.
- **OPINIÓN** = mi juicio, marcado como tal.
- "No verificado" = no lo pude confirmar.

---

## 0. Resumen en 10 líneas

1. **El problema existe y es grande:** ~91% de la carga argentina va en camión (estimación de la BCR, 2018), el sector está muy atomizado (~2 camiones por empresa) y muy poco digitalizado (5% "digitalizado en serio", según un índice que armó Avancargo, que vende software: fuente interesada).
2. **La idea no es nueva, ni acá ni afuera.** En el mundo se gastaron miles de millones de dólares en "Uber de camiones". Los casos de fracaso o de retirada son muchos: Convoy (cerró en 2023 tras levantar más de US$ 900 M), Kobo360 (Nigeria, se fundió por capital de trabajo), Transfix (vendió su brokerage en 2024), BlackBuck (India, vendió su negocio de fletes "por pérdidas y capital de trabajo"), TruckPad (Brasil, vendida a cambio de asumir su deuda). Uber Freight sigue perdiendo plata en 2026.
3. **Los que sobreviven y ganan plata casi nunca viven del margen del flete:** cobran por **servicios al transportista** (pagos, peajes, software, crédito: BlackBuck, Frete.com) o están en **fletes chicos urbanos de alta frecuencia** (Porter, India).
4. **En Argentina ya hay jugadores:** Avancargo (desde ~2017, 125.000 camiones "fiscalizados" según su web, pasó de marketplace a software y control tower), apps de granos (Humber, MuvinApp, que compró la Bolsa de Comercio de Rosario, Circular), Kargho y Fletalo (fletes chicos y mudanzas). Además están los grupos de WhatsApp y los contactos de siempre (no pude medirlos).
5. **La trampa principal para Facu es el capital de trabajo:** si el intermediario le paga al camionero antes de cobrarle al cliente (que paga a 30-90 días), cada viaje inmoviliza cerca de US$ 1.400. Con US$ 1.300 de ahorros da para un solo viaje a la vez. Así se fundió Kobo360.
6. **El nicho de frutas y verduras es real pero desordenado:** el Mercado Central mueve ~1,4 M t/año, llegan miles de camiones por mes (8.000 según un dato de 2016) y el flete lo termina pagando el productor. Casi todo viaja en camión sin frío y muchos camiones vuelven vacíos. No encontré ninguna startup enfocada en este nicho, pero la búsqueda quedó corta.
7. **Puntaje global (detalle en sección 11):** problema 8, pago 5, competencia 4, ventaja de Facu 3, factibilidad 4, escalabilidad 6, riesgo 3.
8. **OPINIÓN — veredicto:** como **startup "Uber de cargas para todo el país"**, no: el formato ya se probó con muchísima más plata y no funcionó. Como **experimento chico de etapa 1** para aprender una industria desde adentro, sí, siempre que sea **sin capital de trabajo**: broker manual por WhatsApp, en **un solo corredor y una sola carga**, por ejemplo los viajes de retorno vacíos de camiones frutihortícolas. Tiene que tener fecha de corte y una pérdida máxima de US$ 200.

---

## 1. Parecidos en el mundo

### 1.1 Tabla comparativa

| Empresa (país) | Año | Plata levantada (DATO) | Modelo | Cómo cobra | Estado (2026-10) | Por qué |
|---|---|---|---|---|---|---|
| **Convoy** (EE.UU.) | 2015 | Más de US$ 900 M; valuación de US$ 3.800 M en 2022 | Broker digital que **toma el riesgo** (le compra el viaje al camionero y se lo vende al cliente) | Diferencia (spread) entre lo que cobra y lo que paga | **Cerró el 2023-10-19.** Flexport se quedó con la tecnología | Recesión del flete, se cortó el financiamiento, "crecer a cualquier costo", no tenía claro si era una empresa de tecnología o de logística, márgenes finos. Un análisis secundario (no verificado) habla de margen bruto ~7% en 2021 y pérdida operativa ~US$ 190 M |
| **Uber Freight** (EE.UU.) | 2017 (no re-verificado) | No verificado | Broker digital + software (TMS, tras comprar Transplace en 2021) | Spread + software | **Vivo, pierde plata.** 2T-2026: ingresos US$ 1.583 M (+25% interanual), pérdida operativa US$ 24 M (−1,5% de lo facturado) | Margen del brokerage muy fino. Desde 2021 solo tuvo algún trimestre en equilibrio |
| **Transfix** (EE.UU.) | 2013 | US$ 125 M; en 2022 se habló de salir a bolsa por US$ 1.100 M | Broker digital + software | Spread + software | **Vendió su brokerage a NFI (junio 2024)** y quedó solo como software | El CEO lo presentó como "estrategia": siendo broker no podía venderles su software a otros brokers. Pasó en plena caída del mercado de fletes |
| **Loadsmart** (EE.UU./Brasil) | No verificado | Ronda de US$ 200 M en 2022 con valuación de US$ 1.300 M (SoftBank LatAm, BlackRock) | Broker digital + software (TMS) | Spread + software | **No verificado** (no encontré noticias 2025-2026) | — |
| **Frete.com** (Brasil; holding de FreteBras + CargoX + FretePago) | FreteBras 2008, holding 2021 | Serie F de US$ 200 M (InfoMoney) o US$ 220 M (Exame) en 2021, liderada por SoftBank y Tencent; US$ 390 M en total; "unicornio" | **Bolsa de cargas por suscripción** + fintech (pagos, crédito) + software para transportistas | **Suscripción**: el camionero se registra gratis; pagan las transportadoras y los dadores de carga. Además anticipo de cobros | **Vivo.** Hay datos de una ronda en enero de 2026 (R$ 150 M liderada por XP según Preqin, o US$ 27,9 M de deuda según VCBacked): fuentes contradictorias, no verificado | CargoX empezó como "Uber de camiones" y **en la pandemia giró a dar tecnología a las transportadoras**. En 2021 anunció que se expandía a Argentina; no verifiqué si lo hizo |
| **TruckPad** (Brasil) | No verificado | Inversores: Movile, Mercedes-Benz, Plug and Play, Full Truck Alliance (China, 2019); montos no publicados | App que conecta camioneros con cargas | No verificado | **Comprada por JSL (grupo Simpar) en mayo de 2022, a cambio de asumir su deuda.** La meta era que generara caja recién a mediados de 2024. Estado actual: no verificado | Quemaba caja |
| **Nuvocargo** (México-EE.UU.) | 2019 | Serie A de US$ 12 M (2021), US$ 20,5 M (Tiger Global, valuación US$ 180 M), Serie B de US$ 36,5 M (junio 2023, valuación > US$ 250 M) | Forwarder digital + despachante de aduana en la frontera México-EE.UU. | No verificado | **Aparentemente vivo** (no encontré noticias de despidos, lo que no prueba nada) | Nicho especializado (cruce de frontera, aduana), no un marketplace general |
| **Lalamove** (Hong Kong/China/Asia/LatAm) | No verificado | Serie F de US$ 1.300 M (2021, Hillhouse) | Marketplace de **fletes chicos urbanos** (furgonetas, motos) | Empezó cobrando **membresías** a los choferes. Desde 2018 cobra **comisión**: en China, 14% para miembros que pagan 239 yuanes por mes y 18% para el resto | **Vivo.** Reportó ganancia ajustada de US$ 501 M en 2024 (Caixin, traducción automática). Los reguladores chinos la citaron varias veces por sus comisiones | Escala gigante en fletes urbanos. Según The Ken, en India estuvo entre los rivales de Porter que "cayeron" (sin detalle) |
| **Porter** (India) | 2014 | Serie F de US$ 200 M (mayo 2025) + ~US$ 100 M previos; valuación US$ 1.200 M | Agregador de **fletes urbanos** con mini camiones y motos (el 60% de los pedidos son en moto) | **Comisión de hasta 30%** sobre lo facturado, según la ciudad | **Vivo y rentable.** Año fiscal 2025: ingresos de ₹ 4.306 crore, ganancia neta de ₹ 55 crore, margen EBITDA de 1,94%. Año fiscal 2026: ganancia de ₹ 229 crore (Inc42) | Viajes urbanos de alta frecuencia (más de 500.000 pedidos por día), con prioridad en la ganancia desde 2023. Sus rivales (Dunzo, Swiggy Genie, Lalamove India) "cayeron" |
| **BlackBuck / Zinka** (India) | No verificado | Salió a bolsa en noviembre de 2024 (₹ 1.115 crore) | Empezó como marketplace de camiones completos. **Hoy:** servicios para el dueño del camión (pagos de peajes con FASTag y de combustible, telemática, crédito) + bolsa de cargas | Comisiones sobre pagos de peajes y combustible, suscripciones de telemática, comisiones por créditos. La bolsa de cargas está pasando a un modelo de broker con **6-8% por operación** | **Vivo.** En agosto de 2024 **vendió su negocio de fletes corporativos** (₹ 133 crore), que la calificadora ICRA describe como "con pérdidas e intensivo en capital de trabajo". Año fiscal 2025: ingresos de ₹ 427 crore, EBITDA ajustado de ₹ 139 crore, pérdida neta de ₹ 8,6 crore (gracias a un crédito fiscal) | **Ganó plata cuando dejó de vivir del flete** y empezó a venderle servicios al camionero |
| **Kobo360** (Nigeria y otros 6 países de África) | 2017 | Serie A de US$ 20 M (2019; Goldman Sachs, IFC, TLcom, Y Combinator) + US$ 10 M de deuda para capital de trabajo; Serie B de US$ 48 M (2021). El total es contradictorio: US$ 30 M o US$ 79 M según la fuente | "Uber de camiones" que **les pagaba a los camioneros por adelantado** y cobraba a las grandes empresas semanas o meses después | Spread | **Prácticamente cerrada desde diciembre de 2024.** Pasivos de más de ₦ 10.000 M (julio 2026) | **Trampa de capital de trabajo:** un banco le cortó la línea de crédito y no pudo pagarles a los camioneros. Además le costaba conseguir inversión |

### 1.2 Qué patrón sale de estos casos

- **DATO (márgenes de la industria, EE.UU.):** el margen bruto de los brokers de carga ronda el **12-16%** (datos de la cámara TIA: ~16% a mediados de 2023 y ~15% a principios de 2025; RXO, un broker que cotiza en bolsa: 14,7% en 2T-2024 y **11,9% en 4T-2025**). Y eso es *antes* de pagar sueldos, sistemas y los clientes que no pagan.
- **DATO:** los marketplaces "puros" de fletes chicos urbanos cobran comisiones más altas: **Porter hasta 30%; Lalamove 14-18% en China.**
- **OPINIÓN (resumen del patrón):**
  1. El broker digital que toma riesgo en camiones completos (Convoy, Transfix, Uber Freight, BlackBuck al principio, Kobo360) es un **negocio de margen fino que necesita mucho capital**. La tecnología no alcanzó para cambiar esa economía.
  2. Los que ganan plata **le venden al camionero** (pagos, software, crédito: BlackBuck, Frete.com) o hacen **fletes urbanos chicos de alta frecuencia** (Porter, Lalamove).
  3. **Sesgo a tener en cuenta:** casi todo lo que circula sobre estas empresas son notas de rondas de inversión o comunicados. Los cierres se cubren menos, y los marketplaces chicos que fracasaron sin haber levantado plata directamente no aparecen en ningún lado (sesgo de supervivencia en los dos sentidos).

---

## 2. Argentina: competidores y estructura del mercado

### 2.1 Competidores locales encontrados

| Nombre | Qué hace | Datos (fuente y fecha) | Estado |
|---|---|---|---|
| **Avancargo** | Nació como "Uber de camiones" B2B (incubada por NXTP Labs, programa AgTech 2017). **Hoy** su web ofrece: TMS en la nube, "Control Tower 4PL", 3PL a demanda (su red de camiones), app de tareas de campo y consultoría | Forbes Argentina, 2023-02-09: **ingresos de US$ 5 M en 2022, meta de US$ 20 M para 2023**, 20.000 transportistas, 1.500 dadores, 30.000 viajes, 30 empleados, Chile y Uruguay. Rondas: friends & family de US$ 300.000; semilla de US$ 1 M en 2019 (Globant, Supervielle, Grupo Murchison, Puerto Asís, Win Win VC); aceleración de BID Lab en 2020. Un estudio de abogados (sin fecha visible) informa una **"quinta ronda" de US$ 500.000**. iProUP (2024-08-01, según el resumen del buscador) habla de US$ 600.000 en diciembre de 2023. Su web (consultada el 2026-10-08) dice: **más de 125.000 camiones fiscalizados y más de 2.000 dadores**; clientes como Rio Tinto, Mercado Libre, Syngenta y Bayer | **Vivo, pero con giro de modelo.** Descubre.vc la sigue mostrando en etapa "Seed". Su CEO describió 2025 como un año "de grandes cambios en el negocio" (repost en LinkedIn: fuente secundaria). **No encontré cuánto facturó realmente en 2023** ni si los "US$ 5 M" eran ingresos propios o el valor total de los fletes movidos |
| **Humber** | App de fletes de granos (la primera, de 2016) | Bichos de Campo / Valor Soja, 2021-06-21 | Estado actual: no verificado |
| **MuvinApp** | App de fletes de granos; fundada por un ex gerente de logística de Cargill | **La compró la Bolsa de Comercio de Rosario.** Acuerdos con Bunge y otros (2021-06-21) | No verificado |
| **Circular** | Logística y turnos de descarga de granos | Acuerdo con Louis Dreyfus (2021-06-21) | No verificado |
| **Kargho / Khargo** | Plataforma de fletes | Los Andes, 2020-11-26: fundada en 2018, inversión inicial de US$ 150.000, **le cobra un honorario al transportista calculado por algoritmo (no un %)**, facturación proyectada de US$ 1,5 M | No verificado |
| **Fletalo** | "Uber de mudanzas y fletes" (fletes chicos), con línea B2B desde febrero de 2023 | Forbes Argentina, 2023-02-16: fundada en 2020, más de 1.000 fleteros. Descubre (junio 2024): **meta de facturar US$ 450.000 en 2024**, Endeavor HIT 2024, AMBA, Rosario y Córdoba | Su sitio fletalo.com.ar responde ("Fletes y repartos"). **No encontré su comisión** |
| **FletArg** | App (App Store): fletes, mudanzas, auxilio, maquinaria | Sin fecha visible | No verificado |
| **Frete.com (Brasil)** | Anunció en 2021 su expansión a Argentina | InfoMoney / Exame, 2021 | **No verifiqué si llegó a operar en Argentina** |
| **Grupos de WhatsApp/Facebook de transportistas, bolsas de carga informales, contactos de siempre** | El "competidor" real | — | **No verificado** (se me acabaron las búsquedas). **Hay que relevarlo en campo:** es probablemente la competencia más dura |

**OPINIÓN:** Avancargo es la señal más importante. Es un equipo con años en el rubro, inversores de primer nivel locales y acceso a grandes dadores de carga, y aun así pasó de "marketplace" a "software + control tower + servicios". Además, lo que levantó en total parece estar en el orden de **pocos millones de dólares** (sumando las rondas que encontré: ~US$ 2-2,5 M, ESTIMACIÓN que puede tener rondas repetidas o faltantes). Comparado con los US$ 900 M de Convoy, eso dice algo sobre **cuánto capital de riesgo hay para esto en Argentina**.

### 2.2 Estructura del mercado de cargas

| Indicador | Valor | Fuente / comentario |
|---|---|---|
| Carga total y reparto por medio de transporte | **~450 M t/año: 91% camión, 4,2% tren, 4,8% hidrovía** | BCR, Informativo Semanal, 2018-04-20 (Calzada y Sesé). Es una estimación de la propia BCR. Otras fuentes dan 90-93% para el camión. En granos el camión pesa menos (~77-83%) |
| Toneladas por camión (2014) | ~409 M t; granos ~137 M t, minería ~120 M t | Instituto Argentino del Transporte (PFETRA 2015), citado por la BCR (2018) |
| Cantidad de camiones | **No hay una cifra oficial única:** ~330.000 camiones y tractores registrados (dato CATAMP/RUTA 2023, citado en un paper académico); "~700.000 circulando" (Forbes 2019, citando a Avancargo); ~350.000 unidades de ~150.000 empresas (Jatib et al., UNTREF, 2019) | Las cifras se contradicen. La de 700.000 viene de una fuente interesada |
| Atomización | **~2 unidades por empresa; solo 51 empresas tienen más de 100 unidades** | Jatib et al., UNTREF, julio 2019 |
| Viajes y viajes vacíos | "50.000 viajes diarios, **30% ociosos (vacíos)**; 15 M de fletes por año, 5 M del agro; viaje promedio de 450 km" | Forbes Argentina, 2019-03-01, **citando a Avancargo (fuente interesada, sin metodología publicada)**. No lo pude verificar con una fuente independiente |
| Digitalización (¿"5%"?) | **Verificado, con matices:** es el Índice de Digitalización del Transporte (IDT) que armó **Avancargo** encuestando a 335 transportistas con 4.998 camiones. Promedio de 2,44 sobre 5. **Solo el 5% tiene una digitalización "significativa" (TMS/ERP integrados)**; el 73% está en los niveles 1-2. El 61% manda la documentación por WhatsApp, el 41% sigue sus cobros "en forma analógica", el 46% calcula costos con los índices de FADEEAC/CATAC | Forbes Argentina, 2023-04-12. **Sesgo:** lo midió una empresa que vende digitalización, con una muestra que no es aleatoria |
| Costos del sector (FADEEAC) | Índice de Costos de Transporte: **+2,55% en septiembre de 2026; +30,3% en 9 meses; +41% interanual.** Marzo de 2026: +10,15% (combustible +24,7%) | Agrofy, 2026-10-06 (una sola fuente; no vi el comunicado original de FADEEAC) |
| Tarifas de referencia | Ya **no son oficiales** (el Estado dejó de avalarlas). Fetra, tarifa orientativa para granos a 400 km: **$ 64.804/t (feb-2026, ≈ US$ 45,6/t) y $ 73.332/t (abr-2026, ≈ US$ 53,7/t)**. En la provincia de Buenos Aires no hubo acuerdo entre transportistas y productores (abril 2026) | Bichos de Campo, 2026-02-13 y 2026-04-07 |
| Plazos de pago | En San Juan, el cobro "habitual a 30 días" se estiró a **60-90 días** según la cámara local de propietarios de camiones | Diario de Cuyo, 2023-06-10. **No encontré datos nacionales 2025-2026** |
| Regulación | Ley 24.653 (1996): cualquiera puede prestar transporte de cargas ajustándose a la ley; **seguro sobre la carga obligatorio (art. 10)**. El Decreto 832/2024 hizo gratuito el registro RUTA y el Decreto 1109/2024 lo **eliminó** (según una resolución posterior en el Boletín Oficial); una nota de 2026 lo sigue describiendo como obligatorio: **verificar** | Boletín Oficial / Microjuris 2024-12-19 / Contadores en Red |
| Carta de porte electrónica | **Obligatoria para granos** (RGC 5017/2021; cambios por la RGC 5821/2026 del 2026-02-10) y para derivados granarios (RGC 5235/2022). **Para carga general no pude verificar que sea obligatoria** | Bichos de Campo, Aduana News, Blog del Contador |
| Frutas y verduras: documento propio | **DTV-e (Documento de Tránsito Vegetal electrónico)**, RG conjunta AFIP-SENASA 4297 (2018-08-24): es el único documento válido para el tránsito de productos vegetales alcanzados (cítricos, peras, manzanas, uvas, papa, ajo, pimiento, etc.; la lista vigente hay que confirmarla) | argentina.gob.ar; jorgevega.com.ar |
| Sindicato de Camioneros | **No verificado en esta investigación** (no llegué a buscarlo). Es un actor de peso conocido en el sector. Antes de operar hay que entender qué pasa si un intermediario coordina choferes en relación de dependencia de terceros, o choferes monotributistas | Pendiente |

---

## 3. El nicho de frutas y verduras

### 3.1 Datos

- **Mercado Central de Buenos Aires (DATO):** más de 500 mayoristas en 18 pabellones comercializan **~1,4 M t por año** de frutas y hortalizas. Abastece a más de 12 M de personas por mes (página de la Corporación en buenosaires.gob.ar, sin fecha visible). En 2018 fueron **1,36 M t: ~500.000 t de fruta y ~860.000 t de hortalizas** (Diario de Cuyo, 2020-07, con datos del propio Mercado).
- **Camiones (DATO viejo):** "ingresan mensualmente **8.000 camiones** desde las zonas de producción de todas las provincias" (Letra P, 2016-07-05). **ESTIMACIÓN:** son ~265 por día calendario. No encontré un dato más reciente.
- **Procedencia (2018):** hortalizas de Buenos Aires 54%, Mendoza 11%, Salta 8%; frutas de Entre Ríos 33%, Río Negro 22%, Mendoza 6%. Por volumen, la papa es el 39%, el tomate 14% y la cebolla 12%.
- **Horario:** desde 2019 la operación mayorista es de lunes a jueves de 2 a 10 h, y el viernes de 2 a 14 h (Bichos de Campo). Eso define cuándo llegan y se van los camiones.
- **Quién paga y quién decide el flete (DATO de práctica, no una norma):** en el esquema de consignación, el consignatario recibe la mercadería, la vende, se queda con una comisión del **10-12%** y **le descuenta al productor el flete y la descarga**. En la práctica, **el flete lo paga el productor** aunque lo adelante otro. Los productores chicos usan **"fleteros comisionistas"** que cobran un fijo por bulto más un porcentaje de la venta (este último dato viene de un medio uruguayo, así que puede no aplicar igual en Argentina). No encontré una norma del Mercado Central que regule quién paga el flete.
- **Frío:** el estudio de Jatib et al. (UNTREF, julio 2019) sobre el Mercado 3 de Febrero, citando una encuesta de la FAO de 2010 a referentes de 8.000 establecimientos en 16 provincias, dice: **"la totalidad se hace en camiones no refrigerados"**; solo el 5% se carga en forma mecánica; el **45% informa daños en el producto durante el transporte**; el 40% de los productos recorre más de 200 km. **Ojo: es un dato de 2010, viejo.** No encontré un dato actual sobre el porcentaje de transporte refrigerado.
- **Viaje de retorno vacío:** en 2020, el área frutihortícola del Instituto Argentino de la Pyme señaló que el camión que trae fruta del interior "regresa vacío" y que ese costo lo absorbe el productor (Diario de Cuyo, abril 2020, en contexto de pandemia).
- **Peso del flete en el precio:** FADEEAC afirmó que llevar manzanas de Cipolletti a Buenos Aires representa el **4%** del precio en el Mercado Central (nota sin fecha clara; **FADEEAC es una fuente interesada**: representa a los transportistas y busca mostrar que el flete no encarece los alimentos).
- **Cumplimiento documental:** una disposición conjunta de 2025 de SENASA, según un blog del agro, dice que ~35% del mercado de cítricos emite el DTV-e pero no cierra el circuito. Es una señal de informalidad y de procesos a medias.

### 3.2 ¿Hay espacio para una solución de nicho?

- **DATO:** no encontré ninguna startup argentina dedicada a la logística frutihortícola. **Pero la búsqueda específica no llegó a hacerse** (se cortó el presupuesto). Hay que verificarlo antes de concluir que el espacio está libre.
- **OPINIÓN, con razonamiento:**
  - **A favor:** hay un **punto físico de concentración** (el Mercado Central, y los mercados del interior como Mendoza, Córdoba o Rosario, que no investigué), un horario fijo, cargas repetitivas por temporada y un **problema concreto de retorno vacío**. Eso permite empezar chico y medible: un corredor, un producto, un horario.
  - **En contra:** es un mundo **muy relacional e informal** (consignatarios, fleteros de confianza, pagos en efectivo). El margen es bajo (la papa, el producto más voluminoso, es de bajo valor por kilo). El flete pesa poco en el precio final (el 4% de FADEEAC, si fuera cierto, da poco margen para cobrar de más). Y el **frío** necesita camiones caros, lo que choca de frente con el modelo "sin activos".
  - **Hipótesis a validar (no es un dato):** el ángulo con más chances no es "conseguirle camión al productor" (ya lo tiene, por relaciones de años), sino **llenar el viaje de vuelta** (insumos, envases, cajones, fertilizantes o carga general hacia zonas productoras) o **consolidar cargas de productores chicos** que no llenan un camión.

---

## 4. Por qué fracasan estos marketplaces

| Mecanismo | Evidencia | Qué implica para Facu |
|---|---|---|
| **Huevo y gallina (liquidez local)** | Cada corredor es un mercado aparte: tener camiones en Mendoza no sirve para una carga en Salta. Por eso Porter y Lalamove ganan en ciudades (alta densidad) y los marketplaces de camiones completos de larga distancia sufren (OPINIÓN, basada en los casos de la sección 1) | Empezar en **un solo corredor** y no en "todo el país" |
| **Desintermediación** (cliente y camionero se pasan el WhatsApp) | Hay estudios en otros marketplaces: introducir comisiones a los choferes **subió las transacciones por fuera de la plataforma ~4 puntos porcentuales** (paper de la PKU sobre un servicio de reparto). Cuanto mayor es la confianza entre las partes, más se saltean la plataforma (Management Science, mercado de freelancers). **No encontré un estudio empírico específico de fletes** | En cargas repetitivas (mismo productor y mismo camionero cada semana), la comisión desaparece después del 2.º viaje. **Hay que cobrar por algo que el camionero o el dador no consiguen solos:** cobro garantizado, viaje de vuelta, documentación, seguro |
| **Margen fino** | Brokers de EE.UU.: margen bruto de 12-16% y bajando (TIA, RXO); Uber Freight con pérdida operativa del −1,5% de lo facturado en 2T-2026; Convoy con un margen bruto estimado de ~7% en 2021 (fuente secundaria) | Con un ticket de ~US$ 1.500 (ver sección 5), cada viaje deja entre US$ 75 y US$ 225. Hacen falta **muchos viajes** para que sea negocio |
| **Capital de trabajo** | Kobo360 les pagaba por adelantado a los camioneros y cobraba semanas o meses después; **un banco le cortó la línea de crédito y quebró**. BlackBuck vendió su negocio de fletes por ser "intensivo en capital de trabajo" (ICRA). En Argentina se reportan cobros a 60-90 días (San Juan, 2023) | **Es el riesgo n.º 1 para Facu.** Ver el cálculo en la sección 5.3 |
| **Ciclos del mercado de fletes** | Convoy cerró en una "recesión del flete" (2022-2023). En 4T-2025, RXO reportó la ganancia por carga de diciembre ~30% por debajo de su promedio de 5 años | En Argentina se suman la inflación de costos (+41% interanual según FADEEAC, septiembre 2026) y las tarifas en pesos que hay que actualizar todo el tiempo |
| **Confusión de identidad (¿tecnología o logística?)** | Convoy (KUOW, 2023-10-26) y Transfix (vendió el brokerage para quedarse con el software) | Definir desde el día 1 qué es el negocio: **¿servicio (broker) o software?** Los resultados son muy distintos |

---

## 5. Modelo de negocio y números (todo ESTIMACIÓN salvo que diga DATO)

### 5.1 Ticket promedio de un flete

- **DATO de base:** tarifa orientativa de Fetra para granos a 400 km, abril 2026: **$ 73.332/t ≈ US$ 53,7/t**.
- **ESTIMACIÓN:** un semirremolque de granos lleva unas 28 t (supuesto mío; no lo verifiqué en esta búsqueda). Entonces **un viaje de 400 km ≈ US$ 1.500** (28 × 53,7). Para fletes frutihortícolas la carga se mide por volumen y bultos, no solo por peso, y no encontré tarifas: **el ticket real hay que relevarlo en campo**. Uso US$ 1.500 como orden de magnitud para un viaje de media distancia.

### 5.2 Comisión y viajes necesarios

Referencias (DATOS): margen de brokers en EE.UU. 12-16%; BlackBuck pasando a 6-8%; Lalamove 14-18%; Porter hasta 30% (urbano); consignatarios del Mercado Central 10-12% sobre la venta (otro negocio, pero sirve de referencia de lo que el sector tolera).

**ESTIMACIÓN.** Viajes por mes necesarios para lograr un margen bruto dado, con un ticket de US$ 1.500:

| Comisión | Margen por viaje | US$ 1.000/mes | US$ 5.000/mes | US$ 20.000/mes |
|---|---|---|---|---|
| 5% (marketplace puro: solo conecta) | US$ 75 | ~13 viajes | ~67 viajes | ~267 viajes |
| 10% (broker liviano: conecta + gestiona) | US$ 150 | ~7 viajes | ~33 viajes | ~133 viajes |
| 15% (broker con riesgo: paga y cobra) | US$ 225 | ~5 viajes | ~22 viajes | ~89 viajes |

- Es **margen bruto**: no descuenta sueldos, teléfono, seguros, clientes que no pagan ni el tiempo de Facu.
- **Para "facturar US$ 1 M al año" midiendo el valor de los fletes** hacen falta ~667 viajes por año (~55 por mes). Con 10% de comisión, eso deja ~US$ 100.000 de margen bruto anual. Para ponerlo en escala: Avancargo apuntaba a US$ 20 M (2023), con una red de 20.000 transportistas y un equipo de 30 personas.
- **OPINIÓN:** con un 5% como marketplace puro, la desintermediación hace muy difícil sostener la comisión en cargas repetitivas. Para cobrar 10-15% hay que **agregar valor real** (garantía de cobro, viaje de vuelta, documentación, seguro, seguimiento), y eso en general requiere capital o mucho trabajo manual.

### 5.3 La trampa del capital de trabajo (ESTIMACIÓN)

Supuestos: ticket de US$ 1.500; al camionero se le paga US$ 1.350 a los 7 días; el cliente paga a los 60 días.
- Cada viaje deja **US$ 1.350 inmovilizados durante ~53 días**.
- Con 20 viajes por mes, el capital que queda atado en la calle es de **~US$ 47.700** (20 × 1.350 × 53/30).
- **Con los US$ 1.300 de Facu: un solo viaje a la vez.** Un cliente que pague tarde o no pague se come todo el ahorro.
- **Conclusión:** el modelo inicial **no puede ser "broker que paga primero"**. Las alternativas son:
  - **(a)** el dador le paga directo al camionero y Facu cobra una comisión fija aparte, cobrada al momento;
  - **(b)** cobro por adelantado al dador (difícil con empresas grandes, más viable con productores chicos);
  - **(c)** financiar con terceros (Factura de Crédito Electrónica MiPyME, que obliga a aceptar o rechazar en 21 días desde abril de 2023, o descuento de e-cheqs), lo que **tiene un costo y achica el margen**.

---

## 6. Versión chica para empezar (con poco capital)

**OPINIÓN / propuesta (para validar, no es un plan probado):**

1. **Un solo nicho y un solo corredor.** Ejemplos posibles (hay que elegir con datos de campo, no por gusto):
   - **Retorno desde el Mercado Central hacia una zona productora** (Mendoza, Alto Valle de Río Negro, Entre Ríos). Hay camiones que llegan llenos y vuelven vacíos: el valor es **conseguirles carga de vuelta**.
   - **Consolidación de cargas de productores chicos** del cinturón hortícola que no llenan un camión (carga fraccionada).
2. **Versión manual primero (broker "concierge"):** un número de WhatsApp Business, una planilla (Google Sheets) con el registro de camiones (patente, seguro, documentación, ruta habitual, días) y de cargas, y un formulario simple. **Nada de app.**
3. **Sin capital de trabajo:** el dador le paga directo al camionero. Facu cobra un fee fijo o un porcentaje, facturado como monotributista, idealmente **al camionero que consigue el viaje de vuelta** (es el que gana algo que antes no tenía).
4. **Qué aporta un ingeniero industrial (lo concreto):**
   - **Modelo de costos por viaje** con la estructura del índice FADEEAC/CATAC (combustible, peajes, neumáticos, amortización, chofer) para cotizar bien y explicarle al dador por qué el precio es justo.
   - **Emparejar viajes de ida y vuelta** (backhaul) y **consolidar cargas** (llenar camiones a medias): es un problema de programación y ruteo, justo su terreno.
   - **Estandarizar procesos:** un checklist de documentación por viaje (DTV-e, seguro de carga, VTV, habilitaciones), con tiempos y KPIs (tiempo para conseguir camión, % de viajes cumplidos a horario, % de viajes de vuelta llenos).
   - Lo que releve en la pasantía de Sporting le sirve como experiencia de relevamiento de procesos logísticos (OPINIÓN: no reemplaza tener contactos en el sector).

---

## 7. MVP: qué haría falta (ESTIMACIONES)

| Fase | Qué es | Equipo | Costo | Tiempo | ¿Factible para Facu? |
|---|---|---|---|---|---|
| **0. Concierge** | WhatsApp Business + Google Sheets + formulario + landing page de 1 página | Facu solo (+ Claude para armar planillas y mensajes) | US$ 0-50 (dominio, WhatsApp gratis) | 1 semana | **Sí** |
| **1. No-code** | App web simple (por ejemplo Glide, Softr o Bubble) con alta de camiones y cargas, avisos por WhatsApp/email y panel de viajes | Facu + 1 amigo programador a tiempo parcial | US$ 30-150/mes en herramientas | 4-8 semanas | **Sí, si la fase 0 dio señales** |
| **2. App propia** | Matching automático, seguimiento GPS (o integración con el GPS de los camiones), validación de documentos, pagos y facturación | 2 desarrolladores + 1 persona de operaciones | Muy variable: de US$ 15.000 a US$ 50.000 si se paga a mercado (ESTIMACIÓN muy gruesa; con amigos a cambio de acciones puede ser menos plata pero más riesgo de que se abandone) | 3-6 meses | **No con US$ 1.300.** Solo con inversión o ingresos previos |

**OPINIÓN:** el cuello de botella de este negocio **no es la app, es la operación y la confianza** (quién responde si se pierde la carga, quién cobra, quién atiende a las 3 de la mañana en el Mercado Central). Avancargo tiene tecnología y aun así suma servicios operativos ("control tower"). Construir la app antes de tener 20-30 viajes manuales cerrados sería empezar por el final.

---

## 8. Riesgos

| Riesgo | Detalle | Severidad (OPINIÓN) |
|---|---|---|
| **Responsabilidad por la carga** | Ley 24.653, art. 10: el seguro sobre la carga es obligatorio. La justicia condenó a un transportista por no haberlo contratado (Cám. Nac. Comercial, Sala C, diciembre 2020, informado por Marval). Un fallo federal de 1997 extendió la condena al **transportista "contractual" que subcontrató el viaje**. **Si Facu "vende el viaje" a su nombre y lo subcontrata, puede responder por la carga.** No encontré una norma argentina específica sobre el comisionista o agente de cargas: **consultar a un abogado antes del primer viaje** | Alta |
| **Capital de trabajo / clientes que no pagan** | Ver sección 5.3 y el caso Kobo360 | Alta |
| **Desintermediación** | Ver sección 4 | Alta |
| **Laboral** | Si la plataforma organiza y controla a los choferes, podría haber reclamos de relación de dependencia. **No verifiqué jurisprudencia argentina sobre esto en plataformas de cargas.** Falta investigar la posición del sindicato de Camioneros | Media (no verificada) |
| **Regulatorio y documental** | DTV-e para vegetales, carta de porte electrónica para granos, seguros obligatorios, RUTA (eliminado o en duda: verificar). El cumplimiento es irregular en el sector (el dato de cítricos de 2025) | Media |
| **Macro / precios** | Costos +41% interanual (FADEEAC, septiembre 2026); tarifas en pesos que se desactualizan; conflictos por tarifas (Buenos Aires, abril 2026) | Media |
| **Competencia** | Avancargo y las apps de granos en carga general y agro; Fletalo en fletes chicos; las redes informales en todos lados | Media-Alta |
| **Seguridad / robos** | Hay fallos por robo de carga en ruta en los dos sentidos (en 2012 el robo no se consideró caso fortuito; un fallo de 2026, según un blog, liberó al transportista porque había tomado medidas de seguridad) | Media |

---

## 9. Cómo validar en 2-4 semanas con menos de US$ 200

**Objetivo:** responder con evidencia tres preguntas: **(1)** ¿hay viajes de retorno vacíos o cargas sin resolver en un corredor concreto?, **(2)** ¿alguien paga por resolverlo, y cuánto?, **(3)** ¿se saltean al intermediario después del primer viaje?

| Semana | Qué hacer | Costo | Métrica |
|---|---|---|---|
| **1** | **15-20 entrevistas en campo:** 6-8 camioneros (playa de camiones del Mercado Central en el horario de 2 a 10 h; estaciones de servicio de ruta), 5-6 productores o consignatarios, 3-4 dadores de carga pyme. Preguntas: ¿cómo consiguen camión o carga hoy?, ¿cuánto pagan?, ¿cada cuánto vuelven vacíos?, ¿a cuántos días cobran?, ¿qué les haría cambiar? **Relevar además los grupos de WhatsApp o Facebook que usan** | US$ 30-60 (viajes y café) | N.º de camioneros que declaran retorno vacío; ticket real de un viaje; plazo de cobro real |
| **2** | Elegir **un corredor** y armar la versión concierge: WhatsApp Business, planilla y landing de una página ("Te conseguimos carga de vuelta Buenos Aires → [zona]"). Ofrecerlo en los canales relevados | US$ 20-80 (dominio + algo de publicidad local, opcional) | N.º de camioneros registrados; N.º de cargas ofrecidas |
| **3-4** | **Intermediar 3-5 viajes reales**, con el pago directo dador → camionero y un fee de Facu acordado de antemano. Hacer seguimiento de cada viaje y preguntar después si lo repetirían a través de Facu | US$ 0-50 | N.º de viajes cerrados; fee cobrado; tiempo para conseguir el match; ¿volvieron a pedir a través de Facu o se contactaron directo? |

**Criterios de corte (propuestos, a acordar con Facu ANTES de empezar):**
- **Seguir** si en 4 semanas: ≥10 pedidos reales (cargas o camiones con necesidad concreta), ≥3 viajes cerrados con fee cobrado, y al menos 1 cliente que repite a través de Facu.
- **Cortar** si: menos de 3 viajes cerrados, o si todos los que cerraron después se arreglan directo. En ese caso igual se escribe el post-mortem: qué aprendió del sector.
- **Pérdida máxima:** US$ 200 de plata + ~40-60 horas de trabajo.

**Aviso legal mínimo antes del primer viaje (OPINIÓN):** dejar por escrito (con un mensaje de WhatsApp alcanza para arrancar, pero mejor un texto revisado por un abogado) que Facu **conecta y coordina** pero **no es el transportista**, y que el seguro de la carga lo tiene el camionero o el dador. Verificar la póliza de cada camionero.

---

## 10. Lo que NO se pudo verificar (pendientes)

1. Postura y peso real del **sindicato de Camioneros** frente a intermediarios y plataformas.
2. **Grupos de WhatsApp/Facebook y bolsas de carga informales**: cuántos hay, cómo funcionan, si cobran.
3. **Startups argentinas o latinoamericanas específicas de logística frutihortícola** (la búsqueda no llegó a hacerse).
4. Estado actual de **Humber, MuvinApp, Circular, Kargho, Loadsmart y TruckPad**; si **Frete.com** opera en Argentina.
5. **Comisión de Fletalo** y facturación real de **Avancargo** en 2023-2025.
6. **Porcentaje actual de transporte refrigerado** en frutas y verduras (el único dato es de la FAO, de 2010).
7. Si la **carta de porte electrónica** es obligatoria para carga general (más allá de granos).
8. **Vigencia del RUTA** después del Decreto 1109/2024.
9. **Mercados concentradores del interior** (Mendoza, Córdoba, Rosario, Tucumán): volúmenes y logística.
10. Año de fundación y fondos de **Uber Freight**, y monto de la compra de Transplace.

---

## 11. Veredicto

| Criterio | Puntaje (1-10) | Justificación en una línea |
|---|---|---|
| **Tamaño del problema** | **8** | El 91% de la carga va en camión (BCR 2018), sector atomizado, poco digitalizado y con viajes vacíos (dato de fuente interesada). |
| **Disposición a pagar** | **5** | El flete se paga siempre, pero el sector es sensible al precio y los márgenes de intermediación son finos (12-16% en EE.UU.); no hay evidencia local de que paguen por *conseguir* camión o carga. |
| **Espacio frente a la competencia** | **4** | En carga general y agro ya hay jugadores (Avancargo, apps de granos, redes informales); el nicho frutihortícola puede estar más libre, pero no lo verifiqué. |
| **Ventaja de Facu** | **3** | Método de ingeniero industrial y una pasantía de relevamiento logístico, pero sin red en transporte ni en el Mercado Central, sin capital y sin saber programar. |
| **Factibilidad con sus recursos** | **4** | El concierge manual sin capital de trabajo es factible ya; la app nacional y el broker que paga primero, no. |
| **Escalabilidad** | **6** | En teoría escala (es un marketplace), pero la evidencia mundial muestra que escala mal en camiones de larga distancia y bien en fletes urbanos o en servicios al camionero. |
| **Riesgo (10 = bajo)** | **3** | Capital de trabajo, responsabilidad por la carga, desintermediación, inflación de costos e informalidad. |

### Opinión (marcada como OPINIÓN)

**¿Vale la pena?** **Como está planteada ("Uber de la logística empresarial en todo el país"), no.** No es un problema de ambición sino de evidencia:
- Ese formato exacto lo probaron empresas con **cientos de millones de dólares**, equipos de primer nivel y mercados más grandes. La mayoría cerró, vendió su brokerage o tuvo que girar.
- En Argentina, el jugador más parecido (Avancargo) tiene años de ventaja y **se movió hacia software y servicios operativos**.
- Ser primero acá no es posible: ya hay varios desde 2016-2018.

**Pero hay dos ángulos que sí tienen sentido:**

1. **Etapa 1 (ahora), como experimento de aprendizaje barato:** un broker concierge manual en **un corredor frutihortícola, centrado en el viaje de vuelta vacío o en consolidar cargas de productores chicos**, siempre **sin poner capital de trabajo**, con 4 semanas, US$ 200 de tope y criterios de corte definidos. Aunque falle, Facu sale con lo más valioso para la etapa 2: **conocer de adentro un sector enorme, informal y poco digitalizado**, y una red de camioneros y productores.
2. **Etapa 2 (después), si en el campo aparece un dolor repetido:** la evidencia mundial dice que la plata está **del lado del camionero chico** (cobrar más rápido, gestionar documentos, pagar peajes o combustible, crédito, software simple por WhatsApp). Los datos del índice de Avancargo apuntan en esa dirección (61% manda los documentos por WhatsApp, 41% sigue sus cobros "en forma analógica"), aunque la fuente sea interesada. Ese podría ser el "algo grande", pero **es una hipótesis**: hay que verificarla en las entrevistas de la semana 1, no darla por cierta.

**Lo que no haría:** construir una app antes de cerrar viajes a mano, pagarles a los camioneros antes de cobrar, o salir a "todo el país" desde el día 1.

---

## 12. Fuentes

Fechas de publicación según cada fuente. "s/f" = sin fecha visible. Consultadas el 2026-10-08.

**Casos internacionales**
- CNBC — "Bezos-backed freight firm Convoy shuts down" (2023-10-19): https://www.cnbc.com/2023/10/19/bezos-backed-freight-firm-convoy-shuts-down-read-ceo-memo-here.html (no se pudo leer completa, error 403; datos a partir del resumen del buscador)
- KUOW — "Convoy promised to revolutionize freight — then it collapsed" (2023-10-26): https://www.kuow.org/stories/this-darling-of-seattle-s-startup-scene-promised-to-change-freight-what-happened
- SupplyChain247 — "Once worth $3.8B, Convoy's future now in doubt" (2023): https://www.supplychain247.com/article/once_worth_3.8b_convoys_future_now_in_doubt/Convoy
- Sacra — "Convoy unfinanceable in freight slump" (s/f; fuente secundaria del margen de ~7%): https://sacra.com/chat/h/83ff7935-458e-448b-beb4-11466c938a3b/
- TTNews — "Convoy shuts down after failing to find buyer" (2023-10): https://www.ttnews.com/articles/convoy-stops-orders-cuts-jobs
- FreightWaves — "Uber Freight still unprofitable after big revenue jump" (2026-08-06): https://www.freightwaves.com/news/uber-freight-still-unprofitable-after-big-revenue-jump
- Uber Technologies — 10-K del año fiscal 2025 (2026): https://www.sec.gov/Archives/edgar/data/1543151/000154315126000015/uber-20251231.htm
- FreightWaves — "Transfix sells brokerage unit to NFI" (2024-06-05): https://www.freightwaves.com/news/transfix-sells-brokerage-unit-to-nfi
- Supply Chain Dive — Transfix/NFI (2024-06): https://www.supplychaindive.com/news/transfix-nfi-acquisition-software-service/718214/
- Nippon.com / Reuters — "Loadsmart valuation hits over $1 billion" (2022-02-02): https://www.nippon.com/en/news/reu20220202KBN2K63OY
- InfoMoney — "Dona da CargoX se torna mais novo unicórnio brasileiro" (2021): https://www.infomoney.com.br/do-zero-ao-topo/logistica-na-america-latina-dona-da-cargox-se-torna-mais-novo-unicornio-brasileiro/
- Exame — "Com aporte de R$ 1,1 bi nasce o unicórnio Grupo Frete.com" (2021): https://exame.com/exame-in/com-aporte-de-r11-bi-nasce-o-unicornio-grupo-frete-com
- Melhor Envio — Blog sobre FreteBras (modelo de suscripción; s/f; fuente comercial): https://melhorenvio.com.br/blog/frete-e-logistica/fretebras/
- Mutuus — Blog sobre FreteBras (s/f): https://www.mutuus.net/blog/fretebras
- Preqin — perfil Frete.com, ronda 2026 (s/f): https://www.preqin.com/data/profile/asset/cargas-transportes-ltda-/201825
- VCBacked — Frete.com (s/f): https://www.vcbacked.co/company/fretecom
- Brazil Journal — "JSL compra a TruckPad; o preço: assumir a dívida" (2022-05): https://braziljournal.com/jsl-compra-a-truckpad-o-preco-assumir-a-divida/
- Mobile Time — compra de TruckPad (2022-06-02): https://www.mobiletime.com.br/?p=721926
- Baguete — "Gigante chinesa FTA investe na TruckPad" (2019): https://www.baguete.com.br/noticias/gigante-chinesa-fta-investe-na-truckpad
- FreightWaves — "Nuvocargo raises $20.5M" (s/f, ~2021): https://www.freightwaves.com/news/nuvocargo-raises-20-5m-to-boost-trade-between-us-and-mexico
- Contxto — "Nuvocargo raises $36.5M" (2023-06-28): https://www.contxto.com/en/mexico/nuvocargo-raises-36-5m-for-nearshoring-opportunities-in-mexico-us-trade/
- DC Velocity — "Nuvocargo raises 12 million" (2021): https://www.dcvelocity.com/articles/50153-nuvocargo-raises-12-million-in-funding-round
- Caixin Global — "China's antitrust regulator summons Lalamove" (2025-09-24): https://www.caixinglobal.com/2025-09-24/chinas-antitrust-regulator-summons-lalamove-over-competition-concerns-102365557.html
- The Standard (HK) — "Share sale on the move again" (s/f; comisiones de Lalamove en China): https://www.thestandard.com.hk/section-news/fc/1/258162/Share-sale-on-the-move-again
- Lalamove — "Secures 3rd round of funding in last 18 months" (2021; fuente de la empresa): https://www.lalamove.com/en-sg/blog/lalamove-secures-3rd-round-of-funding-in-last-18-months
- Wikipedia — Porter (company) (consultada el 2026-10-08): https://en.wikipedia.org/wiki/Porter_(company)
- The Ken — "Logistics firm Porter's rivals dropped like flies" (2025-09-12): https://the-ken.com/story/logistics-firm-porters-rivals-dropped-like-flies-it-lived-to-tell-the-tale/
- Medianama — "Porter profit FY25" (2025-09): https://www.medianama.com/2025/09/223-porter-profit-fy25-revenue-jump-costs-rise/
- Entrackr — "Porter turns profitable with over Rs 4,000 Cr revenue in FY25" (2025): https://entrackr.com/exclusive/exclusive-porter-turns-profitable-with-over-rs-4000-cr-revenue-in-fy25-9496810
- Inc42 — "Porter FY26 profit skyrockets 4X" (2026): https://inc42.com/buzz/porter-fy26-profit-skyrockets-4x-yoy-to-₹229-cr-revenue-up-54/
- YourStory — "Trucking marketplace BlackBuck files for IPO" (2024-07): https://yourstory.com/2024/07/trucking-startup-blackbuck-ipo-sebi-550-crore
- Angel One — "BlackBuck hits the market: Rs 1115 crore IPO" (2024-11): https://www.angelone.in/news/ipos/blackbuck-hits-the-market-details-about-its-rs-1115-crore-ipo
- Inc42 — "BlackBuck posts INR 280 Cr profit in Q4 on tax credit" (2025-05): https://inc42.com/buzz/blackbuck-posts-inr-280-cr-profit-in-q4-on-tax-credit
- ICRA — informe de calificación de Zinka/BlackBuck (s/f): https://www.icra.in/Rating/GetRationalReportFilePdf?id=140442
- YourStory — "BlackBuck's FY23 loss widens to Rs 290 Cr" (2023-12): https://yourstory.com/2023/12/tiger-global-blackbuck-logistics-fy23-loss-widens-revenue-down
- TechCabal — "Kobo360 layoff" (2025-01-20; no se pudo leer completa, error 403): https://techcabal.com/2025/01/20/kobo360-layoff/
- Daba Finance — "Kobo360 cuts jobs amid leadership changes, financial struggles" (2025-01-21): https://dabafinance.com/en/news/kobo360-cuts-jobs-amid-leadership-changes-financial-struggles
- Brand Spur — "Kobo360's rise and fall" (2026-07-20): https://brandspurng.com/2026/07/20/kobo360s-rise-and-fall-how-a-30-million-startup-ended-up-owing-%e2%82%a610-billion/
- TechCabal — "Kobo360 new owner" (2025-03-04): https://techcabal.com/2025/03/04/kobo360-new-owner/

**Márgenes y desintermediación**
- SupplyChain247 — "TIA report signals continued recovery in freight brokerage market" (2025): https://www.supplychain247.com/article/tia_report_signals_continued_recovery_in_freight_brokerage_market
- RXO — comunicado 2T-2024 (8-K, 2024-08): https://www.sec.gov/Archives/edgar/data/1929561/000192956124000098/rxo2024q2pressrelease.htm
- Motley Fool — transcripción de la llamada de resultados 4T-2025 de RXO (2026-02-06): https://www.fool.com/earnings/call-transcripts/2026/02/06/rxo-rxo-q4-2025-earnings-call-transcript/
- PKU HSBC — "Platform Leakage: Disintermediation and Decentralization in Two-Sided Markets" (s/f): https://english.phbs.pku.edu.cn/info/3882/48882.htm
- Management Science — "Trust and Disintermediation: Evidence from an Online Freelance Marketplace": https://pubsonline.informs.org/doi/fpi/10.1287/mnsc.2020.3583

**Argentina — competidores**
- Forbes Argentina — "Las claves de la empresa logística Avancargo para facturar US$ 20 millones en 2023" (2023-02-09): https://www.forbesargentina.com/negocios/las-claves-empresa-logistica-avancargo-facturar-us-20-millones-2023-n29341
- Forbes Argentina — "Avancargo: transporte de carga uberizado" (2019-03-01): https://www.forbesargentina.com/negocios/avancargo-transporte-carga-uberizado-n1522
- Forbes Argentina — "El nivel de digitalización del transporte de cargas en la Argentina apenas llega al 5%" (2023-04-12): https://www.forbesargentina.com/today/el-nivel-digitalizacion-transporte-cargas-argentina-apenas-llega-5-n32138
- Abogados.com.ar — "TCA Tanoira Cassagne asesora a Avancargo en su quinta ronda de inversión" (s/f): https://abogados.com.ar/index.php/tca-tanoira-cassagne-asesora-a-avancargo-en-su-quinta-ronda-de-inversion/34310
- iProUP — "Startup argentina de logística cruza la cordillera y llega a Chile" (2024-08-01 según el buscador; no se pudo leer completa): https://www.iproup.com/innovacion/48999-startup-argentina-de-logistica-cruza-la-cordillera-y-llega-a-chile
- Descubre.vc — ficha de Avancargo (consultada el 2026-10-08): https://www.descubre.vc/avancargo
- Descubre.vc — "Avancargo recibe el Premio Acciones Positivas 2026" (2026-08-11): https://www.descubre.vc/noticia/avancargo-recibe-el-premio-acciones-positivas-2026-por-innovaci-n-en-log-stica-sustentable-2026-08-11
- Avancargo — sitio oficial (consultado el 2026-10-08; fuente de la empresa): https://www.avancargo.com/
- Bichos de Campo / Valor Soja — "Cuatro aplicaciones digitales compiten para captar la mayor parte de la gestión de fletes de granos" (2021-06-21): https://bichosdecampo.com/cuatro-aplicaciones-digitales-compiten-para-captar-la-mayor-parte-de-la-gestion-de-fletes-de-granos/
- Los Andes — "Tiembla Moyano: estos argentinos quieren cambiar el negocio de los camiones" (2020-11-26): https://www.losandes.com.ar/economia/tiembla-moyano-estos-argentinos-quieren-cambiar-el-negocio-de-los-camiones-y-ya-facturan-us-15-millones
- Forbes Argentina — "Fletalo lanza su versión B2B" (2023-02-16): https://www.forbesargentina.com/negocios/fletalo-uber-mudanzas-fletes-lanza-su-version-b2b-n29689
- Descubre.vc — ficha de Fletalo / "Fletalo elegida por Endeavor para el programa HIT 2024" (2024-06-05): https://www.descubre.vc/fletalo ; https://www.descubre.vc/noticia/fletalo-elegida-por-endeavor-para-el-programa-hit-2024-2024-06-05
- App Store — FletArg (s/f): https://apps.apple.com/ar/app/fletarg/id6748755536

**Argentina — estructura, costos y regulación**
- Bolsa de Comercio de Rosario — Informativo Semanal N.º 1855, "Radiografía del transporte de cargas en Argentina" (2018-04-20): https://www.bcr.com.ar/sites/default/files/2019-05/bcr2018_04_20.pdf
- El Economista — transporte ferroviario de cargas (2023-03-28): https://eleconomista.com.ar/economia/pese-precios-mas-bajos-transporte-ferroviario-cargas-crece-n60963
- Revista de la Universidad de Granada (Cuadernos Geográficos) — paper con datos CATAMP/RUTA 2023 (s/f): https://revistaseug.ugr.es/index.php/cuadgeo/article/download/32282/29721/152878
- Agrofy News — "El costo del transporte de cargas acumuló una suba del 30,3% en nueve meses" (2026-10-06): https://news.agrofy.com.ar/noticia/216735/costo-transporte-cargas-acumulo-suba-303-nueve-meses-impacto-gasoil
- Bichos de Campo — "Se actualizaron las tarifas orientativas de fletes" (2026-02-13): https://bichosdecampo.com/se-actualizaron-las-tarifas-orientativas-de-fletes-con-un-valor-de-64-800-pesos-por-tonelada-para-400-kilometros/
- Bichos de Campo — "Conflicto latente en Buenos Aires: no hubo acuerdo por la tarifa referencial" (2026-04-07): https://bichosdecampo.com/conflicto-latente-en-buenos-aires-se-intento-negociar-una-nueva-tarifa-referencial-de-fletes-de-granos-pero-no-hubo-acuerdo/
- Diario de Cuyo — "La suba récord en costos de cargas amenaza el servicio" (2023-06-10): https://www.diariodecuyo.com.ar/noticias/la-suba-record-en-costos-de-cargas-amenaza-el-servicio-48284.html
- Mercado.com.ar — "Piden una ley que regule tiempos de pago a pymes" (s/f; FCE 21 días desde 2023-04-01): https://mercado.com.ar/economia-y-politica/piden-una-ley-que-regule-tiempos-de-pago-a-pymes
- Microjuris — "Se elimina el Registro Único del Transporte Automotor (RUTA)" (2024-12-19): https://aldiaargentina.microjuris.com/2024/12/19/legislacion-transporte-se-elimina-el-registro-unico-del-transporte-automotor-ruta/
- Boletín Oficial — Decreto 1109/2024 (2024-12-19): https://www.boletinoficial.gob.ar/detalleAviso/primera/318417/20241219
- argentina.gob.ar — texto de la Ley 24.653 (consultado el 2026-10-08): https://www.argentina.gob.ar/normativa/nacional/37871/texto
- Marval O'Farrell Mairal — "Una compañía de transporte terrestre es condenada por no asegurar la carga" (s/f, comenta un fallo de diciembre de 2020): https://www.marval.com/Publicacion/una-compania-de-transporte-terrestre-es-condenada-por-no-asegurar-la-carga-13921
- Microjuris — robo de carga no es caso fortuito (2012-12-11): https://aldiaargentina.microjuris.com/2012/12/11/dada-la-profesionalidad-de-la-demandada-no-puede-sostenerse-que-un-robo-sea-un-caso-fortuito-que-lo-exonere-de-responsabilidad/
- Derecho en Zapatillas — "Le robaron la carga en plena ruta y perdió el juicio" (2026): https://www.derechoenzapatillas.com/2026/le-robaron-la-carga-en-plena-ruta-y-perdio-el-juicio-cuando-el-transportista-responde/
- Aduana News — "Argentina moderniza las cartas de porte para granos" (2026): https://aduananews.com/argentina-moderniza-las-cartas-de-porte-para-granos-y-derivados-con-nuevos-controles/
- Blog del Contador — RGC 5821/2026 (2026-02-10): https://siap.blogdelcontador.com.ar/?p=80332
- YoFacturo — "Carta de porte AFIP" (2026-05; afirma que existe un régimen para carga general, no verificado): https://yo-facturo.com/blog/carta-de-porte-afip/

**Frutas y verduras**
- Corporación del Mercado Central — página institucional (s/f): http://buenosaires.gob.ar/gcaba_historico/justicia/corporacion-del-mercado-central-0
- Letra P — "Buscan mayor transparencia y control de calidad en el Mercado Central" (2016-07-05): https://www.letrap.com.ar/nota/2016-7-5-buscan-mayor-transparencia-y-control-de-calidad-en-el-mercado-central
- Diario de Cuyo — "Papa, cebolla, tomate, zapallo y zapallito: el top 5" (2020-07-11): https://www.diariodecuyo.com.ar/noticias/papa-cebolla-tomate-zapallo-y-zapallito-el-top-5-de-las-verduras-248614.html
- Bichos de Campo — horario de operación del Mercado Central (s/f, ~2019): https://bichosdecampo.com/el-aguantadero-de-moreno-ya-fue-con-horarios-fijos-el-mercado-central-quiere-volver-a-funcionar-como-un-mercado
- Jatib, Repetto, Kadener y Díaz — "Estudio sobre el estado actual del Mercado de Tres de Febrero…", Revista Innova UNTREF, 3.ª ed. (julio 2019; cita una encuesta de la FAO de 2010): https://revistas.untref.edu.ar/index.php/innova/article/download/987/823
- Diario de Cuyo — "Mercados, a prevenir" (2020-04-03; retorno vacío, IAPyME). **Atribución probable, no confirmada:** la cita llegó por el resumen del buscador y no leí la nota completa; también podría venir de iProfesional, "Precios y coronavirus: por qué suben tanto las verduras" (2020): https://www.diariodecuyo.com.ar/suplementos/Mercados-a-prevenir-20200403-0073.html ; https://www.iprofesional.com/economia/312757-precios-y-coronavirus-por-que-suben-tanto-las-verduras
- La Capital MdP — "Las fruterías y verdulerías aplican márgenes de hasta un 60%" (s/f; comisión de consignatarios del 10-12% y descuento del flete al productor). **Atribución probable, no confirmada** (dato tomado del resumen del buscador): https://www.lacapitalmdp.com/las-fruterias-y-verdulerias-aplican-margenes-de-utilidad-de-hasta-un-60/
- argentina.gob.ar — DTV-e (s/f): https://www.argentina.gob.ar/node/114064
- Jorge Vega — "Documento de Tránsito Vegetal Electrónico DTV-e, Res. 4297" (s/f): https://jorgevega.com.ar/impuestos/1141-documento-de-transito-vegetal-electronico-dtv-e-res-4297.html

**Nota de método:** varias cifras aparecen solo en resúmenes del buscador o en una única fuente (por ejemplo, el ICT de septiembre de 2026, la ronda 2026 de Frete.com y las cifras de Lalamove). Las marqué en el texto. Antes de usar cualquiera para una decisión con plata, conviene ir a la fuente primaria.
