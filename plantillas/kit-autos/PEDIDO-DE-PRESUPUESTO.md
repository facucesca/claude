# Pedido de presupuesto: corte láser del kit de autos

Archivo generado por `generar.py`. Si cambia el diseño o el espesor, se vuelve a generar.

## Qué mandar al taller
- Los archivos de la carpeta de cada modelo: `hoja-N.svg` o `hoja-N.dxf` (el mismo dibujo, en los
  dos formatos; mandar el que pida el taller).
- **Material:** MDF / fibrofácil **crudo de 3 mm**. Versión premium: terciado de 3 mm
  "para láser" (abedul o álamo; el fenólico no sirve).
- **Colores / capas del archivo:**
  - **Rojo / CORTAR:** corte pasante.
  - **Azul / GRABAR:** grabado de línea y textos (números de las piezas, puertas, dibujos del piso).
  - **Azul relleno / GRABAR_RELLENO:** grabado lleno, no muy profundo (vidrios y discos de las ruedas).
  - **Gris / NOTAS:** son notas, **no se cortan ni se graban**.
- **Medidas:** las ranuras y pestañas están hechas para material de 3 mm justos. Pedirle al
  taller que **mida el espesor real de la placa**: si no es 3 mm, se regenera el archivo con la
  medida correcta (`python3 generar.py 2.8`, por ejemplo). No hace falta compensar el ancho del corte.
- **Primero 1 auto de prueba** de cada modelo, para revisar los encastres antes de cortar la tanda.

## Datos por modelo (1 auto)

| Modelo | Material | Piezas | Corte | Grabado | Tiempo estimado* | Archivos |
|---|---|---|---|---|---|---|
| **Superauto** | 1 hoja de 60 x 40 cm | 70 | 20.1 m | 22 cm² + 0.4 m de línea | 20 a 30 min | `superauto/hoja-1.svg` |
| **Clásico** | 2 hojas: 60 x 40 cm + 60 x 14 cm | 70 | 20.6 m | 26 cm² + 0.6 m de línea | 20 a 30 min | `clasico/hoja-1.svg`, `clasico/hoja-2.svg` |
| **Fórmula** | 1 hoja de 60 x 20 cm | 64 | 11.3 m | 17 cm² + 0.3 m de línea | 11 a 17 min | `formula/hoja-1.svg` |

\* Estimación propia para un láser CO2 de 60 a 80 W. Cada taller tiene su velocidad: pedirles el
precio por minuto o por hoja.

## Mensaje para mandar por WhatsApp
> Hola, quiero cotizar corte y grabado láser en MDF crudo de 3 mm (yo puedo llevar la placa o
> la ponen ustedes). Son kits de autitos de madera. Te mando los archivos (SVG y DXF):
> - Fórmula: 1 hoja de 60 x 20 cm, unos 11 m de corte.
> - Superauto: 1 hoja de 60 x 40 cm, unos 20 m de corte.
> - Clásico: 2 hojas: 60 x 40 cm + 60 x 14 cm, unos 21 m de corte.
>
> Rojo es corte, azul es grabado (el azul relleno es grabado lleno) y lo gris no se hace.
> Quiero primero 1 de cada uno de prueba, y después cotizar 10, 20 y 50 de cada modelo.
> ¿Cuánto me sale cada uno y en cuánto tiempo lo tienen? ¿Pueden medir el espesor real de la placa?
