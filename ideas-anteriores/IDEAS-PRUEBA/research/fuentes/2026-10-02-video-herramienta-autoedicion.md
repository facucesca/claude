# Informe fuente: herramienta propia de AUTO-EDICIÓN de video (2026-10-02)

**Pregunta:** ¿cómo construye un NO programador (con Claude Code) una herramienta local que reciba videos crudos de clientes y los devuelva editados "como un video realmente bueno", para vender un servicio de edición con marca anónima? ¿Qué existe ya, cuánto cuesta cada video, y conviene construir o usar SaaS?

**Fecha de corte de datos:** 2026-10-02. Precios en USD. Todo lo que no pude confirmar en página primaria o en ≥1 fuente secundaria reciente va marcado **[NO VERIFICADO]**.

**No repite** `research/2026-10-01-230-ideas-con-claude.md` ni `research/2026-10-01-200-ideas-rapidas-1-semana.md`: donde una idea se cruza con una ya listada (E12, E13, E37, I20, I28, I31), se indica qué aporta de nuevo.

---

## 0. Resumen ejecutivo (para leer primero)

1. **No hay que construir desde cero.** El 2026 dejó una pieza clave hecha: **`video-use`** (browser-use, licencia MIT, ~27.900 estrellas en GitHub al 2026-10-02) convierte a Claude Code en un editor: soltás el material en una carpeta, le describís lo que querés y devuelve `final.mp4` (quita muletillas y silencios, hace color, fundidos de audio, subtítulos y animaciones con Remotion/PIL). Es literalmente la idea del usuario. Se le suman **auto-editor** (silencios, dominio público), **faster-whisper/WhisperX** (transcripción por palabra), **OpenShorts** (MIT; cortes verticales con tracking de cara) y **FFmpeg** (ya instalado en la PC del usuario, v9.0).
2. **La PC del usuario alcanza para el MVP sin nube.** La revisé el 2026-10-02: Intel Core Ultra 7 258V (8 núcleos), GPU integrada Intel Arc 140V, 32 GB de RAM, 1,6 TB libres, FFmpeg 9.0 con Quick Sync (h264_qsv/av1_qsv) y Python 3.12. **Sin GPU NVIDIA**, así que no corre CUDA (WhisperX acelerado, pyannote rápido). Medido con un video sintético de prueba: 60 s en 1080p30 se codifican en **~10,7 s con x264 medium (CPU)** y en **~5 s con Quick Sync**. Un reel vertical con recorte y zoom: ~6,3 s por minuto. Con material real hay que esperar 2-3 veces eso.
3. **Costo directo de cada video con herramienta propia: USD 0,05-0,60** (transcripción local o Groq + Claude API + render local). Con SaaS: **USD 0,15-3 por video** según la herramienta, más el plan fijo de USD 15-70 por mes y límites de cuota. A volumen bajo la diferencia es chica. Lo que cambia es **el control de calidad, las recetas por cliente, la privacidad y que el servicio no dependa de un tercero**.
4. **Precio de mercado de la edición (fuentes de 2026):** un short o reel cuesta USD 25-75 con un editor principiante y USD 75-200 con uno intermedio. Un episodio de podcast cuesta USD 30-80 la edición básica y USD 80-175 la estándar; un videopodcast completo, USD 150-600. Servicios productizados como VidChops cobran USD 495 por mes por 16 shorts o 4 videos largos. **El margen está en el tiempo humano que la herramienta ahorra, no en el costo de la IA.**
5. **Qué se puede auto-editar bien:** talking heads, podcasts, testimoniales, webinars/clases, grabaciones de pantalla y videos desde fotos (propiedades, autos, productos). **Qué no:** narrativo, cinemático, eventos complejos con mucha cámara y deportes sin cámara fija. Ahí la IA hace un *pre-armado* y el oficio lo pone una persona.
6. **Recomendación:** construir propio, pero **ensamblando** (video-use + auto-editor + whisper + ffmpeg, con Remotion opcional), con revisión humana obligatoria. Las semanas 0-2 vender con un SaaS barato (Submagic, Gling u Opus) para validar demanda mientras se arma el pipeline. Detalle en la sección 11.

---

## 1. Metodología

- **~40 consultas de búsqueda web** (la cuota de WebSearch de la sesión se agotó en la consulta 41) y **~12 lecturas directas** de páginas primarias: precios de Claude (platform.claude.com), licencia de Remotion (GitHub), costos de Remotion Lambda, precios de Klap, OpusClip y Pixabay, y los READMEs de auto-editor, faster-whisper, WhisperX y video-use.
- **Medición local** en la PC del usuario el 2026-10-02: hardware y benchmark de codificación con FFmpeg (x264 contra Quick Sync, con video sintético `testsrc2`, que es más fácil de comprimir que el material real).
- **Criterio:** precios de lista de cada SaaS, con agregadores de precios cuando la página primaria no cargaba (castmagic, costbench, hooked.so, eesel). Los costos por video son cálculos propios con supuestos explícitos.
- **Sesgos señalados:** varias fuentes son blogs de competidores (por ejemplo, el blog de Submagic sobre los precios de Shotstack o el de AutoReel sobre costos inmobiliarios). Las tarifas de freelancers salen de guías de 2026 orientadas a EE. UU. y **no** son la mediana argentina.

---

## 2. Competencia SaaS (precios a 2026-10-02)

### 2.1 Tabla comparativa

| Herramienta | Qué hace bien | Qué hace mal / límites | Precio 2026 | Costo por video (supuesto: material de 10 min) | ¿API? |
|---|---|---|---|---|---|
| **OpusClip** | Clips verticales desde video largo, puntaje de viralidad, reencuadre, B-roll | Puntaje de viralidad poco confiable (usuarios de Reddit reportan que los clips "de bajo puntaje" rinden más), B-roll con errores, colas lentas, cancelación engorrosa (Trustpilot). No hace edición larga | Free (60 créditos); Starter USD 15/mes (150 créditos); Pro USD 29/mes (300 créditos); Business a medida. **1 crédito = 1 minuto de material de entrada** | Pro: 10 créditos ≈ **USD 0,97** (rinde 5-15 clips) | Sí, en Pro y Business (Video API, Scheduler API, MCP) |
| **Descript** | Edición por texto (editar el transcript edita el video), agente Underlord, voces | Desde septiembre de 2025 mide "media minutes" + créditos de IA. Pesado para volumen | Hobbyist USD 24, Creator USD 35, Business USD 65 por usuario y mes (anual: 16/24/50). Créditos de IA: 400/800/1.500 | ~USD 1-3 a volumen bajo **[NO VERIFICADO: cuota exacta de minutos por plan]** | No pública para automatizar |
| **CapCut** (Pro) | Editor completo y barato, plantillas, subtítulos | **Términos (2026-04-15):** licencia "perpetua, mundial, sublicenciable" sobre lo que subís, en plan gratis y pago → **mala opción para material de clientes**. La música integrada **no** tiene derechos comerciales. Sin API oficial. Riesgo regulatorio (ByteDance) | Pro USD 19,99/mes o USD 179,99/año (subió ~130% respecto del plan anterior) | Marginal ≈ 0, pero todo manual | **No** |
| **Submagic** | Subtítulos animados virales, zooms, B-roll, "Magic Clips" | Pensado para shorts; los videos largos solo en planes altos | Starter USD 19 (15 videos), Pro USD 39, Business+API USD 69 (100 videos/mes, hasta 30 min c/u, 100 min de API). Paquetes de API desde USD 0,23/min hasta USD 0,10/min | **USD 0,41-1,27** por video | Sí (Business) |
| **Captions / Mirage** | "AI Edit": estilos que cortan, ritman, subtitulan, ponen B-roll y música; avatares | Créditos opacos; fuerte en celular. Mirage levantó USD 75 M en marzo de 2026 (competidor con mucho capital) | Basic USD 9,99 (200 créditos), Max USD 24,99 (500), Frontier USD 69,99 (1.400) | **[NO VERIFICADO: créditos que consume AI Edit]** | API de pago (help.mirage.app) |
| **Gling** | Para YouTubers: saca silencios, muletillas y tomas malas; edición por texto; exporta a Premiere/Resolve/FCP | Solo el rough cut + extras; no hace "video terminado de agencia" | Free (1 exportación); Plus USD 10/mes anual (10 h); Pro USD 30/mes (30 h) | Pro: **~USD 0,17** | No |
| **AutoCut** (plugin) | Silencios, cortes con zoom, multicámara de podcast, subtítulos; Premiere y **DaVinci Resolve** | Requiere editor host y operador | Basic USD 6,60/mes anual; AI USD 14,90; Pro USD 19,80 | ~USD 0,2-0,5 + tu tiempo | No |
| **FireCut** (plugin Premiere) | Muchas automatizaciones en una suscripción | Requiere Premiere (más costo) | Pro USD 34/mes | ~USD 0,5 + Premiere | No |
| **AutoPod** | Multicámara de podcast en Premiere | Solo Premiere | USD 29/mes | — | No |
| **TimeBolt / Recut** | Cortadores de silencio de escritorio | Funcionalidad que auto-editor (gratis) ya cubre | "Precio a medida" según comparadores **[NO VERIFICADO]** | — | No |
| **Eddie AI** | Rough cut de entrevistas y documentales por conversación (modo "Night Shift" mostrado en NAB 2026) | Apunta a productoras; caro en suscripción | Créditos: paquetes desde USD 10 por 1.000, sin mensualidad; suscripción Pro desde USD 200/mes | ~USD 1-5 en créditos **[NO VERIFICADO]** | No pública |
| **Selects (Cutback)** | Pre-edición profesional: sincronización multicámara, rough cut; integra Premiere/FCP/Resolve | Beta en EE. UU. desde diciembre de 2025, >400 usuarios pagos; para editores pro | **Sin precio público** | — | No |
| **Vizard** | Clips + editor; API incluida en todos los planes pagos | Similar a Opus | Pro USD 29/mes anual (200 créditos); Business USD 49/mes anual | ~USD 0,3-0,5 por video **[estimado]** | **Sí, incluida** |
| **Klap** | Clips verticales en volumen, barato | Solo clips | Basic USD 14 (100 clips), Pro USD 39 (300), Pro+ USD 94 (1.000), facturación anual. API: USD 0,44 por video de entrada + 0,32 por short + 0,48 por exportación | **~USD 0,13 por clip** (plan); por API, ~USD 2,5 por video con 3 clips | Sí (pago por uso) |
| **Veed** | Editor web, traducción, voz clonada | IA fuerte solo en Pro | Base ~USD 12-19; Pro USD 49 por editor y mes | ~USD 1-3 | Limitada |
| **Kapwing** | Editor web colaborativo, plantillas (incluye subtítulos estilo Hormozi) | Créditos | Pro USD 24/mes (1.000 créditos); Business USD 64 (4.000) | ~USD 0,5-2 | No |
| **Riverside** (Magic Clips) | Graba + edita + clips; Magic Clips incluso en el plan gratis | Sirve si el cliente **graba** en Riverside; no procesa crudo de terceros | Pro USD 29/mes, Grow USD 39, Webinar USD 99 | — | No |
| **Adobe Premiere Pro** | Generative Extend (Firefly), Media Intelligence (búsqueda de clips por contenido), traducción de subtítulos a 27+ idiomas | Generative Extend consume créditos Firefly (desde USD 9,99 por 2.000). Curva de aprendizaje | Creative Cloud ~USD 23/mes **[NO VERIFICADO]** | — | UXP/ExtendScript (complejo) |
| **DaVinci Resolve 20/21** | **Gratis**: IntelliCut (silencios y diálogo), subtítulos animados, SmartSwitch (multicámara por hablante), IntelliScript (arma timeline desde guion) | **El scripting Python externo es solo de Studio** (USD 295, pago único); en la 21.1 Python pasó a ser exclusivo de Studio | Free / Studio USD 295 | 0 | Solo Studio |
| **Clipchamp** (Microsoft) | Auto-compose y subtítulos en el plan gratis; viene con Windows 11 | Básico | Free / Premium USD 11,99/mes | 0-0,5 | No |

### 2.2 Lectura de la tabla

- **Ninguna herramienta hace "crudo → video de agencia terminado" sola y con calidad pareja.** Opus, Klap y Vizard hacen clips. Gling, AutoCut y Resolve hacen rough cut. Submagic y Captions hacen el "look viral". Descript es un editor asistido. Eddie y Selects apuntan a productoras. **El hueco es la orquestación con criterio y receta por cliente**, que es justo lo que puede aportar Claude.
- **Las plataformas ricas en capital ya están en el producto masivo:** Mirage con USD 75 M (2026-03), Opus, Descript, CapCut/ByteDance y Adobe. Competirles **como SaaS** no tiene sentido (ver sección 12).
- **CapCut queda descartado para material de clientes** por la cláusula de licencia sobre el contenido subido y por la falta de derechos comerciales sobre su música.

### 2.3 ¿Usar SaaS y revender el servicio?

Es viable **para validar demanda** (semanas 0-2): Submagic Business+API (USD 69/mes, 100 videos) más Gling Pro (USD 30) cubren shorts y rough cuts. Costo fijo ~USD 100/mes. Problemas en régimen:
1. **Cuotas y créditos** que cambian (Descript cambió el modelo en septiembre de 2025, CapCut subió ~130%, OpusClip cambia créditos).
2. **"Look" genérico**: el cliente puede contratar la misma app por USD 15 por mes. Tu diferencial tiene que ser la receta y el criterio, no la app.
3. **Privacidad**: subís material de clientes a terceros con términos variables.
4. **Sin API o con API cara** en la mayoría, así que no se automatiza de punta a punta.

---

## 3. Stack open-source y APIs (qué usar, con licencia y costo)

| Pieza | Herramienta recomendada | Licencia | Costo | Nota para esta PC (Intel, sin NVIDIA) |
|---|---|---|---|---|
| **Orquestador de edición con LLM** | **video-use** (github.com/browser-use/video-use) | MIT | Gratis + transcripción + tokens de Claude | Diseño clave: *el LLM no mira el video, lo lee*: transcript por palabra (~12 KB) + tiras de fotogramas en PNG solo en los puntos de decisión → EDL → render → auto-evaluación (hasta 3 re-renders). Usa ElevenLabs Scribe por defecto; **reemplazable por whisper local o Groq** |
| Corte de silencios | **auto-editor** (WyattBlue) | Dominio público (Unlicense) | 0 | Hoy está escrito en Nim (binario, ya no Python). Exporta a Premiere XML, **DaVinci Resolve**, FCP, Shotcut y Kdenlive → **permite revisar y ajustar en Resolve gratis** |
| Transcripción con timestamps por palabra | **faster-whisper** (local) | MIT | 0 | CPU int8. Benchmark oficial: modelo *small* sobre 13 min de audio = 1 min 42 s en un i7-12700K (8 hilos). En esta PC espero 2-4 min con *small* y ~8-15 min con *large-v3-turbo* **[estimado, no medido]** |
| Ídem, en la nube y barato | **Groq whisper-large-v3-turbo** | API | **USD 0,04 por hora de audio** | 60 min se procesan en <16 s. Alternativas: Deepgram Nova-3 (USD 0,26/h batch), AssemblyAI (USD 0,15-0,21/h), ElevenLabs Scribe v2 (USD 0,22-0,40/h según fuente) |
| Alineación precisa + diarización | **WhisperX** + pyannote *speaker-diarization-community-1* | BSD-2 (WhisperX); modelo CC-BY-4.0 (requiere token de Hugging Face y aceptar condiciones) | 0 | Funciona en CPU (`--device cpu --compute_type int8`) pero lento; **solo hace falta en podcasts de 2+ voces** |
| Motor de render | **FFmpeg 9.0** (instalado) | LGPL/GPL | 0 | Medido: x264 medium ≈ 5,6× tiempo real con video sintético; **h264_qsv ≈ 12×** |
| Plantillas animadas (subtítulos, intros, lower-thirds, gráficos) | **Remotion** (React) | Licencia propia: **gratis para individuos y empresas con ≤3 empleados**; si no, Company License (Creators USD 25/asiento/mes; Automators USD 0,01 por render, mínimo USD 100/mes) | 0 mientras sea unipersonal | Render en Lambda ≈ USD 0,017 por video de 1 min y USD 0,10 por 10 min HD. Local en CPU es más lento que FFmpeg puro **[NO VERIFICADO: velocidad local]**. Tiene "Agent Skills" oficiales para Claude Code |
| Subtítulos animados estilo Hormozi | Archivos **ASS** generados desde los timestamps + FFmpeg (repo de ejemplo: nicolaigaina/ai-video-captions, 6 estilos) | Open source | 0 | Más rápido que Remotion; alcanza para el 80% de los casos |
| Clips verticales con seguimiento de cara | **OpenShorts** (mutonby; MIT, ~3.900 estrellas): faster-whisper + PySceneDetect + LLM puntúa momentos + FFmpeg + MediaPipe | MIT | 0 (usa Gemini Flash para puntuar; **reemplazable por Claude**) | MediaPipe corre bien en CPU |
| Detección de escenas | **PySceneDetect** | BSD-3 | 0 | El detector de contenido es más lento que el de umbral; usarlo solo con material multicámara o con B-roll |
| Edición de clips en Python | MoviePy | MIT | 0 | **Evitarla en producción**: más lenta que FFmpeg directo **[NO VERIFICADO con benchmark 2026]**; sirve para prototipos |
| Normalización de audio | FFmpeg `loudnorm` en dos pasadas, objetivo **-14 LUFS / -1 dBTP / LRA 11** (estándar de redes y YouTube) | — | 0 | — |
| Ducking de música | FFmpeg `sidechaincompress` (referencia: umbral ~0,015, ratio 6, ataque 200 ms, release 1.000 ms) | — | 0 | — |
| Reducción de ruido | **DeepFilterNet3** (mejor calidad; factor de tiempo real 0,19 en una notebook de un hilo) o **RNNoise** (`arnndn` de FFmpeg; casi gratis en CPU) | MIT/Apache · BSD | 0 | Ambos andan en CPU |
| B-roll de stock | **Pexels API** (uso comercial sin atribución obligatoria; 200 pedidos/hora y 20.000/mes) · Pixabay | Licencias Pexels/Pixabay | 0 | Prohibido reventa "standalone"; cuidado con marcas visibles |
| B-roll generado | **Higgsfield** (ya conectado) | Uso comercial **solo en planes pagos** (Starter USD 19, Plus USD 47-59, Ultra USD 99-129) | Por crédito | Usarlo como "plato premium", no por defecto |
| Música | Pixabay Music (licencia comercial, sin atribución) · biblioteca propia pagada (Epidemic, Artlist, etc.) | Ver riesgos | 0 / suscripción | **YouTube Audio Library: solo es segura para YouTube**; fuera de YouTube hay que verificar tema por tema. **Pixabay: puede recibir reclamos de Content ID retroactivos** |
| Visión para elegir tomas | Claude (imágenes de la tira de fotogramas) o Gemini Flash (~300 tokens por segundo de video; 10 min a 1 fps ≈ USD 0,05 con 2.5 Flash) | API | Centavos | Usar visión **solo en puntos de decisión** (enfoque de video-use) |
| Cerebro de decisiones (cortes, hook, títulos, orden, B-roll) | **Claude API**: Sonnet 5.5 (USD 2 / USD 10 por millón de tokens de entrada/salida) u Opus 5.5 (USD 4 / USD 20); Batch con −50%; lecturas de caché a 0,1× (0,05× en Opus 5.5) | API | Ver sección 6 | Los modelos 4.7+ usan un tokenizador que genera ~30% más tokens |
| Eye-contact / upscale | Riverside (incluido en Pro), Nvidia Broadcast (requiere RTX) | — | — | **Evitar en el MVP**: no hay RTX y pocos clientes lo valoran |

**Conclusión del stack:** para esta PC (Intel, sin NVIDIA), la combinación más barata y robusta es **transcripción con Groq (o faster-whisper local si el cliente exige que el material no salga) + Claude como editor + FFmpeg con Quick Sync para el render + ASS para subtítulos**. Remotion entra en la v2 para el "look premium" (intros y gráficos animados).

---

## 4. Arquitectura recomendada para un NO programador

### 4.1 Principios

1. **Todo local, nada expuesto a internet.** Sin servidor web público. El panel escucha **solo en 127.0.0.1**.
2. **La entrada llega por carpetas sincronizadas** (Google Drive para escritorio), no por un formulario propio en la web. Así no hay que manejar subidas, autenticación ni seguridad.
3. **Claude decide; FFmpeg ejecuta; vos aprobás.** Claude nunca "renderiza a ciegas": genera un **EDL** (lista de decisiones de edición en JSON) que queda guardado y versionado.
4. **Recetas en archivos simples** (YAML) por cliente: editables a mano y entendibles.
5. **Siempre hay salida a un editor humano**: el EDL se exporta a XML de DaVinci Resolve (gratis) para ajustar a mano los casos difíciles.

### 4.2 Diagrama

```
 CLIENTE                                    TU PC (Windows, local)
 ───────                                    ───────────────────────────────────────────────
 Sube crudos a                Google Drive para escritorio
 carpeta compartida  ───────► G:\Clientes\<cliente>\ENTRADA\  (sincroniza solo)
 (o WeTransfer → vos                      │
  lo copiás)                              ▼
                              [1] VIGILANTE (script Python, arranca con Windows)
                                  detecta archivo nuevo y estable → crea TRABAJO
                                          │
                                          ▼
                              [2] COLA (SQLite: trabajos.db)  estado: nuevo→procesando→
                                          │                   revisión→aprobado→entregado
                                          ▼
                              [3] PIPELINE por trabajo (un paso = un script chico)
                                  a. Normalizar: copia de trabajo, proxy 720p, audio WAV
                                  b. Transcribir: Groq (o faster-whisper local) → palabras+tiempos
                                  c. Limpiar audio: DeepFilterNet/RNNoise → loudnorm -14 LUFS
                                  d. Pre-corte: auto-editor (silencios) → lista de segmentos
                                  e. CEREBRO (Claude API): lee transcript + RECETA del cliente →
                                     EDL.json {cortes, orden, hook, títulos, zooms, B-roll,
                                     música, capítulos, 9:16/16:9}
                                  f. Visión puntual: tiras de fotogramas en puntos dudosos → Claude
                                     confirma o ajusta cortes (máx. 3 iteraciones)
                                  g. Render: FFmpeg (QSV) + subtítulos ASS + logo/intro/outro
                                     (+ Remotion en v2) → MP4 por formato
                                  h. Auto-chequeo: duración, picos de audio, subtítulos fuera de cuadro,
                                     fotogramas negros → semáforo
                                          │
                                          ▼
                              [4] PANEL LOCAL (http://127.0.0.1:8501, Streamlit o similar)
                                  ver video ▸ leer EDL en lenguaje humano ▸ botones:
                                  [Aprobar] [Re-hacer con nota: "hook más corto"] [Abrir en Resolve]
                                          │ aprobado
                                          ▼
                              [5] SALIDA: G:\Clientes\<cliente>\ENTREGAS\AAAA-MM-DD\ (Drive sincroniza)
                                  + aviso: mail por Gmail (borrador o envío) / WhatsApp manual
                                  + registro: minutos procesados, costo API, tiempo humano
```

### 4.3 La "receta" por cliente (ejemplo de archivo)

```yaml
# recetas/dra-perez.yaml
cliente: "Dra. Pérez - Dermatología"
formato_salida: [vertical_9x16, horizontal_16x9]
duracion_objetivo_short: 30-45 s
tono: "cercano, profesional, sin exagerar"
hook: "primera frase = problema del paciente; máx. 3 s"
subtitulos: {estilo: hormozi_suave, fuente: "Montserrat ExtraBold", color: "#FFFFFF", resaltado: "#F2A1B5", mayusculas: false}
zooms: {cada: 6-9 s, intensidad: 1.08}
broll: {fuente: pexels, maximo_por_minuto: 2, evitar: ["sangre", "jeringas"]}
musica: {carpeta: musica/calma_licenciada, volumen_bajo_voz: -22 dB}
logo: logos/dra-perez.png  # esquina sup. derecha, 70% opacidad
intro: null
outro: plantillas/outro_turnos.mp4
prohibido: ["prometer resultados", "antes/después sin consentimiento"]
```

Claude Code escribe y mantiene estos archivos. El usuario solo los lee o cambia valores.

### 4.4 Qué reutilizar del proyecto previo `proyectos/clipper-semiauto/PLAN.md`

| Pieza del clipper | ¿Se reutiliza? | Cómo |
|---|---|---|
| **Cola de aprobación** (Telegram, un tap) | **Sí, el concepto entero.** Es el mismo principio de "la IA propone, el humano aprueba". | En el MVP, el panel local reemplaza a Telegram. En la v2 se puede sumar aviso por Telegram con botones para aprobar desde el celular |
| Etapa [3] "corte automático + subtítulos + 9:16 + hook" | **Sí, pero mejorada.** El clipper delegaba en Higgsfield o en una API de terceros. | Ahora es el pipeline propio (pasos b-g). El clipper pasa a ser **un cliente más** del motor de edición |
| Reglas duras (publicación oficial, una cuenta, transformación real) | Sí, como cultura | Se traducen en "nunca publicamos por el cliente sin permiso; entregamos archivos" |
| Registro por pieza + gate con números | **Sí** | Mismo formato: AVANCE.md con piezas, minutos humanos, costo y aprobación del cliente al primer intento |
| Scanner de campañas Whop | No | No aplica a un servicio a clientes |
| Higgsfield | Parcial | Solo para B-roll generado o hooks visuales premium (plan pago por los derechos comerciales) |

---

## 5. Plan por fases (MVP → v2 → v3)

> Ritmo del usuario: 10-15 h por semana de construcción. Claude Code escribe todo; el usuario prueba con videos reales y decide.

### MVP — semanas 1-2: "talking head → reel vertical + versión horizontal limpia"
- **Hace:** recibe un video de una persona hablando a cámara (1-15 min). Saca silencios, muletillas y tomas repetidas. Normaliza el audio a -14 LUFS con reducción de ruido. Arma la **versión horizontal limpia** y **3 reels verticales de 30-60 s** con hook elegido por Claude, subtítulos animados (ASS), zooms suaves por receta, logo y música con ducking. Deja todo en una carpeta y lo muestra en el panel local para aprobar o rehacer.
- **No hace todavía:** B-roll automático, Remotion, multicámara, diarización, avisos automáticos, Drive (en el MVP se usa una carpeta local).
- **Base técnica:** clonar video-use + auto-editor + Groq (o faster-whisper) + FFmpeg QSV + plantillas ASS. Una receta YAML.
- **Criterio de salida:** 10 videos reales (propios o de conocidos) con **≥7 aprobados sin retoque manual de más de 10 min** y menos de 15 min de procesamiento por video de 10 min.
- **Costo:** USD 5-20 de API para todas las pruebas.

### v2 — semanas 3-6: "servicio vendible"
- Entrada por **carpeta de Google Drive compartida** por cliente y vigilante automático.
- **Cola** (SQLite) que procesa de noche y deja todo listo a la mañana.
- **B-roll** desde Pexels con filtro de pertinencia de Claude (máx. N por minuto, lista de temas prohibidos).
- **Remotion** para intro/outro, lower-thirds y títulos animados por marca (gratis mientras sea unipersonal).
- Exportación a **DaVinci Resolve** (XML) para el retoque humano.
- Aviso de entrega por **Gmail** (borrador automático que el usuario envía).
- Podcasts de 2 voces: diarización (WhisperX + pyannote; lento en CPU, alternativa por API) y cambio de plano por quién habla.
- Registro de costos y tiempos por trabajo.

### v3 — meses 2-4: "volumen y productos verticales"
- **Módulos por vertical:** video desde fotos (propiedades, autos, productos) a partir de plantillas Remotion + datos de la ficha; webinar → resumen + clips + capítulos; grabación de pantalla → instructivo con zoom a los clics.
- **Aprendizaje de la receta:** el panel guarda el motivo de cada "rehacer" y Claude propone ajustes a la receta del cliente (la receta mejora sola con el uso).
- Aviso y aprobación desde el celular (Telegram, reutilizando el diseño del clipper).
- Plan B de cómputo en la nube (Modal) para picos o para whisper *large* con GPU.
- Evaluar recién acá la productización (sección 12).

---

## 6. Costos

### 6.1 Costo directo por video (herramienta propia)

Supuesto: **material de 10 min de talking head → 1 horizontal limpio de ~6 min + 3 reels**.

| Concepto | Opción barata | Opción "máxima calidad" | Cálculo |
|---|---|---|---|
| Transcripción | faster-whisper local: **USD 0** | Groq turbo: **USD 0,007**; ElevenLabs Scribe: USD 0,04-0,07 | Groq a USD 0,04/h × 1/6 h |
| Claude, una sola llamada (transcript → EDL) | Sonnet 5.5: **~USD 0,05** | Opus 5.5: ~USD 0,10 | ~10.000 tokens de entrada (transcript en español + receta + instrucciones) × USD 2/M + ~3.000 de salida × USD 10/M |
| Claude agéntico estilo video-use (varios turnos + imágenes + auto-evaluación) | Sonnet 5.5: **~USD 0,20** | Opus 5.5: **~USD 0,40** | ~30.000 tokens de entrada sin caché + ~100.000 leídos de caché + ~12.000 de salida (estimado) |
| Visión (tiras de fotogramas) | Incluida arriba | Gemini Flash: ~USD 0,05 por 10 min a 1 fps | — |
| Render | Local: **USD 0** (luz) | Remotion Lambda: ~USD 0,02-0,10 | — |
| B-roll / música | Pexels/Pixabay: USD 0 | Higgsfield: créditos del plan pago | — |
| **Total directo** | **~USD 0,05-0,25** | **~USD 0,40-0,60** | — |

Con la **Batch API (−50%)**, si las entregas no son urgentes y se procesa de noche, el costo de Claude baja a la mitad.

### 6.2 Costo por video si se usa SaaS (mismo supuesto, plan amortizado a ~40 videos por mes)

| Opción | Fijo por mes | Costo por video | Observación |
|---|---|---|---|
| Submagic Business+API | USD 69 | ~USD 0,70-1,70 | Shorts con look viral; el largo con límite |
| Gling Pro + Submagic Starter | USD 30 + 19 | ~USD 1,2 | Combo rough cut + subtítulos |
| OpusClip Pro | USD 29 | ~USD 1 (10 créditos) | Solo clips |
| Klap Pro | USD 39 (anual) | ~USD 0,4 (3 clips) | Solo clips |
| Descript Creator | USD 35 | ~USD 1-3 **[NO VERIFICADO]** | Edición asistida, mucha mano |
| Resolve free + AutoCut AI | USD 14,90 | ~USD 0,4 | Todo manual, pero barato |

**Comparación:** la herramienta propia cuesta ~USD 0,05-0,60 por video **sin fijo** (o solo el de la Claude API). El SaaS cuesta USD 0,4-3 por video **más USD 30-100 de fijo**. A 40 videos por mes, el ahorro es de ~USD 30-100 por mes: **no es la razón principal para construir**. Las razones son calidad controlable, recetas, privacidad y no depender de cuotas ajenas.

### 6.3 Hardware y tiempos (medidos o estimados para esta PC)

| Paso (video de 10 min) | Solo CPU (esta PC) | Con GPU NVIDIA (no hay) | En la nube |
|---|---|---|---|
| Transcribir | 2-4 min (*small* int8) · 8-15 min (*large-v3-turbo*) **[estimado]** | <1 min | Groq: segundos |
| auto-editor | <1 min | — | — |
| Claude (EDL + revisiones) | 1-4 min (latencia de API) | — | — |
| Render horizontal 6 min 1080p | ~1-3 min (QSV) · 2-5 min (x264) **[extrapolado del benchmark ×2-3 por material real]** | ~1 min (NVENC) | Remotion Lambda: <1 min |
| 3 reels con subtítulos y zoom | ~1-3 min | <1 min | — |
| **Total por video** | **~8-25 min de máquina**, sin intervención | ~5 min | ~3-5 min |

- **Veredicto: alcanza con CPU + Quick Sync.** Con una cola nocturna procesa **30-60 videos por noche**. No hace falta comprar GPU (capital < USD 500).
- **Nube si hiciera falta:** Modal (T4 a USD 0,59/h; **USD 30/mes de crédito gratis** en el plan Starter ≈ 50 h de T4). RunPod serverless faster-whisper: USD 0,00025/s (3 min de audio en ~11 s). Replicate: precio por modelo **[NO VERIFICADO]**. Para esta escala, **Groq + render local** sale más barato y simple que cualquier GPU en la nube.

### 6.4 Costos fijos estimados del servicio

| Ítem | USD/mes |
|---|---|
| Claude API (100 videos × USD 0,2-0,4) | 20-40 |
| Groq (transcripción) | <1 |
| Google Drive (si se supera el espacio gratis: 100 GB-2 TB) | 2-10 **[NO VERIFICADO: precio AR]** |
| Música licenciada (opcional pero recomendada) | 10-20 **[NO VERIFICADO]** |
| Higgsfield (si se usa B-roll generado) | 19+ |
| **Total** | **~USD 35-90 por mes a 100 videos** |

---

## 7. Qué se puede auto-editar bien (y qué no)

| Tipo de video | Automatizable | Por qué |
|---|---|---|
| **Talking head** (profesional a cámara, coach, médico) | **80-90%** | Todo lo valioso está en el audio y el transcript: cortes, hook, subtítulos. El caso ideal |
| **Podcast / videopodcast** 1-3 voces | **70-85%** | Cambio de plano por hablante, clips, capítulos. Lo difícil: diarización con voces solapadas y elegir *el* mejor momento (sigue siendo criterio humano, ver la lección del clipper) |
| **Testimoniales** | **75-85%** | Estructura repetible: problema → solución → resultado |
| **Webinars / clases / Zoom** | **75-85%** | Resumen + capítulos + clips. La calidad de imagen de origen suele ser mala |
| **Grabaciones de pantalla / tutoriales** | **70-80%** | Zoom a los clics, cortes de silencios; requiere detectar el cursor (posible con FFmpeg/OpenCV) |
| **Tours inmobiliarios desde fotos** | **85-95%** | Plantilla + Ken Burns + datos de la ficha + música; casi sin juicio humano |
| **Catálogo de productos o autos desde fotos** | **85-95%** | Igual que el anterior |
| Vlogs / viajes con mucho B-roll propio | 40-60% | La IA elige mal las tomas sin hilo narrativo hablado |
| **Narrativos, cortos, publicidad cinematográfica** | **10-30%** | El valor es ritmo emocional, color y diseño sonoro; la IA solo hace pre-armado |
| **Eventos complejos** (bodas, recitales) multicámara | 20-40% | Sin guion, audio caótico, momentos visuales sin palabras |
| **Deportes amateur** (goles) | 30-50% | Sin cámara fija y sin "evento" de audio claro se pierden jugadas; los sistemas que lo hacen bien (Veo, Pixellot) venden **hardware de cámara**. OpusClip falla en gaming por la misma razón: corta tarde porque espera pausas de habla |
| Gaming / reacción | 40-60% | Mismo problema |

**Regla honesta:** "si el valor está en lo que se *dice*, se automatiza; si está en lo que se *ve* o se *siente*, no".

---

## 8. Riesgos

| Riesgo | Gravedad | Mitigación |
|---|---|---|
| **Calidad despareja** (cortes a mitad de palabra, hooks flojos, B-roll fuera de lugar) | Alta al inicio | Revisión humana obligatoria en el panel; auto-chequeos; receta por cliente; registrar cada "rehacer" para mejorar. **No prometer 100% automático** |
| **Derechos de música** | **Alta** | YouTube Audio Library = solo YouTube. Pixabay = licencia válida pero **Content ID puede reclamar retroactivamente** sin integración para resolverlo. CapCut = su música no tiene derechos comerciales. → Usar una biblioteca **pagada con licencia para clientes** o música generada con plan comercial, y guardar la licencia por pieza. Para Reels/TikTok, ofrecer "sin música" y que el cliente agregue un audio de tendencia dentro de la app |
| **B-roll** | Media | Pexels/Pixabay no permiten reventa standalone ni uso con marcas visibles; Higgsfield solo con plan pago. Registrar el origen de cada clip en el EDL |
| **Privacidad del material del cliente** (pacientes, datos) | **Alta** en salud y finanzas | Procesar local; transcripción local (faster-whisper) para clientes sensibles; **no usar CapCut** (licencia perpetua y sublicenciable sobre lo subido); acuerdo simple de confidencialidad; borrar crudos a los N días. Revisar la retención de datos de cada API (Groq, Anthropic) **[NO VERIFICADO en este informe]** |
| **Ley de datos personales AR** (Ley 25.326) y derecho a la imagen | Media | Consentimiento del cliente para su imagen y la de terceros; no usar el material de clientes como portfolio sin permiso |
| **Mantenimiento** (actualizaciones de FFmpeg, Python, APIs) | Media | Fijar versiones; un único `instalar.bat` que Claude Code mantiene; respaldo en GitHub privado; no actualizar en semana de entregas |
| **Dependencia de APIs** (Claude, Groq) | Media-baja | Cada paso con plan B: Groq → faster-whisper local; Claude Sonnet → Haiku 4.5 o Batch; Remotion → ASS |
| **Licencia de Remotion** si crece | Baja | Gratis para individuos o ≤3 empleados; desde el 4º empleado, Company License (Creators USD 25/asiento o Automators USD 0,01/render, mínimo USD 100) |
| **Competencia de las apps** (el cliente aprende a usar Captions/Submagic) | **Alta** | Vender **resultado + criterio + receta + tiempo ahorrado**, no "edición". Clientes que no quieren tocar nada (profesionales ocupados, agencias en volumen) |
| **Aprobación del cliente y revisiones infinitas** | Media | Paquetes con 1 ronda de cambios incluida; la receta documenta el estilo acordado |
| **Uso del plan de Claude Code** como motor de un servicio en régimen | Media | Para la cola automática, usar **API key con facturación propia**; Claude Code (plan del usuario) para construir y ajustar |

---

## 9. ¿Producto (SaaS) después? ¿Conviene?

- **Contra quién competiría un SaaS genérico:** Mirage/Captions (USD 75 M levantados), OpusClip, Descript, CapCut/ByteDance, Adobe y Blackmagic (Resolve gratis con IntelliCut y subtítulos animados). Más los open source (video-use, OpenShorts) que cualquiera instala gratis. **Un SaaS horizontal de edición es una mala idea**: nula diferenciación, soporte pesado y costos de cómputo por usuario.
- **Lo que sí se puede productizar sin "vender software" en sentido pesado** (alineado con el miedo del usuario):
  1. **Recetas/skills** de edición en español para Claude Code o video-use (archivo descargable, sin servidor, sin soporte 24/7): semi-pasivo.
  2. **Plantillas Remotion** de marca (ojo: el comprador con más de 3 empleados necesita su propia licencia de Remotion).
  3. **Servicio white-label para agencias** (sigue siendo servicio, pero en volumen y con "API humana": la agencia sube a una carpeta y recibe).
  4. **Vertical cerrado** (por ejemplo, "videos de propiedades desde la ficha" para inmobiliarias de habla hispana) **si** el servicio manual demuestra demanda. AutoReel cobra USD 30-249 por mes en inglés para EE. UU.; en español y para LatAm el hueco es real **[inferencia, no verificada con datos de demanda]**.
- **Recomendación:** primero **servicio** (aprender qué quiere el cliente y qué receta funciona). Productizar recién después de 30+ clientes o 500+ videos, y solo como vertical o recetas, nunca como editor generalista.

---

## 10. Ideas que salen de esta herramienta (20)

Columnas: % automatizable = trabajo que hace la máquina. Costo por pieza = directo (API + licencias), sin el tiempo humano. Margen bruto = (precio − costo directo) / precio. Los minutos humanos van aparte. Los precios de venta son **hipótesis** basadas en las tarifas de mercado de la sección 0, ajustadas a la baja para LatAm **[NO VERIFICADO con clientes AR]**.

| # | Idea | Qué es | % auto | Costo por pieza | Precio de venta | Margen bruto | Min humanos por pieza | Score |
|---|---|---|---|---|---|---|---|---|
| 1 | **Reels mensuales para profesionales** (médicos, abogados, contadores, coaches) | El cliente graba 1 h por mes "en tanda"; recibe 8-12 reels + 2 videos horizontales con su receta de marca | 80% | USD 0,3-0,6 por reel | USD 150-350 por mes (8-12 reels) | ~97% | 8-12 min por reel | **8** |
| 2 | **Edición white-label para agencias** de marketing/podcast | Mayorista: la agencia sube crudo a una carpeta y recibe editado con *su* marca; vos sos invisible | 75% | USD 0,3-1 | USD 15-30 por short · USD 40-90 por episodio | ~95% | 10-40 min | **7,5** |
| 3 | **Instructivos (SOP) desde grabaciones de pantalla** para PyMEs | El empleado graba la tarea; sale un instructivo con zoom a los clics, subtítulos y capítulos. **Sinergia directa con la consultora de procesos** (ideas/2026-09-07) | 75% | USD 0,2-0,5 | USD 30-80 por instructivo o pack USD 300 por 10 | ~98% | 15-25 min | **7,5** |
| 4 | **Videopodcast completo**: crudo → episodio + 5 shorts + capítulos + títulos | Para podcasters hispanos que graban en video. *Aporta respecto de E12*: el episodio largo y la multicámara, no solo clips | 70% | USD 0,5-1,5 | USD 60-150 por episodio | ~98% | 30-60 min | **7** |
| 5 | **Webinar/clase → paquete de contenido** | 1 resumen de 5 min + 6 clips + capítulos + texto para blog o mail | 75% | USD 0,5-1 | USD 60-150 por webinar | ~98% | 25-40 min | **7** |
| 6 | **Limpieza de clases para cursos online** (Hotmart/Teachable) | Silencios, muletillas, zoom, subtítulos, capítulos en lotes de 20-60 clases | 85% | USD 0,1-0,3 por clase | USD 10-25 por clase | ~98% | 5-10 min | **7** |
| 7 | **Videos de propiedades desde fotos de la ficha** | Tour con Ken Burns + datos + logo + música (+ voz IA opcional). Competidor AutoReel en EE. UU. (USD 30-249 por mes) | 90% | USD 0,05-0,3 | USD 5-15 por propiedad o USD 60-150 por mes por inmobiliaria | ~97% | 3-5 min | **7** |
| 8 | **Testimoniales editados** para PyMEs/clínicas/cursos | El cliente final graba con el celular respondiendo 5 preguntas guiadas; sale testimonial con lower-third y subtítulos | 80% | USD 0,2-0,4 | USD 25-60 por testimonial | ~99% | 10-15 min | **6,5** |
| 9 | **Videos de inventario para concesionarias y agencias de usados** | Desde fotos + ficha (año, km, precio) → reel por unidad. Spyne lo hace en EE. UU. con IA | 90% | USD 0,05-0,2 | USD 80-200 por mes por concesionaria | ~99% | 2-4 min | **6,5** |
| 10 | **Pre-edición (rough cut) para editores freelance** | Les entregás el XML para Premiere/Resolve ya cortado y subtitulado; ellos ponen el arte. B2B de editores | 85% | USD 0,1-0,5 por hora de material | USD 3-10 por hora de material | ~95% | 5 min | **6** |
| 11 | **Recaps de eventos desde clips de invitados** | Código QR → los invitados suben clips → montaje automático con música licenciada. *Aporta respecto de E37*: la mecánica de subida colectiva y el montaje automático | 60% | USD 0,5-2 | USD 50-150 por evento | ~97% | 30-60 min | **6** |
| 12 | **Avance de obra mensual** para constructoras y estudios de arquitectura | Fotos o clips semanales → video mensual (timelapse + hitos + datos) para inversores o clientes | 85% | USD 0,1-0,3 | USD 50-120 por mes por obra | ~99% | 10 min | **6** |
| 13 | **Reels gastronómicos** desde fotos y clips cortos del local | Abono de 8 piezas por mes para restaurantes y cafés con recetas por marca | 80% | USD 0,1-0,3 | USD 80-150 por mes | ~99% | 5-8 min | **6** |
| 14 | **Clips de prédicas y charlas** para iglesias, ONGs y cámaras empresariales | Volumen semanal estable (cultos o charlas de 45-90 min) → 4-6 clips + resumen | 85% | USD 0,3-0,8 | USD 80-200 por mes | ~99% | 15-20 min | **6** **[demanda AR no verificada]** |
| 15 | **Catálogo de productos en video** (Tiendanube/Mercado Libre) | Desde fotos del producto → video de 10-15 s por SKU en lote | 90% | USD 0,02-0,1 | USD 1-3 por SKU (mínimo 50) | ~97% | <1 min | **6** |
| 16 | **Subtitulado + doblaje ES↔EN/PT** de videos de creadores o cursos | Subtítulos en 3 idiomas + doblaje con voz IA (ElevenLabs u otro) | 70% | USD 0,5-3 por minuto **[NO VERIFICADO: costo de doblaje]** | USD 5-15 por minuto | ~70-90% | 5 min por minuto | **5,5** |
| 17 | **Video-presentaciones de candidatos** para consultoras de RR. HH. | Grabación guiada → video de 60 s con datos clave | 80% | USD 0,1 | USD 5-15 por candidato | ~99% | 5 min | **5** |
| 18 | **Recetas/skills de edición en español** para Claude Code o video-use (Gumroad/Whop) | Producto digital: recetas YAML + prompts + plantillas ASS. Semi-pasivo | 95% (una vez hecho) | ~0 | USD 19-49 cada uno | ~90% (fees) | 0 por venta | **5** |
| 19 | **Plantillas Remotion vendibles** (subtítulos animados, intros, lower-thirds) | Pack para devs y creadores técnicos. Mercado chico; el comprador con >3 empleados necesita licencia Remotion | 95% | ~0 | USD 29-99 por pack | ~90% | 0 por venta | **4,5** |
| 20 | **Highlights de fútbol amateur** (complejos de fútbol 5/torneos) | Cámara fija del complejo → detección de festejos por audio y visión → clips por partido | 40-50% | USD 0,5-2 por partido (visión) | USD 2-5 por jugador o abono del complejo | ~80% | 20-40 min | **4,5** (competidores con hardware propio; sin cámara fija no funciona) |
| — | *SaaS horizontal de auto-edición* | Competir con Opus/Captions/Descript | — | — | — | — | — | **3** (no recomendado ahora) |

**Las de score ≥ 7 (1-7) comparten motor:** talking head → transcript → EDL → render con receta. Construir el MVP de la sección 5 sirve para las siete.

---

## 11. Recomendación: construir vs. usar SaaS

**Construir propio, ensamblando open source, con un puente SaaS de 2 semanas.**

1. **Semanas 0-2 (en paralelo):** conseguir 2-3 clientes piloto (profesionales o una agencia) y entregar con **Submagic Starter/Pro + Gling** (~USD 50 por mes) más revisión manual. Objetivo: validar precio y qué valoran. No comprar nada más.
2. **Semanas 1-2:** construir el **MVP** sobre video-use + auto-editor + Groq/faster-whisper + FFmpeg QSV + ASS, con el material real de esos pilotos como set de prueba.
3. **Semana 3:** comparar a ciegas una pieza SaaS contra una propia del mismo crudo. Si la propia gana o empata en ≥7 de 10 piezas, **dar de baja el SaaS**.
4. **Nunca:** CapCut para material de clientes (licencia sobre lo subido); música de YouTube Audio Library fuera de YouTube; prometer "100% automático".
5. **Gate a la semana 8** (mismo estilo que el clipper): ≥3 clientes pagando, ≥USD 300 por mes, ≤15 min humanos por pieza y ≥70% de aprobación al primer intento → sigue y pasa a la v3 vertical. Si no se cumple → se archiva como herramienta interna (sirve igual para la consultora y para el contenido propio).

**Por qué no solo SaaS:** el costo por video es parecido, pero el SaaS (a) da el mismo look que el cliente consigue por USD 15 por mes, (b) sube material privado a terceros con términos cambiantes, (c) no permite recetas por cliente ni automatizar de punta a punta, y (d) sus cuotas y precios cambian cada año (Descript en 2025-09, CapCut +130%).

**Por qué no construir desde cero:** video-use y OpenShorts ya resolvieron el 60-70% del problema técnico con licencia MIT. Claude Code puede adaptarlos en días, no en meses.

---

## 12. Fuentes (consultadas 2026-10-02)

**Competencia y precios**
- [OpusClip pricing (castmagic, verificado 2026-08-20)](https://www.castmagic.io/blog/opus-clip-pricing) · [OpusClip pricing page](https://www.opus.pro/pricing) · [eesel: OpusClip reviews](https://www.eesel.ai/blog/opusclip-reviews) · [toolsforhumans: Opus Clip](https://www.toolsforhumans.ai/ai-tools/opus-clip)
- [Descript pricing 2026 (sonix)](https://sonix.ai/resources/descript-pricing/) · [castmagic: Descript](https://www.castmagic.io/es/blog/descript-pricing)
- [Submagic pricing (hooked.so)](https://www.hooked.so/compare/submagic-pricing) · [costbench Submagic](https://costbench.com/software/ai-video-editing-saas/submagic/)
- [CapCut ToS y precios (podcastle)](https://podcastle.ai/blog/capcut-terms-of-service) · [eesel: CapCut pricing](https://www.eesel.ai/en/blog/capcut-pricing) · [fluxnote: CapCut 2026-06](https://fluxnote.io/guides/capcut-questions-answered)
- [Captions/Mirage (eesel)](https://www.eesel.ai/blog/captions-ai) · [Mirage API pricing](https://help.mirage.app/docs/api/pricing) · [Ronda de USD 75 M (rutab, 2026-03-24)](https://rutab.net/b/hardware/2026/03/24/startap-mirage-privlek-75-mln-na-razvitie-ai-modeley-dlya-videoredaktora-captions.html)
- [Gling (Capterra)](https://www.capterra.co.uk/software/1041465/gling)
- [AutoEdit vs AutoCut vs FireCut vs AutoPod 2026](https://www.autoeditai.net/blog/autoedit-vs-autocut-vs-firecut-vs-autopod) · [AutoCut Capterra](https://www.capterra.com/p/10036511/AutoCut/) · [TimeBolt vs Recut (toolradar)](https://toolradar.com/compare/timebolt-vs-recut)
- [Eddie AI review 2026 (makerstack)](https://makerstack.co/reviews/eddie-ai-review/) · [Eddie AI en NAB 2026 (cined)](https://www.cined.com/eddie-ai-at-nab-2026-hands-on-demo-and-the-night-shift-mode/)
- [Cutback lanza Selects](https://www.theatdb.com/news/cutback-launches-selects-an-ai-pre-editing-tool-for-professional-video-production-teams)
- [Vizard API pricing docs](https://docs.vizard.ai/docs/pricing) · [Klap pricing](https://klap.app/pricing) · [Klap hidden costs (costbench)](https://www.costbench.com/software/ai-video-editing-saas/klap/hidden-costs/)
- [Kapwing pricing (costbench)](https://costbench.com/software/video-editing/kapwing/) · [VEED alternatives (nemovideo)](https://www.nemovideo.com/blog/veed-alternatives)
- [Riverside pricing 2026 (castmagic)](https://www.castmagic.io/blog/riverside-pricing)
- [Adobe: IA en Premiere 25.2](https://blog.adobe.com/en/publish/2025/04/02/introducing-new-ai-powered-features-workflow-enhancements-premiere-pro-after-effects)
- [DaVinci Resolve 20 (postmagazine)](https://www.postmagazine.com/Press-Center/Daily-News/2025/Blackmagic-Design-releases-V-20-of-DaVinci-Resol.aspx) · [Resolve free vs Studio (thepostflow)](https://thepostflow.com/post-production/video-editing/resolve-studio-vs-free/) · [Foro Blackmagic: Python en la versión free](https://forum.blackmagicdesign.com/viewtopic.php?p=438043)
- [Clipchamp pricing (Capterra)](https://www.capterra.com/p/202357/Clipchamp/pricing/)
- [AutoReel: costos de video inmobiliario 2026](https://www.autoreelapp.com/blog/real-estate-video-cost-breakdown-diy-vs-videographer-vs-ai-in-2026) (fuente con conflicto de interés) · [Spyne (softwarefinder)](https://softwarefinder.com/sales-tools/spyne)

**Stack y APIs**
- [video-use (GitHub, MIT)](https://github.com/browser-use/video-use) · [Loudness en video-use](https://instagit.com/browser-use/video-use/loudness-normalization-targets-video-use.md)
- [auto-editor (GitHub)](https://github.com/WyattBlue/auto-editor) · [faster-whisper (GitHub)](https://github.com/SYSTRAN/faster-whisper) · [WhisperX (GitHub)](https://github.com/m-bain/whisperX)
- [OpenShorts (addrom)](https://addrom.com/openshorts-self-hosted-ai-shorts-studio-with-no-subscriptions/) · [AI-Youtube-Shorts-Generator: smart cropping](https://www.mintlify.com/SamurAIGPT/AI-Youtube-Shorts-Generator/features/smart-cropping) · [ai-video-captions (GitHub)](https://github.com/nicolaigaina/ai-video-captions)
- [Licencia de Remotion (GitHub)](https://github.com/remotion-dev/remotion/blob/main/LICENSE.md) · [Remotion pricing](https://www.remotion.dev/docs/license/pricing) · [Remotion Lambda cost example](https://www.remotion.dev/docs/lambda/cost-example) · [Remotion Agent Skills + Claude Code (tella)](https://www.tella.com/blog/how-to-use-remotion-agent-skills-with-claude-code.md)
- [Shotstack pricing (blog de Submagic, competidor)](https://www.submagic.co/blog/shotstack-pricing) · [Creatomate pricing](https://creatomate.com/pricing) · [Creatomate: cálculo de créditos](https://creatomate.com/docs/account/how-are-credits-calculated) · [JSON2Video plans](https://json2video.com/docs/v2/pricing/plans)
- [Precios de Claude API](https://platform.claude.com/docs/en/about-claude/pricing)
- [Groq pricing 2026 (eesel)](https://eesel.ai/blog/groq-pricing) · [Groq whisper turbo](https://groq.com/whisper-large-v3-turbo-now-available-on-groq-combining-speed-quality-for-speech-recognition/) · [Deepgram Nova-3](https://convertaudiototext.com/blog/deepgram-nova-3-explained) · [Comparativa STT 2026](https://convertaudiototext.com/blog/speech-to-text-api-pricing-2026) · [ElevenLabs API pricing](https://developer.puter.com/tutorials/elevenlabs-api-pricing/)
- [Gemini: costo real de video (Fora Soft, 2026-05-23)](https://www.forasoft.com/learn/ai-for-video-engineering/articles-ai/real-cost-of-ai-in-video-products-gemini-openai-pricing)
- [Modal pricing 2026 (spheron)](https://www.spheron.network/blog/modal-gpu-pricing-2026-per-second-billing/) · [RunPod faster-whisper endpoint](https://www.runpod.io/blog/faster-whisper-serverless-endpoint)
- [DeepFilterNet2 (arXiv)](https://arxiv.org/pdf/2205.05474) · [DeepFilterNet3 vs RNNoise (Sinergi)](https://publikasi.mercubuana.ac.id/index.php/sinergi/article/view/21917)
- [NVENC vs x264 (foro NVIDIA)](https://forums.developer.nvidia.com/t/turing-h-264-video-encoding-speed-and-quality/148793) · [PySceneDetect (PyPI)](https://www.pypi.org/project/scenedetect/0.5.6/)

**Licencias de medios**
- [Licencia de Pixabay](https://pixabay.com/service/license-summary/) · [Content ID y Pixabay (thematic)](https://hellothematic.com/thematic-vs-pixabay/) · [YouTube Audio Library fuera de YouTube (lickd)](https://lickd.co/youtube-audio-library/) · [Pexels API (openreplay)](https://blog.openreplay.com/free-stock-photo-resources/) · [Higgsfield pricing (creatify)](https://creatify.ai/blog/higgsfield-pricing-(2026)-plans-and-what-you-ll-actually-pay)

**Mercado de servicios de edición**
- [Tarifas de editores 2026 (sidestackers)](https://www.sidestackers.com/rates/video-editor) · [Cuánto cuesta editar video en 2026 (adsnipper)](https://adsnipper.com/?p=2494) · [Tarifas de editores de podcast 2026 (biztoolkit)](https://www.biztoolkit.co/post/podcast-editor-rates-in-2026-per-episode-pricing-guide) · [Tarifas de producción de podcast (jobbers)](https://www.jobbers.io/podcast-production-freelancing-equipment-rates-client-guide-2026/) · [VidChops pricing (saasworthy)](https://www.saasworthy.com/product/vidchops/pricing) · [La trampa de la edición "ilimitada" (tastyedits)](https://www.tastyedits.com/unlimited-video-editing-the-subscription-trap/)

**Medición local (2026-10-02):** CPU Intel Core Ultra 7 258V (8 núcleos), Intel Arc 140V, 32 GB de RAM, FFmpeg 9.0 (gyan full build) con h264_qsv/av1_qsv, Python 3.12.10. Benchmark de 60 s en 1080p30 (`testsrc2`): libx264 medium 10,7 s · h264_qsv 5,0 s · vertical 9:16 con recorte, escala y zoompan (x264 veryfast) 6,3 s.
