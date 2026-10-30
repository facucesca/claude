# Página de venta: Chispa

La página para vender los autitos. Es una **página estática**: son archivos sueltos (HTML, CSS,
JavaScript e imágenes), sin servidor, sin base de datos y sin cuentas de usuario. Esto la hace
**gratis de publicar** y **muy difícil de hackear**: no hay nada adentro que robar.

## Cómo funciona la venta
1. La persona mira los autos, los agrega al carrito y completa nombre, localidad y forma de entrega.
2. Al tocar «Enviar pedido por WhatsApp», se abre WhatsApp con el pedido ya escrito y un número de pedido.
3. Vos respondés con el total y un **link de pago de Mercado Pago** (o los datos para transferir).

Los datos de tarjeta **nunca pasan por esta página**: los maneja Mercado Pago.

## Qué hay en la página
- **Portada** con la camioneta llegando sobre una ruta y cuenta regresiva a Navidad.
- **Catálogo** con filtros (Para chicos / Coleccionables), tarjetas que se inclinan con el mouse
  y una ventana con el detalle de cada auto.
- **Circuito interactivo**: se aprieta el botón rojo y se ve la corriente andar y la rueda girar.
- Seguridad para chicos, preguntas frecuentes, formulario de pedido y carrito lateral.
- `arrepentimiento.html` (**botón de arrepentimiento**, obligatorio para vender por internet en
  Argentina), `privacidad.html` y `404.html`.
- Se adapta al celular y respeta a quien tiene «reducir movimiento» activado.

## Antes de publicar (obligatorio)
1. **Número de WhatsApp**: en `sitio/js/config.js`, cambiar `whatsapp: '5493810000000'` por el real
   (549 + característica sin 0 + número sin 15). Mientras siga en ceros, los pedidos no llegan.
2. **Precios**: en `sitio/js/productos.js`. Los que están ahora son **estimados** ($28.000 a $42.000).
3. **Nombre**: «Chispa» es provisorio. Si se cambia, buscarlo y reemplazarlo en los `.html` y en `js/config.js`.
4. **Dominio**: reemplazar `tu-dominio.com.ar` en `index.html` (imagen para compartir) y en
   `.well-known/security.txt` (mail para avisos de seguridad).
5. **Certificación de juguetes**: ver `CLAUDE.md`. Vender juguetes en serio exige certificar.
6. **Datos fiscales**: si se vende como negocio, ARCA (ex AFIP) pide poner el QR de «Data Fiscal»
   en el pie de la página.

## Probarla en la compu
Abrir el `index.html` con doble clic **no funciona** (los navegadores no dejan cargar el
JavaScript así). Desde la carpeta `sitio`:
```
python3 -m http.server 8000
```
y abrir http://localhost:8000

## Publicarla gratis (recomendado: Cloudflare Pages)
1. Crear una cuenta en https://pages.cloudflare.com (gratis).
2. «Create a project» → «Direct upload» → arrastrar la carpeta **`sitio`** (solo esa; este LEEME queda afuera a propósito).
3. Queda en una dirección tipo `chispa.pages.dev`, con HTTPS (candadito) y protección contra ataques.
4. Opcional: comprar un dominio `.com.ar` en https://nic.ar (unos pocos miles de pesos por año) y conectarlo.

También sirve **Netlify** (igual de fácil). Los dos leen el archivo `_headers`, que activa las
protecciones de seguridad. GitHub Pages también sirve, pero ignora `_headers` (quedan las
protecciones que van dentro de cada `.html`).

## Ciberseguridad: qué se hizo
| Riesgo | Cómo se cubre |
|---|---|
| Robo de datos de clientes o tarjetas | No hay base de datos ni pagos en la página. El pedido viaja por WhatsApp y el pago por Mercado Pago. |
| Inyección de código (XSS) | Política de contenido (CSP) estricta: solo corre JavaScript de este mismo sitio, nada escrito dentro del HTML. Además «Trusted Types»: el navegador bloquea cualquier intento de meter HTML con código. El JavaScript nunca usa `innerHTML`; todo texto entra con `textContent` y moldes `<template>`. |
| Librerías de terceros comprometidas | No se usa ninguna. Tipografías (Fraunces y Nunito, licencia OFL) e íconos están adentro de la página. No hay Google Fonts, ni CDN, ni analytics. |
| Datos manipulados en el carrito | El carrito guardado en el navegador se revisa al cargar: solo autos que existen y cantidades de 1 a 10. Los precios siempre salen del código, nunca de lo guardado. |
| Textos tramposos en el formulario | Se limpian caracteres invisibles o que dan vuelta el texto, se limita el largo y todo va codificado en el enlace de WhatsApp. El número de WhatsApp se valida (solo dígitos). |
| Meter la página adentro de otra (clickjacking) | `frame-ancestors 'none'` y `X-Frame-Options: DENY`. |
| Conexión espiada | HTTPS obligatorio (HSTS) y `upgrade-insecure-requests`. |
| Enlaces externos | Se abren con `noopener noreferrer`: la otra página no puede controlar esta. |
| Permisos del navegador | Cámara, micrófono, ubicación, pagos, etc. bloqueados (`Permissions-Policy`). |
| Avisos de seguridad | `/.well-known/security.txt` dice a quién avisar si alguien encuentra un problema. |
| Privacidad | Sin cookies, sin seguimiento. Por eso no hace falta el cartel de cookies. |

Para revisar la seguridad una vez publicada: https://securityheaders.com y
https://observatory.mozilla.org (pegar la dirección de la página; debería dar A o A+).

**Para mantenerla segura:** si alguna vez se agrega algo de otro sitio (un chat, Google Analytics,
un botón de Mercado Pago integrado), hay que sumarlo a mano en la CSP de `_headers` y de cada `.html`.
Si no, el navegador lo bloquea (a propósito). La cuenta de Cloudflare/Netlify y la de WhatsApp
Business son la puerta de entrada real: ponerles **verificación en dos pasos**.

## Carpetas
```
web/
├── LEEME.md            esta guía (no se publica)
└── sitio/              ← ESTO es lo que se sube
    ├── index.html            página principal
    ├── arrepentimiento.html  botón de arrepentimiento
    ├── privacidad.html       política de privacidad
    ├── 404.html              página de error
    ├── _headers              cabeceras de seguridad (Cloudflare / Netlify)
    ├── robots.txt
    ├── .well-known/security.txt
    ├── css/estilos.css       colores, letras y animaciones
    ├── js/config.js          ← WhatsApp, fechas, formas de entrega
    ├── js/productos.js       ← autos y precios
    ├── js/app.js             catálogo, carrito, circuito, pedido
    ├── js/carrito.js         carrito guardado en el navegador
    ├── js/util.js            funciones comunes (limpieza de textos, WhatsApp)
    ├── fuentes/              tipografías (licencia OFL)
    └── img/                  fotos de los autos (WebP) e ícono
```

## Próximos pasos posibles
- Cambiar los dibujos por **fotos reales** del prototipo armado (y un video corto del auto andando).
- Si hay muchos pedidos: pasar a **Tiendanube** (tienda argentina con Mercado Pago integrado) o
  agregar **links de pago fijos** de Mercado Pago por auto.
