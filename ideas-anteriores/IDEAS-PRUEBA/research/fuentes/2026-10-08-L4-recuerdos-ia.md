# L4. Revivir con IA a seres queridos (y versiones más sanas): estudio de mercado

- **Fecha:** 2026-10-08
- **Idea (en palabras de Facu):** "Revivir con IA a algunos seres queridos. Hacerlo a través de fotos o videos: nuevas fotos, nuevos videos, replicar voces, etc."
- **Etapa del proyecto:** evaluación para la etapa 1 (negocio intermedio), con una mirada aparte a si podría ser una startup (etapa 2).
- **Método:** unas 36 búsquedas web y 15 lecturas de páginas, hechas el 2026-10-08. Se llegó al **límite de búsquedas de la sesión** antes de cerrar tres puntos (ver "Qué no pude verificar", al final).
- **Etiquetas:** **[DATO]** con fuente y fecha · **[ESTIMACIÓN]** cálculo propio con el razonamiento · **[OPINIÓN]** juicio mío · **[NO VERIFICADO]** no lo pude confirmar.

> Nota de tono: es un tema de duelo. Lo que sigue habla de negocio, pero detrás de cada "cliente" hay una familia que perdió a alguien. Eso cambia cómo se vende, qué se promete y qué no se hace.

---

## 0. Resumen en 10 líneas

1. La idea tiene **tres niveles de intensidad**, con riesgos muy distintos: (A) **preservar** (restaurar, colorizar, digitalizar); (B) **homenajear** (video homenaje, foto animada sin voz); (C) **"revivir"** (voz clonada, video que habla, chatbot del fallecido). Hay un cuarto camino: (D) **grabar en vida**, cuando la persona registra su propia historia.
2. **El nivel C ya existe y le va mal en Occidente:** StoryFile entró en concurso preventivo (Chapter 11) en 2024; Eternos pivoteó en 2025 porque la demanda real no venía de gente que pensaba en la muerte; 2wai tuvo una reacción viral en contra en 2025 ("demoníaco", 22 millones de vistas); Project December perdió el acceso a OpenAI en 2021. En China sí hay un mercado pago (Super Brain dice haber hecho más de 1.000 "resurrecciones" a USD 1.400-2.800), pero con otra cultura del duelo.
3. **La evidencia científica es chica y cualitativa:** estudios de 10, 16 y 25 personas. No hay ensayos controlados. Algunos usuarios encuentran consuelo; los investigadores advierten riesgo de dependencia y de duelo trabado. En una encuesta canadiense de 2026, apenas el 6% quería seguir hablando con una versión digital de su pareja.
4. **En Argentina, legalmente:** el art. 53 del Código Civil y Comercial exige consentimiento para captar o reproducir **imagen y voz**; si la persona murió, lo dan **los herederos** (y si los del mismo grado no se ponen de acuerdo, decide un juez). No hay una ley específica sobre "resurrección digital"; hay varios proyectos sin sanción confirmada.
5. **Las plataformas son un cuello de botella:** HeyGen pide un video de consentimiento de la persona para hacer su "gemelo digital", y un muerto no puede grabarlo. ElevenLabs prohíbe replicar una voz "sin consentimiento o derecho legal". Si un negocio depende de estas herramientas y de una zona gris legal, una cuenta suspendida lo mata.
6. **Lo que sí muestra demanda paga es lo "sano" y, sobre todo, lo B2B:** los crematorios municipales del Reino Unido cobran £50-110 por un video tributo; la española Vivo Recuerdo vende pantallas de homenaje a más de 150 funerarias. Deep Nostalgia (animar fotos viejas) llegó a más de 112 millones de animaciones, pero gratis o dentro de una suscripción.
7. **Argentina:** 353.428 muertes en 2024; entre 438 y más de 1.100 empresas funerarias según la fuente; una cremación directa sale desde $955.900 (mayo de 2026). No encontré cocherías argentinas que ofrezcan un video homenaje (no quiere decir que no existan).
8. **Veredicto [OPINIÓN]:** la versión **"revivir" (C) no la recomiendo**: puntaje promedio **≈ 4/10**, con riesgo ético y reputacional alto y ninguna ventaja de Facu. La versión **"homenaje" (A+B, más un piloto B2B con cocherías)** da **≈ 5,6/10**: sirve como experimento barato de la etapa 1, con ticket bajo y techo de servicio. Como startup, lo único con cierto potencial es una **plataforma de homenaje digital B2B para funerarias en Latinoamérica**, al estilo de Vivo Recuerdo, y eso hay que validarlo primero.

---

## 1. Qué es exactamente la idea: cuatro niveles

| Nivel | Qué se entrega | Ejemplo en el mundo | ¿Hace "decir" algo nuevo al fallecido? | Riesgo ético y legal [OPINIÓN] |
|---|---|---|---|---|
| **A. Preservar** | Restaurar, colorizar, mejorar y digitalizar fotos y videos viejos | Gigs de Fiverr, apps | No | Bajo |
| **B. Homenajear** | Video homenaje con fotos y música; foto con un movimiento leve (parpadeo, sonrisa) **sin voz** | Deep Nostalgia (MyHeritage), crematorios del Reino Unido (Obitus), Vivo Recuerdo | No (se mueve, pero no habla) | Bajo-medio |
| **C. "Revivir"** | Voz clonada, video donde la persona "habla", chatbot o avatar que conversa | Project December, Seance AI, 2wai, Super Brain (China), You, Only Virtual | **Sí**: inventa palabras que la persona nunca dijo | **Alto** |
| **D. Grabar en vida** | La persona graba sus historias **antes** de morir y después se pueden consultar | HereAfter AI, StoryFile, Eternos (antes de pivotear) | No (usa sus propias palabras) | Bajo (hay consentimiento de la propia persona) |

La frase de Facu ("nuevas fotos, nuevos videos, replicar voces") apunta sobre todo al **nivel C**. Este informe lo evalúa, pero también compara A, B y D, porque la evidencia muestra que ahí está la plata con menos riesgo.

---

## 2. Parecidos en el mundo ("grief tech", "deathbots", "digital afterlife")

### 2.1 Tabla de casos

| Empresa / caso | Año | Qué hace | Plata / precio | Uso / usuarios | Estado actual | Polémica | Fuente |
|---|---|---|---|---|---|---|---|
| **Replika** (origen: bot de Roman Mazurenko) | Bot de Roman: 2015-2016; Replika: 2017 | Eugenia Kuyda armó un chatbot con los mensajes de su amigo muerto. Después lo generalizó a una app de "compañero" que **ya no** es del fallecido | [NO VERIFICADO] en esta búsqueda | [NO VERIFICADO] | Replika sigue, pero como app de compañía, no de duelo | Las fuentes no coinciden en el año de la muerte (2013 o 2015) ni en la cantidad de mensajes usados | [DATO] CBC; Light Reading; BBC Mundo vía Metro PR, 2018-10-06 |
| **Project December** (Jason Rohrer) | 2020-2021 | Chatbot de texto basado en GPT-3. Un usuario (Joshua Barbeau) "simuló" a su novia muerta, Jessica | Créditos por tiempo de conversación; "entrada por debajo de £5" (2021). El dato de "USD 10" sale de fuentes débiles | Poca tracción: Rohrer decía que costaba convencer a la gente de pagar | En 2021 dejó OpenAI y pasó a AI21 Labs o a GPT-J. Hoy el sitio sigue online, pero no pude leer sus precios | OpenAI cortó el acceso por sus reglas de uso | [DATO] The Register, 2021-09-08; webcurios, 2021-07-30; Canaltech, 2021 |
| **HereAfter AI** (James Vlahos) | 2016 o 2019, según la fuente | **Nivel D**: entrevista guiada a la persona viva; después los familiares "conversan" con sus respuestas grabadas | Directorios de herramientas: **desde USD 3,99 por mes** con 14 días de prueba; en 2023, USD 8,99 por mes. **No pude abrir la página de precios oficial** (error 404) | [NO VERIFICADO] | Activa en la App Store (descarga gratis con compras dentro de la app) | Responde solo con lo grabado; está limitado por diseño | [DATO débil] AIChief; IEEE Future Directions, 2023-08-20; futurezone.at |
| **StoryFile** | Chapter 11 el 2024-05-05 | Video conversacional grabado en vida (por ejemplo, William Shatner; usado en el memorial de Ed Asner) | Declaró USD 1,5 M de activos y **USD 10,5 M de pasivos** (otra fuente da cifras menores) | [NO VERIFICADO] | Key 7 Investment compró los activos; el concurso se desestimó a pedido de la empresa el 2025-04-30. No encontré noticias de 2026 | Quemaba caja aun con nueva financiación e ingresos, según su CEO interino | [DATO] Westfair; AI Business, 2024 y 2025-03; expediente en Inforuptcy; storyfile.com |
| **You, Only Virtual** (Justin Harrison) | Última ronda: 2022-12-28 (crowdfunding) | "Versonas" de seres queridos fallecidos | **Total levantado ≈ USD 1,24 M**; valuación estimada ≈ USD 13,23 M (estimación de Caplight, no oficial) | [NO VERIFICADO] | [NO VERIFICADO] | — | [DATO débil] Caplight |
| **Seance AI** (AE Studio) | 2023 | Chat con un ser querido a partir de un cuestionario | Gratis en acceso anticipado; **Premium USD 19,99** (voz recreada e imágenes animadas) | [NO VERIFICADO] | La página sigue con "avisanos cuando lancemos" (acceso anticipado) | Su propia FAQ dice que es **"purely for entertainment purposes"** mientras el marketing promete que te "hablen al corazón otra vez" | [DATO] ae.studio/seanceai, consultado 2026-10-08 |
| **2wai** (Calum Worthy) | Beta para iOS: 2025-11-11 | Avatares de video conversacionales a partir de **3 minutos** de grabación, incluso de fallecidos | **USD 5 M pre-seed** (junio de 2025). Gratis en beta; suscripción futura sin precio publicado | — | Beta | El aviso tuvo **≈ 22 M de vistas y más de 5.800 respuestas**, mayoría en contra ("demoníaco", "pesadilla"); comparado con *Black Mirror* | [DATO] Decrypt, 2025-11-14; OECD AI Incidents, 2025-11-14 |
| **Eternos → Uare.ai** (Robert LoCascio) | 2024 (autofinanciada); pivote en 2025-11 | Gemelo digital de la persona para su "legado" | Pivote con **USD 10,3 M seed** (Mayfield, Boldstart) | Primer cliente mediático: Michael Bommer, enfermo terminal, con 25 h de entrevistas | **Pivoteó**: dejó el legado para los deudos y pasó a "gemelos digitales" de profesionales | El fundador dijo que el interés **no venía de gente frente a la muerte**, sino de quienes querían usarlo en vida | [DATO] TechCrunch, 2025-11-11 |
| **MyHeritage Deep Nostalgia** | 2021-02/03 | Anima caras de fotos viejas unos segundos, **sin voz** (a propósito) | Pocas animaciones gratis; el resto dentro de la suscripción | **1 M en 48 h; 72 M en ≈ 5 semanas; más de 112 M a mayo de 2024** (cifras de la propia empresa) | Activa | "Creepy" para algunos; la misma empresa admitió que "a algunos les encanta y a otros les resulta inquietante" | [DATO autodeclarado] MyHeritage wiki; Betanews, 2021-03-03; Guardian, 2021-03-02 |
| **Super Brain** (Zhang Zewei, Nanjing, China) | 2023-2024 | Avatar del fallecido con cara y voz | **10.000-20.000 yuanes (≈ USD 1.400-2.800)** por un avatar básico, en ≈ 20 días | **Más de 1.000 encargos**, según el fundador (Shanghai Observer, citado por Global Times, 2024-03) | [NO VERIFICADO] en 2026 | Dice rechazar casos de riesgo (por ejemplo, una madre que había intentado suicidarse) | [DATO] AFP vía TechXplore, 2023-12; Global Times, 2024-03-29; NPR, 2024-07-18 |
| **Silicon Intelligence** (China) | 2023-2024 | Avatar básico | **199 yuanes (≈ USD 30)** con menos de 1 minuto de video y audio | [NO VERIFICADO] | [NO VERIFICADO] | — | [DATO] AFP vía TechXplore, 2023-12 |
| **DeepBrain AI** (Corea del Sur) | [NO VERIFICADO] | Avatar de video "re;memory" | "Hasta USD 50.000" por filmación y avatar | — | — | — | [DATO débil] una sola fuente (The Namibian, sin fecha verificada) |
| **"Meeting You"** (MBC, Corea; documental, no producto) | 2020-02-06 | Una madre "reencuentra" en realidad virtual a su hija de 7 años fallecida | Producción de TV | 13-19 M de vistas del clip | — | Opiniones divididas: consuelo frente a "sentimientos falsos que profundizan la pérdida" | [DATO] Korea Times, 2020-04; JoongAng Daily; Road to VR |
| **Vivo Recuerdo** (Murcia, España) | 2018 | **B2B para funerarias**: pantalla en la sala velatoria con fotos y mensajes que mandan los asistentes por QR o WhatsApp, más una tablet de recuerdo para la familia | Sin precios publicados | **Más de 150 funerarias, 9 países, más de 65.000 servicios y más de 900.000 fotos** (a enero de 2023) | [NO VERIFICADO] en 2026 | — | [DATO] Xataka, 2023-01-15 |
| **Obitus / crematorios municipales del Reino Unido** | 2025-2027 | Video tributo, presentación de fotos y streaming del servicio | Presentación básica: **£50-69**; con música: **£75-95**; temática: **£95-110**; a medida: £400 (Cornwall) | — | Tarifas vigentes 2026-27 | — | [DATO] tarifas de Newcastle-under-Lyme y SWMC 2026-27; Chelmsford, Weymouth y South Lanarkshire 2025-26 |

### 2.2 Lo que dicen los casos juntos

- **[DATO]** Las empresas de "revivir" del nivel C en Occidente **quebraron, pivotearon o generaron rechazo masivo**: StoryFile (Chapter 11), Eternos (pivote), 2wai (reacción en contra), Project December (OpenAI le cortó el acceso), Seance AI (todavía en acceso anticipado tres años después).
- **[DATO]** Lo que **escaló en volumen** fue la versión liviana y sin voz (Deep Nostalgia, con más de 112 M de animaciones), y como **función gratis dentro de un negocio más grande** (genealogía), no como producto pago aislado.
- **[DATO]** Lo que **cobra de forma estable** es el **B2B o B2B2C en el momento del servicio fúnebre** (crematorios del Reino Unido, Vivo Recuerdo).
- **[DATO]** La excepción es China, donde hay demanda paga del nivel C (más de 1.000 encargos según el fundador de Super Brain). **[OPINIÓN]** No se puede trasladar a Argentina sin más: hay prácticas culturales de culto a los antepasados que acá no existen, y la cifra la declara el propio fundador.
- **[NO VERIFICADO / con alerta]** Una nota de AI Weekly, que cita a Hospice News, dice que el "grief tech" pasaría de ≈ USD 22.000 M (2024) a USD 80.000 M (2034). No vi la metodología y probablemente mete en la misma bolsa todo lo digital ligado a la muerte. **No usar esa cifra para decidir.**
- **[DATO débil]** Una sola fuente menciona que "Eternal Digital Assets", un híbrido de cementerio e IA, cerró por alta rotación de clientes. No lo pude confirmar.

---

## 3. Ética y evidencia sobre el duelo

### 3.1 Qué dice la investigación (de más a menos sólida)

| Estudio | Tipo / muestra | Qué encontró | Fuente |
|---|---|---|---|
| **Hollanek y Nowaczyk-Basińska, Universidad de Cambridge (Leverhulme CFI)**, *Philosophy & Technology*, 2024-05-09, DOI 10.1007/s13347-024-00744-w | Análisis ético con **escenarios hipotéticos** (sin datos clínicos) | Llaman a los deadbots un área de "alto riesgo" y "un campo minado ético". Escenarios: **MaNana** (bot de la abuela sin su consentimiento, que después de la prueba gratis empieza a mostrar publicidad), **Paren't** (una madre terminal deja un bot a su hijo de 8 años, que termina confundiéndolo y sugiere "encontrarse"), **Stay** (suscripción de 20 años que bombardea de mails a los hijos). **Recomiendan**: consentimiento del "donante de datos" en vida, restricción para menores, transparencia constante de que es una IA, nada de publicidad, una forma digna de "retirar" el bot ("funeral digital") y una salida fácil para quien no quiere seguir | [DATO] Comunicado de Cambridge, 2024-05-09; ScienceDaily |
| **Xygkou, She, Prigerson, Neimeyer y otros** ("The Conversation about Loss") | Entrevistas cualitativas a **10 personas** que usaban personajes de IA en el duelo (5 simulaban al fallecido) | Lo usaron como **"puente" en la fase aguda**, en general menos de un año; **no querían una réplica permanente**; sabían que era software. La autora pide que el bot aclare siempre que no es una persona | [DATO] PopSci; Undark. No pude leer el paper original ni confirmar que se publicó en CHI 2023 |
| **Manning y otros, CU Boulder**, DIS 2026 | **16 voluntarios** con un "fantasma" de chatbot **revisado por un humano antes de cada respuesta** | En general les resultó reconfortante ("el cierre que necesitaba"). Los errores de **tono** molestaban más que los inventos de datos. Hubo **temor a la dependencia** ("no sé si me gustaría la persona en la que me convertiría si sigo usándolo"). El propio autor perdió a su hermana y no lo querría para sí | [DATO] Science News, 2026-07-20 |
| **Lu y otros**, *Frontiers in Digital Health*, 2026-06-02 | 25 adultos de Guangdong (China), percepciones, no uso real | "**Ni inherentemente beneficiosos ni dañinos**": el consuelo y el riesgo salen de la misma capacidad de simular la presencia. Preocupa el duelo prolongado, la dependencia y la **explotación de familias con menos educación** | [DATO] Frontiers |
| Opinión en *Undark*, 2024-04-04 | Columna | Falta evidencia de que ayuden más allá de muestras chicas; el sector está casi sin regular | [DATO] Undark |
| Protocolo clínico NCT06932120 | Ensayo planificado (deepfake en terapia para duelo prolongado) | **Sin resultados todavía.** Es uso **clínico, con terapeuta**, no un producto de consumo | [DATO] ClinicalTrials.gov |

**Conclusión sobre la evidencia [DATO]:** **no encontré ningún ensayo controlado** que muestre que los griefbots mejoran o empeoran el duelo. Todo es cualitativo, con 10 a 25 personas.

### 3.2 Opinión de profesionales

- **[DATO]** La terapeuta de duelo Elizabeth Schandelmeier advierte que un avatar "parecido pero no igual" genera disonancia y puede alterar los recuerdos. Robert Neimeyer (referente de la teoría de los "vínculos continuos") advierte que el apego prolongado puede angustiar en vez de consolar (Decrypt; Our Sunday Visitor).
- **[DATO]** La teoría de los **vínculos continuos** dice que seguir "vinculado" con quien murió puede ser sano, **pero solo si la persona puede darle sentido a la pérdida**. Una imitación puede dificultar la aceptación (PopSci, resumiendo a Neimeyer).

### 3.3 ¿Lo quiere la gente? (encuestas)

- **[DATO]** Willful, una empresa canadiense de testamentos online (2026-07): **75%** de los canadianos encuestados (76% en Ontario) **no quiere** que su pareja se convierta en un griefbot; **solo 6%** querría seguir chateando con una versión digital. No publican tamaño de muestra ni fechas de campo (NOW Toronto, 2026-07-15; CTV, 2026-07-31).
- **[DATO con conflicto de interés]** Empathy, una empresa que **vende** herramientas de duelo con IA, encuestó a más de 6.000 personas en Canadá, EE.UU. y Reino Unido: 7 de cada 10 personas en duelo sintieron que no recibieron el apoyo que necesitaban; **86%** dice que es esencial que se aclare qué es real y qué es IA; **≈ 80%** quiere que se exija **consentimiento** antes de usar la voz o la imagen de alguien (Fast Company). Ojo: la encuesta la hizo una empresa interesada.

### 3.4 Casos de daño

- **[DATO]** **No encontré un caso clínico documentado** de daño causado específicamente por un griefbot.
- **[DATO]** El caso más citado, el adolescente de EE.UU. que se suicidó en 2024 tras interactuar con un chatbot, **no es un griefbot**: era un bot de compañía. No hay que mezclarlo.
- **[DATO]** Hay señales de riesgo reconocidas por los propios actores: Super Brain rechaza casos de personas vulnerables, y OpenAI cortó Project December.

### 3.5 Argumentos a favor y en contra

| A favor | En contra |
|---|---|
| Algunas personas reportan consuelo y "cierre", sobre todo con muertes súbitas o despedidas pendientes (CU Boulder, Frontiers) | La persona fallecida **no puede consentir** lo que "dice" su réplica (Cambridge, NPR) |
| El uso suele ser transitorio, como "puente" (Xygkou) | Riesgo de **dependencia** y de duelo trabado (CU Boulder, Frontiers, Neimeyer) |
| Los vínculos continuos son parte normal del duelo | Modelo de negocio peligroso: suscripción y publicidad sobre gente en duelo (escenarios de Cambridge) |
| Recordar con fotos y videos es una práctica de siempre | **Niños**: confusión sobre la muerte (escenario Paren't) |
| — | Rechazo social amplio (2wai; 75% en Canadá) |
| — | **Herederos en conflicto**: un hijo quiere el bot y otro no |

**[OPINIÓN]** La línea ética razonable separa **recordar** (A, B, D: material real o movimiento leve, sin palabras nuevas) de **simular** (C: inventar palabras, opiniones o conversaciones de alguien que no puede opinar). Lo primero es un servicio de memoria; lo segundo es una intervención en el duelo de otra persona sin formación clínica.

---

## 4. Marco legal en Argentina y políticas de las herramientas

> **Esto no es asesoramiento legal.** Es un mapa para llevarle a un abogado.

### 4.1 Imagen y voz: Código Civil y Comercial, art. 53

**[DATO]** Texto (resumido de fuentes jurídicas: pensamientocivil.com.ar, leyfacil, abogados.com.ar):

- "Para captar o reproducir la imagen o la voz de una persona, de cualquier modo que se haga, es necesario su consentimiento", salvo en actos públicos, por interés científico, cultural o educacional prioritario (con precauciones), o en el ejercicio regular del derecho a informar.
- "En caso de personas fallecidas pueden prestar el consentimiento sus **herederos** o el designado por el causante en una disposición de última voluntad. Si hay **desacuerdo entre herederos de un mismo grado, resuelve el juez**. Pasados **veinte años** desde la muerte, la reproducción **no ofensiva** es libre."
- Convive con el **art. 31 de la Ley 11.723** (retrato), que no fue derogado. En el caso Olmedo (Capitán Piluso), pasados más de 20 años de su muerte, se discutió si YPF podía usar su retrato sin los herederos (Microjuris, 2020-12-21). Solo leí el título, no el fallo.

**Consecuencias prácticas [OPINIÓN, a validar con un abogado]:**

1. Quien encarga el trabajo **tiene que ser heredero** (o el designado), y conviene dejarlo **por escrito**. Si hay varios hermanos, cualquiera puede oponerse y el conflicto termina en un juez.
2. El artículo dice "captar o reproducir". **Generar una voz nueva que dice cosas que la persona nunca dijo** podría verse como algo distinto, y más grave: el abogado Fernando Varela (abogados.com.ar, 2025-03-25) dice que **no hay norma que lo prohíba expresamente**, pero que los herederos pueden defenderse de una "resurrección digital" abusiva. Pone como uso abusivo "hacerle decir o hacer cosas que nunca hizo" y como uso legítimo el **homenaje con autorización de los herederos**. Cita el precedente *Ponzetti de Balbín* (intimidad de la familia).
3. Para cosas de la familia (fotos de los abuelos, uso privado), la restauración y el video homenaje encargados por un heredero tienen un riesgo legal bajo. El riesgo sube con la **voz clonada**, con la **difusión pública** y con el **uso comercial** (por ejemplo, usar el caso como publicidad propia sin permiso).

### 4.2 Datos personales: Ley 25.326

- **[DATO]** Art. 14, inc. 4: el derecho de acceso sobre datos de personas fallecidas lo ejercen los **sucesores universales**. Art. 34: los sucesores (línea directa o colateral hasta segundo grado) pueden iniciar el hábeas data (IAPP, 2022-08-03). La ley **no tiene reglas específicas** para tratar datos de fallecidos, y en la práctica se maneja ante la AAIP (IAPP).
- **[OPINIÓN]** Más allá del fallecido, el negocio maneja **datos de clientes vivos** (fotos familiares en las que aparecen vivos, menores, audios de WhatsApp). Hay que pedir el mínimo de datos, borrar después de entregar y no usar nada en el portfolio sin permiso escrito.
- **[NO VERIFICADO en esta sesión]** Según mi conocimiento, la definición de "datos sensibles" de la Ley 25.326 (art. 2) **no menciona expresamente** los datos biométricos (cara, voz). Preguntarle al abogado cómo se tratan.

### 4.3 Proyectos de ley (ninguno con sanción confirmada)

| Proyecto | Qué propone | Estado | Fuente |
|---|---|---|---|
| 7009-D-2024 | Penal (art. 117 ter): prisión de 1 mes a 1 año por usar IA para replicar rostro o voz **con intención de dañar** | [NO VERIFICADO] | HCDN |
| 3558-D-2025 | Registro Nacional de Voces Sintéticas (ENACOM) y advertencias obligatorias en producciones con voz generada por IA | [NO VERIFICADO] | HCDN |
| 5945-D-2025 (Marziotta) | Amparo especial contra deepfakes; lo pueden presentar **los herederos**; el juez resuelve en 24 h | [NO VERIFICADO] | Diario Constitucional, 2025-10-22 |
| Proyecto 2026, art. 139 ter (Código Penal) | 4 a 8 años por generar o modificar audios o videos **sin consentimiento de la persona o de sus herederos** | [NO VERIFICADO] (no confirmé número ni autor) | Documento de HCDN encontrado por buscador |
| "Ley de herencia digital y gestión post mortem de la identidad digital" | Define el **"deepfake post mortem"** (imagen, voz o rasgos de un fallecido recreados con IA) | [NO VERIFICADO] (el documento no tiene fecha visible) | Documento de HCDN encontrado por buscador |

- **[DATO]** La fiscal porteña Marcela Monti inició una demanda colectiva de consumo para que la Ciudad de Buenos Aires **bloquee sitios web de clonación de voz y rostro** con IA (Diario Judicial). **[NO VERIFICADO]**: la fecha exacta de la nota y el estado de la causa.
- **[DATO]** En el exterior la tendencia es endurecer: California (AB 1836, vigente desde 2025-01-01) creó una acción por réplicas digitales de **artistas fallecidos** sin consentimiento del estate, con un mínimo de USD 10.000 o el daño real (Manatt; DGLaw). Una fuente secundaria dice que el NO FAKES Act federal avanzó en el Senado de EE.UU. en junio de 2026, con protección hasta 70 años después de la muerte. **[NO VERIFICADO]**: confirmar en Congress.gov.

### 4.4 Políticas de las herramientas

| Herramienta | Qué dice | ¿Habla de fallecidos? | Fuente |
|---|---|---|---|
| **ElevenLabs** (voz) | Prohíbe replicar intencionalmente la voz de otra persona "**without consent or legal right**", o de forma que engañe sobre si la generó una IA. Política actualizada el **2026-08-17** | **No** | [DATO] elevenlabs.io/use-policy, consultado 2026-10-08 |
| **HeyGen** (avatar en video) | Para un avatar a medida de una persona real exige el **consentimiento explícito del "Actor"**; para un "digital twin" pide **prueba de consentimiento** (la persona se nombra y autoriza). Los "photo avatars" figuran en la documentación como avatares que "no requieren consentimiento" porque no representarían a una persona identificable | **No** | [DATO] Política de moderación vigente desde 2024-07-25; documentación para desarrolladores |
| **Higgsfield** (lo que tiene Facu) | Según páginas de **la propia empresa** (no el contrato): hay que confirmar el permiso sobre todas las caras que se suben, y si no, la cuenta puede suspenderse | **No** | [DATO débil] geo.higgsfield.ai. No pude leer los Términos de Uso vigentes |

**[OPINIÓN]** Un fallecido **no puede grabar el video de consentimiento** que pide HeyGen. Para ElevenLabs, la "autorización legal" sería la de los herederos, una zona gris. Un negocio de "revivir" depende de herramientas de terceros que pueden **suspender la cuenta** ante una denuncia, y eso choca con la regla de independencia del proyecto (que no mande un único cliente o plataforma).

### 4.5 Preguntas para el abogado (una consulta antes de cobrar)

1. ¿Alcanza con un **consentimiento firmado por quien encarga** (declarando que es heredero y que los demás herederos del mismo grado están de acuerdo)? ¿Qué pasa si después aparece un hermano que se opone?
2. ¿Una **foto animada sin voz** para uso privado de la familia necesita lo mismo que una **voz clonada**? ¿Cambia algo si se difunde en redes?
3. ¿Generar **palabras nuevas** con la voz del fallecido puede afectar el honor o la intimidad (arts. 51-53 CCyC) aunque haya consentimiento de un heredero?
4. ¿Cómo tratar las caras y voces según la **Ley 25.326**? ¿Hace falta inscribir una base de datos? ¿Cuánto tiempo se pueden guardar los archivos?
5. ¿Rige el **derecho de arrepentimiento** de 10 días (Ley 24.240) en ventas online de un producto **personalizado**? **[NO VERIFICADO]**: creo que el CCyC exceptúa los bienes hechos según especificaciones del cliente, pero hay que confirmarlo.
6. ¿Qué cláusula de **limitación de responsabilidad** conviene si la IA "cambia" una cara o si un familiar se angustia?
7. Para el modelo B2B: ¿quién es el responsable del tratamiento de datos, la cochería o Facu?

---

## 5. Ángulos más sanos y vendibles

### 5.1 Comparación

| Ángulo | Evidencia de demanda | Evidencia de que se paga | Competencia | Riesgo [OPINIÓN] | Fit con Facu [OPINIÓN] |
|---|---|---|---|---|---|
| **A1. Restaurar y colorizar fotos** (ya era la I19) | Mucha oferta en Fiverr; apps gratis | **[DATO]** Fiverr: gigs **desde USD 5**, paquetes de USD 10, 25 y 40, pedidos de hasta USD 50 (en general **por pedido o paquete**, no queda claro que sea **por foto**). Chile: desde CLP 5.000 por foto. Portugal: desde 10 € por foto | **Muy alta**, y además las apps gratis lo vuelven commodity | Bajo | Alto (Higgsfield + control de calidad) |
| **A2. Digitalizar VHS, casetes y diapositivas** | [NO VERIFICADO] (no lo busqué por el límite de búsquedas) | [NO VERIFICADO] | [NO VERIFICADO] | Bajo | Medio (necesita equipos) |
| **B1. Animar fotos sin voz** (tipo Deep Nostalgia) | **[DATO]** Más de 112 M de animaciones (MyHeritage, mayo de 2024) | Bajo como producto aislado: viene gratis o incluido en una suscripción | MyHeritage, HeyGen ("memorial video maker"), apps | Bajo-medio (puede resultar "creepy"; la IA puede deformar caras) | Alto, como **agregado** de un pack |
| **B2. Video homenaje** (velorio, aniversario, misa, cumpleaños póstumo; era la I20) | **[DATO]** En el Reino Unido es un servicio estándar de los crematorios | **[DATO]** £50-110 por tributo (Reino Unido, 2025-27) | En Argentina: plantillas gratis de CapCut para hacerlo uno mismo; servicios a medida [NO VERIFICADO] | Bajo | Alto |
| **B3. B2B con cocherías y cementerios privados** (pantalla o video homenaje, página memorial con QR, todo como "extra" del servicio) | **[DATO]** Vivo Recuerdo: más de 150 funerarias, más de 65.000 servicios (España, a 2023-01) | **[DATO]** Hay funerarias que lo ofrecen como opcional (no hay precios públicos) | En Argentina **no encontré** ninguna cochería que lo ofrezca (búsqueda limitada) | Bajo | Medio-alto: es una venta B2B a una industria tradicional, cosa que Facu quiere aprender |
| **D. Biografía grabada en vida** ("el documental de la abuela" para sus 80 años) | **[DATO]** El pivote de Eternos sugiere **poca demanda del ángulo "muerte"**; HereAfter cobra poco (≈ USD 4-9 por mes) | Débil como app; **como regalo en vida** [NO VERIFICADO] | HereAfter, StoryFile (en el exterior) | **Bajo** (la propia persona consiente) | Medio-alto: entrevista, edición y video; se enmarca como **regalo de cumpleaños**, no como muerte |
| **C. "Revivir"** (voz, avatar que habla, chatbot) | Nicho: **[DATO]** 6% en Canadá; mercado pago en China | **[DATO]** USD 1.400-2.800 (China); USD 19,99 (Seance) | Apps globales (2wai, Seance, HereAfter) | **Alto** | Bajo: no hay ventaja propia |

### 5.2 Lectura [OPINIÓN]

- **Lo más vendible en Argentina, con menos riesgo y más aprendizaje**, es un **pack de homenaje (A1 + B1 + B2)** vendido por dos canales: **B2C** en fechas clave y **B2B** con cocherías.
- El **B2B** es lo más interesante para aprender y lo único con cierta escalabilidad: una cochería concentra muchas familias por mes, y el servicio entra **en el momento del gasto** (cuando la familia ya está pagando el sepelio).
- El **nivel D**, presentado como **regalo en vida** ("Grabemos las historias del abuelo"), es la versión ética más limpia del "volver a escuchar su voz": es **su voz real**, con su consentimiento. Pero la evidencia de demanda paga es débil (pivote de Eternos) y hay que validarla aparte.
- **Ojo con el calendario:** el **Día de la Madre en Argentina es el domingo 2026-10-18**. Para quien perdió a su mamá es una fecha dolorosa. Un "homenaje a mamá" puede tener demanda, pero el mensaje tiene que ser sobrio ("un recuerdo de mamá", no "volvé a ver a mamá"). Es una fecha a 10 días: sirve para probar, no para planear.

---

## 6. Argentina: mercado funerario

| Indicador | Valor | Fuente / fecha |
|---|---|---|
| Muertes por año | **353.428 (2024)**; 369.843 (2022) | [DATO] UNL, con datos del Ministerio de Salud; Intramed (2022). El total de 2023 no lo pude leer en la síntesis de la DEIS |
| Empresas del rubro | **438 registradas** (MDZ, 2026-05-21) o **"más de 1.100"** (La Nación, sin fecha verificada) | [DATO] Las cifras no coinciden; seguramente miden cosas distintas |
| Facturación del sector | "Más de $20.000 millones por año" (cita sin fuente ni fecha en una columna de Rebelión) | **[NO VERIFICADO / no usar]** |
| Precio de cremación directa sin velatorio (CABA, Cía. Miguel Costa) | **$955.900** | [DATO] MDZ, 2026-05-21 |
| Cremación directa con velatorio de 2 a 4 h | Desde **$1.149.500** | [DATO] MDZ, 2026-05-21 |
| Parque privado o nicho con velatorio | Desde ≈ **$2.044.900** | [DATO] MDZ, 2026-05-21 |
| Funeral completo | **$1.000.000 a $30.000.000** | [DATO] MDZ, 2026-05-21 |
| Velatorio básico (2024) | Desde $550.000 | [DATO] iProfesional, 2024-09-01 (dato visto en el buscador; la nota abierta estaba cortada) |
| Tendencia | **Gana la cremación**: 78,5% de los cuerpos en Buenos Aires en 2018 (conteo de AFP); "casi 90%" pide cremación (Cochería Tacuarí, 2020); **caen los velatorios tradicionales** (Asociación de Empresarios de Servicios Fúnebres) | [DATO] BA Times/AFP; Malay Mail, 2020-01-03 |
| Diversificación | Funerarias que suman **mascotas** (desde $170.000) por la baja de servicios humanos | [DATO] BAE Negocios (fecha no verificada) |
| Oferta digital | Streaming de despedidas en pandemia (Tierra de Paz, 2020; no confirmé el país); **no encontré** cocherías argentinas con video homenaje | [DATO] Economis, 2020; resto [NO VERIFICADO] |

**Tamaño del nicho [ESTIMACIÓN], para tener un orden de magnitud:**

- **Supuestos (no son datos):** entre el 1% y el 5% de las familias compra un homenaje pago; ticket de **ARS 50.000 a 95.000**, que es el 5-10% del precio de una cremación directa ($955.900).
- **Resultado:** 353.428 muertes × 1-5% = **≈ 3.500 a 17.700 pedidos por año** en todo el país, o **≈ ARS 177 M a 1.680 M por año**. A eso se suman aniversarios y fechas, que no estimo.
- **Techo de una persona sola:** con 10-15 h por semana y ≈ 3 h por pedido (ver 7.2), entran **≈ 4-5 pedidos por semana**, unos 16-20 por mes. Con ARS 70.000 de ticket da **≈ ARS 1,1-1,4 M por mes en bruto**.
- **[OPINIÓN]** Como negocio puente es chico pero real. Como startup, **el mercado argentino B2C no alcanza**. Haría falta el modelo B2B o plataforma y salir a Latinoamérica.

---

## 7. Modelo de negocio, MVP, riesgos y validación

### 7.1 Modelo recomendado para probar [OPINIÓN]

**"Homenaje": restauración + video homenaje + (opcional) 1 o 2 fotos con movimiento leve, sin voz, con consentimiento escrito del familiar.**

- **Canal B2C:** familias, por recomendación directa, grupos del barrio, Instagram y WhatsApp. Fechas: aniversarios de fallecimiento, misas, cumpleaños póstumos, Día de la Madre y del Padre.
- **Canal B2B (piloto):** cocherías y cementerios privados de la zona. Ofrecerlo como **extra** que la cochería vende (con comisión o precio mayorista) o como servicio de Facu con derivación de la cochería.
- **Línea roja escrita, que se publica:** **no se clona la voz, no se hace "hablar" al fallecido, no se hacen chatbots, nada para menores sin los padres, nada con un heredero en conflicto.** Es un diferencial de confianza, no solo un límite.

### 7.2 MVP: equipo, costo y tiempo [ESTIMACIÓN]

| Ítem | Detalle | Costo estimado |
|---|---|---|
| Producción | Higgsfield (ya lo tiene; **verificar que su plan permita uso comercial**) + editor de video (CapCut u otro gratis) + Claude para guiones y textos | USD 0 extra si el plan sirve; si no, [NO VERIFICADO] |
| Música | Biblioteca libre de derechos o música generada con licencia comercial | USD 0-15 [NO VERIFICADO] |
| Consentimiento y términos | Modelo de autorización del heredero (declaración de herederos, alcance, uso privado o público, borrado de datos) | Consulta con un abogado: **costo [NO VERIFICADO]** |
| Demos | 3 demos con fotos de la **propia familia**, con permiso de los familiares | USD 0 |
| Difusión | WhatsApp Business, Instagram, 5-10 grupos; tarjetas impresas para cocherías | USD 20-40 |
| Anuncios (opcional) | Meta Ads de prueba, segmentados y con mensaje sobrio | USD 0-80 |
| **Total** | | **< USD 200** (sin contar el abogado si es caro) |

- **Tiempo por pedido [ESTIMACIÓN]:** 2-4 h para un video de 2-3 minutos con 20-40 fotos, contando la conversación con la familia, la selección, la restauración y la edición. Hay que medirlo en los primeros 5 pedidos.
- **Equipo:** Facu solo. Como ingeniero industrial, el aporte es armar la **línea de producción**: formulario de ingreso, checklist, plantilla de edición y control de calidad de caras.

### 7.3 Riesgos

| Riesgo | Por qué importa | Cómo se mitiga [OPINIÓN] |
|---|---|---|
| **La IA altera caras** | Una cara "parecida pero distinta" de mamá arruina el trabajo y lastima | Vista previa con marca de agua, una ronda de cambios y animar solo fotos de buena calidad |
| **Conflicto entre herederos** | El art. 53 manda al juez si hay desacuerdo | Consentimiento escrito y declaración de quien encarga; ante la duda, no se hace |
| **Desgaste emocional** | Trabajar todos los días con duelo, a los 22 años | Límite de pedidos por semana; registrar cómo se siente (es parte del aprendizaje) |
| **Reputación** | Quedar como "el que revive muertos" en tiempos de rechazo a los deepfakes (2wai) | Línea roja pública: **homenaje, no simulación** |
| **Plataforma** | Suspensión de la cuenta de Higgsfield o HeyGen por una denuncia | Nada de voz ni de gemelos digitales; guardar los archivos fuente; tener una herramienta alternativa |
| **Commodity** | CapCut y HeyGen tienen plantillas gratis para hacerlo uno mismo | Vender el **acompañamiento y el "te lo hago yo, bien y rápido"**, no la herramienta |
| **Ticket bajo y estacionalidad** | Ingreso chico e irregular | Canal B2B (flujo constante de servicios) y paquetes |
| **Datos sensibles** | Fotos de menores y vivos, audios | Pedir lo mínimo, borrar a los 30 días y no usar en el portfolio sin permiso |

### 7.4 Validación en 2-4 semanas con menos de USD 200

**Pérdida máxima definida antes de arrancar: USD 200 y 40 horas.**

- **Semana 1 (2026-10-09 a 10-15): preparación**
  - Hacer 3 demos con fotos de la propia familia, con permiso.
  - Una consulta legal o, como mínimo, el modelo de consentimiento.
  - Lista de 40-60 contactos directos y de 15 cocherías o cementerios privados de la zona.
  - Hipótesis de precio, para **probar** y no para cobrar como dato: tres niveles (solo restauración; video homenaje; video + animación + impreso). Ticket central de prueba: ARS 50.000-95.000, que es el 5-10% de una cremación directa.
- **Semana 2 (10-16 a 10-22): B2C**
  - 40-60 mensajes 1 a 1 y 5 grupos, con un mensaje sobrio ("un recuerdo de quien ya no está, hecho con fotos de la familia").
  - Coincide con el Día de la Madre (2026-10-18).
  - Medir conversaciones, pedidos de presupuesto, ventas y precio aceptado.
- **Semanas 2-3: B2B**
  - Visitar o llamar a 15 cocherías u otras empresas del rubro y ofrecer un **piloto gratis para 3 familias** a cambio de opinión y de una propuesta de precio.
  - Preguntar: ¿lo venderían como extra? ¿A cuánto? ¿Quién paga?
- **Semana 4: decisión**
  - **Seguir** si se cumple: **5 o más ventas B2C pagas** con 40 o más conversaciones reales, **o** al menos **1 cochería** que acepte un piloto pago o un acuerdo de comisión. Además, **≤ 3 h por pedido** y ningún conflicto ético que no se haya podido manejar.
  - **Cerrar con post-mortem** si se cumple: menos de 2 ventas con más de 40 conversaciones **y** cero cocherías interesadas, **o** si el desgaste emocional no compensa.
- **Qué se aprende aunque falle:** vender B2B a una industria tradicional, diseñar un consentimiento y un flujo de datos, producir servicios creativos con IA en serie, y la sensibilidad de un mercado delicado. Todo eso sirve para la etapa 2.

---

## 8. Veredicto

### 8.1 Puntajes (1-10; en riesgo, 10 = riesgo bajo)

**Versión C, "Revivir" (voz clonada, video que habla, chatbot)**

| Criterio | Puntaje | Una línea |
|---|---|---|
| Tamaño del problema | 6 | El duelo es universal (353.428 muertes en 2024), pero muy poca gente quiere esto (6% en Canadá, 2026) |
| Disposición a pagar | 4 | Hay pago en China (USD 1.400-2.800); en Occidente es barato o gratis, y las empresas quebraron o pivotearon |
| Espacio frente a la competencia | 3 | Apps globales con financiación (2wai con USD 5 M) y herramientas gratis; no hay foso posible |
| Ventaja de Facu | 2 | No es técnico, no es clínico y no tiene una marca de confianza en el duelo |
| Factibilidad | 5 | Es técnicamente fácil, pero las plataformas exigen un consentimiento que un fallecido no puede dar, y la ley está en zona gris |
| Escalabilidad | 5 | El software escala, pero ese terreno ya lo ocupan jugadores globales |
| Riesgo (10 = bajo) | 2 | Ético, reputacional, legal y de plataforma, todo alto a la vez |
| **Promedio** | **≈ 3,9** | |

**Versión A+B, "Homenaje" (restauración + video homenaje + animación sin voz; B2C y piloto B2B)**

| Criterio | Puntaje | Una línea |
|---|---|---|
| Tamaño del problema | 5 | Es una necesidad real pero de ticket bajo; el nicho nacional da ARS 177 M a 1.680 M por año [ESTIMACIÓN con supuestos] |
| Disposición a pagar | 5 | Probada afuera (£50-110 en el Reino Unido; Vivo Recuerdo); **no verificada en ARS** |
| Espacio frente a la competencia | 5 | Hay commodity para hacerlo uno mismo, pero no vi oferta B2B con cocherías en Argentina (búsqueda limitada) |
| Ventaja de Facu | 5 | Tiene Higgsfield, cabeza de procesos y presencia local; nada único |
| Factibilidad | 8 | Se arranca esta semana con menos de USD 200 |
| Escalabilidad | 4 | Es un servicio por horas; solo escala si se productiza como B2B o plataforma |
| Riesgo (10 = bajo) | 7 | Bajo si no hay voz, hay consentimiento escrito y la línea roja es pública |
| **Promedio** | **≈ 5,6** | |

### 8.2 Opinión [OPINIÓN]

**Sobre "revivir":** no lo recomiendo, y no por miedo al riesgo en general (Facu está dispuesto a equivocarse y eso está bien), sino porque **acá el error no es barato ni es solo de Facu**. Si sale mal, el costo lo paga una familia en duelo. La evidencia no muestra que ayude: solo hay estudios de 10 a 25 personas, sin ensayos controlados, y los propios investigadores temen la dependencia. El mercado occidental ya probó este producto con mucha más plata y le fue mal: StoryFile en concurso, Eternos que pivoteó porque los clientes no estaban donde creía, 2wai con rechazo masivo. Además, el negocio dependería de herramientas que prohíben justamente lo que se vendería (replicar a alguien sin su consentimiento) y de una zona legal gris en Argentina. Y Facu no tiene ninguna ventaja: cualquiera con una cuenta de HeyGen o de 2wai hace lo mismo. "Ser el primero" acá no vale: **no es el primero** (Project December es de 2020) y lo que llegó primero no ganó.

**Sobre las versiones sanas:** el **pack homenaje** es un experimento razonable para la etapa 1. Es barato, rápido de probar, ético si se respeta la línea roja, y enseña venta B2B a una industria tradicional. Pero hay que verlo como lo que es: **un servicio de ticket bajo con techo de horas**, parecido a las ideas I19 e I20 que ya estaban en el menú. **No es una idea nueva de startup.** Si de la prueba con cocherías sale tracción, hay una pregunta más grande para anotar en `ideas/`: **¿hace falta una plataforma de homenaje digital para funerarias en Latinoamérica**, como lo que hizo Vivo Recuerdo en España (más de 150 funerarias)? Eso sí podría escalar, y se valida con el piloto B2B de este experimento.

**Sobre el nivel D (grabar en vida):** es la versión ética más limpia del deseo de Facu de "volver a escuchar su voz", porque es **la voz real, con su permiso**. Vendida como **regalo de cumpleaños** ("el documental de la abuela"), puede tener un mercado distinto del duelo. La evidencia de demanda es débil (el pivote de Eternos), así que, si interesa, se prueba aparte y en pequeño.

**Corrección a un documento previo del proyecto:** en `research/fuentes/2026-10-01-rapidas-personas-estacional.md` dice "en Fiverr cuesta de USD 5 a 50 por foto". Lo que encontré hoy son gigs **desde** USD 5 y paquetes de USD 10, 25 y 40, en general **por pedido o paquete**. No está claro que sea **por foto**. Conviene corregirlo.

---

## 9. Qué no pude verificar (límite de búsquedas alcanzado)

- **Precios en ARS** de restauración de fotos y de videos homenaje en Mercado Libre o Instagram (lo dejo como [NO VERIFICADO]; ya estaba marcado así en el estudio del 2026-10-01).
- Si **alguna cochería o cementerio privado argentino** (Parque Memorial, Jardín de Paz, Lázaro Costa, etc.) ofrece homenaje digital, página memorial o lápida con QR. La búsqueda quedó cortada.
- La demanda de **digitalizar VHS y casetes** en Argentina.
- Los precios oficiales actuales de HereAfter (la página da 404) y de Project December.
- El estado de los proyectos de ley argentinos y del NO FAKES Act.
- Los Términos de Uso vigentes de Higgsfield.

Si Facu quiere cerrar estos puntos, se puede retomar en otra sesión.

---

## 10. Fuentes (consultadas el 2026-10-08; la fecha de publicación va cuando se conoce)

**Casos y empresas**
- Replika y Roman Mazurenko: CBC, https://amp.cbc.ca/lite/story/1.6252286 · Light Reading, https://www.lightreading.com/enterprise-cloud/machine-learning-and-ai/after-raising-the-dead-ai-startup-plans-next-step/d/d-id/729944 · BBC Mundo vía Metro PR (2018-10-06), https://www.metro.pr/pr/bbc-mundo/2018/10/06/cuando-su-mejor-amigo-murio-ella-lo-reconstruyo-digitalmente.html
- Project December: The Register (2021-09-08), https://www.theregister.com/2021/09/08/project_december_openai_gpt_3/ · webcurios (2021-07-30), https://webcurios.co.uk/webcurios-30-07-21/ · Canaltech (2021), https://canaltech.com.br/inteligencia-artificial/empresa-desliga-chatbot-apos-homem-simular-conversas-com-noiva-falecida-196004/ · Decrypt, https://decrypt.co/214163/ai-developer-refutes-eternal-you-documentary-calls-depiction-of-his-chatbot-misleading · sitio, https://projectdecember.net/
- HereAfter AI: AIChief, https://aichief.com/alternatives/hereafter-ai/ · IEEE Future Directions (2023-08-20), https://futuredirections.ieee.org/2023/08/20/digital-after-life · futurezone.at, https://futurezone.at/start-ups/grief-tech-ki-kuenstliche-intelligenz-ai-hereafter-start-up-chatbot-trauer-ethik-tod/402415583
- StoryFile: Westfair, https://westfaironline.com/courts/white-plains-bankruptcy-interrupts-talk-with-the-dead · AI Business (2024), https://aibusiness.com/verticals/startup-behind-ai-william-shatner-files-for-bankruptcy · AI Business (2025-03), https://aibusiness.com/nlp/william-shatner-backed-ai-startup-acquired-real-people-chatbots · Inforuptcy (expediente 7:24-bk-22398), https://www.inforuptcy.com/browse-filings/new-york-southern-bankruptcy-court/7:24-bk-22398/bankruptcy-case-storyfile-inc · StoryFile, https://www.storyfile.com/news/key7-purchase
- You, Only Virtual: Caplight, https://www.caplight.com/company/myyov
- Seance AI: https://www.ae.studio/seanceai (consultado 2026-10-08) · Futurism, https://futurism.com/ai-seance
- 2wai: Decrypt (2025-11-14), https://decrypt.co/348707/demonic-ai-app-lets-users-talk-dead-loved-ones-faces-backlash · OECD AI Incidents (2025-11-14), https://oecd.ai/en/incidents/2025-11-14-277c
- Eternos → Uare.ai: TechCrunch (2025-11-11), https://techcrunch.com/2025/11/11/immortality-startup-eternos-pivots-to-a-personal-ai-that-sounds-like-you/
- Deep Nostalgia: MyHeritage wiki, https://myheritage.com/wiki/What_is_the_Deep_Nostagia_photo_feature_by_MyHeritage · Betanews (2021-03-03), https://betanews.com/2021/03/03/animate-your-ancestors · Guardian vía PressReader (2021-03-02), https://www.pressreader.com/usa/the-guardian-usa/20210302/281479279146700 · Interesting Engineering, https://interestingengineering.com/innovation/myheritage-creepy-deepfake-tool
- China: AFP vía TechXplore (2023-12), https://techxplore.com/news/2023-12-chinese-mourners-ai-digitally-resurrect.pdf · Global Times (2024-03-29), https://www.pressreader.com/china/global-times/20240329/281659670047357 · China Daily (2024-04-04), https://enapp.chinadaily.com.cn/a/202404/04/AP660def77a310115ef066ff83.html · NPR (2024-07-18), https://www.npr.org/2024/07/18/nx-s1-5040583/china-ai-artificial-intelligence-dead-avatars
- DeepBrain AI (fuente única y débil): The Namibian, https://namibian.com.na/?p=724464
- "Meeting You" (MBC): Korea Times (2020-04), https://www.koreatimes.co.kr/www/art/2020/04/688_287372.html · JoongAng Daily, https://www.koreajoongangdaily.com/business/interview-the-controversial-reality-of-bringing-back-a-loved-one/10091178 · Road to VR, https://www.roadtovr.com/mother-meets-recreation-of-deceased-child-in-vr/amp
- Vivo Recuerdo: Xataka (2023-01-15), https://www.xataka.com/empresas-y-economia/libro-condolencias-tanatorio-ahora-enorme-pantalla-qr-para-homenajear-al-difunto · Noticias de Navarra (2020-04-07), https://www.noticiasdenavarra.com/sociedad/2020/04/07/condolencias-virtuales-falta-abrazos-2297437.amp.html
- Tarifas de tributos en el Reino Unido: Newcastle-under-Lyme 2026-27, https://www.newcastle-staffs.gov.uk/downloads/file/2154/obitus-multimedia-system-price-list-2026-27 · SWMC 2026-27, https://www.swmcrematorium.gov.uk/wp-content/uploads/2026/02/SWMC-Obitus-Tribute-Fees-2026-27.pdf · Chelmsford, https://www.chelmsford.gov.uk/cemetery-and-crematorium/fees-and-charges-for-the-cemetery-and-crematorium/cremation-fees · Cornwall (Penmount), https://www.cornwall.gov.uk/births-marriages-deaths/penmount-crematorium/scale-of-charges/webcast-and-visual-tributes/
- Cifra de mercado (no usar): AI Weekly, https://aiweekly.co/alerts/grief-ai-market-projected-at-80b-by-2034-clinicians-wary
- Regulación en EE.UU. 2026, NO FAKES Act y cierre de Eternal Digital Assets: los vi en resúmenes del buscador **sin poder atribuir con certeza cuál página decía cada cosa**. Candidatas: https://www.multistate.ai/updates/vol-89-state-digital-replica-laws-post-mortem-rights · https://www.martincid.com/analysis/digital-afterlife-law-consent-identity/ · https://www.mexc.com/news/167137 . Por eso esos dos datos quedan como [NO VERIFICADO].

**Ética y evidencia**
- Cambridge, comunicado (2024-05-09): https://www.cam.ac.uk/research/news/call-for-safeguards-to-prevent-unwanted-hauntings-by-ai-chatbots-of-dead-loved-ones · ScienceDaily: https://sciencedaily.com/releases/2024/05/240508201408.htm · paper: DOI 10.1007/s13347-024-00744-w
- Xygkou y otros (cobertura): PopSci, https://www.popsci.com/technology/ai-dead-loved-ones/ · Undark (2024-04-04), https://undark.org/2024/04/04/opinion-griefbots-lack-evidence/
- CU Boulder: Science News (2026-07-20), https://www.sciencenews.org/article/ai-ghosts-grief-facts-wrong-chatbot
- Lu y otros: Frontiers in Digital Health (2026-06-02), https://www.frontiersin.org/journals/digital-health/articles/10.3389/fdgth.2026.1852514/full
- Expertos: Decrypt, https://decrypt.co/213802/thanabots-eternal-you-project-december-ai-dead-people · Our Sunday Visitor, https://www.oursundayvisitor.com/?p=109169
- Ensayo clínico: https://clinicaltrials.gov/study/NCT06932120
- Encuestas: NOW Toronto (2026-07-15), https://nowtoronto.com/news/ontario-rejects-ai-griefbots-deceased-partners-survey/ · CTV (2026-07-31), https://www.ctvnews.ca/sci-tech/article/ai-ghosts-are-a-tool-of-our-age-but-should-you-grieve-your-loved-ones-through-technology/ · Fast Company (Empathy), https://www.fastcompany.com/91610459/ai-users-who-use-ai-in-grief

**Legal**
- Art. 53 CCyC: https://www.pensamientocivil.com.ar/system/files/el_derecho_a_la_imagen_en_el_nuevo_proyecto_de_codigo_civil_y.pdf · https://leyfacil.com.ar/?p=208
- Varela, "El derecho de imagen y el deepfake post-mortem" (2025-03-25): https://abogados.com.ar/el-derecho-de-imagen-y-el-deepfake-post-mortem-la-llamada-resurreccion-digital/36499
- Caso Olmedo, Microjuris (2020-12-21): https://aldiaargentina.microjuris.com/2020/12/21/fallos-capitan-piluso-a-mas-de-20-anos-del-fallecimiento-de-olmedo-ypf-puede-utilizar-su-retrato-sin-consentimiento-de-los-herederos/
- Ley 25.326: IAPP (2022-08-03), https://iapp.org/news/a/notas-de-la-directora-general-iapp-america-latina-3-agosto-2022 · texto, https://www.cobioetica.unlu.edu.ar/sites/www.cobioetica.unlu.edu.ar/files/site/LEY%2025326%20Habeas%20Data_0.pdf
- Proyectos: 7009-D-2024, https://www4.hcdn.gob.ar/dependencias/dsecretaria/Periodo2024/PDF2024/TP2024/7009-D-2024.pdf · 3558-D-2025, https://www4.hcdn.gob.ar/dependencias/dsecretaria/Periodo2025/PDF2025/TP2025/3558-D-2025.pdf · 5945-D-2025, Diario Constitucional (2025-10-22), https://www.diarioconstitucional.cl/2025/10/22/proyecto-de-ley-busca-crear-una-accion-de-amparo-especial-para-proteger-el-derecho-a-la-imagen-contra-el-uso-indebido-de-ia-especialmente-en-casos-de-deepfakes/ · Derecho en Zapatillas (2025), https://www.derechoenzapatillas.com/2025/el-testigo-que-volvio-a-hablar-puede-declarar-un-muerto-con-ia/ · Diario Judicial (fiscal Monti; fecha no verificada), https://www.diariojudicial.com/news-98934-la-justicia-se-mete-en-la-clonacion-por-ia · adjuntos de HCDN que encontró el buscador (no pude confirmar cuál corresponde a cada proyecto de 2026): https://rest.hcdn.gob.ar/web/tramites-parlamentarios/render/adjunto/699c90673db91.pdf , https://rest.hcdn.gob.ar/web/tramites-parlamentarios/render/adjunto/6a9065927ab81.pdf
- California AB 1836: Manatt, https://www.manatt.com/insights/newsletters/client-alert/california-enacts-a-host-of-new-ai-and-digital-rep · DGLaw, https://www.dglaw.com/california-passes-new-legislation-prohibiting-unauthorized-ai-replicas/
- ElevenLabs Prohibited Use Policy (actualizada 2026-08-17): https://elevenlabs.io/use-policy
- HeyGen: política de moderación (vigente desde 2024-07-25), https://www.heygen.com/moderation-policy · consentimiento de avatares, https://developers.heygen.com/docs/avatar-consent · memorial video maker, https://www.heygen.com/es-ar/tool/memorial-video-maker
- Higgsfield (páginas de la propia empresa): https://geo.higgsfield.ai/is-higgsfield-ai-safe-for-face-data-guide

**Argentina: mercado**
- Muertes: UNL, https://www.unl.edu.ar/noticias/news/view/el_pulso_demográfico_de_argentina_¿hacia_un_crecimiento_cero_1 · DEIS, síntesis 2023, https://www.argentina.gob.ar/sites/default/files/31-10-sintesis-estadistica2023.pdf · Intramed (2022), https://www.intramed.net/content/publican-estadisticas-vitales-2022-de-argentina
- Precios y empresas: MDZ (2026-05-21), https://www.mdzol.com/dinero/el-precio-un-funeral-completo-oscila-los-1000000-y-30000000-n1523705 · iProfesional (2024-09-01), https://www.iprofesional.com/actualidad/411693-el-costo-de-morir-cuanto-sale-servicio-sepelio-argentina · La Nación (sin fecha verificada), https://www.lanacion.com.ar/economia/la-muerte-tiene-mucho-marketing-nid1208155 · BA Times/AFP, https://www.batimes.com.ar/news/argentina/dying-becomes-a-luxury-as-economic-downturn-hits-home.phtml · Malay Mail (2020-01-03), https://www.malaymail.com/news/life/2020/01/03/dying-has-become-a-luxury-in-crisis-ridden-argentina/1824246 · BAE Negocios, https://www.baenegocios.com/negocios/cada-vez-mas-empresas-funebres-ofrecen-cremacion-de-perros-y-gatos-para-sumar-ingresos/ · Rebelión (cifra sin fuente; no usar), https://rebelion.org/el-valor-de-una-pena/
- Lo digital en sepelios: Ámbito (2020), https://www.ambito.com/informacion-general/coronavirus/velorios-virtuales-y-duelos-atipicos-las-otras-consecuencias-del-n5096392 · Economis (2020), https://economis.com.ar/coronavirus-por-la-cuarentena-podes-dar-el-ultimo-adios-online/ · plantillas de CapCut, https://www.capcut.com/es-es/explore/remembering-someone-who-passed-away

**Precios de restauración**
- Fiverr: https://www.fiverr.com/hatemdesigns/restore-your-old-photos · https://fiverr.com/illus1on1st/restore-fix-and-colorize-your-photos · https://fiverr.com/omarrh/colorize-black-and-white-photo
- Chile: https://www.2x3.cl/servicios/articulo/STzG8pu-restauracion-fotografias-antiguas-desgastadas · Portugal: https://www.custojusto.pt/setubal/emprego-servicos/servicos/outros-servicos/restauro-e-colorizacao-de-foto-45053261 · Panopticon: https://www.panopticonimaging.com/restoration/

**Del proyecto**
- `research/fuentes/2026-10-01-rapidas-personas-estacional.md` (ideas I19 e I20) y `research/2026-10-01-200-ideas-rapidas-1-semana.md`.
