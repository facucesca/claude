// =====================================================================
//  DATOS DEL NEGOCIO: lo único que hay que cambiar para salir a vender.
//  (Los precios y los autos están en productos.js)
// =====================================================================

export const NEGOCIO = Object.freeze({
  nombre: 'Chispa',
  lema: 'Juguetes de madera que se mueven',
  ciudad: 'San Miguel de Tucumán',

  // Número de WhatsApp con código de país, sin +, sin espacios ni guiones.
  // Ejemplo para Tucumán: 549 381 1234567  ->  '5493811234567'
  // MIENTRAS SIGA EN CEROS, LOS PEDIDOS NO LE LLEGAN A NADIE.
  whatsapp: '5493810000000',

  // Hasta qué día se toman pedidos para entregar antes de Navidad.
  ultimoDiaPedidos: '2026-12-15',
  navidad: '2026-12-25T00:00:00-03:00',

  // Formas de entrega que se ofrecen en el formulario.
  entregas: Object.freeze([
    'Retiro en San Miguel de Tucumán',
    'Envío dentro de Tucumán (a coordinar)',
    'Envío a otra provincia (Correo Argentino / Andreani, a cargo del comprador)',
  ]),

  // Cantidad máxima por auto en un mismo pedido.
  maxPorProducto: 10,
});

export const NUMERO_SIN_CONFIGURAR = /^5493810+$/.test(NEGOCIO.whatsapp);
