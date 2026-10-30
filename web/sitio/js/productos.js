// =====================================================================
//  CATÁLOGO. Para cambiar un precio, cambiar el número de "precio"
//  (en pesos, sin puntos). Los precios de abajo son ESTIMADOS: confirmar
//  cuando se sepa el costo real del prototipo.
// =====================================================================

export const CATEGORIAS = Object.freeze({
  auto: 'Kit para chicos (6 a 10 años)',
  pack: 'Pack de regalo',
});

// Lo que trae cada kit (es igual en los 3 autos: cambia solo la madera).
const TRAE_KIT = [
  'Piezas de madera (MDF 3 mm) cortadas con láser y lijadas',
  'Motorcito, goma y polea',
  'Portapilas 2 x AA',
  'Botón, bornes y cables listos para conectar (sin soldar)',
  'Ruedas con cubierta de goma',
  'Instructivo impreso con dibujos, paso a paso',
];

export const PRODUCTOS = Object.freeze([
  {
    id: 'camioneta',
    nombre: 'Camioneta clásica',
    categoria: 'auto',
    precio: 28000,
    etiqueta: 'La preferida',
    resumen: 'Una camioneta de las de antes que se arma toda a presión, sin cola. En la caja abierta se ven las pilas, el botón y los cables.',
    imagen: 'img/camioneta',
    alto: 600, ancho: 1100,
    datos: [
      ['Piezas', '30'],
      ['Armado', 'A presión, sin cola ni herramientas'],
      ['Tiempo de armado', '1 a 2 horas'],
      ['Edad', '6 a 10 años (los más chicos, con un adulto)'],
      ['Largo', 'Unos 22 cm'],
    ],
    trae: TRAE_KIT,
  },
  {
    id: 'jeep',
    nombre: 'Jeep todoterreno',
    categoria: 'auto',
    precio: 30000,
    etiqueta: 'Para aventureros',
    resumen: 'Un jeep abierto como los de campo: parrilla con ranuras, parabrisas, asiento y barra antivuelco. Las pilas y el botón van atrás, a la vista.',
    imagen: 'img/jeep',
    alto: 600, ancho: 1100,
    datos: [
      ['Piezas', '31'],
      ['Armado', 'A presión, sin cola ni herramientas'],
      ['Tiempo de armado', '1 a 2 horas'],
      ['Edad', '6 a 10 años (los más chicos, con un adulto)'],
      ['Largo', 'Unos 22 cm'],
    ],
    trae: TRAE_KIT,
  },
  {
    id: 'colectivo',
    nombre: 'Colectivo',
    categoria: 'auto',
    precio: 32000,
    etiqueta: 'Tiene timbre',
    resumen: 'Un bondi con ventanillas y asientos. El techo se saca para cambiar las pilas, y el botón para arrancar está arriba, como el timbre.',
    imagen: 'img/colectivo',
    alto: 600, ancho: 1100,
    datos: [
      ['Piezas', '30'],
      ['Armado', 'A presión, sin cola ni herramientas'],
      ['Tiempo de armado', '1 a 2 horas'],
      ['Edad', '6 a 10 años (los más chicos, con un adulto)'],
      ['Largo', 'Unos 22 cm, 9 cm de alto'],
    ],
    trae: TRAE_KIT,
  },
  {
    id: 'pack',
    nombre: 'La flota completa',
    categoria: 'pack',
    precio: 80000,
    etiqueta: 'Los 3 con descuento',
    resumen: 'La camioneta, el jeep y el colectivo juntos. Ideal para hermanos, primos o para armar en familia.',
    imagen: 'img/pack',
    alto: 600, ancho: 1100,
    datos: [
      ['Incluye', 'Camioneta, jeep y colectivo'],
      ['Piezas', '91 en total'],
      ['Armado', 'A presión, sin cola ni herramientas'],
      ['Edad', '6 a 10 años (los más chicos, con un adulto)'],
    ],
    trae: [
      'Los 3 kits completos, cada uno en su caja',
      '3 motorcitos, 3 portapilas y 3 botones',
      'Bornes y cables listos para conectar (sin soldar)',
      '3 instructivos impresos',
    ],
  },
].map((p) => Object.freeze({ ...p, datos: Object.freeze(p.datos), trae: Object.freeze(p.trae) })));

export const PRODUCTOS_POR_ID = new Map(PRODUCTOS.map((p) => [p.id, p]));
