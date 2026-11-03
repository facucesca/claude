# Informe fuente: Servicios de automatización con IA / "AI Automation Agency" (2026-10-01)

> Informe crudo del agente de investigación — frente **agencia de automatización con IA** (voz, WhatsApp, chatbots, n8n/Make, reactivación, CRM, documentos, white-label, freelance).
> Marcas de calidad de fuente: **[oficial]** = página/política de la propia plataforma; **[analista]** = firma de research con metodología (Sacra, etc.); **[vendedor]** = blog de una empresa que vende la herramienta o el servicio (conflicto de interés); **[gurú]** = contenido que vende curso/comunidad/herramienta para "agencias"; **[blog]** = sin metodología verificable; **[sin fuente propia]** = inferencia del analista a partir de datos vecinos — verificar antes de decidir.

---

## 0. Resumen ejecutivo (para el que no lee todo)

1. **La demanda es real, pero el negocio de "agencia de IA" genérica está saturado y lleno de gurús.** El mercado de agentes IA ronda USD 7,6-15 mil M en 2026 con CAGR 34-45% [analista vía vendedor, Ciela, 2025-11-15], Retell AI pasó de USD 10M a **USD 60M ARR (abril 2026, +650% interanual)** [analista, Sacra]. Pero el ecosistema de cursos ("AAA") vende el sueño independientemente de si el alumno consigue clientes [blog, Layer3 Labs, 2026-09-02]. **No existe estadística primaria seria de mediana de ingresos de "AI agencies".** Lo más honesto que encontré: "3 a 6 proyectos reales en el primer año" es el rango común [blog, Layer3, 2026-09-02]; mediana de 7 meses desde el primer proyecto hasta USD 10k/mes entre operadores que ya facturan (survivorship: excluye a los que nunca facturaron) [blog, BetOnAI, rate card de 54 operadores, act. 2026-09-20].
2. **Para un argentino que no programa, el terreno con ventaja es WhatsApp + LATAM + vertical aburrido**, no voz en inglés para EE.UU. Penetración de WhatsApp en Argentina: **90%** de usuarios de internet (We Are Social/Meltwater 2025, citado por HubSpot 2026-05-21) [blog que cita encuesta]. Meta habilitó **facturación en ARS desde 2026-04-01** [oficial]. Kommo ofrece programa de partners **gratis** con **35% de descuento / 35-50% de comisión vitalicia y 100% de la primera venta** [oficial, consultado 2026-10-01].
3. **Voz IA hacia EE.UU. = alto ticket pero alto riesgo legal para él.** La FCC (Declaratory Ruling FCC 24-17, 2024-02-08) declaró que las voces de IA son "voz artificial" bajo la TCPA → llamadas salientes requieren consentimiento previo expreso [oficial vía múltiples fuentes]. Inbound (recepcionista) es mucho más seguro que outbound.
4. **WhatsApp cambia reglas y precios cada trimestre**: desde **2026-01-15** Meta prohíbe chatbots de IA de "propósito general" en la API (sí permite bots de soporte, turnos, ventas, seguimiento con derivación a humano) [vendedor, respond.io, citando política Meta]; desde **2026-10-01** los mensajes de servicio se cobran a partir del mensaje 1.001 por número/mes y desde **2026-08-01** las respuestas del "Meta Business Agent" se cobran ~USD 2/M tokens [vendedor-BSP, YCloud]. ⚠️ La página oficial de developers de Meta consultada el 2026-10-01 todavía dice que "utility templates within an open customer service window are free" → **discrepancia a verificar** antes de cotizar.
5. **Ranking del frente para ESTE usuario** (top 5 al final): (1) Implementador partner Kommo + bot WhatsApp vertical, (2) Cobranzas por WhatsApp con link de Mercado Pago, (3) Turnos + recordatorios + reactivación para consultorios, (4) Documentos/facturas → planilla para estudios contables, (5) Reportes automáticos + lectura de remitos para distribuidoras (sinergia con "orden operativo").

---

## 1. Metodología y limitaciones

- **Fecha de corte:** 2026-10-01. Fuentes priorizadas 2025-2026.
- **Búsquedas:** 16 WebSearch + ~30 WebFetch a páginas primarias (pricing oficiales de Meta, Kommo, n8n, GoHighLevel, ElevenLabs, Synthflow, Leadsales; Sacra; Upwork/PYMNTS; AAIP; etc.).
- ⚠️ **Limitación importante:** la cuota de WebSearch de la sesión (200 búsquedas, compartida con otros agentes en paralelo) se agotó después de 16 búsquedas propias. Lo compensé yendo directo a páginas oficiales con WebFetch, pero **varias ideas (marcadas [sin fuente propia])** se apoyan en datos vecinos y en conocimiento previo hasta junio 2026. Antes de pasar cualquiera de ellas a `ideas/`, hacer 3-5 búsquedas de validación específicas.
- **Sesgo dominante del frente:** la enorme mayoría del contenido sobre "AI agencies" lo publican (a) vendedores de plataformas (Vapi, Retell, Ciela, GoHighLevel y sus afiliados) o (b) gurús que venden cursos/comunidades (Skool, YouTube). Los números de "USD 10k/mes en 90 días" son **anecdóticos con conflicto de interés**. Uso rangos de precio de lista como techo, no como mediana.
- Score 1-10 = potencial realista **para este usuario** (AR, no programa, presupuesto < USD 1.000, apoyo en Claude, ing. industrial), no para "un emprendedor genérico".

### Datos transversales del frente (para no repetirlos en cada idea)

| Dato | Valor | Fuente / fecha |
|---|---|---|
| Precio típico agencia recepcionista IA | Setup USD 1.500-5.000; retainer USD 300-800/mes por agente | [gurú/vendedor] Ciela, 2026-01-08 |
| Precio "agentes que pagan las empresas" | Setup 1-15k, mensual 300-1.500 | [gurú] Buldrr 2026 — precios de lista, inflados |
| Costo real voz (all-in) | Vapi USD 0,10-0,30/min; Retell 0,10-0,35; Bland 0,09-0,20 | [blog] Ainora 2026 |
| Retell plataforma | USD 0,055/min + pass-through LLM/STT/TTS | [analista] Sacra, abr-2026 |
| ElevenLabs Agents | Planes USD 6-990/mes; Pro USD 99 = 1.238 min; extra USD 0,08/min; LLM aparte | [oficial] elevenlabs.io/pricing/agents, 2026-10-01 |
| Synthflow | Pricing público solo Enterprise **desde USD 30.000/año** (giró a enterprise) | [oficial] synthflow.ai/pricing, 2026-10-01 |
| GoHighLevel | USD 97 / 297 / 497 (SaaS mode); AI Employee USD 50-97/sub-cuenta; WhatsApp USD 10/sub-cuenta | [oficial] gohighlevel.com/pricing, 2026-10-01 |
| n8n | Cloud Starter €20/mes (2.500 ejecuciones), Pro €50; Community self-hosted gratis | [oficial] n8n.io/pricing, 2026-10-01 |
| Kommo | Desde ~USD 15/usuario/mes; partner gratis, 35% descuento, 35-50% comisión vitalicia, 100% primera venta | [oficial] kommo.com, 2026-10-01 |
| Leadsales (CRM WhatsApp MX) | USD 97-247/mes + agente IA USD 87/mes | [oficial] leadsales.io/precios, 2026-10-01 |
| Bot WhatsApp PyME AR | USD 50-115/mes total (Meta ~8-35 + BSP 40-80) para ~500 conversaciones | [vendedor] Develop Argentina, 2026-06-25 |
| Rate freelance automatización | Principiante n8n USD 60-90/h; LATAM cobra 35-55% de la tabla salvo que venda en USD al exterior | [blog] BetOnAI, 54 operadores, act. 2026-09-20 |
| Upwork | GSV de trabajo IA +22% interanual (~USD 330M anualizado), desacelerando desde +50% en Q4-2025; clientes activos -4% (763k) | [prensa sobre earnings] PYMNTS, 2026-08-10 |
| Upwork In-Demand Skills 2026 | Habilidades IA +109% interanual; "AI integration" +178%; chatbot development +71% | [oficial vía prensa] selfemployed.com citando Upwork (no pude abrir el release: timeout) |
| Demo → cierre | ~25% promedio | [vendedor] Ciela, 2025-12-03 |
| Adopción IA en servicios residenciales EE.UU. | 17% (2026) → >40% proyectado 2028 | [vendedor] Fieldproxy, 2026-03-12 (800 empresas) |

---

## 2. Las ideas (42)

Formato de cada ficha: **Qué es · Quién lo hace / señal · Cobro y precio · Ejecución sin programar · Tipo y horas · Capital y primer dólar · Cobro desde AR · Riesgos · Score**.

---

### BLOQUE A — Agentes de voz

#### 1. Recepcionista IA "fuera de horario" para consultorios odontológicos (EE.UU./España)
- **Qué es:** agente de voz que atiende solo cuando el consultorio está cerrado o saturado: responde FAQ, toma datos, agenda en el calendario y manda resumen por SMS/email.
- **Quién / señal:** es la oferta "de manual" de las agencias de voz; ejemplo publicado: clínica dental de Sídney con 23 turnos agendados en 30 días [gurú, Buldrr 2026 — anecdótico]. Plataforma subyacente en auge: Retell **USD 60M ARR abr-2026, +650%** y 40M+ llamadas/mes [analista, Sacra].
- **Cobro:** setup USD 1.500-5.000 + USD 300-800/mes [gurú/vendedor, Ciela 2026-01-08]. Mediana realista para principiante: setup USD 500-1.500 + USD 200-400/mes [sin fuente propia]. Costo herramienta: USD 0,10-0,30/min + número telefónico (~USD 1-2/mes).
- **Ejecución:** Retell/Vapi tienen editores visuales; Claude escribe el prompt del agente, el árbol de derivación, la base de conocimiento (FAQ de la clínica) y los scripts de prueba. Él hace las llamadas de test, la venta y la integración de calendario vía Cal.com/Google Calendar (no-code). Integración con software dental (Dentrix, etc.) = difícil sin programar → limitar a calendario.
- **Tipo:** semi-pasivo. 1-2 h/semana por cliente en régimen (revisar transcripciones, ajustar).
- **Capital / primer dólar:** USD 50-150 (créditos + número). 2-4 meses (venta en frío al exterior).
- **Cobro AR:** clientes en EE.UU./España vía Payoneer o transferencia; la factura E de exportación de servicios desde monotributo funciona. Desventaja: vender en frío a dentistas de EE.UU. desde AR, con acento y huso horario, es difícil.
- **Riesgos:** inbound es de bajo riesgo TCPA, pero HIPAA (EE.UU.) aplica si maneja datos de salud → necesita BAA con el proveedor (Retell/Vapi lo ofrecen en planes altos). Saturación altísima: es la oferta n°1 de todos los cursos. Churn si el agente se equivoca con un paciente.
- **Score: 5/10.**

#### 2. Recepcionista IA bilingüe para negocios hispanos en EE.UU. (clínicas, talleres, abogados de inmigración)
- **Qué es:** igual que la 1, pero el diferencial es el español rioplatense/neutro de calidad para negocios de dueños o clientela latina en EE.UU. (Texas, Florida, California).
- **Quién / señal:** los agentes globales vienen configurados en inglés por defecto y responden en inglés aunque el usuario hable español — problema reportado en LATAM [blog, HubSpot 2026-05-21]. Que ElevenLabs y Retell soporten español con voces nativas habilita el nicho [oficial].
- **Cobro:** USD 300-1.000 de setup + USD 200-500/mes [sin fuente propia; extrapolado de la 1].
- **Ejecución:** Claude redacta prompts en dos idiomas, guiones de prueba y el material de venta en inglés/español. Él hace demos grabadas en español (su ventaja natural) y outreach por LinkedIn/Facebook a cámaras de comercio hispanas.
- **Tipo:** semi-pasivo, 1-2 h/sem/cliente.
- **Capital / primer dólar:** < USD 150. 2-4 meses.
- **Cobro AR:** exterior vía Payoneer. Clientes pagan en USD (bien).
- **Riesgos:** abogados de inmigración = sensibilidad alta (no dar consejo legal). TCPA si hace outbound. Diferencial frágil: el español de los modelos mejora para todos.
- **Score: 6/10.** Mejor que la 1 por diferencial idiomático.

#### 3. Agente de voz para restaurantes (reservas + pedidos telefónicos)
- **Qué es:** atiende el teléfono del restaurante, toma reservas o pedidos.
- **Quién / señal:** Loman (desde USD 199/mes, toma pedidos y cobra en la llamada, 9 integraciones POS) y Slang.ai (desde USD 399/mes) [vendedor, loman.ai 2026-08].
- **Cobro:** competir con SaaS a USD 199-399/mes deja poco margen para una agencia.
- **Ejecución:** sin integración POS (requiere código o partner) el producto es inferior al SaaS.
- **Tipo:** semi-pasivo.
- **Capital / primer dólar:** bajo; 3-6 meses.
- **Cobro AR:** en AR los restaurantes reciben pedidos por WhatsApp/PedidosYa, no por teléfono → el mercado local es chico.
- **Riesgos:** SaaS verticales ya resolvieron el problema mejor y más barato. Una agencia es intermediario innecesario.
- **Score: 3/10.**

#### 4. Confirmación de turnos por voz (outbound a pacientes con consentimiento)
- **Qué es:** el agente llama 24-48 h antes para confirmar, reprogramar o liberar el turno.
- **Quién / señal:** función estándar en suites de agendamiento; Cliengo y XIAgenda lo hacen por WhatsApp en AR [vendedor].
- **Cobro:** USD 150-400/mes o por turno confirmado [sin fuente propia].
- **Ejecución:** Retell/Vapi + Google Sheets/Calendar + Make/n8n (plantillas existentes); Claude arma el flujo.
- **Tipo:** semi-pasivo, 1 h/sem/cliente.
- **Capital / primer dólar:** < USD 100. 2-3 meses.
- **Cobro AR:** local por Mercado Pago/transferencia.
- **Riesgos:** en AR el paciente prefiere WhatsApp antes que una llamada robótica → el canal correcto es la idea 10, no esta. En EE.UU., outbound con voz IA = consentimiento previo expreso (FCC 24-17).
- **Score: 4/10.**

#### 5. Speed-to-lead por voz para contratistas (HVAC/techos) en EE.UU.
- **Qué es:** cuando un lead completa un formulario, el agente lo llama en menos de 60 s, lo califica y agenda la visita.
- **Quién / señal:** "40% de los contratistas de techos ya usan IA para captar leads en los primeros 60 s" [blog, 2026]; respuesta en < 2 min convierte 62% contra 28% a 42 min [vendedor, sin metodología]. Precio de mercado USD 500-1.500/mes [blog].
- **Cobro:** USD 1.000-3.000 setup + USD 500-1.500/mes.
- **Ejecución:** GoHighLevel o Make + Retell; Claude configura los prompts. Él tiene que entender el CRM del contratista.
- **Tipo:** semi-pasivo; 2-3 h/sem/cliente.
- **Capital / primer dólar:** USD 100-300 (GHL Starter USD 97). 3-6 meses.
- **Cobro AR:** exterior vía Payoneer.
- **Riesgos:** **TCPA**: es outbound con voz artificial; el consentimiento del formulario debe ser explícito; las demandas de clase en EE.UU. cuestan millones. Saturadísimo en YouTube. Sin presencia en EE.UU. cuesta mucho cerrar.
- **Score: 4/10.**

#### 6. Agente telefónico para talleres mecánicos (estado del auto + turnos)
- **Qué es:** atiende "¿está listo mi auto?" y "¿cuánto sale un service?", agenda turnos y deriva lo complejo.
- **Quién / señal:** aparece en las listas de "off-hours receptionist" para repair shops [gurú, Buldrr 2026]. Sin dato de adopción específico [sin fuente propia].
- **Cobro:** USD 150-400/mes en EE.UU.; en AR, el canal es WhatsApp (ver idea 19 de talleres por WhatsApp — combinable).
- **Ejecución:** igual que 1 + planilla de estado de órdenes que el taller actualiza.
- **Tipo:** semi-pasivo.
- **Capital / primer dólar:** < USD 100. 3-5 meses.
- **Cobro AR:** mixto.
- **Riesgos:** el taller tiene que actualizar el estado en algún lado; si no, el agente miente. Problema de proceso, no de IA (le cuadra a su perfil industrial, pero la venta es difícil).
- **Score: 4/10.**

#### 7. Calificación de interesados por voz para inmobiliarias (alquileres)
- **Qué es:** el agente llama/atiende a interesados de portales, pregunta ingresos, garantía, mascotas, fechas y agenda visita solo a los que califican.
- **Quién / señal:** inmobiliarias aparecen como vertical de los partners Kommo (Emarkets, Planiva) [oficial-directorio Kommo]. Sin dato numérico propio [sin fuente propia].
- **Cobro:** USD 150-500/mes.
- **Ejecución:** mejor por WhatsApp (idea 11). Por voz, Retell + planilla.
- **Tipo:** semi-pasivo.
- **Capital / primer dólar:** bajo; 2-4 meses.
- **Cobro AR:** local.
- **Riesgos:** en AR nadie atiende llamadas de números desconocidos → canal equivocado.
- **Score: 3,5/10.**

#### 8. Encuestas post-servicio / NPS por voz o WhatsApp
- **Qué es:** después del servicio, el agente pregunta satisfacción, registra quejas y, si el cliente está feliz, pide reseña en Google.
- **Quién / señal:** "post-job review requests" con aumentos de reseñas de 300-500% en 90 días [vendedor, ScaleLogix en dev.to 2026]; agente de reseñas a USD 300-500/mes [gurú, Buldrr].
- **Cobro:** USD 100-300/mes por local.
- **Ejecución:** WhatsApp + Google Forms/Sheets + Make; Claude arma mensajes y reportes.
- **Tipo:** casi pasivo (0,5 h/sem/cliente).
- **Capital / primer dólar:** < USD 50. 1-2 meses.
- **Cobro AR:** local, bien.
- **Riesgos:** Google prohíbe el "review gating" (pedir reseña solo a los satisfechos) — hay que pedirla a todos o arriesgar el perfil. Commodity (muchas herramientas lo hacen por USD 30-50/mes).
- **Score: 5/10** como add-on, no como negocio único.

#### 9. Reventa white-label de una plataforma de voz IA (estilo "tu propio Synthflow")
- **Qué es:** contratar la plataforma de un tercero con marca propia y revenderla por minuto/mes a agencias o PyMEs.
- **Quién / señal (en contra):** Synthflow, que fue la favorita de los cursos para white-label, hoy solo publica plan Enterprise **desde USD 30.000/año** [oficial, 2026-10-01]. Hay reemplazos (VoiceAI white-label, Vapi + dashboards de terceros).
- **Cobro:** markup sobre minutos (USD 0,10 → 0,25-0,50/min).
- **Ejecución:** requiere soporte técnico de nivel 2 que él no puede dar.
- **Tipo:** "pasivo" en teoría; en la práctica, soporte constante.
- **Capital / primer dólar:** USD 300-2.500+/mes de plataforma. 4-8 meses.
- **Cobro AR:** complicado (facturar uso por minuto al exterior).
- **Riesgos:** márgenes comprimidos por la caída del precio por minuto (Retell vende "70-95% más barato que agentes offshore" [Sacra]); dependencia total de un proveedor que puede cambiar precios, como pasó con Synthflow.
- **Score: 2,5/10.**

---

### BLOQUE B — WhatsApp (el corazón LATAM)

#### 10. Turnos + recordatorios + confirmación por WhatsApp para consultorios y centros médicos (AR)
- **Qué es:** bot de WhatsApp (API oficial) que agenda, confirma 48 h antes con botones, reprograma y libera huecos; deriva a la secretaria lo que no entiende.
- **Quién / señal:** XIAgenda (agente IA por WhatsApp para clínicas AR), Cliengo (agente IA que agenda/confirma/reprograma, AR) [vendedor]; Wati tiene landing específica para turnos clínicos en Argentina [vendedor]. Penetración WhatsApp AR 90% [encuesta, We Are Social 2025].
- **Cobro:** setup USD 150-500 + USD 60-150/mes por consultorio pequeño (costo herramienta USD 50-115/mes según Develop Argentina) [vendedor + sin fuente propia]. Centros con varios profesionales: USD 200-400/mes.
- **Ejecución:** él NO construye la plataforma: elige un SaaS (Kommo, Cliengo, Botmaker, Wati, o Chatwoot + n8n si quiere más margen) y hace la **implementación**: relevar agenda, reglas, FAQs, mensajes, pruebas, capacitación de la secretaria. Claude redacta flujos, FAQs, plantillas de Meta (para que las aprueben), manuales y propuestas.
- **Tipo:** semi-pasivo. Setup 10-20 h; régimen 1 h/sem/cliente.
- **Capital / primer dólar:** USD 0-100 (cuentas demo). 1-2 meses con red local.
- **Cobro AR:** local, en pesos o USD MEP por transferencia/Mercado Pago, factura C de monotributo. **Viable.**
- **Riesgos:** compite con el SaaS directo (el consultorio puede contratar Cliengo solo); el valor está en la implementación y el acompañamiento. **Datos de salud = datos sensibles bajo Ley 25.326** → registro de base ante AAIP, consentimiento, y contrato de encargado de tratamiento [oficial AAIP]. Meta exige derivación a humano [respond.io]. Precios de Meta cambiando (2026-10-01).
- **Score: 7/10.**

#### 11. Bot de WhatsApp para inmobiliarias (AR): califica leads de portales y agenda visitas
- **Qué es:** los leads de Zonaprop/Argenprop/Mercado Libre caen al WhatsApp; el bot responde al instante con la ficha, hace 4-5 preguntas de calificación, ofrece horarios de visita y pasa al corredor solo los calificados.
- **Quién / señal:** partners Kommo LATAM implementan exactamente esto (Planiva, Emarkets, 9 Ideas) [oficial-directorio Kommo]. Leadsales (MX) vende CRM WhatsApp + "Lead Agent" IA a USD 87/mes [oficial].
- **Cobro:** setup USD 300-800 + USD 100-250/mes (o sumarlo a la licencia Kommo con comisión).
- **Ejecución:** Kommo + Salesbot (constructor visual) + plantillas; Claude escribe el árbol de calificación y los mensajes por tipo de propiedad. Él releva el proceso comercial (le sirve su formación de procesos).
- **Tipo:** semi-pasivo; 1-2 h/sem/cliente.
- **Capital / primer dólar:** USD 0 (partner gratis). 1-3 meses.
- **Cobro AR:** local. Las inmobiliarias tienen caja en USD.
- **Riesgos:** las inmobiliarias chicas son reacias a pagar mensualidades; mercado inmobiliario AR cíclico. Calidad del bot = calidad de los datos de la ficha.
- **Score: 6,5/10.**

#### 12. Cobranzas y recordatorios de pago por WhatsApp con link de Mercado Pago
- **Qué es:** sistema que lee una planilla de deudores (cuotas de gimnasio, colegios, clubes, cooperativas, alquileres, cuotas de consorcios), manda recordatorios escalonados con link de pago de Mercado Pago, registra respuestas ("pago el viernes") y avisa al dueño.
- **Quién / señal:** la cobranza es la categoría "utility" de WhatsApp que Meta explícitamente permite [oficial/respond.io]; los partners Kommo ofrecen "mensajería masiva" para colegios y clínicas (Emarkets "WhatsFlash") [oficial-directorio]. Sin dato de mercado AR específico [sin fuente propia] — validar.
- **Cobro:** setup USD 200-500 + USD 80-200/mes, o **% de lo recuperado** (3-8%) para morosos viejos — modelo fácil de vender porque se paga solo [sin fuente propia].
- **Ejecución:** Google Sheets + n8n/Make + API de WhatsApp (vía BSP no-code) + API de links de Mercado Pago (Make tiene módulo). Claude arma el workflow paso a paso y redacta mensajes que no suenen a amenaza.
- **Tipo:** semi-pasivo. Corre solo; 0,5-1 h/sem/cliente.
- **Capital / primer dólar:** < USD 100. 1-2 meses.
- **Cobro AR:** local, perfecto; el ROI se mide en pesos recuperados.
- **Riesgos:** Ley de Defensa del Consumidor y prácticas abusivas de cobranza (no horarios nocturnos, no tono intimidatorio, no avisar a terceros); mensajes "utility" se cobran por mensaje desde 2026-10-01. Meta puede bloquear el número si hay muchos reportes de spam.
- **Score: 7/10.** ROI medible, venta simple, encaja con su perfil de procesos.

#### 13. Bot de pedidos por WhatsApp para gastronomía (alternativa a comisiones de apps)
- **Qué es:** menú + toma de pedido + cobro por link + aviso a cocina por WhatsApp.
- **Quién / señal:** "gastronomía" es rubro citado por las guías de chatbot AR [vendedor, Develop Argentina]. Ya existen SaaS de menú-WhatsApp baratos (Pedix, Takeaway apps) [sin fuente propia].
- **Cobro:** USD 30-80/mes — ticket bajo.
- **Ejecución:** fácil con plantillas.
- **Tipo:** semi-pasivo.
- **Capital / primer dólar:** bajo; 1 mes.
- **Cobro AR:** local.
- **Riesgos:** ticket bajo + churn alto de gastronomía + SaaS baratos = mal negocio de servicios.
- **Score: 3,5/10.**

#### 14. WhatsApp para agencias de autos usados / concesionarias: calificación + seguimiento
- **Qué es:** leads de Mercado Libre Autos/Facebook al WhatsApp → bot pregunta modelo, forma de pago, permuta; agenda test drive; seguimiento automático a 3/7/15 días.
- **Quién / señal:** las concesionarias son vertical típico de partners CRM LATAM [sin fuente propia específica]; "seguimiento automático de presupuestos" mejora el cierre 18-35% en servicios [vendedor, ScaleLogix 2026].
- **Cobro:** setup USD 400-1.000 + USD 150-300/mes.
- **Ejecución:** Kommo/Leadsales + Salesbot; Claude arma la secuencia.
- **Tipo:** semi-pasivo.
- **Capital / primer dólar:** USD 0-100; 2-3 meses.
- **Cobro AR:** local, en USD.
- **Riesgos:** vendedores de autos resisten el CRM ("yo tengo mis clientes en el celu"); adopción es el problema.
- **Score: 5,5/10.**

#### 15. Atención postventa y "¿dónde está mi pedido?" por WhatsApp para tiendas Tiendanube/Shopify LATAM
- **Qué es:** bot que responde estado de envío, cambios, talles, medios de pago con datos reales de la tienda.
- **Quién / señal:** "retail/e-commerce" es el primer rubro listado por las guías AR [vendedor]; Cliengo/Botmaker ya tienen integraciones e-commerce [vendedor].
- **Cobro:** USD 100-300/mes + setup.
- **Ejecución:** apps de la tienda de Tiendanube ya lo hacen; él implementa + ajusta. Integración de tracking de correos AR (Andreani, OCA, Correo Argentino) a veces requiere código.
- **Tipo:** semi-pasivo.
- **Capital / primer dólar:** bajo; 2-3 meses.
- **Cobro AR:** local.
- **Riesgos:** las apps nativas del marketplace de Tiendanube le comen el mercado a la agencia; queda el segmento medio que necesita personalización.
- **Score: 5/10.**

#### 16. Recuperación de carritos abandonados por WhatsApp con revenue share
- **Qué es:** mensaje de WhatsApp a quien abandonó el carrito (con opt-in) + cupón; cobra % de lo recuperado.
- **Quién / señal:** función estándar de BSPs (Wati, Kommo, Botmaker) [vendedor].
- **Cobro:** 5-10% de ventas recuperadas o USD 100-200/mes.
- **Ejecución:** apps existentes; él configura y mide.
- **Tipo:** casi pasivo.
- **Capital / primer dólar:** bajo; 1-2 meses.
- **Cobro AR:** local.
- **Riesgos:** requiere opt-in para mensajes de **marketing** (los más caros: ~USD 0,04-0,07/mensaje en AR/BR según Kommo y Develop Argentina) [vendedor]; las plataformas ya lo ofrecen nativo → la agencia sobra salvo en tiendas que no saben configurarlo.
- **Score: 4,5/10.**

#### 17. Implementador certificado Kommo (partner) para PyMEs que venden por WhatsApp
- **Qué es:** convertirse en partner oficial de Kommo (CRM conversacional para WhatsApp/Instagram, muy usado en LATAM) y vender implementación llave en mano: pipeline, Salesbot con IA, plantillas, capacitación. Gana **dos veces**: el fee de implementación + la comisión recurrente sobre las licencias.
- **Quién / señal:** Kommo declara **5.000+ partners** en su directorio (otra página dice 1.000+ en 60+ países — inconsistencia) [oficial]; partners LATAM activos como Planiva Group, Emarkets LLC (Gold), 9 Ideas [oficial-directorio]. Programa: **gratis**, **100% de la primera venta**, **35-50% de comisión vitalicia** (50% a partir de USD 10.000 vendidos), 100% de los servicios propios [oficial, 2026-10-01].
- **Cobro:** implementación básica USD 300-1.000 (PyME de 2-5 usuarios), compleja USD 1.500-4.000 [sin fuente propia: rango de partners LATAM]. Recurrente: si un cliente paga 5 usuarios × USD 25 = USD 125/mes → USD 44-62/mes de comisión vitalicia. 20 clientes ≈ USD 900-1.250/mes pasivos + retainers de soporte.
- **Ejecución:** Kommo es 100% no-code. Él hace la certificación (capacitación + quiz), Claude le arma los procesos comerciales por vertical, los Salesbots, las plantillas para que Meta las apruebe, manuales y videos-guion. Es el mismo trabajo de "relevar un proceso y ordenarlo" de su perfil de ingeniería industrial.
- **Tipo:** semi-pasivo (la comisión es genuinamente pasiva; la implementación es activa). 2-4 h/sem en régimen con 15-20 clientes.
- **Capital / primer dólar:** USD 0. 1-2 meses (el primer cliente paga 100% de la licencia como comisión).
- **Cobro AR:** clientes locales pagan la implementación en pesos/USD; las comisiones de Kommo hay que confirmar cómo las paga (Payoneer/transferencia internacional) — **verificar**.
- **Riesgos:** dependencia de una plataforma (si Kommo cambia el programa o sube precios, golpea); 5.000 partners compitiendo (pero la mayoría genéricos); churn de PyMEs AR en crisis; Kommo te asigna clientes existentes solo si sos bueno. Las reglas de Meta afectan a todo el ecosistema por igual.
- **Score: 7,5/10.** Mejor relación capital cero / recurrente / fit no-code del frente.

#### 18. Bot de WhatsApp para estudios contables: recolección de comprobantes + vencimientos
- **Qué es:** el bot le pide a cada cliente del estudio sus facturas/tickets del mes, los recibe por foto/PDF, los clasifica con IA en una planilla y manda recordatorios de vencimientos (monotributo, IIBB, ARCA).
- **Quién / señal:** hay decenas de gigs en Fiverr/Upwork de "AI invoice processing con n8n + OCR" (oferta saturada a nivel global) [oficial-marketplaces, 2026]; ángulo AR: ARCA y monotributo son específicos y la oferta local en español es menor [sin fuente propia]. "83% de las empresas procesa facturas a mano" circula sin fuente primaria — no usar.
- **Cobro:** setup USD 300-800 + USD 100-250/mes por estudio (un estudio con 100+ clientes ahorra horas de cadete).
- **Ejecución:** WhatsApp BSP + n8n/Make + Claude/Gemini para extraer datos de imágenes → Google Sheets. Claude puede escribir el workflow completo; él lo importa y prueba. Plantillas n8n públicas como base.
- **Tipo:** semi-pasivo; 1 h/sem/estudio.
- **Capital / primer dólar:** USD 20-50/mes (n8n Starter €20 + API). 1-3 meses.
- **Cobro AR:** local. Los contadores son prescriptores: un estudio te recomienda a otros.
- **Riesgos:** datos fiscales sensibles (Ley 25.326, secreto profesional); errores de extracción = errores impositivos → siempre con revisión humana. Los sistemas contables (Tango, Xubio, Colppy) agregan IA propia.
- **Score: 6,5/10.**

#### 19. WhatsApp para talleres, gomerías y service: turnos + aviso "tu auto está listo" + recordatorio de service
- **Qué es:** versión WhatsApp de la idea 6, con recordatorio automático de service a los 6 meses / X km (reactivación).
- **Quién / señal:** la reactivación de clientes pasados generó USD 40-80k en una campaña a 800 clientes en home services [vendedor, ScaleLogix 2026 — anecdótico].
- **Cobro:** USD 50-120/mes.
- **Ejecución:** planilla de órdenes + bot + Make.
- **Tipo:** semi-pasivo.
- **Capital / primer dólar:** bajo; 1-2 meses.
- **Cobro AR:** local.
- **Riesgos:** ticket bajo; el taller tiene que cargar los datos (problema de proceso).
- **Score: 5/10.**

#### 20. Reactivación de socios de gimnasios/estudios (Pilates, crossfit) por WhatsApp
- **Qué es:** campaña a ex socios y leads fríos con oferta de vuelta + seguimiento conversacional con IA + agenda de clase de prueba.
- **Quién / señal:** caso de cadena de Pilates con 47 leads fríos convertidos [gurú, Buldrr]; reactivación de bases dormidas recupera ~5-15% de una lista [vendedor, Ciela 2026-04-24].
- **Cobro:** por socio recuperado (USD 10-30 c/u en AR) o fee por campaña USD 150-400.
- **Ejecución:** Kommo/BSP + plantilla de marketing aprobada + Claude para segmentación y mensajes.
- **Tipo:** activo por campaña; 3-5 h por campaña.
- **Capital / primer dólar:** bajo; 2-6 semanas.
- **Cobro AR:** local.
- **Riesgos:** mensajes de marketing requieren opt-in y son los más caros; bases viejas sin consentimiento = bloqueo del número.
- **Score: 5,5/10.**

---

### BLOQUE C — Reactivación, outbound y generación de leads

#### 21. Reactivación de bases de leads por SMS con IA, cobrando por cita (EE.UU.)
- **Qué es:** el negocio "DBR" (database reactivation) que promocionan los cursos: tomar la base dormida de un negocio (hipotecas, solar, clínicas estéticas), mandar SMS conversacional con IA y cobrar por cada cita agendada.
- **Quién / señal:** "una de las ofertas más calientes de 2026 para negocios locales"; servicios reportan 15-25% de respuesta en leads de < 6 meses y 30-40% de esos agendan [vendedor, Xpand Digital]; caso: USD 600k en préstamos hipotecarios en 90 días [vendedor — anecdótico]. Ciela estima 5-15% de recuperación [vendedor/gurú, 2026-04-24].
- **Cobro:** "decenas a unos cientos de USD por cita", o build fee + % de cierres [gurú, Ciela].
- **Ejecución:** GoHighLevel (tiene "conversation AI" + SMS) + plantillas; Claude escribe los guiones. Él necesita registro A2P 10DLC del número en EE.UU. (requiere empresa/EIN o hacerlo bajo la cuenta del cliente).
- **Tipo:** activo por campaña.
- **Capital / primer dólar:** USD 100-300 (GHL + SMS). 1-3 meses si consigue el primer cliente.
- **Cobro AR:** exterior vía Payoneer.
- **Riesgos:** **TCPA + A2P 10DLC**: mandar SMS a bases sin consentimiento expreso documentado es la forma más rápida de recibir una demanda (la fuente gurú admite "no es asesoramiento legal" y no detalla requisitos [Ciela]). Saturadísimo por los cursos. Las agencias de este modelo dependen de que el cliente tenga una base grande y "limpia" — pocas la tienen.
- **Score: 4/10.**

#### 22. Reactivación de pacientes inactivos (odontología/estética) por WhatsApp en LATAM
- **Qué es:** la 21 adaptada a AR: pacientes que no vienen hace 12+ meses → recordatorio de control + turno en 2 clics.
- **Quién / señal:** misma lógica DBR; en salud el "recall" es práctica clínica normal (control semestral), lo que da base legítima de contacto [sin fuente propia].
- **Cobro:** por turno recuperado (USD 5-15 en AR) o por campaña USD 150-300.
- **Ejecución:** exportar planilla de pacientes + BSP + plantilla utility/marketing + bot de agenda (combinar con idea 10).
- **Tipo:** activo por campaña / semi-pasivo si queda como recall permanente.
- **Capital / primer dólar:** bajo; 2-6 semanas.
- **Cobro AR:** local.
- **Riesgos:** consentimiento y datos de salud (Ley 25.326); costo por mensaje de marketing.
- **Score: 6/10** (como upsell de la 10, muy bueno).

#### 23. Cold email con IA "llave en mano" para empresas B2B (agencia de lead gen)
- **Qué es:** montar dominios secundarios, calentar casillas, scrapear listas, personalizar con IA y entregar reuniones.
- **Quién / señal:** es el modelo de agencia más promocionado 2023-2026 (Instantly, Smartlead, Clay). No pude acceder al benchmark de Instantly (404); históricamente reportan reply rates de 1-5% [sin fuente propia en esta sesión].
- **Cobro:** USD 1.500-5.000/mes retainer o USD 150-500 por reunión.
- **Ejecución:** herramientas no-code (Instantly + Apollo/Clay); Claude escribe secuencias.
- **Tipo:** activo; 5-10 h/sem/cliente.
- **Capital / primer dólar:** USD 150-300/mes en herramientas + dominios. 2-4 meses.
- **Cobro AR:** exterior.
- **Riesgos:** desde 2024 Google/Yahoo exigen autenticación y < 0,3% de spam rate a remitentes masivos; entregabilidad en caída; mercado archi-saturado y con churn altísimo (el cliente se va si no hay reuniones en 60 días). GDPR si apunta a la UE.
- **Score: 3,5/10.**

#### 24. Seguimiento automático de presupuestos ("estimate follow-up") para servicios y PyMEs industriales
- **Qué es:** cada presupuesto enviado dispara una secuencia (mismo día, 48 h, 5 días, 10 días) por WhatsApp/email; las respuestas las clasifica la IA y avisa al vendedor.
- **Quién / señal:** mejora de cierre de 18-35% "sin trabajo extra" [vendedor, ScaleLogix en dev.to, 2026 — sin metodología].
- **Cobro:** setup USD 300-800 + USD 80-200/mes.
- **Ejecución:** planilla/CRM + Make/n8n + WhatsApp/Gmail; Claude arma todo. Muy apto para metalúrgicas, imprentas, proveedores industriales (sinergia con su red de ingeniería).
- **Tipo:** semi-pasivo.
- **Capital / primer dólar:** < USD 50. 1-2 meses.
- **Cobro AR:** local.
- **Riesgos:** si el vendedor no carga el presupuesto en la planilla, no hay automatización (de nuevo, proceso). Bajo riesgo legal (es comunicación con alguien que pidió presupuesto).
- **Score: 6,5/10.**

#### 25. Generador automático de reseñas en Google para comercios locales
- **Qué es:** tras la compra/servicio, mensaje con link directo a la reseña; respuestas a reseñas redactadas con IA para aprobación.
- **Quién / señal:** estudio de Pilates con 140 reseñas en 45 días [gurú, Buldrr]; agente de reseñas a USD 300-500/mes en EE.UU. [gurú].
- **Cobro:** en AR USD 30-80/mes por local.
- **Ejecución:** muy simple (Make + WhatsApp + planilla).
- **Tipo:** casi pasivo.
- **Capital / primer dólar:** ~USD 0. 2-4 semanas.
- **Cobro AR:** local.
- **Riesgos:** commodity; política de Google contra incentivos y gating; churn cuando el local "ya tiene suficientes".
- **Score: 4,5/10** (bueno como gancho de entrada barato).

#### 26. "Llamada perdida → WhatsApp automático" (missed-call text-back)
- **Qué es:** si nadie atiende el teléfono fijo/celular del negocio, sale automáticamente un WhatsApp "te vimos llamar, ¿en qué te ayudamos?" y el bot sigue.
- **Quién / señal:** función estrella de GoHighLevel y de agencias de home services; "un negocio que pierde 8 llamadas/día con trabajos de USD 400 pierde USD 3.200/día" [vendedor — cálculo teórico].
- **Cobro:** USD 50-150/mes.
- **Ejecución:** requiere telefonía con webhook (Twilio/GHL) → más técnico; Claude puede guiar.
- **Tipo:** pasivo una vez instalado.
- **Capital / primer dólar:** USD 50-100. 1-2 meses.
- **Cobro AR:** local/exterior.
- **Riesgos:** en AR muchas PyMEs ya usan WhatsApp como canal principal, no el teléfono → problema más chico. En EE.UU., SMS requiere A2P 10DLC.
- **Score: 4/10.**

---

### BLOQUE D — Back-office, documentos y reportes (donde pesa su perfil industrial)

#### 27. Extracción de facturas de proveedores → planilla/sistema (cuentas a pagar para PyMEs)
- **Qué es:** las facturas que llegan por mail/WhatsApp se leen con IA (proveedor, CUIT, fecha, ítems, IVA, total) y se cargan a Google Sheets o al sistema, con alerta de duplicados y vencimientos.
- **Quién / señal:** oferta muy presente en marketplaces: Fiverr y Upwork tienen múltiples gigs de "AI invoice processing con n8n + OCR" (2026) [oficial-marketplace]; Growwstacks publica workflows de n8n para cuentas a pagar [vendedor].
- **Cobro:** setup USD 300-1.500 + USD 80-250/mes (o por volumen de facturas).
- **Ejecución:** n8n (plantillas públicas) + Claude/Gemini visión + Sheets. Claude escribe y explica el workflow; él lo ajusta al formato de factura AR (A/B/C, CAE).
- **Tipo:** semi-pasivo; 1 h/sem/cliente.
- **Capital / primer dólar:** USD 20-50/mes. 1-3 meses.
- **Cobro AR:** local (o exterior en Upwork, con mucha competencia de India/Pakistán a USD 50-150 por gig).
- **Riesgos:** commoditización global; los ERP (Tango, Xubio) incorporan esto nativo. Errores = problemas fiscales → siempre "humano en el loop".
- **Score: 6/10.**

#### 28. Lectura de remitos/órdenes de compra para distribuidoras + conciliación con stock (sinergia "orden operativo")
- **Qué es:** IA que lee órdenes de compra (PDF, foto, WhatsApp de clientes) y remitos de proveedores, los pasa a planilla estructurada, los cruza con el stock y alerta faltantes/diferencias. Es el "brazo digital" de la consultora de orden operativo ya existente — **no la repite**, la productiza.
- **Quién / señal:** "AI document processing" es parte de las categorías IA de mayor crecimiento en Upwork ("AI integration" +178%, In-Demand Skills 2026) [oficial vía prensa]; Upwork reporta que "AI strategy & consulting" crece > 50% [PYMNTS 2026-08-10]. Sin un competidor AR identificado en esta sesión [sin fuente propia].
- **Cobro:** setup USD 500-1.500 + USD 150-300/mes, o como módulo de un engagement de orden operativo.
- **Ejecución:** n8n/Make + modelo con visión + Sheets/AppSheet. Claude diseña el modelo de datos (SKU, cantidad, lote) y él aporta el método de ingeniería industrial (ABC, conciliación, KPIs de exactitud de inventario).
- **Tipo:** semi-pasivo.
- **Capital / primer dólar:** < USD 100. 2-3 meses (más rápido si viene con la consultora).
- **Cobro AR:** local.
- **Riesgos:** cada distribuidora tiene formatos caóticos; si el maestro de artículos está sucio, la IA amplifica el caos (primero ordenar, después automatizar — justamente su pitch).
- **Score: 6,5/10.** Su mejor diferencial en todo el frente.

#### 29. Reportes automáticos semanales a WhatsApp/email (ventas, stock, cobranzas) para dueños de PyME
- **Qué es:** cada lunes el dueño recibe por WhatsApp un resumen en lenguaje natural ("vendiste 12% menos que la semana pasada; 3 productos A sin stock; 5 clientes deben más de 30 días") generado por IA desde sus planillas/sistema.
- **Quién / señal:** "Care & Feeding"/"Standard Ops" retainers de automatización USD 650-2.400/mes en mercados centrales; LATAM 35-55% de eso [blog, BetOnAI 2026-09-20]. Sin competidor AR identificado específico [sin fuente propia].
- **Cobro:** setup USD 200-600 + USD 50-150/mes.
- **Ejecución:** Google Sheets/Looker Studio + n8n + Claude API para el resumen; Claude arma todo. Exportar datos del sistema del cliente (Tango, Excel) puede ser lo más difícil.
- **Tipo:** **casi pasivo** una vez instalado (0,25-0,5 h/sem/cliente).
- **Capital / primer dólar:** < USD 50. 1-2 meses.
- **Cobro AR:** local.
- **Riesgos:** valor percibido bajo si el reporte no dispara decisiones; churn a los 3-6 meses si "ya me acostumbré". Mitigación: incluir alertas accionables, no solo resumen.
- **Score: 6,5/10.**

#### 30. Agente cotizador para fabricantes/talleres a medida (carpintería, metalúrgica, imprenta)
- **Qué es:** el cliente manda medidas/fotos por WhatsApp o formulario; la IA arma un presupuesto preliminar con la lista de precios del taller y lo pasa para aprobación.
- **Quién / señal:** caso UK de home services: tiempo de cotización de 48 h a 4 min [gurú, Buldrr]; precio de lista USD 10.000-15.000 en EE.UU. [gurú — inflado].
- **Cobro:** AR: setup USD 500-1.500 + USD 100-200/mes.
- **Ejecución:** planilla de costos + reglas + Claude para interpretar el pedido; complejo si hay muchas variantes. Necesita al ingeniero (él) para modelar costos.
- **Tipo:** semi-pasivo.
- **Capital / primer dólar:** bajo; 2-4 meses.
- **Cobro AR:** local.
- **Riesgos:** un error de precio = pérdida directa para el cliente → responsabilidad. Siempre aprobación humana.
- **Score: 5,5/10.**

#### 31. Respuestas con IA a preguntas de compradores en Mercado Libre (vendedores medianos)
- **Qué es:** configurar respuestas automáticas con IA y base de conocimiento por producto para vendedores con muchas publicaciones.
- **Quién / señal (en contra):** Real Trends (AR) ya ofrece "respuestas automáticas con AI" y declara **+25.000 empresas** clientes [vendedor, 2026-10-01]; Mercado Libre agrega herramientas nativas.
- **Cobro:** USD 50-150/mes como servicio — compite con un SaaS establecido.
- **Ejecución:** fácil, pero el SaaS lo hace mejor.
- **Tipo:** semi-pasivo.
- **Capital / primer dólar:** bajo.
- **Cobro AR:** local.
- **Riesgos:** commodity cubierto por SaaS + plataforma.
- **Score: 3/10** como servicio; ok como parte de un paquete e-commerce.

#### 32. Intake de clientes para estudios jurídicos (formularios + WhatsApp + resumen IA del caso)
- **Qué es:** el potencial cliente cuenta su caso por WhatsApp/formulario; la IA estructura hechos, fechas y documentos y el abogado recibe un resumen + checklist; agenda de consulta paga.
- **Quién / señal:** "law firms" aparecen en las listas de receptionist/intake [gurú, Buldrr]. Sin dato AR [sin fuente propia].
- **Cobro:** setup USD 300-800 + USD 80-200/mes.
- **Ejecución:** Typeform/Tally + Make + Claude; nada de código.
- **Tipo:** semi-pasivo.
- **Capital / primer dólar:** bajo; 2-3 meses.
- **Cobro AR:** local.
- **Riesgos:** el bot no puede dar consejo legal; secreto profesional; abogados conservadores.
- **Score: 5/10.**

#### 33. Agente de soporte nivel 1 (deflection) para e-commerce/SaaS mediano
- **Qué es:** agente IA sobre Zendesk/Gorgias/Intercom/web chat que resuelve 40-70% de tickets repetitivos con la base de conocimiento.
- **Quién / señal:** precio de proyecto "AI customer-support agent (Tier-1 deflection)" USD 5.500-15.000 en mercados centrales [blog, BetOnAI 2026-09-20]; Sierra USD 150M ARR, Decagon USD 35M ARR (abr-2026) → la categoría la están ganando plataformas grandes [analista, Sacra].
- **Cobro:** exterior USD 2.000-8.000 setup + retainer; AR USD 500-1.500 setup.
- **Ejecución:** las plataformas traen agente IA nativo (Intercom Fin, Zendesk AI); él configura base de conocimiento con Claude. Medio-difícil.
- **Tipo:** semi-pasivo.
- **Capital / primer dólar:** bajo; 3-6 meses.
- **Cobro AR:** ambos.
- **Riesgos:** la plataforma nativa elimina al intermediario; clientes medianos exigen experiencia demostrable.
- **Score: 4,5/10.**

#### 34. Chatbot web + WhatsApp con base de conocimiento para colegios, municipios y cooperativas
- **Qué es:** responde inscripciones, trámites, horarios, requisitos; deriva a humano.
- **Quién / señal:** colegios listados como vertical por partners Kommo (Emarkets) [oficial-directorio]. Sin cifras [sin fuente propia].
- **Cobro:** USD 100-400/mes; licitaciones públicas para municipios.
- **Ejecución:** fácil con plataformas; Claude arma la base de conocimiento.
- **Tipo:** semi-pasivo.
- **Capital / primer dólar:** bajo; **ciclo de venta lento** (3-9 meses en sector público).
- **Cobro AR:** local; el sector público paga tarde y en pesos.
- **Riesgos:** compras públicas, pagos atrasados, política.
- **Score: 4/10** (colegios privados: 5).

---

### BLOQUE E — Modelos de negocio / canales de venta

#### 35. Freelance "AI automation / implementation" en Upwork y Contra (clientes en USD)
- **Qué es:** perfil especializado (ej. "n8n + Claude automations for logistics/ops teams") para proyectos de USD 300-3.000.
- **Quién / señal:** Upwork In-Demand Skills 2026: habilidades IA **+109%** interanual, "AI integration" **+178%** [oficial vía prensa]; pero el GSV de trabajo IA de Upwork crece **+22%** (desaceleró desde +50%) y los clientes activos cayeron **-4% a 763k** (Q2-2026, publicado 2026-08-10) [prensa sobre earnings]. Cita del CEO Hayden Brown: el cuello de botella es "access to people who understand how to apply it". La cifra "+340% de 'AI automation specialist'" que circula no tiene fuente primaria verificada — no usar.
- **Cobro:** principiante USD 45-90/h en tabla central; LATAM entrega a 35-55% de eso salvo que se posicione en USD [blog, BetOnAI]. Upwork cobra 10% de comisión (aprox., verificar) + Connects para postular.
- **Ejecución:** Claude hace el trabajo técnico (workflows n8n/Make importables, prompts, documentación); él gestiona al cliente, prueba y entrega. **Riesgo real: no saber programar se nota cuando algo falla en producción** — compensar eligiendo proyectos no-code (Make, Zapier, Airtable, GHL) y con buena documentación.
- **Tipo:** activo; 10-20 h/sem.
- **Capital / primer dólar:** USD 20-50 (Connects). 1-3 meses para el primer contrato (el perfil sin reseñas es la gran barrera).
- **Cobro AR:** **bueno**: Upwork paga a Payoneer o transferencia; desde sept-2025 el BCRA prohibió comisiones bancarias sobre cobros de exportación de servicios (dato del informe 2026-09-02 de este repo).
- **Riesgos:** competencia global de India/Pakistán/Europa del Este a precios bajos; los primeros proyectos se cobran casi gratis para conseguir reseñas; no es pasivo.
- **Score: 6/10.** Útil como canal de cash en USD y laboratorio para encontrar el nicho.

#### 36. Retainer "Care & Feeding" de automatizaciones (mantenimiento mensual)
- **Qué es:** después de cada proyecto, un abono mensual por monitorear, corregir y hacer 1 mejora chica/mes.
- **Quién / señal:** retainer de mantenimiento USD 650-1.200/mes en mercados centrales; "AI-Agent Integration" es la categoría de retainer de mayor crecimiento en 2026 [blog, BetOnAI 2026-09-20]. Layer3 (2026-09-02): la falla más común de las agencias es **no mantener la relación post-lanzamiento**, no la técnica [blog].
- **Cobro:** AR USD 50-200/mes; exterior USD 300-1.000/mes.
- **Ejecución:** n8n tiene alertas de error; Claude diagnostica; él responde.
- **Tipo:** semi-pasivo (alert-driven — encaja con su regla de oro).
- **Capital / primer dólar:** 0; depende de tener proyectos previos.
- **Cobro AR:** ambos.
- **Riesgos:** si algo se rompe y él no sabe arreglarlo sin Claude, depende de Claude para un SLA. Pocos clientes al principio.
- **Score: 7/10 como modelo** (no como idea independiente: se suma a 10, 12, 17, 18, 28, 29).

#### 37. GoHighLevel en "SaaS mode": CRM vertical con marca propia (ej. "CRM para centros de estética LATAM")
- **Qué es:** pagar GHL Agency Pro (USD 497/mes) y revender sub-cuentas con marca propia + snapshot vertical a USD 97-297/mes por cliente.
- **Quién / señal:** GHL es "el white-label SaaS más popular para agencias en 2026" [blog, dmchamp]; precios estables en 2026 [blog, ecosire]. Sin dato público de cuántas agencias usan SaaS mode.
- **Cobro:** USD 97-297/mes por cliente; costo GHL USD 297-497/mes + AI Employee USD 50-97/sub-cuenta + WhatsApp USD 10/sub-cuenta [oficial].
- **Ejecución:** no-code pero con curva de aprendizaje grande; interfaz en inglés (traducción parcial).
- **Tipo:** semi-pasivo si escala; necesita 5+ clientes para cubrir el costo fijo.
- **Capital / primer dólar:** USD 297-497/mes desde el día 1 → quema el presupuesto en 1-3 meses. 3-6 meses al break-even.
- **Cobro AR:** cobrar USD 97+/mes a PyMEs argentinas es difícil; Kommo/Leadsales ya ocupan ese lugar en LATAM con precio y soporte en español.
- **Riesgos:** **el ecosistema GHL es el epicentro del marketing de gurús** (programas de afiliados de 40% recurrente que incentivan a recomendarlo); costo fijo alto; dependencia total.
- **Score: 3,5/10.**

#### 38. Fulfillment white-label para agencias de marketing (él construye, la agencia vende)
- **Qué es:** agencias de marketing/publicidad (AR, España, EE.UU.) que ya tienen clientes pero no saben automatizar le subcontratan los bots/automatizaciones.
- **Quién / señal:** modelo extendido en el ecosistema GHL/Kommo; Kommo deja a partners trabajar con clientes de otros [oficial]. Sin dato cuantitativo [sin fuente propia].
- **Cobro:** 40-60% de lo que cobra la agencia; USD 200-1.000 por proyecto.
- **Ejecución:** idéntica a las ideas de WhatsApp; él no vende al cliente final (sin el problema de venta en frío).
- **Tipo:** activo por proyecto.
- **Capital / primer dólar:** 0. 1-2 meses (pocas reuniones con dueños de agencias).
- **Cobro AR:** ambos.
- **Riesgos:** depende de 1-3 agencias; no construye marca propia; la agencia puede internalizar.
- **Score: 6/10** — **muy buen canal de arranque** para alguien que no quiere hacer venta en frío.

#### 39. Workshops in-company "IA aplicada para tu equipo" (Claude/ChatGPT/Gemini para PyMEs)
- **Qué es:** capacitación de 4-8 h para equipos administrativos/comerciales: casos de uso, prompts, armado de 2-3 automatizaciones simples en vivo.
- **Quién / señal:** "AI workshops" de USD 5.000-100.000+ en enterprise [gurú, Buldrr — inflado]; Upwork reporta que "AI strategy & consulting" crece > 50% [PYMNTS 2026-08-10].
- **Cobro:** AR USD 300-1.500 por workshop.
- **Ejecución:** Claude arma el material, ejercicios y casos por rubro; él da el workshop (habilidad de presentación).
- **Tipo:** activo; 8-15 h por workshop (prep + dictado).
- **Capital / primer dólar:** 0. 1-2 meses (cámaras empresarias, colegios profesionales).
- **Cobro AR:** local; factura C.
- **Riesgos:** sin credenciales es difícil vender a empresas medianas; mucha competencia de "influencers de IA". **Es el mejor generador de leads** para las demás ideas (cada workshop = 1-2 proyectos de automatización).
- **Score: 5,5/10** (como embudo, 7).

#### 40. Paquete vertical productizado: "WhatsApp + turnos + recordatorios + reseñas" por precio fijo para un rubro
- **Qué es:** en vez de servicio a medida, un paquete cerrado (ej. "Kit Consultorio": bot de turnos + recordatorios + reactivación semestral + reseñas) a precio fijo de instalación + abono. Es la forma de pasar de activo a semi-pasivo.
- **Quién / señal:** Layer3 (2026-09-02): los que sobreviven son nichos específicos ("automatizar intake para consultorios dentales"), no pitches genéricos [blog]; el tier especializado "no está saturado" [vendedor, Ciela].
- **Cobro:** USD 300-600 instalación + USD 80-150/mes.
- **Ejecución:** el primer cliente se hace a mano; Claude documenta todo como plantilla replicable (snapshot Kommo / workflows n8n exportables); los siguientes se instalan en 3-5 h.
- **Tipo:** semi-pasivo; 0,5-1 h/sem/cliente.
- **Capital / primer dólar:** USD 0-100. 2-3 meses.
- **Cobro AR:** local; escalable a México/Colombia (93-94% penetración WhatsApp [encuesta 2025]) con cobro vía Payoneer.
- **Riesgos:** elegir mal el rubro; los SaaS verticales (Cliengo/XIAgenda para salud) compiten. Ventaja: precio fijo = venta más fácil.
- **Score: 7/10** (es la forma correcta de ejecutar las ideas 10, 12, 17, 22).

#### 41. Asistente de tracking/consultas de envíos por WhatsApp para operadores logísticos y transportes chicos
- **Qué es:** el cliente final pregunta "¿dónde está mi envío?" y el bot responde desde la planilla/sistema del transporte; avisos automáticos de entrega/demora.
- **Quién / señal:** sinergia directa con su experiencia en logística; sin dato de mercado específico [sin fuente propia].
- **Cobro:** USD 100-300/mes.
- **Ejecución:** requiere que el transporte tenga los datos de estado en algún formato (planilla, sistema con exportación). BSP + n8n.
- **Tipo:** semi-pasivo.
- **Capital / primer dólar:** bajo; 2-4 meses.
- **Cobro AR:** local.
- **Riesgos:** los transportes chicos no registran estados; volver a problema de proceso (que él sabe resolver, pero alarga la venta).
- **Score: 5,5/10.**

#### 42. Afiliados/reseller de herramientas de automatización (n8n, Make, Kommo, GHL) como capa sobre los servicios
- **Qué es:** no un negocio solo, sino cobrar la comisión de las herramientas que ya instala.
- **Quién / señal:** Kommo 35-50% vitalicio [oficial]; n8n afiliados 30% el primer año (informe 2026-09-02 del repo) [oficial]; GHL ~40% recurrente [sin fuente propia en esta sesión].
- **Cobro:** 30-50% de licencias.
- **Ejecución:** links de afiliado/portal partner en cada implementación (con transparencia al cliente).
- **Tipo:** pasivo.
- **Capital / primer dólar:** 0; depende de clientes.
- **Cobro AR:** verificar cada programa (Payoneer/PayPal).
- **Riesgos:** conflicto de interés propio (recomendar la herramienta que paga más, no la mejor) → declararlo. "Afiliados desde cero" ya está descartado en el proyecto; esto es distinto porque va atado a clientes reales.
- **Score: 6/10 como capa**, no como idea independiente.

---

## 3. Top 5 de este frente (para ESTE usuario)

| # | Idea | Por qué | Score |
|---|---|---|---|
| 1 | **Partner Kommo + paquete WhatsApp vertical** (17 + 40) | Capital USD 0, 100% no-code, comisión vitalicia 35-50% + fee de implementación; demanda LATAM real (WhatsApp 90% en AR); su skill de relevar procesos es el producto. | 7,5 |
| 2 | **Cobranzas por WhatsApp + link Mercado Pago** (12) | ROI medible en pesos recuperados (se vende solo), modelo % de lo recuperado, encaja en lo que Meta sí permite (utility), sin competencia SaaS dominante identificada. | 7 |
| 3 | **Turnos + recordatorios + reactivación para consultorios** (10 + 22) | Dolor universal (ausentismo, secretaria saturada), recurrente, paquete replicable; ojo con datos sensibles de salud. | 7 |
| 4 | **Documentos → planilla para estudios contables** (18 + 27) | Contadores = prescriptores; ARCA/monotributo es nicho local en español; n8n + Claude lo resuelven sin programar. | 6,5 |
| 5 | **Reportes automáticos + lectura de remitos para distribuidoras** (28 + 29) | Única idea donde su ingeniería industrial es diferencial real; convierte la consultora de "orden operativo" en abono mensual casi pasivo. | 6,5 |

**Canales de arranque recomendados (no son ideas, son cómo vender):** fulfillment white-label para agencias de marketing (38) y workshops (39) como embudo; Upwork (35) solo como cash en USD + laboratorio. **Modelo de ingresos transversal:** retainer de mantenimiento alert-driven (36) + comisiones de herramientas (42).

**Secuencia sugerida (a validar en `ideas/`):** 1) certificarse en Kommo y armar 1 paquete vertical con 1 cliente piloto a precio reducido a cambio de caso de estudio con números antes/después; 2) sumar cobranzas como módulo; 3) replicar en el mismo rubro; 4) recién con 5+ clientes, evaluar México/Colombia.

---

## 4. Trampas comunes del frente

1. **El "AAA" es un producto de los gurús, no solo un negocio.** El grueso del contenido (YouTube, Skool, "AI Automation Agency" de 2023-2026) lo producen quienes venden cursos, comunidades, plantillas o plataformas con afiliados (GHL paga comisión recurrente a quien lo recomienda). Layer3 (2026-09-02) lo compara con el dropshipping: el curso gana aunque el alumno nunca consiga un cliente. **No hay estadística primaria de mediana de ingresos**; los "USD 10k/mes" son survivorship.
2. **Vender es el 80% del trabajo, no construir.** Con Claude cualquiera arma un bot en una tarde; por eso el valor no está en la tecnología. Cierre demo → venta ~25% [vendedor, Ciela], y llegar a la demo es lo difícil. Un argentino sin red que vende en frío a EE.UU. compite con miles de agencias con presencia local.
3. **Voz IA outbound en EE.UU. = mina legal.** FCC 24-17 (2024-02-08): voz IA = voz artificial bajo la TCPA → consentimiento previo expreso, sin excepción para "equivalente a humano"; SMS además requiere registro A2P 10DLC. Las demandas colectivas TCPA son una industria. Inbound (atender) es seguro; outbound (llamar/mensajear bases frías) no.
4. **Meta cambia las reglas de WhatsApp cada trimestre.** Prohibición de chatbots de propósito general (2026-01-15), cobro de mensajes de servicio > 1.000/mes y de utility dentro de la ventana (2026-10-01, según BSP — la página oficial todavía dice lo contrario: verificar), cobro de respuestas del Meta Business Agent (2026-08-01). **Nunca cotizar abonos con costo de Meta incluido fijo**: trasladar el costo de mensajes al cliente o poner tope.
5. **Usar números no oficiales es la forma más rápida de perder al cliente.** Bots sobre WhatsApp Web/no oficiales (librerías tipo "whatsapp-web.js") se baratean pero Meta banea el número; para un negocio el número es su canal de ventas. Solo API oficial vía BSP.
6. **El SaaS vertical te come el margen.** Restaurantes (Loman USD 199), Mercado Libre (Real Trends 25.000+ empresas), salud (Cliengo, XIAgenda), e-commerce (apps de Tiendanube): si existe un SaaS de USD 50-200/mes que resuelve el problema, la agencia solo vive de la implementación y del acompañamiento — cobrar eso explícitamente.
7. **Dependencia de proveedor.** Synthflow pasó de favorito de las agencias a "Enterprise desde USD 30.000/año"; GHL, Kommo, Vapi pueden cambiar precios o programas. Diversificar herramientas y que el cliente sea dueño de sus cuentas.
8. **Costo por minuto ≠ costo real.** Vapi anuncia USD 0,05/min pero el all-in es USD 0,10-0,30 (LLM, STT, TTS, telefonía aparte). Cotizar abonos de voz con margen y tope de minutos.
9. **Datos personales (Ley 25.326, Argentina).** Las bases de datos de clientes de tus clientes requieren registro ante la AAIP; datos de salud son sensibles; mandar datos a APIs en EE.UU. es transferencia internacional (cláusulas modelo de la AAIP). La ley está en proceso de reforma [oficial AAIP]. Grabación de llamadas: avisar al inicio ("esta llamada puede ser grabada") — en EE.UU. varios estados exigen consentimiento de todas las partes.
10. **Churn por "ya funciona solo".** El cliente PyME cancela el abono cuando la automatización anda bien y no ve trabajo. Antídoto: reporte mensual de valor (turnos confirmados, pesos cobrados, horas ahorradas) generado automáticamente.
11. **No saber programar se paga en producción, no en la demo.** Claude construye; pero cuando un webhook se rompe un sábado, él tiene que diagnosticar. Elegir plataformas no-code maduras (Kommo, Make, n8n Cloud) antes que self-hosting, y vender SLA realistas (respuesta en 24 h hábiles, no 2 h).
12. **Estadísticas fantasma.** Circulan cifras sin fuente primaria ("+340% AI automation specialist en Upwork", "83% procesa facturas a mano", "21x más conversión en 5 minutos"): no usarlas en propuestas comerciales sin verificar.

---

## 5. Fuentes (consultadas 2026-10-01 salvo indicación)

- Meta — WhatsApp Business Platform pricing [oficial]: https://developers.facebook.com/docs/whatsapp/pricing/
- YCloud — cambios de precio WhatsApp 2026-08-01 y 2026-10-01 [vendedor-BSP]: https://www.ycloud.com/blog/whatsapp-api-message-pricing-update-effective-october-1-2026
- respond.io — política de chatbots WhatsApp 2026 [vendedor]: https://respond.io/blog/whatsapp-chatbot-policy-2026
- HubSpot ES — Agentes IA en LATAM (2026-05-21; cita We Are Social/Meltwater 2025) [blog]: https://blog.hubspot.es/service/agentes-ia-latam
- Develop Argentina — costos chatbot WhatsApp AR (2026-06-25) [vendedor]: https://developargentina.com/blog/chatbot-whatsapp-argentina-implementar-empresa-2026
- Kommo — programa de partners [oficial]: https://www.kommo.com/partners/become-partner/ · directorio: https://www.kommo.com/partners/ · Planiva: https://www.kommo.com/partners/planiva-group/ · Emarkets: https://www.kommo.com/partners/emarkets-llc/
- Leadsales — precios [oficial]: https://leadsales.io/precios/
- Wati AR — turnos clínicos [vendedor]: https://www.wati.io/geo-argentina-es/automatiza-los-turnos-clinicos-por-whatsapp-sin-perder-el-cont
- Cliengo — guía WhatsApp para clínicas [vendedor]: https://guiawabusiness.cliengo.com/whatsapp-para-clinicas
- Real Trends [vendedor]: https://www.real-trends.com/ar/
- Sacra — Retell AI USD 60M ARR (abr-2026) [analista]: https://sacra.com/research/retell-ai-60m-yr-up-650-yoy
- Ainora — costo por minuto voz IA 2026 [blog]: https://ainora.lt/blog/ai-voice-agent-cost-per-minute-2026
- Vapi pricing real [blog]: https://zeeg.me/en/blog/post/vapi-ai-pricing
- ElevenLabs Agents pricing [oficial]: https://elevenlabs.io/pricing/agents
- Synthflow pricing [oficial]: https://synthflow.ai/pricing
- GoHighLevel pricing [oficial]: https://www.gohighlevel.com/pricing · SaaS mode [blog]: https://www.webdew.com/blog/gohighlevel-saas-mode
- n8n pricing [oficial]: https://n8n.io/pricing/
- Ciela — precios recepcionista IA (2026-01-08), por qué fallan las agencias (2025-12-03), estadísticas (2025-11-15), DBR (2026-04-24) [gurú/vendedor]: https://ciela.ai/blogs/how-much-to-charge-for-ai-voice-agent · https://ciela.ai/blogs/why-ai-automation-agencies-fail-data · https://ciela.ai/blogs/ai-automation-agency-statistics-2026 · https://ciela.ai/blogs/database-reactivation-ai-offer-for-agencies
- Layer3 Labs — ¿vale la pena una AI automation agency? (2026-09-02) [blog]: https://www.layer3labs.io/guides/is-an-ai-automation-agency-worth-it
- BetOnAI — rate card 2026, 54 operadores (act. 2026-09-20) [blog, baja trazabilidad]: https://betonai.net/ai-automation-rate-card-2026-what-to-charge-for-n8n-make-and-zapier-builds-real-rates-from-54-operators/
- Buldrr — 7 agentes IA y precios [gurú]: https://buldrr.com/7-ai-agents-businesses-are-paying-for-in-2026/
- PYMNTS — Upwork Q2-2026 (2026-08-10) [prensa]: https://pymnts.com/earnings/2026/upwork-navigates-cross-currents-as-ai-reshapes-freelance-demand
- Upwork In-Demand Skills 2026 [oficial; no abrió por timeout, cifras vía prensa]: https://investors.upwork.com/news-releases/news-release-details/upworks-demand-skills-2026-demand-top-ai-skills-more-doubles-ai · https://www.selfemployed.com/news/ai-freelance-skills-demand-2026/
- Fieldproxy — informe servicios residenciales 2026 (2026-03-12) [vendedor]: https://www.fieldproxy.ai/resources/blog/residential-service-industry-report-2026-ai-agents
- ScaleLogix (dev.to) — IA en home services 2026 [vendedor]: https://dev.to/scalelogix_ai/ai-for-home-service-businesses-whats-actually-working-in-2026-hvac-plumbing-roofing-d9l
- Xpand Digital — DBR [vendedor]: https://xpanddigital.io/topics/database-reactivation
- Loman vs Slang (2026-08) [vendedor]: https://loman.ai/blog/loman-vs-slang-ai-restaurant-phone-ordering
- FCC — AI voices bajo TCPA (FCC 24-17, 2024-02-08) [oficial vía resumen]: https://regulations.ai/regulations/RAI-US-NA-FCCAITC-2024 · https://www.mondaq.com/unitedstates/telecoms-mobile-cable-communications/1428382/fcc-declares-ai-generated-robocalls-unlawful
- AAIP — Datos personales (Ley 25.326) [oficial]: https://www.argentina.gob.ar/aaip/datospersonales
- Fiverr/Upwork — gigs de invoice processing n8n [oficial-marketplace]: https://www.upwork.com/services/product/development-it-ai-invoice-processing-automation-pdf-image-ocr-to-sheets-n8n-2027937010899955596
