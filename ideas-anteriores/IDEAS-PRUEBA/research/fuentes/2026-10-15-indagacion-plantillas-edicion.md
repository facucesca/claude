# Indagación a fondo: T19 — Plantillas (Remotion) y venta automatizada de edición

**Fecha:** 2026-10-15 · **Pedido:** separar las ideas que pasaron el filtro en "primeras" y "pendientes".
**Idea de origen:** "Plantillas Remotion vendibles (subtítulos animados, intros)", puntaje 4,5 en el estudio del 2026-10-02 (`research/2026-10-02-video-foto-133-ideas.md`). Remotion es una herramienta para hacer videos con código.
**Comentario de Facu (2026-10-15):** "si se automatiza la venta de edición y plantillas y creación de todo es un gran negocio que funcionaría prácticamente solo, debería estar más arriba y creo que vale la pena explotarlo".

**Cómo leer este documento (Regla N.º 1):**
- **DATO** = verificado, con fuente y fecha (la lista completa está en la sección 9).
- **ESTIMACIÓN** = cuenta o supuesto mío, con el razonamiento.
- **OPINIÓN** = mi juicio.
- Lo que una empresa dice de sí misma va marcado **"según la propia empresa"**.
- **NO VERIFICADO** = lo busqué y no lo pude confirmar en una fuente primaria.
- Usé 14 de 15 búsquedas web permitidas. Además abrí unas 45 páginas (WebFetch) y consulté dos APIs públicas (npm y GitHub).

**Cruce con el registro (Regla N.º 2):** no hay filas nuevas. Todo lo de este informe es **dato nuevo de ideas ya registradas**:
- Plantillas sueltas → **T19** (la misma idea).
- "Venta automatizada de edición" como servicio para un nicho → es el mismo problema y el mismo cliente que **L8** (edición automática para inmobiliarias y concesionarias), **T7** (propiedades desde fotos), **T9** (inventario de concesionarias), **T15** (catálogo de productos en video), **T2/O3** (edición white-label para agencias) y **E13** (edición de YouTube con IA). Si se elige alguno de esos nichos, es **repetida**; con otro nicho es **parecida**.
- Paquetes de plantillas para usar con Claude Code → **T18** (recetas de edición para Claude Code). El repositorio gratuito `video-shotcraft` (sección 3) es un dato en contra de T18.

---

## En corto (5 líneas)

1. **Hay gente que paga plantillas, pero casi toda la plata se la llevan pocos.** En VideoHive, de las plantillas de Premiere Pro publicadas en los últimos 12 meses, el **85% no vendió ninguna** y la mejor vendió 24 (DATO, 2026-10-15).
2. **Las plantillas de Remotion en particular casi no tienen mercado pago:** el propio Remotion publica componentes y plantillas, hay más de 15 bibliotecas gratis y cualquiera hace una con Claude Code en minutos.
3. **"Funcionaría prácticamente solo": no.** Producir sí se automatiza. Que alguien te encuentre y te compre, no. Y los servicios de edición que venden hoy usan personas.
4. **La parte que sí sirve es la plantilla como motor interno** de un servicio de video para un nicho. Pero eso ya es la idea L8 (en reserva), no algo nuevo.
5. **Filtro: 16/25 → PENDIENTE** como negocio aparte. Si Facu igual quiere probar la "venta sola", hay un experimento de 30 días con pérdida máxima de USD 200 (sección 8).

---

## 1. Qué es exactamente (la versión con más chances, especificada)

### Las cuatro versiones posibles

| Versión | Qué se vende | A quién | Cómo se cobra | Qué es automático |
|---|---|---|---|---|
| A. Plantillas sueltas | Archivos de plantilla (Remotion, After Effects, Premiere, CapCut, Canva) | Editores, creadores, programadores | Pago único USD 10-40 en un marketplace o tienda propia | Todo, una vez hecha la plantilla |
| B. Suscripción de plantillas | Acceso a un catálogo propio | Los mismos | USD X por mes | Todo |
| C. Video por pedido de autoservicio | Un video terminado, hecho desde una plantilla propia con los datos y fotos que sube el cliente | Pequeños negocios de un nicho con videos repetitivos | Precio fijo por video, pagado en la página | Todo menos conseguir clientes y una revisión corta |
| D. Servicio de video por pedido con motor propio | Paquete mensual de videos para un nicho | Negocios o agencias de un nicho | Abono mensual | Producción 80-95% (dato del estudio del 2026-10-02); venta, revisión y cambios son humanos |

### La versión con más chances (OPINIÓN, fundada en las secciones 2 y 3)
- **De las que encajan con "T19" tal cual (A y B): ninguna tiene buenas chances.** Los datos de la sección 2 muestran que la persona típica que sube plantillas no vende nada.
- **La versión con más chances dentro del tema es la D**, con las plantillas como motor interno y no como producto. Pero la D **ya es L8** (o T7, T9, T15 según el nicho). No es una idea nueva.
- **La versión C** es la más cercana a lo que imagina Facu ("venta automatizada... funcionaría solo"). Es la única que vale la pena **probar** como T19, con un experimento barato (sección 8). La especifico así:
  - **Qué se vende:** un video corto (15-60 segundos) terminado. Sale de una plantilla propia hecha en Remotion, más las fotos, textos o datos que sube el cliente.
  - **A quién:** un solo tipo de pequeño negocio que necesite muchos videos parecidos. Facu tiene que elegirlo. Sugerencia: negocios hispanos de EE.UU., porque pagan en dólares y hablan español (recomendación ya hecha en el estudio del 2026-10-02).
  - **Cómo se cobra:** pago en la misma página, con una plataforma que actúa como vendedor registrado (la plataforma vende en tu nombre y se ocupa de los impuestos de cada país). La opción más clara desde Argentina es **Polar** (ver sección 5).
  - **Qué parte es automática:** el pedido, el pago, la carga del material, el armado del video, la entrega y el cobro. **No es automático:** conseguir clientes, revisar cada video unos minutos y atender reclamos.

---

## 2. Mercado (afuera y en Argentina)

### 2.1 ¿Cuánto ganan de verdad los que venden plantillas de video?

**No hay medianas oficiales.** Envato, Motion Array, Canva y Etsy no publican cuánto gana el vendedor típico. Por eso fui a contar ventas a mano en VideoHive (de Envato), que muestra cuántas ventas tiene cada plantilla.

**DATO: VideoHive, búsqueda "subtitles", todas las fechas (consultado el 2026-10-15).**

| Posición (ordenado por ventas) | Ventas de por vida | Precio |
|---|---|---|
| 1 | 4.600 | USD 19 |
| 10 | 936 | USD 29 |
| ~151-180 | 53-63 | USD 14-49 |
| ~331-360 | 6-8 | USD 9-16 |
| **~511-540 (la mitad de la lista)** | **1** | USD 11-49 |
| ~751-780 | ninguna | USD 19-29 |

- Total: 1.029 plantillas. **408 (40%) con cero ventas.** La plantilla del medio vendió **una vez en toda su vida**.
- Envato las agrupa en "Low", "Medium", "High" y "Top Sellers", pero no dice qué significa cada grupo. Por eso uso las ventas contadas, no esos grupos.

**DATO: lo que vende un recién llegado (plantillas publicadas en los últimos 12 meses, consultado el 2026-10-15).**

| Búsqueda | Plantillas nuevas | Con cero ventas | La mejor vendió | Bruto de la mejor |
|---|---|---|---|---|
| "subtitles" | 206 | 155 (**75%**) | 16 ventas a USD 21 | ~USD 336 |
| Categoría "Premiere Pro Templates" | 6.073 | 5.175 (**85%**) | 24 ventas a USD 16 | ~USD 384 |

- **ESTIMACIÓN:** la mejor plantilla nueva del año se llevó menos de USD 200 para su autor. Razonamiento: el bruto de arriba menos la parte de Envato. Si el cobro del 50% del que se habla es cierto (ver abajo), al autor le queda menos de la mitad.
- **Límite del dato:** VideoHive solo muestra las ventas sueltas. Las mismas plantillas pueden ganar algo más en **Envato Elements** (la suscripción de Envato), que paga por descarga desde un fondo común. Un blog dice que paga **USD 0,20-1,00 por descarga**; **NO VERIFICADO** (blog de baja calidad, sin método).

**Cambios recientes en Envato (señales de que se pone peor para el autor):**
- Un artículo de Purethemes (2026-07-02) dice que Envato pasó a todos los autores a una **comisión fija del 50% desde el 2026-07-01**. Antes, los autores exclusivos grandes pagaban desde 12,5%. **NO VERIFICADO en Envato:** su página de ayuda me devolvió error 403. **Conflicto de interés:** Purethemes vende sus propios temas y recomienda vender por fuera de Envato.
- Payhip dice que Envato **no acepta nuevos autores desde marzo de 2026** y que prohíbe vender contenido hecho con IA. **NO VERIFICADO.** **Conflicto de interés:** Payhip compite con Envato.

**Motion Array:**
- Según su centro de ayuda (resumen del buscador; no pude abrir la página): paga regalías del 10% al 50% de lo que factura cada categoría en el mes, repartido en 7 niveles según descargas. Paga desde USD 50, por PayPal o Payoneer.
- El buscador indicó que la página para nuevos autores decía "submissions closed" (no se aceptan nuevos). **NO VERIFICADO:** la página me dio error 403.
- Artlist (dueña de Motion Array) dijo en 2020 que un artista promedio gana más de USD 10.000 por año. Es lo que **dice la propia empresa**, sin datos auditados.

**Canva (programa de creadores):** el fondo de regalías y los pagos son confidenciales; no hay mediana publicada (centro de ayuda de Canva, vía buscador, 2026-10-15).

**Gumroad (tiendas propias de productos digitales):**
- **DATO (estimado por un tercero):** profitable.app (actualizado al 2026-10-08) sigue ~4 millones de productos. Solo **2,3-2,5% tiene alguna venta registrada**. De los que venden, la mitad junta **menos de USD 90 en toda su vida**. Solo ~0,4% de todos los productos pasó los USD 1.000. Sus ingresos son **estimados** desde datos públicos, no reales.
- InsightRaider dice que el creador mediano de Gumroad gana USD 72 por mes. Su método multiplica reseñas por precio por un factor supuesto, y sus páginas se contradicen. **No lo tomo como dato firme.**
- Esto **actualiza y corrige un poco** el estudio del 2026-09-02, que citaba "la mediana gana menos de USD 100 en toda su vida" con fuente "[blog]": la fuente era InsightRaider, cuyo método es débil. El dato de profitable.app va en la misma dirección.

**Etsy:** no encontré datos confiables de tiendas de plantillas de video. El único número (USD 8.000-15.000 por mes por vendedor de plantillas de reels) sale de un blog que **vende su propio paquete de plantillas**: conflicto de interés, lo descarto.

**OPINIÓN sobre 2.1:** sí, hay gente que paga plantillas (la mejor de "subtitles" vendió 4.600 veces). Pero el negocio es de **pocos ganadores viejos**. Para el que entra hoy, la mediana es cero. Y los marketplaces le están bajando la parte al autor.

### 2.2 ¿Y las plantillas de Remotion en particular?

- **DATO: Remotion está creciendo muy rápido.** Descargas mensuales del paquete `remotion` en npm (el repositorio de paquetes de programación):
  - 2024-09-13 a 2024-10-12: 221.109
  - 2025-09-13 a 2025-10-12: 490.657
  - 2026-09-13 a 2026-10-12: **8.406.351** (unas 17 veces más que hace un año)
  - El repositorio tiene 64.303 estrellas en GitHub (2026-10-15).
  - Ojo: las descargas incluyen servidores y procesos automáticos. No son personas.
- **OPINIÓN:** el salto coincide con la llegada de los agentes de IA. Remotion tiene "Agent Skills" oficiales para Claude Code (estudio del 2026-10-02). Esto **juega en contra** de vender plantillas: la misma IA que le permite a Facu hacer una plantilla sin programar le permite a cualquier comprador hacerla gratis.
- **No encontré ningún vendedor externo de plantillas Remotion con ventas visibles.** Dos búsquedas (en Gumroad, Lemon Squeezy, Polar y en general) solo devolvieron bibliotecas gratis y la tienda oficial de Remotion. En la lista de recursos de Remotion hay una sola plantilla que parece paga ("Faceless Shorts Kit", en Gumroad), sin precio ni ventas visibles.
- **Quién compraría una plantilla Remotion:** programadores y empresas que arman videos con código. Hablan inglés. Si el comprador es una empresa de 4 personas o más, además tiene que pagar su propia licencia de Remotion (sección 5).

### 2.3 Precios del servicio de edición "hecha" (para la versión D)

- **DATO:** 99dollarsocial vende videos cortos hechos por personas: **USD 99 por mes por 4 videos**, USD 189 por 8, hasta USD 629 por 30. Dice "Real humans, not AI" (personas reales, no IA). Según la propia empresa (2026-10-15).
- **DATO:** Kimp dice que los servicios de edición "ilimitada" cuestan en general **USD 400-3.000 por mes o más**. Su plan de video permite 2 pedidos activos a la vez (página de Kimp, 2026-10-15).
- Un blog de un editor competidor (Tasty Edits) dice que lo "ilimitado" rinde en la práctica 3-4 proyectos por mes. Conflicto de interés: vende edición.
- **Dato del estudio 2026-10-02 (no re-verificado hoy):** Vidchops cobra USD 495 por mes por 4 videos largos; la mediana en Upwork es ~USD 35 por hora; hay editores argentinos a **USD 5,50-8,50 por hora**.

### 2.4 Argentina
- **No encontré datos** de cuánta gente compra plantillas de video en Argentina, ni lo investigué a fondo: este es un mercado global en inglés.
- Para la versión D en Argentina: se compite con editores locales a USD 5,50-8,50 por hora (estudio del 2026-10-02). Por eso ese estudio recomendó apuntar a hispanos de EE.UU.
- Lo que sí importa de Argentina es **cómo cobrar** (sección 5).

---

## 3. Qué existe (verificado), con precios

### 3.1 Plantillas y componentes de Remotion (la competencia directa de T19)

| Qué | Quién | Precio | Fuente y fecha |
|---|---|---|---|
| Tienda oficial: Editor Starter, Timeline, Colors and Shapes, Cube Transition, NPM Kiosk | Remotion | USD 600, 300, 20, 10 y 40 | remotion.pro, 2026-10-15 |
| Animated Captions (subtítulos animados) | Remotion | USD 100 según el buscador; la página tenía pie de 2025. **Precio actual NO VERIFICADO** | convert.remotion.dev, vía buscador |
| "Remotion Elements": 5 estilos de subtítulos, carteles con nombre ("lower thirds"), cierres para YouTube, gráficos, mapas, etc. Se adaptan "con un agente" | Remotion | **No dice.** La página de cada elemento muestra el código, lo que sugiere que es libre, pero **NO VERIFICADO** | remotion.dev/elements, actualizada el 2026-10-15 |
| Plantilla oficial de subtítulos estilo TikTok | Remotion | Gratis | GitHub, 2026-10-15 |
| 81 plantillas (textos, intros, cierres, transiciones, logos) | React Video Editor | **Gratis** (licencia MIT, uso comercial permitido) | GitHub, 2026-10-15 |
| video-shotcraft: habilidad para Claude Code con 152 "recetas" de tomas y una plantilla | Comunidad | **Gratis** (Apache-2.0); **12.038 estrellas**, creado el 2026-07-19 | API de GitHub, 2026-10-15 |
| Más de 15 bibliotecas listadas por Remotion (Onda: 70 componentes; RenderComp Free: 50 plantillas; cliphou.se; Clippkit; etc.) | Comunidad | Casi todas gratis | remotion.dev/resources, 2026-10-15 |

**Además:** la lista de recursos de Remotion muestra **~23 productos comerciales hechos sobre Remotion** (editores con IA, subtítulos automáticos, generadores de shorts, videos de lanzamiento, etc.). La venta automatizada de video con plantillas **ya tiene muchos jugadores**.

**Un dato a seguir:** la página de Elements dice que se pueden agregar "Element Libraries" de otros creadores dentro de Remotion Studio. Es un canal posible, pero **no pude verificar si permite cobrar**.

### 3.2 Herramientas que editan solas o dan plantillas gratis o baratas

| Herramienta | Qué hace | Precio verificado (2026-10-15) | Cambio respecto del estudio del 2026-10-02 |
|---|---|---|---|
| **CapCut** | Editor completo con plantillas | Gratis (con "free templates"); Pro USD 17,99/mes o USD 149,99/año; Ultra USD 79/mes | **Bajó:** antes figuraba Pro a USD 19,99/mes o 179,99/año. Aparece el plan Ultra |
| **Canva** | Diseño y video con plantillas | Plan gratis permanente. Pro ~USD 15-18/mes según terceros (Piktochart, Costbench). **La página oficial me dio error 403; precio NO VERIFICADO** | Nuevo en el análisis |
| **Submagic** | Subtítulos animados, zooms, B-roll | Starter USD 19/mes (USD 12 anual) por 15 videos; Pro USD 39 (23); Business USD 69 (41) por 100 videos. API desde USD 0,23 hasta 0,10 por minuto | Igual; se agregan los precios anuales |
| **OpusClip** | Clips verticales desde videos largos | Gratis (con marca de agua y 3 días de guardado); Starter USD 15/mes; Pro USD 29/mes con API | Igual |
| **Descript** | Edición por texto | Gratis (60 min/mes, 720p, con marca de agua); Hobbyist USD 16-24; Creator USD 24-35; Business USD 50-65 por persona | Igual; se agregan los minutos: 10, 30 y 40 horas por mes |
| **Envato Elements** | Suscripción a plantillas y recursos | Desde **USD 16,50/mes** por descargas ilimitadas de **más de 29 millones** de recursos | Nuevo en el análisis |

**OPINIÓN:** contra Envato Elements (29 millones de recursos por USD 16,50 por mes) y CapCut o Canva gratis, una **suscripción propia de plantillas (versión B) no tiene lugar** sin una audiencia propia.

### 3.3 Servicios de edición que se venden "automatizados" (pregunta 4)

| Ejemplo | Qué automatiza | Quién edita | Precio | Fuente |
|---|---|---|---|---|
| 99dollarsocial | Formulario, carga, aprobación en panel, publicación programada | **Personas** ("Real humans, not AI") | USD 99 por 4 videos al mes | Su página, 2026-10-15 |
| Kimp Video | Pedidos por plataforma, cola de trabajo | Equipo de editores (lo da a entender; no lo dice explícito) | Rango del rubro USD 400-3.000/mes; su precio exacto no aparece | Su página, 2026-10-15 |
| Submagic, OpusClip, Descript | Todo: el cliente sube y el sistema edita | Nadie (lo hace el cliente con la app) | USD 0-69/mes | Tabla 3.2 |
| Fiverr Go (lanzado 2025-02) | El comprador paga y descarga al instante lo que genera el modelo de IA del freelancer | La IA, con el freelancer como respaldo | USD 25/mes para el freelancer; arrancó en voz, música, diseño y texto. **No encontré video** | Fiverr y TechCrunch, 2025-02 |

**Lo que muestran los ejemplos:** o es **software de autoservicio barato** (el cliente hace el trabajo), o es un **servicio con personas**. No encontré un servicio de edición "hecho para vos" que funcione sin personas y cobre bien.

### 3.4 Qué parte se automatiza de verdad

| Paso | ¿Automatizable? | Base |
|---|---|---|
| Que el cliente te encuentre | **No.** Hacen falta anuncios, contenido, mails o un marketplace | DATO: aun dentro de VideoHive, que ya trae compradores, el 75-85% de lo nuevo no vende |
| Tomar el pedido y cobrar | Sí, 100% (página + pago + formulario) | Polar, Paddle, Gumroad lo hacen (sección 5) |
| Recibir el material | Sí | — |
| Editar | 80-95% en formatos repetitivos que salen de una planilla o de fotos; 30-50% en material crudo variado | Estudio del 2026-10-02 (sección 9 de la herramienta de auto-edición) |
| Revisar la calidad | **No.** Hace falta una persona: 5-15 minutos por pieza | Meta del estudio del 2026-10-02: "≤15 min humanos por pieza" |
| Entregar | Sí, 100% | — |
| Cambios, reclamos, reembolsos | Parcial: la plataforma de cobro maneja disputas; los cambios los hace una persona | — |

---

## 4. Cómo se construiría y cuánto costaría (ESTIMACIÓN)

### Versión C (video por pedido de autoservicio), que es la que se prueba en la sección 8
1. **Plantilla:** Claude Code arma 1 plantilla en Remotion usando las Agent Skills oficiales. Facu decide el diseño y revisa. Tiempo estimado: 10-20 horas de Facu.
2. **Página de venta:** página simple en Cloudflare Pages (Facu ya tiene Cloudflare conectado; plan gratis).
3. **Pago:** Polar, plan gratis. Comisión: 5% + USD 0,50 por venta, más 1,5% si la tarjeta es extranjera (DATO, docs de Polar, 2026-10-15). En un video de USD 19 quedan ~USD 17,25 (ESTIMACIÓN: 19 − 0,95 − 0,50 − 0,29).
4. **Carga del material:** formulario después del pago (Polar permite campos propios; si no alcanza, un formulario gratis).
5. **Armado del video:** en la PC de Facu (gratis) o en Remotion Lambda (servicio en la nube), ~USD 0,02-0,10 por video (estudio del 2026-10-02, con datos de remotion.dev).
6. **Revisión:** Facu mira cada video 5-10 minutos antes de mandarlo.
7. **Entrega:** mail automático con el enlace.

| Costo | Primer mes | Por mes después |
|---|---|---|
| Remotion | 0 (Facu solo entra en la licencia gratis) | 0 hasta 3 personas |
| Polar | 0 fijo + comisiones | Igual |
| Dominio | ~USD 10-15 por año (**NO VERIFICADO hoy**) | — |
| Hosting | 0 (Cloudflare gratis) | 0 |
| Anuncios para probar | USD 150 | Según resultado |
| **Total** | **~USD 165-200** | Comisiones + anuncios |

### Versión A (plantillas sueltas)
- Costo en plata: ~USD 0 (Polar o Gumroad no cobran fijo). Costo real: **tiempo** (estimación: 3-6 horas por plantilla con Claude Code).
- Sin canal de venta, los datos de la sección 2 dicen que lo más probable es no vender.

---

## 5. Regulación, licencias y riesgos

### 5.1 Licencia de Remotion (verificada en remotion.dev y GitHub, 2026-10-15)
- **Gratis** para: personas, empresas con fines de lucro de **hasta 3 empleados**, organizaciones sin fines de lucro, y para evaluar sin uso comercial.
- **Licencia de empresa** para el resto:
  - "Creators": **USD 25 por mes por puesto**.
  - "Automators": **USD 0,01 por video armado, mínimo USD 100 por mes**.
  - "Enterprise": desde **USD 500 por mes**.
- **¿Se pueden vender plantillas?** La licencia no lo prohíbe ni lo menciona. La regla general de las preguntas frecuentes es: "Any commercial use case is allowed as long as you are not selling Remotion as a product itself" (cualquier uso comercial vale mientras no vendas Remotion en sí). Lo prohibido es copiar o modificar el código de Remotion para venderlo o licenciarlo.
- **Lo que complica vender plantillas:** si el cliente **es dueño del proyecto o lo usa**, "both companies' headcount is aggregated" (se suman los empleados de las dos empresas para el límite de 4). Es decir, **una empresa de 4 personas o más que compra una plantilla Remotion necesita su propia licencia** (USD 25 por mes como mínimo). Eso frena la venta a empresas.
- **Si Facu entrega solo el video terminado** (versiones C y D), el cliente "is not a User" (no es usuario de Remotion) y sus empleados no cuentan. Facu, solo o con hasta 3 personas, usa la licencia gratis.
- **Productos donde el cliente arma su video:** permitidos con la licencia gratis ("even if you... launch a SaaS"), incluso con IA que genera código Remotion. Lo que no se permite es dejar que el usuario suba su propio código Remotion.
- **Cambio que viene:** en Remotion 5.0 la telemetría (envío de datos de uso) será obligatoria para los clientes "Automators". Para la licencia gratis sigue siendo voluntaria.

### 5.2 Cobro desde Argentina (verificado el 2026-10-15)

| Plataforma | ¿Acepta vendedores argentinos? | Cómo llega la plata | ¿Acepta servicios con personas? | Comisión |
|---|---|---|---|---|
| **Polar** | **Sí:** Argentina está en su lista de países de pago (paga por Stripe Connect Express) | Transferencia al banco. Costos: USD 2 por mes con pagos activos + 0,25% + USD 0,25 por pago + 0,25-1% de cambio de moneda | **No:** prohíbe "human services". Sí acepta explícitamente "templates" y "videos" | 5% + USD 0,50 (plan gratis); +1,5% tarjetas extranjeras |
| **Paddle** | **Sí:** Argentina no está en la lista de países no admitidos | Transferencia o **Payoneer**, una vez por mes, mínimo USD 100 (resumen del buscador de la ayuda de Paddle) | **No:** prohíbe servicios humanos no ligados a un software; "está hecho para empresas de software". No menciona plantillas | **NO VERIFICADO hoy** (estudio del 2026-09-02: ~5% + USD 0,50) |
| **Gumroad** | Probablemente sí, **pero el medio de pago se contradice**: Wise incluye a Argentina entre los países con pago a banco (sin fecha); el estudio del 2026-09-02 decía solo PayPal y que ya lo cortó una vez (2024-10 a 2025-01). **NO VERIFICADO** | Banco o PayPal, según el país | Vende productos digitales; es vendedor registrado desde el 2025-01-01 | 10% + USD 0,50 venta directa; **30%** si la venta viene de su marketplace |
| **Lemon Squeezy** | En transición a **Stripe Managed Payments**, que **no incluye a Argentina** en sus países admitidos | — | Stripe Managed Payments excluye servicios profesionales y todo lo que tenga "human intervention" | — |
| **Payoneer + factura E** (para la versión D) | Sí (estudios del 2026-09-02 y 2026-10-02) | Cobro directo al cliente | Sí, es la vía para servicios | Hasta 2% por retiro (estudio del 2026-09-02) |

**Conclusión práctica:**
- **Plantillas o video 100% automático → Polar** (el más claro), o Paddle si aprueba la cuenta.
- **Servicio con revisión humana → Payoneer + factura E.** Las plataformas que se ocupan de los impuestos por vos **no aceptan servicios hechos por personas**. Un video automático con 5 minutos de revisión humana queda en **zona gris**: preguntarle a Polar antes de vender.
- **No construir sobre Lemon Squeezy** desde Argentina.

### 5.3 Otros riesgos
- **Recursos dentro de las plantillas:** tipografías, música y videos de stock necesitan licencia que permita redistribuirlos. Pexels prohíbe la reventa "standalone" (estudio del 2026-10-02). Si se usa Higgsfield para fondos o clips, **no verifiqué** sus derechos de reventa como parte de una plantilla.
- **IA en marketplaces:** Envato restringiría el contenido hecho con IA (fuentes secundarias; **NO VERIFICADO**).
- **Riesgo de plataforma alto:** Envato sube comisiones y frena autores (reportado); Motion Array cerró la entrada de autores (reportado); Lemon Squeezy cambia de dueño técnico; Gumroad ya cortó pagos por PayPal una vez.
- **Riesgo de producto:** el propio Remotion publica componentes y plantillas (Elements, tienda). Cualquier plantilla que funcione puede ser copiada, o pasar a ser gratis en la biblioteca oficial.
- **Impuestos en Argentina:** exportación de servicios o monotributo; consultar a un contador (estudios anteriores).

---

## 6. Respuestas a las dudas de Facu

### ¿Funcionaría "prácticamente solo"?
**OPINIÓN: no. Con los datos de hoy, la frase es más deseo que diagnóstico.** Cinco razones:

1. **Lo que se automatiza es producir. Lo que vende es que te encuentren.** Aun dentro de VideoHive, que ya trae los compradores a la puerta, el **75-85% de las plantillas nuevas del último año no vendió ninguna** (DATO). Hacer más plantillas más rápido sube la oferta, no la demanda.
2. **La IA que te deja producir gratis también se lo deja a todos.** Remotion publica sus propios subtítulos y carteles. Hay más de 15 bibliotecas gratis. Un repositorio gratis de "recetas" para Claude Code juntó 12.038 estrellas en 3 meses (DATO). El valor de una plantilla Remotion tiende a cero.
3. **Los que venden edición "hecha para vos" usan personas.** 99dollarsocial lo pone como argumento de venta: "Real humans, not AI" (DATO). Lo 100% automático existe, pero es software barato o gratis (CapCut, Canva, OpusClip, Submagic: USD 0-69 por mes).
4. **Las plataformas que cobran solas no aceptan servicios con personas** (Polar, Paddle, Stripe; DATO). Si es 100% automático, compite como software contra CapCut y Canva. Si tiene una persona, es un servicio, y no es "solo".
5. **Lo más automático que se puede lograr es "semi-solo".** La meta del estudio del 2026-10-02 era ≤15 minutos humanos por pieza, **más** las horas de vender. Eso está bien, pero no es un negocio que funcione solo.

**Lo que sí tiene razón Facu (OPINIÓN):** un **motor propio de plantillas** baja mucho el costo por video y hace escalable un servicio de video. Ese es un activo real. Pero el activo vale **dentro de un negocio que ya vende**, no como producto suelto.

### ¿Debería estar más arriba?
**OPINIÓN: como negocio aparte, no.** El 4,5 del estudio del 2026-10-02 era razonable, y los datos nuevos lo empujan para abajo:
- La mediana del que vende plantillas es cero (DATO, sección 2).
- Remotion compite con sus propias plantillas.
- El cliente con 4 empleados o más tiene que pagar otra licencia.
- Es un mercado en inglés, y Facu tiene inglés básico.
- El proyecto dice que lo pasivo es un complemento, no el objetivo de la etapa 1.

**Como pieza de otro negocio, sí debería subir.** Si Facu elige un servicio de video (L8 u otro de la familia T), las plantillas Remotion son la forma de llegar a "pocos minutos humanos por video". Mi recomendación es **anotar T19 como componente de L8** y no como negocio separado.

### ¿Cuánto se puede esperar ganar? (ESTIMACIÓN, con mediana, no con el mejor caso)

| Versión | Mediana a 6-12 meses | Caso bueno (no el mejor) | Razonamiento |
|---|---|---|---|
| A. Plantillas sueltas (20 plantillas en marketplaces, sin audiencia) | **USD 0-20 por mes** | USD 50-150 por mes | 75-85% de lo nuevo vende cero; la mejor nueva hizo ~USD 340-380 brutos en un año (DATO). Si 1 de cada 5 plantillas vende ~3 veces por año a ~USD 9 netos: 20 × 0,2 × 3 × 9 ≈ USD 108 por año |
| A'. Plantillas Remotion en tienda propia (Polar o Gumroad) | **~USD 0** | USD 20-100 por mes con audiencia propia | 2,3-2,5% de los productos de Gumroad tiene alguna venta (DATO estimado por terceros); además hay oferta gratis |
| B. Suscripción propia | **~USD 0** | — | Contra Envato a USD 16,50 por 29 millones de recursos |
| C. Video por pedido de autoservicio | **USD 0-100 por mes** | USD 300-800 por mes si se encuentra un canal que traiga clientes a menos de lo que paga cada uno | Depende del costo de conseguir cada cliente, que no conozco; lo mide el experimento |
| D. Servicio con motor propio (≈ L8) | **USD 300-800 por mes** con 3-8 clientes, y 10-15 horas por semana | USD 1.000-2.000 por mes | Referencia: USD 99-189 por mes por 4-8 videos hechos por personas (99dollarsocial); un recién llegado cobra 30-50% de los precios de agencia (estudio del 2026-10-02). **Pero esta es la idea L8, no T19** |

---

## 7. Filtro final (evalúo la versión C, que es la mejor versión de T19 que no es otra idea ya registrada)

| Criterio | Puntaje | Justificación |
|---|---|---|
| **F1 Demanda comprobable** (alguien paga) | **2** | Hay gente que paga plantillas (4.600 ventas la mejor de "subtitles"), pero la paga se concentra en pocos y viejos; lo nuevo vende cero en 75-85% de los casos. Para plantillas Remotion de terceros no encontré ninguna venta visible. Para video por pedido de autoservicio, la evidencia de pago es de servicios con personas, no de la versión automática |
| **F2 Producto automatizable y global** | **4** | Producir, cobrar y entregar se automatiza casi del todo, y se puede vender a todo el mundo desde Argentina (Polar o Paddle). Le resto un punto porque conseguir clientes y revisar no se automatiza, y porque la licencia de Remotion frena la venta de plantillas a empresas de 4 o más personas |
| **F3 Validable rápido y barato** (30 días, <USD 300) | **4** | Se arma con Claude Code y se prueba con ~USD 200 en un mes. Le resto un punto porque, si el canal es un marketplace, 30 días sin ventas no distinguen "producto malo" de "nadie lo vio" |
| **F4 Riesgo legal manejable** (5 = bajo) | **4** | Licencia de Remotion clara y gratis para Facu solo. Riesgos menores: licencias de música, tipografías y stock dentro de las plantillas; reglas de IA de los marketplaces; zona gris de "servicio humano" en las plataformas de cobro |
| **F5 Encaje con Facu** | **2** | A favor: no hace falta programar (Claude Code más las Agent Skills de Remotion), y entra en su presupuesto. En contra: el comprador de plantillas Remotion habla inglés (Facu tiene inglés básico); enseña poco de vender a clientes, que es lo que pide la etapa 1; y lo pasivo es complemento según el propósito del proyecto |
| **Total** | **16/25** | |

**Recomendación: PENDIENTE.**
**Por qué:** la demanda para el que entra hoy es casi nula (F1 = 2) y aprende poco de lo que la etapa 1 necesita (F5 = 2). Lo valioso de la idea, el motor de plantillas, **se aprovecha mejor dentro de L8** (o del servicio de video que Facu elija). Si Facu igual quiere probar su hipótesis de "venta sola", puede hacerlo como el **experimento chico en paralelo** que permiten las reglas de la etapa 1, con el tope de la sección 8.

---

## 8. Primer experimento concreto

**Nombre:** "¿Alguien compra un video sin que yo le hable?"
**Qué prueba:** la hipótesis de Facu: que la venta de video con plantillas se hace sola, sin contacto humano.

- **Qué:**
  - 1 formato de video corto (15-30 segundos) hecho con 1 plantilla propia en Remotion.
  - Página de venta + pago con Polar + formulario de carga + armado + revisión de ≤10 minutos + entrega por mail (sección 4).
  - Precio de prueba: **USD 19 por video** (ESTIMACIÓN: debajo de los ~USD 25 por video del servicio con personas de 99dollarsocial y por encima de las apps de USD 12-19 por mes, porque acá el cliente no toca nada).
- **Con quién:** un solo tipo de pequeño negocio, elegido por Facu antes de empezar. Sugerencia: negocios hispanos de EE.UU.
  - **Ojo, Regla N.º 2:** si elige inmobiliarias o concesionarias, es la idea L8 (repetida) y conviene correr el experimento de L8. Si elige tiendas online, es parecida a T15.
- **Cómo llegan los clientes:** USD 150 en anuncios (Meta) dirigidos a ese nicho, más publicaciones gratis. **Sin mensajes uno a uno**: eso probaría la venta manual, no la automática.
- **Días:** 1-10 construir con Claude Code; 11-30 vender. Total: **30 días**.
- **Costo:** ~USD 165-200 (anuncios USD 150 + dominio ~USD 15 + margen para comisiones y pruebas).
- **Qué medir:** visitas, compras, costo de anuncios por compra, minutos humanos por pedido, reembolsos.
- **Número para SEGUIR** (propuesta mía): **5 compras o más** de desconocidos, **costo de anuncios por compra ≤ USD 19** (lo que paga el cliente) y **≤10 minutos humanos por pedido**.
- **Número para CORTAR** (propuesta mía): **1 compra o ninguna** con 300 visitas o más, o costo por compra **mayor a USD 38** (el doble del precio).
- **Zona gris (2-4 compras):** una sola vuelta más, cambiando una sola cosa (precio o nicho), con el mismo tope de plata.
- **Pérdida máxima: USD 200** + ~40-60 horas de Facu. Si se llega al tope, se corta aunque "falte poco".
- **Qué se aprende aunque falle:** cuánto cuesta conseguir un cliente con anuncios; si el formato que Facu eligió le importa a alguien; y Facu queda con un motor de plantillas reutilizable para L8.

**Variante mínima (si Facu quiere probar T19 tal cual, plantillas sueltas):**
- Pack de 5 plantillas Remotion (subtítulos en español + carteles con nombre) en Polar a USD 19, con una versión gratis de muestra. Se difunde en la comunidad de Remotion y en X.
- 14 días, USD 0-15. SEGUIR con 10 ventas o más; CORTAR con 2 o menos.
- **Pronóstico (OPINIÓN): 0-2 ventas**, por la oferta gratis de la sección 3.1. Sirve solo para que Facu lo vea con sus propios números.

---

## 9. Fuentes (todas consultadas el 2026-10-15, salvo que se indique)

**Remotion (licencia, tienda, ecosistema)**
- Licencia: https://github.com/remotion-dev/remotion/blob/main/LICENSE.md
- Preguntas frecuentes de la licencia: https://www.remotion.dev/docs/license/faq
- Precios de la licencia de empresa: https://www.remotion.pro/license
- Tienda oficial: https://www.remotion.pro/ y https://www.remotion.pro/store
- Animated Captions (precio vía buscador): https://convert.remotion.dev/docs/animated-captions
- Remotion Elements: https://www.remotion.dev/elements · https://convert.remotion.dev/elements · https://remotion.dev/elements/captions/basic-captions/
- Recursos y bibliotecas de la comunidad: https://remotion.dev/resources
- 81 plantillas gratis: https://github.com/reactvideoeditor/remotion-templates
- video-shotcraft (API de GitHub): https://api.github.com/repos/Vincentwei1021/video-shotcraft
- Plantilla oficial de subtítulos TikTok: https://github.com/remotion-dev/template-tiktok
- Estrellas de Remotion (API de GitHub): https://api.github.com/repos/remotion-dev/remotion
- Descargas de npm: https://api.npmjs.org/downloads/point/last-month/remotion · https://api.npmjs.org/downloads/point/2025-09-13:2025-10-12/remotion · https://api.npmjs.org/downloads/point/2024-09-13:2024-10-12/remotion

**Marketplaces de plantillas y su distribución de ventas**
- VideoHive "subtitles" por ventas (páginas 1, 6, 12, 18 y 26): https://videohive.net/search/subtitles?sort=sales
- VideoHive "subtitles", últimos 12 meses: https://videohive.net/search/subtitles?date=this-year&sort=sales
- VideoHive Premiere Pro, últimos 12 meses: https://videohive.net/category/premiere-pro-templates?date=this-year&sort=sales
- Envato Elements, precios: https://elements.envato.com/pricing
- Comisión del 50% en Envato (Purethemes, 2026-07-02; conflicto de interés): https://purethemes.net/envato-author-exclusivity-merchant-of-record/
- Pausa de autores y regla de IA en Envato (Payhip, competidor): https://payhip.com/hub/what-is-envato/
- Pago por descarga en Elements (blog, no confiable): https://earnifyhub.com/blog/motion-array-vs-envato-elements-subscription
- Motion Array, regalías (no pude abrirla; resumen del buscador): https://artists.motionarray.com/en/articles/5836981-how-will-i-earn-royalties-as-a-motion-array-artist
- Motion Array, alta de autores (error 403): https://motionarray.com/become-a-producer/
- Compra de Motion Array por Artlist (2020): https://rightstech.com/2020/12/artlist-acquires-digital-assets-marketplace-motion-array-for-65m/
- Canva Creators (vía buscador): https://www.canva.com/help/canva-creators-program/
- Gumroad, estadísticas estimadas (actualizado al 2026-10-08): https://profitable.app/gumroad/stats
- Gumroad, InsightRaider (método débil): https://insightraider.com/en/data/gumroad-statistics-2026
- Etsy, blog con conflicto de interés (descartado): https://digitalbizplr.com/blogs/learn/best-digital-products-sell-etsy-2026

**Herramientas y precios**
- Submagic: https://www.submagic.co/pricing
- OpusClip: https://www.opus.pro/pricing
- Descript: https://www.descript.com/pricing
- CapCut: https://www.capcut.com/pricing
- Canva (la página oficial dio error 403; precios de terceros): https://piktochart.com/blog/canva-pricing-2026-costs-raised/ · https://costbench.com/software/design/canva/free-plan/

**Servicios de edición**
- 99dollarsocial: https://www.99dollarsocial.com/short-form-video
- Kimp: https://www.kimp.io/unlimited-video-editing/
- Tasty Edits (competidor): https://www.tastyedits.com/unlimited-video-editing-the-subscription-trap/
- Fiverr Go (2025-02): https://www.fiverr.com/news/fiverr-go · https://techcrunch.com/2025/02/18/fiverr-wants-gig-workers-to-offload-some-of-their-work-to-ai

**Cobro desde Argentina**
- Polar, países: https://polar.sh/docs/merchant-of-record/supported-countries
- Polar, qué se puede vender: https://polar.sh/docs/merchant-of-record/acceptable-use
- Polar, comisiones: https://polar.sh/docs/merchant-of-record/fees
- Paddle, países: https://www.paddle.com/help/start/intro-to-paddle/which-countries-are-supported-by-paddle
- Paddle, qué no se puede vender (actualizada el 2026-04-13): https://www.paddle.com/help/start/intro-to-paddle/what-am-i-not-allowed-to-sell-on-paddle
- Paddle, pagos (vía buscador): https://www.paddle.com/help/manage/get-paid/when-and-how-do-i-get-paid · https://www.paddle.com/help/manage/get-paid/is-there-a-fee-taken-for-payouts
- Gumroad, comisiones: https://gumroad.com/pricing
- Gumroad y Argentina (fuentes contradictorias): https://wise.com/us/blog/gumroad-fees · https://www.dreamgrow.com/payment-processing-payouts-and-paypal-a-chance-for-creators-to-thrivecart-at-the-end-of-the-gumroad/
- Lemon Squeezy, estado 2026 (2026-01-28): https://www.lemonsqueezy.com/blog/2026-update
- Stripe Managed Payments, países y productos: https://docs.stripe.com/payments/managed-payments/eligibility

**Estudios internos usados (no re-verificados hoy, salvo lo indicado)**
- `research/2026-10-02-video-foto-133-ideas.md` (Vidchops, Upwork, editores argentinos, puntaje 4,5 de T19)
- `research/fuentes/2026-10-02-video-herramienta-autoedicion.md` (costos de Remotion Lambda, % automatizable por formato, Agent Skills de Remotion, licencias de stock)
- `research/fuentes/2026-09-02-productos-digitales.md` y `research/fuentes/2026-09-02-microsaas-productos-dev.md` (Payoneer, Paddle, Gumroad)
- `research/fuentes/2026-10-01-rapidas-digital-gigs-ia.md` (plazos de cobro de Gumroad y Lemon Squeezy)
