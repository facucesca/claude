# F17 — IA para estudios contables argentinos: indagación a fondo

- **Fecha:** 2026-10-15. Todas las páginas se consultaron ese día.
- **Pedido de Facu (2026-10-15):** ver qué problema repetitivo tiene el contador en el día a día, y averiguar qué leyes o tareas son claramente repetitivas.
- **Método:** 15 búsquedas web (el tope) y unas 45 lecturas directas de páginas. Para normas, siempre que pude, fuente oficial (argentina.gob.ar, arca.gob.ar / afip.gob.ar, boletinoficial.gob.ar, ca.gob.ar).
- **Cómo leer este documento:** **DATO** = verificado, con fuente. **ESTIMACIÓN** = cálculo mío, con el razonamiento. **OPINIÓN** = juicio mío. "Según la propia empresa" = lo que la empresa dice de sí misma, sin verificar.

### Siglas usadas (una vez)

ARCA = Agencia de Recaudación y Control Aduanero (ex AFIP). DDJJ = declaración jurada. PH = persona humana (persona física). BP = Bienes Personales. IIBB = Ingresos Brutos. CM = Convenio Multilateral (IIBB cuando se vende en varias provincias). SIFERE = sistema de la Comisión Arbitral para liquidar IIBB de CM. SIRCREB = retenciones de IIBB sobre lo que entra a las cuentas bancarias. DFE = Domicilio Fiscal Electrónico (el buzón oficial de ARCA). DJS = Declaración Jurada Simplificada de Ganancias (formulario F.2711). RG = Resolución General. F.931 = DDJJ mensual de cargas sociales del empleador. SIRADIG / F.572 = sistema donde el empleado informa sus deducciones de Ganancias. SICORE / SIRE = sistemas de los agentes de retención y percepción. REIBP = Régimen Especial de Ingreso de Bienes Personales. CPCECABA = Consejo Profesional de Ciencias Económicas de CABA. FACPCE = federación que agrupa a los consejos. MVP = primera versión mínima del producto.

### Resumen en 6 líneas

1. Por ley, un estudio repite cada mes IVA y Libro de IVA Digital, IIBB, cargas sociales, monotributo y la revisión del buzón de ARCA, por cada cliente. Una vez al año, Ganancias y Bienes Personales de cada persona.
2. **El dolor mejor documentado de 2026 es la temporada anual de Ganancias y Bienes Personales de personas humanas.** Hubo 4 prórrogas (3 verificadas en fuente oficial o de un consejo; la cuarta solo la vi en el buscador), pedidos de los consejos profesionales y notas sobre burnout de contadores.
3. Las tareas mensuales ya están bastante cubiertas por software argentino (SOS-Contador, Witmi, CONTA, Holistor, Genio Contable con IA, ConciliaBot con IA).
4. **Producto elegido (opinión):** armador de la DDJJ anual de personas humanas para estudios. Hace el pedido de papeles, lee los documentos con IA, valúa los bienes, compara contra lo que precargó ARCA y entrega el papel de trabajo.
5. **Riesgo grande:** ARCA ya precarga buena parte de Ganancias, y desde la Ley 27.826 (octubre 2026) cualquier persona humana puede usar la DJS. Además el negocio es estacional.
6. **Filtro: 17/25 → PENDIENTE.** Igual conviene hacer ya las entrevistas, en noviembre de 2026, porque la temporada termina el 2026-10-30 y el dolor está fresco.

---

## 1. Qué es exactamente (el producto elegido, especificado)

### Los 3 productos que evalué

Los tres están dentro del tema F17 y apuntan a un estudio contable que paga una suscripción.

| | P1. Vigía de notificaciones fiscales | **P2. Temporada de personas humanas (elegido)** | P3. Cartera de monotributistas en piloto automático |
|---|---|---|---|
| Tarea que resuelve | Revisar cada semana el DFE de ARCA y de las provincias de cada cliente. La IA dice qué es cada aviso, qué plazo tiene y qué hacer. | Armar cada año la DDJJ de Ganancias y Bienes Personales de cada persona humana: pedir papeles, leerlos, valuar y comparar contra ARCA. | Controlar cada mes los topes del monotributo. Hacer la recategorización de toda la cartera en febrero y agosto. Avisar al cliente. |
| Base legal | RG 4280/2018 (DFE) | Ley 27.799, Ley 27.826, RG 5820, RG 5836/2026 y prórrogas | Régimen simplificado, según el micrositio de ARCA |
| Frecuencia | Semanal | Anual, con pico | Mensual y semestral |
| Competencia local verificada | **Alta para ARCA:** Witmi, SOS-Contador, Plan In, Aconpy. Las provincias: no lo pude verificar. | **Parcial:** ARCA precarga, el módulo de Onvio calcula, ConciliaBot convierte resúmenes. No encontré a nadie que haga todo el circuito. | **Alta:** SOS-Contador, AppContador, Witmi, EC Sistemas, CONTA |
| Cuánto aporta la IA | Media: leer y clasificar avisos | **Alta:** documentos de decenas de bancos y brokers, todos en formatos distintos | Baja: es aritmética y alertas |
| Riesgo de que ARCA lo absorba | Bajo | **Alto** para Ganancias, medio para Bienes Personales | Alto |
| Encaje con Facu | Alto: bots y alertas | **Muy alto:** pedir y ordenar documentos, como en CEMEVA | Medio |
| Cruce con el registro (Regla N.º 2) | Parecida a SER-1-4 y SER-2-1 | Parecida a B18 y SER-1-1 (por la parte de pedir papeles) | Parecida a I14 |

**Por qué elijo P2 (opinión).** Es donde el dolor está mejor probado con datos de 2026 (sección 3). Es donde la IA rinde más, porque hay que leer documentos desordenados. Encaja casi exacto con lo que Facu ya hizo en CEMEVA. Y no encontré en Argentina una herramienta que haga todo el circuito.

P1 queda segunda. Es más estable porque es mensual, pero la parte de ARCA ya está resuelta por al menos 4 productos locales. Su hueco depende de las provincias, que no pude verificar. P3 queda descartada como producto suelto: el mercado está lleno y la IA aporta poco.

### P2 especificado

**Nombre de trabajo:** "Temporada PH". Es un armador de las declaraciones anuales de personas humanas (Ganancias y Bienes Personales) para estudios contables.

**El problema**

- **DATO:** cada año, por cada cliente persona humana, el estudio presenta Ganancias y/o Bienes Personales. Para el período fiscal 2025, el vencimiento de presentación de Ganancias se movió varias veces (3 cambios verificados, un cuarto solo visto en el buscador) y terminó el 2026-10-30. Bienes Personales venció el 2026-07-27 (detalle y fuentes en la sección 3).
- **DATO (iProfesional, 2026-08-18):** mayo, junio y julio son los meses más pesados del año para los contadores.
- **ESTIMACIÓN (sin fuente, a validar en las entrevistas):** en cada cliente hay que:
  - pedirle los papeles (certificados de saldos al 31/12, resúmenes de brokers, el certificado anual de sueldo F.1357, alquileres, compras y ventas de bienes, deudas);
  - perseguirlo hasta que los mande;
  - pasar todo a una planilla;
  - valuar cada bien con las reglas y tablas de ARCA;
  - comparar contra lo que ARCA ya precargó;
  - ajustar y cargar.

**Quién paga:** el socio del estudio contable. El cliente final le paga el honorario al estudio y no ve la herramienta.

**Qué hace (primera versión)**

1. **Lista de pedido por cliente.** Se arma a partir de la DDJJ del año anterior: "el año pasado tenías cuenta en el banco X y en el broker Y; mandá el certificado al 31/12".
2. **Pedido y seguimiento automático** por WhatsApp o mail hasta que el cliente completa. Es el patrón de la app de CEMEVA que persigue a terceros por documentos.
3. **Lectura con IA de cada documento.** Extrae saldo, moneda, tenencia, fecha y titular.
4. **Valuación.** Aplica las tablas de valuación que publica ARCA cada año y la cotización al 31/12. **DATO:** al momento de una nota de Blog del Contador, ARCA todavía no había publicado las valuaciones del período fiscal 2025. Eso muestra que el producto depende de esa publicación.
5. **Control cruzado** contra lo que ARCA precarga. **DATO (manual oficial de la DJS, versión 2.09/26, septiembre 2026):** ARCA muestra ingresos y egresos facturados, que se pueden bajar en un archivo CSV, más retenciones (Mis Retenciones) y deducciones del SIRADIG. La herramienta marca diferencias.
6. **Entrega:**
   - un Excel con el papel de trabajo;
   - un resumen en lenguaje simple para el cliente;
   - la lista de lo que falta.

**Qué NO hace:** no presenta nada ante ARCA, no usa la clave fiscal del cliente en la primera versión y no asesora. El contador revisa, carga y firma.

**Cómo se cobra (estimación y opinión)**

- Por declaración procesada, con un mínimo por temporada y pago anticipado en marzo y abril.
- **Referencia de afuera, según un blog de Filed, que es un proveedor:**
  - Juno cobra unos USD 45 por declaración, que bajan a algo más de USD 30 con volumen (mínimo 100 declaraciones);
  - Soraban cobra USD 25 a 40 por declaración (mínimo 50).
- **No sé cuánto cobra un estudio argentino por cada DDJJ de persona humana.** No lo pude verificar: los honorarios sugeridos de los consejos no estaban detallados en lo que encontré. Es una pregunta obligatoria del experimento.
- **Opinión:** el precio tiene que ser una fracción chica de ese honorario. Como techo de referencia, hoy los estudios pagan por mes entre $15.000 y $206.000 por herramientas parecidas (sección 2).

**Por dónde empezar (opinión):** estudios chicos y medianos que hacen entre 30 y 300 DDJJ de personas humanas por año. Primer contacto: el estudio que atiende a CEMEVA. **No sé** si tiene clientes productores agropecuarios. Si los tiene, es un sub-nicho con bienes difíciles de valuar (hacienda, granos, maquinaria) que conviene explorar. Es una hipótesis, no un dato.

---

## 2. Mercado en Argentina

### Cuántos contadores hay

**No encontré una cifra nacional oficial y actual de matriculados.** Lo que sí encontré:

| Dato | Fuente | Confianza |
|---|---|---|
| La FACPCE agrupa **25 consejos profesionales** en 24 jurisdicciones (Santa Fe tiene 2). | facpce.org.ar. Conté los enlaces de la sección "miembros" el 2026-10-15; la página no da el número. | Alta |
| El CPCECABA "reúne sesenta mil matriculados" y da "aproximadamente 3.000 matrículas" por año. El "55% de los profesionales del país son de la Ciudad", y de ellos el 90% son contadores. | Revista Mercado, nota de **abril de 2008** (la fecha sale de la ruta de la imagen y del texto). | Baja: tiene 18 años |
| El consejo de la Provincia de Buenos Aires tiene "más de 20.000 profesionales" (nota de junio de 2024). | Resumen del buscador; no la abrí. | Media |
| "Aproximadamente 140.000 contadores públicos matriculados" en el país. | Un sitio de noticias de Misiones, sin fecha ni método (resumen del buscador). | Baja: no verificado |

**ESTIMACIÓN (confianza baja).**

- Si en 2008 CABA tenía 60.000 matriculados y eso era el 55% del país, el total era de unos 109.000.
- Con unas 3.000 matrículas nuevas por año solo en CABA, el total de hoy puede rondar los 120.000 a 160.000 profesionales de ciencias económicas. No resto bajas ni jubilaciones, así que puede estar sobreestimado.
- **Cuántos tienen estudio propio con cartera de clientes: no lo sé.** Si fuera entre el 20% y el 40% (supuesto sin fuente), serían entre 25.000 y 60.000 estudios o contadores independientes.
- Para tener un dato firme, hay que pedirle el padrón a la FACPCE o a cada consejo.

**Piso de mercado que paga software (según la propia empresa):** ConciliaBot dice que la usan "más de 1000 estudios contables".

### Cuántas personas presentan Ganancias o Bienes Personales

**No lo pude verificar.** Busqué en estadísticas de ARCA y en prensa y no encontré la cantidad de DDJJ presentadas. Algunos datos que achican el universo:

- **DATO (argentina.gob.ar, noticia de 2026-05-22):** las DDJJ informativas de las RG 2442 y 4003 vencieron el 2026-07-31.
- **Sin verificar en fuente oficial (según el buscador):**
  - la RG 5683/2025 subió a $150.000.000 el umbral de la DDJJ informativa de patrimonio para empleados y jubilados;
  - quienes entraron al REIBP quedan exentos de esa obligación hasta 2027.
- **Opinión:** el REIBP y la DJS achican el número de declaraciones complejas en el corto plazo.

### Cuánto se paga hoy por software para estudios (precios publicados, 2026-10-15)

| Producto | Precio publicado | Qué incluye |
|---|---|---|
| SOS-Contador | Plan gratis; Premium $54.780/mes con IVA, para 10 CUIT | Página sin fecha de vigencia |
| Witmi | $131.500/mes (plan estudio o plan operativo); $195.500/mes (completo) | Con IVA, ajuste trimestral, actualizado 10/2026 |
| CONTA | De $49.000/mes (5 responsables inscriptos + 10 monotributistas) a $206.000/mes (20 + 40, con contabilidad) | — |
| ConciliaBot (Contatech) | $45.000/mes; $65.000/mes la versión Plus + Flow | Más IVA |
| Contador-IA (IAra Labs) | $15.000/mes (50 interacciones); $40.000/mes (200 interacciones) | — |
| EC Sistemas | Versión Full del módulo monotributo: USD 120 cada 6 meses | Según el buscador |

**OPINIÓN:** el contador ya paga entre decenas y cientos de miles de pesos por mes en software. Hay costumbre de pagar. Pero el presupuesto se lo lleva la suite principal, y una herramienta nueva tiene que justificar un gasto extra.

---

## 3. Tabla de tareas repetitivas por ley

**Columna "Cuánto duele":** "Alto (evidencia)" quiere decir que hay fuente pública. Si no la hay, va como estimación.

| # | Tarea | Norma (fuente) | Frecuencia | Cuánto duele | ¿Ya automatizada? ¿Por quién? |
|---|---|---|---|---|---|
| 1 | **DDJJ de IVA** de cada cliente responsable inscripto | RG 5705/2025 de ARCA, publicada el 2025-06-02: determinación e ingreso del IVA (listado en argentina.gob.ar). Octubre 2026: vence del 19 al 23/10 según la terminación de CUIT (portada de ARCA citada por el buscador; no la abrí). | Mensual | **Medio (estimación).** Es por volumen: cada cliente, cada mes. Nodecraft, un proveedor, calcula 3 a 6 h/mes solo en bajar comprobantes por PyME. Es su estimación, sin método publicado. | **Sí.** SOS-Contador, Witmi, CONTA, Holistor, Genio Contable (con IA). |
| 2 | **Libro de IVA Digital** | RG 4597/2019 (Boletín Oficial 2019-10-01), modificada por RG 4671/2020, 4796/2020, 4925/2021, 5133/2021, 5707/2025 y 5762/2025. Art. 12: registración mensual, aun "SIN MOVIMIENTO". Art. 7: ARCA pone a disposición los comprobantes de su base. | Mensual | **Medio (estimación).** Según El Economista (2026-05-09), las entidades piden que los datos de ARCA sean consistentes con el Libro IVA. | **Sí.** SOS-Contador lo genera; CONTA y Witmi importan; Genio Contable. |
| 3 | **Monotributo:** pago mensual, control de topes y **recategorización semestral** | Micrositio de ARCA: "Todos los años, en febrero y agosto, se debe hacer la recategorización semestral". Categorías vigentes desde el 2026-08-01: la A tope $12.009.410,45; la K tope $126.610.838,75. Fuentes secundarias viejas dicen "enero y julio": la oficial dice febrero y agosto. | Mensual y semestral | **Alto en los picos (evidencia parcial).** iProfesional (2026-08-18) cuenta de equipos que trabajan pasada la medianoche "categorizando" contribuyentes. Que se refiera a la recategorización es interpretación mía. | **Sí.** SOS-Contador (simulación, topes, alertas de exclusión), AppContador, Witmi (novedades del padrón de toda la cartera), EC Sistemas, CONTA. |
| 4 | **IIBB Convenio Multilateral:** DDJJ mensual y anual (CM05) en SIFERE | Comisión Arbitral: RG CA 16/2016 (SIFERE obligatorio desde 11/2016); vencimientos 2026 en RG CA 20/2025 (ca.gob.ar/sistemas/sifere). | Mensual y anual | **Medio-alto (estimación):** hay que cargar retenciones, percepciones y coeficientes de cada provincia. No encontré cifras. | **Sí.** Genio Contable genera el archivo para SIFERE con IA (según la empresa); SOS-Contador (SIFERE Web); Witmi; CONTA (CM05). |
| 5 | **SIRCREB:** retenciones de IIBB en cuentas bancarias; controlar alícuota y computarlas | RG CA 104/2004 y siguientes; la consulta del contribuyente pasó a SIFERE Web (RG CA 8/2015) (ca.gob.ar/sistemas/sircreb). | Mensual | **Medio (estimación).** | Parcial: Genio Contable (regímenes de retención y percepción); ConciliaBot (cruza retenciones con los datos de ARCA). |
| 6 | **IIBB locales** (ARBA, AGIP y demás provincias) | **No lo pude verificar** por provincia: las páginas de ARBA y AGIP no devolvieron contenido. | Mensual | No verificado | Genio Contable dice bajar datos de AGIP y ARBA. |
| 7 | **Agente de retención o percepción nacional** (SICORE / SIRE) | RG 2233/2007 (SICORE); RG 3726/2015 (SIRE), modificada por RG 4523/2019 y RG 4798/2020 (afip.gob.ar/sire, normativa). | Periódica (no la verifiqué) | **Medio (evidencia).** iProfesional (2026-08-18): los mínimos de retención de Ganancias llevan unos 15 años sin actualizarse y obligan a emitir certificados por montos muy chicos. | Lo incluyen las suites (no verifiqué el detalle). |
| 8 | **Sueldos:** F.931 (Declaración en Línea) y **Libro de Sueldos Digital** | RG 4265/2018 (Declaración en Línea); RG 3960/2016 (SUSS); RG 5250/2022 (Libro de Sueldos Digital, reemplazó a la RG 3781). Fuente: páginas de normativa de ARCA. | Mensual (la página no lo dice; no verificado) | **Medio (estimación).** El cuello está en juntar las novedades del cliente (ya investigado: SER-4-1). | **Sí.** Witmi (formato SICOSS + Libro Sueldos Digital), CONTA (F.931, más de 45 convenios), SOS-Contador, Calim (tercerización para estudios). |
| 9 | **SIRADIG (F.572) y retención de Ganancias a empleados**; liquidación anual (F.1357) | RG 4003/2017, modificada por RG 5547/2024; RG 4396/2019 (certificado de liquidación de 4ª categoría). Fuente: afip.gob.ar/572web, normativa. | Continua y anual | **Medio (estimación).** | Módulos de sueldos. La DJS de ARCA trae sola las deducciones del SIRADIG (manual de la DJS). |
| 10 | **Ganancias de personas humanas** (régimen general o DJS F.2711) | Ley 27.799 (Inocencia Fiscal), Decreto 93/2026, RG 5820, RG 5836/2026. Vencimientos del período fiscal 2025: RG 5851 (2026-07-27); RG 5876 (presentación 2026-08-27, pago 2026-07-27); RG 5890 (2026-09-22, según el buscador, no la abrí); **RG 5911/2026 (2026-10-30)**. Esta última se confirmó en el micrositio de ARCA y en el CPCECABA, que dice que responde a la Ley 27.826. | Anual, con pico de mayo a octubre de 2026 | **ALTO (evidencia).** (a) 4 prórrogas (la de la RG 5890 no la pude abrir). (b) Según argentina.gob.ar (2026-05-22), la primera fue a pedido de "entidades profesionales de ciencias económicas". (c) Según El Economista (2026-05-09), el CPCECABA y la FAGCE (una entidad de graduados en ciencias económicas) pidieron ajustes de sistema y postergar vencimientos; las entidades también señalaron inconsistencias en el sistema nuevo de Ganancias Simplificada. (d) Según iProfesional (2026-08-18), hay burnout; mayo a julio son los meses más pesados y las caídas de la web de ARCA llegan en los picos. | **Parcial.** ARCA precarga facturación, retenciones y SIRADIG en la DJS. El módulo de Onvio (Thomson Reuters) calcula y arma papeles de trabajo; su página no menciona lectura de documentos ni IA. Holistor no muestra el detalle. **Genio Contable dice que no cubre Ganancias ni Bienes Personales.** |
| 11 | **Bienes Personales de personas humanas** | Micrositio de ARCA de Ganancias y Bienes Personales; período fiscal 2025 vencido el 2026-07-27 (RG 5876 lo dejó sin cambios). La ley del impuesto no la abrí en esta sesión. | Anual (mismo pico) | **ALTO (evidencia de pico; es el mismo período del punto 10).** Hay que valuar cada bien con las tablas anuales de ARCA. | **Parcial.** ConciliaBot convierte a Excel resúmenes de "más de 80 bancos y más de 60 sociedades de inversión" (según la empresa). Onvio calcula. ARCA muestra datos de "ingresos, activos, consumos, retenciones y percepciones" (Blog del Contador). |
| 12 | **DDJJ informativas** (RG 2442 y RG 4003) | argentina.gob.ar, noticia de 2026-05-22: vencieron el 2026-07-31. | Anual | No verificado | No verificado |
| 13 | **Revisar el Domicilio Fiscal Electrónico** de cada cliente | RG 4280/2018 (vigente desde 2018-08-01). Art. 1: el DFE es obligatorio. **Art. 7: la notificación se da por hecha el día en que se abre o a las 0 horas del lunes siguiente a que quedó disponible, lo que pase primero.** Art. 6: los terceros autorizados pueden consultar por servicio web. | Semanal en la práctica (estimación, por el art. 7) | **Alto cuando se escapa algo (evidencia parcial).** iProfesional (2026-08-18): levantar un embargo lleva 7 a 8 días de trámite y las multas se describen como desproporcionadas. | **Sí, para ARCA.** Witmi (DFE de todos los clientes en un paso), SOS-Contador (importa e-Ventanilla y tiene un "Asistente Antimulta" por WhatsApp), Plan In y Aconpy (ya relevados el 2026-10-13). Las provincias: no lo pude verificar. |
| 14 | **Calendario general de vencimientos** | RG 4172 y modificatorias fijan cada año las fechas (citada en la RG 5847/2026, Boletín Oficial 2026-05-15). | Continua | Medio (estimación) | **Sí, y mucho** (ya investigado: SER-1-4). Aconpy, Witmi, CONTA; Genio Contable da el calendario gratis. |
| 15 | **Anticipos de Ganancias y Bienes Personales** de personas humanas | 2º anticipo del período 2026: del 13 al 15/10/2026 (portada de ARCA citada por el buscador; no la abrí). 1º anticipo movido a septiembre por las RG 5876 y 5890. | Periódica | Bajo-medio (estimación) | Lo calculan las suites. |

### Qué duele más, según la evidencia (no según supuestos)

1. **La temporada anual de personas humanas (filas 10 y 11).** Es la única tarea con evidencia oficial de dolor: prórrogas pedidas por las entidades profesionales. Además, en 2026 cambió la ley en plena temporada (Ley 27.826).
2. **La inestabilidad de los sistemas de ARCA y los cambios normativos constantes** (iProfesional y El Economista). **OPINIÓN:** ningún producto arregla las caídas de ARCA. Los cambios normativos sí son una fuente de trabajo repetitivo, pero ya hay consultores con IA (Errepar Consultor IA, lanzado según una nota de 2026-08-21; Contador-IA).
3. **Multas y embargos por algo que no se vio a tiempo** (fila 13).
4. **Los picos de la recategorización del monotributo** (fila 3).

**Lo que no encontré:** una encuesta a contadores argentinos que ordene las tareas por horas. La única tabla de horas es de un proveedor (Nodecraft), sin método publicado.

---

## 4. Qué existe en Argentina y afuera (verificado)

### Argentina

| Herramienta | URL | Qué hace (según su sitio, 2026-10-15) | IA | Precio |
|---|---|---|---|---|
| SOS-Contador | sos-contador.com | IVA, Libro IVA Digital, SIFERE Web, monotributo (simulación y topes), sueldos. "Autoimpo" baja de ARCA la e-Ventanilla, comprobantes, padrón y otros. "Asistente Antimulta" por WhatsApp. "15 años" y "miles de usuarios" (según la empresa). | BOT de ayuda | Gratis / $54.780 por mes (10 CUIT) |
| Witmi | witmi.ar | Legajos con padrón de ARCA, novedades de toda la cartera, DFE de todos los clientes "tras una autorización inicial con la clave fiscal de cada uno", IVA, IIBB, CM, sueldos, honorarios. | No menciona | $131.500 a $195.500 por mes |
| CONTA | conta.com.ar | Importa Mis Comprobantes, IVA, IIBB, Ganancias, CM05, sueldos (F.931), balances, panel mensual por cliente. | No menciona | $49.000 a $206.000 por mes |
| AppContador | appcontador.com.ar | Conexión con ARCA "de solo lectura" (según la empresa), con clave fiscal o delegación; panel de cartera para contadores. | No menciona | No publica |
| Aconpy | aconpy.com | Bots, login ARCA, alertas fiscales, monotributo, vencimientos, Libro IVA, sueldos, "IA". | Sí (sin detalle) | No publica |
| **Genio Contable** | geniocontable.com | Importa del ERP o de planillas, baja datos de ARCA, AGIP y ARBA, concilia contra el fisco y genera los archivos para los aplicativos. Cubre IVA, IIBB, SIFERE, tasa de Seguridad e Higiene y regímenes de retención. **No cubre Ganancias ni Bienes Personales.** Dice reducir "hasta 83%" el trabajo operativo (iProfesional, 2026-05-16, cifra de la empresa). Usa modelos de OpenAI y Anthropic. | **Sí** | No publica; primeras liquidaciones gratis |
| **ConciliaBot (Contatech)** | contatech.org/conciliabot | Por Telegram o web: pasa extractos, resúmenes, DDJJ, facturas y tickets a Excel; concilia contra los datos de ARCA; balances según la norma técnica RT 54; IVA, IIBB y Ganancias; VEP masivos (volantes de pago de ARCA); vencimientos por WhatsApp. Dice tener "más de 1000 estudios" y soportar más de 80 bancos y más de 60 sociedades de inversión. | **Sí** | $45.000 o $65.000 por mes, más IVA |
| Contador-IA (IAra Labs) | contador-ia.com | Chat con IA para contadores: declaraciones, conciliaciones, lectura de documentos. Sus cifras de ahorro no cierran entre sí (lo marqué). | **Sí** | $15.000 a $40.000 por mes |
| Onvio (Thomson Reuters), módulo Ganancias y Bienes Personales | thomsonreuters.com.ar (nota de 2026-04-06) | Liquida Ganancias y Bienes Personales, actualiza escalas y cotizaciones, genera papeles de trabajo. No menciona lectura de documentos ni IA. | No | No publica |
| Errepar Consultor IA | documento.errepar.com (nota de 2026-08-21) | Responde consultas profesionales con IA. No automatiza liquidaciones. | **Sí** | No publica |
| Holistor | holistor.com.ar | Software para estudios: laboral, contable e impositivo. Dice tener 36 años, más de 90.000 licencias y certificación ISO 9001. | No menciona | No publica |
| Calim | calim.com.ar | Estudio contable online: liquidaciones y sueldos; también terceriza sueldos para estudios. "Más de 10.000 trámites y clientes" (según la empresa). | No menciona | Cotiza por WhatsApp |
| Afip SDK (infraestructura) | afipsdk.com | API comercial sobre los servicios web de ARCA, más automatizaciones (descargar Mis Comprobantes, monotributo, retenciones, deudas). No tiene relación con el organismo. | — | No publica |
| EC Sistemas, KM44 | estudiocodina.com.ar, km44.com.ar | Software para estudios (resumen del buscador; no los abrí). | — | Según el buscador: USD 120 cada 6 meses / "desde $46.000" |

Relevados el 2026-10-13 y no revisados de nuevo: Xubio, Colppy, Contabilium, Tango, Plan In.

### Afuera (lo mejor del rubro, 2026)

| Empresa | Qué hace | Señal |
|---|---|---|
| **Juno** | Extrae datos de más de 92 tipos de documento, prepara la declaración y la revisa marcando cambios contra el año anterior, siempre con una persona que decide. Dice bajar 50% el tiempo por declaración (según la empresa). | USD 12 millones de ronda semilla liderada por Bonfire Ventures (CPA Practice Advisor, 2026-04-13). Unos USD 45 por declaración (blog de Filed). |
| **Basis** | Agentes de IA que hacen de punta a punta trabajo de asesoría, impuestos y auditoría para estudios. Dice usarla "aproximadamente el 30%" de las 25 firmas más grandes. | USD 100 millones Serie B con valuación de USD 1.150 millones, liderada por Accel (CPA Practice Advisor, 2026-02-24). |
| **Black Ore (Tax Autopilot)** | Del documento del cliente a la declaración lista para firmar. Disponible para todos desde abril de 2026. | Según el blog de Filed (proveedor) y el buscador. |
| **Accrual** | Agentes que actúan como preparador de declaraciones. | USD 75 millones, General Catalyst (según el buscador, febrero de 2026; no abrí la nota). |
| **Filed, Soraban, SurePrep** | Revisión, captura de documentos, envío y firma. | Soraban cobra USD 25 a 40 por declaración (blog de Filed). |

Relevados el 2026-10-13: Content Snare, Financial Cents, Dext, AutoEntry, Booke AI, Double, Karbon, Canopy, DataSnipper, Fieldguide.

**OPINIÓN.** Afuera, "IA que arma la declaración anual de la persona a partir de sus documentos" es una de las categorías con más inversión de 2026. Eso confirma que el problema es real y se paga en EE.UU. No prueba nada sobre Argentina, donde los honorarios y los precios son mucho más bajos. Además, ARCA precarga más datos que el fisco de EE.UU.: no lo comparé, es opinión.

### Datos nuevos sobre ideas ya investigadas (Regla N.º 2: se anotan, no son filas nuevas)

- **B18 / SER-1-1 (pedir comprobantes al cliente):** SOS-Contador manda comprobantes por WhatsApp y ConciliaBot manda vencimientos por WhatsApp. No encontré todavía un portal argentino de pedido de documentos con recordatorios automáticos.
- **SER-1-2 (carga de facturas):** ConciliaBot y Contador-IA leen facturas y tickets con IA. CONTA, Witmi y SOS-Contador importan Mis Comprobantes.
- **SER-1-3 (conciliación bancaria):** ConciliaBot hace "conciliaciones automáticas" contra mayores, retenciones y comprobantes de ARCA ($45.000 por mes más IVA; "más de 1000 estudios" según la empresa). Esto **achica el hueco** que se había visto el 2026-10-13.
- **SER-1-4 (vencimientos):** se suman Genio Contable (calendario gratis), CONTA y Witmi.

---

## 5. Cómo se construiría y cuánto costaría (estimación)

### Fases

| Fase | Qué | Cuándo (propuesta) | Costo en plata (estimación) | Horas de Facu (estimación) |
|---|---|---|---|---|
| 0. Experimento | Entrevistas y una prueba "conserje", hecha a mano con Claude y una plantilla de Excel (sección 8) | 2026-10-20 a 2026-11-20 | USD 0 a 100 | 40 h |
| 1. Primera versión | Portal o WhatsApp para recibir documentos, clasificador de documentos, extractor con IA, motor de valuación con las tablas de ARCA, comparación contra el CSV de ARCA, salida en Excel, seguimiento automático de lo que falta | 2026-12 a 2027-03, solo si el experimento da "seguir" | USD 30 a 150 por mes (hosting, IA, dominio, proveedor de WhatsApp; los precios de cada servicio no los verifiqué) | 10 a 15 h por semana × 16 semanas ≈ 160 a 240 h |
| 2. Temporada 2027 | Venta anticipada en marzo y abril; uso de mayo a julio (si no hay prórrogas) | 2027-03 a 2027-07 | Costo de IA por declaración (ver abajo) | Soporte en el pico |

### Costo de IA por declaración (estimación)

- **Precios usados:** tabla de precios de modelos de Anthropic incluida en la documentación de Claude Code, guardada el 2026-10-06. Antes de presupuestar en serio, hay que verificarla en la página oficial de precios.
  - Claude Sonnet 5.5: USD 2 por millón de tokens de entrada y USD 10 por millón de salida.
  - Claude Haiku 5.5: USD 0,10 y USD 0,50.
  - Claude Opus 5.5: USD 4 y USD 20.
- **Supuestos míos, sin medir:**
  - un cliente manda unos 15 documentos;
  - cada documento son unos 10.000 tokens de entrada y 1.500 de salida.
- **Cuenta:** 150.000 tokens de entrada y 22.500 de salida por declaración. Con Sonnet 5.5 da **unos USD 0,50 por declaración**; con Haiku 5.5, unos USD 0,03.
- **Conclusión (opinión):** el costo de la IA no es el problema. Lo caro es el tiempo de construcción, el mantenimiento de las reglas que cambian cada año y conseguir clientes.

### Cómo encaja con lo que Facu ya sabe hacer (opinión)

- **Lo que se reutiliza:** la app de CEMEVA renombra y ordena facturas y liquidaciones, arma mails con adjuntos y persigue a terceros. Es casi la misma lógica de "pedir, recibir, ordenar y perseguir lo que falta".
- **Lo que NO conviene al principio:** el bot que carga datos en un sistema sin API. Llevado a ARCA, significaría operar con la clave fiscal de cada cliente (ver la sección 6).
- **Lo que falta:** saber de impuestos. Las reglas de valuación de Bienes Personales y las categorías de Ganancias son técnicas. **Hace falta un contador socio o asesor desde el día 1.** El primer candidato es el contador de CEMEVA. Su costo no lo sé: puede ser un porcentaje o horas pagas.

---

## 6. Regulación y riesgos

### Regulación (con fuente)

1. **Datos personales: Ley 25.326, sancionada el 2000-10-04.** Un patrimonio con saldos, inversiones e inmuebles es información muy sensible.
   - Art. 9: hay que aplicar medidas técnicas y organizativas para "garantizar la seguridad y confidencialidad".
   - Art. 10: quien trata los datos guarda secreto, aun después de terminar la relación.
   - **Art. 25 (el más importante para este producto):** quien procesa datos por cuenta de otro, como un software al servicio de un estudio, no puede usarlos para otro fin ni cederlos. Además, "una vez cumplida la prestación contractual los datos personales tratados deberán ser destruidos". Se pueden guardar hasta 2 años solo si el cliente lo autoriza expresamente.
   - **Consecuencia práctica (opinión):** hace falta un contrato con cada estudio, cifrado, borrado automático al terminar la temporada y no usar los datos para entrenar modelos.
2. **Clave fiscal: RG 5048/2021, vigente desde 2021-09-01.**
   - Art. 4: "La utilización de la Clave Fiscal, su resguardo y protección, son de exclusiva responsabilidad del usuario".
   - Arts. 6, 9 y 12: existe la delegación de servicios a un "usuario externo" mediante el Administrador de Relaciones, y el designado tiene que aceptarla.
   - **Opinión:** guardar claves fiscales de clientes es el riesgo legal y de seguridad más grande del rubro. **La primera versión no lo hace:** el contador baja él mismo el CSV de ARCA y lo sube.
   - Si más adelante se automatiza el acceso a ARCA, que sea por delegación de servicios o por servicio web con certificado, nunca guardando claves. Ojo: Witmi pide autorización con la clave de cada cliente para leer el DFE.
3. **DFE: RG 4280/2018, art. 6.** Los terceros autorizados pueden consultar las comunicaciones por servicio web. Sirve si algún día se suma la función de P1.
4. **Responsabilidad profesional (opinión):** el contador firma la DDJJ. El producto entrega un borrador para revisar. Si hay un error de valuación, la multa cae sobre el cliente y el reclamo, sobre el estudio. Hay que dejarlo claro en el contrato y en la pantalla.
   - Según medios (no lo verifiqué en el texto oficial), la Ley 27.826 baja automáticamente un 25% las multas formales para personas humanas y PyMEs.

### Riesgos del negocio

| Riesgo | Evidencia | Gravedad (opinión) |
|---|---|---|
| **ARCA se come el trabajo de Ganancias.** La DJS precarga facturación, retenciones y SIRADIG, y la Ley 27.826 sacó los topes de ingresos y patrimonio para usarla. | Manual de la DJS (septiembre 2026); notas sobre la Ley 27.826 (contadoresenred.com, noticiasnqn.com.ar, iproup.com, 2026-10). Los textos oficiales no los abrí. | **Alta** para Ganancias simple; **media** para Bienes Personales y para casos complejos (agro, inversiones, exterior). |
| **Estacionalidad.** Casi todo el ingreso cae en 3 a 5 meses. En 2026 la temporada se estiró hasta octubre por las prórrogas. | Prórrogas citadas en la sección 3. | Alta para la caja; también da tiempo para construir entre temporadas. |
| **Las reglas cambian cada año.** Solo en 2026: Decreto 93/2026, RG 5820, RG 5836, RG 5851, 5876, 5890, 5911 y Ley 27.826. | Sección 3. | Alta: es mantenimiento fijo. También es una barrera para competidores menos atentos. |
| **Competencia local que suma IA rápido** (ConciliaBot, Genio Contable, Contador-IA, Errepar, Onvio). | Sección 4. | Alta. **Opinión:** la ventana estimada el 2026-10-01 (12 a 24 meses) se está cerrando. |
| **REIBP y umbrales altos** achican el número de declaraciones de Bienes Personales hasta 2027. | Según el buscador; no verificado en fuente oficial. | Media |
| **Facu no es contador.** | — | Media. Se mitiga con un socio contador. |

---

## 7. Filtro final (producto elegido: P2, "Temporada PH")

| Criterio | Nota | Justificación |
|---|---|---|
| **F1. Demanda comprobable en Argentina** | **3** | El dolor está probado con fuentes oficiales y de prensa: 4 prórrogas, una de ellas pedida por las entidades profesionales; pedidos del CPCECABA y la FAGCE; burnout de mayo a julio. Pero **que alguien pague por esta herramienta en particular no está probado.** Hay señales indirectas: ConciliaBot dice tener más de 1000 estudios pagos, Onvio armó un módulo y afuera la categoría recibe cientos de millones de dólares. |
| **F2. Producto automatizable y global** | **3** | Las normas son nacionales e iguales para todos los estudios, así que es global. Pero los documentos vienen de decenas de bancos y brokers, las tablas de valuación cambian cada año y siempre hace falta revisión humana. Es automatizable al 70 u 80%, no al 100% (estimación). |
| **F3. Validable rápido y barato (30 días, menos de USD 300)** | **4** | Las entrevistas y la prueba conserje cuestan casi nada y el momento es ideal: la temporada cierra el 2026-10-30. Le falta el 5 porque el pago real solo puede ser una venta anticipada para la temporada 2027, no uso pago inmediato. |
| **F4. Riesgo legal manejable (5 = bajo)** | **3** | No necesita la clave fiscal al principio, lo cual es bueno. Pero maneja datos patrimoniales muy sensibles (Ley 25.326, arts. 9, 10 y 25) y un error de valuación genera reclamos. |
| **F5. Encaje con Facu** | **4** | Es el patrón de CEMEVA casi exacto (pedir, ordenar, perseguir, leer documentos) y hay un primer contacto cercano (el contador de CEMEVA). Pierde un punto porque hace falta saber de impuestos, que Facu no tiene. |
| **Total** | **17 / 25** | |

### Recomendación: **PENDIENTE**

**Por qué (opinión)**

- El dolor es real y es el mejor documentado del rubro.
- Pero el hueco se está achicando por dos lados: ARCA precarga cada vez más (la DJS ahora para cualquier persona humana) y las herramientas locales ya suman IA.
- Además, no se puede cobrar en serio hasta la temporada 2027 (marzo a julio).
- Como negocio para arrancar ahora, no le gana a una idea que pueda facturar en semanas.

**Excepción que recomiendo hacer igual:** el experimento de la sección 8, en noviembre de 2026. Cuesta casi cero y el momento no se repite hasta dentro de un año. Si da "seguir", la idea sube a PRIMERA, con este calendario: construir de diciembre a marzo y vender en marzo y abril de 2027.

---

## 8. Primer experimento concreto

**Qué:**

1. 10 entrevistas al estilo The Mom Test: se pregunta por lo que el contador ya hizo, no por lo que haría, y no se vende nada.
2. Una prueba "conserje" con 3 carpetas reales de la temporada 2025, anonimizadas y con permiso del cliente. Facu, a mano con Claude y una plantilla de Excel, arma el papel de trabajo: valuación, diferencias contra lo que precargó ARCA y lista de faltantes. Después se compara con lo que hizo el estudio.

**Con quién y cómo llegar**

1. **El contador o estudio que atiende a CEMEVA** (contacto cercano). Pedirle una entrevista y 3 colegas referidos.
2. Contadores que publican en LinkedIn o en redes sobre la temporada de Ganancias. Contacto uno a uno, nunca masivo.
3. Comunidades y sitios del rubro: Blog del Contador y Contadores en Red, que existen. No verifiqué si tienen foros o grupos.
4. Actividades del consejo profesional local, como charlas o cursos.

**Calendario**

- 2026-10-20 a 2026-10-31: preparar la guía, la plantilla y los contactos. No pedir entrevistas antes del 2026-10-30: están en pleno vencimiento.
- 2026-11-02 a 2026-11-20: entrevistas y pruebas conserje.

**Costo y tiempo:** USD 0 a 100 (traslados y cafés; Claude ya lo tiene). 30 días y unas 40 h.

**Número para "seguir" (se tienen que cumplir los 4)**

- Al menos 6 de 10 contadores ponen la temporada de personas humanas entre sus 2 peores dolores **sin que se lo sugieras**.
- Al menos 3 entregan una carpeta real para la prueba.
- La prueba ahorra al menos 40% del tiempo que ellos dicen haber usado en ese cliente.
- Al menos 2 dejan una seña o firman un compromiso de compra para la temporada 2027. El precio sale de lo que digan que cobran por cada DDJJ.

**Número para "cortar" (alcanza con 1)**

- Menos de 3 de 10 lo ponen entre sus 2 peores dolores.
- Nadie entrega una carpeta.
- Ningún compromiso de pago.
- La prueba ahorra menos de 20% del tiempo.

**Pérdida máxima:** USD 150 y 40 horas. Si se pasa, se corta igual.

**Qué anotar en cada entrevista:**

- cuántas DDJJ de personas humanas hicieron en 2026;
- horas de la más difícil y en qué se fueron;
- cuánto cobran por cada DDJJ (dato que no conseguí);
- qué software pagan hoy y cuánto;
- si tienen clientes productores agropecuarios.

### 5 preguntas al estilo The Mom Test

1. "Contame cómo fue la última declaración de Bienes Personales o Ganancias de una persona que hiciste esta temporada, desde que le pediste los papeles hasta que la presentaste. ¿Qué pasó en el medio?"
2. "¿Cuál fue la que más horas te llevó este año? ¿En qué se fueron esas horas, concretamente?"
3. "La última vez que un cliente no te mandaba un certificado o un resumen a tiempo, ¿qué hiciste? ¿Cuántas veces le escribiste?"
4. "¿Qué diferencias encontraste entre lo que ARCA te precargó y lo que traía el cliente? ¿Cómo las resolviste y cuánto tardaste?"
5. "¿Qué usás hoy para esto (planilla, sistema, Onvio, ConciliaBot, otro)? ¿Cuánto pagás? ¿Probaste algo este año y lo dejaste? ¿Por qué?"

Para cerrar: "¿A quién más le pasa esto? ¿Me lo presentarías?"

---

## 9. Fuentes (todas consultadas el 2026-10-15)

**Marcas:** [abierta] = leí la página. [buscador] = solo vi el resumen del buscador; no la abrí.

### Normas y organismos oficiales

- RG 4597/2019, Libro de IVA Digital: texto actualizado https://www.argentina.gob.ar/normativa/nacional/norma-329339/actualizacion [abierta]; normas que la modifican https://www.argentina.gob.ar/normativa/nacional/resoluci%C3%B3n-4597-2019-329339/normas-modifican [abierta]; RG 5707/2025 https://www.argentina.gob.ar/normativa/nacional/norma-413495 [abierta]
- Monotributo, recategorización: https://www.arca.gob.ar/monotributo/ayuda/desarrollo-de-la-actividad.asp [abierta]; categorías: https://www.arca.gob.ar/monotributo/categorias.asp [abierta]
- Prórroga de Ganancias y Bienes Personales, RG 5876/2026: https://servicioscf.afip.gob.ar/publico/sitio/contenido/novedad/ver.aspx?id=5823 [abierta]
- Prórroga excepcional (2026-05-22): https://www.argentina.gob.ar/noticias/prorroga-excepcional-para-la-presentacion-y-pago-de-ganancias-bienes-personales-y-cedular [abierta]
- Nota de ARCA sobre la RG 5890: https://servicioscf.afip.gob.ar/publico/sitio/contenido/novedad/ver.aspx?id=5877 [la página no devolvió contenido; dato del buscador]
- Micrositio de Ganancias y Bienes Personales (vencimiento 2026-10-30): https://www.afip.gob.ar/gananciasYBienes/ [abierta]; Ganancias: https://www.afip.gob.ar/gananciasYBienes/ganancias/default.asp [abierta]
- Manual de la DJS (F.2711), versión 2.09/26: https://www.afip.gob.ar/gananciasYBienes/documentos/Manual-DJS.pdf [abierta; texto extraído del PDF]
- Régimen de Inocencia Fiscal, Decreto 93/2026: https://www.argentina.gob.ar/normativa/nacional/decreto-93-2026-423013/texto [buscador]; https://www.arca.gob.ar/comunicacion/inocencia-fiscal/ [buscador]; RG 5836/2026: https://www.boletinoficial.gob.ar/detalleAviso/primera/340959/20260420 [buscador]
- RG 5847/2026 (cita la RG 4172 como base del calendario): https://www.boletinoficial.gob.ar/detalleAviso/primera/341998/20260515 [buscador]
- Calendario 2026 de la Comisión Arbitral, RG CA 21/2025: https://www.argentina.gob.ar/normativa/nacional/norma-421279/actualizacion [buscador]
- Comisión Arbitral: https://www.ca.gob.ar/ [abierta]; SIFERE: https://www.ca.gob.ar/sistemas/sifere [abierta]; SIRCREB: https://www.ca.gob.ar/sistemas/sircreb [abierta]
- Declaración en Línea, normativa: https://www.afip.gob.ar/declaracionEnLinea/ayuda/normativa.asp [abierta]
- Libro de Sueldos Digital, normativa: https://www.afip.gob.ar/LibrodeSueldosDigital/ayuda/normativa.asp [abierta]
- SIRADIG, normativa: https://www.afip.gob.ar/572web/ayuda/normativa.asp [abierta]
- SIRE / SICORE, normativa: https://www.afip.gob.ar/sire/ayuda/normativa.asp [abierta]
- RG 4280/2018, Domicilio Fiscal Electrónico: https://www.argentina.gob.ar/normativa/nacional/resoluci%C3%B3n-4280-2018-312678/texto [abierta]
- RG 5048/2021, Clave Fiscal: https://www.argentina.gob.ar/normativa/nacional/norma-352970/texto [abierta]
- Ley 25.326, Protección de Datos Personales: https://www.argentina.gob.ar/normativa/nacional/ley-25326-64790 y https://www.argentina.gob.ar/normativa/nacional/ley-25326-64790/texto [abiertas]
- Vencimientos de ARCA: https://www.arca.gob.ar/vencimientos/ [abierta, sin datos]; https://www.argentina.gob.ar/arca/vencimientos [buscador]

### Consejos profesionales

- FACPCE: https://www.facpce.org.ar/ [abierta]
- CPCECABA: https://www.consejo.org.ar/ [abierta]; prórroga de Ganancias 2025 (RG 5911/2026, Ley 27.826): https://www.consejo.org.ar/noticias/2026/ganancias-2025-nueva-prorroga-para-la-presentacion-de-la-declaracion-jurada [abierta]
- Honorarios mínimos del consejo de Salta (módulo $18.500 desde 2026-10-01): https://www.consejosalta.org.ar/2026/03/actualizacion-del-valor-del-modulo-para-honorarios-minimos/ [buscador]
- Revista Mercado, nota de 2008 sobre el CPCECABA: https://mercado.com.ar/revista/numero-1081/apertura-a-egresados-de-las-nuevas-carreras/ [abierta]

### Prensa

- iProfesional, 2026-08-18, "El reto de ser contador en Argentina…": https://www.iprofesional.com/impuestos/461079-el-desafio-de-ser-contador-en-argentina-de-luchar-con-arca-a-los-cambios-normativos [abierta]
- El Economista, 2026-05-09, "Ganancias: cada vez son más los contadores que piden una prórroga…": https://eleconomista.com.ar/economia/ganancias-cada-vez-son-mas-contadores-piden-una-prorroga-impuesto-n94802 [abierta]
- iProfesional, 2026-05-16, Genio Contable: https://www.iprofesional.com/impuestos/454685-son-argentinos-y-crearon-una-ia-que-permite-liquidar-impuestos-facil-como-funciona [abierta]
- Blog del Contador, aplicativos web de Ganancias y Bienes Personales 2025: https://siap.blogdelcontador.com.ar/?p=82544 [abierta]
- Ley 27.826 (Inocencia Fiscal II): https://contadoresenred.com/?p=33294 , https://www.noticiasnqn.com.ar/noticias/2026/10/09/355866-inocencia-fiscal-ii-los-cambios-en-ganancias-los-controles-de-arca-y-las-multas , https://www.iproup.com/economia-digital/72205-el-gobierno-reglamento-la-ley-de-inocencia-fiscal-ii [buscador]
- Errepar Consultor IA (2026-08-21): https://documento.errepar.com/actualidad/presentamos-consultor-ia-una-nueva-forma-de-resolver-consultas-profesionales-con-inteligencia-20260819194358688 [abierta]
- Onvio, módulo de Ganancias y Bienes Personales (2026-04-06): https://www.thomsonreuters.com.ar/es/soluciones-fiscales-contables-gestion/blog-contadores/llega-el-nuevo-modulo-de-onvio-ganancias-y-bienes-personales.html [abierta]
- Nodecraft (proveedor, 2026-04-24), horas por tarea: https://www.nodecraft.com.ar/blog/cuanto-tiempo-pierde-tu-contador [abierta]

### Empresas argentinas (sitios propios)

- https://www.sos-contador.com/ [abierta]
- https://witmi.ar/ [abierta]
- https://conta.com.ar/ [abierta]
- https://appcontador.com.ar/ [abierta]
- https://www.aconpy.com/ [abierta]
- https://geniocontable.com/ [abierta]
- https://contatech.org/conciliabot [abierta]
- https://contador-ia.com/ [abierta]
- https://calim.com.ar/ [abierta]
- https://afipsdk.com/ [abierta]
- https://www.holistor.com.ar/ [abierta]
- https://www.estudiocodina.com.ar/Sistemas.htm , https://km44.com.ar/ , https://gestorando.com/recategorizacion-del-monotributo/ [buscador]

### Afuera

- Juno: https://www.cpapracticeadvisor.com/2026/04/13/juno-raises-12m-seed-to-scale-ai-tax-preparation-platform-that-automates-90-of-busy-work/181502/ [abierta]
- Basis: https://www.cpapracticeadvisor.com/2026/02/24/basis-raises-100-million-to-deploy-ai-agents-for-accounting-firms/178759/ [abierta]
- Filed (proveedor, 2026-06-16), comparación de plataformas y precios: https://www.filed.com/blog/best-ai-tax-prep-platforms [abierta]
- Accrual: https://www.cpapracticeadvisor.com/2026/02/05/startup-accrual-officially-launches-with-75m-in-funding-to-bring-ai-native-automation-to-accounting/177600/ [buscador]

### Interno

- Precios de modelos de Anthropic: documentación de la API de Claude incluida en Claude Code (tabla guardada el 2026-10-06). Verificar en la página oficial antes de presupuestar.
- Registro de ideas del proyecto: `research/datos/registro-de-ideas.csv` (B18, F17, F18, I14, SER-1-1 a SER-1-5, SER-2-1, SER-4-1).
