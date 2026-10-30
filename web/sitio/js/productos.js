// =====================================================================
//  CATÁLOGO. Para cambiar un precio, cambiar el número de "precio"
//  (en pesos, sin puntos). Los precios de abajo son ESTIMADOS: confirmar
//  cuando se sepa el costo real del prototipo.
// =====================================================================

export const CATEGORIAS = Object.freeze({
  chicos: 'Para chicos (6 a 10 años)',
  coleccion: 'Coleccionables (+12 y adultos)',
});

export const PRODUCTOS = Object.freeze([
  {
    id: 'camioneta',
    nombre: 'Camioneta clásica',
    categoria: 'chicos',
    precio: 28000,
    etiqueta: 'Ideal para regalar',
    resumen: 'Una camioneta de las de antes que se arma toda a presión, sin cola. Con la caja abierta se ven las pilas, el botón y los cables.',
    imagen: 'img/camioneta',
    alto: 600, ancho: 1100,
    datos: [
      ['Piezas', '30'],
      ['Armado', 'A presión, sin cola ni herramientas'],
      ['Tiempo de armado', '1 a 2 horas'],
      ['Edad', '6 a 10 años (los más chicos, con un adulto)'],
      ['Largo', 'Unos 22 cm'],
    ],
    trae: [
      'Piezas de madera (MDF 3 mm) cortadas con láser y lijadas',
      'Motorcito, goma y polea',
      'Portapilas 2 x AA con tapa de tornillo',
      'Botón, bornes y cables listos para conectar',
      'Ruedas con cubierta de goma',
      'Instructivo impreso con dibujos, paso a paso',
    ],
  },
  {
    id: 'formula',
    nombre: 'Fórmula',
    categoria: 'coleccion',
    precio: 32000,
    etiqueta: 'El más fácil de la colección',
    resumen: 'Un auto de carrera con las ruedas a la vista. Se ve cómo la goma lleva la fuerza del motor al eje trasero.',
    imagen: 'img/formula',
    alto: 568, ancho: 1100,
    datos: [
      ['Piezas', '64'],
      ['Armado', 'Chasis encastrado y carrocería en capas pegadas'],
      ['Escala', '1:24 (20 cm de largo)'],
      ['Edad', 'Desde 12 años o para armar en familia'],
    ],
    trae: [
      'Chasis con el circuito grabado en la madera',
      'Carrocería en capas de MDF 3 mm y pernos de madera',
      'Motorcito, goma, polea y botón',
      'Portapilas 2 x AA con tapa de tornillo',
      'Ruedas de 5 rayos con cubierta de goma',
      'Instructivo impreso de 12 pasos',
    ],
  },
  {
    id: 'superauto',
    nombre: 'Superauto',
    categoria: 'coleccion',
    precio: 38000,
    etiqueta: 'El más pedido',
    resumen: 'Un deportivo en cuña, bien bajito, hecho con 28 capas de madera. Se levanta la carrocería y aparecen el motor y las pilas.',
    imagen: 'img/superauto',
    alto: 568, ancho: 1100,
    datos: [
      ['Piezas', '70'],
      ['Armado', 'Chasis encastrado y carrocería en capas pegadas'],
      ['Escala', '1:24 (20 cm de largo)'],
      ['Edad', 'Desde 12 años o para armar en familia'],
    ],
    trae: [
      'Chasis con el circuito grabado en la madera',
      'Carrocería en 28 capas de MDF 3 mm y pernos de madera',
      'Motorcito, goma, polea y botón',
      'Portapilas 2 x AA con tapa de tornillo',
      'Ruedas de 5 rayos con cubierta de goma',
      'Instructivo impreso de 12 pasos',
    ],
  },
  {
    id: 'clasico',
    nombre: 'Clásico',
    categoria: 'coleccion',
    precio: 42000,
    etiqueta: 'Para los nostálgicos',
    resumen: 'Una coupé fastback como las que andaban por las rutas argentinas en los 70. El más grande y pesado de la colección.',
    imagen: 'img/clasico',
    alto: 568, ancho: 1100,
    datos: [
      ['Piezas', '70'],
      ['Armado', 'Chasis encastrado y carrocería en capas pegadas'],
      ['Escala', '1:24 (20 cm de largo)'],
      ['Edad', 'Desde 12 años o para armar en familia'],
    ],
    trae: [
      'Chasis con el circuito grabado en la madera',
      'Carrocería en capas de MDF 3 mm y pernos de madera',
      'Motorcito, goma, polea y botón',
      'Portapilas 2 x AA con tapa de tornillo',
      'Ruedas de 5 rayos con cubierta de goma',
      'Instructivo impreso de 12 pasos',
    ],
  },
].map((p) => Object.freeze({ ...p, datos: Object.freeze(p.datos), trae: Object.freeze(p.trae) })));

export const PRODUCTOS_POR_ID = new Map(PRODUCTOS.map((p) => [p.id, p]));
