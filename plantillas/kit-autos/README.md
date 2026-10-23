# Kit de autos de madera con motor (v4)

Un **chasis común** con toda la electrónica resuelta y **3 carrocerías** que se apoyan encima.
Para cambiar las pilas o ver el motor, se levanta la carrocería.

| | Fórmula | Superauto | Clásico |
|---|---|---|---|
| Estilo | Auto de carrera, ruedas a la vista | Deportivo en cuña, estilo italiano | Coupé fastback de los 70 |
| Dificultad | La más fácil | Media | Media |
| Madera (MDF 3 mm) | **60 x 20 cm** | 60 x 40 cm | 60 x 40 + 60 x 14 cm |
| Piezas | 64 | 70 | 70 |
| Corte láser | ~11 m (~11-17 min) | ~20 m (~20-30 min) | ~21 m (~20-30 min) |
| Peso de la madera | ~110 g | ~250 g | ~330 g |

Todos: escala 1:24 (20 cm de largo), mismo chasis, misma electrónica y mismas ruedas.

## Carpetas
- `formula/`, `superauto/`, `clasico/`: cada una tiene
  - `hoja-N.svg` y `hoja-N.dxf`: **para mandar al láser** (chasis + carrocería + ruedas de 1 auto).
  - `hoja-N.png`: imagen de la hoja.
  - `vista-3d.png`: cómo queda el auto.
  - `instructivo.pdf`: **instrucciones para imprimir**, paso a paso con imágenes (y `instructivo.html`).
  - `pasos/`: las imágenes del instructivo.
- `PEDIDO-DE-PRESUPUESTO.md`: qué mandarle al taller de corte y un mensaje listo para WhatsApp.
- `kit.py`: el motor (chasis, carrocería en capas, acomodo en hojas, dibujos 3D).
- `modelos.py`: las 3 carrocerías. Para un modelo nuevo, se agrega una clase con su perfil.
- `generar.py`: arma todo.

## El chasis (igual para todos)
- Piso con todo **grabado**: dónde va el portapilas, el motor, los 3 bornes (B1, B2, B3) y por dónde
  pasan los cables.
- 2 largueros (con los agujeros de los ejes), 2 travesaños, soporte del motor y torre del botón.
- Motor 130 acostado en el piso; **goma** del eje del motor a una **polea** en el eje trasero (reduce
  la velocidad y da fuerza).
- Pulsador con traba en la torre, que asoma por un agujero arriba de la carrocería.
- Circuito sin soldar: pila (+) → B1 → botón → B2 → motor → B3 → pila (−).
- La altura de la torre se ajusta sola según el modelo (la tapa queda 1,5 mm debajo de la carrocería).

## Volver a generar
```
pip install shapely ezdxf pillow
python3 generar.py          # material de 3 mm
python3 generar.py 2.8      # si la placa mide otra cosa (las ranuras se ajustan)
```
Tarda 1 a 2 minutos. Necesita Chromium para las imágenes y los PDF.

## Para revisar en el primer corte (prototipo, sin probar)
- Encastres de las pestañas en las ranuras (si el MDF no mide 3 mm justos, regenerar).
- Hueco del motor (20,4 x 15,4 mm) y agujero del pulsador (12,5 mm): medir lo comprado.
- Que la gomita no patine (si patina, una más chica o una polea más grande).
- Que las ruedas giren libres sin tocar la carrocería.
- Que el motor 130 mueva bien el peso (el Clásico es el más pesado).
