# 230 ideas para generar ingresos con Claude: síntesis y ranking

**Fecha:** 2026-10-01
**Pedido:** investigación profunda de ideas que se estén haciendo hoy en el mundo, que estén arrancando o en auge, que se puedan vender y publicitar y que el usuario pueda ejecutar de verdad con Claude. Incluye cursos, sistemas, automatizaciones (llamadas, mensajes) e ingeniería industrial (cuellos de botella, etc.).
**Dato nuevo que cambia el filtro:** el usuario **no sabe programar** (aclarado 2026-10-01). Todo el ranking asume que Claude hace lo técnico y que el usuario no puede auditar código en producción.

---

## 0. Método y limitaciones

- **6 frentes investigados en paralelo** por agentes independientes, cada uno con su informe crudo en `research/fuentes/`:

| Frente | Ideas | Informe |
|---|---|---|
| A. Cursos, educación e infoproductos | 40 | [cursos-educacion](fuentes/2026-10-01-ideas-cursos-educacion.md) |
| B. Agencia de automatización (voz, WhatsApp, CRM) | 42 | [agencia-automatizacion](fuentes/2026-10-01-ideas-agencia-automatizacion.md) |
| C. Ingeniería industrial y operaciones | 34 | [ingenieria-industrial-ops](fuentes/2026-10-01-ideas-ingenieria-industrial-ops.md) |
| D. Software sin programar | 38 | [software-sin-programar](fuentes/2026-10-01-ideas-software-sin-programar.md) |
| E. Contenido, marketing y e-commerce | 38 | [contenido-ecommerce](fuentes/2026-10-01-ideas-contenido-ecommerce.md) |
| F. Olas emergentes y verticales de nicho | 38 | [olas-emergentes-verticales](fuentes/2026-10-01-ideas-olas-emergentes-verticales.md) |
| **Total** | **230 fichas** | ≈ **205 ideas distintas** (hay ~25 que se repiten entre frentes con otro ángulo; ver §5) |

- Cada ficha tiene: qué es, ejemplo real con link, señal de auge con fecha y fuente, precio, cómo hacerlo con Claude sin programar, tipo, horas/semana, capital, tiempo al primer dólar, cobro desde Argentina, riesgos y score de 1 a 10. **El detalle y las fuentes están en los informes crudos.** Este documento es el mapa.
- **~190 búsquedas web y ~85 lecturas directas de páginas.** Se agotó la cuota de 200 búsquedas de la sesión, así que algunas fichas quedaron marcadas `[sin fuente propia]` o `[NO VERIFICADO]`. Los pendientes concretos están en §7.
- **El score es para ESTE usuario**, no para el mercado en general: argentino, no programa, formación en ingeniería industrial (caso Sporting), menos de USD 1.000 de capital, Higgsfield, Cloudflare, GitHub y Gmail conectados.

---

## 1. La conclusión en 30 segundos

**Cuatro de los seis frentes, investigados por separado, llegaron a la misma conclusión:** tu ventaja real no es "la IA" (la tiene todo el mundo). Es la combinación de **método de ingeniería industrial + Claude + herramientas no-code**, vendida a PyMEs que tienen procesos desordenados. Eso hoy no se consigue en español a buen precio.

Las **olas reales** que encontramos (con fecha y fuente, no hype):

1. **Adopción de Claude/Cowork en equipos no técnicos.** Anthropic lanzó Claude for Small Business (2026-05-13), su Partner Network (2026-03) y Claude for Excel en beta (2026-05). Las empresas compran la herramienta y no saben implementarla. En Fiverr, la demanda de "Claude Code" subió +938% (dato de la plataforma). Es el único trabajo nuevo donde **no programar no es desventaja**.
2. **WhatsApp como canal de negocio en LATAM.** Partners de Kommo con comisión vitalicia del 35-50%, cobranzas y turnos por WhatsApp. Ojo: **los precios de Meta por mensaje cambian justo hoy, 2026-10-01**, y hay fuentes que se contradicen (§7).
3. **PyMEs argentinas con márgenes aplastados.** La industria está en contracción: índice de desempeño industrial de la UIA en 36,5 en enero 2026 (expansión = 50) y capacidad usada de 58-59% en mayo-junio 2026. Gastronomía con márgenes de 5-10% (antes 20-25%). **No se vende "más productividad", se vende "menos stock parado, menos merma, menos costo".**
4. **Mercado Libre como ecosistema:** 2,7 M de vendedores en AR y el 49% depende de ML (iProfesional 2026-06-27). Programa de afiliados de ML en AR desde 2026-03-11 (hasta 15%, cobro por Mercado Pago). YouTube Shopping AR desde 2026-07.
5. **Creatividades en volumen para anuncios.** El algoritmo de anuncios de Meta (Andromeda) premia la cantidad y variedad de piezas, y Higgsfield ya está pago.

**Sobre "ganar mucho", con honestidad:** ninguna de las 230 ideas da plata grande rápido para alguien sin audiencia, sin portfolio y sin programar. Las que llegan antes al primer dólar son **servicios**. Lo pasivo (cursos, plantillas, skills) **funciona después** de tener 3-5 casos reales que mostrar. Los informes marcan como trampa a las fuentes que dicen lo contrario: casi siempre venden un curso.

---

## 2. Top 15 consolidado (deduplicado entre frentes)

| # | Idea (combinada) | Frentes | Tipo | Score | Primer dólar | Por qué |
|---|---|---|---|---|---|---|
| 1 | **Implementador de Claude/IA para equipos no técnicos de PyMEs** (diagnóstico → setup de Claude/Cowork + Skills a medida → capacitación → abono) | F4, F5, F15, D3, A22 | Activo → semi | **8** | 3-6 sem | Ola nueva creada por Anthropic, no requiere programar y tu método de relevar procesos es el producto |
| 2 | **Orden Operativo productizado** (Diagnóstico Express a precio fijo → Stock Sano ABC/reorden → SOPs → mantenimiento mensual) | C1, C2, C3, C22, D1, D5 | Activo → semi | **8** | 4-8 sem | Única ventaja diferencial real (caso Sporting); se hace con Claude en Excel/Sheets + AppSheet y los datos quedan en la cuenta del cliente |
| 3 | **Ops para vendedores de Mercado Libre** (stock, Full/Flex, picking, fichas) | C4, E6, D20 | Activo → semi | 7,5 | 4-8 sem | La base de clientes más grande y accesible del país; se vende remoto con un export de ventas/stock |
| 4 | **Partner Kommo + paquete WhatsApp vertical a precio fijo** | B17, B40, B42 | Semi | 7,5 | 4-8 sem | Capital 0, no-code, fee de implementación + comisión recurrente oficial |
| 5 | **IA aplicada a logística/depósitos: curso + toolkit en español** | A8, A25, A9 | Semi → pasivo | 7,5* | 2-4 meses | En inglés cuesta USD 750-1.500 y en español casi no hay. *Recién después de tener casos (si no, es "curso sin credibilidad") |
| 6 | **Talleres de IA in-company para PyMEs (AR)** | A1, B39 | Activo | 7 | 2-4 sem | Cash más rápido con ticket decente: 46% de las PyMEs exige IA y solo 11% capacita formalmente (Trendsity/Deel 2026); funciona como embudo para #1 y #2 |
| 7 | **IA + automatización para estudios contables (ARCA/monotributo)** | F17, B18, B27, A2 | Activo + semi | 7 | 4-8 sem | Dolor documentado (311 h/año de cumplimiento fiscal) y los contadores recomiendan entre colegas. Ventana de 12-24 meses antes de que el software contable lo integre |
| 8 | **Cobranzas por WhatsApp + link de Mercado Pago** (cobro por % de lo recuperado) | B12 | Semi | 7 | 3-6 sem | El ROI se mide en pesos recuperados, así que se vende solo |
| 9 | **Turnos, recordatorios y recall de pacientes para consultorios** | B10, B22 | Semi | 7 | 4-6 sem | Dolor universal y recurrente; cuidado con los datos de salud (ley 25.326) |
| 10 | **Costeo de recetas + mermas para gastronomía** | C10, F29 | Activo → semi | 7 | 3-6 sem | Dolor agudo y fechado (cierres en Rosario, 2026-07-28); el mantenimiento mensual es casi mecánico |
| 11 | **Estudio de creatividades IA para e-commerce** (fotos/fichas → packs de anuncios → suscripción) | E1, E3, E4, E5 | Activo → semi | 7,5 | 2-4 sem | Higgsfield ya pago, 65.000 tiendas Tiendanube en AR y cobro en pesos. Es el que menos usa tu ingeniería |
| 12 | **Radar de licitaciones + resumen de pliegos con IA** (+ subsidios) | F19, F33 | Semi | 7 | 2-3 meses | Demanda estructural; sinergia con el proyecto stack-de-datos. ⚠ Requiere scraping (Claude lo hace, pero hay que mantenerlo) |
| 13 | **Implementación IA en español para PyMEs hispanas de EE.UU.** | F34, B2 | Activo → semi | 7 | 2-3 meses | Mismo servicio que #1 cobrado en USD, con ventaja de idioma y horario. Lo difícil es conseguir clientes desde AR |
| 14 | **Evaluador de modelos de IA en español** (Mercor/Micro1/Turing) | F1 | Activo (empleo) | 7 | 2-6 sem | **Puente de caja** en USD 25-60/h sin capital (929 ofertas listadas para AR al 2026-10-01). No es un negocio |
| 15 | **Afiliados ML + YouTube Shopping AR con reseñas en video** | E24, E25 | Semi-pasivo | 7 | 2-4 meses | Única idea que reabre un descarte con evidencia nueva: cobro en pesos y se fusiona con el canal long-form en cartera. Exige monotributo y YPP |

**Notas:**
- Las ideas 1, 2, 3, 7, 9 y 10 son **el mismo servicio** (método de procesos + IA no-code) **vendido a rubros distintos**. Conviene elegir **un rubro de entrada**, no seis.
- Las ideas 4, 8 y 9 son **el mismo stack técnico** (WhatsApp + Kommo/n8n).

---

## 3. Los 4 "sistemas" (230 ideas → 4 negocios posibles)

Mirando las 230 ideas juntas, casi todas las buenas caben en 4 sistemas. Cada uno tiene una **puerta de entrada** (barata, rápida), un **núcleo** (servicio que paga) y una **capa semi-pasiva** que se construye después.

### Sistema A: "Orden Operativo + IA" (ingeniería industrial productizada) — el más tuyo
- **Entrada:** Diagnóstico Express a precio fijo (C1), plantilla o calculadora gratis como imán (D38, C32), taller in-company (A1).
- **Núcleo:** Stock Sano (C2), re-slotting (C3), SOPs con IA (C22), costeo y mermas (C10/C9), digitalización con AppSheet (C23).
- **Abono:** reposición mensual + tablero KPI (D4) + auditoría 5S por fotos (C19) + reportes automáticos por WhatsApp (B29).
- **Capa semi-pasiva (después de 3-5 casos):** toolkit (A25), curso de logística con IA en español (A8), pack de Skills de operaciones (A22), curso "Claude en Excel para operaciones" (C33).
- **Verticales de venta:** vendedores de ML (remoto) y gastronomía o distribuidoras (local).

### Sistema B: "Implementador de Claude para PyMEs" — la ola más nueva
- **Entrada:** taller (A1), diagnóstico "IA-ready" (F15), kit de política de uso de IA (F7).
- **Núcleo:** setup de Claude/Cowork + Skills a medida por equipo (F4, F5, D3), herramientas internas sobre stack gestionado (D2).
- **Abono:** responsable de IA fraccional (F6) + mantenimiento alert-driven (B36).
- **Capa semi-pasiva:** cohortes de Cowork en español (A17/F38), Skills empaquetadas por oficio (A22).
- **Mercados:** PyMEs de AR → estudios contables (F17) → PyMEs hispanas de EE.UU. (F34, en USD).

### Sistema C: "WhatsApp vertical" — automatización de mensajes
- **Entrada:** partner Kommo (B17) con paquete a precio fijo (B40).
- **Núcleo por rubro:** cobranzas (B12), consultorios (B10+B22), contadores (B18), inmobiliarias (B11), seguimiento de presupuestos (B24).
- **Abono:** retainer de mantenimiento (B36) + comisiones de la herramienta (B42).
- **Llamadas con IA (voz):** según la investigación, **en AR el canal es WhatsApp, no la voz** (nadie atiende números desconocidos). La voz solo tiene sentido para EE.UU./España (B1, B2), con riesgo legal TCPA y mucha saturación. Se deja para más adelante.

### Sistema D: "Estudio de producción IA" — contenido con Higgsfield
- **Entrada:** fotos/fichas de producto (E5), videos para eventos (E37).
- **Núcleo:** packs de creatividades para anuncios de Meta/TikTok (E1), UGC/explicativos con avatar para marcas del exterior en USD (E2).
- **Abono:** suscripción de creatividades (E4), clipping con abono mensual (E12).
- **Capa semi-pasiva:** afiliados ML + YouTube Shopping (E24).
- ⚠ Es el sistema **más commoditizado**: las plataformas absorben el servicio (Meta Advantage+, la IA propia de Tiendanube, el doblaje gratis de YouTube). Y es el que menos aprovecha tu formación.

**Sinergias:** A y B se venden juntos ("ordeno tus procesos y pongo la IA a trabajar en ellos"). C es la capa técnica de A y B. D es otro negocio.

---

## 4. Catálogo completo (230 fichas)

Formato: `# | idea | tipo | score | por qué en 1 línea`. El número es el de la ficha dentro de su informe; la referencia cruzada se escribe frente + número (ej.: C2 = frente C, idea 2).

### Frente A — Cursos, educación e infoproductos (40)

| # | Idea | Tipo | Score | Por qué |
|---|---|---|---|---|
| A1 | Talleres in-company de IA para PyMEs (AR) | activo | 7 | Cash más rápido; 46% exige IA, 11% capacita (Trendsity/Deel 2026) |
| A2 | IA para estudios contables (ARCA/monotributo) | semi | 6 | Demanda real; necesita socio contador |
| A3 | IA para estudios jurídicos | semi | 4 | UCA y Thomson Reuters ocupan el espacio; no es abogado |
| A4 | IA para administración de consultorios | activo | 4 | Hueco no clínico; paga poco; datos de salud |
| A5 | Cursos de IA con puntaje docente | semi | 3 | El Estado capacitó gratis a 26.000 docentes en CABA |
| A6 | IA para inmobiliarias | semi | 4 | Comunidades a USD 97/mes con poca tracción |
| A7 | IA para RRHH/recruiters | activo | 3 | Cohortes a USD 995; sin credibilidad en el dominio |
| A8 | **IA aplicada a logística y depósitos (en español)** | semi/activo | **8** | Su ventaja real; en inglés USD 750-1.500 y casi nada en español |
| A9 | Lean / mejora continua + IA | semi | 6 | Loyola cobra USD 750 en 2026; mejor como módulo de A8 |
| A10 | Excel + IA (Claude for Excel/Copilot) para operaciones | semi | 7 | Ola nueva (beta 2026-05) |
| A11 | Capacitador Copilot M365 subcontratado | activo | 4 | Casi un empleo; pide certificación |
| A12 | AI literacy corporativa (art. 4 EU AI Act) | semi | 4 | Proveedores consolidados; venta B2B a Europa difícil |
| A13 | IA para adultos mayores | activo | 3 | OpenAI y AARP lo dan gratis |
| A14 | Bootcamp de IA para chicos | activo | 4 | Ticket bajo en AR; estacional; menores |
| A15 | Taller de búsqueda laboral con IA | semi | 4 | Público con poca plata |
| A16 | Claude Code para no programadores (español) | semi | 5 | Imperio Digital: 836 miembros a USD 67/mes; caduca rápido |
| A17 | Claude Cowork para profesionales hispanos | semi | 7 | Ventana nueva (Cowork Academy 2026-07); ventana corta |
| A18 | Curso/comunidad de n8n en español | semi | 3 | Océano rojo; el líder cobra USD 7/mes |
| A19 | Comunidad paga de nicho en Skool | semi | 5 | Ingresos publicados = techo; cobro AR no verificado |
| A20 | Cohorte de vibe coding para fundadores | semi | 4 | Survivorship; zona gurú |
| A21 | Workshops de 1 día / lightning lessons | activo | 5 | Herramienta de validación |
| A22 | Claude Skills empaquetadas por oficio | semi | 7 | Claude las escribe y él pone el criterio; sin marketplace oficial |
| A23 | Plantillas Excel de inventario | pasivo | 5 | USD 8-49; mejor como lead magnet |
| A24 | Kit ISO 9001 / SOPs en español | semi | 5 | Referencia: Qlause USD 99; exige conocer la norma |
| A25 | Toolkit "Orden operativo de depósito" | semi | 7 | Producto de entrada a la consultora |
| A26 | Plantillas Notion | pasivo | 2 | Saturado; Notion AI ya las genera |
| A27 | Membresía de recursos IA para docentes | semi | 3 | Ticket bajo, competencia gratuita |
| A28 | Newsletter paga "IA para operaciones/PyMEs" | semi | 5 | Lenta; Substack no paga a AR |
| A29 | Newsletter gratis B2B con sponsors | semi | 4 | Necesita miles de suscriptores |
| A30 | Curso en Udemy | pasivo | 3 | Revenue share de suscripción en 15% (2026) |
| A31 | Docente en Coderhouse/Crehana/Platzi/Domestika | activo | 5 | Credencial y práctica |
| A32 | Infoproducto IA en Hotmart (LATAM) | semi | 6 | R$ 140M en 2025 (+326% vs 2023); mejor canal de cobro desde AR |
| A33 | Diseño instruccional con IA para empresas | activo | 6 | Lo tradicional cuesta USD 2-4k por hora de video |
| A34 | Producción de cursos llave en mano para expertos | activo | 5 | Cobrar fijo, no revenue share |
| A35 | Localización/doblaje de cursos con IA | activo | 5 | Las plataformas lo automatizan |
| A36 | Clases particulares de ingeniería con IA | activo | 5 | Primer dólar en 1-3 semanas; ingreso por hora bajo |
| A37 | Preparación de certificaciones con bancos de preguntas IA | pasivo | 4 | Saturado; preguntas mal generadas = malas reseñas |
| A38 | Coaching 1:1 de implementación IA para dueños de PyME | activo | 6 | Orden Operativo en formato educativo |
| A39 | Cohorte "IA para ingenieros industriales/estudiantes" | semi | 6 | Credibilidad de par; demanda de Power BI + IA |
| A40 | Programas "montá tu agencia de IA" (meta-gurú) | — | 1 | **Trampa**: denuncias y FTC vs Air AI (~USD 19M) |

### Frente B — Agencia de automatización: voz, WhatsApp, CRM (42)

| # | Idea | Tipo | Score | Por qué |
|---|---|---|---|---|
| B1 | Recepcionista IA fuera de horario (dentistas EE.UU./España) | semi | 5 | Ticket alto; saturado, HIPAA, venta en frío difícil |
| B2 | Recepcionista IA bilingüe para hispanos en EE.UU. | semi | 6 | Ventaja de idioma, pero frágil |
| B3 | Voz IA para restaurantes | semi | 3 | Loman (USD 199) y Slang (USD 399) ya lo resuelven |
| B4 | Confirmación de turnos por voz | semi | 4 | En AR el canal es WhatsApp |
| B5 | Speed-to-lead por voz para contratistas EE.UU. | semi | 4 | Riesgo TCPA (FCC 24-17) |
| B6 | Voz para talleres mecánicos | semi | 4 | Es un problema de proceso, no de voz |
| B7 | Calificación por voz para inmobiliarias | semi | 3,5 | En AR nadie atiende números desconocidos |
| B8 | NPS y pedido de reseñas post-servicio | casi pasivo | 5 | Add-on; commodity |
| B9 | Reventa white-label de plataforma de voz | "pasivo" | 2,5 | Synthflow pasó a Enterprise (USD 30k/año) |
| B10 | **Turnos y recordatorios por WhatsApp para consultorios** | semi | **7** | Dolor universal y recurrente |
| B11 | WhatsApp para inmobiliarias (leads de portales) | semi | 6,5 | Los partners Kommo ya lo venden |
| B12 | **Cobranzas por WhatsApp + link Mercado Pago** | semi | **7** | ROI en pesos recuperados |
| B13 | Pedidos por WhatsApp para gastronomía | semi | 3,5 | Ticket bajo; SaaS baratos |
| B14 | WhatsApp para concesionarias de usados | semi | 5,5 | Buen ticket; vendedores resisten el CRM |
| B15 | Postventa por WhatsApp para Tiendanube/Shopify | semi | 5 | Apps nativas |
| B16 | Carritos abandonados por WhatsApp | casi pasivo | 4,5 | Mensajes de marketing caros |
| B17 | **Partner certificado Kommo + implementación** | semi | **7,5** | Capital 0, comisión vitalicia 35-50% + setup |
| B18 | Bot de comprobantes y vencimientos para contadores | semi | 6,5 | Nicho ARCA; contadores recomiendan |
| B19 | WhatsApp para talleres (turnos + service) | semi | 5 | Ticket bajo |
| B20 | Reactivación de socios de gimnasios | activo | 5,5 | Requiere opt-in |
| B21 | Reactivación de bases por SMS pago por cita (EE.UU.) | activo | 4 | TCPA/A2P; producto de gurús |
| B22 | Recall de pacientes inactivos | semi | 6 | Upsell de B10 |
| B23 | Agencia de cold email con IA | activo | 3,5 | Saturada, entregabilidad en caída |
| B24 | Seguimiento automático de presupuestos | semi | 6,5 | Simple; encaja con PyMEs industriales |
| B25 | Generador de reseñas Google | casi pasivo | 4,5 | Commodity |
| B26 | Llamada perdida → WhatsApp | pasivo | 4 | Problema chico en AR |
| B27 | Extracción de facturas → planilla | semi | 6 | Útil; commoditizado |
| B28 | **Lectura de remitos/OC + conciliación de stock (distribuidoras)** | semi | 6,5 | Productiza Orden Operativo |
| B29 | Reportes automáticos semanales por WhatsApp | casi pasivo | 6,5 | Abono casi pasivo |
| B30 | Agente cotizador para fabricantes y talleres | semi | 5,5 | Un error es responsabilidad |
| B31 | Respuestas IA a preguntas de ML | semi | 3 | Real Trends tiene 25.000+ empresas |
| B32 | Intake por WhatsApp para estudios jurídicos | semi | 5 | Abogados conservadores |
| B33 | Agente de soporte nivel 1 | semi | 4,5 | Plataformas nativas |
| B34 | Chatbot para colegios, municipios y cooperativas | semi | 4 | Venta pública lenta |
| B35 | Freelance de implementación IA en Upwork/Contra | activo | 6 | Cash en USD vía Payoneer |
| B36 | **Retainer de mantenimiento alert-driven** | semi | **7** | Modelo transversal; encaja con tu regla de no vigilar a diario |
| B37 | GoHighLevel SaaS mode vertical | semi | 3,5 | USD 297-497/mes fijos; epicentro de gurús |
| B38 | Fulfillment white-label para agencias de marketing | activo | 6 | Evita la venta en frío |
| B39 | Workshops de IA in-company | activo | 5,5 | Embudo (= A1) |
| B40 | **Paquete vertical productizado a precio fijo** | semi | **7** | Forma de pasar de activo a semi |
| B41 | Tracking de envíos por WhatsApp para transportes | semi | 5,5 | Sinergia con logística |
| B42 | Comisiones de herramientas (Kommo/n8n) como capa | pasivo | 6 | Atadas a clientes reales |

### Frente C — Ingeniería industrial y operaciones (34)

`⊂OO` = superposición total con la idea Orden Operativo.

| # | Idea | Tipo | Score | Por qué |
|---|---|---|---|---|
| C1 | **Diagnóstico Express a precio fijo** | activo | **7** | Puerta de entrada; modelo usado afuera (Osher, Upwork ~USD 800) |
| C2 | **Stock Sano (ABC + punto de reorden)** ⊂OO | activo→semi | **7,5** | Se vende remoto con un export; Claude en Excel |
| C3 | Re-slotting/layout de depósito ⊂OO | activo | 7 | 15-30% menos recorrido (dato de vendedores de software); caso Sporting |
| C4 | **Ops para vendedores de Mercado Libre** | activo→semi | **7,5** | 2,7 M de vendedores en AR; probable hueco |
| C5 | Consultor de 3PL para marcas Shopify (USD) | activo | 4 | Sin credibilidad en EE.UU. |
| C6 | Forecast para vendedores Amazon FBA (Upwork) | activo | 5,5 | Software a USD 49/mes lo reemplaza |
| C7 | Forecast y compras con Claude en Excel | activo→semi | 6,5 | El cliente puede terminar haciéndolo solo |
| C8 | Ruteo de reparto | activo | 5,5 | El valor está en rediseñar zonas |
| C9 | Mermas y vencimientos en retail chico ⊂OO | semi | 6 | Ticket bajo |
| C10 | **Costeo de recetas + mermas (gastronomía)** | activo→semi | **7** | Márgenes de 5-10% |
| C11 | Planilla de costeo gastronómico | pasivo | 5 | Calculadoras gratis |
| C12 | Costeo industrial y lista de precios | activo | 6 | El contador compite |
| C13 | Tiempos y métodos con video + IA | activo | 6 | Tendencia fuerte, industria en caída |
| C14 | Estudio de tiempos remoto | activo | 4,5 | Compite con software |
| C15 | Balanceo de línea / Yamazumi | activo | 4,5 | Sector textil en crisis |
| C16 | OEE "light" | activo→semi | 5 | ~41% de capacidad ociosa |
| C17 | Mantenimiento preventivo con MaintainX gratis | activo | 4,5 | Pide saber de mantenimiento |
| C18 | Control de calidad visual con IA | activo técnico | 2,5 | Hardware + programación |
| C19 | Kit 5S + auditoría mensual por fotos | semi | 6,5 | Sostiene el orden |
| C20 | Coaching Kaizen mensual | activo | 5 | Compite con el INTI |
| C21 | Auditoría de energía por facturas | activo | 6 | Tarifazo 2026; cobra por ahorro |
| C22 | **Manuales de procedimientos (SOPs) con IA** | activo productizado | **7** | Entregable transversal |
| C23 | Digitalizar procesos en papel con AppSheet | activo→semi | 6,5 | No-code |
| C24 | Tableros KPI en Looker Studio | semi | 5 | Commodity en Fiverr; suma como componente |
| C25 | Documentación ISO 9001 con IA | activo | 4,5 | Hacen falta credenciales |
| C26 | Back-office IA para profesionales de Higiene y Seguridad | semi | 6,5 | B2B2B; cuello de botella = papeleo |
| C27 | Process mining "light" | activo técnico | 3 | Mercado de empresas grandes |
| C28 | Diagnóstico de IA/automatización | activo | 5,5 | Saturado de agencias |
| C29 | Jefe de operaciones part-time | activo | 6 | Retainer post-proyecto |
| C30 | Ops manager remoto para EE.UU. | empleo | 6 | USD en 1-3 meses, pero es empleo |
| C31 | Presentaciones a subsidios (PAC/ANR) | activo | 3 | Sin convocatoria vigente verificada |
| C32 | Pack de plantillas de ingeniería industrial | pasivo | 5 | Lead magnet |
| C33 | Curso "Claude en Excel para operaciones" | semi | 5,5 | Después de 3-5 casos |
| C34 | Calculadoras web de ingeniería industrial (SEO) | pasivo | 4,5 | Lento |

### Frente D — Software sin programar (38)

| # | Idea | Tipo | Score | Por qué |
|---|---|---|---|---|
| D1 | **Kit Orden Operativo (Sheets + AppSheet/Glide + método)** | activo→semi | **8** | Diferencial + stack entendible; datos en la cuenta del cliente |
| D2 | **Herramientas internas a medida sobre stack gestionado** | activo | **7,5** | USD 500-3.000; sin pagos ni datos personales |
| D3 | Setup de Claude Skills + capacitación para PyMEs | activo | 7 | Fiverr +938% Claude Code |
| D4 | Tableros KPI como abono (Looker Studio) | semi | 7 | 1 h/cliente/mes |
| D5 | Limpieza de datos maestros (SKUs, precios) | activo | 7 | Puerta de entrada barata |
| D6 | Automatizaciones Apps Script | activo | 6,5 | Scripts cortos y auditables |
| D7 | Implementador de bots de WhatsApp (plataformas gestionadas) | activo→semi | 6,5 | Saturado; precios de Meta cambian |
| D8 | Partner Tiendanube/ERPs con comisión recurrente | activo + cola | 6 | Cero código |
| D9 | MCP a medida para PyMEs | activo | 4 | Credenciales + inyección de prompts |
| D10 | Agencia de recepcionista de voz IA | activo | 4 | En AR domina WhatsApp |
| D11 | MVPs para no técnicos | activo | 3,5 | Responde por código que no entiende |
| D12 | Rescate de apps vibe-coded | activo | 1,5 | Exige leer código en producción |
| D13 | Auditoría de seguridad | activo | 1,5 | No puede firmar seguridad |
| D14 | Plantillas Sheets/Apps Script en español | semi | 6,5 | Salen de lo que hace para clientes |
| D15 | Apps no-code de plantilla (inventario) | semi | 6 | Depende de la plataforma |
| D16 | Biblioteca de Claude Skills por rubro | pasivo | 5,5 | Sin store pago; se copian |
| D17 | Curso/comunidad vibe coding en español | semi | 4,5 | Saturado de gurús |
| D18 | Plantillas Notion/Airtable | pasivo | 4 | PyMEs AR usan Sheets |
| D19 | App para Tiendanube | semi | 5 | NubeSDK obligatorio desde 2026-08-30 + datos de compradores |
| D20 | Herramientas para vendedores de ML | semi | 5,5 | Real Trends incumbente |
| D21 | Add-on de Google Sheets | semi | 5 | Verificación OAuth pendiente |
| D22 | Agente de reposición/compras | semi | 5,5 | Mejor como función de D1 |
| D23 | Wrapper vertical de IA | semi | 4 | Lo más fácil de copiar |
| D24 | Directorio de nicho con IA | pasivo lento | 4,5 | AI Overviews |
| D25 | Micro-SaaS Lovable para un rubro AR | semi | 4 | Patrón de las brechas 2026 (Supabase sin RLS) |
| D26 | Plugin de WordPress | semi | 2,5 | Vector de hackeo |
| D27 | App de Shopify | semi | 3 | Revisión dura |
| D28 | App móvil vibe-coded | semi | 3 | Mediana USD 72/mes |
| D29 | App en el directorio de ChatGPT | semi | 3 | Descubrimiento, no cobro |
| D30 | Plugin de Claude Code propio | pasivo | 4 | Sin cobro nativo |
| D31 | MCP pago en marketplaces | pasivo | 5 | Menos del 5% monetiza |
| D32 | Telegram Mini App con Stars | pasivo | 2,5 | Retiro solo vía TON |
| D33 | Escáner de seguridad SaaS | semi | 1,5 | TrustMRR: USD 0-942/mes |
| D34 | Boilerplates "seguros" | pasivo | 2 | Vende seguridad que no puede verificar |
| D35 | Construir y vender apps vibe-coded | activo | 3 | Se venden a USD 100-5.000 |
| D36 | Generador de informes de relevamiento con IA | herramienta propia | 6,5 | Apalanca la consultoría |
| D37 | Portal de pedidos B2B por WhatsApp | semi | 5,5 | Sin pagos ni cuentas |
| D38 | Calculadoras logísticas gratis (EOQ, cubicaje) | pasivo | 6 | Imán de leads |

### Frente E — Contenido, marketing y e-commerce (38)

| # | Idea | Tipo | Score | Por qué |
|---|---|---|---|---|
| E1 | **Estudio de creatividades IA para e-commerce LATAM** | activo→semi | **7,5** | Meta Andromeda + 65.000 tiendas Tiendanube + Higgsfield |
| E2 | Packs UGC/explicativos con avatar para marcas del exterior | activo | 6,5 | USD vía Upwork (+329%); testimonios con avatar = ilegal (FTC) |
| E3 | Producción de creatividades white-label para agencias | activo | 6 | Margen bajo |
| E4 | Suscripción de creatividades "ilimitadas" | semi | 6,5 | Fase 2 de E1 |
| E5 | Fotos de producto IA para ML/Tiendanube | activo | 5,5 | Oferta de entrada |
| E6 | Optimización de fichas y catálogo en ML | activo | 6 | Se cruza con Orden Operativo |
| E7 | Staging virtual + reels para inmobiliarias | activo | 5,5 | Herramientas a USD 0,24 por foto |
| E8 | Fotos de menú para gastronomía | activo | 4,5 | Rubro con poca plata |
| E9 | Logos/branding | activo | 3,5 | Commoditizado |
| E10 | Pitch decks | activo | 4 | Gamma/Claude |
| E11 | Videos de capacitación con avatar | activo | 5 | Upsell de Orden Operativo |
| E12 | Clipping con abono mensual para podcasts hispanos | activo | 6,5 | Reutiliza el clipper en cartera |
| E13 | Edición long-form con IA | activo | 5 | Exige oficio de edición |
| E14 | Miniaturas y títulos A/B | activo | 4,5 | Commoditizado |
| E15 | Podcast → newsletter/LinkedIn/carruseles | activo | 5,5 | Complemento de E12 |
| E16 | Doblaje de canales de YouTube | activo | 3,5 | YouTube lo hace gratis en 27 idiomas |
| E17 | Localización de cursos | activo | 3 | Hotmart AI nativo |
| E18 | Redes sociales para PyMEs locales | activo | 5 | Saturado |
| E19 | Ghostwriting de LinkedIn en español | activo | 6 | USD 300-1.000/mes; sirve para vender la consultora |
| E20 | Ghostwriting en X/Threads | activo | 4 | Audiencia hispana chica |
| E21 | "Clon digital" en video para profesionales | activo | 5,5 | Etiquetado obligatorio |
| E22 | Newsletter en inglés con sponsors | semi | 4,5 | Mediana USD 32 por mil suscriptores |
| E23 | Newsletter B2B para vendedores de ML | semi | 5,5 | Más fuente de clientes que negocio |
| E24 | **Reseñas en video + afiliados ML / YouTube Shopping AR** | semi | **7** | Evidencia nueva (ML AR 2026-03-11) |
| E25 | Shorts/TikTok "hallazgos de ML" | semi | 6 | Brazo de distribución de E24 |
| E26 | Podcasts generados con IA | pasivo | 2,5 | Solo funciona a escala industrial |
| E27 | Canal faceless nuevo | semi | 4,5 | Regla de contenido inauténtico (2025-07-15) |
| E28 | Influencer virtual | semi | 3 | Survivorship; leyes de NY y la UE |
| E29 | Afiliado de TikTok Shop | semi | 2 | No disponible en AR |
| E30 | Tienda Tiendanube con marca propia | activo | 4 | Capital de inventario |
| E31 | Dropshipping internacional | activo | 2 | Cobro + saturación |
| E32 | Auditoría GEO/AEO | activo | 5 | IA = 0,32% del tráfico web |
| E33 | Reporte mensual de visibilidad en IA | semi | 4,5 | Sería 6,5 si programara |
| E34 | SEO programático | pasivo | 2,5 | Update de Google de marzo 2026: -60/80% de tráfico para granjas IA |
| E35 | Canciones personalizadas IA (regalo) | activo | 5,5 | Demanda probada; licencias |
| E36 | Jingles para marcas | activo | 4,5 | Derechos poco claros |
| E37 | Videos personalizados para eventos | activo | 6 | Primer peso en 1-3 semanas |
| E38 | Libros infantiles personalizados | semi | 4 | Survivorship |

### Frente F — Olas emergentes y verticales (38)

| # | Idea | Tipo | Score | Por qué |
|---|---|---|---|---|
| F1 | **Evaluador de modelos IA en español** | activo (empleo) | **7** | USD 25-60/h; 929 ofertas para AR |
| F2 | Experto en ing. industrial para evaluar IA | activo | 3 | USD 70-110/h pero exige residir en EE.UU. + 4 años |
| F3 | Red teaming IA | activo | 3 | Torneo: cobraron 4 equipos de 339 |
| F4 | **Implementador Claude/Cowork para equipos no técnicos** | activo→semi | **8** | Anthropic crea la necesidad |
| F5 | Constructor de Claude Skills a medida | activo | 7 | Productización de F4 |
| F6 | Responsable de IA fraccional | activo | 6 | Etapa 2 de F4 |
| F7 | Kit de política de uso de IA / shadow AI | semi | 5 | 81% usa IA no aprobada; gancho |
| F8 | Cumplimiento EU AI Act para PyMEs | activo | 3 | Alto riesgo postergado al 2027-12-02 |
| F9 | Conectores MCP para software argentino | semi | 5 | Requiere código |
| F10 | Catálogo "listo para agentes" (Tiendanube/ML) | recurrente | 6,5 | MODO+Frávega en ChatGPT (2026-09-23); demanda chica todavía |
| F11 | Endpoints x402 | pasivo | 3 | ~USD 28k/día en total |
| F12 | GEO para negocios hispanos | recurrente | 5 | Medición difusa |
| F13 | "AI operations" remoto para startups EE.UU. | activo | 5 | Es empleo |
| F14 | QA y evals de chatbots en español | activo | 6 | Arbitraje de idioma |
| F15 | Diagnóstico "IA-ready" a precio fijo | activo | 6 | Embudo |
| F16 | Ordenar datos de PyMEs para que la IA sirva | activo | 5,5 | Difícil de vender solo |
| F17 | **IA para estudios contables argentinos** | activo+semi | **7** | 311 h/año de impuestos; ventana de 12-24 meses |
| F18 | Pack de Skills para contadores | semi | 5 | Complemento de F17 |
| F19 | **Radar de licitaciones + resumen de pliegos** | semi+activo | **7** | Demanda estructural; requiere scraping |
| F20 | IA para estudios jurídicos chicos | activo | 5 | Jugadores grandes |
| F21 | Kit IA para inmobiliarias | recurrente | 5 | Los portales la integran |
| F22 | Back-office IA para consultorios / obras sociales | semi | 5 | Datos sensibles |
| F23 | Asistente para productores de seguros (PAS) | activo→semi | 6,5 | Cara (EE.UU.) a 7 cifras de ARR en 7 meses |
| F24 | Cobranzas por WhatsApp con IA | semi | 5 | Riesgo de baneo (= B12, que lo puntúa 7) |
| F25 | Reclutamiento asistido por IA | activo | 5 | Bumeran y LinkedIn la integran |
| F26 | Clasificación NCM para importadores | activo | 5 | Un error = multas |
| F27 | Hotelería/cabañas: consulta → reserva directa | semi | 4,5 | WeSpeak ya está |
| F28 | Cómputo y presupuesto de obra con IA | activo | 4,5 | Falta credibilidad técnica |
| F29 | Gastronomía: costeo y mermas | activo | 5,5 | = C10 |
| F30 | Distribuidoras: ruteo y stock | activo | 6 | Problema eterno, encaja con Sporting |
| F31 | Capacitación IA para docentes | activo | 4 | El Estado capacita gratis |
| F32 | Municipios: chatbot vecinal | activo | 3 | Venta política |
| F33 | Subsidios PyME: alertas + postulaciones | activo | 5 | Fusionable con F19 |
| F34 | **Implementación IA en español para PyMEs hispanas de EE.UU.** | activo→semi | **7** | Cobro en USD con ventaja de idioma |
| F35 | Subcontratista white-label para agencias | activo | 6 | Depende de 1-2 agencias |
| F36 | Método "traer al español lo que en EE.UU. tiene funding" | meta | n/a | Se aplicó en F22-F28 |
| F37 | Verifactu (España) | activo | 3 | Ola de una sola vez |
| F38 | Cohortes de Claude/Cowork en español | semi | 5 | Canal de adquisición de F4 |

---

## 5. Duplicados entre frentes (para no contar dos veces)

| Tema | Fichas | Score unificado |
|---|---|---|
| Claude Skills / setup de Claude | A22, D3, D16, F5, F18 | 7 (como servicio), 5-5,5 (como producto suelto) |
| Estudios contables | A2, B18, B27, F17, F18 | 7 |
| Talleres in-company | A1, B39 | 7 |
| Cohortes Claude/Cowork | A17, F38 | 6-7 (ventana corta) |
| GEO / visibilidad en IA | E32, E33, F12 | 5 |
| Vibe coding (curso) | A16, A20, D17 | 4-5 |
| Bots de WhatsApp genéricos | D7 vs B10-B19 | se puntúan por rubro (B) |
| Recepcionista de voz | D10, B1-B7 | 4-6 (para AR no) |
| Plantillas de inventario/IE | A23, C32, D14 | 5-6,5 (lead magnet) |
| KPI dashboards | C24, D4 | 5-7 (solo como abono) |
| Gastronomía | C10, C11, F29, B13, E8 | 7 (costeo/mermas) |
| Distribuidoras | F30, B28, B29 | 6,5 |
| Diagnóstico | C1, C28, F15 | 7 |
| Subsidios/licitaciones | C31, F19, F33 | 7 (licitaciones) |
| Cobranzas | B12, F24 | 7 (con opt-in y mensajes utility) |
| Cursos de IA para docentes | A5, A27, F31 | 3-4 |
| Localización/doblaje | A35, E16, E17 | 3-5 |

---

## 6. Trampas transversales (lo que detectaron los 6 frentes)

1. **Gurús que venden "cómo montar tu agencia de IA" o "cómo vender cursos".** Ganan con el curso, no con el método. Es la categoría con más denuncias (Trustpilot, FTC vs Air AI por ~USD 19M). Si la fuente vende un curso sobre el tema, sus cifras no cuentan.
2. **Cifras inventadas que circulan:** el "marketplace oficial de Claude Skills con USD 48M" **no existe**. Lo detectaron dos frentes por separado.
3. **Los "ingresos" de Skool y otras comunidades son precio × miembros**, o sea un techo, no facturación real.
4. **Las plataformas absorben servicios:** doblaje (YouTube, gratis en 27 idiomas), localización (Hotmart AI), creatividades (Meta Advantage+), fotos (la IA propia de Tiendanube), respuestas en ML (Real Trends). **Antes de elegir un servicio, preguntar: ¿lo va a hacer gratis la plataforma en 12 meses?**
5. **Fechas regulatorias mal citadas:** la regla de contenido inauténtico de YouTube es de **2025-07-15** (no de 2026). Las obligaciones de alto riesgo del EU AI Act se **postergaron al 2027-12-02** (no "agosto 2026").
6. **Software vibe-coded = riesgo real.** Según un estudio de Symbiotic Security (que vende escáneres, así que hay conflicto de interés), el 98% de 1.072 apps tenía al menos una falla (2026-06-02). Además, la propia plataforma Lovable tuvo una brecha de 48 días en abril de 2026. **Regla para vos:** nada que maneje pagos, datos personales o un backend propio expuesto a internet. Usá stacks gestionados (Google Workspace, AppSheet, Kommo) donde los datos viven en la cuenta del cliente.
7. **Industria argentina en contracción:** se vende ahorro (stock parado, merma, costo), no "más productividad".
8. **Voz IA en Argentina:** nadie atiende números desconocidos. El canal es WhatsApp.
9. **Cobro desde AR:** Hotmart (vía Payoneer) y Lemon Squeezy (banco o PayPal) están verificados. Skool, Maven y Substack pagan por Stripe y **probablemente no** pagan a AR (sin verificar). TikTok Shop no está disponible en AR.

---

## 7. Pendientes de verificar (cuota de búsqueda agotada)

Antes de pasar cualquier idea a `ideas/`, verificar los puntos que la afectan:

- [ ] **Precios de WhatsApp de Meta desde 2026-10-01:** ¿se cobran los mensajes utility dentro de la ventana de 24 h? YCloud dice que sí y la página oficial de Meta, que no. **Afecta a todo el Sistema C.**
- [ ] Comisión real y requisitos del programa de partners de Kommo para AR.
- [ ] Si Skool, Maven, Substack y Beehiiv pagan a cuentas argentinas.
- [ ] Precios 2026 de AppSheet/Glide; verificación OAuth para add-ons de Google Workspace.
- [ ] Si Stripe Managed Payments acepta vendedores argentinos.
- [ ] Tarifas 2026 en ARS de community managers, creatividades y consultores de procesos en AR.
- [ ] Términos de uso comercial de los generadores de música IA.
- [ ] Fecha de llegada de TikTok Shop a AR.
- [ ] Gastronomía, logística, subsidios y nearshoring (frente F): evidencia débil, marcada [NO VERIFICADO].

---

## 8. Recomendación (para decidir, no está decidido)

**Impacto en lo que ya está en marcha:** el proyecto `stack-de-datos` (actores Apify, micro-SaaS, MCP) **asumía que sabías programar**. Con el dato nuevo, su riesgo sube mucho: tendrías código en producción que no podés auditar, y clientes que pagan por él. **Hay que re-evaluarlo**: pausarlo, achicarlo a una sola pieza o mantenerlo solo como experimento.

**Recomendación:** fusionar los Sistemas A y B en **una sola oferta**:

> **"Ordeno tus operaciones y pongo la IA a trabajar en ellas"** — método de ingeniería industrial + Claude + herramientas no-code, para PyMEs con stock (vendedores de ML, distribuidoras, gastronomía).

- **Por qué esta y no otra:** es la única combinación donde (a) tenés una ventaja que no se copia con una suscripción a la IA, (b) la ola es nueva y está creciendo (Claude para PyMEs, 2026), (c) no necesitás programar y (d) se productiza hacia semi-pasivo (toolkit, curso, skills) una vez que tengas casos.
- **Escalera:** taller in-company o Diagnóstico Express → proyecto (Stock Sano + SOPs + Claude configurado) → abono mensual alert-driven (B36, encaja con tu regla de no vigilar a diario) → a los 6-12 meses, curso/toolkit en Hotmart con los casos reales.
- **WhatsApp (Sistema C)** entra como **capa técnica** cuando un cliente la necesite (Kommo partner), no como negocio aparte desde el día 1.
- **Puente de caja opcional** si necesitás ingresos mientras arranca: evaluador de modelos en español (F1), USD 25-60/h, sin capital. Compite por las mismas horas.
- **Expectativa realista** (estimación propia, no dato de fuente): un servicio así, bien vendido, puede llegar a varios clientes con abono en 6-12 meses. Eso son algunos miles de USD por mes **si la venta funciona**. El cuello de botella no va a ser Claude, va a ser **conseguir clientes**. Por eso lo primero a validar es la venta, no el producto.

**Próximo paso propuesto:** elegir el rubro de entrada (vendedores de ML / distribuidoras / gastronomía / estudios contables) y armar en `ideas/` la ficha seria con scoring, precio, guion de oferta y un test de validación con 5-10 conversaciones reales antes de construir nada.
