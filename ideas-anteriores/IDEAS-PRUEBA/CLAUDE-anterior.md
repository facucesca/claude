# IDEAS-PRUEBA — El camino de Facu a su propia empresa

## REGLA N.º 1 — Nada inventado (pedido explícito de Facu, 2026-10-06)

- **Nunca inventar datos, cifras, fuentes, citas, nombres ni resultados.** Si no lo sé, digo "no lo sé". Si no lo pude verificar, digo "no lo pude verificar". Si no puedo hacer algo, lo aclaro.
- Separar siempre tres cosas: **dato verificado** (con fuente y fecha), **estimación propia** (marcada como tal, con el razonamiento) y **opinión** (marcada como tal).
- No dar la razón por dar la razón: si Claude no está de acuerdo con Facu, lo dice y explica por qué, con datos.
- Si un documento previo de este proyecto tiene un dato dudoso o sin fuente, se marca como tal en vez de repetirlo.

## REGLA N.º 2 — No repetir ideas entre investigaciones (pedido explícito de Facu, 2026-10-13)

Cada investigación nueva tiene que traer cosas nuevas. Nada que ya se haya investigado vuelve a aparecer como si fuera nuevo.

- **Registro único:** `research/datos/registro-de-ideas.csv` tiene todo lo ya investigado (las 633 de `TODAS-LAS-IDEAS.xlsx`, las ideas propias de Facu de la hoja "Fase 2" y los problemas de `NICHOS-Y-PROBLEMAS.xlsx` y `NICHOS-Y-PROBLEMAS-2.xlsx`). Se regenera con `python research/datos/build_registro.py`.
- **Vale para todo, ganadores y rechazados** (pedido de Facu, 2026-10-14: "no quiero volver a rechazar"). La columna `decision_facu` del registro dice qué eligió y qué no. Nada de eso vuelve a proponerse, y algo **parecido a una idea que no eligió o descartó tampoco vuelve**. Solo puede quedar algo parecido a un ganador, marcado como variante.
- **Antes de investigar:** leer el registro y pasárselo a cada investigador como lista de exclusión: "no propongas nada que ya esté acá; si encontrás datos nuevos sobre algo de la lista, anotalos como dato de esa idea, no como fila nueva".
- **Después de investigar, antes de entregar:** cruzar fila por fila contra el registro (primero automático por palabras, después a mano):
  - **Repetida** = mismo problema y mismo tipo de cliente que algo anterior, aunque antes estuviera planteado distinto (por ejemplo, como servicio). Sale de la lista principal; sus datos nuevos se guardan aparte con la referencia a la idea vieja (no se pierden).
  - **El mismo problema en dos nichos** dentro de la misma investigación = una sola fila, con "también aparece en".
  - **Parecida** = comparte cliente o un problema vecino, pero no es la misma. Se queda, marcada con la referencia.
- **Al entregar:** decirle a Facu cuántas quedaron nuevas, parecidas y repetidas. Después, actualizar el registro.

## Propósito

**Que Facu tenga su empresa propia (sin jefe) y, con el tiempo, escale a una startup.** Se hace en dos etapas, en este orden (definido por Facu el 2026-10-06):

1. **Etapa 1 — Negocios intermedios (AHORA).** Empresa propia de producto o servicio, aprovechando la ola de la IA, para **ganar plata, experiencia y un piso económico**. Se prueban varios negocios, se equivoca, se aprende. Las ideas del Excel y de `research/` son el menú de esta etapa.
2. **Etapa 2 — Startup (DESPUÉS).** Cuando haya piso económico y experiencia, se va por algo más grande. Lo que se aprenda en la etapa 1 (clientes, industrias, problemas vistos de adentro) es la materia prima para encontrarla. Toda idea de startup que aparezca antes se anota en `ideas/` y no se pierde.

Reglas de la etapa 1 (propuestas por Claude, aceptadas o a ajustar por Facu):
- **Secuencial, no disperso:** un negocio principal a la vez y como máximo un experimento chico en paralelo. Cada uno con pérdida máxima y fecha de corte para seguir o cerrar, definidas antes de empezar.
- **Cada negocio se elige también por lo que enseña** para la etapa 2 (vender, operar, contratar, conocer una industria por dentro).
- Equivocarse vale solo si se registra qué se aprendió: cada intento cierra con un post-mortem escrito.

Los ingresos pasivos/semi-pasivos quedan como complemento, no como objetivo.

Historia: el proyecto arrancó el 2026-09-02 como "laboratorio de ingresos pasivos con IA"; se amplió a todo tipo de ingresos el 2026-09-07 y pasó a este propósito el 2026-10-05/06. Los estudios anteriores (`research/`, `TODAS-LAS-IDEAS.xlsx`) se hicieron bajo el propósito viejo: **no se descartan**; son el menú de la etapa 1 (ojo: algunos datos de esos estudios pueden ser estimaciones, revisar antes de usarlos).

El objetivo NO es velocidad, es calidad. Preferimos descartar una idea mediocre antes que endulzarla.

## Premisa del usuario (2026-10-05) — manda sobre todo lo demás

Facu tiene 22 años, está por recibirse de ingeniero industrial y **quiere tener su propio negocio: no quiere relación de dependencia** (no trabajar para otra persona). Esto es una decisión de vida, no una búsqueda de ingresos extra. Consecuencias para el trabajo:

- **Foco en negocios activos / semi-activos** que pueda construir y ser dueño; lo pasivo queda como complemento, no como objetivo.
- **Dispuesto a invertir plata, equivocarse y volver a intentar.** Equivocarse es parte del plan: "mientras más me equivoque, mejor". Por eso se valora **aprender rápido y barato** (experimentos chicos con gates claros) por encima de evitar todo error. Un fracaso barato y bien medido cuenta como resultado.
- Evaluar cada idea también por: ¿construye un **activo propio** (clientes, marca, método, producto) y no solo horas vendidas? ¿Es **independiente** (sin un único cliente/plataforma que mande)? ¿Qué se **aprende** aunque falle?
- El escepticismo sigue: arriesgar plata está bien, pero con números realistas y pérdida máxima definida de antemano por experimento.

## Pacto de trabajo (2026-10-05) — acordado entre Facu y Claude

1. **Ambición: una startup.** Facu quiere descubrir una idea, explotarla y ser el primero en algo; quiere algo grande y se siente capaz. El horizonte es construir una empresa escalable, no solo un buen ingreso. Los negocios de servicios (consultora, productora) valen como **vehículo para aprender, financiarse y validar**, no necesariamente como destino.
2. **Orden y profundidad por encima de todo.** Todo lo que hagamos se hace a fondo y con método; no se salta de etapa ni se improvisa. Si algo no está bien hecho, se rehace.
3. **Método primero, ideas después.** Antes de elegir idea definimos el método de descubrimiento y validación (se afina en las próximas sesiones). El Excel de ideas es insumo, no el plan; Facu lo revisa con calma.
4. **Escepticismo honesto sobre "ser el primero" y "algo grande".** Ser primero no es ventaja por sí solo: se verifica con evidencia de demanda (¿quién paga, cuánto, por qué ahora?, ¿qué ventaja injusta tenemos?). Claude señala los puntos ciegos aunque incomoden; la confianza de Facu es un activo, pero no reemplaza la validación.
5. **Facu responde las preguntas abiertas** (plata disponible, horas/semana, inglés, gustos, ideas marcadas en el Excel) y con eso se arma el plan.

## Cómo trabajar acá

- **Metódico y ordenado**: investigación → filtrado → decisión → plan paso a paso → ejecución → medición. No saltear etapas.
- **Todo con fuentes**: cualquier afirmación de mercado lleva fuente y fecha. Las fechas siempre absolutas (ej: "2026-09-02", nunca "hace dos meses").
- **Escepticismo por defecto**: usar números de mediana, no casos de éxito virales. Señalar survivorship bias y conflictos de interés (gurús que venden cursos).
- **Trading = software con riesgo explícito**: los bots de trading se analizan como sistemas, con datos de pérdidas retail incluidos. Nunca consejo financiero personalizado.
- **Contexto Argentina**: siempre verificar disponibilidad de la plataforma/programa y cómo se cobra desde Argentina (Payoneer, merchant of record, etc.).
- **Idioma**: documentación en español.
- Antes de tocar ideas o proyectos, leer `MEMORY.md` (estado vivo del proyecto).

## Estructura

- `CLAUDE.md` — este archivo (propósito y reglas de trabajo).
- `MEMORY.md` — memoria viva: perfil del usuario, decisiones, estado, preguntas abiertas. Actualizar en cada sesión relevante.
- `research/` — estudios de mercado, con fecha en el nombre (`YYYY-MM-DD-tema.md`).
- `ideas/` — un archivo por idea evaluada en profundidad (se crea cuando una idea pasa a evaluación seria).
- `proyectos/` — ejecución de ideas aprobadas; cada proyecto con su carpeta, su plan paso a paso y su registro de avance.

## Criterios de filtrado de ideas (score 1-10 cada uno)

> Nota (2026-10-06): estos criterios son para **negocios de ingresos / negocio puente**. Los criterios para evaluar **problemas y startups** (tamaño del problema, quién paga, por qué ahora, ventaja de Facu, escalabilidad) están pendientes de definir junto con el método.

1. **Rentabilidad realista** — mediana esperable a 6-12 meses, no top 1%.
2. **Grado de automatización** — horas humanas/semana necesarias en régimen.
3. **Capital requerido** — inicial y costos mensuales.
4. **Tiempo hasta el primer dólar**.
5. **Riesgo** — dependencia de plataforma, cambios de políticas, legal, baneos, saturación.
6. **Durabilidad 2026+** — ¿sobrevive a cambios de algoritmos/políticas/IA de otros?
7. **Fit con el stack** — dev solo + Claude Code + APIs de IA (+ herramientas ya conectadas, ver MEMORY.md).

> Nota (2026-09-07): para ideas **activas** (servicios), el criterio 2 mide pasividad, no calidad — no se las castiga por diseño. Evaluarlas por rentabilidad/tiempo/fit y por su potencial de productizarse hacia semi-pasivo.

## Estado

- 2026-09-02: arranque del proyecto. Primer estudio de mercado en `research/`.
- 2026-09-07: se me ocurrió una idea nueva — consultora de mejora de procesos + automatización con IA (auditorías de eficiencia para PyMEs). Es negocio de *servicios* (no pasivo), así que se evalúa aparte. Ficha: `ideas/2026-09-07-consultora-mejora-procesos.md`. Decisión de foco pendiente.
- 2026-10-01: el usuario aclara que **no sabe programar**. Estudio de 230 ideas (`research/2026-10-01-230-ideas-con-claude.md`): convergen en método de ing. industrial + Claude + no-code para PyMEs. Pendiente: elegir rubro de entrada y re-evaluar stack-de-datos.
- 2026-10-05: el usuario fija su **premisa de vida**: 22 años, por recibirse, quiere negocio propio sin relación de dependencia; prioriza activos, dispuesto a invertir y a equivocarse. Ver sección "Premisa del usuario". Se pasa de "buscar ingresos" a "elegir el negocio de entrada".
- 2026-10-05 (2ª): **pacto cerrado**: el objetivo es una startup grande (ser primero en algo), con orden y profundidad; primero se define el método. Ver "Pacto de trabajo".
- 2026-10-06: se reescribe el propósito (empresa propia/startup + negocio puente) y se agrega la **Regla N.º 1: nada inventado**. Facu confiesa que el Excel lo armó "de onda" y no lo leyó. Pendiente: acordar el método (propuesta de Claude en la sesión 2026-10-06) y qué hacer con el Excel.
- 2026-10-06 (2ª): Facu ordena las etapas: **primero negocios intermedios** (plata + experiencia), después startup. Se generó una shortlist de 39 ideas que Facu **rechazó el 2026-10-07** (archivada en `research/datos/archivo/`). Ahora marca en amarillo el Excel original.
- 2026-10-07: idea de Facu, intermediario de pagos seguros con el exterior (escrow), candidata a etapa 2. Ficha: `ideas/2026-10-07-intermediario-pagos-seguros.md`.
- 2026-10-08: Facu pasó 10 ideas de su libreta (L1-L10). Análisis a fondo en `research/2026-10-08-ideas-de-facu-analisis.md` + hoja "Ideas de Facu" en el Excel. Propuesta en debate: L9 "Diagnóstico de stock" (etapa 1) + validar L10 "auditoría de góndola por foto" (candidata a startup).
- 2026-10-09: las ideas propias de Facu + las 33 marcadas quedan en la hoja "Fase 2" del Excel, en pausa por decisión de Facu.
- 2026-10-13: Excel nuevo **`NICHOS-Y-PROBLEMAS.xlsx`**: 250 problemas (10 nichos × 5 especialidades × 5), cada uno con 2 soluciones verificadas afuera, presencia en Argentina, puntajes y familia transversal. Síntesis: `research/2026-10-13-nichos-y-problemas.md`. Facu lo marca; después se cruza con "Fase 2" para llegar a 5-10 finalistas y elegir UNA.
- 2026-10-13 (2ª): limpieza de repetidas a pedido de Facu: de 250, 65 repetían ideas anteriores (hoja "Ya estaban antes") y 12 se fusionaron → **quedan 173 únicas (114 nuevas + 59 parecidas)**. Nace la **Regla N.º 2 (no repetir)** y el registro `research/datos/registro-de-ideas.csv`.
- 2026-10-14: Facu marcó el embudo (25 problemas + ideas nuevas L11-L15). Le atraen la tecnología del mundo físico (cámaras, RFID, fotos con IA), las apps que conectan dos partes y también automatizar papeles y procesos, **siempre que sea un producto global y no trabajo a medida por empresa**. Es una primera instancia (buscar, analizar, descartar). Análisis en `research/2026-10-14-marcas-de-facu-nichos.md`. Ganadores guardados en la hoja "Fase 2" de `TODAS-LAS-IDEAS.xlsx`: **74 en total** (con L15, efectivo por transferencia, descartada).
- 2026-10-14 (2ª): los 74 quedaron **ordenados** en la hoja "Orden de Claude" de `TODAS-LAS-IDEAS.xlsx` (7 criterios, opinión): 7 para indagar ya, encabezados por el territorio stock y piezas (COM-3-5, L9, L14). Búsqueda nueva "por las dudas" en otro chat con `research/PROMPT-busqueda-nueva-2026-10-14.md`.
- 2026-10-14/15: búsqueda nueva **`NICHOS-Y-PROBLEMAS-2.xlsx`**: 20 nichos nuevos, 500 problemas → tras la limpieza contra TODO el registro (ganadores y rechazados) **quedan 365 (212 nuevas + 153 parecidas a ganadores)**. Familia más fuerte: rastreo de activos que se pierden. Síntesis: `research/2026-10-14-nichos-y-problemas-2.md`. Facu lo marca.
- 2026-10-15: indagación a fondo de las 15 ideas que pasó Facu → **3 primeras** (idea integral de stock para piezas chicas; profesores con pago protegido; Papá Noel como caja de temporada) y el resto **pendientes**. Síntesis: `research/2026-10-15-indagacion-ganadores.md`; hoja "Primeras y pendientes" en `TODAS-LAS-IDEAS.xlsx`.
- 2026-10-18: **Gimnasio de ideas** (pedido de Facu: material para aprender a ver negocios, no la idea ganadora). 43 agentes: lentes de sus 10 libros de startup (140 lentes, 91 semillas, 149 advertencias), 30 patrones de intermediación y paquete, contraste de 89 empresas EE.UU./otros vs Argentina, y 191 ideas web → **113 vivas (79 nuevas + 34 parecidas a elegidas)**, 78 salieron (37 repetidas, 41 duplicadas). Entregables: `GIMNASIO-DE-IDEAS.xlsx` (raíz) + `research/2026-10-18-gimnasio-de-ideas.md`. Registro: 1.402 → 1.515 filas (decisión de Facu pendiente). Limitación: el cupo de búsqueda web se agotó a mitad; la mitad de las fichas dice "no verificado" en Argentina.
- 2026-10-19: **Gimnasio de ideas, versión 2** (pedido de Facu: "bien completa" sin reventar el uso). 78 agentes más: verificación web en Argentina de todas las ideas, re-verificación del contraste, segunda pasada de 4 ángulos, **18 fichas a fondo** (`research/2026-10-19-gimnasio-top-a-fondo.md`), **programa de 30 días** de lentes (`research/2026-10-19-gimnasio-programa-30-dias.md`), matriz patrón×sector y `research/LENTES-MAESTRAS.html`. Resultado: **125 vivas verificadas** (15 sin nada parecido en Argentina, 99 con algo parcial, 11 con competencia directa), 91 salieron. Registro: 1.402 → 1.527 filas (pendiente que Facu marque). Uso: la semana quedó en 17%.
- 2026-10-20: Facu marcó 8 problemas de `NICHOS-Y-PROBLEMAS-2.xlsx` (PET-1-3, SEG-3-4, HOG-3-2, ALQ-2-3, TEL-5-5, EVE-4-5, SEG-2-5, MOV-2-5), casi todos con comentario que cambia la idea. Lista y lectura en `research/2026-10-20-marcas-nichos-2.md`. Registro actualizado.
- 2026-10-21: Facu marcó el Excel del gimnasio con colores (amarillo = interesante: 25 ideas; verde = explicar mejor: 4; azul = buenísima: ninguna) y agregó 3 ideas propias al pie. Se juntó TODO lo que marcó en los 4 Excel con sus comentarios, más sus ideas propias, en **`MARCAS-DE-FACU.xlsx`** (116 filas: ideas, anotaciones y puntuación de Claude; método en la hoja «Cómo puntué»; datos y script en `research/datos/2026-10-21-marcas-todas/`). Registro actualizado.
- 2026-10-23: **MARCAS-DE-FACU.xlsx v2.** Las 116 ideas marcadas se investigaron una por una con sus comentarios (30 investigadores, 14 lotes + segunda pasada profunda de las 60 mejores): opinión, variantes, puntaje, tema, tipo, etapa y dificultad; hoja «A fondo» con competencia, regulación, números y experimento. Arriba: PET-1-3 (7,9), COM-3-5 (7,7), AUT-1-2 y LOG-1-4 (7,6), L9+L5 (7,5), L14 (7,4). Facu las clasifica y filtra; de ahí se elige con qué empezar. Datos en `research/datos/2026-10-21-marcas-todas/` (v1 guardada). Uso: la investigación costó menos de 1 punto semanal.
- 2026-10-02: investigación de video/foto con marca anónima + email frío + herramienta propia de auto-edición (`research/2026-10-02-video-foto-133-ideas.md`). Recomendación: productora B2B de contenido desde charlas (EE.UU. hispano) con motor propio. Pendiente: decisión del usuario y su nivel de inglés.
