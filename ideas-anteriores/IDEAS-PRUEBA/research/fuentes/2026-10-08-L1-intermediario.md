# L1 — Intermediario de transacciones (escrow): investigación de nichos en Argentina

- **Fecha:** 2026-10-08
- **Construye sobre:** `ideas/2026-10-07-intermediario-pagos-seguros.md` (Escrow.com, Upwork, Trustap, regulación PSP del BCRA). Acá no se repite eso: se agrega dolor argentino con datos, soluciones locales, nichos que funcionaron afuera, disputas, nichos candidatos, figura legal, MVP, validación y veredicto.
- **Convención:** **DATO** = verificado, con fuente y fecha. **ESTIMACIÓN** = cálculo o supuesto mío, con el razonamiento. **OPINIÓN** = juicio mío. "No verificado" = no lo pude confirmar.
- **Límite de esta investigación (aviso honesto):** hice 23 búsquedas web y unas 20 lecturas de páginas. Ahí se agotó el cupo de búsquedas de la sesión. Quedaron **sin investigar**: datos de impago a freelancers y exportadores argentinos, garantías de reventa de entradas tipo StubHub, condiciones de Mercado Pago Argentina para link de pago y "liberación diferida" de fondos, escribanías como depositarias y costo de una consulta legal. Están marcados abajo como pendientes.

---

## 0. Correcciones a la ficha del 2026-10-07

| Lo que decía la ficha | Lo que encontré hoy |
|---|---|
| Payoneer Escrow: "si sigue activo, no lo pude verificar" | **DATO: cerró.** Payoneer avisó en julio de 2018 que dejaba el negocio de escrow. El servicio se dejó de ofrecer el **2018-10-18**. No dio motivo. La prensa del rubro dominios lo atribuyó a márgenes finos y a que hace falta mucha escala (eso es opinión de esa prensa). Fuentes: [Domain Name Wire, 2018-07-10](https://domainnamewire.com/2018/07/10/payoneer-exits-the-escrow-business/), [DomainInvesting](https://domaininvesting.com/payoneer-exiting-domain-escrow-business/), [PYMNTS](https://www.pymnts.com/?p=523413). |
| Kustodia (México): solo había un artículo pago | Hay una nota periodística firmada en El Observador (2026-06-01), sin rótulo de publicidad. Pero todo lo que dice sale de la boca del fundador: no hay datos independientes de volumen, licencias ni financiamiento. Ver punto 2.5. |

---

## 1. El dolor en Argentina, con datos

### 1.1 Estadística oficial nacional (la mejor que existe)

**DATO** — Unidad Fiscal Especializada en Ciberdelincuencia (UFECI, Ministerio Público Fiscal), informe anual 2024, publicado el 2025-06-30 ([fiscales.gob.ar](https://www.fiscales.gob.ar/ciberdelincuencia/la-unidad-fiscal-especializada-en-ciberdelincuencia-informa-que-en-2024-se-registro-un-aumento-interanual-del-211-en-la-cantidad-de-reportes-de-delitos-informaticos/); [PDF del informe](https://www.fiscales.gob.ar/wp-content/uploads/2025/06/UFECI_informe_anual_2024.pdf)):

| Indicador 2024 | Valor |
|---|---|
| Reportes totales de delitos informáticos | **34.468** (+21,1% contra 2023) |
| Serie anterior | 2021: 22.364 · 2022: 32.395 · 2023: 28.456 ([Chequeado, 2025-07-04](https://chequeado.com/el-explicador/las-denuncias-de-estafas-virtuales-aumentaron-un-21-en-2024-cuales-son-los-tipos-de-fraude-mas-comunes/)) |
| "Fraude en línea" | **21.729 reportes (63%)** |
| …de eso, **compraventa de bienes o servicios por internet** | **56%** del fraude en línea |
| …homebanking / esquemas Ponzi / otros | 18% / 10% / 16% |
| Fraudes con **alquileres temporarios** | **488 reportes** (el 51% en el primer trimestre) |
| Acceso ilegítimo a cuentas: Mercado Pago | 26% de 2.877 casos (740) ([Chequeado](https://chequeado.com/el-explicador/las-denuncias-de-estafas-virtuales-aumentaron-un-21-en-2024-cuales-son-los-tipos-de-fraude-mas-comunes/)) |

- **ESTIMACIÓN (cálculo mío):** 56% de 21.729 son **unos 12.170 reportes de estafas en compraventas online en 2024**. Es lo más parecido a "el mercado de víctimas" que pude encontrar.
- **Ojo con esta cifra:**
  - Son reportes a la UFECI, no todos los delitos. Muchas víctimas denuncian en la comisaría o en fiscalías provinciales, y muchas no denuncian. Cuánto es el subregistro: **no lo sé**, no encontré un estudio.
  - No dice **cuánta plata** se perdió ni el ticket promedio. Ese dato, clave para saber si alguien pagaría una comisión, **no lo encontré**.
  - El dato nacional de 2025 **todavía no estaba publicado**: Chequeado, el 2025-12-31, seguía usando 2024 como último dato ([Chequeado](https://chequeado.com/nota/las-estafas-con-las-que-intentaron-enganarnos-en-2025)).
- **DATO provincial (no comparable con el nacional):** San Juan registró 3.713 denuncias por estafas y delitos informáticos en 2025, sin contar los últimos 20 días de diciembre ([Diario de Cuyo, 2026-01-25](https://www.diariodecuyo.com.ar/sanjuan/san-juan-registro-mas-de-3-700-denuncias-por-estafas-y-delitos-informaticos-en-2025-pornografia-infantil-y-el-grooming-con-numeros-que-preocupan-1821952.html)).

### 1.2 Autos usados (el nicho con más plata por operación)

- **DATO — tamaño:** en 2025 se transfirieron **1.887.024 autos usados**, récord histórico (+8,12% contra 2024). Fuente: Cámara del Comercio Automotor (CCA), vía [El Economista, 2026-01-12](https://eleconomista.com.ar/autos/la-venta-autos-usados-alcanzo-su-record-historico-2025-n91863). Ojo: la CCA agrupa a concesionarios de usados, o sea que es la fuente del propio sector.
- **DATO — 2026:** entre enero y mayo hubo 736.136 transferencias, un 5% menos que en el mismo período de 2025 (CCA, vía [Ámbito, 2026-06-17](https://www.ambito.com/autos/mercado-usados-cuanto-sale-transferir-un-auto-hoy-la-argentina-n6289659)). En el primer semestre, 891.628 ventas de usados (informe de Kavak, vía [El Economista, 2026-08-25](https://eleconomista.com.ar/autos/cuales-son-preferencias-argentinos-elegir-auto-usado-n97671)).
- **No verificado:** qué parte de esas transferencias son **entre particulares** y cuál es el **precio promedio**. Ninguna fuente que vi separa particulares de concesionarias.
- **DATO — modalidad de fraude ("autos mellizos"):**
  - Dos ONG que encabeza el abogado Javier Miglino afirman que hay **más de 80.000 autos "mellizos"** en el país, la mayoría camionetas y pick-ups ([Sitio Andino, 2025-11-02](https://www.sitioandino.com.ar/policiales/autos-mellizos-la-trampa-que-ya-afecta-mas-80-mil-vehiculos-argentina-n5711182)). **No publican metodología**: tomar con pinzas.
  - Cómo funciona: roban el auto, le ponen la patente de otro igual, falsifican los papeles y lo venden en Marketplace u OLX. **La víctima paga antes de revisar** y la anomalía aparece recién en el Registro. Según Miglino, las ventas se pactan **en días y horarios con los registros cerrados**.
- **DATO — casos de seña sin entrega y estafas con pago adelantado:**
  - Neuquén: un grupo familiar pedía señas por autos publicados y no los entregaba ([LM Neuquén](https://www.lmneuquen.com/familia-gitanos-detenida-una-estafa-300-mil-n509132)).
  - Comprador que pagó USD 10.300 por un Scirocco que nunca recibió ([Río Negro](https://www.rionegro.com.ar/justicia/lo-acusan-de-estafar-por-37-000-dolares-y-42-000-pesos-con-la-venta-de-vehiculos-2220199/?amp=1)).
  - Fiat Argo comprado por Marketplace en USD 2.800 que resultó robado, San Juan, 2021 ([Diario de Cuyo](https://diariodecuyo.com.ar/policiales/Compro-un-auto-por-2-800-dolares-y-su-usado-era-robado-y-ahora-cayo-el-estafador-20210319-0028.html)).
- **DATO — dato regulatorio útil:** si el precio supera **$92.663.642**, se exige una declaración jurada de licitud de fondos (según [Canal 26, 2026-01-10](https://www.canal26.com/economia/2026/01/10/comprar-un-auto-usado-en-2026-cuanto-sale-la-transferencia-y-la-documentacion-obligatoria/); no lo verifiqué en la norma). La transferencia se inicia con una precarga online en la DNRPA y se termina en forma presencial ([iProfesional](https://www.iprofesional.com/autos/346333-guia-paso-a-paso-como-hacer-una-transferencia-digital)).

### 1.3 Marketplace, celulares y electrónica

- **DATO:** en Córdoba detuvieron a una banda que se hacía pasar por compradora en Marketplace y pagaba **celulares y computadoras con dólares falsos** ([La Voz](https://grupoclarin-la-voz-prod.cdn.arcpublishing.com/sucesos/desbaratan-una-banda-que-estafaba-vendedores-con-dolares-falsos-por-facebook-en-cordoba-tres-detenidos); la nota no muestra fecha).
- **DATO:** estafa del "te pagué de más": un supuesto comprador de un mueble manda un **comprobante falso** y después aparecen falsos empleados bancarios ([iProUP](https://www.iproup.com/economia-digital/48129-estafa-robo-cuenta-billetera-virtual-facebook)).
- **DATO:** a comienzos de 2024 mataron a un hombre en Wilde en un encuentro para comprar una moto por Marketplace (resumen de búsqueda; no abrí la nota original).
- **DATO:** en julio de 2025, un especialista de Jujuy dijo que crecen las denuncias por estafas en Marketplace. Es una afirmación sin número ([Todo Jujuy](https://www.todojujuy.com/jujuy/crecen-las-estafas-marketplace-y-la-clonacion-whatsapp-n276913)).
- **No encontré** una estadística de estafas en Marketplace separada del resto.

### 1.4 Entradas de recitales y partidos

- **DATO, casos 2025:**
  - Bahía Blanca: una influencer no entregó entradas para Argentina–Brasil y **más de 260 personas** la acusan de estafa ([Misiones Online, 2025-03-24](https://misionesonline.net/2025/03/24/escandalo-en-bahia-blanca-influencer/)).
  - Al menos 20 misioneros pagaron $510.000 y no pudieron entrar a Argentina–Venezuela porque sus entradas eran de reventa ([Misiones Online, 2025-09-05](https://misionesonline.net/2025/09/05/misioneros-estafados-partido-de-argenitna/)).
  - Detuvieron a la "Reina de la reventa" en CABA ([Los Andes, 2025-09-04](https://www.losandes.com.ar/policiales/cayo-la-reina-la-reventa-buenos-aires-ofrecia-entradas-la-despedida-messi-n5961751)).
- **DATO legal clave:** en CABA **la reventa con fines de lucro está prohibida** (es contravención) ([Chequeado](https://chequeado.com/el-explicador/el-escandalo-por-las-entradas-para-el-partido-de-despedida-de-lionel-messi-que-dice-la-ley-sobre-la-reventa-en-caba/)). Hay un proyecto de ley nacional para habilitar solo la reventa oficial (expediente [0932-D-2025](https://www4.hcdn.gob.ar/dependencias/dsecretaria/Periodo2025/PDF2025/TP2025/0932-D-2025.pdf)). **No verifiqué** si se aprobó.

### 1.5 Freelancers y exportadores de servicios que no cobran

- **No investigado** (se agotó el cupo de búsquedas). No tengo datos argentinos de impago a freelancers. Queda pendiente, y es justo el segmento que Facu mencionó primero.

---

## 2. Soluciones que existen hoy (Argentina y LATAM)

### 2.1 Mercado Libre / Mercado Pago — "Compra Protegida"

- **DATO:** cubre falta de entrega, producto distinto o con fallas, **solo para compras hechas dentro de Mercado Libre**. La página oficial de México: "El Programa cubre transacciones que se realizan dentro de la plataforma" ([Mercado Libre México](https://www.mercadolibre.com.mx/l/compra-seguro)).
- **DATO (Argentina):** los términos citados en un fallo de 2019 excluyen productos "no adquiridos a través de Mercado Libre o abonados a través de envíos o ingresos de dinero en Mercado Pago". El caso: un comprador de OLX señó por Mercado Pago, la venta se cayó y no le devolvieron la plata. La Cámara anuló la multa a Mercado Libre porque el mail que "prometía" protección era falso ([Diario Judicial, 2019-07-10](https://www.diariojudicial.com/news-83900-mercado-libre-de-incumplir-promesas); la página muestra "2026" en el encabezado, pero la nota es de 2019).
- **Consecuencia (OPINIÓN):** el hueco existe. **Una transferencia por Mercado Pago entre dos desconocidos de Marketplace no tiene ninguna protección.** Mercado Pago tiene la infraestructura para cerrarlo cuando quiera. En Brasil ya promociona su link de pago como protección para "comprador y vendedor" en ventas por redes, exigiendo código de seguimiento y aviso de recepción ([Mercado Pago Brasil](https://www.mercadopago.com.br/blog/link-pagamento-mercado-pago-seguranca-redes-sociais)). Si eso existe o va a existir en Argentina: **no verificado**.

### 2.2 Autos: los que hay son compradores, no intermediarios

| Quién | Qué hace | Estado | Fuente |
|---|---|---|---|
| **Kavak** | Compra y vende autos como concesionaria (no es escrow entre particulares) | **Activo en Argentina**: publicó un informe con datos propios del primer semestre de 2026 | [El Economista, 2026-08-25](https://eleconomista.com.ar/autos/cuales-son-preferencias-argentinos-elegir-auto-usado-n97671) |
| **OLX Autos** | Compraba autos a particulares con pago inmediato y bancarizado (2021) | **Cerró en Argentina**: dejó de tomar operaciones nuevas el 2023-06-14 | [Los Andes, 2021-09-24](https://www.losandes.com.ar/economia/como-entregar-tu-auto-y-recibir-de-inmediato-la-paga/), [iProUP](https://www.iproup.com/startups/40914-olx-autos-por-que-el-unicornio-se-fue-de-argentina) |
| **VendeTuAuto.com.ar** (Americas Car Group) | Venta "segura" con inspección, escribano y transferencia bancaria (2018-2019) | **Estado actual: no verificado** | [Autotest, 2019-02-13](https://autotest.com.ar/noticias/plataforma-para-evitar-el-fraude-en-la-venta-online-de-autos/) |

- **OPINIÓN:** el que vende a Kavak (y antes a OLX Autos) cambia seguridad por precio. En 2021, Los Andes mostraba que la cotización de OLX Autos estaba por debajo del precio entre particulares en Marketplace. **No encontré ningún servicio argentino que proteja el pago entre dos particulares** que se venden un auto entre ellos.

### 2.3 Cripto P2P (Binance y similares)

- **DATO:** el escrow de Binance P2P **retiene la cripto, no los pesos**. La transferencia en pesos ocurre fuera del sistema, y ahí aparecen los comprobantes falsos y los pagos desde cuentas de terceros ([Montevideo Portal](https://www.montevideo.com.uy/Negocios-y-Tendencias/Binance-aconseja--como-evitar-ser-victima-de-estafas-cripto--uc859500), [CriptoNoticias](https://www.criptonoticias.com/comunidad/aumenta-compraventa-cuentas-verificadas-binance-latinoamerica/)).
- **DATO:** Binance figura como PSAV registrado ante la CNV con el n.º 76 ([Finantres](https://finantres.mx/binance-argentina/); fuente secundaria).
- **OPINIÓN:** demuestra que los argentinos **ya entienden y usan el concepto de "plata retenida hasta que el otro cumple"**, pero solo para cripto.

### 2.4 Escribanías y depósito bancario en garantía

- **No verificado.** Por conocimiento general: el escribano suele hacer de depositario en operaciones grandes (inmuebles), y existe la figura del fideicomiso de garantía. No encontré fuentes sobre costos, ni sobre si los colegios de escribanos permiten retener fondos en compraventas chicas. **Pendiente: preguntarle a un escribano.**

### 2.5 LATAM: lo que apareció

| Quién | País | Qué hace | Lo verificado y lo no verificado | Fuente |
|---|---|---|---|---|
| **Kustodia** | México | Escrow por WhatsApp. El comprador paga en pesos a una referencia bancaria, se convierte a stablecoins y queda en un contrato inteligente hasta que se cumplen las condiciones. Arrancó con inmuebles y planea autos usados y servicios profesionales. En disputas, las partes suben pruebas (chats, documentos, fotos) y Kustodia decide | Fundada en 2021. Dice evitar "~90% de las disputas" con contratos claros (**dato de la empresa, no verificado**). Sin datos de volumen, licencias ni financiamiento. No dice que opere en Argentina | [El Observador, 2026-06-01](https://www.elobservador.com/argentina/economia-y-negocios/los-pagos-cripto-llegan-whatsapp-asi-funciona-la-startup-que-protege-transacciones-america-latina-n6045950), [Cointelegraph (publicidad paga)](https://cointelegraph.com/commissioned/after-losing-money-to-fraud-enterpreneur-builds-an-infrastructure-for-a-600m-problem) |
| **Pulga** | Chile | Marketplace de segunda mano con pago retenido. El comprador tiene 48 h para revisar antes de liberar. Envíos con Blue Express | Lanzada en marzo de 2026. Fundadores ex-Wallapop. Dice tener "más de 100.000 usuarios" en semanas (**dato de la empresa**). Comisión no publicada | [CNN Chile](https://www.cnnchile.com/pais/adios-a-las-estafas-en-compras-de-segunda-mano-app-chilena-promete-transacciones-online-mas-seguras/) |
| **CarroYa — "Transacción Segura"** | Colombia (Bogotá) | **Custodia la plata y también el auto**, en un estacionamiento propio, hasta que el auto queda a nombre del comprador. La comisión depende del precio del auto | Nota del 2026-09-23 que lo presenta como lanzamiento. Montos no publicados | [CarroYa](https://www.carroya.com/noticias/noticias-y-lanzamientos/compra-y-venta-segura?amp=1) |
| **Webmotors — Autopago** | Brasil | Billetera: el comprador deposita y el vendedor cobra recién después de la transferencia de documentos. Incluía una revisión de 250 ítems y garantía de que el auto no era robado | Lanzado en 2018. La meta era que el 60% de las operaciones entre particulares de la plataforma pasaran por ahí en 2 años. **Si lo logró o sigue activo: no verificado** | [IstoÉ Dinheiro, 2018-10-08](https://istoedinheiro.com.br/webmotors-cria-plataforma-de-pagamento-especializada-em-carros) |
| **Contran, Resolución 1.027** | Brasil | **El Estado crea la "transferencia electrónica custodiada" de autos entre particulares**: el pago queda retenido hasta completar la transferencia, con reversión si se traba | Aprobada en agosto de 2026. **Todavía no funciona** en la app CNH do Brasil y no tiene fecha | [AutoPapo, 2026-08-24](https://autopapo.com.br/curta/transferencia-de-carro-usado-podera-ser-feita-pelo-celular-sem-cartorio-e-com-dinheiro-sob-custodia/) |

**OPINIÓN — esto es lo más importante de la sección:**
1. En 2026, en tres países de la región (Colombia, Brasil, Chile) aparecieron soluciones de "pago custodiado" para compraventas entre particulares. **En autos, el mecanismo que se repite es liberar la plata cuando el registro confirma la transferencia.** Es la señal de demanda más fuerte que encontré.
2. Brasil muestra el riesgo mayor: **el Estado puede meter el escrow adentro del trámite registral** y dejar sin negocio a los privados. En Argentina, la DNRPA ya digitalizó parte del trámite (Legajo Digital Único y Certificado Digital Automotor, 2024). Que copie el modelo brasileño es una posibilidad, no un dato.

---

## 3. Escrow en nichos que funcionaron (y que fracasaron) en el mundo

### 3.1 El escrow "genérico" es un negocio chico y maduro

**DATO — Escrow.com, ejercicio 2025** (lo reporta su dueña, Freelancer Ltd.) ([Domain Name Wire, 2026-02-25](https://domainnamewire.com/2026/02/25/escrow-com-reports-record-revenue-but-payments-fall/)):
- Ingresos: **A$12,3 M** (récord, +18,8%).
- Ganancia antes de impuestos: **A$3,1 M**.
- Volumen de pagos: **−8,6%**, cuarto año seguido de caída desde el pico de 2021 (sigue arriba de antes de la pandemia). Un resumen de búsqueda habla de 748,1 M de volumen anual, pero **no lo confirmé en la fuente primaria** (no se sabe la moneda).
- Mejor trimestre: el cuarto, con USD 102,5 M solo en dominios.
- Subieron los ingresos con menos volumen porque **cobra un porcentaje más alto** por operación. Esto lo vi en el resumen de búsqueda de los resultados de Freelancer; no abrí el documento original, así que tomarlo como fuente secundaria ([anuncio de Freelancer, PDF](https://bulletin.webull.com/qbd/announcement/20260225/499502567/3f5e11865579313550ceb604920d9a0c.pdf), [Edison Research](https://www.edisongroup.com/research/operational-improvements-boost-profits/BM-2914/)).

**OPINIÓN:** el líder mundial, con 26 años y licencias en EE.UU., factura unos A$12 M por año. Su fuerte son los dominios: activos digitales de ticket alto, que se pueden verificar al instante (el dominio cambia de dueño o no). **El escrow solo, sin un nicho, no es "algo grande".**

### 3.2 Los que se vendieron o crecieron estaban metidos en un nicho

| Caso | Nicho | Resultado | Fuente |
|---|---|---|---|
| **Caramel** (EE.UU., 2021) | "Checkout" para venta de autos entre particulares: verificación de identidad, papeles, transferencia del título, pago, seguro | Levantó unos USD 19 M al lanzar y una Serie A de USD 21,3 M (2024). **Lo compró eBay en enero de 2025** (precio no informado) | [TechCrunch, 2025-01-13](https://techcrunch.com/2025/01/13/ebay-acquires-caramel-to-reduce-risk-and-complexity-of-online-car-sales) |
| **PrivateAuto** (EE.UU., 2020) | Autos entre particulares: identidad, firma electrónica y pago, pensado para no necesitar un escrow aparte | Sin datos verificados | [CB Insights](https://www.cbinsights.com/compare/caramel-vs-privateauto) |
| **Trustap** (Irlanda) | Escrow para marketplaces. Con DoneDeal (el mayor sitio de autos de Irlanda) lanzó "Reserve Online": seña reembolsable desde €149 que reserva el auto hasta 5 días, **apuntado a concesionarias** | Según un perfil secundario, el volumen del primer semestre de 2025 creció 370% interanual (no lo confirmé en una fuente de la empresa). En su documentación, un ejemplo cobra USD 10,50 al comprador por una operación de USD 200 (≈5,25%: **inferencia de un solo ejemplo**) | [UCC Ignite](https://www.ucc.ie/en/ignite/news/ignite-alumnus-trustap-partners-with-donedeal.html), [yespress](https://yespress.io/conor-lyden), [docs Trustap](https://docs.trustap.com/docs/concepts/pricing) |
| **Alibaba Trade Assurance** | Importaciones B2B: el pago queda retenido hasta que el comprador confirma la recepción. Reembolso si no se envía, se pierde o llega con defectos. Alibaba media | Comisiones no publicadas en la página | [Alibaba](https://tradeassurance.alibaba.com/) |
| **eBay Authenticity Guarantee** | Zapatillas, carteras, relojes, joyas, cartas coleccionables, monedas: **autenticadores revisan el objeto antes de que llegue al comprador** | Costo no publicado en la página | [eBay](https://www.ebay.com/authenticity-guarantee) |

**OPINIÓN:** el patrón es claro. **El escrow funciona como función adentro de un nicho o de un marketplace, no como producto suelto.** Caramel no "vendía escrow": vendía "cerrar la venta de un auto sin miedo" (identidad + papeles + pago). Por eso lo compró un marketplace.

### 3.3 Los que cerraron (para aprender barato)

- **Payoneer Escrow** (ex Armor Payments): cerrado en 2018, ver punto 0.
- **Shypp.it** (Alemania): plataforma de envíos colaborativos que cerró a los ~15 meses porque cumplir la ley bancaria por retener plata de terceros en escrow era "caro" y con mucha carga de reportes ([ShareTraveler](https://sharetraveler.com/shypp-shut-legal-perils-crowdsourced-delivery/)).
- **OpenBazaar** (marketplace con escrow multifirma): cerró por baja adopción y falta de fondos ([Bitcoin World](https://bitcoinworld.co.in/openbazaar-decentralized-marketplace-shutdown/)).
- **LocalBitcoins** (P2P cripto con escrow): cerró en febrero de 2023, después de años bajo exigencias estrictas de identidad y antilavado y de la caída del mercado cripto. Los estafadores atacaban a los usuarios que **salían del escrow para ahorrarse la comisión** ([Traders Union](https://tradersunion.com/brokers/crypto/view/localbitcoins/); fuente de baja autoridad).
- **OPINIÓN:** las cuatro causas de muerte que se repiten son la regulación por tener plata de terceros, la poca adopción, la falta de escala (márgenes finos) y que los usuarios esquiven el sistema. Las cuatro aplican a una versión argentina.

### 3.4 Entradas

- **No investigado a fondo** (cupo agotado). Única referencia: para el Mundial 2026, la FIFA tiene su propia plataforma oficial de reventa e intercambio (resumen de búsqueda, no abrí la fuente primaria).
- **OPINIÓN:** en Argentina, un escrow para reventa de entradas **facilitaría una actividad prohibida en CABA**. Queda descartado como nicho.

---

## 4. Resolución de disputas: la respuesta a "la caja llega perfecta pero vacía"

| Mecanismo | Quién lo usa | Cómo resuelve la caja vacía | Fuente |
|---|---|---|---|
| **1. Liberar con un evento objetivo de un tercero** (el registro confirma la transferencia) | CarroYa, Contran (Brasil), Webmotors Autopago, Caramel | No hay "caja": el bien es registrable y el registro hace de juez | Ver 2.5 y 3.2 |
| **2. Custodia física del bien** | CarroYa (guarda el auto en su estacionamiento) | El intermediario tiene el bien y la plata a la vez | [CarroYa](https://www.carroya.com/noticias/noticias-y-lanzamientos/compra-y-venta-segura?amp=1) |
| **3. Inspección por un tercero antes de la entrega** | eBay Authenticity Guarantee, Webmotors (250 ítems) | Un tercero abre la caja, no el comprador | [eBay](https://www.ebay.com/authenticity-guarantee) |
| **4. Período de inspección + devolución + arbitraje externo** | Escrow.com | El comprador rechaza y devuelve. Si el vendedor rechaza la devolución: 14 días de negociación y después arbitraje con un tercero. **Escrow.com no juzga** | Ficha 2026-10-07 |
| **5. Prueba de entrega con seguimiento** | Mercado Pago Brasil (protección al vendedor) | El vendedor demuestra el envío y la recepción, pero **no prueba el contenido** | [Mercado Pago Brasil](https://www.mercadopago.com.br/blog/link-pagamento-mercado-pago-seguranca-redes-sociais) |
| **6. Decisión de la plataforma con pruebas** (chats, fotos, video) | Kustodia, Alibaba (mediación) | Alguien decide y asume el costo de equivocarse | Ver 2.5 y 3.2 |
| **7. Ventana corta para revisar** | Pulga (48 h), Trustap (entrega + 24 h, ficha anterior) | Se limita el tiempo para reclamar | Ver 2.5 |

**OPINIÓN, la conclusión práctica:** la caja vacía es un problema de **envíos a distancia de cosas que no se pueden verificar a distancia**. No hay mecanismo barato que lo resuelva del todo. Por eso Escrow.com lo deriva a árbitros y Alibaba media. **La mejor respuesta es elegir nichos donde no haya caja:**
- entrega **en persona** (el comprador revisa en el momento y libera con un botón);
- o entrega **registrable** (auto, moto, dominio, inmueble).

Así el "juez" es un hecho objetivo y no la palabra de una de las partes. El video de apertura del paquete es una costumbre que recomiendan foros y blogs. **No encontré una plataforma que lo use como prueba formal**: es una práctica, no un estándar.

---

## 5. Los 2-3 nichos argentinos más prometedores

Criterios: transacción entre desconocidos, ticket medio-alto, entrega verificable, sin buena solución hoy.

| Nicho | Desconocidos | Ticket | Verificable | Solución hoy | Resultado |
|---|---|---|---|---|---|
| **A. Autos y motos usados entre particulares** | Sí | Alto | **Sí (registro)** | Ninguna para particulares (solo venderle a Kavak, más barato) | **1.º** |
| **B. Alquileres temporarios contratados directo** (Instagram, WhatsApp, Marketplace) | Sí | Medio | Sí (check-in) | Airbnb/Booking dentro de su plataforma; fuera, nada | **2.º** |
| **C. Electrónica de alto valor entregada en mano** (iPhone, notebooks, consolas) | Sí | Medio | Sí (en persona) + IMEI | Nada fuera de Mercado Libre | **3.º** |
| Freelancers con clientes del exterior | Sí | Medio-alto | **Subjetivo** | Upwork (10%), Escrow.com | Sin datos (no investigado); servicios = disputas subjetivas |
| Entradas | Sí | Medio | Difícil (QR duplicable) | Reventa oficial | **Descartado** (ilegal en CABA) |

### Nicho A — "Cierre seguro" de autos usados entre particulares

- **Tamaño:**
  - **DATO:** 1.887.024 transferencias de usados en 2025.
  - **ESTIMACIÓN (supuestos sin fuente argentina):** si entre el 30% y el 50% fueran entre particulares, serían **566.000 a 944.000 operaciones por año**. El único dato comparable que encontré: en Webmotors (Brasil, 2018), el 35-40% de las operaciones eran entre particulares, pero es de otro país y de una sola plataforma.
  - **ESTIMACIÓN de ingresos** (comisión supuesta de USD 100 por operación):

    | Adopción | Operaciones por año | Ingresos por año |
    |---|---|---|
    | 0,1% | 570-940 | USD 57.000-94.000 |
    | 1% | 5.700-9.400 | USD 566.000-944.000 |

  - **OPINIÓN:** llegar al 1% de un mercado tan fragmentado es muy ambicioso y llevaría años.
- **Quién paga:** el que más riesgo corre al pagar primero, el **comprador** (seña perdida, auto mellizo, deudas). El **vendedor** también gana algo: se cuida de billetes falsos y comprobantes falsos, y vende más rápido. Hipótesis a validar: **comisión compartida o a cargo del comprador.**
- **Producto (hipótesis):**
  1. **"Seña protegida":** la seña queda retenida hasta que el comprador ve el auto y sale bien el informe de dominio.
  2. **Verificación previa:** informe de dominio, chequeo de titular, verificación policial.
  3. **Pago coordinado el día de la firma:** la plata se libera cuando la transferencia entra al registro.

  Es lo mismo que hacen CarroYa, Caramel y la custodiada brasileña.
- **Riesgos:**
  - Regulación (retener plata).
  - **Pagos en dólares billete.** Que en Argentina los usados se paguen mucho en efectivo es **conocimiento general, no verificado**; si es así, cuesta meter la plata en un sistema.
  - Responsabilidad si el auto resulta robado.
  - Que entre el Estado (caso Brasil), Mercado Libre o Kavak.

### Nicho B — Seña protegida para alquileres temporarios directos

- **Tamaño:** **DATO:** 488 reportes de fraude con alquileres temporarios en 2024 (UFECI), el 51% en el primer trimestre (temporada de verano). Monto por operación y cantidad de alquileres directos: **no lo sé**.
- **Quién paga:** el inquilino (paga por adelantado a un desconocido). El dueño podría pagar para "verse confiable" y no pagarle la comisión a Airbnb (cuánto es esa comisión: **no verificado hoy**).
- **Producto:** la seña queda retenida y se libera al dueño en el check-in o 24 h después (como Trustap). Más verificación del dueño (identidad y que la propiedad sea suya).
- **Contras (OPINIÓN):** es muy estacional, Airbnb/Booking ya lo resuelven adentro de su plataforma, y el que alquila directo muchas veces lo hace justamente para no pagar comisión.

### Nicho C — Pago verificado para encuentros en persona (electrónica)

- **Dolor:** billetes falsos, comprobantes falsos, equipos robados o bloqueados (ver 1.3).
- **Producto:**
  1. El comprador deposita antes del encuentro.
  2. El vendedor ve que los "fondos están asegurados" (no hay captura de pantalla que se pueda falsificar).
  3. Se chequea el IMEI.
  4. En el encuentro, el comprador revisa y libera con un toque.

  **Resuelve muy bien la caja vacía**, porque no hay caja.
- **Contras (OPINIÓN):** el ticket es bajo (ESTIMACIÓN: USD 300-1.500 por equipo), así que la comisión es chica (unos pocos dólares). Hace falta volumen masivo, que es una app de consumo con un costo de captar usuarios muy alto. Y Mercado Pago lo podría lanzar en una semana.

---

## 6. Cómo operar sin licencia propia (no es asesoramiento legal)

| Opción | Cómo sería | Lo que hay que verificar |
|---|---|---|
| **1. No tocar la plata** (modelo "coordinador") | La empresa verifica (identidad, dominio, IMEI), arma el contrato y coordina que el pago y la entrega pasen **en el mismo momento** (por ejemplo, transferencia inmediata en el registro, delante de las dos partes). Cobra por el servicio, no custodia fondos | Si eso queda fuera del régimen de PSP. Responsabilidad si falla la verificación. Contrato tipo de mandato o servicio |
| **2. Encima de un escrow licenciado** | API de Escrow.com (ficha anterior: "desde 0,89%", Argentina no está en su lista de países excluidos) | Funciona en USD con transferencias internacionales (USD 25). **No sirve para operaciones en pesos dentro de Argentina** (OPINIÓN) |
| **3. Encima de un PSP o banco local** con pagos retenidos o liberación diferida | Usar la función de marketplace o de split de un procesador local | Si Mercado Pago u otros PSP argentinos permiten retener y liberar por evento, y en qué condiciones: **no verificado** |
| **4. Escribano como depositario** | El escribano retiene la plata y la libera cuando se firma o inscribe | Si es viable y cuánto cuesta en operaciones de USD 5.000-20.000: **no verificado** |
| **5. Fideicomiso de garantía** con un fiduciario profesional | Figura del Código Civil y Comercial | Costo y viabilidad para tickets chicos: **no verificado** (OPINIÓN: probablemente caro) |
| **6. Registro propio como PSP** ante el BCRA | Ver ficha anterior (Com. "A" 6859: fondos en cuentas a la vista en bancos locales, régimen sancionatorio) | Requisitos actuales, capital, plazos. Es para la etapa 2 |

**Preguntas para el abogado** (todas a verificar; algunas salen de conocimiento general, no de fuentes de hoy):
1. Retener plata de terceros aunque sea por horas, ¿es actividad de PSP? ¿Puede considerarse intermediación financiera (Ley de Entidades Financieras 21.526)?
2. ¿La empresa pasa a ser **sujeto obligado ante la UIF** (Ley 25.246)? ¿Qué exige?
3. **Defensa del consumidor (Ley 24.240):** ¿qué responsabilidad hay si el auto verificado resulta robado o mellizo? Mercado Libre tuvo fallos en contra por falta de entrega ([iProfesional](https://www.iprofesional.com/legales/438359-fallo-justicia-argentino-contra-mercado-libre-por-no-entregar-2-aires-acondicionados)).
4. **Datos personales (Ley 25.326):** ¿qué se exige para guardar DNI y selfies de verificación?
5. Impuestos: IVA sobre la comisión, límites del monotributo, impuesto al cheque si la plata pasa por una cuenta propia.
6. Contrato modelo entre las partes y con la empresa (mandato, servicio, cláusula de arbitraje).
7. Operaciones en dólares billete: ¿se pueden canalizar y cómo?

---

## 7. MVP y costos (todo ESTIMACIÓN, sin cotizar)

| Etapa | Qué es | Costo estimado | Factible para Facu |
|---|---|---|---|
| **MVP 0 — servicio a mano, sin custodia** (opción 1) | Página web simple + WhatsApp Business + formulario + contrato modelo + checklist de verificación (informe de dominio, titular, verificación policial) + acompañar la firma | USD 0-50 de herramientas + consulta legal (**costo desconocido**; buscar consultorios jurídicos gratuitos de la facultad o del colegio de abogados: existencia **no verificada**) + aranceles oficiales que paga el cliente | **Sí**: diseño de procesos de ingeniero industrial, sin programar |
| **MVP 1 — con custodia vía un socio** (escribano, PSP o banco) | Integrar el socio, panel simple hecho por amigos programadores o no-code, verificación de identidad tercerizada | USD 2.000-10.000 entre legal e integración (**ESTIMACIÓN muy gruesa**) | Solo con socio o con inversión |
| **Producto propio con licencia** | Registro PSP, oficial de cumplimiento, antifraude, capital | USD 50.000-200.000+ (**ESTIMACIÓN sin fuente**; es solo el orden de magnitud) | No en la etapa 1 |

---

## 8. Cómo validar en 2-4 semanas con menos de USD 200 (nicho A)

**Semana 1 — entrevistas (USD 0):**
- 15-20 personas que **compraron o vendieron un auto usado a un particular en los últimos 12 meses** (familia, amigos, grupos de compraventa de autos en Facebook).
- 3-5 actores del medio: un gestor, un empleado de registro, un escribano.
- Método Mom Test, preguntando por hechos:
  - ¿Cómo pagaste? ¿Efectivo, dólares, transferencia? ¿Dónde?
  - ¿Cuál fue el peor momento?
  - ¿Pagaste seña sin ver el auto?
  - ¿Pagaste a alguien para que te ayude (gestor, mecánico, escribano)? ¿Cuánto?
- **Gate 1:** si menos de 6 de 20 cuentan un miedo concreto que les cambió la conducta, o una pérdida real, o que pagaron por protegerse → **cortar o cambiar de nicho** (probar el B o el C con el mismo método).

**Semana 2 — demanda (USD 80-120):**
- Página simple "Cierre seguro de autos usados entre particulares" con **precio visible** (por ejemplo, el equivalente a USD 50-80 por operación; a ajustar con las entrevistas) y botón de WhatsApp.
- Publicaciones en 10-20 grupos de compraventa más USD 80-100 de anuncios en Meta, segmentados.
- Medir: visitas, conversaciones por WhatsApp, personas que **reservan con un pago** (la mejor señal).

**Semanas 3-4 — prueba a mano (USD 30-50 de viáticos):**
- Hacer 1-3 operaciones reales con el MVP 0 (sin custodiar plata): verificar, armar el contrato, acompañar la firma y el pago simultáneo.
- Medir horas, costos, qué falló y si el cliente lo recomendaría.
- **Gate 2:** 0 operaciones pagas en 4 semanas, o menos de 1 de cada 3 conversaciones dispuesta a pagar → **cerrar el experimento y escribir el post-mortem.**

**Antes de cobrar:** una consulta legal sobre la opción 1. **Nunca recibir plata de terceros en una cuenta propia durante la validación.**

**Pérdida máxima:** USD 200 más unas 40-60 horas (ESTIMACIÓN).

---

## 9. Veredicto (OPINIÓN)

| Criterio | Puntaje | Por qué |
|---|---|---|
| Tamaño del problema | **7** | ~12.170 reportes de estafas en compraventas online en 2024 (UFECI) y 1,89 M de autos transferidos en 2025. Falta saber cuánta plata se pierde. |
| Disposición a pagar | **4** | Sin datos argentinos. El líder mundial factura solo A$12,3 M y la gente esquiva las comisiones (LocalBitcoins). Hay que demostrarla. |
| Espacio frente a la competencia | **6** | No encontré escrow entre particulares en Argentina. Pero Mercado Pago, Kavak o el Estado (como en Brasil) pueden entrar rápido. |
| Ventaja de Facu | **3** | No tiene contactos en autos, ni experiencia en fintech, ni socio legal. Su formación en procesos ayuda en el servicio a mano, pero no es una ventaja injusta. |
| Factibilidad con sus recursos | **4** | El servicio a mano sí (7). La custodia de fondos no (2). |
| Escalabilidad | **5** | El servicio a mano no escala. Con licencia y un nicho de autos podría ir a LATAM (Caramel terminó vendida a eBay). |
| Riesgo (10 = bajo) | **3** | Regulación, imán de fraude, responsabilidad si el auto es robado, juicios de consumo y competencia estatal. |

**Opinión:** el escrow "para todo" no es buena idea: el líder mundial factura poco, Payoneer cerró el suyo y los que ganaron se metieron en un solo nicho. La versión que vale la pena testear es un **"cierre seguro de autos usados entre particulares"**, donde el registro hace de juez y no hay caja vacía posible. Como empresa de la etapa 1 **no conviene custodiar plata**. En cambio, sí se puede validar en 4 semanas con menos de USD 200 como servicio a mano de verificación y cierre coordinado. Aunque falle, enseña cosas útiles para la etapa 2: una industria por dentro (autos, registros, gestores), vender confianza y el marco legal de pagos. Si las entrevistas muestran que la gente paga en dólares billete y no quiere intermediarios, hay que cortar rápido y probar el nicho B o C. Mi duda principal: que en Argentina la desconfianza se resuelva "a la argentina" (encontrarse en el registro con la plata en mano) y que nadie quiera pagar por algo que ya hace gratis. Eso es lo primero que tienen que contestar las entrevistas.

---

## Fuentes (consultadas el 2026-10-08)

**Datos de fraude y mercado en Argentina**
- UFECI / MPF, informe anual 2024 (publicado 2025-06-30): https://www.fiscales.gob.ar/ciberdelincuencia/la-unidad-fiscal-especializada-en-ciberdelincuencia-informa-que-en-2024-se-registro-un-aumento-interanual-del-211-en-la-cantidad-de-reportes-de-delitos-informaticos/ — PDF: https://www.fiscales.gob.ar/wp-content/uploads/2025/06/UFECI_informe_anual_2024.pdf
- Chequeado, denuncias +21% en 2024 (2025-07-04): https://chequeado.com/el-explicador/las-denuncias-de-estafas-virtuales-aumentaron-un-21-en-2024-cuales-son-los-tipos-de-fraude-mas-comunes/
- Chequeado, estafas de 2025 (2025-12-31): https://chequeado.com/nota/las-estafas-con-las-que-intentaron-enganarnos-en-2025
- Diario de Cuyo, San Juan 3.713 denuncias en 2025 (2026-01-25): https://www.diariodecuyo.com.ar/sanjuan/san-juan-registro-mas-de-3-700-denuncias-por-estafas-y-delitos-informaticos-en-2025-pornografia-infantil-y-el-grooming-con-numeros-que-preocupan-1821952.html
- El Economista, récord de usados 2025 (2026-01-12): https://eleconomista.com.ar/autos/la-venta-autos-usados-alcanzo-su-record-historico-2025-n91863
- Ámbito, transferencias enero-mayo 2026 (2026-06-17): https://www.ambito.com/autos/mercado-usados-cuanto-sale-transferir-un-auto-hoy-la-argentina-n6289659
- El Economista, informe de Kavak del primer semestre de 2026 (2026-08-25): https://eleconomista.com.ar/autos/cuales-son-preferencias-argentinos-elegir-auto-usado-n97671
- Sitio Andino, autos mellizos (2025-11-02): https://www.sitioandino.com.ar/policiales/autos-mellizos-la-trampa-que-ya-afecta-mas-80-mil-vehiculos-argentina-n5711182
- Cadena 3, autos mellizos: https://www.cadena3.com/noticia/sociedad/denuncian-que-en-la-argentina-hay-mas-de-80-mil-autos-mellizos_481156
- LM Neuquén, estafa con señas de autos (sin fecha visible): https://www.lmneuquen.com/familia-gitanos-detenida-una-estafa-300-mil-n509132
- Río Negro, estafa por USD 37.000 con autos: https://www.rionegro.com.ar/justicia/lo-acusan-de-estafar-por-37-000-dolares-y-42-000-pesos-con-la-venta-de-vehiculos-2220199/?amp=1
- Diario de Cuyo, auto robado comprado por Marketplace (2021-03-19): https://diariodecuyo.com.ar/policiales/Compro-un-auto-por-2-800-dolares-y-su-usado-era-robado-y-ahora-cayo-el-estafador-20210319-0028.html
- Canal 26, transferencia y licitud de fondos (2026-01-10): https://www.canal26.com/economia/2026/01/10/comprar-un-auto-usado-en-2026-cuanto-sale-la-transferencia-y-la-documentacion-obligatoria/
- iProfesional, transferencia digital: https://www.iprofesional.com/autos/346333-guia-paso-a-paso-como-hacer-una-transferencia-digital
- La Voz, banda de dólares falsos en Marketplace: https://grupoclarin-la-voz-prod.cdn.arcpublishing.com/sucesos/desbaratan-una-banda-que-estafaba-vendedores-con-dolares-falsos-por-facebook-en-cordoba-tres-detenidos
- iProUP, estafa del comprobante y robo de billetera: https://www.iproup.com/economia-digital/48129-estafa-robo-cuenta-billetera-virtual-facebook
- Todo Jujuy, estafas en Marketplace: https://www.todojujuy.com/jujuy/crecen-las-estafas-marketplace-y-la-clonacion-whatsapp-n276913
- Misiones Online, influencer de Bahía Blanca (2025-03-24): https://misionesonline.net/2025/03/24/escandalo-en-bahia-blanca-influencer/
- Misiones Online, estafados en Argentina–Venezuela (2025-09-05): https://misionesonline.net/2025/09/05/misioneros-estafados-partido-de-argenitna/
- Los Andes, "Reina de la reventa" (2025-09-04): https://www.losandes.com.ar/policiales/cayo-la-reina-la-reventa-buenos-aires-ofrecia-entradas-la-despedida-messi-n5961751
- Chequeado, reventa en CABA: https://chequeado.com/el-explicador/el-escandalo-por-las-entradas-para-el-partido-de-despedida-de-lionel-messi-que-dice-la-ley-sobre-la-reventa-en-caba/
- HCDN, proyecto 0932-D-2025: https://www4.hcdn.gob.ar/dependencias/dsecretaria/Periodo2025/PDF2025/TP2025/0932-D-2025.pdf

**Soluciones existentes en Argentina**
- Mercado Libre México, Compra Protegida: https://www.mercadolibre.com.mx/l/compra-seguro
- Diario Judicial, fallo Compra Protegida/OLX (2019-07-10): https://www.diariojudicial.com/news-83900-mercado-libre-de-incumplir-promesas
- iProfesional, fallo contra Mercado Libre por falta de entrega: https://www.iprofesional.com/legales/438359-fallo-justicia-argentino-contra-mercado-libre-por-no-entregar-2-aires-acondicionados
- Mercado Pago Brasil, link de pago en redes: https://www.mercadopago.com.br/blog/link-pagamento-mercado-pago-seguranca-redes-sociais
- Los Andes, OLX Autos (2021-09-24): https://www.losandes.com.ar/economia/como-entregar-tu-auto-y-recibir-de-inmediato-la-paga/
- iProUP, salida de OLX Autos: https://www.iproup.com/startups/40914-olx-autos-por-que-el-unicornio-se-fue-de-argentina
- Autotest, VendeTuAuto (2019-02-13): https://autotest.com.ar/noticias/plataforma-para-evitar-el-fraude-en-la-venta-online-de-autos/
- Montevideo Portal, estafas en Binance: https://www.montevideo.com.uy/Negocios-y-Tendencias/Binance-aconseja--como-evitar-ser-victima-de-estafas-cripto--uc859500
- CriptoNoticias, compraventa de cuentas verificadas de Binance: https://www.criptonoticias.com/comunidad/aumenta-compraventa-cuentas-verificadas-binance-latinoamerica/
- Finantres, Binance en Argentina (PSAV CNV n.º 76): https://finantres.mx/binance-argentina/

**LATAM**
- El Observador, Kustodia (2026-06-01): https://www.elobservador.com/argentina/economia-y-negocios/los-pagos-cripto-llegan-whatsapp-asi-funciona-la-startup-que-protege-transacciones-america-latina-n6045950
- Cointelegraph, Kustodia (contenido pago): https://cointelegraph.com/commissioned/after-losing-money-to-fraud-enterpreneur-builds-an-infrastructure-for-a-600m-problem
- CNN Chile, Pulga: https://www.cnnchile.com/pais/adios-a-las-estafas-en-compras-de-segunda-mano-app-chilena-promete-transacciones-online-mas-seguras/
- CarroYa, Transacción Segura (2026-09-23): https://www.carroya.com/noticias/noticias-y-lanzamientos/compra-y-venta-segura?amp=1
- IstoÉ Dinheiro, Webmotors Autopago (2018-10-08): https://istoedinheiro.com.br/webmotors-cria-plataforma-de-pagamento-especializada-em-carros
- AutoPapo, Contran Res. 1.027 (2026-08-24): https://autopapo.com.br/curta/transferencia-de-carro-usado-podera-ser-feita-pelo-celular-sem-cartorio-e-com-dinheiro-sob-custodia/

**Internacional**
- Domain Name Wire, resultados 2025 de Escrow.com (2026-02-25): https://domainnamewire.com/2026/02/25/escrow-com-reports-record-revenue-but-payments-fall/
- Edison Research, Freelancer Ltd.: https://www.edisongroup.com/research/operational-improvements-boost-profits/BM-2914/
- Domain Name Wire, Payoneer sale del escrow (2018-07-10): https://domainnamewire.com/2018/07/10/payoneer-exits-the-escrow-business/
- DomainInvesting, Payoneer: https://domaininvesting.com/payoneer-exiting-domain-escrow-business/
- PYMNTS, Payoneer: https://www.pymnts.com/?p=523413
- TechCrunch, eBay compra Caramel (2025-01-13): https://techcrunch.com/2025/01/13/ebay-acquires-caramel-to-reduce-risk-and-complexity-of-online-car-sales
- CB Insights, Caramel vs PrivateAuto: https://www.cbinsights.com/compare/caramel-vs-privateauto
- UCC Ignite, Trustap + DoneDeal: https://www.ucc.ie/en/ignite/news/ignite-alumnus-trustap-partners-with-donedeal.html
- yespress, perfil del fundador de Trustap: https://yespress.io/conor-lyden
- Trustap, documentación de precios: https://docs.trustap.com/docs/concepts/pricing
- Alibaba Trade Assurance: https://tradeassurance.alibaba.com/
- eBay Authenticity Guarantee: https://www.ebay.com/authenticity-guarantee
- ShareTraveler, cierre de Shypp.it: https://sharetraveler.com/shypp-shut-legal-perils-crowdsourced-delivery/
- Bitcoin World, cierre de OpenBazaar: https://bitcoinworld.co.in/openbazaar-decentralized-marketplace-shutdown/
- Traders Union, LocalBitcoins: https://tradersunion.com/brokers/crypto/view/localbitcoins/
