// Funciones chicas que usan todas las páginas.
// Regla de seguridad: nunca se usa innerHTML. Todo texto entra con textContent.

import { NEGOCIO } from './config.js';

export const $ = (sel, raiz = document) => raiz.querySelector(sel);
export const $$ = (sel, raiz = document) => [...raiz.querySelectorAll(sel)];

const PESOS = new Intl.NumberFormat('es-AR', {
  style: 'currency', currency: 'ARS', maximumFractionDigits: 0,
});
export const formatoPrecio = (n) => PESOS.format(n);

export const sinMovimiento = () =>
  window.matchMedia('(prefers-reduced-motion: reduce)').matches;

// Limpia lo que escribe la gente: saca caracteres invisibles o de control
// (que se usan para engañar con textos dados vuelta), junta espacios y corta el largo.
const INVISIBLES = /[\u0000-\u001F\u007F-\u009F\u200B-\u200F\u2028-\u202E\u2060-\u206F\uFEFF]/g;
export function limpiarTexto(valor, largoMax) {
  return String(valor ?? '')
    .normalize('NFC')
    .replace(INVISIBLES, ' ')
    .replace(/\s+/g, ' ')
    .trim()
    .slice(0, largoMax);
}

// Arma el enlace a WhatsApp. El número sale de config.js y se revisa
// que sean solo dígitos: así nadie puede meter otra dirección en el enlace.
export function enlaceWhatsApp(mensaje) {
  const numero = String(NEGOCIO.whatsapp);
  if (!/^\d{10,15}$/.test(numero)) throw new Error('Número de WhatsApp inválido en config.js');
  return `https://wa.me/${numero}?text=${encodeURIComponent(mensaje)}`;
}

// Abre un enlace externo en otra pestaña sin darle acceso a esta página.
export function abrirAfuera(url) {
  const a = document.createElement('a');
  a.href = url;
  a.target = '_blank';
  a.rel = 'noopener noreferrer';
  a.click();
}

// localStorage puede fallar (modo privado, bloqueado): nunca rompe la página.
export function leerGuardado(clave) {
  try {
    return JSON.parse(localStorage.getItem(clave) ?? 'null');
  } catch {
    return null;
  }
}
export function guardar(clave, valor) {
  try {
    localStorage.setItem(clave, JSON.stringify(valor));
  } catch {
    /* sin almacenamiento: el carrito vive solo mientras la página está abierta */
  }
}

// Avisito que aparece abajo de la pantalla.
let temporizador;
export function avisar(texto) {
  const caja = $('#aviso');
  if (!caja) return;
  caja.textContent = texto;
  caja.classList.add('visible');
  clearTimeout(temporizador);
  temporizador = setTimeout(() => caja.classList.remove('visible'), 2600);
}

// Número de pedido corto para que la persona lo pueda dictar o copiar.
export function numeroDePedido() {
  const bytes = crypto.getRandomValues(new Uint8Array(3));
  const fecha = new Date();
  const dd = String(fecha.getDate()).padStart(2, '0');
  const mm = String(fecha.getMonth() + 1).padStart(2, '0');
  return `${dd}${mm}-${[...bytes].map((b) => b.toString(16).padStart(2, '0')).join('').toUpperCase()}`;
}

// Año del pie de página y menú del celular: iguales en todas las páginas.
export function iniciarComunes() {
  $$('[data-anio]').forEach((el) => { el.textContent = String(new Date().getFullYear()); });

  const boton = $('#boton-menu');
  const menu = $('#menu');
  if (boton && menu) {
    const cerrar = () => {
      boton.setAttribute('aria-expanded', 'false');
      menu.classList.remove('abierto');
    };
    boton.addEventListener('click', () => {
      const abierto = boton.getAttribute('aria-expanded') === 'true';
      boton.setAttribute('aria-expanded', String(!abierto));
      menu.classList.toggle('abierto', !abierto);
    });
    $$('a', menu).forEach((a) => a.addEventListener('click', cerrar));
    document.addEventListener('keydown', (e) => { if (e.key === 'Escape') cerrar(); });
  }
}
