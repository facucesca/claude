# Indagación a fondo: SER-4-4, validar certificados médicos de empleados con IA

Fecha: 2026-10-15. Investigador: Claude (subagente). Tema único: SER-4-4 del registro (`research/datos/registro-de-ideas.csv`, línea 822). La parte de RFID para fichar ya se había descartado. Acá solo se estudia la validación de certificados.

**Cómo leer este documento**

- **[DATO]**: verificado, con fuente y fecha.
- **[ESTIMACIÓN]**: cálculo mío, con el razonamiento a la vista.
- **[OPINIÓN]**: mi juicio, discutible.
- "No lo pude verificar" quiere decir exactamente eso.

**Resumen en 6 líneas**

1. **El Decreto 407/2026 existe y es real.** Lo leí en el Boletín Oficial, incluido el anexo: se publicó el 2026-06-01. Exige que todo certificado con reposo sea **electrónico**, emitido por una plataforma registrada en **ReNaPDiS** y firmado por un médico habilitado en **REFEPS**. Además tiene que decir diagnóstico, tratamiento y días de reposo.
2. **La base de médicos que imagina Facu existe:** es REFEPS, dentro de SISA (Ministerio de Salud). Cualquiera la puede consultar a mano. La consulta automática (servicio web WS020) existe, pero pide usuario, clave y autorización del Ministerio, y no sé si se la darían a una empresa privada.
3. **La base de certificados que imagina Facu no existe para los empleadores** (al menos, no la encontré). Hay repositorios de recetas, pero el acceso garantizado es para las autoridades sanitarias.
4. **Fraude:** en Argentina no hay una cifra nacional. Hay casos fuertes en el sector público: en Río Negro (2024), 2 médicos firmaron 472 certificados y el gobierno estimó 6.602 días no trabajados. Ojo: eran **médicos reales**. Revisar la matrícula no los habría detectado; buscar patrones sí.
5. **Afuera ya existe casi exactamente este producto:** Closecare (Brasil) dice tener "agentes de IA" que validan certificados, con más de 200 mil documentos por mes (dato de la propia empresa).
6. **Filtro: 16/25 → PENDIENTE.** Se puede validar barato, pero el riesgo legal es alto (datos de salud), la demanda privada no está probada y el propio Estado puede terminar dando la verificación gratis.

---

## 1. Qué es exactamente (especificación integrada con lo que pidió Facu)

### El problema

- [DATO] Desde la reforma laboral, el art. 210 de la Ley de Contrato de Trabajo (sustituido por el art. 45 de la Ley 27.802, publicada en el B.O. el 2026-03-06) dice que el certificado tiene que contener **diagnóstico, tratamiento y cantidad de días de reposo**. También dice que lo emite un profesional habilitado, con firma por plataformas autorizadas por la Ley 27.553. Fuente: texto actualizado en Infoleg.
- [DATO] El Decreto 407/2026 (firmado el 2026-05-29, B.O. 2026-06-01, vigente desde ese día) reglamenta el art. 210 en su Anexo I, art. 6. Textual: la prescripción con reposo debe "ser emitida electrónicamente mediante sistema de información o plataforma digital debidamente registrada en el REGISTRO NACIONAL DE PLATAFORMAS DIGITALES SANITARIAS (ReNaPDiS) y suscrita por profesional habilitado ante la RED FEDERAL DE REGISTROS DE PROFESIONALES DE LA SALUD (REFEPS)". El papel queda solo como excepción, si hay falta de conectividad o caída de sistemas "debidamente acreditadas".
- [OPINIÓN] Para RR.HH., eso convierte cada certificado en una lista de chequeo nueva: ¿tiene los 3 datos? ¿la plataforma está registrada? ¿el médico está habilitado? ¿llegó en papel y, si es así, se justifica? ¿avisó el primer día? (art. 209). Hoy eso lo hace una persona a ojo, si es que lo hace.

### Quién paga (hipótesis, sin validar)

- [OPINIÓN] El comprador más probable es el **responsable de RR.HH. o de liquidación de sueldos** en empresas de 50 a 1.000 empleados con mucha gente en planta, local o turno: comercio, gastronomía, logística, industria, seguridad, limpieza, call centers.
- [OPINIÓN] Un segundo comprador posible: las **empresas de medicina laboral** que ya venden control de ausentismo. Ya cobran por un ítem llamado "control remoto de licencias" (ver sección 2). Para ellas sería una herramienta interna, y además ya tienen médicos, que son los únicos que pueden opinar sobre un diagnóstico.
- [DATO] El sector público también sufre el problema (caso Río Negro, sección 2). Pero venderle al Estado implica licitaciones, que son lentas.

### Qué haría el producto (versión realista, integrando la idea de Facu)

Facu pidió: "que lo busque en una base de datos de certificados y lo compare con lo que está ahí y con el médico que está ahí". Con lo que verifiqué, el producto posible es este:

1. **Recibir** el certificado (PDF o foto) por WhatsApp, mail o web. Es lo mismo que ya hace CEMEVA con documentos.
2. **Leerlo con IA:** empleado, DNI, médico, matrícula, plataforma emisora, diagnóstico, días, fechas.
3. **Chequeo de forma:** ¿tiene diagnóstico, tratamiento y días? ¿es electrónico? Si es papel, ¿se invocó la excepción?
4. **Chequeo del médico contra REFEPS:** ¿existe?, ¿tiene la matrícula habilitada?, ¿la profesión es la correcta? (a mano al principio; automático solo si el Ministerio da acceso al WS020).
5. **Chequeo de la plataforma:** ¿está en el listado público de plataformas aprobadas?
6. **Chequeo de autenticidad del documento:** si trae QR o enlace de la plataforma (Santa Fe lo trae), abrirlo y comparar con el original. Si el PDF trae firma digital, verificarla. **No sé** qué porcentaje de los certificados reales trae una firma verificable: hay que verlo con certificados reales.
7. **Patrones dentro de cada empresa** (lo que de verdad habría destapado el caso Río Negro): mismo médico firmando para muchos empleados, certificados en serie, lunes y viernes, días pegados a feriados.
8. **Salida:** un semáforo con el motivo ("médico no figura en REFEPS", "plataforma no registrada", "falta diagnóstico", "patrón raro"), más un botón para pedir el control médico. **La IA no decide.** Decide RR.HH. o el médico laboral.

### Cómo se cobra (estimación)

- [ESTIMACIÓN] Hay dos formas posibles. Una: por certificado procesado. Otra: un abono por empleado por mes. Referencia de precio verificada: en octubre de 2025, la Auditoría General de la Nación pagaba **$12.000 por cada "control remoto de licencias"** y **$24.000 por cada visita a domicilio en CABA**. Un chequeo de software tendría que costar una fracción de eso, por ejemplo $2.000 a $4.000 por certificado a precios de octubre de 2025. Ese número es mío y no está validado con nadie. No lo pasé a dólares porque no verifiqué el tipo de cambio de esa fecha.

---

## 2. Mercado en Argentina

### Tamaño

- [DATO] Asalariados registrados del sector privado: **6,082 millones en julio de 2026**. Fuente: informe "Situación y evolución del trabajo registrado (SIPA)", Secretaría de Trabajo, octubre de 2026.
- [DATO, fuente secundaria] "Durante el tercer trimestre de 2025, el 12,6% de los empleados privados registrados faltó al menos un día al mes". Además, "el 49% de los empleados ausentes fue por enfermedades no laborales" y "un 20% de las faltas ocurrió sin aviso". Lo dijo Jorge Colina (IDESA), según El Economista del 2026-02-19. **No vi el informe original de IDESA.**
- [ESTIMACIÓN] 6,08 M × 12,6% × 49% ≈ **375.000 empleados privados por mes** que faltan por enfermedad, y en general cada uno trae un certificado. Es un orden de magnitud, no un dato: puede estar ±50%. Supone un certificado por persona y por mes, y no todos los días de falta llevan certificado (hay convenios que piden certificado recién desde cierto día).
- [ESTIMACIÓN] Si se cobrara $3.000 por certificado y se lograra el 1% del mercado: 3.750 certificados × $3.000 = **unos $11 millones por mes**, a precios de octubre de 2025. Con el 5%, unos $56 millones por mes. Son números ilustrativos que dependen de un precio que nadie aceptó todavía.

### ¿Las empresas ya pagan por controlar esto?

- [DATO] Sí, por el **control médico**, no por el software. La Auditoría General de la Nación adjudicó la Licitación Pública 12/2025 (aviso del B.O. del 2025-10-20) a Centro Médico del Plata S.R.L., con estos precios unitarios:

| Ítem | Precio unitario (oct-2025) |
|---|---|
| Control de ausentismo en consultorio | $18.000 |
| Control en domicilio (CABA) | $24.000 |
| Control en domicilio (hasta 20 km de CABA) | $29.000 |
| Control en domicilio (hasta 40 km) | $31.000 |
| Control en domicilio (hasta 50 km) | $42.000 |
| **Control remoto de licencias** (corto y largo tratamiento, etc.) | **$12.000** |
| Evaluación de licencias por especialista | $32.000 |

- [DATO] En esa licitación, la oferta de "Medicina Laboral para Empresas S.A." fue declarada inadmisible. O sea, hay al menos 2 proveedores privados de este rubro que se presentan a licitaciones.
- [Dato no abierto] Según el resumen del buscador, en la licitación 6/2024 de la misma AGN el control en CABA costaba $16.000 y el remoto $8.000. No abrí ese aviso.
- [DATO viejo] En 2017, según Mercer Marsh Beneficios, el 54% de las empresas relevadas aplicaba políticas para bajar el ausentismo (iProfesional, 2017-05-18). En 2019, Adecco Argentina listaba el "control médico domiciliario" y "el control de los certificados presentados" entre las medidas de las empresas, sin porcentajes (Ámbito, 2019-09-07). Son datos viejos y no sirven para medir el mercado de hoy.

### ¿Qué tan común es el certificado falso? (pregunta 3 de Facu)

- [DATO] **No encontré ninguna cifra nacional ni encuesta de RR.HH. sobre certificados falsos en Argentina.** Hay casos judiciales y administrativos, casi todos del **sector público**:
  - **Río Negro, 2024.** Según el gobernador Alberto Weretilneck (La Nación, 2024-06-25), 2 médicos de General Roca y Villa Regina entregaron **472 certificados** entre diciembre de 2023 y mayo de 2024 a policías y a empleados de Educación y de Salud. Eso equivale a **6.602 días no trabajados** y a más de **$400.000.000** de costo para la provincia. "En algunos casos se emitían 20 o 30 certificados por día" (gobierno de Río Negro, 2024-06-24). Más de 20 médicos investigados. Según el gobernador, los certificados se daban por WhatsApp, sin consulta. Una médica fue cesanteada después de emitir 65 certificados. La denuncia se hizo por fraude (art. 174 inc. 5 del Código Penal) y por certificado médico falso (art. 295).
  - **Cómo se detectó:** por las juntas médicas provinciales y por el aumento de certificados que llegaban a RR.HH. de cada ministerio. Un mismo médico atendía empleados en distintas partes de la provincia. **Fue detección por patrones, no por una base de datos.**
  - Chubut (2025), un médico con más de 50 certificados falsos; y Provincia de Buenos Aires, una banda que vendía certificados a docentes: **solo los vi en el resumen del buscador; no abrí esas notas.**
- [DATO, Brasil, como referencia] El consejo médico de Bahía (Cremeb) recibió 1.505 pedidos de verificación de certificados en un año y **203 eran falsos (13%)** (Correio, 2024-11-05). Ojo: esa muestra está sesgada, porque solo se mandan a verificar los que ya parecen dudosos. La startup Closecare estimó en 2022 que "cerca de 13%" de los certificados se validan indebidamente. Es la estimación de una empresa interesada y no muestra método (Jornal Contábil, 2022-04-28).
- [OPINIÓN] El problema existe y es caro cuando aparece. Pero en el sector privado argentino **no hay evidencia pública de cuán frecuente es**. Eso es justo lo que tiene que medir el experimento de la sección 8.

### Por qué ahora

- [DATO] La Ley 27.802 (B.O. 2026-03-06) y el Decreto 407/2026 (B.O. 2026-06-01) cambiaron las reglas este año. La prensa lo describe como "nuevo foco de conflicto entre trabajadores y empleadores" (La Capital MdP, 2026-07-03).
- [OPINIÓN, punto incómodo] El "por qué ahora" corta para los dos lados. La misma norma que crea la necesidad de chequear también **achica el problema del documento trucho**: si todo certificado tiene que ser electrónico, venir de una plataforma registrada y estar firmado por un médico de REFEPS, falsificar un papel con Photoshop sirve menos. Lo que sigue intacto es el **médico real que firma de favor**, como en Río Negro. Eso no se detecta con una base: se detecta con patrones y con control médico.

---

## 3. Qué existe en Argentina y afuera (verificado)

### Argentina: lo oficial

| Qué | Qué es | ¿Lo puede usar un tercero? | Fuente |
|---|---|---|---|
| **REFEPS / SISA** (Ministerio de Salud) | Registro nacional de profesionales de la salud. Se alimenta de las provincias y de los colegios | **Sí, a mano.** "Toda persona que desee verificar si un profesional de la Salud está matriculado y habilitado para ejercer" puede entrar a sisa.msal.gov.ar y buscar por documento, matrícula o apellido y nombre | Instructivo oficial (jun-2024) y ayuda SISA |
| **WS020** (servicio web de REFEPS) | Consulta automática de profesionales: devuelve nombre, DNI, matrícula, profesión, jurisdicción y estado (habilitada o no) | **Restringido:** "se requiere cuenta en el sistema y permisos de acceso". Hay cupo diario y la autorización la da la Dirección Nacional. Los servicios "están orientados al sistema público de salud". Se pide con el "Formulario A1" | Ayuda en línea SISA |
| **ReNaPDiS** | Registro de plataformas digitales de salud (recetarios, repositorios, teleasistencia). Creado por la Res. MSAL 1959/2024 | Hay un listado público de "plataformas aprobadas" en argentina.gob.ar. No pude contar cuántas hay (la página se cortó) | argentina.gob.ar |
| **Repositorios de recetas + CUIR** | Toda prescripción lleva una Clave Única de Identificación de Receta. Los repositorios guardan la receta y mandan la información al Ministerio (Res. MSAL 2214/2025, arts. 2, 6 y 7) | **No para empleadores.** El art. 2 obliga a garantizar "los mecanismos de acceso correspondientes a las autoridades sanitarias competentes". No encontré acceso para empresas | Res. 2214/2025 (B.O. 2025-07-21) |
| **Res. 1648/2022** (REFEPS) | Prevé una "herramienta digital de consulta pública" y acuerdos de uso con "más de CIEN (100) organismos e instituciones" (RENAPER, obras sociales, etc.) | Las vías de acceso de terceros dependen de cada jurisdicción; la norma no fija reglas para privados | argentina.gob.ar/normativa |

- [DATO] El Decreto 407/2026 le ordenó al Ministerio de Salud dos cosas: en 30 días, fijar las condiciones para que las plataformas permitan "texto libre" en los certificados; en 60 días, aprobar el procedimiento de los institutos públicos para las discrepancias. **No encontré esas resoluciones.** Puede que existan y no las haya hallado, o que estén demoradas. La Res. MSAL 638/2026 (B.O. 2026-06-05) trata de identificación del paciente en recetas (token), no de certificados.

### Argentina: lo privado o provincial

- [DATO] **Santa Fe:** la Caja de Arte de Curar y los Colegios de Médicos lanzaron www.certificadomedicosantafe.org.ar. El médico firma digitalmente y el certificado llega al celular del paciente "con un código QR de validación" para mandarlo a escuelas, clubes o empleadores. Tiene unos 5.000 profesionales activos (El Litoral; la nota no muestra la fecha, probablemente julio de 2026). Es la prueba de que **una base con verificación puede existir, pero la arma el colegio médico, no una startup.**
- [DATO] Proveedores de control de ausentismo: **Centro Médico del Plata S.R.L.** y **Medicina Laboral para Empresas S.A.** (licitación de la AGN, arriba). "Medical Service" apareció en un aviso de empleo: **no lo verifiqué**.
- [DATO] **No encontré software argentino que valide certificados con IA** (búsquedas del 2026-10-15). Eso no prueba que no exista. Certuma, de Martín Varsavsky, es un copiloto clínico para médicos: no es lo mismo.

### Afuera

| Empresa / sistema | País | Qué hace | Clientes pagando / estado | Fuente |
|---|---|---|---|---|
| **Closecare** | Brasil | "Um time de agentes de IA especialistas em gestão de atestados": recibe, lee, chequea legibilidad y duplicados, verifica el registro del médico en bases oficiales, abre el QR para traer el original, verifica la firma en el ITI y analiza "11 tipos de rasuras". También detecta ausencias frecuentes y arma tableros | Según la propia empresa: "mais de 200 mil documentos por mês" y unos 22 logos de clientes. Precio a pedido | closecare.com.br |
| **Pipefy, agente de validación de certificados** | Brasil / global | Cruza el certificado con las políticas internas y lo registra. No dice que verifique autenticidad | Según la empresa: −70% de errores y −90% de tiempo. Precio a pedido | pipefy.com |
| **Atesta CFM** | Brasil (Consejo Federal de Medicina) | La "base de certificados" que imagina Facu: las empresas validan en validar.atestacfm.org.br con el código del documento | **Suspendida por la Justicia Federal desde noviembre de 2024**, tras una demanda del Movimento Inovação Digital (más de 180 empresas digitales). Al 2025-12-11 seguía sin funcionar | Correio (2024-11-05), Aos Fatos (2025-12-11), Tribuna Online |
| **INSS / Atestmed** | Brasil (Estado) | IA que cruza bases: CRM del médico, caligrafía, envíos masivos desde una misma IP | Anunciado el 2023-12-07; sin cifras de resultados | Baguete |
| **MedHelp Care** | Suecia | El empleado avisa que está enfermo por app, web o teléfono; lo atiende una enfermera y se avisa al jefe y a RR.HH. Seguimiento de licencias largas. **No es verificación de certificados**: es gestión del aviso | Casos con Saab (~15.000 empleados) e Inter IKEA (~5.000). La empresa dice ~500 organizaciones en una página y "over 100 leading companies" en otra: sus propias cifras no coinciden | medhelp.se |
| **Softworks** | Irlanda | Gestión de ausencias: registro, carga de certificados, vuelta al trabajo, factor Bradford. **No dice que verifique certificados** | Muestra logos de Intel, Hertz, Tesco (sin verificar) | softworks.com |
| **eAU** | Alemania (Estado) | Desde el 2023-01-01, el empleador está **obligado** a pedirle los datos de incapacidad a la caja de salud del empleado, en forma electrónica. El papel desapareció para el empleador | Sistema público. La página de la AOK muestra que el empleador recibe el período de baja, sin mencionar diagnóstico ni médico. Según der-betrieb.de (solo vi el resumen del buscador), no se transmite qué médico la emitió | aok.de |

- [OPINIÓN] Lo de afuera enseña tres cosas:
  1. **El producto de Facu ya existe y vende en Brasil** (Closecare). Es buena señal de demanda y mala señal de "ser el primero".
  2. **Donde hay una base central de certificados, la arma el Estado o el colegio médico** (Alemania, Brasil, Santa Fe), no una startup.
  3. Cuando la base es del Estado, **el empleador recibe menos datos, no más**: Alemania no le pasa ni el diagnóstico ni el médico.

---

## 4. Cómo se construiría y cuánto costaría (estimación)

### ¿Se puede consultar una base oficial automáticamente?

| Chequeo | ¿Automático hoy? | Cómo |
|---|---|---|
| Médico habilitado (REFEPS) | **No, sin permiso.** El WS020 existe, pero pide usuario, clave, cupo y autorización discrecional del Ministerio, orientada al sistema público | Al principio, a mano en SISA (1 a 2 minutos por consulta: estimación mía). Se pide el WS020 con el Formulario A1 y se ve qué contestan. **No recomiendo "raspar" el buscador público**: es una zona gris legal y técnica, y si la tapan, el producto se cae |
| Plataforma registrada (ReNaPDiS) | Casi: el listado es público, aunque no sé si está en un formato fácil de leer con una máquina | Se baja el listado y se compara |
| Certificado auténtico | **Depende del certificado.** No hay base central para empleadores | QR o enlace de la plataforma (si lo trae) + verificación de la firma del PDF (si la trae). **Incógnita clave:** no sé qué formato tienen hoy los certificados reales de las distintas plataformas |
| Contenido mínimo (art. 210) | **Sí** | Lectura con IA, igual que CEMEVA |
| Patrones (médico en serie, lunes, etc.) | **Sí**, dentro de la base de cada cliente | Reglas simples primero; la IA después |

### Construcción

- [ESTIMACIÓN] Lo técnico es parecido a CEMEVA (recibir documentos, leerlos, ordenarlos y perseguir al que falta). Un MVP con Claude Code: **2 a 4 semanas** del tiempo de Facu. Es una estimación por analogía, sin validar.
- [ESTIMACIÓN] Costo mensual de infraestructura: bajo (hosting chico, que Facu ya usa con Cloudflare). **No verifiqué precios actuales de la API de IA.** El mejor dato que tiene Facu es su propio costo por documento en CEMEVA.
- [ESTIMACIÓN] El costo grande **no es técnico, es legal**: un contrato de encargado de datos con cada cliente, la revisión de la transferencia internacional de datos y quizás la inscripción de la base. **No sé cuánto cobra un abogado de datos personales por esto: no lo verifiqué.**
- [OPINIÓN] Para validar **no hace falta construir nada**. El experimento de la sección 8 es "concierge": Facu hace los chequeos a mano con el responsable de RR.HH., sin guardar datos.

---

## 5. Regulación y riesgos

### Datos de salud (Ley 25.326). Pregunta 6 de Facu

- [DATO] La información sobre salud es **dato sensible** (art. 2).
- [DATO] Art. 7: "Ninguna persona puede ser obligada a proporcionar datos sensibles"; solo se tratan "cuando medien razones de interés general autorizadas por ley". Además, se prohíbe formar archivos que revelen datos sensibles, con algunas excepciones.
- [DATO] Art. 8: los que pueden tratar datos de salud de pacientes son los establecimientos y los profesionales de la salud, con secreto profesional.
- [DATO] Art. 25 (**lo que permite a un tercero como Facu**): quien trata datos "por cuenta de terceros" no puede usarlos para otro fin que el del contrato, ni pasárselos a nadie. Al terminar el servicio, tiene que destruirlos (o conservarlos hasta 2 años si se lo autorizan expresamente, en los casos previstos).
- [DATO] Art. 9 (seguridad) y art. 10 (confidencialidad): el que procesa también queda obligado al secreto.
- [DATO] Art. 12 (**transferencia internacional**): está prohibido mandar datos a países sin protección adecuada, salvo excepciones. La Disposición 60-E/2016 lista los países adecuados (UE, Suiza, Uruguay, Canadá sector privado, Israel, Nueva Zelanda, etc.). **Estados Unidos no está en la lista.** La misma disposición aprueba cláusulas modelo para contratos de prestación de servicios (Anexo II). No verifiqué si hubo cambios posteriores.
- [OPINIÓN, no es consejo legal] Consecuencias prácticas:
  - (a) El empleador tiene base legal para recibir el certificado con diagnóstico (el nuevo art. 210 lo exige). Facu, como encargado, puede procesarlo **solo por contrato y para ese fin**.
  - (b) Mandar certificados con diagnóstico a una API de IA alojada en EE.UU. es una **transferencia internacional de datos sensibles**. Hay que resolverlo antes de procesar un solo certificado real: con cláusulas, anonimizando el diagnóstico antes de mandarlo o con otro proveedor.
  - (c) El art. 21 obliga a inscribir ciertas bases privadas. Si aplica a este caso, lo tiene que decir un abogado.

### Riesgos laborales y de producto

- [DATO] La empresa conserva el control médico; la discrepancia se resuelve por junta médica oficial o por dictamen de un instituto con al menos 5 años en el Registro Federal de Establecimientos de Salud, pagado por el empleador (Decreto 407/2026; art. 210 LCT).
- [DATO] Según un análisis doctrinario citado por La Capital MdP (2026-07-03), la empresa no puede desconocer automáticamente una licencia válida ni descontar o sancionar sin analizar el caso.
- [DATO] Código Penal: art. 295, prisión de 1 mes a 1 año para "el médico que diere por escrito un certificado falso"; art. 296, el que usa un certificado falso es reprimido "como si fuere autor de la falsedad".
- [OPINIÓN] Riesgos concretos:
  1. **Falsos positivos:** si la herramienta marca como "dudoso" a un empleado realmente enfermo y la empresa lo sanciona, hay juicio laboral y daño reputacional. El producto tiene que ser un asistente, nunca un juez.
  2. **Acto médico:** opinar sobre si un diagnóstico es creíble es tarea de un médico. El software solo puede chequear forma, origen y patrones.
  3. **El Estado puede hacerlo gratis:** si el Ministerio de Salud abre un validador público (como intentó el CFM de Brasil o como hizo Santa Fe con su QR), el chequeo central se vuelve gratis. Lo que quedaría es el flujo de trabajo y los patrones.
  4. **Dependencia de SISA:** el acceso automático a REFEPS es discrecional.
  5. **Volatilidad regulatoria:** en Brasil, la base oficial quedó suspendida por la Justicia un año después de lanzarse.
  6. **Conflicto gremial:** una herramienta "para cazar truchos" puede generar rechazo sindical.

---

## 6. Respuestas a las dudas de Facu

**"¿Existe la base de datos que imagino?"**

- **De médicos: sí.** Es REFEPS, dentro de SISA. Es pública para consultar a mano (por DNI, matrícula o nombre) y dice si el profesional está matriculado y habilitado. Ojo: si un médico no aparece, puede ser que su provincia no lo informó, no necesariamente que sea falso. Lo dice la propia página oficial.
- **De certificados: no, al menos no para empleadores.** Lo que existe:
  - Repositorios de recetas con un código único (CUIR), con acceso para las autoridades sanitarias.
  - [OPINIÓN, inferencia mía] Como el decreto llama "prescripción" al certificado con reposo, es probable que esos certificados terminen en los mismos repositorios. O sea, el Estado tendría la base, pero no le da acceso a las empresas.
  - Plataformas que ponen su propio QR (Santa Fe).
  - En Brasil el colegio médico armó exactamente esa base (Atesta CFM) y la Justicia la suspendió.

**"¿Se puede comparar el certificado con el médico?"**

- **Sí, en parte.** Se puede chequear que el nombre y la matrícula del certificado coincidan con un profesional habilitado en REFEPS, con la profesión y la provincia correctas.
- **Lo que esa comparación no dice:**
  - (a) Si **ese** médico emitió **ese** certificado. Para eso hace falta el QR o la firma digital de la plataforma.
  - (b) Si el empleado estaba realmente enfermo. En Río Negro los médicos eran reales y estaban habilitados. Lo que los delató fue el **patrón**: 20 o 30 certificados por día, empleados de toda la provincia.
- [OPINIÓN] La idea de Facu sirve, pero el valor no está en "buscar en la base" (eso va a tender a ser gratis). Está en **juntar en un solo paso** forma + médico + plataforma + QR/firma + patrones + derivar al control médico. Es exactamente lo que vende Closecare en Brasil.

---

## 7. Filtro final

| Filtro | Puntaje | Por qué |
|---|---|---|
| **F1. Demanda comprobable en Argentina** | **3** | A favor: ausentismo alto (12,6% de los asalariados privados faltó al menos un día al mes, según IDESA), empresas que ya pagan por control ($12.000 a $24.000 por control en la AGN) y una norma nueva que obliga a revisar más. En contra: **no hay ninguna evidencia de que una empresa privada argentina pague por software de validación**, no hay cifras de fraude privado y los casos fuertes son del sector público |
| **F2. Producto automatizable y global** | **3** | Leer, chequear forma y buscar patrones es global (Closecare lo demuestra). Pero la verificación depende del registro de cada país (REFEPS, CRM, etc.), y en varios países el Estado ya lo resuelve por su cuenta (Alemania, Brasil, Santa Fe) |
| **F3. Validable rápido y barato** | **4** | 30 días y menos de USD 300 son realistas con entrevistas y un concierge sin guardar datos. Le resto 1 porque Facu no tiene, que yo sepa, una red de responsables de RR.HH., y porque no se pueden procesar certificados reales sin resolver antes lo legal |
| **F4. Riesgo legal manejable** (5 = bajo) | **2** | Datos sensibles de salud, transferencia internacional si se usa IA en EE.UU., riesgo de juicio laboral por falsos positivos y la línea con el acto médico. Es manejable, pero con abogado y diseño cuidadoso desde el día 1 |
| **F5. Encaje con Facu** | **4** | Le gusta (marca celeste, comentario del 2026-10-15) y es casi CEMEVA: leer documentos, cruzarlos y perseguir al que falta. Encaja con la ingeniería industrial (proceso y control). Le resto 1: no tiene ventaja de acceso a RR.HH. ni al mundo médico |
| **Total** | **16/25** | |

**Recomendación: PENDIENTE.**

[OPINIÓN] Por qué pendiente y no primera:

1. El riesgo legal es el más alto que vi en este tipo de ideas.
2. La demanda privada está sin probar.
3. La propia reforma achica el problema del papel falso.
4. El chequeo central (¿este médico existe?, ¿este certificado es auténtico?) tiende a volverse gratis por obra del Estado o de los colegios médicos.

Lo que podría hacerla subir a PRIMERA: que el experimento de 30 días muestre dolor concreto y gente dispuesta a pagar, o que una empresa de medicina laboral quiera usarla. Ese segundo camino, además, resuelve el problema del acto médico y parte del riesgo legal. Como validarla es barato, conviene correr el experimento aunque quede pendiente.

---

## 8. Primer experimento concreto

**Qué:** 12 entrevistas estilo The Mom Test a responsables de RR.HH. o de liquidación de sueldos, más 3 a empresas de medicina laboral. A los que muestren dolor, se les ofrece un **piloto concierge pago**: durante 2 semanas, Facu revisa con ellos, en videollamada y con la pantalla de RR.HH., cada certificado que llega (checklist art. 210 + REFEPS en SISA + plataforma en el listado ReNaPDiS + QR si lo trae). **Facu no recibe ni guarda los certificados**: así evita el problema de datos sensibles sin contrato.

**Con quién:**
- Empresas de 50 a 1.000 empleados con personal en turnos o locales: comercio, gastronomía, logística, industria, seguridad, limpieza.
- 3 empresas de medicina laboral (por ejemplo, las que se presentaron a la licitación de la AGN).
- 2 o 3 estudios contables o laborales que liquidan sueldos de PyMEs, porque ven muchos casos.

**Cómo llegar:**
- LinkedIn (cargos "Jefe/Responsable de RR.HH.", "Liquidación de sueldos").
- Contactos de la facultad y de CEMEVA.
- Cámaras empresarias locales.
- Asociaciones de RR.HH.: no verifiqué nombres ni condiciones; hay que chequearlo antes de contactar.

**Costo:** USD 0 a 150 (transporte, cafés, algún mes de una herramienta de contacto si hace falta). Una consulta legal corta sobre datos personales antes de cobrar el piloto: **costo no verificado**; buscar una opción gratuita o barata. Si supera el tope, el piloto se hace sin cobrar.

**Días:** 30. Del día 1 al 20, entrevistas. Del 21 al 30, pilotos concierge.

**Número para SEGUIR (las tres a la vez):**
1. Al menos **6 de 12** cuentan un episodio concreto en los últimos 6 meses (certificado dudoso, conflicto o juicio) y pueden decir cuánto les costó.
2. Al menos **3** aceptan el piloto pagando algo (aunque sea simbólico) o firman una carta de intención con precio.
3. Al menos **1** empresa de medicina laboral quiere probarlo con sus clientes.

**Número para CORTAR (cualquiera de estas):**
- **Menos de 3 de 12** con episodio concreto.
- **0** dispuestos a pagar.
- La mayoría dice "eso ya lo resuelve el médico laboral" o "con el certificado digital ya no hay problema".

**Pérdida máxima:** USD 150 en efectivo + 40 horas de Facu.

**5 preguntas estilo The Mom Test** (sobre hechos pasados, sin mencionar la idea):

1. "Contame la última vez que te llegó un certificado médico que te hizo dudar. ¿Qué pasó, qué hiciste y cuánto tiempo te llevó?"
2. "¿Cómo se revisa hoy un certificado desde que llega hasta que impacta en el sueldo? ¿Quién lo hace y cuántos llegan por mes?"
3. "Desde junio, con la reforma, ¿qué cambió en los certificados que reciben? ¿Siguen llegando en papel o en foto? ¿Qué hacen con esos?"
4. "¿Cuánto gastaron el último año en control de ausentismo (médico a domicilio, médico laboral)? ¿Cuántos controles pidieron el último mes?"
5. "¿Alguna vez sancionaron, despidieron o tuvieron un juicio por un certificado? ¿Cómo terminó y cuánto les costó?"

---

## 9. Fuentes (todas consultadas el 2026-10-15)

### Normas oficiales

- Decreto 407/2026, Boletín Oficial, 2026-06-01: https://www.boletinoficial.gob.ar/detalleAviso/primera/342620/20260601 (leí el Anexo I, IF-2026-53626853-APN-STEYSS#MCH, art. 6, descargado desde ese mismo aviso).
- Sumario del B.O. del 2026-06-01: https://www.boletinoficial.gob.ar/seccion/primera/20260601
- Res. MSAL 638/2026, B.O. 2026-06-05: https://www.boletinoficial.gob.ar/detalleAviso/primera/342821/20260605
- Res. MSAL 2214/2025 (B.O. 2025-07-21): https://e-legis-ar.msal.gov.ar/legisalud/migration/pdf/msres2214_2025.pdf
- Ley de Contrato de Trabajo, texto actualizado (arts. 208-211; art. 210 sustituido por la Ley 27.802, B.O. 2026-03-06): https://servicios.infoleg.gob.ar/infolegInternet/anexos/25000-29999/25552/texact.htm
- Ley 25.326 de Protección de Datos Personales: https://servicios.infoleg.gob.ar/infolegInternet/anexos/60000-64999/64790/texact.htm
- Disposición DNPDP 60-E/2016 (países adecuados): https://servicios.infoleg.gob.ar/infolegInternet/anexos/265000-269999/267922/norma.htm
- Código Penal, arts. 295 y 296: https://servicios.infoleg.gob.ar/infolegInternet/anexos/15000-19999/16546/texact.htm
- Res. MSAL 1648/2022 (REFEPS): https://www.argentina.gob.ar/normativa/nacional/norma-370489/texto
- Licitación Pública 12/2025 de la AGN, B.O. 2025-10-20: https://www.boletinoficial.gob.ar/detalleAviso/tercera/2402313/20251020
- Licitación 6/2024 de la AGN (**no abierta**, solo el resumen del buscador): https://www.boletinoficial.gob.ar/detalleAviso/tercera/2376370/20240708

### Sitios oficiales

- Receta electrónica, profesionales: https://www.argentina.gob.ar/receta-electronica/profesionales
- Instructivo de búsqueda de profesionales (junio de 2024): https://www.argentina.gob.ar/sites/default/files/2024/06/2024-06_instructivo_busqueda_profesionales_2182024.pdf
- Plataformas de receta electrónica: https://www.argentina.gob.ar/receta-electronica/plataformas
- Plataformas aprobadas: https://www.argentina.gob.ar/plataformas-aprobadas-por-el-ministerio-de-salud-de-la-nacion
- SISA, buscador público: https://sisa.msal.gov.ar/sisadoc/docs/050102/refeps_buscador_publico_profesionales.jsp
- SISA, WS020: https://sisa.msal.gov.ar/sisadoc/docs/050102/refeps_ws_020.jsp
- SISA, servicios web (acceso y cupos): https://sisa.msal.gov.ar/sisadoc/docs/0203/ws_intro.jsp y https://sisa.msal.gov.ar/sisadoc/docs/0203/ws_sisa.jsp
- Informe SIPA (octubre de 2026, datos de julio de 2026): https://www.argentina.gob.ar/sites/default/files/trabajoregistrado_2607_informe.pdf
- Gobierno de Río Negro, 2024-06-24: https://rionegro.gov.ar/articulo/49863/tania-lastra-encontramos-una-fabrica-de-certificados-medicos

### Prensa Argentina

- iProfesional, 2026-07-17: https://www.iprofesional.com/legales/460200-reforma-laboral-certificados-medicos-digitales-justificar-inasistencias-licencias-enfermedad
- iProfesional (la nota muestra 2026-06-22; el buscador mostraba 2026-07-16): https://www.iprofesional.com/management/457940-certificado-medico-digital-obligatorio-cambia-justificacion-faltas-laborales
- Contadores en Red (fechas del decreto): https://contadoresenred.com/reglamentacion-de-la-ley-de-modernizacion-laboral-27-802/amp/
- La Capital MdP, 2026-06-02: https://www.lacapitalmdp.com/reforma-laboral-cuando-el-empleador-podra-pedir-una-junta-medica-ante-licencias-por-enfermedad/
- La Capital MdP, 2026-07-03: https://www.lacapitalmdp.com/certificados-medicos-digitales-el-nuevo-foco-de-conflicto-entre-trabajadores-y-empleadores/
- Ámbito, 2026-10-05 (contenido de Arizmendi): https://www.ambito.com/que-cambia-el-dia-dia-del-control-medico-patronal-n6328149
- El Economista, 2026-02-19 (IDESA): https://eleconomista.com.ar/politica/reforma-laboral-alerta-ausentismo-126-n92728
- iProfesional, 2026-06-19 (Grupo Gestión): https://www.iprofesional.com/management/457801-licencias-medicas-en-argentina-el-ausentismo-laboral-subio-68-por-este-motivo
- iProfesional, 2017-05-18 (Mercer): https://www.iprofesional.com/management/249556-ausentismo-mas-de-la-mitad-de-las-empresas-ya-aplica-politicas-activas-para-reducir-los-faltazos
- Ámbito, 2019-09-07 (Adecco): https://www.ambito.com/como-combatir-el-ausentismo-laboral-n5053122
- La Nación, 2024-06-25: https://www.lanacion.com.ar/politica/descubren-una-fabrica-de-certificados-truchos-para-no-ir-a-trabajar-nid24062024/
- Noticias NQN, 2024-06-22: https://www.noticiasnqn.com.ar/noticias/2024/06/22/298926-una-medica-otorgo-2000-dias-de-licencias-en-rio-negro
- El Litoral (Santa Fe, sin fecha visible): https://www.ellitoral.com/salud/adios-papel-santa-fe-lanza-certificado-medico-digital-terminar-falsificaciones-agilizar-tramites_0_ZcNcA4Pv9f.html

### Afuera

- Closecare: https://www.closecare.com.br/
- Jornal Contábil, 2022-04-28 (Closecare, 13%): https://jornalcontabil.com.br/noticia/veja-dicas-para-evitar-a-validacao-indevida-de-atestados-pelo-setor-de-rh/
- Pipefy: https://www.pipefy.com/ai-agents/certificate-validation-agent/
- Correio 24 Horas, 2024-11-05 (Atesta CFM, Cremeb): https://www.correio24horas.com.br/minha-bahia/empresas-poderao-descobrir-se-atestado-medico-de-funcionario-e-falso-entenda-1124
- Aos Fatos, 2025-12-11: https://www.aosfatos.org/noticias/atestado-medico-papel-valido-2026/
- Tribuna Online (suspensión del Atesta CFM, sin fecha en la extracción): https://tribunaonline.com.br/economia/veto-a-sistema-antifraude-em-atestado-revolta-empresarios-207861
- Baguete, 2023-12-07 (INSS): https://www.baguete.com.br/noticias/inss-adota-ia-para-identificar-fraudes-em-atestados
- MedHelp Care: https://www.medhelp.se/en/about-medhelp/ y https://www.medhelp.se/en/absence-management/ (la segunda, solo vista en el resumen del buscador)
- Softworks: https://www.softworks.com/absence-management/
- AOK (eAU, Alemania): https://www.aok.de/fk/sozialversicherung/entgeltfortzahlung-und-ausgleichsverfahren/eau-die-elektronische-au-bescheinigung/
- der-betrieb.de (eAU sin datos del médico; **solo el resumen del buscador**): https://der-betrieb.de/meldungen/die-elektronische-arbeitsunfaehigkeitsbescheinigung/

### Lo que no pude verificar

- Las resoluciones del Ministerio de Salud que el Decreto 407/2026 ordenó dictar en 30 y en 60 días.
- Si una empresa privada puede obtener el WS020 de REFEPS.
- Qué porcentaje de los certificados electrónicos reales trae QR o una firma digital verificable.
- Cifras de certificados falsos en el sector privado argentino.
- Precios de abonos privados de control de ausentismo.
- El tipo de cambio para pasar los precios a dólares.
- El costo actual de la API de IA por documento.
- El costo de un abogado de datos personales.
- Los casos de Chubut y Provincia de Buenos Aires (solo vistos en el resumen del buscador).
