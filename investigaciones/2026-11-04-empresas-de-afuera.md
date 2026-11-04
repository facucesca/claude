# Empresas de afuera que no existen en Argentina — 2026-11-04

Pedido de Facu: dejar de inventar ideas y buscar **empresas reales que ya funcionan en otros países
(China, India, etc.) y que en Argentina no existen**, con más profundidad y leyendo las páginas.

Excel: `investigaciones/2026-11-04-EMPRESAS-DE-AFUERA.xlsx` (hoja EMPRESAS; la lista corta va arriba, en amarillo).
Datos, prompts, descartadas y script: `investigaciones/datos/2026-11-04-afuera/`.

## Cómo se hizo
- **Ronda 1** (6 exploradores por región): China; India; Sudeste Asiático + Japón/Corea; Latinoamérica;
  Turquía + Europa del sur/este; África + Medio Oriente → **74 empresas**.
- **Ronda 2** (6 exploradores más): EE.UU./Canadá/Australia (empresas medianas y "aburridas"); Europa del
  norte; Rusia/Asia Central/Pakistán; China e India 2.ª pasada; agro y alimentos (mundo); industria y
  construcción (mundo) → **61 empresas**.
- Cada empresa: tracción con al menos 2 fuentes, búsqueda en Argentina, por qué funcionó allá, si esa
  condición se da acá, cómo gana plata y por qué la necesitarían. Filtro duro (Regla N.º 3): nada que
  ChatGPT resuelva gratis, nada trivial ni rebuscado, la plata tiene que pasar por el negocio.
- Los exploradores descartaron además unas **250** candidatas (por parecerse a lo anterior o porque ya
  existen acá); están con el motivo en los archivos `*descart*`.
- **Lista corta de Claude: 40 modelos** (algunos juntan 2 empresas del mismo tipo). 20 salieron en el
  cruce final (repetidas o parecidas a ideas viejas).

## Lista corta
**Ronda 1:** Beike (red de inmobiliarias con comisión repartida), MonotaRO + ZKH (insumos de mantenimiento
online para fábricas), Buser + IntrCity (micros por demanda), Grão Direto (compraventa digital de granos),
OfBusiness (materias primas + crédito para PyMEs), Lenskart + Ben & Frank (ópticas baratas con fábrica
propia), Duskin (alfombras y mopas con recambio), Klaim (adelanto a clínicas sobre lo facturado a obras
sociales), Plenergy (estaciones de autoservicio baratas), BasiGo (colectivos eléctricos por km), InPost
(casilleros de paquetes), Via (transporte a demanda municipal), Tuhu (cubiertas online + talleres en red),
Mixue (franquicia que gana con los insumos), Guoquan (comida para preparar en casa), ZhongAn (seguro de
devolución), Pristyn Care (cirugías a precio cerrado), Ayenda + H World (hoteles independientes bajo una
marca), Contabilizei (estudio contable online), Trucksters (camiones por relevos), Jobandtalent (agencia
eventual digital), Reclame Aqui (reclamos públicos).

**Ronda 2:** Pirtek (camionetas que cambian mangueras hidráulicas donde está la máquina), Radwell
(repuestos de automatización discontinuados, reparados y con garantía), Howdens (cocinas en stock solo
para constructores), Tractive (GPS para mascotas con abono), Smart Joules (eficiencia energética pagada con
el ahorro), Buyers Edge (central de compras para restaurantes, la pagan los fabricantes), Acrisure (comprar
carteras de productores de seguros), Snap-on (camioneta-tienda de herramientas para talleres, cuotas
semanales), SERVPRO + Johns Lyng (secado y reparación tras inundación o incendio, paga el seguro),
casas de empeño en cadena (M-Lombard, FirstCash), Ramudden (señalización de obras viales), Timpson
(arreglos rápidos en cabinas de súper), Universal Pure (alta presión HPP a fasón para alimentos),
Busy Ming (golosinas a precio de descuento en franquicia), IndiaMART (marketplace B2B de cotizaciones),
Konsol.pro (contratar y pagar independientes en masa), Pillar To Post (inspección de vivienda antes de
comprar), U-Haul (alquiler de camiones que maneja el cliente).

## Lo que falta verificar
Varias empresas tienen una sola búsqueda en Argentina (cupo de 30 búsquedas por explorador). Antes de
elegir, la **fase 3** hace la ficha a fondo: unidad económica, competencia argentina con varias búsquedas,
regulación, capital necesario y cómo arrancar.
