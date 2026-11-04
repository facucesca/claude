# Proyecto: buscar el negocio para ganarse la vida (escalable a gran escala)

## Al empezar cada conversación (leer primero)
Si el primer mensaje es un saludo ("hola") o no dice qué hacer:
1. Saludar y avisar que se está preparando todo. El hook `.claude/hooks/session-start.sh`
   instala lo necesario (`requirements.txt`: openpyxl para los Excel, etc.) y deja escrito
   "INSTALACIÓN: ...". Si falló, explicarlo en palabras simples.
2. Contar **en qué está el proyecto** (sección "Estado y próximos pasos") en 4 o 5 líneas.
3. Proponer **el próximo paso concreto** y preguntar si arrancamos por ahí.

Después de cambiar algo: actualizar "Estado y próximos pasos" y **hacer commit y push**, para
que no se pierda nada.

## Para qué es este proyecto
Investigar a fondo **ideas de negocio nuevas** y quedarse con **la mejor para ganarse la vida**:
un negocio propio, **escalable a gran escala** (que pueda crecer mucho sin que el trabajo o el
costo crezcan igual), no un ingreso chico ni un trabajo a medida por cliente.

Se trabaja con **investigación profunda + Excels**: cada búsqueda termina en un `.xlsx` para
leer, marcar en colores y comentar, más un resumen en `investigaciones/`.

## REGLA N.º 1 — Nada inventado
- Nunca inventar datos, cifras, fuentes, nombres ni resultados. Si no se sabe o no se pudo
  verificar, se dice.
- Separar siempre: **dato verificado** (con link y fecha), **estimación propia** (marcada,
  con el razonamiento) y **opinión de Claude** (marcada).
- No dar la razón por dar la razón: si una idea es mala, se dice con datos.
- Fechas siempre absolutas (2026-11-03, nunca "hace un mes").

## REGLA N.º 2 — No coincidir con nada de lo anterior (pedido explícito, 2026-11-03)
Lo nuevo **no puede repetir ni parecerse** a nada de lo que ya se investigó:
- **Todo `ideas-anteriores/IDEAS-PRUEBA/`** (≈1.500 ideas y problemas ya vistos, elegidos o
  descartados). La lista única está en
  `ideas-anteriores/IDEAS-PRUEBA/research/datos/registro-de-ideas.csv` (633 de
  `TODAS-LAS-IDEAS.xlsx`, 250 de `NICHOS-Y-PROBLEMAS.xlsx`, 500 de `NICHOS-Y-PROBLEMAS-2.xlsx`,
  129 de `GIMNASIO-DE-IDEAS.xlsx`, ideas propias de "Fase 2") **más** lo que haya en
  `MARCAS-DE-FACU.xlsx`, `ideas/` y `proyectos/` de esa carpeta que no esté en el registro.
- **El proyecto de juguetes de madera** (`backup-juguetes-madera/`) y todo lo que se le parezca
  (kits educativos, juguetes, STEM).
- **Las investigaciones nuevas entre sí** (lo que ya esté en `investigaciones/`).

Cómo se aplica:
1. **Antes:** pasarle a cada investigador la lista de exclusión (el registro + los temas de
   arriba): "no propongas nada que esté acá ni que comparta el mismo problema y el mismo tipo
   de cliente".
2. **Después, antes de entregar:** cruzar fila por fila contra el registro (primero automático
   por palabras, después a mano). Lo repetido o parecido **sale** de la lista principal (va a
   una hoja aparte "Descartadas por parecido", con la referencia a la idea vieja).
3. **Al entregar:** decir cuántas quedaron nuevas y cuántas salieron por parecido.
4. **Al final:** sumar lo nuevo al registro de esta carpeta: `investigaciones/registro-nuevo.csv`
   (mismas columnas que el registro viejo), para que la próxima búsqueda tampoco lo repita.

## REGLA N.º 3 — Ideas para ganar plata, no apps que regalan algo (pedido de Facu, 2026-11-04)
Facu rechazó las ideas tipo "foto de tu factura y la IA te la explica": eso lo hace ChatGPT gratis y
nadie paga. Toda idea tiene que pasar estas 3 preguntas antes de entrar a una lista:
1. **¿Lo resuelve ChatGPT gratis en 2 minutos?** Si sí, se descarta (salvo que la plata salga de otro lado).
2. **¿Por dónde pasa la plata?** Tiene que haber margen sobre un producto, comisión sobre una venta,
   un cliente empresa que paga, o plata que circula por nosotros. "Suscripción de la persona" sola no alcanza.
3. **¿Por qué nos necesitan?** Algo que el otro no consigue solo: oferta juntada, logística, operación
   física, contactos, confianza o garantía, permisos, datos propios. La IA es la herramienta, no el negocio.

## Criterios para evaluar cada idea (puntaje 1 a 5, se explica cada uno)
1. **Escala:** ¿puede llegar a miles o millones de clientes / varios países? ¿El costo por
   cliente nuevo baja con el tamaño?
2. **Tamaño del mercado:** cuánta gente o empresas tienen el problema y cuánto pagan hoy (con fuente).
3. **Quién paga y por qué ahora:** cliente claro, dolor real, qué cambió (tecnología, ley, costumbre).
4. **Hueco:** competencia en Argentina, LATAM y el mundo (con links). Si ya existe igual, se dice.
5. **Arranque barato:** se puede validar con poca plata (ver perfil) en 30 a 60 días.
6. **Construible con lo que hay:** Claude Code + no-code + amigos que programan; sin depender
   de saber programar uno mismo.
7. **Riesgo:** regulación, dependencia de una sola plataforma, plata de terceros, legal.
8. **Ventaja propia:** qué tiene el usuario que otros no (ing. industrial, CEMEVA/granos,
   Tucumán, contactos).

## Perfil del usuario (resumen; detalle en `ideas-anteriores/IDEAS-PRUEBA/MEMORY.md`)
- Facu, 22 años, Argentina (Tucumán), por recibirse de **ingeniero industrial**. Quiere negocio
  propio, sin relación de dependencia; apunta a algo grande (startup).
- Ahorros ~USD 1.300 a oct-2026 (no arriesgarlo entero). Inglés básico. No le gusta mostrar la cara.
- No programa, pero ya llevó con Claude una app a producción (CEMEVA, empresa de granos del papá).
- Le atraen: tecnología del mundo físico (cámaras, RFID, foto con IA), apps que conectan dos
  partes, automatizar papeles y procesos **si es producto igual para muchos** (no a medida).
- Si estos datos cambiaron, preguntar y actualizar acá.

## Estado y próximos pasos (actualizar cada vez que cambie algo)
- **2026-11-03:** se reorganizó el proyecto. El de juguetes de madera **no funcionó** y quedó
  como **backup** en `backup-juguetes-madera/`. Se cargó la carpeta de ideas anteriores
  (`ideas-anteriores/IDEAS-PRUEBA/`) como lista de exclusión.
- **2026-11-03 — investigación en curso** (datos en `investigaciones/datos/2026-11-03/`):
  pedido del usuario: **sin límite de plata, medio y largo plazo, cualquier nicho, nada repetido**.
  - Tanda A (6 investigadores × 30): gran escala — megatendencias, ventajas de Argentina,
    deeptech, industria B2B, "picos y palas" de las olas, modelos grandes que no son app.
  - Tanda B (6 × 20, pedida después): **cosas chicas y cotidianas, fuera de la caja, que le den
    la vuelta a algo, con potencial de startup** — objetos cotidianos, modelos dados vuelta,
    tiempo muerto, costumbres argentinas, vida adulta joven, lo que sobra.
  - **Terminada.** 300 ideas → 232 nuevas tras sacar 57 repetidas entre investigadores y 11
    parecidas a lo anterior (`descartes.json`). Excel: `investigaciones/2026-11-03-IDEAS-NUEVAS.xlsx`;
    resumen: `investigaciones/2026-11-03-ideas-nuevas.md`; registro: `investigaciones/registro-nuevo.csv`.
    Se regenera con `python3 investigaciones/datos/2026-11-03/build_excel.py`.
  - 21 ideas quedaron **SIN VERIFICAR** y 97 **parciales** (se agotó el cupo de 200 búsquedas web
    por turno). Verificar antes de profundizar cualquiera de esas.
- **2026-11-04 — investigación C terminada** (`investigaciones/datos/2026-11-04/`): ideas **chicas, en
  nichos, fáciles de lanzar**, que destraban **cuellos de botella con app / web / WhatsApp + IA** y dan la
  vuelta a algo que ya existe; cada una trae la "jugada mental" y hay 30 LECCIONES para entrenar la cabeza.
  6 ángulos: salud, ingeniería industrial en una app, mundo real + IA, formas de pagar, agregar valor,
  personas afectadas. 120 → **105 nuevas** (10 repetidas internas + 5 parecidas a lo anterior).
  Excel: `investigaciones/2026-11-04-IDEAS-NICHOS-Y-APPS.xlsx`; resumen: `investigaciones/2026-11-04-ideas-nichos-y-apps.md`.
  Competencia en Argentina y mercado casi siempre "Parcial" (se limitó a 30 búsquedas por investigador
  para cuidar el uso). Todas sumadas a `investigaciones/registro-nuevo.csv`.
- **2026-11-04 — Facu rechazó las 337 ideas** ("rebuscadas", "superficiales", "eso lo hace ChatGPT
  gratis"). Pidió más profundidad: **empresas reales que funcionan afuera (China, India, etc.) y no
  existen en Argentina**, con lectura real de páginas (abrió la red del entorno). Nació la Regla N.º 3.
- **2026-11-04 — investigación "afuera" en curso** (`investigaciones/datos/2026-11-04-afuera/`):
  Fase 1 = 6 exploradores por región (China; India; Sudeste Asiático + Japón/Corea; Brasil/México/
  Colombia/Chile/Perú; Turquía + Europa; África + Medio Oriente), 15 empresas cada uno, filtro duro.
  Fase 2 = filtro de Claude → 20-25. Fase 3 = ficha a fondo de cada una (unidad económica, por qué
  funcionó allá, si se da en Argentina, competencia verificada, regulación, cómo arrancar).
  - Fase 1 terminada: 74 empresas (`f1-*.json`). Fase 2: lista corta de 22 en `FASE2-lista-corta.md`.
    A Facu le gustó. Pidió **otra ronda con empresas nuevas** antes de las fichas a fondo.
  - **Ronda 2 terminada:** 61 empresas más (`r2-*.json`). Total 135; **lista corta de 40 modelos**.
    Excel: `investigaciones/2026-11-04-EMPRESAS-DE-AFUERA.xlsx` (regenerar con `build_excel.py` de esa
    carpeta; la lista corta está en `lista_corta.json`). Resumen: `investigaciones/2026-11-04-empresas-de-afuera.md`.
  - **Próximo:** que Facu elija cuáles van a fase 3 (ficha a fondo) o que Claude elija las 10-15 mejores.
  - **Ronda 3 terminada** (`r3-*.json`): 8 exploradores por rubro → 66 empresas; 17 a la lista corta.
    **Total: 201 empresas, lista corta de ~57 modelos** en `2026-11-04-EMPRESAS-DE-AFUERA.xlsx`.
    Todas sumadas a `registro-nuevo.csv` (ids EMP-001…). Exclusión para la próxima: `exclusion-ronda3.txt`
    + `empresas-ronda2.txt` + las r3 (regenerar antes de otra ronda).
  - **Próximo:** fase 3 (ficha a fondo) de las que elija Facu, o las 10-15 mejores elegidas por Claude.
- **Pendiente de Facu (opcional):** marcar en colores los dos Excel (`2026-11-03-IDEAS-NUEVAS.xlsx` y `2026-11-04-IDEAS-NICHOS-Y-APPS.xlsx`).
- **Después:** Excel con las ideas nuevas puntuadas → el usuario marca → investigación a fondo
  de las marcadas → elegir 1 y armar el plan de validación.

## Mapa de carpetas
| Carpeta / archivo | Qué hay |
|---|---|
| `investigaciones/` | Lo nuevo: un `.md` por investigación (`AAAA-MM-DD-tema.md`), sus Excel y `registro-nuevo.csv`. |
| `ideas-anteriores/IDEAS-PRUEBA/` | Todo lo investigado antes (sep-oct 2026). **Solo consulta y exclusión, no se repite.** Sus reglas viejas en `CLAUDE-anterior.md`. |
| `backup-juguetes-madera/` | Proyecto de juguetes de madera con electrónica, guardado tal cual. Sus instrucciones en `CLAUDE-juguetes.md`. **No tocar** salvo que el usuario lo pida. |
| `herramientas/md_a_pdf.py` | Pasa un `.md` a PDF para imprimir. |

## Notas para Claude
- Responder en español, simple y directo.
- Toda afirmación de mercado lleva link y fecha; usar números medianos, no casos virales.
- Siempre chequear cómo se cobra y opera desde Argentina.
- Los Excel: una fila por idea, columnas con explicación simple, cliente, cómo gana plata,
  escala, competencia (links), puntajes, fuentes, y una columna vacía "Mis comentarios".
  Se generan con un script en `investigaciones/datos/` para poder regenerarlos.
