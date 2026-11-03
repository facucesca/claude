# Ideas rápidas (primer cobro ≤ 7 días): comercio, reventa y arbitraje en Argentina

- **Fecha:** 2026-10-01
- **Frente:** comercio, reventa, consignación, mayorista/preventa, subastas, logística de barrio.
- **Pedido:** ver el primer dólar en ≤ 7 días (hasta 2026-10-08), aunque cueste mucho esfuerzo. Capital disponible: menos de USD 300-500.
- **Perfil considerado:** no programa, usa Claude a diario, formación en ingeniería industrial (logística/stock), tiene Higgsfield, cobra con Mercado Pago, efectivo y transferencia.
- **Tipo de cambio de referencia:** USD 1 = ARS 1.545 (dólar oficial venta, [dolarapi.com](https://dolarapi.com/v1/dolares), 2026-10-01 18:00 UTC; blue $1.555). Todas las conversiones usan ese valor.
- **No repite:** las ideas de la sección 4 de `research/2026-10-01-230-ideas-con-claude.md`. Hay dos solapamientos parciales y los marco (fotos de producto = E5; logística para vendedores de ML = C4). Acá van en su versión "cobro inmediato, presencial, sin software".

---

## 0. Metodología y limitaciones

1. **Búsquedas:** 34 consultas a WebSearch (la cuota de la sesión se agotó en la consulta 35) + 8 WebFetch a fuentes primarias. Mercado Libre bloquea el fetch automático (HTTP 403) de sus listados y de su ayuda, así que **los precios de usados de ML/Marketplace no pude verificarlos uno por uno**. Los precios de nuevos salen de agregadores que leen ML (mejorescompras.com.ar, 2026-07-18) y de Frávega.
2. **[NO VERIFICADO]:** marca todo número que estimé yo (precios de usados, márgenes por pieza, volúmenes semanales). Antes de comprar nada, el paso 1 de cada plan es **verificar 20 avisos reales** del producto en Marketplace y en ML (filtro "Usado").
3. **Números:** uso medianas y rangos para alguien **sin reputación previa, sin vehículo propio garantizado y en AMBA**. Los "ingresos por semana" son **ganancia bruta** (precio de venta menos costo de compra, menos comisiones y fletes). No descuentan su tiempo ni el monotributo.
4. **"Primer cobro"** = el primer peso que entra a su cuenta o a su mano **como ganancia o seña de un cliente**. Cuando lo que entra es solo una seña (no ganancia), lo aclaro.
5. **Sesgo que hay que tener en cuenta:** el contenido sobre "flipping" en redes está dominado por casos de éxito. La mayoría de los que empiezan venden 0-2 piezas la primera semana. Mis medianas lo reflejan.

### Datos base verificados (con fuente y fecha)

| Dato | Valor | Fuente |
|---|---|---|
| Comisión ML clásica | 11,8% (Supermercado) a 15% (Electrónica); premium 14,8% a 17,14% | [algoritmodigital / iProfesional](https://www.iprofesional.com/negocios/419524-como-calculo-a-cuanto-vender-productos-mercado-libre-para-no-perder-dinero) (2026) |
| IVA sobre comisión ML | 21% sobre comisión + costo fijo + cargo por cuotas | idem |
| Costo fijo ML (productos < $33.000) | desde $1.330 (≤ $14.999, ≤ 0,3 kg) en adelante; tablas de agosto: ~$1.115 / $2.300 / $2.810 por tramo | [NoticiasNQN 2026-09-10](https://www.noticiasnqn.com.ar/noticias/2026/09/10/352025-mercado-libre-cambia-una-de-sus-condiciones-y-desde-el-lunes-habra-envios-gratis-desde-15000), [jaguarsheet](https://jaguarsheet.com/es/blog/costo-fijo-mercado-libre) |
| Cambio 2026-09-01 | Subió el costo de ofrecer envío gratis en productos ≥ $33.000 | [algoritmodigital](https://algoritmodigital.com.ar/?p=4171) |
| Cuotas sin interés (premium) | +5,75% (3 cuotas), +10,75% (6 cuotas) | algoritmodigital (2026) |
| Liberación del dinero en ML | **Usado: 14 días después de la entrega** (aun con reputación). Nuevo con reputación: 8 días. Sin reputación: 14 días. Full: 6 días | [UpSeller](https://upseller.com/es/blog-article-511) (2026) [verificar en "detalle de la venta"] |
| Retenciones ML | IIBB 1,5-5% según provincia (también a monotributistas); IVA/Ganancias a no inscriptos con habitualidad (≈ 10+ ventas/mes y montos mínimos, umbrales en revisión: $200.000 / $400.000 / $750.000 según la fuente) | [jaguarsheet](https://jaguarsheet.com/es/blog/retenciones-mercado-libre), [iProfesional 2026-06-19](https://www.iprofesional.com/impuestos/443223-nuevas-reglas-vendedores-mercado-libre-limites-percepcion-iva) |
| Mercado Pago | Transferencia entre cuentas: gratis e inmediata. QR débito ~1,35% (+IVA); link de pago "al instante" ~6,29% + IVA; QR interoperable 0,8% + IVA | [yo-facturo](https://yo-facturo.com/blog/qr-mercado-pago-comisiones-cobrar/), [jonatanalmeira](https://www.jonatanalmeira.com/?p=70857) (2026) [verificar en la app] |
| Monotributo categoría A (desde 2026-08-01) | Cuota **$49.527,18/mes**; tope de ingresos brutos **$12.009.410,45/año** (≈ $1.000.000/mes ≈ USD 650/mes) | [Ámbito 2026-07-29](https://www.ambito.com/informacion-general/aumentos-arca-cuanto-se-pagara-monotributo-partir-agosto-2026-n6304386), [El Sol](https://www.elsol.com.ar/el-pais/arca-actualizo-los-topes-de-facturacion-y-el-costo-del-monotributo-desde-agosto/) |
| Alta de monotributo | Online, gratis, ~15 minutos, factura el mismo día (CUIT + clave fiscal nivel 3 desde la app Mi ARCA) | [yo-facturo](https://yo-facturo.com/blog/como-inscribirse-en-arca-por-primera-vez/), [Tiendanube](https://www.tiendanube.com/blog/como-hacerse-monotributista/) |
| Día de la Madre 2026 | **Domingo 2026-10-18** (tercer domingo de octubre) | [Lenovo AR](https://www.lenovo.com/ar/es/ofertas/dia-de-la-madre/cuando-es-el-dia-de-la-madre/) + calendario |
| Día de la Madre 2025 (CAME) | Ventas pyme −3,5% interanual (4.º año de caída); **ticket promedio $37.124**; solo creció electro (+0,6%) | [Río Negro](https://www.rionegro.com.ar/economia/dia-de-la-madre-las-ventas-cayeron-un-35-y-marcan-cuatro-anos-de-bajas-4341810/?amp=1), [La Capital](https://www.lacapital.com.ar/informacion-general/las-ventas-el-dia-la-madre-cayeron-35-y-marcaron-el-cuarto-ano-consecutivo-baja-n10225076.html) |
| CyberMonday 2026 | 2, 3 y 4 de noviembre (CACE) | [Tiendanube](https://www.tiendanube.com/blog/cuando-es-el-cybermonday) [verificar en cybermonday.com.ar] |
| Cierres de comercios | CABA, ene-feb 2026: 284 locales en venta, alquiler o cerrados en los corredores principales (+38,5% interanual) | [Canal26 2026-03-10](https://www.canal26.com/economia/2026/03/10/locales-vacios-en-la-ciudad-de-buenos-aires-estas-son-las-principales-avenidas-con-mas-persianas-bajas/), [BAE Negocios](https://www.baenegocios.com/negocios/mas-persianas-bajas-en-caba-ya-son-284-los-locales-vacios/) |
| Muebles usados | 40-70% más baratos que nuevos; rangos: < $100.000 (sillas, mesas de luz), $100-300.000 (escritorios, bibliotecas), > $300.000 (comedores, sillones) | [iProfesional 2026-07-08](https://www.iprofesional.com/finanzas/459474-mudanza-o-renovacion-donde-comprar-muebles-usados-en-excelente-estado-y-ahorrar-hasta-70) |
| Ropa usada | Locales compran en el acto, en consignación o con crédito en tienda; descuentos de 40-80% sobre el precio original | [iProfesional 2026-07-02](https://www.iprofesional.com/economia/458978-moda-circular-donde-comprar-y-vender-ropa-usada-de-calidad-a-los-mejores-precios) |
| Flete chico CABA | $45.000-90.000 (Kangoo/Partner, mínimo 2 h) | [Servidos](https://servidos.ar/servicios/limpieza/buenos-aires/retiro) (2026-07) |
| Courier | Tope USD 3.000 por envío, franquicia USD 400; puerta a puerta de Aerolíneas: 3-4 días desde Miami | [Diario Panorama](https://www.diariopanorama.com/noticia/509427/aerolineas-incorpora-entrega-domicilio-compras-realizadas-estados-unidos) |

**Conclusión operativa de la tabla (es la más importante del informe):** con una venta de usado por **Mercado Libre** el dinero se libera **14 días después de la entrega**: entre 16 y 20 días desde la venta. **Ninguna idea que dependa de cobrar por ML cumple el objetivo de 7 días.** Para la primera semana, los canales son **Facebook Marketplace, WhatsApp, Instagram, grupos de barrio y la venta presencial**, con cobro por **transferencia (gratis e inmediata)** o efectivo. ML queda como canal de la semana 3 en adelante.

### Ejemplo de neto en ML (para comparar)

Usado vendido a $100.000 en publicación clásica, categoría al 14%:
- Comisión 14% + IVA 21% = $16.940.
- Envío gratis a cargo del vendedor en productos ≥ $33.000: **$6.000-12.000 [NO VERIFICADO: depende de peso y reputación; mirar el simulador]**.
- Retención IIBB 1,5-5%: $1.500-5.000.
- **Neto: ≈ $66.000-75.500 (66-75%)**, cobrado entre 16 y 20 días después.
- **En Marketplace la misma venta deja $100.000 el mismo día** (menos tu transporte). En reventa de usados de ticket medio, esa diferencia de 25-34 puntos es casi todo el margen.

---

## 1. Lista de ideas (37)

Escala de probabilidad de cobrar en 7 días: **alta** (> 60%), **media** (30-60%), **baja** (10-30%), **muy baja** (< 10%), para alguien que le pone 6-10 h/día esta semana.

### BLOQUE A — Flipping de usados (comprar barato, acondicionar, revender)

#### 1. Flipping de electrónica chica (consolas, notebooks, auriculares, parlantes, smartwatch)
- **Qué es:** comprar en Marketplace avisos subvaluados ("urgente", "por viaje", "mudanza", fotos malas, títulos mal escritos), limpiar, probar, sacar buenas fotos y revender en Marketplace (y en ML desde la semana 2).
- **Evidencia:** el rubro tecnología fue el más elegido para el Día de la Madre (17%) según [iProfesional 2026-07-17](https://www.iprofesional.com/economia/439458-dia-madre-2025-cuales-son-regalos-mas-elegidos-y-cual-es-precio-promedio). Precios de usados: [NO VERIFICADO], hay que relevar 20 avisos por modelo.
- **Números [NO VERIFICADO]:** inversión por ciclo $150-400k (USD 100-260). Margen bruto típico 15-30% en piezas comunes; 40%+ solo cuando el aviso original está mal puesto. Ganancia por pieza $25-70k. **Con mucho esfuerzo: 1-3 piezas por semana → $25-180k/semana (USD 16-115), mediana ~USD 45.** La primera semana, lo más probable es 0-1 pieza.
- **Plan de 7 días:** D1: elegir 3 modelos líquidos (por ejemplo, una consola de generación anterior, auriculares de marca, notebooks de 4-6 años) y relevar 20 avisos de cada uno → planilla de precio de compra y de venta. D2-D3: ofertar en 15-25 avisos por debajo de la mediana; comprar 1-2 piezas probándolas en persona. D4: limpieza y fotos (luz natural, fondo neutro, foto del número de serie). D5-D7: publicar en Marketplace + 3 grupos locales; responder rápido; vender con transferencia verificada en la app.
- **Claude / él:** Claude arma la planilla de precios (él le pega los avisos copiados), detecta avisos subvaluados, redacta ofertas y publicaciones, arma un checklist de prueba por producto y un guion para negociar. Él busca, va a ver, prueba, paga y entrega.
- **Primer cobro:** 3-7 días. **Probabilidad en 7 días: media.**
- **Escala / qué construye:** una base de precios por modelo (un "stock" con rotación, que es su área). Escala a 5-8 piezas por semana con capital rotando. Techo: el tiempo de traslado.
- **Riesgos:** comprar algo robado (encubrimiento, art. 277 del Código Penal), fallas ocultas, billetes falsos en la reventa ([La Voz](https://grupoclarin-la-voz-prod.cdn.arcpublishing.com/sucesos/desbaratan-una-banda-que-estafaba-vendedores-con-dolares-falsos-por-facebook-en-cordoba-tres-detenidos)), comprobantes falsos. **Celulares: solo con IMEI verificado** en el chequeo de ENACOM/SINARC y con factura o caja ([iProfesional 2026-08-08](https://www.iprofesional.com/tecnologia/352497-comprar-celulares-usados-claves-para-no-caer-en-enganos)). Mi sugerencia: **excluir celulares la primera semana**.
- **Score: 6,5/10.**

#### 2. Flipping de herramientas eléctricas y de jardín (taladros, amoladoras, hidrolavadoras, bordeadoras, cortacésped)
- **Qué es:** lo mismo que la idea 1, pero en herramientas. La primavera (octubre) es temporada de jardín y de arreglos.
- **Evidencia:** [NO VERIFICADO] precios. La demanda estacional de jardín de octubre a diciembre es conocida, pero no la pude medir.
- **Números [NO VERIFICADO]:** compra $30-120k por pieza, venta +30-50%. Ganancia por pieza $15-45k. **Semana con mucho esfuerzo: $30-130k (USD 20-85), mediana ~USD 40.**
- **Plan de 7 días:** D1: relevar precios de 5 herramientas (taladro percutor, amoladora, hidrolavadora, bordeadora, cortacésped eléctrico). D2-D3: comprar 2-3 piezas probadas en marcha. D4: limpieza, cambio de cable o escobillas si hace falta (corralón). D5-D7: publicar con un video corto funcionando.
- **Claude / él:** igual que la idea 1. Además, Claude arma fichas con especificaciones (potencia, accesorios incluidos) que el comprador de herramientas valora.
- **Primer cobro:** 3-7 días. **Probabilidad: media.**
- **Escala:** combinada con la idea 34 (alquiler de herramientas), las piezas que no se venden se alquilan.
- **Riesgos:** herramientas robadas (pedir factura o caja; desconfiar de lotes grandes muy baratos), fallas eléctricas (probar en el momento). La estafa típica es menor que en electrónica.
- **Score: 6,5/10.**

#### 3. Muebles: rescate barato o regalado + limpieza + reventa
- **Qué es:** comprar o recibir gratis muebles de mudanzas ("lo regalo si lo retirás"), limpiarlos, retocarlos (lija, cera, tiradores) y revenderlos.
- **Evidencia:** muebles usados 40-70% más baratos que nuevos; rangos de $100-300k en escritorios y bibliotecas ([iProfesional 2026-07-08](https://www.iprofesional.com/finanzas/459474-mudanza-o-renovacion-donde-comprar-muebles-usados-en-excelente-estado-y-ahorrar-hasta-70)). Flete $45-90k ([Servidos](https://servidos.ar/servicios/mudanzas), 2026-07).
- **Números [NO VERIFICADO]:** compra $0-60k + retoques $5-15k + **flete (el gran costo: $45-90k si no tiene vehículo)**. Venta $80-250k. Ganancia por pieza $30-100k **solo si el comprador retira** o si él tiene vehículo. **Semana: $0-150k (USD 0-100), mediana ~USD 35.**
- **Plan de 7 días:** D1: buscar "regalo", "mudanza" y "retirar hoy" en Marketplace y grupos; priorizar madera maciza y piezas chicas (mesas de luz, sillas, banquetas, estantes) que entran en un auto. D2-D3: retirar 3-5 piezas. D4-D5: limpiar y retocar. D5-D7: publicar con "retiro en [barrio]" y flete opcional cobrado aparte.
- **Claude / él:** Claude le dice qué piezas valen la pena según fotos y medidas, calcula el margen después del flete y redacta los avisos. Él retira, restaura y entrega.
- **Primer cobro:** 4-7 días. **Probabilidad: media** (con auto) / **baja** (sin auto).
- **Escala:** depende del espacio de guardado y del vehículo. Si no tiene lugar para guardar, no escala.
- **Riesgos:** quedarse con stock voluminoso, plagas (polilla, chinches en tapizados: **evitar colchones y tapizados**), lesiones al cargar.
- **Score: 6/10.**

#### 4. Bicicletas usadas con puesta a punto
- **Qué es:** comprar bicis usadas con fallas simples (cubierta, cámara, frenos, cambios desregulados), dejarlas a punto en una bicicletería o él mismo con tutoriales, y revenderlas en primavera.
- **Evidencia:** las rodado 29 nuevas cuestan $228-269k ([mejorescompras, 2026-07-18](https://mejorescompras.com.ar/comparar/bicicletas)). Usadas: [NO VERIFICADO].
- **Números [NO VERIFICADO]:** compra $70-120k + service $15-35k → venta $130-190k. Ganancia por bici $25-50k. **Semana: 1-2 bicis → $25-100k (USD 16-65), mediana ~USD 30.**
- **Plan de 7 días:** D1: relevar precios y conseguir presupuesto de service en una bicicletería del barrio. D2-D3: comprar 1-2 bicis (pedir factura o constancia; anotar el número de cuadro). D4-D5: service. D6-D7: publicar con video andando.
- **Claude / él:** Claude evalúa por fotos y arma un checklist de inspección (cuadro, rodamientos, transmisión). Él compra, lleva al service y vende.
- **Primer cobro:** 5-10 días. **Probabilidad: baja-media.**
- **Escala:** buena temporada de octubre a marzo.
- **Riesgos:** **bicis robadas** (riesgo alto en el rubro: pedir factura, desconfiar de precios muy bajos y verificar el número de cuadro en registros o grupos de bicis robadas), costo del service mayor al estimado.
- **Score: 5,5/10.**

#### 5. Artículos de bebé y niños usados (cochecitos, practicunas, sillitas de comer, juguetes grandes)
- **Qué es:** categoría de alta rotación (los chicos crecen rápido y las familias compran usado). Comprar lotes de familias que "ya no usan", limpiar y revender.
- **Evidencia:** [NO VERIFICADO] precios. Moda circular y consumo de usados en alza por precio ([iProfesional 2026-07-02](https://www.iprofesional.com/economia/458978-moda-circular-donde-comprar-y-vender-ropa-usada-de-calidad-a-los-mejores-precios)).
- **Números [NO VERIFICADO]:** compra $20-70k por pieza, venta +40-80%. Ganancia por pieza $15-40k. **Semana: $20-100k (USD 13-65), mediana ~USD 30.**
- **Plan de 7 días:** D1: relevar cochecitos, practicunas y triciclos. D2-D3: ofrecer en grupos de mamás del barrio "compro/vendo en consignación" (combinarlo con la idea 11). D4: limpieza profunda (fundas lavadas, fotos). D5-D7: vender.
- **Claude / él:** Claude escribe avisos que transmiten higiene y estado; arma un checklist de seguridad (frenos, trabas, retiros del mercado del modelo). Él limpia y entrega.
- **Primer cobro:** 3-7 días. **Probabilidad: media.**
- **Escala:** ideal como consignación (sin capital).
- **Riesgos:** **NO revender sillas de auto usadas** (no se sabe si sufrieron un choque; seguridad) ni productos con retiro del mercado. Higiene.
- **Score: 6/10.**

#### 6. Ropa de marca circular (curaduría y reventa)
- **Qué es:** comprar prendas de marca en buen estado (ferias americanas, placares de conocidos, liquidaciones) y revenderlas curadas por Instagram, Marketplace o ML, o venderlas a locales de segunda mano.
- **Evidencia:** boom de segunda mano; locales como Galpón de Ropa pagan en efectivo o con crédito en tienda; descuentos de 40-80% sobre el original ([iProfesional 2026-07-02](https://www.iprofesional.com/economia/458978-moda-circular-donde-comprar-y-vender-ropa-usada-de-calidad-a-los-mejores-precios)).
- **Números [NO VERIFICADO]:** compra $3-12k por prenda → venta $12-35k. Ganancia por prenda $8-20k. **Semana: 5-12 prendas → $40-200k (USD 26-130), mediana ~USD 40.** Ticket bajo: mucho trabajo por peso ganado.
- **Plan de 7 días:** D1: elegir nicho (por ejemplo, camperas y buzos de marcas deportivas o outdoor). D2: recorrer 3-4 ferias o placares de familiares. D3: lavado, planchado y fotos en percha o con maniquí. D4-D7: publicar en Marketplace y en un Instagram de nicho; ofrecer el remanente a un local de segunda mano.
- **Claude / él:** Claude detecta marcas y temporadas con demanda, redacta descripciones con medidas y arma la grilla de precios. **Higgsfield solo para piezas de portada del perfil, nunca para mostrar la prenda en venta** (tiene que verse la prenda real).
- **Primer cobro:** 3-7 días. **Probabilidad: media.**
- **Escala:** limitada por el ticket. Funciona mejor como consignación (idea 11).
- **Riesgos:** **réplicas o falsificaciones** (excluidas: aprender a autenticar o evitar marcas muy falsificadas); fardos importados de origen dudoso ([Chequeado](https://chequeado.com/el-explicador/ropa-usada-frontera-y-crisis-textil-que-hay-detras-del-fenomeno-que-tiene-a-jujuy-como-principal-puerta-de-entrada/): la importación de ropa usada se liberó en 2024, pero buena parte entra por circuitos de frontera; además hay un proyecto de ley para volver a prohibirla, [iProfesional 2026-07-22](https://www.iprofesional.com/negocios/455969-ropa-usada-el-kirchnerismo-impulsa-polemico-proyecto-para-prohibir-su-importacion)). **No comprar fardos sin papeles.**
- **Score: 5,5/10.**

#### 7. Libros universitarios y escolares usados
- **Qué es:** comprar lotes de libros de carreras masivas y revenderlos por título a estudiantes.
- **Evidencia:** libros usados al ~60% del nuevo en librerías del centro; ferias escolares a mitad de precio ([Infobae](https://www.infobae.com/leamos/2024/01/23/como-leer-en-tiempos-de-inflacion-y-crisis-los-libros-usados-pueden-ser-la-solucion/), [La Capital MdP](https://www.lacapitalmdp.com/la-feria-de-libros-escolares-usados-ofrece-abaratar-gastos/)).
- **Números [NO VERIFICADO]:** ticket $10-40k; ganancia por libro $5-15k. **Semana en octubre: $0-40k (USD 0-25), mediana ~USD 5.** La demanda pica en marzo y agosto (inicio de cursada) y en febrero (escolares).
- **Plan de 7 días:** no recomendado ahora. Si se hace: comprar lotes de egresados (fin de cursada en diciembre) para vender en marzo de 2027.
- **Primer cobro:** 7-21 días. **Probabilidad: baja.**
- **Riesgos:** fotocopias o PDF (no vender: propiedad intelectual), stock que no rota.
- **Score: 3,5/10** (para este objetivo; 5 como estacional de febrero-marzo).

#### 8. Lotes "llevate todo" + venta desagregada (unbundling)
- **Qué es:** comprar lotes completos (mudanzas, "vacío baulera", "lote de cocina", "todo por $X") a precio de bulto y vender pieza por pieza. Es el arbitraje más claro del rubro: el vendedor del lote paga con descuento su apuro.
- **Evidencia:** [NO VERIFICADO] márgenes. La práctica es común en Marketplace (búsquedas "lote", "todo junto", "liquido todo").
- **Números [NO VERIFICADO]:** lote $50-200k → valor desagregado 2-4x en 2-6 semanas. La primera semana suele recuperar 40-80% del costo con las 3-5 piezas más líquidas. **Ganancia semanal en régimen: $50-180k (USD 30-115), mediana ~USD 50.** La primera semana, la ganancia neta puede ser negativa aunque haya cobros.
- **Plan de 7 días:** D1: buscar 10 lotes; pedirle a Claude que tasee cada pieza visible (con precios relevados). D2: comprar 1 lote con un valor desagregado estimado de 3x o más. D3: clasificar en A (vender ya), B (ML más adelante), C (donar/feria). D4-D7: publicar las A de a 5 por día; las C a la feria (idea 35).
- **Claude / él:** Claude tasea por lista o fotos, arma el inventario (planilla con SKU, estado, precio piso, canal) y genera los avisos en lote. **Acá su perfil de stock pesa:** rotación, piso de precio, ABC.
- **Primer cobro:** 2-5 días. **Probabilidad: media-alta.**
- **Escala:** sí, con espacio de guardado y vehículo. Construye un sistema de inventario reutilizable.
- **Riesgos:** sobreestimar el valor (Claude tasando sin precios reales = error; siempre con relevamiento), quedarse con la cola C, objetos de origen dudoso.
- **Score: 7/10.**

#### 9. Reparación simple + reventa (con técnico tercerizado)
- **Qué es:** comprar equipos "para repuesto" o con una falla conocida y barata (batería de notebook, joystick con drift, pantalla de tablet) y pagarle a un técnico la reparación.
- **Números [NO VERIFICADO]:** el margen existe solo si la falla es diagnosticable por foto o video. Si no, se pierde. **Semana: $0-80k, mediana ~USD 10** al principio.
- **Plan de 7 días:** conseguir 1-2 técnicos con presupuesto cerrado → comprar 1 equipo con falla típica → reparar (2-5 días) → vender. Muy justo para 7 días.
- **Primer cobro:** 7-14 días. **Probabilidad: baja.**
- **Riesgos:** diagnóstico equivocado; él no tiene el oficio, así que depende del técnico.
- **Score: 4,5/10.**

#### 10. Arbitraje Marketplace → Mercado Libre (y al revés)
- **Qué es:** comprar en Marketplace (más barato, más informal) y vender en ML (mayor audiencia y precio).
- **Números:** el neto de ML es 66-75% del precio (ver el ejemplo de la sección 0). Para ganar, el precio de ML tiene que ser más de 1,4 veces el de compra. **Cobro: 16-20 días después de la venta (usado).**
- **Plan de 7 días:** no sirve para el objetivo. Sirve como canal de salida de las piezas B de la idea 8.
- **Primer cobro:** 15-25 días. **Probabilidad en 7 días: muy baja.**
- **Riesgos:** reclamos y devoluciones en ML (el comprador está protegido y el vendedor nuevo pierde las disputas), retenciones si no está inscripto.
- **Score: 4/10** (para este objetivo).

### BLOQUE B — Vender lo de otros (sin capital): consignación y servicios de venta

#### 11. "Te vendo lo que no usás": consignación para familiares, vecinos y conocidos
- **Qué es:** retira (o fotografía en el lugar) cosas que la gente no usa, las publica y vende, y se queda con **20-30% de comisión**. El dueño cobra cuando se vende.
- **Evidencia:** referencia de comisión del 25% en garage sales organizadas ([Infonegocios, Córdoba](https://infonegocios.info/que-dice-la-gente/sobre-los-garage-sale-y-la-comision-del-25), **nota vieja, 2009-04-21: tomarla solo como orden de magnitud**). Los locales de ropa usada pagan al consignante 30-75% del valor final. [NO VERIFICADO para 2026.]
- **Números:** **inversión $0** (más transporte). Si en la semana vende $300-800k de objetos ajenos → comisión **$60-240k (USD 40-155), mediana ~USD 60.** Primera semana realista: 1-4 ventas → $15-80k.
- **Plan de 7 días:** D1: Claude redacta un mensaje para 30 contactos (familia, vecinos, grupo del edificio): "Vendo por vos lo que no usás, 25% de comisión, vos no hacés nada". D2: visitas, fotos, **acta simple de consignación** (Claude la redacta: lista de objetos, precio piso, comisión, plazo de 30 días, qué pasa si no se vende). D3: publicar 15-30 artículos en Marketplace y grupos. D4-D7: responder, mostrar, cobrar por transferencia a **su** cuenta y liquidarle al dueño en 24 h con un detalle.
- **Claude / él:** Claude tasea con precios relevados, escribe avisos, responde consultas (él copia y pega), lleva la planilla de consignación (dueño, artículo, piso, vendido, comisión, liquidado) y redacta el contrato. Él consigue clientes, fotografía, muestra y entrega.
- **Primer cobro:** 2-7 días. **Probabilidad: alta** (si tiene 3-5 conocidos con cosas para vender).
- **Escala / qué construye:** reputación local + base de clientes + planilla de consignación = un negocio de "liquidación de bienes" que escala a mudanzas, sucesiones y comercios (ideas 12-15). Muy en línea con su perfil de stock.
- **Riesgos:** roturas o pérdidas de objetos ajenos (aclarar responsabilidad en el acta), discusiones de precio con el dueño (el precio piso firmado lo evita), estafas al vender (ver sección 3). **Fiscal: la comisión es su ingreso** si está bien documentado como consignación (mandato). Conviene que el comprador le pague a él y él liquide con comprobante. Consultar con un contador si conviene que el dueño cobre directo.
- **Score: 7,5/10.**

#### 12. Venta de mudanza o garage sale organizada (evento de fin de semana)
- **Qué es:** a una familia que se muda (o achica, o se va del país) le organiza una venta presencial de 1-2 días: tasación, etiquetado, difusión y cobro. Comisión de 20-30%.
- **Evidencia:** en Mendoza hay personas que organizan este tipo de ventas todos los fines de semana desde hace más de 10 años ([UNCuyo / Unidiversidad](https://www.unidiversidad.com.ar/si-viajas-heredas-o-no-tenes-lugar-hay-una-pregunta-a-resolver-que-hago-con-los-muebles)); comisión del 25% como referencia (Infonegocios, 2009).
- **Números [NO VERIFICADO]:** casa con $1-3 millones en objetos vendibles; en un evento se vende 40-60% → $0,4-1,8 millones × 25% = **$100-450k por evento (USD 65-290).** Mediana ~USD 120 por evento; **el cuello de botella es conseguir el cliente esta semana.**
- **Plan de 7 días:** D1-D2: avisar a la red y a 2-3 inmobiliarias o fleteros de la zona (ellos ven las mudanzas primero). D3: tasación y etiquetado. D4-D5: difusión (Marketplace "venta de mudanza sábado y domingo", grupos del barrio, carteles). D6-D7: evento; cobro con QR o transferencia; lo no vendido pasa a consignación (idea 11) o a donación.
- **Claude / él:** Claude arma el inventario con precios, el plan de difusión, los textos, la cartelería y el reparto de comisiones. Él coordina, atiende y cobra.
- **Primer cobro:** 5-10 días. **Probabilidad: baja-media** (depende de conseguir el cliente).
- **Escala:** muy buena como servicio recurrente con derivación de inmobiliarias.
- **Riesgos:** seguridad (gente desconocida en una casa: hacer el evento con 2-3 personas y con un recorrido cerrado), robos durante el evento, objetos de valor (tasar joyas o arte no es su terreno: derivarlos).
- **Score: 7/10.**

#### 13. Vaciado de casas y sucesiones (comprar el contenido o vaciar + vender)
- **Qué es:** herederos o propietarios que necesitan vaciar rápido un inmueble para venderlo o alquilarlo. Dos modelos: (a) **comprar el contenido completo** a precio de bulto, o (b) **cobrar por vaciar** (flete + limpieza) y quedarse con lo vendible.
- **Evidencia:** limpieza profunda $60-130k; flete chico $45-90k ([Servidos](https://servidos.ar/servicios/limpieza/buenos-aires/retiro), 2026-07). [NO VERIFICADO] precios de compra de contenido.
- **Números [NO VERIFICADO]:** por trabajo, $150-600k de ganancia, pero con 2-4 semanas de ciclo.
- **Plan de 7 días:** contactar a 10 inmobiliarias o escribanías del barrio ofreciendo "vaciado + liquidación"; si sale un trabajo, cobrar **anticipo** por el vaciado.
- **Primer cobro:** 7-21 días. **Probabilidad: baja.**
- **Escala:** es el formato "grande" de las ideas 11-12. Requiere vehículo o fletero de confianza y depósito.
- **Riesgos:** **titularidad**: en sucesiones, solo con autorización de todos los herederos o del administrador judicial (pedirla por escrito), residuos, sobreestimación.
- **Score: 6/10.**

#### 14. Liquidación de stock de comercios que cierran (consignación o compra)
- **Qué es:** a un comercio que cierra (o que tiene stock muerto) le ofrece vender el remanente: (a) en consignación con 20-30% de comisión o (b) comprarlo a 25-40% del costo.
- **Evidencia:** 284 locales cerrados o en venta en corredores de CABA en ene-feb 2026, +38,5% interanual ([Canal26 2026-03-10](https://www.canal26.com/economia/2026/03/10/locales-vacios-en-la-ciudad-de-buenos-aires-estas-son-las-principales-avenidas-con-mas-persianas-bajas/)); galerías con alta tasa de cierres ([iProfesional](https://www.iprofesional.com/economia/319359-galerias-comerciales-en-decadencia-alarmante-cifra-de-cierres)).
- **Números [NO VERIFICADO]:** stock de $1-3 millones a costo. La primera semana en consignación se venden $200-600k → comisión **$40-180k (USD 25-115), mediana ~USD 50.** Comprar el stock exige capital, que él no tiene; arrancar con consignación.
- **Plan de 7 días:** D1: listar 20 locales con cartel de "liquidación por cierre" o "se alquila" en la zona (recorrida + Marketplace + Google Maps). D2-D3: visitas con una propuesta de una página (Claude). D4: inventario rápido (sus skills: conteo, SKU, planilla). D5-D7: publicar packs y unidades; vender en el mismo local si sigue abierto.
- **Claude / él:** Claude arma la propuesta comercial, la planilla de inventario, los precios de liquidación (escalonados por semana) y los avisos. Él consigue el comercio, cuenta y vende.
- **Primer cobro:** 4-10 días. **Probabilidad: media.**
- **Escala / qué construye:** es su cancha (inventario y rotación). Puede derivar en "liquidador de stock para pymes", que conecta con la consultora de procesos (ficha `ideas/2026-09-07-consultora-mejora-procesos.md`).
- **Riesgos:** **facturación**: lo que vende el comercio tiene que salir facturado por el comercio (mandato) o por él como monotributista; nada en negro. Mercadería con marca registrada: verificar que sea original. Que el dueño cambie de idea.
- **Score: 7/10.**

#### 15. Equipamiento gastronómico y comercial de locales que cierran
- **Qué es:** heladeras exhibidoras, cafeteras, hornos, mesas, góndolas y mostradores de locales que cierran → revender a emprendedores que abren (también hay muchos). En consignación o con compra apalancada.
- **Números [NO VERIFICADO]:** ticket alto ($300k-3M); comisión de 10-20% → $50-400k por pieza vendida. Pocas operaciones.
- **Plan de 7 días:** como la idea 14, focalizado en gastronomía; publicar en grupos de "equipamiento gastronómico usado".
- **Primer cobro:** 7-14 días. **Probabilidad: baja.**
- **Riesgos:** fletes caros, equipos con fallas (probar en el lugar), prendas o embargos sobre bienes de comercios en quiebra (verificar que el dueño pueda vender).
- **Score: 6/10.**

#### 16. Asistente de venta de auto o moto de un conocido (tarifa fija, NO corretaje)
- **Qué es:** el dueño vende su vehículo y él le hace el trabajo pesado: tasación de mercado con relevamiento, fotos, aviso en ML y Marketplace, filtrado de consultas, coordinación de visitas, checklist de documentación (formulario 08, título, verificación policial). **Cobra una tarifa fija por servicio, no un porcentaje de la venta.**
- **Evidencia legal:** en CABA, el corretaje **inmobiliario** sin matrícula está prohibido y no da derecho a cobrar ([Ley 2340](https://boletinoficial.buenosaires.gob.ar/normativaba/norma/101209); fallos en [Microjuris](https://aldiaargentina.microjuris.com/2014/09/26/rechazo-del-pedido-de-remuneracion-a-favor-del-corredor-inmobiliario-ante-la-falta-de-matriculacion-del-intermediario/)). Para muebles y automotores rige en general la Ley 20.266 de martilleros y corredores **[NO VERIFICADO su alcance a esta actividad: consultar a un abogado]**. Por eso propongo cobrar por un **servicio de marketing y gestión** (no por intermediar ni cerrar el precio), sin firmar nada en nombre del dueño. La transferencia la hace el dueño o un gestor; arancel de ~1% del valor ([iProfesional 2026-06-23](https://www.iprofesional.com/autos/343934-cuanto-sale-la-transferencia-de-un-auto-en-argentina)).
- **Números [NO VERIFICADO]:** tarifa de $60-150k por vehículo (50% por adelantado). 1-2 por semana si hay demanda en la red → **USD 40-190**; mediana ~USD 50.
- **Plan de 7 días:** D1: ofrecerlo a la red ("¿alguien vende auto o moto?"). D2: relevamiento de 30 avisos del mismo modelo/año/km → precio sugerido. D3: fotos (limpieza previa) y aviso. D4-D7: filtrar consultas con un guion y coordinar visitas en lugar seguro.
- **Claude / él:** Claude releva y analiza precios, escribe el aviso, el guion de filtrado y el checklist de documentación. Él fotografía, coordina y acompaña.
- **Primer cobro:** 2-7 días (anticipo). **Probabilidad: media** (si aparece un conocido que vende).
- **Riesgos:** **legal** (no presentarse como corredor ni cobrar comisión sobre el precio), estafas típicas de autos (señas falsas, "test drive" robado: acompañar siempre, pedir DNI y foto del registro), ninguna responsabilidad sobre el estado del vehículo.
- **Score: 5,5/10.**

#### 17. Inmuebles: solo material de marketing para el dueño o para una inmobiliaria matriculada
- **Qué es:** fotos, video, plano simple y texto del aviso, cobrados **al dueño o a la inmobiliaria** por el trabajo, sin intermediar, sin mostrar como agente y sin cobrar comisión.
- **Legal:** en CABA, la intermediación inmobiliaria es exclusiva de corredores matriculados en CUCICBA (Ley 2340); en otras provincias hay colegios equivalentes. **No intermediar.** Hacer staging virtual con IA solo si se aclara en el aviso. (Solapa con la idea E7 del primer estudio: staging para inmobiliarias.)
- **Números [NO VERIFICADO]:** $40-100k por propiedad.
- **Primer cobro:** 3-10 días. **Probabilidad: baja.**
- **Score: 3,5/10.**

#### 18. Fotos + publicación para particulares que venden usados (C2C)
- **Qué es:** servicio de una sola vez: va a la casa, saca fotos buenas de 5-20 objetos, Claude escribe los avisos y él los publica **en la cuenta del dueño**. Tarifa fija. (Solapa con E5 del primer estudio, que apuntaba a tiendas; acá es para particulares y con cobro inmediato.)
- **Números [NO VERIFICADO]:** $3-6k por aviso o $30-60k por visita. **Semana: $30-150k (USD 20-100), mediana ~USD 30.**
- **Plan de 7 días:** ofrecerlo en grupos de barrio junto con la idea 11 ("o te lo vendo yo con comisión, o te armo los avisos y vendés vos").
- **Primer cobro:** 2-5 días. **Probabilidad: media.**
- **Riesgos:** **no usar IA para "mejorar" el producto en la foto** (la política de ML exige que la foto corresponda al artículo real: [Políticas de publicación de ML](https://www.mercadolibre.com.ar/seguro_publicacion.html)); para usados, foto real siempre.
- **Score: 5,5/10.**

### BLOQUE C — Mayorista, kits y preventa (vender antes de comprar)

#### 19. Kits de regalo para el Día de la Madre (domingo 2026-10-18) en preventa
- **Qué es:** 3-4 kits cerrados de regalo con productos **envasados y sellados** (sin fraccionar): por ejemplo, kit matero (mate, bombilla, yerbera, yerba envasada), kit desayuno (taza + productos envasados con RNPA + tarjeta), kit spa (velas, toalla, cosmética **sellada** de marca registrada), kit planta (idea 28). Se vende con **seña del 50% por transferencia** antes de comprar los insumos.
- **Evidencia:** ticket promedio CAME 2025 $37.124 (ventas −3,5%, [La Capital](https://www.lacapital.com.ar/informacion-general/las-ventas-el-dia-la-madre-cayeron-35-y-marcaron-el-cuarto-ano-consecutivo-baja-n10225076.html)). Set matero completo en Frávega: $64.732-66.678 ([Frávega](https://www.fravega.com/p/equipo-set-matero-completo-termo-mate-latas-y-canasta-matera-21283643/), 2026); en ML $59.999-63.999 con descuento. **Mercado en caída: el kit tiene que entrar en $30-45k, cerca del ticket promedio.**
- **Números [NO VERIFICADO costos de mayorista]:** costo del kit $16-25k (Once y mayoristas de bazar) + packaging $2-4k → venta $32-45k. Ganancia $10-18k por kit. **10-30 kits → $100-540k (USD 65-350) en total por la fecha (no por semana); mediana ~USD 130.** Capital: cero si la seña cubre los insumos.
- **Plan de 7 días:** D1 (2026-10-01): Claude diseña 3 kits con costo y precio; él releva precios en 2 mayoristas (online o Once). D2: fotos de los prototipos (uno armado de cada uno) + flyer; **Higgsfield sirve acá para la ambientación del flyer, pero el producto que se muestra tiene que ser el real**. D2-D3: difusión a la red (WhatsApp, estados, grupos del trabajo y de la facultad, del edificio) con fecha de corte el 2026-10-13. D3-D7: **cobrar señas** (primer cobro). D8-D15: compra, armado y entrega el 16-17 de octubre (o retiro).
- **Claude / él:** Claude arma el costeo, nombres, textos, flyer, planilla de pedidos (cliente, kit, seña, saldo, entrega) y la ruta de entregas. Él compra, arma y entrega.
- **Primer cobro:** 2-6 días (seña). **Probabilidad: alta** (si su red es de 100+ contactos activos).
- **Escala / qué construye:** plantilla reutilizable para Navidad, Día del Padre y Día del Maestro, y para la idea 23 (B2B). Su perfil logístico encaja: lista de materiales (BOM), compras, armado en línea, entregas por ruta.
- **Riesgos:** **alimentos**: solo productos envasados con RNPA y vencimiento visible, sin fraccionar ni reetiquetar; nada casero (ver idea 29). **Cosmética**: solo sellada, de marca registrada, sin fraccionar. Quedarse con stock si se compra antes de cobrar (no hacerlo). Logística de entrega concentrada en 2 días.
- **Score: 7,5/10.**

#### 20. Mayorista Avellaneda/Once → reventa por WhatsApp, Instagram y barrio (preventa por catálogo)
- **Qué es:** catálogo de 15-30 productos de mayoristas (ropa básica, pijamas, ropa interior, medias, bazar, accesorios) con fotos de los propios mayoristas (con permiso) o propias; se toma el pedido con seña y se compra después.
- **Evidencia:** la avenida Avellaneda vende 30-60% más barato que los shoppings; muchos locales piden un mínimo (por ejemplo, 3 prendas) y en las galerías es más fácil comprar de a una ([iProfesional 2026-06-19](https://www.iprofesional.com/actualidad/408386-uno-por-uno-mejores-locales-comprar-ropa-barata-avellaneda)). Distrito Moda permite compra mayorista online combinando marcas y con un solo envío ([iProfesional 2026-07-30](https://www.iprofesional.com/actualidad/408825-como-comprar-ropa-barata-avellaneda-online)). [NO VERIFICADO] mínimos de compra 2026.
- **Números [NO VERIFICADO]:** margen de 40-80% sobre el costo; ticket de $10-30k. **Semana: 10-30 prendas → $40-200k (USD 26-130), mediana ~USD 45.**
- **Plan de 7 días:** D1: elegir 1 categoría con demanda por la fecha (pijamas y ropa de entrecasa para el Día de la Madre). D2: ir a Avellaneda u Once, fotografiar y anotar precio y mínimo de 20 artículos. D3: catálogo en PDF o estado de WhatsApp (Claude). D3-D6: pedidos con seña. D6-D7: compra y entrega.
- **Claude / él:** Claude arma el catálogo, la tabla de talles, las respuestas tipo y la planilla. Él compra y entrega.
- **Primer cobro:** 3-7 días (seña). **Probabilidad: media-alta.**
- **Escala:** es un comercio en serio; necesita monotributo enseguida (ver sección 4).
- **Riesgos:** **marcas falsificadas** en ciertos puestos (excluir todo lo que imite una marca), cambios de talle, deudores.
- **Score: 6,5/10.**

#### 21. Compras comunitarias de bultos mayoristas (limpieza, almacén seco) para un edificio o barrio
- **Qué es:** junta pedidos de vecinos con pago anticipado, compra por bulto en un mayorista (Maxiconsumo, Diarco, Vital, Makro o distribuidoras) y reparte. Cobra un recargo de 8-15% sobre el precio mayorista, que igual queda por debajo del supermercado.
- **Evidencia:** [NO VERIFICADO] la brecha entre mayorista y supermercado en 2026. Es un formato extendido en grupos de barrio.
- **Números [NO VERIFICADO]:** pedido semanal de $300k-1,2M → recargo **$30-150k (USD 20-100), mediana ~USD 40.** Capital: cero (prepago).
- **Plan de 7 días:** D1: lista de 40 productos de alta rotación (lavandina, detergente, papel higiénico, aceite, yerba, fideos, arroz) con precio mayorista vs. supermercado (Claude arma la comparativa). D2: mensaje al grupo del edificio o de la cuadra. D3-D4: pedidos con pago por transferencia hasta el corte. D5: compra. D6: armado por pedido (picking: es su terreno). D7: entrega.
- **Claude / él:** Claude arma la lista, la comparativa, el formulario de pedido (Google Forms), la consolidación y las etiquetas de cada pedido. Él compra, arma y reparte.
- **Primer cobro:** 3-7 días. **Probabilidad: alta** (si tiene un grupo de vecinos activo).
- **Escala / qué construye:** recurrencia semanal + datos de demanda → un "almacén de barrio sin local". Sinergia total con logística (consolidación, picking, ruteo).
- **Riesgos:** **solo productos envasados y sellados; nunca fraccionar** (fraccionar alimentos o domisanitarios exige habilitación), cadena de frío (evitar refrigerados), inscripción en algunos mayoristas (piden CUIT: conviene el monotributo), habilitación municipal para comercializar alimentos en forma habitual **[NO VERIFICADO: consultar al municipio]**.
- **Score: 6,5/10.**

#### 22. Bolsones de frutas y verduras por pedido
- **Qué es:** compra a cajón en el Mercado Central o en un mayorista frutihortícola y arma bolsones semanales para pedidos prepagos.
- **Números [NO VERIFICADO]:** bolsón de $15-20k con un costo de $10-13k; 15-30 bolsones por semana → **$60-200k (USD 40-130) menos nafta; mediana ~USD 45.**
- **Plan de 7 días:** D1-D2: precios del Central y del verdulero del barrio; armar 2 bolsones tipo. D3-D5: pedidos con pago anticipado. D6: compra de madrugada. D7: armado y entrega.
- **Primer cobro:** 3-7 días. **Probabilidad: media-alta** (con vehículo).
- **Riesgos:** perecederos (merma de 5-15%), madrugar, **habilitación municipal para venta de alimentos y transporte [NO VERIFICADO]**; las frutas y verduras frescas sin elaborar no requieren RNPA, pero la venta habitual sí puede requerir permiso local.
- **Score: 6/10.**

#### 23. Canastas y regalos corporativos de fin de año (B2B) en preventa con seña
- **Qué es:** a pymes (contadores, consultorios, distribuidoras) les vende canastas navideñas o kits de regalo para empleados y clientes, armados con productos envasados. Seña del 50% hoy y entrega del 10 al 20 de diciembre.
- **Evidencia:** las canastas premium y la personalización son tendencia en regalos corporativos ([Tiendanube](https://www.tiendanube.com/blog/ideas-para-regalar-clientes-en-navidad/)). [NO VERIFICADO] precios de 2026.
- **Números [NO VERIFICADO]:** pedido de 15-40 canastas a $35-60k → ventas de $0,5-2,4M; margen de 25-40% → **$130-900k por cliente**, cobrado mitad ahora y mitad en diciembre.
- **Plan de 7 días:** D1: catálogo de 3 niveles (Claude). D2-D5: escribirles a 30 pymes de la red (incluida la red de la consultora de procesos) y visitar 5. D5-D7: primera seña.
- **Primer cobro:** 5-10 días (seña). **Probabilidad: media.**
- **Escala:** mucha, y es estacional. Construye una cartera B2B que sirve para la consultora.
- **Riesgos:** **facturación**: las empresas piden factura (necesita monotributo; si el pedido es grande, cuidado con el tope de la categoría), cumplir en fecha, precios que suben entre octubre y diciembre (cerrar los precios de los proveedores al cobrar la seña).
- **Score: 6,5/10.**

#### 24. Preventa de verano (ventiladores, piletas de lona, sombrillas, conservadoras)
- **Qué es:** vender por anticipado productos de verano comprados al por mayor o en ofertas reales.
- **Evidencia:** ventilador de pie Peabody 18": $54.999-84.999 (mínimo de los últimos 64 días: $55.000); Liliana 20": $95.800 ([mejorescompras, 2026-07-18](https://mejorescompras.com.ar/comparar/ventiladores)). CyberMonday del 2 al 4 de noviembre.
- **Números [NO VERIFICADO]:** margen de 15-25% sobre un nuevo, comprando a mayorista con factura; mucha competencia de ML con cuotas sin interés.
- **Plan de 7 días:** en octubre la demanda todavía no pica; la ventana real es la primera ola de calor (noviembre-diciembre).
- **Primer cobro:** 14-40 días. **Probabilidad en 7 días: baja.**
- **Riesgos:** **protector solar y repelentes son productos regulados (ANMAT): solo revender envasados, sellados y de marca registrada, con factura del proveedor; nunca fraccionar ni importar sin registro.** Stock que no rota si el verano es fresco. Garantía de electrodomésticos.
- **Score: 4,5/10** (reevaluar el 2026-11-01).

#### 25. Kits de mate personalizados (grabado tercerizado) para regalo y empresas
- **Qué es:** mate + bombilla + yerbera con grabado láser de nombre o logo, tercerizado en un taller. Sirve para el Día de la Madre, para egresados y para regalos corporativos.
- **Evidencia:** set matero completo a $59.999-66.678 en Frávega y ML (2026); [NO VERIFICADO] costo del grabado.
- **Números [NO VERIFICADO]:** costo de $15-25k + grabado de $3-6k → venta de $35-50k.
- **Plan de 7 días:** D1: cotizar 2 talleres de grabado y 2 mayoristas de regionales. D2: prototipo y fotos. D3-D7: preventa con seña.
- **Primer cobro:** 4-7 días (seña). **Probabilidad: media.**
- **Riesgos:** plazos del taller, tiempos de grabado en temporada alta.
- **Score: 6/10** (se superpone con las ideas 19 y 23; conviene fusionarla).

#### 26. Regalos de fin de ciclo lectivo (docentes y egresados) y útiles 2027 en preventa
- **Qué es:** kits para regalarles a docentes en diciembre, souvenirs de egresados y combos de útiles para marzo de 2027.
- **Evidencia:** la canasta escolar de CABA subió 75,34% interanual en 2025 ([iProfesional](https://www.iprofesional.com/management/422705-cuanto-aumento-la-canasta-escolar-2025-y-principales-promociones)).
- **Primer cobro:** 14-60 días. **Probabilidad en 7 días: baja.**
- **Score: 4,5/10** (para este objetivo).

#### 27. Revendedor de venta directa (catálogos de cosmética y hogar)
- **Qué es:** sumarse como revendedor de una empresa de venta directa (cosmética, hogar), con márgenes fijados por la empresa.
- **Números [NO VERIFICADO]:** margen de 20-30% sobre el precio de catálogo; ciclos de pedido de 2-3 semanas; algunas empresas exigen un pedido mínimo.
- **Primer cobro:** 10-21 días (la ganancia llega con la entrega). Se puede cobrar una seña antes. **Probabilidad: baja.**
- **Riesgos:** cuidado con esquemas que pagan más por reclutar que por vender (multinivel); pedidos mínimos que se convierten en stock propio.
- **Score: 4/10.**

#### 28. Plantas: plantines de vivero mayorista + maceta decorada
- **Qué es:** comprar plantines y suculentas en un vivero mayorista (zona de Escobar o productores locales), trasplantar a macetas decoradas y vender como regalo (Día de la Madre) o en una feria.
- **Evidencia:** los productores de cactus y suculentas venden con envío y pagos electrónicos ([Catálogo de Economía Social de Mendoza](https://www.mendoza.gov.ar/catalogoeconomiasocial/producto/suculentas/)); [NO VERIFICADO] precios mayoristas de 2026.
- **Números [NO VERIFICADO]:** costo de $3-8k por planta y maceta → venta de $8-20k. 20-50 unidades → **$60-300k (USD 40-195) por la fecha; mediana ~USD 60.**
- **Plan de 7 días:** D1: contactar 2 viveros mayoristas. D2: compra de prueba (20 unidades). D3: armado y fotos. D3-D7: venta por WhatsApp y Marketplace; sumar al kit de la idea 19.
- **Primer cobro:** 3-7 días. **Probabilidad: media.**
- **Riesgos:** perecedero (riego, transporte), estacionalidad. **Especies protegidas o extraídas de la naturaleza: no.**
- **Score: 6/10.**

#### 29. Comida casera (evaluación honesta)
- **Qué es:** viandas, budines, panificados o conservas hechos en casa.
- **Regulación:** la venta a terceros de alimentos elaborados exige **habilitación bromatológica municipal**. Algunos municipios tienen registros de **cocina domiciliaria** (clase 1), con declaración jurada, inspección, curso de manipulación de alimentos y libreta sanitaria ([Ordenanza 38/2021 de General Acha, La Pampa](https://concejo.generalacha.gob.ar/images/docs/ordenanzas_2021/ORDENANZA_N_38_2021_REGISTRO_COCINAS_DOMICILIARIAS.pdf); [Derecho en Zapatillas](https://www.derechoenzapatillas.com/2019/que-dice-la-ley-sobre-la-venta-de-comida-casera/)). **Para vender productos envasados a comercios o fuera del municipio hace falta RNPE/RNPA**, cosa que no se consigue en 7 días.
- **Veredicto:** **en 7 días, legalmente, solo es posible si su municipio tiene un registro de cocina domiciliaria con trámite rápido y él ya tiene el carnet de manipulador.** Si no, queda descartada para este objetivo. La alternativa legal inmediata es **vender productos ya envasados con RNPA de terceros** (ideas 19 y 21) o vender a comisión para un elaborador habilitado.
- **Primer cobro:** n/d. **Probabilidad (legal) en 7 días: muy baja.**
- **Score: 3/10.**

### BLOQUE D — Subastas, importación, temporada y canales

#### 30. Subastas del Banco Ciudad y judiciales
- **Qué es:** comprar lotes (vehículos, materiales fuera de uso, mobiliario) en remates y revenderlos.
- **Evidencia:** inscripción hasta 48 h hábiles antes; caución obligatoria; todo online en subastas.bancociudad.com.ar ([iProfesional 2026-07-16](https://www.iprofesional.com/negocios/458739-subasta-banco-ciudad-julio-2026-como-participar-departamentos-desde-29000-dolares-autos-desde-500000-pesos)). Autos desde $500.000.
- **Números:** comisión del martillero + IVA + gastos + retiro; la caución inmoviliza capital. Con USD 300-500 el acceso es muy limitado.
- **Primer cobro:** 21-60 días. **Probabilidad en 7 días: muy baja.**
- **Riesgos:** comprar sin inspeccionar ("en el estado en que se encuentra"), costos de retiro y traslado, deudas asociadas a vehículos.
- **Score: 3/10.**

#### 31. Remates privados de liquidaciones y quiebras (lotes de mercadería)
- **Qué es:** igual que la idea 30, pero en martilleros privados que rematan stock de empresas.
- **Primer cobro:** 10-30 días. **Probabilidad: muy baja.**
- **Score: 4/10** (más interesante con capital y experiencia de la idea 14).

#### 32. Importación chica por courier con preventa
- **Qué es:** traer productos de nicho (accesorios, repuestos, gadgets) por courier vendiéndolos antes.
- **Evidencia:** tope de USD 3.000 por envío y franquicia de USD 400; el puerta a puerta de Aerolíneas tarda 3-4 días **desde Miami** ([Diario Panorama](https://www.diariopanorama.com/noticia/509427/aerolineas-incorpora-entrega-domicilio-compras-realizadas-estados-unidos)). En la práctica: compra (1 día) + envío al depósito de Miami (2-5 días) + consolidación + vuelo + entrega = **10-20 días**.
- **Números:** la competencia con Temu, Shein y ML internacional es feroz; el régimen de courier está pensado para uso personal y **la reventa habitual puede requerir inscripción como importador [NO VERIFICADO: consultar un despachante]**.
- **Primer cobro:** seña en 7 días posible; ganancia en 15-30 días. **Probabilidad (ganancia) en 7 días: muy baja.**
- **Score: 3,5/10.**

#### 33. Arbitraje de ofertas (CyberMonday del 2 al 4 de noviembre, liquidaciones de temporada)
- **Qué es:** comprar en promociones reales y revender a precio lleno.
- **Evidencia:** **"más de 7 de cada 10 descuentos vigentes en ML no son un ahorro real"** ([mejorescompras, 2026-07-18](https://mejorescompras.com.ar/comparar/bicicletas)). El margen es chico y riesgoso.
- **Primer cobro:** después del 2026-11-04. **Probabilidad en 7 días: nula.**
- **Score: 3/10.**

#### 34. Alquiler P2P de herramientas o equipos (hidrolavadora, taladro percutor, escalera, mesas y sillas)
- **Qué es:** comprar 2-3 equipos usados (idea 2) y alquilarlos por día a vecinos, con depósito en garantía.
- **Números [NO VERIFICADO]:** alquiler de $8-20k por día por equipo; 3-6 alquileres por semana → **$25-100k (USD 16-65), mediana ~USD 25.** El equipo se amortiza en 4-10 alquileres.
- **Plan de 7 días:** D1-D3: comprar 1-2 equipos (o usar los propios o los de la familia). D3: contrato simple + depósito (Claude). D4-D7: avisos en grupos de barrio.
- **Primer cobro:** 3-7 días. **Probabilidad: media.**
- **Riesgos:** roturas y robos (depósito equivalente al valor del equipo + DNI), lesiones del usuario (instructivo de uso seguro + deslinde).
- **Score: 5/10.**

#### 35. Puesto de fin de semana en una feria o mercado de pulgas
- **Qué es:** un canal más que una idea: vender el remanente de las ideas 8, 11 y 12 en una feria barrial o americana.
- **Evidencia:** ferias de moda circular en crecimiento ([iProfesional 2026-07-02](https://www.iprofesional.com/economia/458978-moda-circular-donde-comprar-y-vender-ropa-usada-de-calidad-a-los-mejores-precios)). [NO VERIFICADO] costo del puesto (suele ir de $0 en ferias barriales a $20-60k en ferias organizadas).
- **Números [NO VERIFICADO]:** ventas de $100-400k por jornada con buen surtido.
- **Primer cobro:** el sábado o domingo de esta semana (2026-10-03/04) si consigue lugar. **Probabilidad: media.**
- **Riesgos:** permisos municipales para ferias no autorizadas, clima.
- **Score: 5,5/10.**

### BLOQUE E — Logística de barrio (gig y servicio; encajan con su perfil)

#### 36. Cadete Flex para vendedores de Mercado Libre del barrio (gig)
- **Qué es:** los vendedores de ML que usan Flex (envío en el día que gestiona el vendedor) necesitan quien reparta. Él ofrece reparto por paquete a 3-10 vendedores de su zona.
- **Evidencia:** repartidores de ML: hasta ~$890.000 por mes a tiempo parcial y $1,5-1,7 millones con más volumen ([iProfesional 2026-06-05](https://www.iprofesional.com/management/385494-cuanto-gana-un-repartidor-de-mercado-libre-en-argentina)). Son contratistas independientes que ponen su vehículo y sus costos. [NO VERIFICADO] tarifa por paquete y frecuencia de pago (suele ser semanal o quincenal según el vendedor o la empresa logística).
- **Números [NO VERIFICADO]:** neto de nafta y desgaste: **$100-250k por semana (USD 65-160) a tiempo parcial**, pero es tiempo vendido, no un negocio.
- **Plan de 7 días:** D1: contactar vendedores locales (ML → perfil del vendedor → zona; grupos de "Flex"). D2-D3: acordar la tarifa y una prueba. D4-D7: repartir.
- **Primer cobro:** 7-14 días (según el ciclo de pago). **Probabilidad en 7 días: baja-media.** Requiere moto o auto con seguro.
- **Riesgos:** accidentes, seguro, desgaste del vehículo, no registrado como empleado (monotributo obligatorio).
- **Score: 5/10** (como fuente de caja, no como negocio).

#### 37. "Depósito y empaque de barrio" para vendedores chicos (versión física e inmediata de C4)
- **Qué es:** 2-5 emprendedores le dejan stock; él lleva el inventario, arma los pedidos, etiqueta y despacha (Colecta, Places o Flex). Cobra por pedido despachado + almacenamiento. Es la versión física y de caja inmediata de "Ops para vendedores de ML" (C4 del primer estudio).
- **Números [NO VERIFICADO]:** $1.500-3.000 por pedido + almacenamiento mensual; 50-150 pedidos por semana → **$75-450k por semana**, pero se necesitan semanas para conseguir clientes.
- **Plan de 7 días:** D1: oferta de una página (Claude) + lista de 30 emprendedores locales (Instagram, ferias). D2-D5: 10 conversaciones. D6-D7: el primero en prueba (cobrar la primera semana por adelantado).
- **Primer cobro:** 7-14 días. **Probabilidad en 7 días: baja.**
- **Escala / qué construye:** **la que más construye** (procesos, KPIs de stock, casos para la consultora). Requiere espacio seco y seguro.
- **Riesgos:** responsabilidad por mercadería ajena (contrato + inventario firmado), espacio, seguro.
- **Score: 6,5/10** (alto como negocio; bajo para el objetivo de 7 días).

### Excluidas explícitamente (no se evaluaron como ideas)
- **Reventa de entradas:** reventa por encima del valor y reventa no autorizada; riesgo legal y de fraude. Excluida.
- **Réplicas o falsificaciones** (ropa, zapatillas, perfumes): delito marcario. Excluido.
- **Fardos de ropa usada importada sin papeles:** origen dudoso. Excluido.
- **Celulares sin IMEI verificado ni factura:** riesgo de encubrimiento. Excluidos.
- **Medicamentos, suplementos, protector solar o cosmética fraccionados o sin registro, alimentos caseros sin habilitación:** excluidos (ver ideas 24 y 29).
- **Compraventa propia de autos o motos:** el capital (> USD 500) no alcanza. Excluida.
- **Arbitraje de dólares o cripto ("rulo"):** es una operación financiera, no comercio, y el proyecto la excluye.
- **Corretaje inmobiliario sin matrícula:** prohibido (Ley 2340 de CABA). Excluido.

---

## 2. Top 5 para cobrar esta semana (2026-10-01 → 2026-10-08)

| # | Idea | Por qué entra al top | Primer cobro | Prob. 7 días | Score |
|---|---|---|---|---|---|
| 11 | **Consignación "te vendo lo que no usás"** | Capital $0, demanda inmediata en la red propia, construye la base de todo el bloque B | 2-7 días | Alta | 7,5 |
| 19 | **Kits del Día de la Madre en preventa** | Fecha fija (2026-10-18), se cobra la seña antes de comprar, plantilla reutilizable para Navidad | 2-6 días (seña) | Alta | 7,5 |
| 8 | **Lotes + venta desagregada** | El arbitraje con más margen del rubro; su perfil de inventario es una ventaja real | 2-5 días | Media-alta | 7 |
| 14 | **Liquidación de stock de comercios que cierran (consignación)** | Hay oferta abundante (cierres +38,5%), es su cancha y lleva a la consultora | 4-10 días | Media | 7 |
| 21 | **Compras comunitarias de bultos mayoristas** | Prepago (capital $0), recurrente, picking y ruteo puro | 3-7 días | Alta | 6,5 |

**Combinación sugerida para la semana 1** (las cinco comparten canal y planilla):
- **Día 1 (2026-10-01):** un solo mensaje a la red con tres ofertas: "te vendo lo que no usás (25%)", "kits del Día de la Madre (reservá con seña)" y "compra mayorista del edificio".
- **Días 2-3:** visitas de consignación + 1 lote de Marketplace + recorrida de 10 comercios en liquidación.
- **Días 3-7:** publicar todo en Marketplace y grupos, cobrar señas y comisiones, primera entrega comunitaria.
- **Meta honesta de la semana 1:** $50-250k de ganancia (USD 30-160); **mediana estimada ~USD 60**. Lo valioso de la semana no es el monto, sino validar qué canal responde.
- **Herramienta común (Claude):** una planilla única con hojas de Inventario (propio y consignado), Pedidos/Señas, Clientes, Liquidaciones y Caja. Es la base del sistema si el rubro funciona.

---

## 3. Seguridad: cómo no ser estafado comprando y vendiendo

**Vendiendo (las estafas más comunes en AR en 2026 según los medios):**
1. **Comprobante falso de transferencia:** **nunca entregar sin ver el dinero acreditado en la app** (no captura, no mail, no "ya te transferí"). Revisar el saldo y el movimiento con el nombre del ordenante ([El Litoral](https://www.ellitoral.com/informacion-general/marketplace-facebook-evitar-estafas_0_HnJUNzaYjd.amp.html), [El Ancasti 2026-08-02](https://www.elancasti.com.ar/opinion/el-nuevo-cuento-del-tio-marketplace-como-operan-los-estafadores-y-que-meta-no-los-frena-n590570)).
2. **"Te transferí de más, devolveme":** siempre es estafa. No devolver nada; si de verdad entró dinero de más, que lo reclame por el banco ([La Nación](https://www.lanacion.com.ar/tecnologia/transferencia-por-error-y-engano-en-facebook-la-estafa-virtual-que-simula-enviar-dinero-de-mas-nid25072022/)).
3. **"Mi hermano te transfiere":** pagos desde una cuenta de un tercero pueden venir de cuentas robadas o de otra víctima, y después el banco revierte o te denuncian a vos. **Solo aceptar pagos de una cuenta a nombre de quien retira** ([Derecho en Zapatillas](https://www.derechoenzapatillas.com/2025/%f0%9f%8e%ae-mi-hermano-te-transfiere-la-nueva-vieja-estafa-del-marketplace/)).
4. **Falsos empleados de banco o de Mercado Pago:** nadie legítimo pide códigos, claves, "simular un préstamo" ni instalar una app. Cortar.
5. **Robo de cuenta de WhatsApp o billetera:** nunca compartir códigos de verificación por SMS ([iProUP](https://www.iproup.com/economia-digital/48129-estafa-robo-cuenta-billetera-virtual-facebook)). Activar la verificación en dos pasos de WhatsApp y de Mercado Pago **hoy**.
6. **Billetes falsos** (hubo bandas que compraban electrónica en Marketplace con dólares falsos en Córdoba: [La Voz](https://grupoclarin-la-voz-prod.cdn.arcpublishing.com/sucesos/desbaratan-una-banda-que-estafaba-vendedores-con-dolares-falsos-por-facebook-en-cordoba-tres-detenidos)): preferir transferencia; si es efectivo, contar y revisar en una entidad o con un marcador.
7. **Lugar de entrega:** de día, en lugares concurridos con cámaras (estaciones de servicio, puertas de bancos o de shoppings, frente a comisarías); hay iniciativas de "puntos seguros" para Marketplace ([Unidiversidad](https://www.unidiversidad.com.ar/avanza-la-propuesta-para-crear-puntos-seguros-para-la-compraventa-de-los-articulos-de-marketplace)). **No dar la dirección de su casa a desconocidos**; ir acompañado en ventas de más de $150k.

**Comprando:**
1. **Probar siempre en persona** (encender, cargar, conectar). Nada "sellado" a precio de usado.
2. **Origen:** pedir factura, caja o foto del comprador original; desconfiar de precios < 60% del mercado, de vendedores sin historial y de lotes de "muchas unidades nuevas iguales". **Celulares: verificar el IMEI** (`*#06#` + el chequeo de ENACOM). Bicis: número de cuadro.
3. **No pagar señas a desconocidos por Marketplace** antes de ver el producto (la estafa más común del lado comprador).
4. **Guardar evidencia** (capturas del chat y del aviso, DNI del vendedor si es una compra grande) por si aparece un reclamo de origen.
5. **Claude como filtro:** pegarle el chat completo antes de pagar o entregar; Claude marca las señales de alarma (apuro, terceros, cambios de método de pago).

---

## 4. Aspecto fiscal mínimo (monotributo y ARCA)

- **Vender cosas propias usadas en forma ocasional** (vaciar la casa) no es una actividad habitual. En la práctica no requiere monotributo, **pero en ML hay percepciones y retenciones si se superan umbrales de habitualidad** (≈ 10+ ventas por mes o montos mínimos; los umbrales publicados varían: $200.000, $400.000 o $750.000 según la fuente y la fecha, [iProfesional 2026-06-19](https://www.iprofesional.com/impuestos/443223-nuevas-reglas-vendedores-mercado-libre-limites-percepcion-iva)). **[Verificar con un contador]**
- **Flipping, mayorista, kits y consignación sistemática = actividad habitual con fin de lucro → monotributo.** El alta es online, gratis, en ~15 minutos, y permite facturar el mismo día con factura C.
- **Categoría A (desde 2026-08-01):** cuota de $49.527,18 por mes (≈ USD 32), que incluye impuesto, jubilación y obra social. Tope de **$12.009.410 por año ≈ $1.000.000 por mes de ingresos brutos**.
- **Trampa clave de la reventa:** para el monotributo cuenta la **facturación bruta (todo lo vendido), no la ganancia**. Revender $1 millón por mes con 25% de margen te pone en el tope de la categoría A ganando $250k. Con kits, mayorista y lotes, el tope se alcanza rápido: planificar la categoría (B, C...) con un contador.
- **Consignación (ideas 11, 12 y 14) es fiscalmente más eficiente:** si está documentada como mandato (acta de consignación + liquidación al dueño), **su ingreso es la comisión**, no el total vendido. **[Confirmar con un contador cómo facturar: comisión al dueño vs. venta a terceros por cuenta y orden.]**
- **Ingresos Brutos:** en varias jurisdicciones (CABA, Provincia de Buenos Aires y otras) existe el **régimen simplificado unificado con el monotributo** (se paga junto). Verificar la propia jurisdicción. ML retiene IIBB de 1,5-5% según provincia aun a monotributistas ([jaguarsheet](https://jaguarsheet.com/es/blog/retenciones-mercado-libre)).
- **Mercado Pago informa movimientos a ARCA.** Cobrar ventas habituales a una cuenta personal sin estar inscripto es la forma más rápida de tener un problema. **Recomendación: alta en monotributo en la semana 1 si se elige cualquier idea habitual** (todo el top 5 salvo la venta ocasional de cosas propias).
- **Alimentos y productos regulados:** el monotributo no habilita a vender alimentos elaborados. La habilitación bromatológica es municipal (idea 29).

---

## 5. Trampas comunes

1. **Contar ML como "cobro rápido":** usado = 14 días después de la entrega. En la semana 1, vender por Marketplace y WhatsApp.
2. **Calcular el margen sin flete ni tiempo:** en muebles, un flete de $45-90k borra la ganancia. Calcular **siempre** el margen neto de transporte, comisiones y viajes perdidos.
3. **Tasar "a ojo" o con Claude sin datos:** Claude no conoce los precios de hoy. Siempre darle 15-20 avisos reales pegados; el precio de venta es la **mediana de lo publicado menos 10-15%** (lo publicado no es lo vendido).
4. **Stock que no rota:** comprar lo que "parece barato" en lugar de lo que se vende rápido. Regla: **no comprar nada que no esté en la lista de productos líquidos relevados**; liquidar a costo lo que pase 21 días sin vender.
5. **Comprar antes de cobrar en preventa:** el modelo de kits y mayorista solo es de capital cero si **primero se cobra la seña**.
6. **Fotos con IA de productos usados:** engaña al comprador y viola la política de ML (la foto debe corresponder al artículo). Higgsfield solo para flyers, portadas y ambientación de kits armados reales.
7. **Origen dudoso:** "lote de 10 auriculares nuevos a mitad de precio" = probablemente robado o falsificado. El encubrimiento es delito aunque se compre "de buena fe" si las señales eran obvias.
8. **Garantía implícita:** como vendedor habitual, la Ley 24.240 de Defensa del Consumidor aplica a ventas profesionales. Describir el estado con precisión y probar delante del comprador.
9. **Mercado deprimido:** las ventas del Día de la Madre cayeron 4 años seguidos (CAME); el ticket de 2025 fue de $37.124. **Precio de entrada bajo, no "kits premium".**
10. **Gurús del flipping:** los casos de "gané USD 1.000 en una semana revendiendo" son sesgo de supervivencia y suelen vender cursos. Las medianas de este informe (USD 30-60 por semana por idea al arrancar) son la referencia honesta.
11. **Monotributo y tope:** en reventa, la facturación bruta crece mucho más rápido que la ganancia; recategorizar a tiempo.
12. **Seguridad personal:** las ventas presenciales con desconocidos implican riesgo físico. Lugar público, de día, acompañado en montos altos.

---

## Fuentes principales (todas consultadas el 2026-10-01)
- Comisiones y costos de ML: [algoritmodigital](https://algoritmodigital.com.ar/cuanto-es-la-comision-de-mercado-libre-por-vender/), [iProfesional](https://www.iprofesional.com/negocios/419524-como-calculo-a-cuanto-vender-productos-mercado-libre-para-no-perder-dinero), [NoticiasNQN 2026-09-10](https://www.noticiasnqn.com.ar/noticias/2026/09/10/352025-mercado-libre-cambia-una-de-sus-condiciones-y-desde-el-lunes-habra-envios-gratis-desde-15000), [jaguarsheet](https://jaguarsheet.com/es/blog/costo-fijo-mercado-libre).
- Liberación de dinero en ML: [UpSeller](https://upseller.com/es/blog-article-511).
- Retenciones: [jaguarsheet](https://jaguarsheet.com/es/blog/retenciones-mercado-libre), [iProfesional](https://www.iprofesional.com/impuestos/443223-nuevas-reglas-vendedores-mercado-libre-limites-percepcion-iva), [Contablix](https://contablix.ar/blog/impuestos-mercado-libre-2026-guia-definitiva).
- Mercado Pago: [yo-facturo](https://yo-facturo.com/blog/qr-mercado-pago-comisiones-cobrar/), [jonatanalmeira](https://www.jonatanalmeira.com/?p=70857).
- Monotributo: [Ámbito](https://www.ambito.com/informacion-general/aumentos-arca-cuanto-se-pagara-monotributo-partir-agosto-2026-n6304386), [El Sol](https://www.elsol.com.ar/el-pais/arca-actualizo-los-topes-de-facturacion-y-el-costo-del-monotributo-desde-agosto/), [yo-facturo](https://yo-facturo.com/blog/como-inscribirse-en-arca-por-primera-vez/).
- Consumo y fechas: [CAME vía La Capital](https://www.lacapital.com.ar/informacion-general/las-ventas-el-dia-la-madre-cayeron-35-y-marcaron-el-cuarto-ano-consecutivo-baja-n10225076.html), [Tiendanube CyberMonday](https://www.tiendanube.com/blog/cuando-es-el-cybermonday), [Canal26 cierres](https://www.canal26.com/economia/2026/03/10/locales-vacios-en-la-ciudad-de-buenos-aires-estas-son-las-principales-avenidas-con-mas-persianas-bajas/).
- Precios de referencia: [mejorescompras ventiladores](https://mejorescompras.com.ar/comparar/ventiladores), [mejorescompras bicicletas](https://mejorescompras.com.ar/comparar/bicicletas), [Frávega set matero](https://www.fravega.com/p/equipo-set-matero-completo-termo-mate-latas-y-canasta-matera-21283643/), [Servidos fletes](https://servidos.ar/servicios/mudanzas).
- Usados: [iProfesional muebles](https://www.iprofesional.com/finanzas/459474-mudanza-o-renovacion-donde-comprar-muebles-usados-en-excelente-estado-y-ahorrar-hasta-70), [iProfesional ropa circular](https://www.iprofesional.com/economia/458978-moda-circular-donde-comprar-y-vender-ropa-usada-de-calidad-a-los-mejores-precios), [Chequeado ropa importada](https://chequeado.com/el-explicador/ropa-usada-frontera-y-crisis-textil-que-hay-detras-del-fenomeno-que-tiene-a-jujuy-como-principal-puerta-de-entrada/).
- Legal: [Ley 2340 CABA](https://boletinoficial.buenosaires.gob.ar/normativaba/norma/101209), [Microjuris](https://aldiaargentina.microjuris.com/2014/09/26/rechazo-del-pedido-de-remuneracion-a-favor-del-corredor-inmobiliario-ante-la-falta-de-matriculacion-del-intermediario/), [Derecho en Zapatillas, comida casera](https://www.derechoenzapatillas.com/2019/que-dice-la-ley-sobre-la-venta-de-comida-casera/), [iProfesional transferencia de autos](https://www.iprofesional.com/autos/343934-cuanto-sale-la-transferencia-de-un-auto-en-argentina).
- Seguridad: [El Ancasti](https://www.elancasti.com.ar/opinion/el-nuevo-cuento-del-tio-marketplace-como-operan-los-estafadores-y-que-meta-no-los-frena-n590570), [Derecho en Zapatillas](https://www.derechoenzapatillas.com/2025/%f0%9f%8e%ae-mi-hermano-te-transfiere-la-nueva-vieja-estafa-del-marketplace/), [iProfesional celulares usados](https://www.iprofesional.com/tecnologia/352497-comprar-celulares-usados-claves-para-no-caer-en-enganos).
- Subastas y courier: [iProfesional Banco Ciudad](https://www.iprofesional.com/negocios/458739-subasta-banco-ciudad-julio-2026-como-participar-departamentos-desde-29000-dolares-autos-desde-500000-pesos), [Diario Panorama](https://www.diariopanorama.com/noticia/509427/aerolineas-incorpora-entrega-domicilio-compras-realizadas-estados-unidos).
- Tipo de cambio: [dolarapi.com](https://dolarapi.com/v1/dolares) (2026-10-01).
