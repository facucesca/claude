# Empezar acá (para analizar todo con Claude en tu compu)

1. Descomprimí el zip en una carpeta (por ejemplo `Documentos/negocios`).
2. Abrí esa carpeta con Claude Code (app de escritorio → Code → elegir carpeta) y escribí "hola".
   Claude lee solo el `CLAUDE.md`: ahí están las reglas (nada inventado, no repetir, Regla N.º 3) y el estado.

## Qué hay (todo lo investigado, sin excepción)
| Dónde | Qué |
|---|---|
| `investigaciones/2026-11-04-EMPRESAS-DE-AFUERA.xlsx` | **Lo más útil:** 201 empresas reales de afuera que no existen en Argentina (3 rondas), lista corta de ~57 en amarillo. Resumen en `2026-11-04-empresas-de-afuera.md`. |
| `investigaciones/2026-11-03-IDEAS-NUEVAS.xlsx` | 232 ideas (gran escala + chicas). Rechazadas por Facu el 2026-11-04, quedan como consulta. |
| `investigaciones/2026-11-04-IDEAS-NICHOS-Y-APPS.xlsx` | 105 ideas de nichos/apps + 30 lecciones. Rechazadas, quedan como consulta. |
| `investigaciones/registro-nuevo.csv` | Todo lo investigado desde el 2026-11-03 (ideas y empresas), para no repetir. |
| `investigaciones/datos/` | Datos crudos de cada investigación: JSON de cada explorador, descartadas con su motivo, prompts usados, listas de exclusión y scripts que regeneran los Excel (`build_excel.py`). |
| `ideas-anteriores/IDEAS-PRUEBA/` | Todo lo de septiembre-octubre 2026 (≈1.500 ideas, Excels, MEMORY.md con tu perfil). |
| `backup-juguetes-madera/` | El proyecto de juguetes de madera, guardado tal cual. |
| `herramientas/` | `md_a_pdf.py` (pasar un .md a PDF). |

## Ideas de preguntas para tu Claude local
- "Leé `investigaciones/2026-11-04-EMPRESAS-DE-AFUERA.xlsx` y armá la ficha a fondo de [empresa]."
- "De la lista corta, ¿cuáles puedo arrancar con menos de USD 1.000 y aprovechando CEMEVA?"
- "Buscá patrones entre las 201 empresas: qué tipo de negocio se repite más."

Para regenerar los Excel hace falta Python con `openpyxl` (`pip install -r requirements.txt`).
