// Página del botón de arrepentimiento: arma el mensaje y lo manda por WhatsApp.

import { NEGOCIO } from './config.js';
import { $, limpiarTexto, enlaceWhatsApp, abrirAfuera, avisar, iniciarComunes } from './util.js';

iniciarComunes();

const nombre = $('#a-nombre');
const pedido = $('#a-pedido');
const fecha = $('#a-fecha');

// No se puede elegir una fecha futura.
fecha.max = new Date().toISOString().slice(0, 10);

function mostrarError(input, error, hayError) {
  error.hidden = !hayError;
  input.toggleAttribute('aria-invalid', hayError);
}

$('#form-arrepentimiento').addEventListener('submit', (e) => {
  e.preventDefault();
  const nombreLimpio = limpiarTexto(nombre.value, 80);
  // El número de pedido solo puede tener letras, números y guiones.
  const pedidoLimpio = limpiarTexto(pedido.value, 20).replace(/[^0-9A-Za-z-]/g, '');
  const fechaValida = /^\d{4}-\d{2}-\d{2}$/.test(fecha.value) && fecha.value <= fecha.max;

  mostrarError(nombre, $('#ea-nombre'), nombreLimpio.length < 2);
  mostrarError(fecha, $('#ea-fecha'), !fechaValida);
  if (nombreLimpio.length < 2) return nombre.focus();
  if (!fechaValida) return fecha.focus();

  const [anio, mes, dia] = fecha.value.split('-');
  const texto = [
    `Hola ${NEGOCIO.nombre}, quiero ejercer mi derecho de arrepentimiento (botón de arrepentimiento).`,
    `Nombre: ${nombreLimpio}`,
    `Pedido: ${pedidoLimpio || 'no lo tengo'}`,
    `Lo recibí el: ${dia}/${mes}/${anio}`,
    'Por favor, envíenme el código de trámite.',
  ].join('\n');

  abrirAfuera(enlaceWhatsApp(texto));
  avisar('Abrimos WhatsApp con tu pedido. ¡Solo falta tocar Enviar!');
});
