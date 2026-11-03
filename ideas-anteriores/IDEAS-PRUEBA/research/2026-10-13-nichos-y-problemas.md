# Nichos y problemas — 250 investigados, 173 únicos (2026-10-13)

**Archivo para Facu:** `NICHOS-Y-PROBLEMAS.xlsx` (raíz del proyecto). Hojas: Cómo leer, Problemas, Ranking, Familias, Por nicho, Ya estaban antes.
**Datos crudos:** `research/datos/2026-10-13-nichos/*.json` (uno por nicho) + `parches/` (2.ª pasada y revisión de coherencia).
**Familias:** `research/datos/2026-10-13-familias.json`. **Script:** `research/datos/build_nichos_excel.py` (regenera el Excel).

## Qué se pidió

Facu (2026-10-13): un Excel de 200-300 opciones buenas (nicho → especialidad → problema), cada una con 2 soluciones que ya funcionan afuera y que en Argentina no existan o no sean conocidas. Es un embudo: se espera descartar 70-90%, filtrar junto con la hoja "Fase 2" a 5-10 y elegir UNA para arrancar.

## Cómo se hizo

1. **10 nichos × 5 especialidades × 5 problemas = 250 filas.** Nichos: Salud, Alimentación y gastronomía, Transporte y logística, Comercio y distribución, Construcción e inmuebles, Industria PyME, Servicios profesionales y back-office, Educación, Automotor, Agro (1 de 10: Facu lo conoce por CEMEVA pero no quiere ir 100% por ahí). Las especialidades las eligió Claude por tamaño estimado (estimación, no ranking verificado).
2. **1.ª pasada:** 10 investigadores en paralelo (uno por nicho). Cada solución extranjera se comprobó en su sitio oficial (WebFetch) o con búsqueda. Resultado: **500 de 500 soluciones verificadas**; las que no se pudieron comprobar se reemplazaron. La tracción es casi siempre lo que la empresa dice de sí misma.
3. **Se agotó la cuota de búsqueda (200)** a mitad de camino: 105 filas quedaron sin búsqueda (o con búsqueda incompleta) de presencia en Argentina.
4. **2.ª pasada:** 4 investigadores con tope de búsquedas completaron 101 filas (las otras 4 ya tenían búsqueda). Regla: con 1 búsqueda sin resultados, hueco máximo 4; 5 solo con 2 búsquedas vacías.
5. **Revisión de coherencia (Claude):** 7 filas con el mismo problema en distintos nichos tenían huecos contradictorios; se ajustaron con la evidencia de la fila gemela (`parches/e-revision-coherencia.json`).
6. **Familias transversales (Claude, opinión):** los 250 problemas se agruparon en 17 familias + "específicos del rubro".
7. **Limpieza de repetidas (pedido de Facu, Regla N.º 2):** cruce fila por fila contra las 633 de `TODAS-LAS-IDEAS.xlsx` y las ideas propias de la hoja "Fase 2" (`research/datos/2026-10-13-deduplicacion.json`). **65 repetían** algo anterior (mismo problema y mismo tipo de cliente) → hoja "Ya estaban antes", con la referencia; **12 eran el mismo problema en dos nichos** → fusionadas. **Quedan 173 únicas: 114 nuevas y 59 parecidas** (con referencia). Registro único para no repetir en el futuro: `research/datos/registro-de-ideas.csv` (897 entradas).

## Hallazgos (opinión de Claude, salvo que diga dato)

1. **El problema que más se repite entre rubros es back-office documental hecho a mano** (el "patrón CEMEVA"): 137 de 250 filas lo tienen marcado. Familias: pedidos por WhatsApp/mail/PDF, liquidaciones, recupero, facturas de proveedores, cobranza, listas de precios.
2. **Familia "pedidos que llegan por WhatsApp, mail o PDF y se cargan a mano"**: antes de la limpieza era la de mejor total (22/25), pero **repetía B28 y D37 de las 633** (salió a "Ya estaban antes"). Dato nuevo que aporta a esas ideas viejas: afuera cobran Choco, Conexiom y REKKI; acá ya están Galo AI (startup argentina con inversores), Duotach (a medida) y Softland Pedidos IA. Quedan como nuevas solo LOG-1-4 (pedidos de flete) e IND-4-5 (talleres de estampado).
3. **Familia "recupero" (plata que se pierde por no controlar o reclamar)**: mayor hueco en Argentina (4,1 promedio). Se puede cobrar a éxito. Destacan (las dos son nuevas): notas de débito de cadenas a proveedores (COM-1-4, fusionada con ALI-3-5: nada local en 2 búsquedas) y control de facturas de flete (LOG-1-2, fusionada con AGR-3-4). **A verificar:** cambio de AFIP (2019) sobre quién emite notas de débito.
4. **Corrección importante:** "documentación de terceros" (fleteros, contratistas) tiene competencia local fuerte para empresas grandes: Certronic (más de 40.000 contratistas por día según ITSitio, 2025-09-26), Avancargo, FlowDocs. Capacitación de operarios: RogerThat y Humand (US$66 M según El Economista). Esto baja varias filas que parecían muy buenas.
5. **Para descartar como familia:** atención al cliente con chatbots (hueco 2,6, 8 nichos, saturado), fintech (capital y regulación), capacitación (ya cubierta).

## Top 10 de las 173 únicas (puntajes = opinión de los investigadores)

| # | ID | Problema | Total | Hueco AR | ¿Nueva? |
|---|---|---|---|---|---|
| 1 | IND-2-5 | Controles de calidad en papel y certificados por lote armados a mano | 24 | 5 | parecida a C25 (ISO 9001) |
| 2 | LOG-1-4 | Pedidos y cotizaciones de fletes por mail y WhatsApp cargados a mano | 24 | 5 | nueva |
| 3 | AGR-3-1 | Contratistas rurales registran labores y facturan hectáreas en papel | 23 | 5 | nueva |
| 4 | IND-3-2 | Marcas no saben qué tiene ni cuándo entrega cada taller tercerizado | 23 | 5 | nueva |
| 5 | LOG-1-2 | Control manual de facturas de flete contra viajes y tarifas (+ AGR-3-4) | 23 | 4 | nueva |
| 6 | ALI-1-5 | Pronóstico de producción diaria en cocinas y panaderías (+ ALI-2-1) | 22 | 5 | parecida a C7 |
| 7 | COM-1-4 | Notas de débito y deducciones de cadenas a proveedores (+ ALI-3-5) | 22 | 5 | nueva |
| 8 | CON-4-4 | Vencimientos legales del edificio controlados de memoria | 22 | 5 | nueva |
| 9 | AUT-1-4 | Talleres de camiones: órdenes, aprobaciones y facturación a mano | 22 | 4 | nueva |
| 10 | COM-3-2 | Presupuestos de materiales armados a mano desde listas por WhatsApp | 22 | 4 | parecida a K2 |

## Límites (Regla N.º 1)

- Los puntajes los pusieron 10 investigadores distintos: no son perfectamente comparables entre nichos.
- "No encontrado en Argentina" sale de 1-2 búsquedas rápidas: no prueba que no exista. Antes de elegir, búsqueda a fondo.
- Leyes y normas citadas en las filas (Ley 27.802 sobre contratistas, RG de ARCA, Decreto 407/2026, etc.) están marcadas como no verificadas en el Boletín Oficial.
- La demanda de afuera no prueba que alguien pague en Argentina (advertencia de F36 que sigue vigente).

## Próximo paso

Facu marca en la hoja "Problemas" (columna "Me gusta" o pintando). Después: cruzar sus marcas con la hoja "Fase 2" de `TODAS-LAS-IDEAS.xlsx` → 5-10 finalistas → búsqueda a fondo de competencia local + mapeo del proceso solo en las finalistas → elegir UNA.
