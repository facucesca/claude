# Consigna de limpieza (Regla N.º 2) — búsqueda NICHOS-Y-PROBLEMAS-2 (2026-10-14)

Sos revisor. Tenés que clasificar cada fila nueva contra TODO lo investigado antes. Español, criterio estricto, nada inventado.

## Insumos
- Las filas nuevas: `C:\FACU\IDEAS-PRUEBA\research\datos\2026-10-14-nichos-2\NN-*.json` (los archivos que te tocan). Leé `problema`, `detalle`, `quien_paga` y `parecido_a` de cada fila (ignorá el objeto `_extras`).
- El registro: `C:\FACU\IDEAS-PRUEBA\research\datos\registro-de-ideas.csv` (902 entradas: 633 ideas de TODAS-LAS-IDEAS, ideas propias "Lx (propia)", y 250 problemas de la búsqueda anterior con ids tipo SAL-1-1). La columna `decision_facu` dice si Facu la ELIGIÓ ("elegida...") o NO ("NO elegida...", "DESCARTADA", "repetía..."). Leelo COMPLETO (no solo por palabras).
- Ayuda automática (solo pista, no decisión): `C:\FACU\IDEAS-PRUEBA\research\datos\2026-10-14-nichos-2\_cruce-automatico.txt` (para cada fila, las entradas del registro con más palabras en común).
- Aclaración: EDU-1-4 en el registro dice "cubrir ausencia docente", pero Facu lo eligió con una nota propia: "RFID para chicos en jardines/colegios". Tratalo como ganador de ambos temas. L12 = cámaras de seguridad con IA (ganador). L13 = RFID para otras cosas (ganador). L14 = stock de piezas chicas (ganador). L10 = góndola/stock por foto (ganador). L6 = Uber de logística (ganador). L1 = intermediario/cierre seguro de autos usados (ganador). A1 = escrow (ficha propia).

## Estados (uno por fila)
- **C = repite**: mismo problema y mismo tipo de cliente que una entrada anterior (ganadora o no), aunque esté planteada distinto (por ejemplo antes como servicio y ahora como software, o en otro rubro con el mismo cliente y el mismo dolor). → sale.
- **R = parecida a algo NO elegido/rechazado/descartado**: no es idéntica, pero comparte el problema central o es la misma solución aplicada a un cliente vecino, de modo que Facu la estaría rechazando de nuevo (ej.: agenda/turnos online, chatbot de atención, reactivación de clientes, contenido para redes, planilla de socios/cuotas, monitoreo de precios genérico, si ya fueron rechazados). → sale.
- **P = parecida a un GANADOR** (decision_facu empieza con "elegida"): comparte cliente o tecnología o un problema vecino con algo que Facu eligió, sin ser idéntica. → queda como variante. Si es IDÉNTICA a un ganador (mismo problema, mismo cliente), es C.
- **N = nueva**: nada parecido en el registro.
Regla de desempate: si se parece a un ganador Y a un rechazado, decidí cuál es más cercano; si es idéntica al rechazado, R/C. Un parecido solo de tecnología (ej.: "usa RFID", "usa cámaras") NO alcanza para R: tiene que compartir el problema y el tipo de cliente. Un parecido de tecnología con un ganador (L12, L13, L14, L10) sí alcanza para P.

## Salida
Escribí con Write un JSON en la ruta que te indico, con este formato:
```json
{"cruce": {"TUR-1-1": {"estado": "N|P|C|R", "repite_o_se_parece_a": "ids del registro separados por coma, ej. 'F27, H34' ('' si N)", "nota": "una frase: por qué"}, ...},
 "posibles_fusiones_dentro_de_mis_nichos": [["ID1","ID2","tema"]]}
```
Todas las filas de tus archivos tienen que estar en `cruce`. Respondé al final solo con un resumen de ≤80 palabras: cuántas N, P, C, R.
