# Nichos y problemas 2 — 500 investigados, 365 únicos (2026-10-14 / 2026-10-15)

**Archivo para Facu:** `NICHOS-Y-PROBLEMAS-2.xlsx` (raíz del proyecto). Hojas: Cómo leer, Problemas, Ranking, Familias, Por nicho, Ya estaban antes.
**Datos crudos:** `research/datos/2026-10-14-nichos-2/*.json` (uno por nicho) + `parches/` (2.ª y 3.ª pasada) + `dedup/` (limpieza por partes).
**Consignas:** `CONSIGNA.md` (investigadores), `CONSIGNA-LIMPIEZA.md` (Regla N.º 2), `CONSIGNA-2A-PASADA.md` (presencia en Argentina), en la misma carpeta.
**Limpieza:** `research/datos/2026-10-14-deduplicacion-2.json`. **Familias:** `research/datos/2026-10-14-familias-2.json`.
**Scripts:** `research/datos/build_nichos2_excel.py` (arma el Excel; copia adaptada de `build_nichos_excel.py`, que no se tocó), `research/datos/cruce_registro_nichos2.py` (cruce automático por palabras), `research/datos/build_registro.py` (actualizado: ahora incluye esta búsqueda).

## Qué se pidió

Facu (2026-10-14): una búsqueda nueva "por las dudas", con la misma estructura que `NICHOS-Y-PROBLEMAS.xlsx`, sin repetir NADA de lo investigado (ni ganadores ni rechazados). Aprobó 10 nichos y pidió sumar 10 más ("extendé la búsqueda").

## Cómo se hizo

1. **20 nichos × 5 especialidades × 5 problemas = 500 filas.** Nichos: turismo y hotelería; deporte, gimnasios y clubes; mascotas (sin veterinarias); belleza y cuidado personal; eventos; energía y servicios; seguridad privada y barrios cerrados; reciclaje y residuos; proveedores de petróleo y minería; alquiler de equipos; municipios; telecomunicaciones chicas; estacionamientos y movilidad; mudanzas y guarda; comercios especializados; hogar y jardín; funerarias y previsión; cultura y espectáculos; ONGs, iglesias, cooperativas y mutuales; familias y cuidado infantil. Especialidades propuestas por Claude y aprobadas por Facu.
2. **1.ª pasada:** 20 investigadores en paralelo, cada uno con el registro completo (902 entradas) como lista de exclusión y tope de 8 búsquedas. Las soluciones extranjeras se verificaron en su sitio (WebFetch o descarga directa cuando WebFetch quedó limitado).
3. **Limpieza (Regla N.º 2):** cruce automático por palabras + 4 revisores fila por fila + revisión de Claude (6 ajustes de coherencia, ver `ajustes_de_claude` en el JSON de limpieza) + 59 grupos de fusión (mismo problema en dos o más nichos nuevos).
4. **Familias transversales:** 25 (24 + "específicos del rubro"), clasificadas por un agente; opinión, no dato.
5. **2.ª y 3.ª pasada (presencia en Argentina):** solo sobre las filas que quedaron después de la limpieza (para no gastar búsquedas en filas que salían). Se cortó una vez porque venció la sesión (2026-10-14 a la noche) y se relanzó el 2026-10-15. También se verificaron o reemplazaron las soluciones extranjeras que habían quedado sin verificar.

## Números

| | Cantidad |
|---|---|
| Investigadas | 500 |
| Salieron por **repetir** algo anterior | 3 (FAM-1-5 = EDU-1-4; MUD-5-4 = L1/A1; ESP-4-1 = COM-3-5) |
| Salieron por **parecerse a algo que Facu NO eligió o rechazó** | 69 |
| Fusionadas en otra fila (mismo problema en dos nichos nuevos) | 63 |
| **Quedan** | **365: 212 nuevas + 153 parecidas a un ganador de Facu** (quedan como variantes, con la referencia) |
| Soluciones extranjeras verificadas | 990 de 1.000 (las 500 filas originales; las que no se pudieron verificar se reemplazaron o quedaron marcadas "no") |
| Filas que quedan sin ninguna búsqueda en Argentina | 14 de 365 |
| Filas que quedan con "patrón CEMEVA" (papeles hechos a mano) | 71 de 365 (19%; en el primer Excel eran 57%) |

Los temas que más salieron por parecerse a rechazados: ruteo y prueba de entrega, fotos de daños, bolsas de personal por turno, cotizar a muchos proveedores, precios dinámicos, ahorro de energía, liquidaciones en Excel, turnos y agendas.

## Top 10 (por total /25; puntajes = opinión de los investigadores)

| # | ID | Problema | Total | Hueco AR | ¿Nueva? |
|---|---|---|---|---|---|
| 1 | BEL-1-1 | En peluquerías la tintura se prepara a ojo: se tira producto y el color no se costea por gramo | 22 | 4 | parecida a L14 |
| 2 | MUN-2-1 | Baches detectados tarde y por reclamo: cámara en vehículos municipales (+ inventario de señales) | 22 | 4 | parecida a L10/L12 |
| 3 | PET-1-3 | Proveedores petroleros cargan cada factura y certificado en el portal de cada operadora | 22 | 4 | nueva |
| 4 | PET-3-1 | Coordinar camiones de arena entre cantera, planta y set de fractura | 22 | 4 | parecida a L6 |
| 5 | CUL-1-1 | Equipos técnicos de teatros y salas sin inventario | 21 | 4 | parecida a L13/L14 |
| 6 | PET-3-5 | Traslado diario de miles de operarios a locación armado a mano | 21 | 4 | parecida a EDU-1-5 |
| 7 | RES-2-2 | Volqueteras que no saben dónde está cada volquete ni cuántos días lleva (+ ALQ-2-2) | 21 | 4 | nueva |
| 8 | SEG-1-2 | Portería de planta o depósito que controla camiones, patentes y remitos a mano | 21 | 4 | parecida a L12 |
| 9 | TEL-3-2 | Instalaciones de fibra mal hechas que nadie revisa por foto | 21 | 4 | parecida a D36 |
| 10 | ALQ-1-1 | Equipos y herramientas alquilados que se pierden entre obras (+ PET-2-4) | 20 | 4 | parecida a L13 |

**Ninguna fila tiene hueco 5:** en la 2.ª y 3.ª pasada cada fila tuvo una sola búsqueda (la regla dice que 5 necesita dos búsquedas vacías).

## Familias que más se repiten (por cantidad de nichos)

| Familia | Problemas | Nichos | Total promedio | Hueco AR promedio |
|---|---|---|---|---|
| Registros obligatorios, certificados, vencimientos y libros en papel | 21 | 16 | 15,8 | 3,6 |
| Sensores y monitoreo remoto | 26 | 16 | 15,6 | 3,4 |
| **Rastreo de activos y equipos que se pierden (RFID/QR/GPS)** | 19 | 13 | **19,1** (el mejor) | 3,6 |
| Financiar el acceso: cuotas, seguros, garantías, alquiler en vez de compra | 21 | 13 | 14,7 | 3,7 |
| Mano de obra por turno y prestadores verificados | 15 | 12 | 14,7 | 3,1 |
| Evidencia: prueba de servicio hecho (fotos, GPS, NFC) | 12 | 11 | 17,6 | 3,1 |
| Visión por computadora y cámaras con IA | 18 | 10 | 15,7 | 3,5 |
| Reventa, segunda mano y economía circular | 29 | 9 | 15,3 | 3,1 |

## Hallazgos (opinión de Claude, salvo que diga dato)

1. **El territorio más fuerte es "cosas que se pierden": rastreo de activos.** Es la familia con mejor promedio (19,1) y aparece en 13 de 20 nichos: equipos de alquiler, andamios, volquetes, garrafas, vajilla de eventos, equipos de teatros, bicis y kayaks, cajas de archivo, ropa blanca de hoteles. Es casi el mismo producto en todos (etiqueta QR/RFID + app de escaneo + disponibilidad por fecha + quién lo tiene), o sea **producto global**, tecnología física y la experiencia de stock de Facu (Sporting). Conecta con sus ganadores L13 (RFID) y L14 (piezas chicas). Ojo: en rubros grandes (andamios, maquinaria) pueden existir sistemas locales que 1 búsqueda no encontró.
2. **Petróleo y minería tuvo el mejor promedio por nicho (17,6)** pero son pocos clientes, con venta por contactos y certificaciones. PET-1-3 (cargar facturas en los portales de cada operadora) es casi exactamente el bot que Facu ya hizo en CEMEVA.
3. **La 2.ª y 3.ª pasada bajaron varios huecos** que parecían libres (datos con fuente en cada fila): L'Oréal ya ofrece prueba virtual de color a profesionales (BEL-1-3); AgendaPro tiene consentimientos digitales (BEL-2-3); SADAIC cobra derechos afuera (CUL-3-1); La Plata ya controla el estacionamiento medido con cámaras lectoras de patentes (MUN-1-4); Pilar, Río Negro y ARBA detectan construcciones no declaradas con imágenes satelitales (MUN-1-2); CABA revisa planos con IA, "Model BA" (MUN-3-2); PictureThis ya está en Argentina (HOG-2-5); la cremación directa ya existe en funerarias tradicionales (FUN-4-3).
4. **El patrón CEMEVA bajó de 57% a 19%**: esta vez dominan sensores, cámaras, rastreo y marketplaces, que es lo que Facu dijo que le atrae (2026-10-14).
5. **153 filas son "parecidas a un ganador"**, casi todas por tecnología (L12 cámaras, L13 RFID, L14 stock, L10 foto, L6 logística): sus ganadores de tecnología física se pueden aplicar en muchos rubros. Eso refuerza elegir una **tecnología** y después buscarle el rubro de entrada, en vez de al revés.

## Límites (Regla N.º 1)

- Los puntajes los pusieron 20 investigadores distintos: no son exactamente comparables entre nichos. No incluyen los criterios de Facu "me gusta" ni "producto global" (este último va en una columna aparte, opinión del investigador).
- Presencia en Argentina: 1 búsqueda por fila en la mayoría. "No encontrado" no prueba que no exista. 14 filas quedaron sin ninguna búsqueda (marcadas "sin buscar").
- DuckDuckGo pedía captcha (no se resolvió; un investigador lo consultó una vez por error, sin resolver nada); Brave por WebFetch daba 429 enseguida; Bing devolvía resultados irrelevantes. Por eso la presencia en Argentina es la parte más floja.
- La tracción de las empresas extranjeras es casi siempre lo que dicen de sí mismas. Leyes y normas citadas (ej. Res. SE 64/2026 sobre envases de GLP, Decreto 144/2022 sobre guarderías, Ley 24.901) no se verificaron en el Boletín Oficial.
- La limpieza R ("parecida a algo no elegido") es criterio: puede haber sacado alguna fila que Facu vería distinta. Están todas en la hoja "Ya estaban antes" con el motivo.

## Próximo paso

Facu marca la hoja "Problemas" de `NICHOS-Y-PROBLEMAS-2.xlsx` (columna "Me gusta" o pintando). Después: sumar sus marcas a la hoja "Fase 2" de `TODAS-LAS-IDEAS.xlsx`, reordenar con los 7 criterios de "Orden de Claude" y pasar a la búsqueda a fondo de las finalistas.
