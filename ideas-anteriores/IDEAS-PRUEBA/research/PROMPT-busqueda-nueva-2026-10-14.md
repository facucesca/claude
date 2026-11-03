# Prompt para una búsqueda nueva en otro chat (preparado el 2026-10-14)

Copiar todo lo que está dentro del bloque y pegarlo como primer mensaje en un chat nuevo de este proyecto (C:\FACU\IDEAS-PRUEBA).

```
Hola. Vamos a hacer una búsqueda NUEVA de oportunidades de negocio, distinta de todo lo que ya investigamos en este proyecto. Es "por las dudas": en la hoja "Fase 2" de TODAS-LAS-IDEAS.xlsx ya tengo 74 ganadores ordenados (hoja "Orden de Claude"). Esta búsqueda NO puede repetir NADA de lo ya investigado: ni lo que elegí (ganadores) ni lo que no elegí, rechacé o descarté. No quiero volver a ver ni a rechazar las mismas ideas con otro nombre.

ANTES DE EMPEZAR, LEÉ:
1. CLAUDE.md completo. Respetá la REGLA N.º 1 (nada inventado: separar dato / estimación / opinión, decir "no lo pude verificar") y la REGLA N.º 2 (no repetir nada entre investigaciones).
2. MEMORY.md (estado del proyecto, sobre todo las entradas del 2026-10-13 y 2026-10-14).
3. research/datos/registro-de-ideas.csv: tiene TODO lo ya investigado (902 entradas: las 633 ideas, mis ideas propias con id "L1 (propia)"... y los 250 problemas de NICHOS-Y-PROBLEMAS). La columna decision_facu dice qué elegí (75), qué no elegí o rechacé (759), qué descarté y qué estaba repetido. TODO el registro es la lista de exclusión: ganadores Y rechazados.
4. research/2026-10-13-nichos-y-problemas.md y research/2026-10-14-marcas-de-facu-nichos.md: cómo se hizo la búsqueda anterior y qué me gustó.

QUÉ QUIERO:
Un Excel nuevo, NICHOS-Y-PROBLEMAS-2.xlsx, con la misma estructura del anterior: nicho → especialidad → problema concreto → 2 soluciones (empresas o productos) que YA funcionan afuera con clientes pagando y que en Argentina no existan o no sean conocidas. Unas 200-250 filas antes de limpiar.

NICHOS: NO repitas los 10 que ya hicimos (Salud; Alimentación y gastronomía; Transporte y logística; Comercio y distribución; Construcción, vivienda e inmuebles; Industria y manufactura PyME; Servicios profesionales y back-office; Educación; Automotor; Agro). Elegí unos 10 nichos nuevos que atraviesen la vida de mucha gente o de muchas empresas. Ejemplos para elegir o reemplazar con criterio: turismo y hotelería; deporte, gimnasios y clubes; mascotas (más allá de veterinarias); belleza, peluquerías y estética; eventos y salones; energía, solar y servicios públicos; seguridad privada y barrios cerrados; reciclaje y residuos; proveedores de minería y petróleo (Vaca Muerta); municipios y gobierno local; ONGs, iglesias y clubes de barrio; hogar y consumo de las personas; medios y entretenimiento. Antes de lanzar la investigación, mostrame los 10 nichos y las 5 especialidades de cada uno en una tabla corta, y esperá mi OK.

LO QUE ME GUSTA (usalo para elegir problemas, no para inventar demanda):
- Tecnología del mundo físico: cámaras con IA, RFID, sensores, rastreadores, identificar cosas por foto.
- Apps que conectan dos partes (intermediarios).
- Automatizar papeles y mejorar procesos (soy ingeniero industrial), PERO como producto global, igual para muchos clientes. NO trabajo a medida empresa por empresa.
- Mis ventajas: stock y depósito (pasantía en Sporting), logística y fleteros, procesos, y CEMEVA (dirigí con Claude una app de escritorio real en producción y un bot que carga datos en sistemas viejos).
- Criterios con los que después voy a filtrar: producto global, que me guste, mercado grande, hueco en Argentina, construible con Claude sin mucho capital, regulación manejable, mi ventaja.

CÓMO HACERLO:
- Investigadores en paralelo, uno por nicho, cada uno con la lista de exclusión del registro completo (ganadores y rechazados) y con la consigna: "no propongas nada que ya esté acá, ni algo parecido a lo que Facu no eligió o descartó; si encontrás datos nuevos sobre algo de la lista, anotalo como dato de esa idea, no como fila nueva".
- Cada empresa de afuera se verifica en su sitio oficial (WebFetch) o con búsqueda; la tracción solo con fuente; la presencia en Argentina con al menos una búsqueda ("no encontré" no es "no existe").
- OJO con la cuota de WebSearch (200 compartidas): poné un tope por investigador (unas 18) y usá WebFetch para verificar empresas. Si quedan filas sin búsqueda en Argentina, hacé una segunda pasada con tope.
- Guardá los datos en research/datos/2026-10-XX-nichos-2/ (un JSON por nicho, mismo esquema que research/datos/2026-10-13-nichos/01-salud.json).
- Armá el Excel copiando y adaptando research/datos/build_nichos_excel.py a un script nuevo (no pises el anterior ni NICHOS-Y-PROBLEMAS.xlsx).

ANTES DE ENTREGARME (REGLA N.º 2):
- Cruzá cada fila contra el registro completo (automático por palabras y después a mano):
  * Repetida (mismo problema y mismo tipo de cliente que algo anterior, sea ganador o rechazado) → sale; va a la hoja "Ya estaban antes" con la referencia.
  * Parecida a algo que NO elegí, rechacé o descarté → también sale (hoja "Ya estaban antes"): no quiero volver a rechazarla.
  * Parecida a un ganador → puede quedar, marcada con la referencia (sirve como variante).
  * Mismo problema en dos nichos nuevos → una sola fila con "también aparece en".
- Agregá las familias transversales (como en la búsqueda anterior).
- Actualizá research/datos/build_registro.py para que incluya la búsqueda nueva y regenerá el registro.
- Decime cuántas quedaron nuevas, cuántas parecidas a ganadores, cuántas salieron por repetir o parecerse a rechazadas, el top 10 y las familias que más se repiten.

NO TOQUES: TODAS-LAS-IDEAS.xlsx, NICHOS-Y-PROBLEMAS.xlsx (tienen mis marcas) ni la carpeta C:\FACU\CEMEVA. Documentación en español y fechas absolutas. Al terminar, actualizá MEMORY.md, el "Estado" del CLAUDE.md e ideas/LISTA-DE-IDEAS.md.
```
