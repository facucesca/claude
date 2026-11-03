// Página principal: catálogo, carrito, circuito interactivo y pedido por WhatsApp.

import { NEGOCIO, NUMERO_SIN_CONFIGURAR } from './config.js';
import { PRODUCTOS, PRODUCTOS_POR_ID, CATEGORIAS } from './productos.js';
import * as carrito from './carrito.js';
import {
  $, $$, formatoPrecio, sinMovimiento, limpiarTexto, enlaceWhatsApp,
  abrirAfuera, avisar, numeroDePedido, iniciarComunes,
} from './util.js';

// ---------- Imágenes ----------
function ponerImagen(img, producto, sizes) {
  img.src = `${producto.imagen}.webp`;
  img.srcset = `${producto.imagen}-chica.webp 600w, ${producto.imagen}.webp ${producto.ancho}w`;
  img.sizes = sizes;
  img.width = producto.ancho;
  img.height = producto.alto;
}

// ---------- Catálogo ----------
const molde = $('#molde-auto');
const catalogo = $('#catalogo');

function tarjetaDeAuto(producto) {
  const nodo = molde.content.firstElementChild.cloneNode(true);
  nodo.dataset.categoria = producto.categoria;
  $('.auto__etiqueta', nodo).textContent = producto.etiqueta;
  ponerImagen($('.auto__imagen', nodo), producto, '(max-width: 640px) 92vw, 380px');
  $('.auto__categoria', nodo).textContent = CATEGORIAS[producto.categoria];
  $('.auto__nombre', nodo).textContent = producto.nombre;
  $('.auto__resumen', nodo).textContent = producto.resumen;
  $('.auto__precio', nodo).textContent = formatoPrecio(producto.precio);

  const tarjeta = $('.auto__tarjeta', nodo);
  tarjeta.setAttribute('aria-label', `Ver detalle de ${producto.nombre}, ${formatoPrecio(producto.precio)}`);
  tarjeta.addEventListener('click', () => abrirProducto(producto.id));
  inclinarAlPasar(tarjeta);

  const agregar = $('.auto__agregar', nodo);
  agregar.setAttribute('aria-label', `Agregar ${producto.nombre} al carrito`);
  agregar.addEventListener('click', () => agregarAlCarrito(producto.id, agregar));
  return nodo;
}

function mostrarCatalogo(filtro) {
  const cambiar = () => {
    catalogo.replaceChildren(
      ...PRODUCTOS
        .filter((p) => filtro === 'todos' || p.categoria === filtro)
        .map(tarjetaDeAuto),
    );
  };
  // View Transitions: las tarjetas se acomodan con animación si el navegador lo permite.
  if (document.startViewTransition && !sinMovimiento() && catalogo.children.length) {
    document.startViewTransition(cambiar);
  } else {
    cambiar();
  }
}

function iniciarFiltros() {
  const botones = $$('.filtro');
  botones.forEach((boton) => boton.addEventListener('click', () => {
    botones.forEach((b) => b.setAttribute('aria-pressed', String(b === boton)));
    mostrarCatalogo(boton.dataset.filtro);
  }));
}

// La tarjeta se inclina un poquito siguiendo el mouse.
function inclinarAlPasar(el) {
  if (sinMovimiento() || !window.matchMedia('(hover: hover)').matches) return;
  el.addEventListener('pointermove', (e) => {
    const r = el.getBoundingClientRect();
    const x = (e.clientX - r.left) / r.width - 0.5;
    const y = (e.clientY - r.top) / r.height - 0.5;
    el.style.setProperty('--giro-x', `${(-y * 6).toFixed(2)}deg`);
    el.style.setProperty('--giro-y', `${(x * 8).toFixed(2)}deg`);
  });
  el.addEventListener('pointerleave', () => {
    el.style.removeProperty('--giro-x');
    el.style.removeProperty('--giro-y');
  });
}

// ---------- Detalle de un auto ----------
const ventanaProducto = $('#ventana-producto');
let productoAbierto = null;

function abrirProducto(id) {
  const p = PRODUCTOS_POR_ID.get(id);
  if (!p) return;
  productoAbierto = p.id;
  ponerImagen($('#vp-imagen'), p, '(max-width: 720px) 100vw, 720px');
  $('#vp-etiqueta').textContent = p.etiqueta;
  $('#vp-nombre').textContent = p.nombre;
  $('#vp-resumen').textContent = p.resumen;
  $('#vp-precio').textContent = formatoPrecio(p.precio);
  $('#vp-datos').replaceChildren(...p.datos.flatMap(([dato, valor]) => {
    const dt = document.createElement('dt');
    const dd = document.createElement('dd');
    dt.textContent = dato;
    dd.textContent = valor;
    return [dt, dd];
  }));
  $('#vp-trae').replaceChildren(...p.trae.map((cosa) => {
    const li = document.createElement('li');
    li.textContent = cosa;
    return li;
  }));
  ventanaProducto.showModal();
}

$('#vp-agregar').addEventListener('click', (e) => {
  if (productoAbierto) agregarAlCarrito(productoAbierto, e.currentTarget);
  ventanaProducto.close();
});

// Todas las ventanas se cierran con la X o tocando afuera.
$$('dialog').forEach((d) => {
  $$('[data-cerrar]', d).forEach((b) => b.addEventListener('click', () => d.close()));
  d.addEventListener('click', (e) => { if (e.target === d) d.close(); });
});

// ---------- Carrito ----------
const ventanaCarrito = $('#ventana-carrito');
const moldeLinea = $('#molde-linea');

function agregarAlCarrito(id, origen) {
  if (!carrito.agregar(id)) return;
  const p = PRODUCTOS_POR_ID.get(id);
  avisar(`${p.nombre} se agregó al carrito`);
  const icono = $('#abrir-carrito');
  icono.classList.remove('salto');
  void icono.offsetWidth; // reinicia la animación
  icono.classList.add('salto');
  origen?.classList.add('agregado');
  setTimeout(() => origen?.classList.remove('agregado'), 900);
}

function lineaDeCarrito({ producto, cantidad, subtotal }) {
  const nodo = moldeLinea.content.firstElementChild.cloneNode(true);
  const img = $('.linea__imagen', nodo);
  img.src = `${producto.imagen}-chica.webp`;
  $('.linea__nombre', nodo).textContent = producto.nombre;
  $('.linea__precio', nodo).textContent =
    `${cantidad} × ${formatoPrecio(producto.precio)} = ${formatoPrecio(subtotal)}`;
  $('.cantidad__valor', nodo).textContent = String(cantidad);
  const menos = $('[data-accion="menos"]', nodo);
  const mas = $('[data-accion="mas"]', nodo);
  menos.setAttribute('aria-label', `Sacar un ${producto.nombre}`);
  mas.setAttribute('aria-label', `Sumar un ${producto.nombre}`);
  mas.disabled = cantidad >= NEGOCIO.maxPorProducto;
  menos.addEventListener('click', () => carrito.cambiar(producto.id, cantidad - 1));
  mas.addEventListener('click', () => carrito.cambiar(producto.id, cantidad + 1));
  return nodo;
}

function actualizarCarrito() {
  const lineas = carrito.lineas();
  const unidades = carrito.totalUnidades();
  const total = formatoPrecio(carrito.totalPesos());

  const burbuja = $('#burbuja-carrito');
  burbuja.hidden = unidades === 0;
  burbuja.textContent = String(unidades);
  $('#abrir-carrito').setAttribute('aria-label', `Ver el carrito (${unidades} ${unidades === 1 ? 'auto' : 'autos'})`);

  $('#carrito-lista').replaceChildren(...lineas.map(lineaDeCarrito));
  $('#carrito-vacio').hidden = lineas.length > 0;
  $('#carrito-total').textContent = total;
  $('.carrito__pie').hidden = lineas.length === 0;

  // Resumen dentro del formulario de pedido
  $('#resumen-vacio').hidden = lineas.length > 0;
  $('#resumen-lista').replaceChildren(...lineas.map(({ producto, cantidad, subtotal }) => {
    const li = document.createElement('li');
    const nombre = document.createElement('span');
    const precio = document.createElement('span');
    nombre.textContent = `${cantidad} × ${producto.nombre}`;
    precio.textContent = formatoPrecio(subtotal);
    li.append(nombre, precio);
    return li;
  }));
  const totalResumen = $('#resumen-total');
  totalResumen.hidden = lineas.length === 0;
  totalResumen.textContent = `Total: ${total}`;
}

$('#abrir-carrito').addEventListener('click', () => ventanaCarrito.showModal());
$('#ir-al-pedido').addEventListener('click', () => ventanaCarrito.close());
$('#vaciar-carrito').addEventListener('click', () => {
  carrito.vaciar();
  avisar('Carrito vacío');
});
document.addEventListener('carrito:cambio', actualizarCarrito);

// ---------- Formulario de pedido ----------
const form = $('#form-pedido');
const campos = {
  nombre: { input: $('#f-nombre'), error: $('#e-nombre'), max: 60 },
  localidad: { input: $('#f-localidad'), error: $('#e-localidad'), max: 60 },
};

function iniciarFormulario() {
  const entrega = $('#f-entrega');
  entrega.replaceChildren(...NEGOCIO.entregas.map((texto, i) => new Option(texto, String(i))));

  const mensaje = $('#f-mensaje');
  const contador = $('#contador-mensaje');
  mensaje.addEventListener('input', () => {
    contador.textContent = `${mensaje.value.length} / ${mensaje.maxLength}`;
  });

  Object.values(campos).forEach(({ input, error }) => {
    input.addEventListener('input', () => {
      if (input.checkValidity()) {
        error.hidden = true;
        input.removeAttribute('aria-invalid');
      }
    });
  });

  form.addEventListener('submit', (e) => {
    e.preventDefault();
    enviarPedido();
  });
}

function validar() {
  let primero = null;
  for (const { input, error, max } of Object.values(campos)) {
    const limpio = limpiarTexto(input.value, max);
    const bien = limpio.length >= 2;
    error.hidden = bien;
    input.toggleAttribute('aria-invalid', !bien);
    if (!bien && !primero) primero = input;
  }
  if (primero) primero.focus();
  return !primero;
}

function enviarPedido() {
  const lineas = carrito.lineas();
  if (lineas.length === 0) {
    avisar('Primero elegí al menos un auto');
    $('#autos').scrollIntoView({ behavior: sinMovimiento() ? 'auto' : 'smooth' });
    return;
  }
  if (!validar()) return;

  const indiceEntrega = Number($('#f-entrega').value);
  const entrega = NEGOCIO.entregas[indiceEntrega] ?? NEGOCIO.entregas[0];
  const nombre = limpiarTexto(campos.nombre.input.value, campos.nombre.max);
  const localidad = limpiarTexto(campos.localidad.input.value, campos.localidad.max);
  const nota = limpiarTexto($('#f-mensaje').value, 400);

  const texto = [
    `¡Hola ${NEGOCIO.nombre}! Quiero hacer un pedido (N.º ${numeroDePedido()}):`,
    '',
    ...lineas.map(({ producto, cantidad, subtotal }) =>
      `• ${cantidad} × ${producto.nombre}: ${formatoPrecio(subtotal)}`),
    '',
    `Total: ${formatoPrecio(carrito.totalPesos())}`,
    `Nombre: ${nombre}`,
    `Localidad: ${localidad}`,
    `Entrega: ${entrega}`,
    ...(nota ? [`Nota: ${nota}`] : []),
  ].join('\n');

  if (NUMERO_SIN_CONFIGURAR) {
    console.warn('Falta poner el número de WhatsApp en js/config.js');
  }
  abrirAfuera(enlaceWhatsApp(texto));
  avisar('Abrimos WhatsApp con tu pedido. ¡Solo falta tocar Enviar!');
}

// ---------- Circuito interactivo ----------
function iniciarCircuito() {
  const figura = $('#circuito');
  const boton = $('#probar-circuito');
  const botonSvg = $('#boton-svg');
  const estado = $('#estado-circuito');

  const alternar = () => {
    const encendido = !figura.classList.contains('encendido');
    figura.classList.toggle('encendido', encendido);
    boton.setAttribute('aria-pressed', String(encendido));
    boton.textContent = encendido ? 'Soltar el botón' : 'Apretar el botón';
    estado.textContent = encendido
      ? 'Circuito cerrado: la corriente da toda la vuelta y el motor gira.'
      : 'El circuito está abierto: el motor está quieto.';
  };
  boton.addEventListener('click', alternar);
  botonSvg.addEventListener('click', alternar);

  // Al pasar por cada parte de la lista, se marca en el dibujo.
  $$('#partes [data-parte]').forEach((item) => {
    const parte = $(`#circuito .parte[data-parte="${item.dataset.parte}"]`);
    const marcar = (si) => {
      parte.classList.toggle('marcada', si);
      item.classList.toggle('marcada', si);
    };
    item.addEventListener('pointerenter', () => marcar(true));
    item.addEventListener('pointerleave', () => marcar(false));
  });
}

// ---------- Cuenta regresiva a Navidad ----------
function iniciarCuentaRegresiva() {
  const navidad = new Date(NEGOCIO.navidad);
  const ultimo = new Date(`${NEGOCIO.ultimoDiaPedidos}T23:59:59-03:00`);
  const dias = Math.ceil((navidad - Date.now()) / 86400000);
  if (!(dias > 0)) return;

  const fechaUltimo = ultimo.toLocaleDateString('es-AR', { day: 'numeric', month: 'long', timeZone: 'America/Argentina/Tucuman' });
  $$('[data-ultimo-dia]').forEach((el) => { el.textContent = fechaUltimo; });

  const texto = Date.now() <= ultimo
    ? `Faltan ${dias} días para Navidad · pedidos hasta el ${fechaUltimo}`
    : `Faltan ${dias} días para Navidad · consultá por entregas`;
  $('#cuenta-texto').textContent = texto;
  $('#cuenta-regresiva').hidden = false;
}

// ---------- Aparecer al bajar ----------
function iniciarApariciones() {
  const elementos = $$('.aparecer');
  if (sinMovimiento() || !('IntersectionObserver' in window)) {
    elementos.forEach((el) => el.classList.add('visible'));
    return;
  }
  const observador = new IntersectionObserver((entradas) => {
    entradas.forEach((entrada) => {
      if (entrada.isIntersecting) {
        entrada.target.classList.add('visible');
        observador.unobserve(entrada.target);
      }
    });
  }, { rootMargin: '0px 0px -8% 0px' });
  elementos.forEach((el) => observador.observe(el));
}

// La cabecera se marca cuando se baja un poco.
function iniciarCabecera() {
  const cabecera = $('.cabecera');
  const marcar = () => cabecera.classList.toggle('con-sombra', window.scrollY > 8);
  window.addEventListener('scroll', marcar, { passive: true });
  marcar();
}

// ---------- Arranque ----------
document.documentElement.classList.add('js-listo');
iniciarComunes();
iniciarCabecera();
iniciarFiltros();
mostrarCatalogo('todos');
iniciarFormulario();
iniciarCircuito();
iniciarCuentaRegresiva();
actualizarCarrito();
iniciarApariciones();
