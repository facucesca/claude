# Proyecto: Juguetes de madera con electrónica para armar

## La idea
Kits de juguetes de madera (MDF / fibrofácil cortado con láser) que se combinan con
electrónica simple. Los chicos arman el juguete, conectan el circuito y aprenden
jugando. Referencias que marcan el rumbo:
- [Wooden RGB House](https://market.samm.com/en/wooden-rgb-house): casita de madera con LEDs, interruptor y pilas.
- [Kit de 4 vehículos de madera (Funduino)](https://funduinoshop.com/en/diy-workshop/kits/chassis/diy-kit-of-4-wooden-vehicles): unos 13,35 €.
- [Eureka / Small Machines](https://littlebirdelectronics.com.au/products/eureka-build-your-own-kits.json): madera con mecanismos, sin electrónica.

## Reglas del proyecto
- **Lo más barato posible.** Cada decisión se mide por el costo por kit.
- **Nada de soldar.** Solo conectores fáciles: bornes a presión, portapilas con
  cables, clips cocodrilo, cinta de cobre o conectores tipo JST ya armados.
- **Circuitos sencillos.** Pila, interruptor, LED, motorcito y zumbador. Arduino o
  microcontrolador solo en una línea "avanzada" (chicos más grandes o adultos).
- **Seguridad para chicos.** Usar pilas AA/AAA en portapilas con tornillo. Evitar
  pilas de botón (CR2032), que son peligrosas si se tragan. Bordes lijados, sin
  piezas chicas sueltas en los kits para chicos chicos.
- **Plantillas:** usar libres solo si la licencia permite uso comercial. Si no,
  diseñarlas nosotros (MDF de 3 mm, archivos SVG/DXF).

## Datos del usuario
- Ubicación: **Tucumán, Argentina** (puede comprar de cualquier lado).
- No tiene láser ni CNC, pero **conoce gente que corta**.
- Fecha objetivo: **Navidad 2026**.
- Edad de los chicos: sin definir. Propuesta: 6 a 10 años (ver más abajo).
- Venta: **todavía sin decidir** si es para vender o uso personal.

## Plan de trabajo
1. [x] Ver plantillas y juguetes de referencia (primera búsqueda hecha).
2. [ ] Proveedores de madera / servicios de corte láser (prioridad: Tucumán y NOA).
3. [x] Proveedores de electrónica (local, Mercado Libre, AliExpress / Temu).
4. [ ] Diseñar 1 prototipo y calcular el costo real por kit.
5. [ ] Decidir: venta chica de prueba, taller o regalo.

## Plantillas propias (carpeta `plantillas/`)
- `plantillas/auto-motor-goma/`: auto con motor DC 130, transmisión por goma a
  polea en el eje trasero, pulsador y 2 pilas AA. MDF 3 mm, hoja de 30 x 20 cm,
  13 piezas. **v1 sin probar**: ajustar ranuras y huecos con el primer corte.
- `plantillas/auto-clasico/`: **v2 linda y de calidad** del mismo auto.
  Carrocería clásica con ventanillas caladas, grabados (puertas, parrilla,
  patente), cubiertas de goma (o-ring) y techo removible para las pilas. Hoja de
  40 x 30 cm, 30 piezas. Se regenera con `generar.py` según el espesor real.
  **Sin probar todavía.** Al usuario le pareció feo.
- `plantillas/auto-deportivo/`: **v3, la actual.** Superauto en cuña estilo
  deportivo italiano (sin marcas), escala 1:24 (20 x 8,4 x 4,7 cm). Carrocería de
  28 capas de 3 mm apiladas, con guardabarros, toma de aire, vidrio grabado, tapa
  que se levanta (pilas y motor adentro) y ruedas de 5 rayos con o-ring. 70 piezas
  en 2 hojas de 60 x 40 cm (SVG + DXF), unos 23 m de corte. Se regenera con
  `generar.py` (necesita shapely y ezdxf). **Sin probar.** Pesa unos 300 g en MDF.
  El usuario pidió: lindo, llamativo, deportivo y de buena calidad.
- No se encontró una plantilla gratis con auto, motor, goma y botón. Lo más
  parecido: [Thunder Laser, auto STEAM con motores TT](https://www.thunderlaser.com/laser-wiki-info63.html)
  (con control remoto), [Cart Bot de Instructables](https://instructables.com/Laser-Cut-Cart-Pushing-Robot)
  (motor TT, archivo SVG), [3axis.co, autos de juguete gratis](https://3axis.co/laser-cut/toy-cars/)
  (sin motor) y la [guía SFI de motor con polea y goma](https://www.sfi.ie/site-files/primary-science/media/pdfs/col/motor_vehicles.pdf).

## Proveedores de electrónica (búsqueda del 23/10/2026)
Precios sacados de los resúmenes de búsqueda, sin abrir cada aviso: **confirmar
antes de comprar**. [V] = visto, [E] = estimado. ML = Mercado Libre.

| Componente | Dónde | Precio |
|---|---|---|
| Motor 130 3-6 V | [ML pack x10](https://www.mercadolibre.com.ar/a-10-piezas-130-micro-motor-motores-de-juguete-dc-motor/p/MLA2059622817), [AliExpress x10](https://de.aliexpress.com/item/1005003468620982.html) | ML ~$1.855 c/u en pack [V]; Ali ~USD 2 los 10 [V] |
| Motorreductor TT (alternativa, no entra en la v3) | [ML](https://articulo.mercadolibre.com.ar/MLA-737788100-motor-tt-l-eje-metalico-motoreductor-3-6v-robotica-itytarg-_JM) | x10 $25.700 [V] |
| Portapilas 2xAA con cables | [ML x10](https://articulo.mercadolibre.com.ar/MLA-1108393166-10-unidades-portapilas-2-pila-aa-porta-pilas-2x-aa-con-cable-_JM); con tapa a tornillo solo en [AliExpress](https://www.aliexpress.us/item/3256804464956524.html) | ML ~$925 a $1.100 c/u [V] |
| Pulsador 12 mm con traba | [ML](https://listado.mercadolibre.com.ar/pulsadores-con-retencion), [AliExpress x10](https://de.aliexpress.com/item/32801816101.html) | ML x10 $10.274 [V] |
| Bornes sin soldar | [Wago 221 x10 ML](https://articulo.mercadolibre.com.ar/MLA-769183930-conector-empalme-reutilizable-2-vias-221-412-wago-x10u-symnet-_JM), [genéricos AliExpress](https://www.aliexpress.us/item/3256812261198594.html) | Wago ~$1.700 c/u [V]; genéricos centavos de dólar [V] |
| O-ring 31x3 (pedir 37 mm ext. x 3) | [AliExpress x50](https://www.aliexpress.us/item/3256805919968959.html); plan B [kit surtido ML](https://articulo.mercadolibre.com.ar/MLA-860373253-juego-orings-de-goma-419-piezas-sistema-metrico-kit-_JM) | Ali ~USD 1 los 50 [V] |
| Gomitas de silicona | [ML](https://listado.mercadolibre.com.ar/gomitas-para-pelo-silicona) | x1000 $5.190 [V] |
| Palitos de brochette 3 mm | [ML](https://listado.mercadolibre.com.ar/palitos-de-madera-para-brochette) | x90 $2.100 [V] |
| LED 5 mm (opcional) | [ML](https://listado.mercadolibre.com.ar/led-5mm-blanco) | x100 ~$7.000 [V] |

- **Electrónica por kit [E]:** unos $4.500 a $6.000 comprando packs (ML y
  AliExpress); unos $12.000 a $15.000 comprando todo suelto en ML.
- **Plazos:** ML llega en días. AliExpress tarda de 3 a 45 días más aduana: pedir
  ya lo liviano (o-rings, bornes, portapilas con tornillo) y tener plan B en ML.
- **En Tucumán (sin precios online):** Electrónica Santa Fe (Santa Fe 2020, tel.
  381 524-7386) y Computer-C.
- **Corte láser en Tucumán (de directorios, sin verificar):** Noagraf (Pasaje
  Padilla 29), Jackito's Corte y Grabado Láser, Laser Guimi (Sáenz Peña 775),
  Tucumán Artística MDF. No hay precios publicados: pedir presupuesto con el archivo.
- **Madera:** placa de MDF 3 mm de 1,83 x 2,60 m, de $12.170 a $26.731 [V].
  Terciado guatambú 3 mm de 2,20 x 1,60 m en [DAC](https://www.dacmaderas.com.ar/shop/multilaminado-fenlico/terciado-guatamb-3mm-220x160),
  $27.098 [V]. Para la v3 (0,48 m² de hoja por auto) salen unos 9 autos por placa
  de MDF, o sea **$1.400 a $3.000 de madera por auto [E]**.

## Plantillas encontradas (sin electrónica, hay que agregar el circuito)
| Fuente | Qué hay | Licencia / ojo |
|---|---|---|
| [Freepatternsarea](https://www.freepatternsarea.com/designs/downloads/free-wooden-rocking-horse-laser-cut-template-diy-download) | Caballito, cunita (DXF, SVG, CDR, PDF) | CC BY-NC-SA: **no comercial** |
| [Atomm](https://www.atomm.com/th/project/53845-aser-cut-wooden-race-car-toy-free-vector) | Autos, aviones, puzzles | Revisar cada archivo |
| [xTool Projects](https://projects.xtool.com/project/37855-cupids-treehouse-kit) | Casita en MDF 3 mm (SVG, XCS) | Revisar términos |

Proyectos con electrónica (para adultos, sirven de idea): [Arduino Toy](https://www.instructables.com/Arduino-Toy),
[Companion Cube](https://www.instructables.com/Companion-Cube).

## Competencia en Argentina (octubre 2026)
Precios de búsqueda; hay que confirmarlos en cada publicación.

| Competidor | Qué vende | Precio aprox. |
|---|---|---|
| Juguetes de madera en Mercado Libre ([ej.](https://listado.mercadolibre.com.ar/kit-robot-mdf)) | Robots de fibrofácil y encastres, **sin electrónica** | $11.000 a $16.000 |
| Kits STEM genéricos en Mercado Libre ([ej.](https://listado.mercadolibre.com.ar/kit-robotica-educativa-ni%C3%B1os)) | Robótica STEM 5 en 1, kits Steam (en su mayoría importados) | $99.000 a $119.000 |
| [Kit electrónica para niños en ML](https://listado.mercadolibre.com.ar/kit-electronica-para-ninos) | Alarmas y circuitos para armar | Variable |
| [MonoListo](https://www.monolisto.com.ar/) | Fábrica argentina de juguetes STEM, módulos de electrónica, vende mayorista | Consultar |
| [Snap Circuits (vía desertcart)](https://desertcart.com.ar/products/277147877-snap-circuits-green-energy-electronics-exploration-kit-over-125-exciting-stem-projects-full-color-project-manual-45-snap-circuits-parts-stem-educational-toys-for-kids-8) | Circuitos a presión sin soldar, importado | ~$52.800 |
| [Makeblock mBot (Frávega)](https://www.fravega.com/p/kit-de-robotica-makeblock-mbot-con-scratch-y-arduino-de-8-a-12-anos-22698028/) | Robot programable 8 a 12 años | ~$278.000 |
| Tiendas maker ([TodoMicro](https://www.todomicro.com.ar/194-kits-de-robotica), [La Tienda Bot](https://www.latiendabot.ar/kits-de-robotica-educativa/)) | Kits Arduino, más técnicos | $100.000+ |

**Hueco de mercado (estimación propia):** casi no hay kits de **madera con
electrónica simple, hechos en Argentina**, entre los juguetes de madera baratos
(~$15.000) y los kits STEM importados (~$100.000). Un kit local en el rango de
$25.000 a $45.000 tendría lugar.

## Normas para vender juguetes en Argentina
- La seguridad de juguetes es **certificación obligatoria** para fabricantes e
  importadores ([INTI](https://www.inti.gob.ar/areas/servicios-regulados/certificaciones/organismo-de-certificacion/tramites/juguetes),
  [Argentina.gob.ar](https://www.argentina.gob.ar/servicio/certificar-la-seguridad-de-juguetes)).
- La [Resolución 313/2025](https://www.argentina.gob.ar/normativa/nacional/resoluci%C3%B3n-313-2025-416329/texto)
  actualizó el régimen. Acepta certificados de laboratorios acreditados, nacionales
  o extranjeros, con normas ISO, EN, ASTM, IRAM o NM (base técnica: IRAM-NM 300).
- Hace falta una declaración jurada de conformidad, el certificado y la marca de
  conformidad antes de comercializar.
- **Pendiente:** averiguar el costo y el plazo de certificar con INTI, y si un
  "kit educativo / maqueta para mayores de 14" o un "taller de armado" cambia la
  obligación. Consultar con INTI o con un contador o gestor antes de vender en
  serio.

## Evaluación: ¿conviene?
**Sí, como prueba chica para esta Navidad. Todavía no como negocio formal.**

A favor:
- Hay un hueco de precio y casi no hay oferta local de madera más electrónica.
- La electrónica simple (LED, motor, pila, interruptor) es barata y no necesita soldar.
- El corte láser se puede tercerizar con conocidos, sin comprar máquina.
- Navidad es la mejor temporada para juguetes y regalos educativos.

En contra / riesgos:
- **Certificación:** vender juguetes en serio (Mercado Libre, jugueterías) exige
  certificar, y eso cuesta tiempo y plata.
- **Tiempo:** quedan unas 9 semanas a Navidad. Alcanza para 1 o 2 diseños simples,
  no para una línea completa.
- **Competencia china** muy barata en kits STEM genéricos. Hay que diferenciarse
  con lo local, lo artesanal, el armado y la madera.
- Hay que hacer instructivos claros, que los chicos puedan seguir solos.

Camino recomendado:
1. Un solo diseño simple, por ejemplo una **casita o farol con luz LED** o un **auto
   con motorcito**, para 6 a 10 años.
2. Hacer un prototipo y calcular el costo real.
3. Hacer una tanda chica (10 a 30 kits) para conocidos, ferias navideñas o como
   **taller de armado**. Ver la reacción.
4. Si funciona, después de Navidad averiguar la certificación y escalar.

## Notas para Claude
- Responder en español, simple y directo. El usuario no es técnico.
- Guardar acá los proveedores, precios y decisiones que se vayan encontrando.
- Citar fuentes con link y aclarar cuando un precio es estimado.
