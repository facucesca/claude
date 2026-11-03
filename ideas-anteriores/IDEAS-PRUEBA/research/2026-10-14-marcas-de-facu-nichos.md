# Lo que marcó Facu en NICHOS-Y-PROBLEMAS (2026-10-14)

**Fuente:** marcas de Facu en la hoja "Problemas" de `NICHOS-Y-PROBLEMAS.xlsx` (leídas el 2026-10-14; respaldo en `research/datos/archivo/2026-10-14-NICHOS-Y-PROBLEMAS-marcado-por-Facu.xlsx`; extracción completa en `research/datos/2026-10-14-marcas-facu-nichos.json`).
**Convención de Facu:** amarillo = me gustó; celeste = me llamó más la atención; la nota va en la columna "Me gusta"; las ideas nuevas las escribió al fondo.
**Búsquedas de verificación:** 12, hechas el 2026-10-14 para contestar los "no sé si existe" de sus notas. Fuentes al final.

---

## 1. Qué marcó (datos)

- **25 de 173 problemas**: 22 amarillos y 3 celestes (SER-4-4, EDU-1-4, EDU-5-3). Más una nota sin color (EDU-2-1) y **3 ideas nuevas** al fondo.
- **Sus marcas casi no coinciden con el puntaje de los investigadores:** promedio 16,8 contra 18,0 de todas; **solo 1 de sus 25 está en el top 30** (LOG-1-4, puesto 2, y la anotó como "medio flojo y complicado"). Las demás están del puesto 35 al 169.
- **El patrón CEMEVA (papeles hechos a mano) aparece en 8 de sus 25 marcas (32%)**, contra 99 de 173 en el Excel (57%).

## 2. Qué dicen sus marcas (opinión de Claude)

Hay tres gustos claros. (El punto 4 era una lectura mía equivocada: Facu la corrigió en el chat; ver la sección 7.)

1. **Tecnología del mundo físico: cámaras, RFID, rastreadores, sensores, fotos que la IA interpreta.** Es el gusto más fuerte: SER-4-4 y EDU-1-4 (los dos celestes con RFID), EDU-2-1, EDU-1-5, COM-2-4, COM-4-4, ALI-4-4, COM-3-5, CON-2-3 (dron), AGR-4-2 (collares), AGR-4-4, y 2 de sus 3 ideas nuevas. **No es nuevo:** ya estaba en L10 (cámara en el súper, 2026-10-08), en X1d (pick-to-light, marcado el 2026-10-07) y en el "Jarvis holográfico" (2026-09-10). Un interés que vuelve durante un mes es una señal seria.
2. **Apps que conectan a dos partes (intermediarios):** SAL-4-2 (enfermeros), SAL-5-2 (compradores y proveedores B2B), AUT-1-2 (repuestos cerca), EDU-5-3 (profesores, celeste), ALI-2-2. También estaba en L1, L6 y en la idea de escrow (A1).
3. **Que las cosas "estén en regla" en alimentos caseros** (ALI-2-4, ALI-2-5, ALI-3-2: "falta de regulación").
4. ~~Lo que NO le atrae: automatizar papeles de oficina.~~ **Corregido por Facu (chat, 2026-10-14):** sí le atrae automatizar papeles y todo lo de mejora de procesos de ingeniería industrial. Lo que no quiere es el trabajo **a medida, empresa por empresa** ("cada caso de cada empresa es un mundo, una gran inversión de tiempo"): busca **algo más global**. Que casi no haya marcado facturas o liquidaciones se explica por eso, no por el tema.

**Riesgos de cada gusto (opinión):**
- **Hardware** (RFID, collares, drones, sensores): más capital, stock, importación, instalación y soporte en el lugar. Posible homologación de equipos de radio (ENACOM) y reglas para drones (ANAC): **no lo verifiqué**, hay que confirmarlo antes.
- **Intermediarios de dos lados:** hay que conseguir oferta y demanda a la vez. En casi todos sus casos ya hay alguien local (ver sección 3).

**El puente que veo (opinión):** **software que interpreta el mundo físico usando equipos que el cliente ya tiene** (las cámaras del local, el celular). Es tecnología física, que es lo que le gusta, pero se construye como software con Claude, que es lo que ya sabe hacer, y casi sin capital. Ejemplo verificado: Veesion detecta robos usando las cámaras que el comercio ya tiene (Perfil; Forbes Argentina).

## 3. Respuesta a cada nota

| ID | Lo que propuso Facu | Qué existe (dato, con fuente en la sección 6) | Opinión de Claude |
|---|---|---|---|
| **SER-4-4** ⭐ | Ausentismo con RFID: tarjeta en la billetera, lector en la entrada, la IA saca los comprobantes, barato | **Ya existe y es común:** relojes de fichaje con huella, PIN o tarjeta se venden en Argentina (GeoVictoria); hay software gratis (Jibble); terminales con RFID desde ~US$ 82-85 FOB en mayoristas chinos | El RFID para fichar no tiene hueco. Lo que sí podría tenerlo es la otra mitad de la fila: **validar certificados médicos con IA** (afuera MedHelp). Hay un posible "por qué ahora", el Decreto 407/2026 de certificados electrónicos, **no verificado** en el Boletín Oficial |
| **EDU-1-4** ⭐ | RFID en la ropa o credencial y sensores en cada puerta para jardines y colegios con pileta: saber si falta alguien | **No encontré** un producto así en Argentina. Afuera hay patentes y trabajos académicos (lectores en la puerta del aula) y sistemas que avisan a los padres. El caso local más cercano: Efesur (Bariloche), pulseras RFID en viajes de egresados | **Lo más original de tus notas.** Detectar al pasar por una puerta exige etiquetas de lectura a distancia (UHF), no las de "apoyar la tarjeta". Riesgos: datos de menores (Ley 25.326, consentimiento de padres, **a verificar**) y, sobre todo, **responsabilidad**: si el sistema falla y un chico sale, ¿de quién es la culpa? Antes de construir nada hay que hablar con 5-10 directoras de jardín |
| **EDU-5-3** ⭐ | App para profesores particulares: coordinar clases, pagos anticipados, turnos | Superprof opera en Argentina como marketplace con suscripción (hay muchas quejas públicas por cómo cobra). **No encontré** una app local de agenda + cobro anticipado. Afuera: TutorBird, TutorCruncher. Precio de referencia: $45.000-120.000 por hora (comparador, abril 2026) | Es la más barata y rápida de construir con Claude. Riesgo: **ticket chico** (cada profe paga poco), lo que choca con tu "no achicar ideas". Mejor si apunta a academias e institutos (EDU-2-1) |
| SAL-4-2 | "PedidosYa de enfermeros" | Afuera Homage y Papa. Acá: Cuidarlos (app para **gestionar** un cuidador que ya tenés, no para buscarlo), agencias (Mayores Cuidadores) y avisos sueltos | Hay hueco de marketplace, pero con matrículas, responsabilidad médica e informalidad laboral |
| SAL-5-2 | Un mercado B2B de compradores y proveedores, con "una vuelta de tuerca" | **Mercado Libre Negocios** ya existe (lanzado en 2025, 2,6 millones de productos mayoristas según la empresa), además de Markley y Compre Ahora | El B2B general es pelear contra Mercado Libre: no. La vuelta de tuerca tiene que ser un **rubro puntual** (como Vetcove con veterinarias) |
| ALI-2-2 | Como las apps de comida que sobra, pero con todo lo desechable | Cheaf ya tiene más de 700 comercios en Argentina | Coincido con tu duda: bajo |
| ALI-2-4 | App de cálculo nutricional y etiquetado para casas de comida casera | **ANMAT ya tiene una calculadora oficial y gratis** de sellos (Disposición 2673/2022). Y el Poder Ejecutivo mandó al Senado un proyecto para **derogar** la Ley 27.642 (no confirmé si se aprobó) | Como herramienta para cumplir la ley es débil: la versión oficial es gratis y la ley puede caer. Tu pregunta "¿cómo sé qué tan sano es?" es otro producto: **transparencia para el que compra**, no cumplimiento |
| ALI-2-5, ALI-3-2 | "Más de lo mismo: falta de regulación" | Afuera FoodDocs, Ekos | Juntaría las tres (con ALI-2-4) en "orden sanitario para productores chicos de alimentos". La bromatología es municipal y el control varía mucho |
| ALI-4-4 | Foto de la fruta y la IA dice qué tan buena está | Es exactamente lo que hacen Clarifresh e Intello Labs | Técnicamente posible con los modelos de visión actuales, pero hay que juntar miles de fotos etiquetadas. El que paga es un empacador o exportador, no un verdulero |
| COM-3-5 | Foto de un tornillo sobre una regla: la IA lo identifica, lo mide y dice dónde está (con pick-to-light) | Identificar piezas por foto es lo que hacen nyris y Partium | La regla como referencia de medida es una muy buena idea. Se puede empezar **solo con software** (identificar y devolver el código) y dejar el pick-to-light (hardware) para después |
| CON-2-3 | App con cálculos por rubro, dron o celular para medir la casa | Hover mide la casa con fotos del celular | La versión con celular es software; el dron suma hardware y permisos (ANAC, **a verificar**) |
| AUT-1-2 | Encontrar repuestos y stock en negocios cercanos | Acá existen Autominuto (pedís presupuesto y te responden por mail) e Inforepuestos (directorio). **No encontré** stock en vivo. Afuera PartsTech | El problema real es conseguir el stock de cada casa de repuestos (cada una usa su sistema). Es marketplace más integración |
| SER-4-5 | Base de datos de antecedentes | **Ya existe:** HireRight compró Inquiro Vitae (con sede en Argentina) y está Referencias Laborales | Bajo hueco; además necesita consentimiento del candidato (Ley 25.326, **a verificar**) |
| EDU-1-5 | Rastreadores en la combi escolar | Afuera Here Comes the Bus, SafeStop. Acá no apareció nada en la 2.ª pasada | **Casi sin hardware:** el celular del chofer comparte la ubicación y los padres miran la app. Rápido de probar. ¿Quién paga: el transportista o los padres? |
| EDU-2-1 | RFID en el gimnasio + sensor de luz para detectar colados | — | Creo que esto ya existe en control de acceso profesional ("antipassback"), pero **no lo verifiqué** |
| EDU-3-1 | "No sé si descartarlo: predecir con tantos datos es complicado" | — | Coincido: descartar por ahora. Además, vender a universidades es lento y muchas usan SIU-Guaraní |
| EDU-3-2 | "IA que compare programas: ya debe existir" | Afuera sí (DegreeSight, TES); acá no apareció | Existe afuera, no acá. El cliente es la universidad (venta lenta) |
| AGR-4-2 | Alambrado virtual: collares con descarga, carga solar y rastreador | **Es exactamente Halter y Nofence** (la misma fila). Halter tiene sitio para Argentina y Uruguay; la 2.ª pasada indicó que todavía no vende acá | Buena intuición: llegaste solo a lo que funciona afuera. Pero competir es hardware pesado y con mucho capital: no para la etapa 1 |
| LOG-1-4 | "Unificar pedidos con IA en una sola plataforma; medio flojo" | Vooma, HappyRobot afuera; nada acá | Es la mejor puntuada y la más cercana a CEMEVA, pero no te entusiasma. La dejo como referencia |

Sin nota, pero marcadas: LOG-3-4 (productividad en depósito), COM-2-3 (fiado), COM-2-4 (robos hormiga), COM-4-4 (conteo de gente), IND-4-4 (cajas a medida), AGR-4-4 ("tal vez").

**Algo que se repite y vale la pena decirlo:** en 6 de tus notas (ALI-4-4, COM-3-5, CON-2-3, AGR-4-2, LOG-1-4, EDU-5-3), la solución que imaginaste es casi la misma que ya funciona afuera. Es buena señal: tu intuición apunta a cosas que la gente paga. Y es lo que buscábamos: no inventar, sino adaptar lo que ya funciona.

## 4. Las 3 ideas nuevas (con la Regla N.º 2)

| Idea | ¿Está repetida? | Qué existe | Opinión |
|---|---|---|---|
| **L11.** Plataforma de aprendizaje confiable (contra la información dispersa y los vendedores de cursos baratos) | **Nueva.** Las 633 tenían decenas de ideas de *vender cursos*, pero ninguna de *ordenar y certificar* lo que se enseña | Afuera, Class Central se presenta como "un Tripadvisor de la educación online": reseñas propias y cobra comisión cuando alguien se anota a un curso (según su página "About"). Un perfil de terceros dice que ayudó a 4 millones de personas (no verificado) | La confianza tarda años en construirse y las comisiones de afiliado en Argentina son chicas. Mejor como proyecto a largo plazo o de marca que como negocio de la etapa 1 |
| **L12.** Cámaras de seguridad con IA en Argentina | **No es nueva:** junta L10 (tu idea del súper), COM-2-4 (robos hormiga) y COM-4-4 (conteo de gente). La anoto como el **territorio** que las une | Veesion (Francia, opera en Iberoamérica, usa las cámaras existentes); Sumato ID (**argentina**, desde 2013, analítica de clientes con las cámaras existentes); KSI Vision (Uruguay); Batech (México, apunta al robo hormiga); Irisity + Intel (seguridad pública, Vicente López) | Hay jugadores, pero **no encontré a nadie local enfocado en robo hormiga para autoservicios chicos** (la búsqueda fue limitada) |
| **L13.** RFID para otras cosas, stickers lindos, algo distinto | **Nueva** (no había nada de RFID) | — | Ojo: es una tecnología buscando un problema, justo lo que el método de "notar, no inventar" (Graham, 2012) dice evitar. Los problemas concretos donde a vos te sirvió el RFID ya están: EDU-1-4, SER-4-4 y EDU-2-1. La uniría a ellos |

## 5. Propuesta de finalistas (opinión, para discutir)

Cruzando tus marcas con la hoja "Fase 2" (tus favoritas eran L1, L6, L9 y L10), salen **3 territorios** que te atraen y **8 finalistas**:

**Territorio A — "Ojos": IA que interpreta imágenes, con cámaras o celulares que ya existen** (agrupa L10, L12, COM-2-4, COM-4-4, COM-3-5 y ALI-4-4)
1. **Robos hormiga en autoservicios con las cámaras que ya tienen** (COM-2-4). La pérdida se mide en plata. Veesion dice detectar entre 10 y 15 robos por semana por local (cifra de la empresa, nota de 2023).
2. **Identificar una pieza por foto sobre una regla** en ferreterías y casas de repuestos (COM-3-5, con AUT-1-2).
3. **Calidad de fruta por foto** para empacadores (ALI-4-4).

**Territorio B — "Presencia": saber dónde está cada persona** (agrupa L13, EDU-1-4, EDU-1-5, SER-4-4 y EDU-2-1)

4. **Seguridad de chicos en jardines y colegios** (EDU-1-4).
5. **Combi escolar con seguimiento** desde el celular del chofer (EDU-1-5).

**Territorio C — "Conectar": apps entre dos partes** (agrupa L1, L6, SAL-4-2, SAL-5-2 y EDU-5-3)

6. **App de gestión y cobro para profesores particulares y academias** (EDU-5-3, con EDU-2-1).

**De la hoja "Fase 2":**

7. **L9, diagnóstico de stock**: era la mejor puntuada de tus ideas (6/10) y usa lo de Sporting.

**De referencia:**

8. **LOG-1-4, pedidos de flete por WhatsApp**: la mejor puntuada del Excel y la más parecida a CEMEVA, aunque no te entusiasma.

**Próximo paso propuesto:** que elijas 2 o 3 de estas 8. Para esas hago una búsqueda a fondo de la competencia en Argentina y de cuánto paga hoy el cliente, y armamos 5 conversaciones con clientes reales por idea (método The Mom Test: preguntar por el pasado, no "¿lo usarías?"). Con eso elegís UNA, con pérdida máxima y fecha de corte.

## 6. Fuentes (búsquedas del 2026-10-14)

- Reloj de fichaje con tarjeta en Argentina: [GeoVictoria Argentina](https://www.geovictoria.com/es-ar/marcaje/reloj-control/); software gratis: [Jibble](https://www.jibble.io/es/mejor-software/sistemas-control-asistencia-rfid); terminales: [Made-in-China](https://es.made-in-china.com/category23_Security-Protection/Access-Control-System_963.html) (precios FOB, sin impuestos).
- RFID en aulas: [patente USPTO 8353705](https://image-ppubs.uspto.gov/dirsearch-public/print/downloadPdf/8353705); pulseras RFID en viajes de egresados (Efesur): [InfoNegocios](https://infonegocios.info/y-ademas/rfid-para-cuidar-adolescentes).
- Antecedentes laborales: [HireRight compra Inquiro Vitae](https://www.hireright.com/company/newsroom/hireright-adquiere-inquiro-vitae-y-fortalece-su-oferta-en-latinoamerica); [Referencias Laborales (La Gaceta)](https://www.lagaceta.com.ar/nota/1110825/economia/referencias-laborales-sitio-se-puede-consultar-datos-postulantes.html).
- Cámaras con IA: Veesion en [Perfil](https://www.perfil.com/noticias/modo-fontevecchia/la-startup-que-detecta-gestos-sospechosos-de-robo-en-supermercados-modof.phtml), [Forbes Argentina](https://www.forbesargentina.com/innovacion/desarrollan-software-detecta-gestos-sospechosos-hurto-supermercados-n33239/amp) e [iProfesional (2023)](https://www.iprofesional.com/tecnologia/380616-inteligencia-artificial-para-detectar-robos-en-tiempo-real); [Sumato ID](https://www.descubre.vc/sumato-id); [KSI Vision (Forbes Argentina)](https://www.forbesargentina.com/negocios/ksi-vision-startup-uruguaya-analiza-comportamiento-tiendas-conquisto-clientes-como-inditex-mango-falabella-n73108); [Batech](https://www.descubre.vc/batech); [Irisity + Intel](https://dplnews.com/?p=231755).
- Etiquetado frontal: [Disposición ANMAT 2673/2022](https://www.argentina.gob.ar/normativa/nacional/norma-363374/texto); proyecto de derogación: [Derecho en Zapatillas (2026)](https://www.derechoenzapatillas.com/2026/los-octogonos-negros-vuelven-al-congreso-que-pasa-con-la-ley-de-etiquetado-frontal/).
- Repuestos: [Autominuto (Autotest)](https://autotest.com.ar/noticias/autominuto-com-la-solucion-para-resolver-todo-lo-que-necesitas-para-tu-auto/); [Inforepuestos (16 Válvulas)](https://www.16valvulas.com.ar/inforepuestos-para-una-busqueda-de-nuestros-repuestos/).
- Profesores particulares: [Superprof en Trustpilot](https://ca.trustpilot.com/review/superprof.com.ar); [reclamo sobre cobro de Superprof](https://tuquejasuma.com/superprof-argentina/reclamos/suscripcion-mal-cobrada-no-hay-telefono-de-reclamo); [precios, Cuánto Me Cuesta (abril 2026)](https://cuantomecuesta.com/ar/clases-particulares/).
- Cuidadores: [Cuidarlos (App Store)](https://apps.apple.com/ar/app/cuidarlos/id1458778617); [Mayores Cuidadores](https://www.idealist.org/es/empresa/2a3d240947bb433d9fee659f93f0051b-mayores-cuidadores-buenos-aires).
- B2B: [Mercado Libre Negocios (Mercado)](https://mercado.com.ar/negocios/mercado-libre-introduce-mercado-libre-negocios-plataforma-exclusiva-para-operaciones-b2b-en-argentina); [Markley](https://www.descubre.vc/markley).
- Aprendizaje: [Class Central, About](https://classcentral.com/about).

## 7. Correcciones y agregados de Facu en el chat (2026-10-14)

1. **Etapa del trabajo:** "esto es una primera instancia: buscamos oportunidades, analizamos y descartamos. Aún no empezamos." Juntando todo se empieza a ver qué onda.
2. **Papeles y mejora de procesos: sí le atraen** (corrige el punto 4 de la sección 2). Lo que evita es lo **a medida por empresa**; busca una idea **global**.
   - Opinión de Claude: las soluciones de afuera de esa familia (Conexiom, MarginEdge, Loop) son globales justamente porque hacen **un solo proceso, para un solo tipo de cliente, con el mismo software para todos**. Así es como "automatizar papeles" deja de ser "cada empresa es un mundo". Sirve como criterio de filtro: *¿es un producto igual para muchos clientes o es trabajo a medida?*
3. **Profesores particulares (EDU-5-3): le gusta mucho.** Lo ve como un rubro poco regulado para entrar como intermediario. Su versión: que nadie se clave con clases (ni alumnos ni profesores); **la app retiene el pago hasta que todos dan por concluida y puntuada la clase**; reseñas, comentarios, seguridad, puntuación y bonos; después, publicidad y suscripciones. **"Que sea el Instagram de profesores particulares."**
   - Opinión de Claude, a verificar: el rubro de las clases está poco regulado, pero **retener la plata de terceros sí lo está** en Argentina (custodia de fondos, BCRA Com. A 6859; ver la ficha de escrow A1). Habría que resolverlo con un procesador de pagos habilitado en vez de custodiar el dinero propio.
4. **RFID:** si ya está muy usado se descarta (en empresas, fichar con tarjeta es común), pero **no lo ve en colegios ni instituciones**. Por ahora son datos: se decide más adelante si se descarta.
5. **Idea nueva L14, stock de piezas chicas:** mercerías, bulonerías, ferreterías y multimarcas. Siente que hay sistemas para ordenar, pero no uno definitivo ni dominante. Quiere algo muy bien desarrollado, muy ordenado, adaptable a cualquier comercio, que además evite robos y controle todo. Pidió dejar anotado cómo podría ser la tecnología ("¿por peso? ¿cómo?").
   - Regla N.º 2: **parecida**. Une COM-3-5 (pieza por foto, que marcó), COM-3-3 (conteo de miles de ítems chicos; repetía K14), X1/X1d (Orden Operativo, pick-to-light), L9 (diagnóstico de stock) y L10 (stock con cámara). Lo nuevo es el foco en comercios de piezas chicas y el control por peso y contra robos.
   - Tecnologías a evaluar más adelante (ideas, **sin verificar**): balanzas cuentapiezas (cuentan por peso unitario); estantes o cajones con sensores de peso que avisan faltantes y retiros; identificar por foto (pieza sobre una regla); código en cada cajón + pick-to-light; cámaras contra robo. Ojo: el RFID suele andar mal con piezas metálicas chicas (a verificar).
   - Opinión: es su interés más constante desde septiembre (Orden Operativo, Sporting, pick-to-light, L9, L10, COM-3-5) y junta ingeniería industrial con tecnología física.
6. **Guardado en el Excel de ganadores:** hoja "Fase 2" de `TODAS-LAS-IDEAS.xlsx`, sin tocar lo anterior. Bloque C: 26 ganadores de este Excel (3 celestes, 22 amarillos y EDU-2-1 sin color pero con nota). Bloque D: 4 ideas nuevas (L11-L14). **Total en Fase 2: 10 + 33 + 26 + 4 = 73.** Script: `research/datos/add_fase2_nichos.py`; respaldo previo en `research/datos/archivo/2026-10-14-TODAS-LAS-IDEAS-respaldo.xlsx`.

## 8. Idea nueva L15: intercambiar efectivo por transferencia (chat, 2026-10-14)

**La idea de Facu:** puntos donde alguien deja efectivo y recibe una transferencia, o al revés. La plata pasa por una cuenta de la app, que la libera cuando se completa el intercambio. Él mismo dice: "medio rebuscado, no creo que funcione, pero se me ocurrió".

**Regla N.º 2:** nueva, pero parecida a A1 (escrow), porque la app custodia la plata hasta que la operación se completa.

**Qué existe hoy (datos, búsquedas del 2026-10-14):**
- **De efectivo a digital:** Mercado Pago genera un código para cargar efectivo en Rapipago, Pago Fácil y Cobro Express. Comisión del 1,5% al 3% y tope de $1.000.000 por mes según [Ámbito (2025)](https://www.ambito.com/economia/ingresa-dinero-mercado-pago-todas-las-opciones-disponibles-y-el-paso-paso-n6116970).
- **De digital a efectivo:**
  - Mercado Pago "Sacar": con QR en comercios como Carrefour, Coto, Día y Diarco, o en Rapipago con código y DNI. Hasta $200.000 por operación según una nota de agosto de 2026 ([TodoJujuy](https://www.todojujuy.com/como-retirar-efectivo-billeteras-virtuales-el-fin-semana-largo-n287657); [iProfesional](https://www.iprofesional.com/finanzas/388263-mercado-pago-te-permite-extraer-efectivo-como-podes-hacerlo)).
  - Visa **Extracash**: más de 2.500 puntos, entre ellos Coto, Carrefour, Farmacity y La Anónima ([Mercado](https://mercado.com.ar/protagonistas/los-socios-visa-podran-extraer-dinero-en-efectivo-de-las-cajas-de-comercios); [Canal 26, 2026-04-30](https://www.canal26.com/economia/2026/04/30/tres-dias-sin-bancos-las-alternativas-a-los-cajeros-automaticos-para-conseguir-efectivo-durante-el-fin-de-semana-largo/)).
  - También Mastercard Cash Plus y los comercios con Payway.

**Opinión de Claude:** para descartar, por tres motivos.
1. **La necesidad ya está cubierta** por redes con miles de puntos. Además, en esas redes **el comercio ya es el "punto de intercambio" que imagina Facu**: cambia el efectivo que le sobra por tu dinero digital. La intuición era correcta, pero ya existe.
2. **Lo propio de la idea es lo más difícil:** custodiar plata de terceros está regulado (BCRA Com. A 6859, según la ficha A1), y manejar efectivo implica prevención de lavado ante la UIF (no verificado en esta sesión).
3. **Riesgo físico:** robo y billetes falsos en los puntos.

Queda anotada en la hoja "Fase 2" (bloque D) y en el registro. **Total en Fase 2: 74.**
