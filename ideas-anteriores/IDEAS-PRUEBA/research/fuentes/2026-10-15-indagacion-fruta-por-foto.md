# Indagación a fondo: ALI-4-4 — Calidad de fruta por foto

**Fecha:** 2026-10-15 · **Pedido:** separar las ideas que pasaron el filtro en "primeras" y "pendientes".
**Idea de origen:** "Calidad de fruta en recepción controlada a ojo y en papel" (NICHOS-Y-PROBLEMAS.xlsx). Nota de Facu del 2026-10-14: una app o página para saber qué tan buena está la fruta, entrenando una IA a la que se le saca una foto.

**Cómo leer este documento (Regla N.º 1):**
- **DATO** = verificado, con fuente y fecha (la lista completa está en la sección 9).
- **ESTIMACIÓN** = cuenta o supuesto mío, con el razonamiento.
- **OPINIÓN** = mi juicio.
- Lo que una empresa dice de sí misma va marcado **"según la propia empresa"**.
- Usé 15 de 15 búsquedas web permitidas. Además abrí unas 30 páginas y documentos (WebFetch y descargas).

---

## 1. Qué es exactamente (especificación)

### El problema
- En los empaques y exportadoras, la calidad de la fruta (tamaño, color, defectos de la piel) se controla **por muestreo**: un inspector toma frutas, las mira, las mide con un calibre manual y anota en una planilla.
  - **DATO:** el caso de Gesex (exportadora chilena de uva y carozo, cliente de Clarifresh) describe justo eso antes de la herramienta: inspecciones en papel, mediciones distintas según el inspector y reportes lentos en plena temporada (Clarifresh, caso publicado el 2026-08-25).
- Ese control ocurre en **tres momentos** donde hay plata en juego:
  1. **Recepción de la fruta del productor en el empaque.** La clasificación y el porcentaje de descarte definen cuánto cobra el productor.
     - **DATO:** en Río Negro, la Ley 3611 (promulgada el 2002-02-08) obliga a que los contratos de compraventa de fruta digan por escrito las pautas de clasificación y cómo se controlan, las causas de rechazo y cómo se determina el descarte (art. 4). El productor tiene derecho a supervisar la clasificación y a recibir un comprobante con el resultado dentro de las 72 horas (art. 7). Si el empaque no prueba que el productor supervisó o que lo avisó con 24 horas, no puede alegar descartes desfavorables fuera de lo normal (art. 8). Los empaques deben mandar cada semana a la autoridad una planilla diaria de clasificación (art. 10). **No verifiqué si la ley fue modificada después ni qué tanto se cumple hoy.**
  2. **Control del producto terminado antes de embarcar.** Se revisa que cada caja cumpla lo que pide el comprador.
     - **DATO:** el presidente del Comité Argentino de Arándanos (ABC) lo resumió así: "Salir con fruta que no cumpla los estándares implica pérdidas absolutas" (Portal Frutícola, 2026-06-08).
  3. **Recepción en destino o en el mercado.** El comprador inspecciona y puede reclamar o rechazar.
     - **DATO:** el Mercado Central de Buenos Aires tiene un Departamento de Inspección que hace todos los días inspección "organoléptica" (a ojo, olfato y tacto) y toma muestras para controlar plaguicidas, madurez y jugo (sitio del Mercado Central, consultado el 2026-10-15).

### Qué haría el producto
- **App de celular** (o página web que funcione en el celular). El inspector saca una foto a una muestra: una bandeja con 10 a 20 frutas sobre un fondo liso, con una regla y una tarjeta de colores al lado.
- La IA cuenta las frutas, estima el tamaño de cada una, el color de la piel y los defectos visibles. Arma un **informe con foto, fecha, lote y productor**.
- El informe se comparte con la otra parte: con el productor (es justo el "comprobante" que pide la ley de Río Negro) o con el comprador (es evidencia ante un reclamo).
- **Lo que una foto NO puede medir:** firmeza, azúcar, defectos internos. Eso sigue necesitando penetrómetro y refractómetro.
  - **DATO:** Clarifruit (hoy Clarifresh) conectaba su app por inalámbrico a esos instrumentos (Fresh Fruit Portal, 2020-12-02, nota firmada por la propia empresa).

### Quién paga (OPINIÓN, a validar)
1. **El primero: el empaque o exportadora mediana**, a través de su jefe de calidad. Le ahorra horas de inspector y le da evidencia ante clientes y productores. Los grandes ya tienen máquinas en la línea (ver sección 3), pero el control por muestreo sigue siendo manual.
2. **El segundo: cámaras o federaciones de productores.** La misma ley de Río Negro prevé convenios para que técnicos de la Federación o de las Cámaras de productores hagan los controles de clasificación (art. 11). Una "segunda opinión con foto" para el productor encaja ahí. No es una idea nueva: es el mismo problema, con otro pagador.
3. **El tercero: cadenas de supermercados**, en la recepción de su centro de distribución. No investigué cómo controlan hoy.
- **Quién NO paga:** el verdulero o el consumidor que quiere saber "qué tan buena está la fruta". Técnicamente es fácil, pero no encontré a nadie que pague por eso. Ya lo había marcado la síntesis del 2026-10-14.

### Cómo se cobra (ESTIMACIÓN)
- **DATO:** ninguna de las empresas que revisé publica precios (Clarifresh, Intello Labs, AgShift). Todas piden "agendar una demo".
- **ESTIMACIÓN:** una suscripción **por planta y por temporada**, de USD 150 a 400 por mes durante los 6 a 8 meses activos, o sea USD 1.000 a 3.000 por planta por año. **No tengo ningún dato de precio real en Argentina.** El experimento de la sección 8 sirve justamente para averiguarlo.

---

## 2. Mercado en Argentina

### Tamaño del sector (DATOS)
| Qué | Cifra | Fuente |
|---|---|---|
| Producción total de fruta 2025 | 5.548.721 t | Federcitrus, "Actividad Citrícola 2026" (fuente citada: TOP INFO-Federcitrus) |
| — cítricos | 3.756.721 t (68 %) | ídem |
| — pera y manzana | 1.230.000 t | ídem |
| — carozo y cereza | 298.000 t | ídem |
| — tropicales (palta, banana, kiwi) | 159.000 t | ídem |
| — berries (arándano, frutilla, frambuesa) | 65.000 t | ídem |
| — uva de mesa | 40.000 t | ídem |

Nota: saqué el texto del PDF con una herramienta y las columnas vinieron desordenadas. Las reordené y **la suma da exacta (5.548.721 t)**, lo que confirma la lectura.

### Peras y manzanas (Alto Valle de Río Negro y Neuquén)
- **DATO (USDA, informe AR2025-0019 del 2025-12-02, que cita a SENASA):**
  - Producción proyectada para 2025/26: pera 658.000 t y manzana 528.000 t. Exportación proyectada: pera 345.000 t y manzana 86.000 t.
  - Río Negro produce el 82 %, Neuquén el 15 % y el Valle de Uco (Mendoza) el 3 %.
  - Productores: eran unos 9.000 en 2005 y quedaban **1.605 en 2023**.
  - Hay **260 plantas de empaque y 220 frigoríficos**, con unos 60.000 empleos directos.
  - **Las 6 empresas más grandes hacen más del 60 % de la exportación.**
  - Costo de producción: USD 0,72 por kg. El 40 % de ese costo es mano de obra de empaque.
  - Precio FOB de la pera: USD 821 por tonelada de promedio entre enero y agosto de 2025. Manzana: USD 756 por tonelada de promedio en 2024.
  - El informe dice que **no se esperan inversiones en tecnología en el corto plazo**, por precios bajos y costos altos. Es una señal en contra de la disposición a pagar (ver F1).
- **DATO (Federcitrus 2026, con fuente INDEC-SENASA):** en 2025 se exportaron 338.110 t de pera y 91.540 t de manzana.
- **ESTIMACIÓN:** el valor exportado de pera ronda los **USD 280 millones** (338.110 t × USD 821 por t). El de manzana ronda los USD 70 millones (91.540 t × USD 756 por t).
- **DATO (Bichos de Campo, 2025-02-07):** en el verano de 2025 se tiraron miles de toneladas de fruta empacada en 2024 que no se vendió. Un empresario del sector le atribuyó el 15 % del problema al calibre chico y el 85 % a la falta de mercados. **OPINIÓN:** el gran dolor del sector es comercial (mercados y precio), no la inspección de calidad.

### Cítricos (NOA y NEA)
- **DATO (Federcitrus 2026):**
  - Producción 2025: limón 2.213.559 t (Tucumán sola 1.731.132 t), naranja 1.003.144 t, mandarina 410.324 t y pomelo 129.694 t.
  - El NOA produce el 66 % y el NEA el 34 %.
  - Destino: 56,7 % industria, 33,3 % consumo interno y **10,0 % exportación en fresco (321.046 t)**.
  - Hay 5.300 productores, **330 empaques (80 de ellos exportan)** y 26 plantas industriales.
  - El complejo citrícola exportó USD 713 millones en 2025 (dato de INDEC citado por Federcitrus). El limón es el 80 % de ese valor.
  - Exportación fresca de limón en 2025: 216.919 t, casi toda entre abril y septiembre.

### Arándanos (Tucumán, Entre Ríos, Corrientes, Buenos Aires)
- **DATO:** hay unas 3.500 hectáreas. SENASA certificó más de 4.200 t de arándano fresco exportado desde Entre Ríos en la temporada 2025/26 (Portal Frutícola, 2026-02-04).
- **DATO (ABC, Portal Frutícola 2026-06-08):** la cosecha proyectada para 2026 es de unos 15 millones de kg. El 60 % va a exportación, el 20 % a congelado y el 20 % al mercado interno.
- **DATO, con salvedad:** según una nota de FreshPlaza que cita a ABC, toda la fruta fresca se exporta por avión. Solo vi el resumen, no la nota completa. **OPINIÓN:** si es así, cada kilo rechazado en destino cuesta caro, porque el flete aéreo ya se pagó.

### Dónde hay plata en juego (resumen)
| Momento | Quién pierde | Evidencia | Tamaño del dolor (OPINIÓN) |
|---|---|---|---|
| Recepción productor → empaque | El productor, si le clasifican de más como descarte; el empaque, si tiene juicios | Ley 3611 (arts. 4, 7, 8 y 10). Juicio de un productor contra Standard Fruit por USD 291.049 (Bichos de Campo, 2019-09-16), aunque ese juicio fue por **precio**, no por clasificación | Medio. Es real y está en la ley, pero no encontré cifras de cuánto se discute por clasificación |
| Producto terminado → embarque | Exportador | Caso Gesex (Chile). La frase del presidente de ABC citada arriba | Medio-alto en fruta de alto valor (arándano por avión, cereza) |
| Destino / mercado | Exportador o mayorista | Inspección diaria en el Mercado Central | **No lo pude cuantificar**: no encontré cifras de reclamos o rechazos de fruta argentina |

### Tamaño del mercado para este producto (ESTIMACIÓN)
- **Clientes posibles en Argentina:** 80 empaques de cítricos que exportan, una parte de los 260 empaques de pera y manzana, los exportadores de arándano (no encontré cuántos son) y los de nuez. Digamos entre **100 y 200 plantas**.
- **Facturación posible si las tuviéramos a todas:** 100 a 200 plantas × USD 1.000 a 3.000 por año = **USD 100.000 a 600.000 por año**.
- **Captura realista a 2 años:** 5 a 15 clientes, o sea **USD 5.000 a 45.000 por año**.
- **OPINIÓN:**
  - Como negocio de etapa 1 para una persona, puede andar.
  - Como startup, el mercado argentino es chico. Habría que salir a Chile, Perú y otros países, donde ya están Clarifresh y Nativa Labs.

---

## 3. Qué existe en Argentina y afuera (verificado)

### Afuera, con clientes
| Empresa | Qué hace | Clientes y señales | Precio | Fuente |
|---|---|---|---|---|
| **Clarifresh** (ex Clarifruit). País: indicios de Israel (perfil de CB Insights, LinkedIn) | App de celular para el inspector más un tablero para el gerente de calidad. Mide tamaño y defectos por foto | Testimonios de Zespri, Dole Sunshine, Wish Farms y WorldWide Fruit. **En Chile: Gesex** (uva y carozo). Según la propia empresa: 20 % menos desperdicio y +40 % de productividad. CB Insights informa una ronda de USD 12 M del 2022-11-16 (es un agregador; no lo verifiqué en la fuente original) | No publica | clarifresh.com, caso Gesex (2026-08-25) |
| **Intello Labs** (India) | Hoy se presenta como fabricante de **máquinas** de clasificación con cámaras, más una plataforma de subastas por calidad. En su página actual no aparece una app de celular | Según la propia empresa: más de 100.000 t procesadas, más de 95 % de precisión y más de 1.000 millones de imágenes de entrenamiento. Opera en India, Europa y Sudáfrica. América Latina figura solo como "expansión futura" | No publica | intellolabs.com |
| **AgShift** | "Hydra", un analizador de calidad con cámara e IA. Frutilla, frambuesa y almendra | Logos de Driscoll's, Olam y Wish Farms. Según la propia empresa: "30+" equipos instalados | No publica | agshift.com |
| **Nativa Labs** (Chile) | "Nueces IA": inspección de nueces por imagen, con informes automáticos | **8 exportadoras en Chile y Coralino, principal exportador de nueces de Argentina.** La fundadora fue inspectora de calidad. Planea entrar a California en 2026 | No publica | Fresh Fruit Portal, 2026-06-11 |
| Otros que nombra CB Insights (no los verifiqué uno por uno) | AgriNorm, QC One, Neolithics, RAAV Techlabs | — | — | cbinsights.com |

**OPINIÓN:**
- Nativa Labs es la señal más importante de esta investigación. Una startup chilena chica, fundada por una ex inspectora, vende inspección por imagen en el Cono Sur y ya tiene un cliente argentino.
- Eso prueba dos cosas: que hay quien paga en la región, y que la competencia regional ya existe.

### Máquinas en la línea de empaque (otra categoría)
- **DATO:** TOMRA y MAF Roda venden clasificadoras ópticas que separan la fruta por defectos de piel, tamaño y color dentro de la línea de empaque (material comercial de las propias empresas, Portal Frutícola).
- **DATO:** según el diario Río Negro (2026-05-06), en los galpones del Alto Valle las máquinas clasifican la fruta por peso, calibre y color.
- **No pude verificar** qué empaques del Alto Valle tienen clasificadoras ópticas de defectos y cuáles no.
- **OPINIÓN:** el control **dentro de la línea** ya está automatizado en los empaques grandes. El hueco está en el control **por muestreo**: en la recepción, antes del embarque y en destino. Eso sigue siendo a ojo y en papel.

### En Argentina
| Quién | Qué hace | ¿Compite? | Fuente |
|---|---|---|---|
| **ZoomAgri** (Buenos Aires, con oficinas en Madrid, Londrina y Perth) | Calidad física y variedad de **granos** (cebada, trigo, soja, maíz) con imágenes e IA. Su sitio enlaza noticias de rondas de USD 3,3 M y USD 6 M (esta última con GrainCorp) | No: no hace fruta | zoomagri.com |
| **MachVision** (Argentina, según su dominio y su teléfono) | Equipos de visión para granos, semillas, arroz, mazorcas y frutos secos. Logos de Bayer, Corteva, Syngenta y Adecoagro | No hace fruta fresca. Podría entrar en nuez | machvision.com.ar |
| **Baufest** (consultora) | En 2021 presentó un desarrollo de visión para detectar daños y madurez en embarques de fruta | No sé si es un producto a la venta: la nota no nombra clientes | Mercado, 2021-09-09 |
| Universidad Nacional de Santiago del Estero | Investigación sobre visión artificial para daños en fruta | Es académico | amcaonline.org.ar |

**Resultado:** **no encontré ninguna empresa argentina que venda inspección de fruta fresca por foto de celular.** Ojo: tenía un tope de 15 búsquedas compartidas, así que "no encontré" no significa "no existe".

**Dato previo dudoso:** la tabla del 2026-10-13 decía que Intello Labs tenía como clientes a Reliance Fresh, Amazon India y Dole Asia. Hoy eso solo aparece en los metadatos ocultos de su página, no en el texto. Hay que tomarlo como no confirmado.

---

## 4. Cómo se construiría y cuánto costaría (ESTIMACIÓN)

### Fase 0 — Prueba de concepto sin entrenar nada (30 días, menos de USD 300)
1. **Protocolo de foto fijo:** bandeja con 10 a 20 frutas, fondo mate de un color, una regla o un círculo de tamaño conocido para calcular milímetros y una tarjeta de colores. Siempre a la misma altura y con luz pareja (de día a la sombra, o una caja de luz barata).
2. **App web** hecha con Claude Code, igual que CEMEVA: sacar foto → mandarla a un modelo general de visión (Claude, Gemini o GPT) con instrucciones y ejemplos → recibir un resultado ordenado por fruta (tamaño, color y defectos) → generar un informe PDF con la foto.
3. **El tamaño en milímetros no conviene pedírselo al modelo general.** Es más confiable medirlo con procesamiento clásico de imagen, usando la referencia de tamaño. Esto lo puede programar Claude.
4. **Medir contra el inspector:** las mismas frutas, clasificadas por el inspector y por la app. Contar en cuántas coinciden.

| Costo Fase 0 | USD (ESTIMACIÓN) |
|---|---|
| Uso de la API de visión (algunos cientos de fotos; menos de USD 0,05 por foto; hay que verificar la tarifa vigente) | 10 a 30 |
| Hosting (Cloudflare gratis, Facu ya lo tiene conectado) y dominio | 0 a 15 |
| Bandeja, fondo, regla, tarjeta de color y luz | 30 a 80 |
| Viaje a 1 o 2 empaques (opcional; depende de dónde esté Facu, que no lo sé) | 0 a 170 |
| **Total** | **40 a 295** |

### Fase 1 — Modelo ajustado con fotos del cliente (2 a 4 meses, solo si pasa el corte)
- **ESTIMACIÓN:** **1.000 a 3.000 fotos por especie**, con varios cientos de ejemplos de cada defecto común. Los defectos raros piden más fotos. **No encontré una fuente que fije este número**: sale de la práctica habitual con detectores de objetos, y el piloto lo va a corregir.
- **El etiquetado lo hace el inspector del cliente, como parte de su trabajo:** cada foto va con su planilla.
- **OPINIÓN:** ese archivo de fotos etiquetadas con el criterio local es lo único difícil de copiar del negocio.
- Costo de entrenamiento en la nube: decenas a pocos cientos de USD (ESTIMACIÓN). Hay datasets públicos de defectos de manzana (por ejemplo, uno en Roboflow Universe; lo vi en los resultados de búsqueda, no lo abrí).

### Fase 2 — Producto para varios clientes (6 a 12 meses)
- Que funcione sin señal en el galpón y sincronice después.
- Que cada cliente configure sus propias normas: cada mercado pide calibres y defectos distintos.
- Tablero por productor y por lote, y exportación a planilla.
- **ESTIMACIÓN de costo propio:** sobre todo horas de Facu con Claude, más USD 50 a 150 por mes de infraestructura y API cuando haya clientes.

### Celular o cámara fija (OPINIÓN)
- **Celular:** cuesta cero en equipos, sirve en recepción, en control final y en destino, y es lo que usan Clarifresh y Gesex. La contra es la variación de luz y ángulo, que se maneja con el protocolo de bandeja.
- **Cámara fija:** da más precisión, pero hay que instalar equipos y compite con TOMRA y MAF Roda.
- **Empezar con celular.**

---

## 5. Regulación y riesgos

### Regulación (DATOS)
- **Para vender software de control interno de calidad, no encontré ninguna norma que exija habilitación.** OPINIÓN: no la necesita, mientras el producto se venda como herramienta de apoyo y no como certificación oficial.
- **SENASA certifica la sanidad, no reemplazable por una app.**
  - La Resolución SENASA 94/2003 regula la inspección de pera, manzana y membrillo en las plantas de empaque para Brasil y mercados parecidos. La hacen inspectores habilitados que no pueden tener ningún vínculo con el empaque, y todas las partidas a Brasil se inspeccionan junto con el organismo brasileño.
  - El foco es sanitario (por ejemplo, la carpocapsa) y de trazabilidad. No trata la calidad comercial.
- **Normas de calidad comercial.**
  - DATO: el protocolo del Sello "Alimentos Argentinos" para manzana fresca (Secretaría de Agricultura, sello voluntario) fija:
    - tamaño mínimo de 61 mm de diámetro;
    - defectos graves hasta 2 % en categoría Extra y 6 % en categoría I;
    - defectos leves hasta 5 % y 10 %, y total de defectos hasta 5 % y 12 %;
    - color según la proporción de piel con el color de la variedad;
    - firmeza medida con penetrómetro.
  - **OPINIÓN:** esto es justo lo que la app tendría que medir, salvo la firmeza.
  - **No pude verificar** cuál es la norma nacional de calidad comercial vigente para exportar fruta fresca de pepita.
- **Ley 3611 de Río Negro (transparencia frutícola):** ver la sección 1. Hace que la clasificación sea materia de contrato y de control.
- **Mercado interno de hortalizas:** la Resolución SENASA 328/2025 aprobó la reglamentación de hortalizas frescas. **No cubre fruta**; la menciono solo porque apareció en la búsqueda.

### Riesgos (OPINIÓN, salvo que diga DATO)
1. **Pocos clientes y concentrados.**
   - DATO: 6 empresas hacen más del 60 % de la exportación de pera y manzana.
   - Perder o no conseguir a 2 o 3 cuentas cambia todo.
2. **Sector en crisis, con poca plata para tecnología.** DATO: de 9.000 a 1.605 productores, y el USDA no espera inversiones en tecnología en el corto plazo.
3. **Precisión.** Un error en la clasificación termina en una discusión de plata. El producto tiene que presentarse como "evidencia y registro", no como "juez".
4. **Tensión política.** Una herramienta que genera evidencia puede gustarle al productor y molestarle a algunos empaques. Hay que elegir de qué lado se vende primero.
5. **Datos sensibles.** Las fotos y los porcentajes de calidad son información de negociación.
   - DATO: un trabajo académico de 2025 dice que los minoristas de alimentos evitan los modelos de IA de terceros por privacidad de datos (arXiv 2511.01449).
   - Hay que ofrecer confidencialidad por contrato.
6. **Temporada.** Se trabaja 6 a 8 meses por año por especie. Para tener ingresos todo el año hay que combinar especies (arándano, cereza, pera y manzana, cítricos).
7. **Competencia regional.** Clarifresh ya está en Chile. Nativa Labs ya le vende a un argentino y podría pasar de nuez a fruta fresca.
8. **Depender del proveedor de IA.** Si cambian el modelo o la tarifa, el resultado puede cambiar. Conviene guardar las fotos etiquetadas para no depender de un solo proveedor.

---

## 6. Respuestas a las dudas de Facu: ¿se puede entrenar una IA que lo haga con una foto?

**Respuesta corta: sí para lo que se ve en la piel; no para lo de adentro. Y para empezar no hace falta entrenar nada.**

- **Lo que una foto puede medir:** tamaño (si hay una referencia de medida en la foto), color de la piel, defectos visibles (manchas, heridas, quemado de sol, golpes marcados, podredumbre, deformaciones) y cantidad de frutas.
- **Lo que no puede medir:** firmeza, azúcar, defectos internos y golpes recientes que todavía no se ven.
- **¿Hay pruebas de que funciona?**
  - **DATO:** Clarifresh lo hace con celular en clientes reales (caso Gesex: tamaño y defectos).
  - **DATO:** Nativa Labs lo hace con nueces en 9 exportadoras.
  - **DATO, según la propia empresa:** Intello Labs dice tener más de 95 % de precisión.
- **¿Sirve un modelo general sin entrenar?**
  - **DATO (arXiv 2511.01449, 2025-11-03):** en una prueba académica chica, Gemini sin ningún ejemplo acertó **83,3 %** al clasificar 10 frutas en 5 niveles de frescura. Con algunos ejemplos acertó 84,9 %. El método entrenado de los autores llegó a 92,7 %.
  - Ojo: eran unas 300 fotos de prueba sacadas de internet, y medían frescura, no defectos de exportación.
  - **OPINIÓN:** un modelo general alcanza para un prototipo que impresione y para medir la brecha con el inspector. No alcanza para reemplazar al inspector en defectos chicos. Para eso hace falta ajustar con fotos propias etiquetadas (Fase 1).
- **"Entrenar una IA" en la práctica significa:**
  1. Fijar cómo se saca la foto.
  2. Probar con un modelo general.
  3. Medir contra el inspector.
  4. Juntar las fotos donde falla, con la respuesta correcta del inspector.
  5. Ajustar un modelo con esas fotos.
  - No se arranca de cero, y el trabajo pesado es juntar y etiquetar fotos, no programar.
- **¿Una página para que cualquiera saque una foto y sepa qué tan buena está la fruta?** Se puede hacer en una semana. **OPINIÓN:** no hay quien pague. El valor está en el empaque, donde la clasificación mueve plata.

---

## 7. Filtro final

| Filtro | Puntaje | Por qué |
|---|---|---|
| **F1 — Demanda comprobable en Argentina** | **3** | **A favor:** Coralino (Argentina) le paga a Nativa Labs por inspección por imagen de nueces; Gesex (Chile) le paga a Clarifresh; la Ley 3611 convierte la clasificación en materia de contrato; el Mercado Central inspecciona todos los días. **En contra:** no encontré ningún empaque de fruta fresca en Argentina que pague por esto, el sector está en crisis y con poca inversión, y no pude cuantificar los reclamos |
| **F2 — Producto automatizable y global** | **4** | Es software con IA y el mismo producto sirve en Chile, Perú o Sudáfrica. **Resta:** hay que ajustarlo por especie y por norma, la puesta en marcha en cada cliente es presencial y trabaja por temporadas |
| **F3 — Validable rápido y barato (30 días, < USD 300)** | **3** | El prototipo con un modelo general sale en días y por menos de USD 100. Es temporada alta de arándano (pico en las semanas 40 a 44 = 2026-09-28 a 2026-11-01) y hay pera en frío. **Resta:** hay que conseguir que un jefe de calidad colabore sin tener contactos, y probar la precisión de verdad requiere su tiempo. La cosecha de pera y manzana, donde más se discute la recepción, es recién de enero a abril de 2027 |
| **F4 — Riesgo legal manejable (5 = bajo)** | **4** | No hay habilitaciones. No reemplaza a SENASA. **Resta:** si el informe se usa en una disputa de plata, hay riesgo de reclamo, y los datos del cliente son sensibles. Se maneja con contrato y con presentarlo como "evidencia", no como "juez" |
| **F5 — Encaje con Facu** | **4** | Es tecnología del mundo físico con cámaras, como le gusta. Ya hizo con Claude una app de **calidad y liquidaciones de granos** (CEMEVA): es el mismo problema, con fruta en lugar de grano. Como ingeniero industrial maneja muestreo y control de calidad. **Resta:** no sé si tiene contactos en la fruticultura ni dónde vive respecto del Alto Valle, Concordia o Tucumán. Su inglés básico pesa poco porque el Cono Sur habla español |
| **TOTAL** | **18 / 25** | |

### Recomendación: **PRIMERA, como experimento chico de validación (no como negocio principal todavía)**
**Por qué (OPINIÓN):**
- La duda principal es si un empaque argentino paga. Esa duda **solo se resuelve hablando con empaques**, y averiguarlo cuesta menos de USD 300 y 30 días.
- **El momento es ahora:** el pico de arándano termina el 2026-11-01. Si se deja pasar, la próxima ventana fuerte es la cosecha de pera y manzana (enero a abril de 2027). Las entrevistas de ahora sirven para llegar a esa ventana con un piloto acordado.
- Encaja muy bien con lo que Facu ya hizo (CEMEVA) y con lo que le gusta.
- **Aunque falle, enseña algo valioso para la etapa 2:** vender a la agroindustria y trabajar con visión por IA en el mundo físico.
- **Freno honesto:** el mercado argentino es chico (ver la estimación de la sección 2) y hay competidores regionales con capital. Si el experimento no muestra pago o compromiso concreto, se corta sin culpa.

---

## 8. Primer experimento concreto

**Nombre:** "Foto contra inspector" + 15 entrevistas
**Fechas:** del 2026-10-16 al 2026-11-15 (30 días).

### Qué
1. **15 entrevistas** (en persona, por videollamada o por teléfono), al estilo The Mom Test:
   - 10 con jefes de calidad o de recepción de empaques: arándano ahora, más pera y manzana, y cítricos;
   - 3 con productores o con una cámara de productores;
   - 2 con exportadores de nuez o de cereza.
   - Lo ideal es que una sea con alguien de **Coralino**, para preguntarle por qué le compró a Nativa Labs y cuánto le cambió.
2. **Prototipo "foto → informe"** con un modelo general (sección 4, Fase 0). Mostrarlo recién **después** de escuchar el problema, nunca antes.
3. **Prueba de precisión** con al menos 1 empaque: que el inspector mande por WhatsApp unas 10 fotos de bandeja con su planilla. Comparar fruta por fruta (meta: más de 100 frutas comparadas).

### Con quién y cómo llegar
- **LinkedIn:** buscar "calidad", "control de calidad", "recepción" o "empaque" junto con Concordia, Cipolletti, General Roca, Villa Regina, Tucumán o Famaillá. Mandar un mensaje corto que pida 20 minutos para aprender cómo controlan la calidad hoy, sin vender nada.
- **Entidades** (las tres existen, según las fuentes de este informe): CAFI (Cámara Argentina de Fruticultores Integrados), ABC (Comité Argentino de Arándanos) y Federcitrus. Además, la Secretaría de Fruticultura de Río Negro, que recibe las planillas de clasificación (Ley 3611).
- **Universidad:** compañeros o docentes de ingeniería industrial o agronomía que trabajen en empaques. **No sé si Facu los tiene: hay que preguntárselo.**
- **Regla:** cada entrevista termina pidiendo un nombre más ("¿con quién más debería hablar?").

### Números
| Concepto | Valor |
|---|---|
| Costo (ESTIMACIÓN) | USD 40 a 295 (ver la sección 4) |
| Horas de Facu (ESTIMACIÓN) | unas 40 en total (15 entrevistas de 30 a 45 minutos, más prototipo, mensajes y análisis) |
| Días | 30 |
| **Pérdida máxima** | **USD 300 y 40 horas.** Si se pasa de eso, se corta igual |

### Número para SEGUIR (tienen que darse las tres cosas)
1. Al menos **4 de 10 empaques** cuentan **con hechos concretos** (una fecha, un monto, un caso real) un costo actual: un reclamo, horas de inspector o una discusión con un productor.
2. Al menos **1 empaque** se compromete a algo que le cuesta: un piloto pago, una carta de intención con precio, o darnos 300 o más fotos etiquetadas y 2 horas de su inspector para la temporada 2027.
3. El prototipo coincide con el inspector en **al menos 80 %** de las frutas en tamaño y categoría, sobre más de 100 frutas. (Es un umbral propio; los competidores no publican cifras comparables.)

### Número para CORTAR (alcanza con una)
- Menos de **2 de 10** empaques describen un costo concreto.
- **Ningún** empaque acepta dar fotos, tiempo o plata.
- El prototipo coincide menos del **60 %** y no mejora después de dos ajustes del protocolo de foto.

### 5 preguntas al estilo The Mom Test (para jefes de calidad o de recepción)
1. "Contame la última vez que tuvieron una diferencia de calidad con un productor o con un cliente. ¿Qué pasó, cuánto se discutió y cómo terminó?"
2. "¿Cómo hicieron el control de calidad ayer? ¿Quién lo hizo, cuántas muestras, dónde quedó anotado y quién lo miró después?"
3. "¿Cuánto les costó el último reclamo o rechazo por calidad? ¿Tenían fotos o registros para defenderse?"
4. "¿Probaron alguna vez algo para digitalizar esto (planillas en tablet, apps, Clarifresh u otra)? ¿Qué pasó? ¿Por qué lo dejaron o lo siguen usando?"
5. "La última vez que compraron una herramienta o un servicio para calidad, ¿quién lo decidió, de qué presupuesto salió y cuánto costó?"

*(Para productores: "¿Cuándo fue la última vez que no estuviste de acuerdo con la clasificación o el descarte que te liquidaron? ¿Qué hiciste? ¿Te sirvió?")*

**Qué NO preguntar:** "¿Usarías una app que...?" o "¿Te parece buena idea?". Esas preguntas generan cumplidos, no datos.

---

## 9. Fuentes (todas consultadas el 2026-10-15)

**Sector y cifras**
- USDA FAS, *Argentina: Fresh Deciduous Fruit Annual*, informe AR2025-0019, 2025-12-02 (PDF descargado de la API de reportes GAIN): https://apps.fas.usda.gov/newgainapi/api/Report/DownloadReportByFileName?fileName=Fresh%20Deciduous%20Fruit%20Annual_Buenos%20Aires_Argentina_AR2025-0019
- Federcitrus, *Actividad Citrícola 2026* (datos de 2025): https://www.federcitrus.org/wp-content/uploads/2026/08/Federcitrus-AC-2026.pdf · índice: https://www.federcitrus.org/estadisticas/
- Cancillería argentina, apertura de Chile al limón argentino (2025-07-11): https://cancilleria.gob.ar/es/actualidad/noticias/apertura-del-mercado-chileno-para-exportaciones-argentinas-de-limones-frescos
- Argentina.gob.ar, informe estadístico frutícola norpatagónico (datos 2020, publicado el 2021-01-26): https://www.argentina.gob.ar/noticias/informe-estadistico-sobre-la-produccion-fruticola-de-la-region-norpatagonica
- SENASA, *Mensuario estadístico frutícola*, mayo de 2024 (las tablas son imágenes; no extraje cifras): https://www.argentina.gob.ar/sites/default/files/mensuario_estadistico_fruticola_-_mayo_de_2024_-_senasa_centro_regional_patagonia_norte.pdf
- Bichos de Campo, estimaciones de la cosecha 2024 de pera y manzana (2024-06-12): https://bichosdecampo.com/primeras-estimaciones-de-la-cosecha-de-peras-y-manzanas-cayo-la-fruta-enviada-a-industria-y-aumentaron-las-exportaciones/
- Bichos de Campo, fruta empacada descartada (2025-02-07): https://bichosdecampo.com/comienza-la-nueva-cosecha-de-peras-y-manzanas-con-un-dato-alarmante-las-empresas-del-alto-valle-descartan-miles-de-toneladas-de-fruta-empacada-en-2024-que-no-se-lograron-vender/
- Diario Río Negro, la cadena de pera y manzana eslabón por eslabón (2026-05-06): https://www.rionegro.com.ar/rural/una-de-las-mayores-economias-regionales-del-pais-esta-en-la-patagonia-como-funciona-eslabon-por-eslabon-la-cadena-de-peras-y-manzanas-4564498/
- Portal Frutícola, arándanos de Entre Ríos 2025/26 (2026-02-04): https://www.portalfruticola.com/?p=611184
- Portal Frutícola, proyección de la temporada 2026 de arándanos (2026-06-08): https://www.portalfruticola.com/noticias/2026/06/08/arandano-argentina-15/
- FreshPlaza, ventana de exportación del arándano argentino (solo vi el resumen de la búsqueda): https://www.freshplaza.com/north-america/article/9792465/supply-window-is-argentina-s-competitive-advantage-in-global-blueberry-landscape

**Normas y control de calidad**
- Ley 3611 de Río Negro (2002), texto en PDF de la Legislatura: https://web.legisrn.gov.ar/legislativa/legislacion/documento?id=3815
- Resolución SENASA 94/2003: https://www.argentina.gob.ar/normativa/nacional/resolución-94-2003-83908/texto
- Protocolo SAA147 del Sello Alimentos Argentinos, manzanas frescas: https://alimentosargentinos.magyp.gob.ar/HomeAlimentos/sello/sistema_protocolos/SAA147_Auditoria_MANZANAS_FRESCAS_v04.docx
- Resolución SENASA 328/2025 (hortalizas): https://www.argentina.gob.ar/normativa/nacional/norma-412720/texto
- Mercado Central, inspección de frutas y hortalizas: https://mercadocentral.gob.ar/paginas/inspecci%C3%B3n-de-frutas-y-hortalizas
- Bichos de Campo, condena a una exportadora por liquidar mal la fruta (2019-09-16): https://bichosdecampo.com/cronicas-robadas-una-exportadora-fue-condenada-por-liquidar-mal-los-precios-de-la-fruta-a-un-productor/
- Diario de Cuyo, piloto SAG-Asoex de inspección en líneas, Chile (2019-12-20): https://www.diariodecuyo.com.ar/suplementos/Sistema-piloto-de-inspeccion-para-frutas-20191220-0134.html

**Competencia y tecnología**
- Clarifresh, inicio: https://clarifresh.com/ · clientes: https://clarifresh.com/es/customers · caso Gesex (2026-08-25): https://clarifresh.com/case-studies/gesex-quality-control/
- Fresh Fruit Portal, nota firmada por Clarifruit (2020-12-02): https://www.freshfruitportal.com/archive/2020/12/02/clarifruits-automated-qc-solution-provides-big-benefits-for-both-suppliers-and-retailers/
- CB Insights, competidores de Clarifruit (agregador; perfiles no verificados): https://www.cbinsights.com/company/clarifruit/alternatives-competitors
- Intello Labs: https://www.intellolabs.com/
- AgShift: https://www.agshift.com/
- Fresh Fruit Portal, Nativa Labs / Nueces IA (2026-06-11): https://www.freshfruitportal.com/news/2026/06/11/walnut-ai/
- ZoomAgri: https://www.zoomagri.com/
- MachVision: https://www.machvision.com.ar/
- Mercado, Baufest (2021-09-09): https://mercado.com.ar/tecnologia/baufest-utiliza-ia-para-detectar-danos-en-frutas
- UNSE, visión artificial para daños en fruta: https://amcaonline.org.ar/ojs/index.php/mc/article/download/4272/4198
- Portal Frutícola, TOMRA para empaques de manzana (2022-06-23, material de la empresa): https://www.portalfruticola.com/noticias/2022/06/23/las-soluciones-de-tomra-food-permiten-superar-los-retos-operativos-de-las-empaquetadoras-de-manzanas
- Portal Frutícola, MAF Roda en cítricos: https://www.portalfruticola.com/?p=616745
- Jain et al., "Privacy Preserving Ordinal-Meta Learning with VLMs for Fine-Grained Fruit Quality Prediction", arXiv 2511.01449 (2025-11-03): https://arxiv.org/abs/2511.01449 · tablas: https://arxiv.org/html/2511.01449v1
- Roboflow Universe, dataset de defectos de manzana (no lo abrí): https://universe.roboflow.com/fruitgradechecking/apple_defect_checking

**No pude abrir** (error 403 o 404, o páginas que solo vi en resultados de búsqueda): la ficha del USDA en fas.usda.gov (bajé el PDF por otra vía), la nota de Vía País, MDPI *Agriculture* 15(11):1173 y el espejo del informe del USDA en APEDA.
