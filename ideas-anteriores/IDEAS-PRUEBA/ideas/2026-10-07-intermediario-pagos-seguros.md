# Idea: intermediario de pagos seguros para transacciones con el exterior (escrow)

- **Origen:** idea de Facu, 2026-10-07.
- **Etapa:** candidata a **etapa 2 (startup)**. Es fintech regulada; no entra como negocio intermedio con USD 1.300 y sin programar, pero se puede **validar barato** desde ya.
- **Estado:** anotada + primera investigación (2026-10-07). Sin decisión.

## 1. La idea, en palabras de Facu (resumida fielmente)

Un intermediario para compras de productos o pagos de servicios entre personas o empresas de distintos países, para que nadie estafe a nadie. Ejemplos de Facu:
- Le entrego un producto o servicio a una empresa del exterior y nunca me paga.
- Al revés: me pagan por adelantado y yo nunca entrego.

Cómo funcionaría: las dos partes entran a la app, se verifica la identidad de ambos, el comprador deja el pago retenido y **la plata se libera recién cuando se cumple lo acordado** (por ejemplo, que el producto llegó). El negocio cobra una **comisión por transacción**. "Parecido a Mercado Libre o Amazon, pero más destinado a servicios y productos."

## 2. Cómo se llama esto

Es un servicio de **escrow** (custodia de pagos o depósito en garantía): un tercero neutral retiene la plata hasta que se cumplen las condiciones.

## 3. ¿Ya existe? Sí, en varias formas (datos verificados el 2026-10-07)

| Quién | Qué hace | Dato clave | Fuente |
|---|---|---|---|
| **Escrow.com** (EE.UU.) | Escrow genérico online: dominios, vehículos, mercadería, servicios por hitos ("Milestone Escrow"), API para plataformas | Licenciado en los 50 estados de EE.UU. Comisión desde 2024-05-31: 2,60% hasta USD 5.000 (mínimo USD 50), bajando a 0,70% arriba de USD 10 M. API "desde 0,89%" sin mínimo. Clientes como eBay, GoDaddy, AutoTrader | [DomainInvesting](https://domaininvesting.com/escrow-com-escrow-fee/), [Escrow.com: anuncio de API (PDF)](https://www.escrow.com/build/pdfs/api-launch/Escrowcom-announces-Platform-API.pdf), [Wikipedia](https://Www.Wikipedia.org/wiki/Escrow.com) |
| **Upwork** | Escrow para servicios freelance: el cliente deposita cada hito y se libera cuando aprueba | Comisión al freelancer: 10% fijo (2026). El cliente tiene hasta 14 días para revisar, si no se aprueba solo. Mediación en disputas | [Upwork](https://www.upwork.com/resources/securely-safely-pay-freelancers), [Unilink](https://www.unilink.us/blog/upwork-hourly-vs-fixed-2026) |
| **Workana** (LATAM) | Plataforma freelance que usa escrow | Mencionado en un artículo de ecosistemastartup.com; no verifiqué detalles | [ecosistemastartup](https://ecosistemastartup.com/?p=62466) |
| **Trustap** (Irlanda) | Escrow para transacciones entre desconocidos y para marketplaces | Levantó USD 5,5 M (Serie A, 2024-07). Opera en más de 100 países. Retiene hasta la entrega + 24 h de reclamo. **Si funciona para Argentina: no lo pude verificar** (sus notas de versión no la mencionan) | [Tech.eu](https://tech.eu/2024/07/09/trustap-bags-5-5m-series-a-for-its-secure-marketplace-transaction-platform/), [Sharetribe](https://www.sharetribe.com/academy/marketplace-payments/trustap-overview/), [docs Trustap](https://docs.trustap.com/docs/intro/release-notes) |
| **Payoneer Escrow** (ex Armor Payments) | Escrow B2B internacional, USD 500 a 1 M por transacción | Comprado por Payoneer en 2016. **Corrección 2026-10-08: cerró.** Payoneer dejó de ofrecerlo el 2018-10-18 ([Domain Name Wire, 2018-07-10](https://domainnamewire.com/2018/07/10/payoneer-exits-the-escrow-business/)) | [TechCrunch 2016](https://techcrunch.com/2016/03/15/b2b-payment-service-payoneer-acquires-escrow-as-a-service-platform-armor-payments) |
| **Mercado Pago / Mercado Libre** | Retiene el pago del comprador y lo libera al vendedor cuando se verifica la operación (dentro de su ecosistema) | Fuente secundaria (Harvard D3); no verifiqué condiciones actuales | [Harvard D3](https://d3.harvard.edu/platform-digit/submission/the-latin-american-ebay-transforms-the-region/index.html) |
| **Kustodia** (México) | Pagos con escrow sobre blockchain, operado dentro de WhatsApp | Artículo comisionado (publicidad paga), tomar con cuidado | [Cointelegraph](https://cointelegraph.com/commissioned/how-whatsapp-is-becoming-latin-americas-consumer-fintech-interface) |
| **Escrowpay** (India) | Escrow digital | Levantó USD 6 M (2024-01) | [Fintech Global](https://fintech.global/2024/01/02/digital-escrow-services-leader-escrowpay-raises-6m-in-extended-series-a-round/) |

Otros que conozco pero **no verifiqué hoy**: Alibaba Trade Assurance (protección para compras a proveedores), protección al comprador y al vendedor de PayPal, P2P de exchanges cripto (retienen los USDT hasta que se confirma el pago).

**Dato técnico importante:** Stripe aclara que **no ofrece escrow** (tiene una definición legal precisa). Solo permite retener pagos de una plataforma hasta 90 días. Fuente: [Stripe Docs, manual payouts](https://docs.stripe.com/connect/manual-payouts).

## 4. Regulación en Argentina (verificado parcialmente)

- Una empresa no financiera que ofrece cuentas de pago es **Proveedor de Servicios de Pago (PSP)**. Tiene que inscribirse en un registro del BCRA y queda bajo su vigilancia (Comunicación "A" 6859).
- Los fondos de los clientes tienen que estar **disponibles en todo momento** y **depositados en su totalidad en cuentas en pesos en bancos locales**.
- Los directivos del PSP responden con el régimen sancionatorio de la Ley de Entidades Financieras.
- Fuentes: [abogados.com.ar (Com. A 6859)](https://abogados.com.ar/el-bcra-reglamento-mediante-la-comunicacion-a-6859-la-actuacion-de-los-proveedores-de-servicios-de-pago-psp/25113), [BCRA](https://www.bcra.gob.ar/noticias/el-banco-central-complemento-el-marco-general-para-los-proveedores-de-servicios-de-pago/).
- **No verificado todavía** (hay que verlo con un abogado antes de cualquier paso real):
  - si retener plata de terceros para escrow encaja en PSP o necesita otra figura;
  - las reglas de cambio para cobrar y pagar en dólares con el exterior a octubre de 2026;
  - las obligaciones de prevención de lavado ante la UIF.
- **Conocimiento general, no verificado hoy:** guardar datos de tarjetas exige cumplir el estándar PCI DSS. En la práctica, nadie chico guarda tarjetas: se usa un procesador de pagos.

## 5. Opinión de Claude (2026-10-07) — opinión, no dato

**Lo bueno:**
- El problema es real y lo detectaste mirando una necesidad concreta, no sentándote a "inventar". Así suelen nacer las buenas ideas (Graham, 2012).
- La confianza en transacciones con el exterior es un dolor especialmente argentino: desconfianza, dificultad para cobrar en dólares, poca protección legal entre países.

**Lo difícil:**
1. **La versión "intermediario genérico para todo" ya existe** (Escrow.com, Trustap, Payoneer) y la versión para servicios está metida dentro de los marketplaces (Upwork, Workana). Competir de frente contra eso, sin capital ni licencias, es muy difícil.
2. **El corazón del negocio no es retener la plata, es resolver disputas.** ¿Quién decide si el servicio se cumplió? En productos hay tracking. En servicios ("el logo no me gustó") es subjetivo, y ahí se rompen estos negocios.
3. **Las dos partes tienen que aceptar usarlo.** El que tiene más poder (por ejemplo, la empresa grande que compra) no quiere sumar un paso ni una comisión.
4. **Atrae fraude.** Los estafadores prueban justamente los sistemas de pago seguro.
5. **Regulación y capital:** manejar plata de terceros es fintech regulada (ver punto 4). Necesita abogados, licencias o un socio licenciado, y probablemente inversión externa.

**Dónde podría haber un hueco (hipótesis a validar, no datos):**
- **Ir a un nicho, no a "todo".** Un nicho donde se cumplan tres cosas: hay transacciones con el exterior entre desconocidos; lo entregado se puede verificar objetivamente; y las plataformas actuales no lo cubren, no funcionan desde Argentina o cobran caro. Candidatos a explorar:
  - freelancers y agencias argentinas con clientes directos del exterior, fuera de Upwork (que cobra 10%);
  - exportadores PyME que venden por primera vez;
  - compra o venta de bienes usados de valor alto entre países (maquinaria, equipos);
  - importaciones chicas.
- **No tener la plata vos.** Construir encima de alguien licenciado (por ejemplo, la API de Escrow.com) y que tu valor sea el nicho, el español, la verificación y la resolución de disputas. Si Escrow.com acepta usuarios argentinos: **no verificado**.

## 6. Cómo validarla barato (propuesta, sin manejar plata de nadie)

1. **15 a 20 entrevistas** con argentinos que compran o venden al exterior: freelancers, agencias, exportadores chicos. Método "The Mom Test": preguntar por hechos pasados, no por opiniones. ¿Te estafaron o te dejaron de pagar alguna vez? ¿Cuánto perdiste? ¿Qué usás hoy para protegerte? ¿Cuánto pagaste por eso?
2. Con las entrevistas, **elegir el nicho donde más duele** y donde lo entregado es verificable.
3. **Prueba "a mano"**: ayudar a 3 a 5 transacciones reales usando un escrow que ya existe, cobrando por la gestión, para ver si alguien paga por la tranquilidad. **Antes, consulta legal.** Nunca retener plata de terceros en cuentas propias.
4. Recién con evidencia de pago: pensar el producto propio, los socios y el financiamiento.

## 7. Preguntas abiertas

- ¿Qué nicho? (sale de las entrevistas)
- ¿Funciona Trustap para argentinos hoy? (Escrow.com sí, verificado el 2026-10-07; Payoneer Escrow cerró en 2018.)
- ¿Qué figura legal hace falta en Argentina para custodiar pagos de terceros?
- ¿Facu tiene contactos que vendan o compren al exterior para las primeras entrevistas?

## 8. Escrow.com en detalle (investigado el 2026-10-07)

- **Historia:** fundada en **1999** por Fidelity National Financial. Fidelity la liquidó en 2002. La compró un inversor privado en 2004 y **Freelancer.com en 2015, por USD 7,5 M**. Sede en San Francisco. Fuente: [Wikipedia](https://en.wikipedia.org/wiki/Escrow.com).
- **Volumen:** superó **USD 2.000 M acumulados en 2013**. No encontré cifras más nuevas. Fuente: Wikipedia.
- **Licencias:** según Wikipedia, 42 licencias de servicios financieros otorgadas o en trámite (escrow y transmisión de dinero en varios estados de EE.UU.).
- **Cómo funciona** (fuente: [escrow.com](https://www.escrow.com/what-is-escrow)):
  1. Las partes acuerdan los términos.
  2. El comprador paga a la cuenta de escrow.
  3. Verificado el pago, el vendedor envía.
  4. El comprador tiene un período de inspección para aceptar o rechazar.
  5. Si acepta, se libera la plata al vendedor.
- **Disputas** (fuente: [escrow.com, disputas](https://www.escrow.com/learn-more/how-escrow-works/escrow-dispute)):
  - Hay disputa cuando el comprador devuelve la mercadería y el vendedor rechaza esa devolución.
  - Tiene dos etapas de 14 días: primero negociación entre las partes; después tienen que iniciar **arbitraje con un tercero** (recomiendan American Arbitration Association, JAMS o net-ARB).
  - **Dato clave para la idea: Escrow.com no se pone a juzgar quién tiene razón. Retiene la plata y deriva el conflicto a árbitros externos.** Así resuelve el problema de "la caja llegó vacía" que planteó Facu.
- **Argentina:** Escrow.com dice operar "en todo el mundo" con dos listas de excepciones (países restringidos y sancionados). **Argentina no figura en ninguna** (verificado el 2026-10-07). Las transferencias internacionales suman USD 25. Fuente: [escrow.com, países no soportados](https://www.escrow.com/support/faqs/what-countries-are-not-supported-by-escrowcom).
- **Consecuencia (opinión):** un argentino ya puede usar Escrow.com hoy. "Traerlo a Argentina" tiene sentido solo si se agrega algo que Escrow.com no da. Por ejemplo: español, pesos y medios de pago locales, operaciones chicas (su mínimo es USD 50 de comisión), verificación en destino o un nicho específico. Hay que averiguar qué le falta a un argentino al usarlo, y eso sale de las entrevistas.

## 9. Investigación de nichos (2026-10-08)

Ver `research/fuentes/2026-10-08-L1-intermediario.md`. Resumen:
- El escrow genérico es un negocio chico: Escrow.com facturó A$12,3 M en 2025, con volumen en caída por cuarto año seguido ([Domain Name Wire, 2026-02-25](https://domainnamewire.com/2026/02/25/escrow-com-reports-record-revenue-but-payments-fall/)).
- Los que ganaron estaban metidos en un nicho. Por ejemplo, Caramel (cierre de compraventas de autos entre particulares) fue comprada por eBay en enero de 2025 ([TechCrunch](https://techcrunch.com/2025/01/13/ebay-acquires-caramel-to-reduce-risk-and-complexity-of-online-car-sales)).
- Nicho argentino n.º 1 propuesto: **"cierre seguro" de autos usados entre particulares**. El registro hace de juez, así que no hay "caja vacía" posible. En 2025 hubo 1.887.024 transferencias de usados (CCA vía El Economista, 2026-01-12).
