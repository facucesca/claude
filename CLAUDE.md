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
3. [ ] Proveedores de electrónica (local, Mercado Libre, AliExpress / Temu).
4. [ ] Diseñar 1 prototipo y calcular el costo real por kit.
5. [ ] Decidir: venta chica de prueba, taller o regalo.

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
