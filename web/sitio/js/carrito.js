// El carrito se guarda solo en el navegador de la persona (localStorage).
// No viaja a ningún servidor. Al leerlo se revisa todo, porque cualquiera
// puede tocar lo guardado: solo se aceptan autos que existen y cantidades válidas.

import { NEGOCIO } from './config.js';
import { PRODUCTOS_POR_ID } from './productos.js';
import { leerGuardado, guardar } from './util.js';

const CLAVE = 'chispa-carrito-v1';
const items = new Map();

function cantidadValida(n) {
  return Number.isInteger(n) && n >= 1 && n <= NEGOCIO.maxPorProducto;
}

function cargar() {
  const guardado = leerGuardado(CLAVE);
  if (!guardado || typeof guardado !== 'object' || Array.isArray(guardado)) return;
  for (const [id, cantidad] of Object.entries(guardado)) {
    if (PRODUCTOS_POR_ID.has(id) && cantidadValida(cantidad)) items.set(id, cantidad);
  }
}

function avisarCambio() {
  guardar(CLAVE, Object.fromEntries(items));
  document.dispatchEvent(new CustomEvent('carrito:cambio'));
}

export function agregar(id, cantidad = 1) {
  if (!PRODUCTOS_POR_ID.has(id)) return false;
  const nueva = Math.min((items.get(id) ?? 0) + cantidad, NEGOCIO.maxPorProducto);
  items.set(id, nueva);
  avisarCambio();
  return true;
}

export function cambiar(id, cantidad) {
  if (!items.has(id)) return;
  if (cantidad <= 0) items.delete(id);
  else items.set(id, Math.min(cantidad, NEGOCIO.maxPorProducto));
  avisarCambio();
}

export function vaciar() {
  items.clear();
  avisarCambio();
}

export function lineas() {
  return [...items].map(([id, cantidad]) => {
    const producto = PRODUCTOS_POR_ID.get(id);
    return { producto, cantidad, subtotal: producto.precio * cantidad };
  });
}

export const totalUnidades = () => [...items.values()].reduce((a, b) => a + b, 0);
export const totalPesos = () => lineas().reduce((a, l) => a + l.subtotal, 0);

cargar();
