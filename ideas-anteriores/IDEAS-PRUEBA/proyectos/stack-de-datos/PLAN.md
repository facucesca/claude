# Proyecto: Stack de Datos — Plan de ejecución

**Aprobado:** 2026-09-03 · **Dedicación elegida:** 10-15 h/semana del usuario (los agentes construyen, el usuario dirige) · **Horizonte:** ~3 meses hasta stack completo operando.

**Qué es:** un solo activo subyacente — scrapers de datos de nichos LATAM/agénticos, auto-reparables — monetizado por varias bocas: Apify Store (núcleo), micro-herramientas web, servidores MCP, bot de Telegram, y más adelante SaaS de alertas B2B. Basado en el estudio `research/2026-09-02-estudio-mercado-ingresos-pasivos-ia.md`.

## Regla de oro (no negociable)

El usuario NO vigila nada a diario. Diseño obligatorio de cada pieza:
- Corre en la nube (Apify / Cloudflare). La PC del usuario puede estar apagada.
- Si algo falla → alerta al Telegram del usuario. Sin alerta = no existe.
- La guardia técnica la hacen agentes programados (triage de errores, reparación de scrapers, borradores de soporte). El usuario aprueba, no ejecuta.
- Todo lo que requiere decisión humana se acumula en UN bloque semanal (2-3 h).
- En régimen: ≤5 h/semana en total. Idea que exija más sistemáticamente → se automatiza más, se vende o se mata.

---

## FASE 0 — Rieles y nichos (semanas 1-2)

### 0.1 Rieles de cobro (bloquean todo lo demás — empezar acá)
- [ ] Payoneer: abrir/verificar cuenta.
- [ ] Apify: crear cuenta, configurar payout (SWIFT, mín USD 100) y leer términos vigentes de monetización + KYC para pagos agénticos.
- [ ] Paddle: iniciar onboarding como seller argentino (revisan el producto; puede tardar — por eso va primero).
- [ ] Contador: consulta por Factura E, monotributo exportación de servicios, y tratamiento de cobros en cripto. (30-60 min de reunión.)
- [ ] Registrar en AVANCE.md qué riel quedó operativo y cuál trabado.

### 0.2 Elección de 3 nichos de datos
Criterios (todos deben cumplirse):
1. Demanda comprobable: gente/empresas/agentes que ya buscan ese dato (búsquedas en Apify Store, foros, keywords).
2. Sin incumbente fuerte en Apify (los nichos obvios — LinkedIn, Amazon, Instagram — están tomados; el caso de referencia ganó con nichos vacíos).
3. Fuente scrapeable de forma sostenible y legalmente defendible (datos públicos; evitar login walls y datos personales).
4. Bonus LATAM: fuentes hispanas que la competencia anglo ignora.

Candidatos a investigar (del estudio — validar, no asumir):
- [ ] Mercado Libre por verticales (precios/sellers/tendencias por categoría).
- [ ] Portales inmobiliarios AR/LATAM (Zonaprop, Argenprop, etc.).
- [ ] Empleo AR/LATAM (portales locales que los agregadores globales ignoran).
- [ ] Licitaciones y compras públicas AR/LATAM (boletines oficiales).
- [ ] Datos regulatorios/normativa (BCRA, ARCA, boletín oficial — alertas de cambios).
- [ ] Un vertical B2B global sin cobertura (detectar huecos buscando en Apify Store qué se pide y no existe).
- [ ] **Entregable:** documento `ideas/nichos-elegidos.md` con los 3 elegidos, evidencia de demanda y fuente por nicho.

**Gate Fase 0:** rieles operativos (mínimo Payoneer + Apify) y 3 nichos documentados. Sin esto no se escribe código de producción.

---

## FASE 1 — Núcleo Apify (semanas 3-8)

### 1.1 Fundación técnica (semana 3-4)
- [ ] Template "gold standard" de actor: pricing pay-per-event bien diseñado, README orientado a humanos Y agentes (casos de uso, ejemplos de output), tests, manejo de errores, logging.
- [ ] Pipeline de auto-reparación: workflow con Claude Code que, ante falla de selector/HTML, intenta el fix, corre tests y deja PR/alerta para aprobar en el bloque semanal.
- [ ] Canal de alertas: bot de Telegram propio que reporta fallas, ventas y métricas diarias en UN mensaje resumen.
- [ ] Primeros 3 actores del nicho 1 publicados.

### 1.2 Catálogo (semanas 5-6)
- [ ] 6-8 actores más (nichos 2 y 3). Regla: mejor 10 actores excelentes con README/SEO cuidado que 30 mediocres (una review de 1 estrella cuesta semanas de uso).
- [ ] SEO del listing: keywords en título/descripción, ejemplos de datos reales, video corto si aplica.

### 1.3 Iteración con uso real (semanas 7-8)
- [ ] Analizar qué actores tienen runs/usuarios → duplicar ahí, matar los muertos.
- [ ] Ajustar pricing PPE según consumo real (la migración forzada de Apify a PPE en oct-2026 deja competidores mal precificados — ventaja para nosotros).
- [ ] Habilitar elegibilidad agéntica (x402) donde aplique.

**Gate día 60:** ≥1 actor con usuarios pagos y ≥USD 50 cobrados acumulados por cualquier vía. Si no se cumple: sesión de replanteo de nichos (los 3 elegidos, no el modelo).

---

## FASE 2 — Bocas adicionales (semanas 9-12)

### 2.1 Micro-herramientas web (sobre los MISMOS datos)
- [ ] 10-15 herramientas (calculadoras/consultas/generadores) en Cloudflare Pages/Workers. Prioridad: español + long-tail sin competencia (sueldo neto AR, monotributo, comparadores con datos de los actores).
- [ ] Cada página diseñada para ser citada por LLMs: datos con fecha, estructura limpia, llms.txt.
- [ ] AdSense: aplicar apenas haya 10+ páginas con tráfico inicial.
- [ ] Tier pro (sin límites/API) vía Paddle en las 2 mejores herramientas.

### 2.2 Capa MCP
- [ ] Exponer los 5 mejores actores como servidores MCP (mismo código, boca nueva; cobro por llamada vía Apify).

### 2.3 Bot de Telegram (si algún nicho tiene público local)
- [ ] Bot de alertas sobre los datos ya scrapeados (ej: alertas inmobiliarias, licitaciones, precios). Cobro: Stars o Mercado Pago según público.

**Gate día 120:** portfolio combinado ≥ USD 150-300/mes. Pasa → Fase 3. No pasa → duplicar solo en lo que tenga señal y matar el resto sin nostalgia.

---

## FASE 3 — El activo grande (mes 4+, plan detallado recién al llegar)

- SaaS de alertas B2B sobre el nicho ganador (hard paywall + trial 2-4 semanas, Paddle). Objetivo: activo vendible a ~3,9x profit anual.
- Newsletter de retención sobre la audiencia de las herramientas.
- (Opcional, decisión separada: YouTube editorial — recordar deadline YPP 1/2/2027.)

---

## Operación en régimen (el diseño anti-"estar arriba")

| Pieza | Quién la hace | Frecuencia |
|---|---|---|
| Chequeo de salud de actores/tools | Monitoreo automático | Continuo |
| Reparación de scrapers rotos | Agente programado (propone fix + test) | Al fallar |
| Soporte a usuarios | Agente deja borrador de respuesta | Al llegar |
| Resumen de métricas y ventas | Bot de Telegram, 1 mensaje diario | Diario |
| Decisiones (aprobar fixes, responder, pricing) | **Usuario — bloque único** | 1 bloque/semana (2-3 h) |

## Métricas (revisar en el bloque semanal, registrar en AVANCE.md)

- Actores publicados / con usuarios activos / con revenue.
- Revenue por boca (Apify, ads, Paddle, Telegram) — bruto y neto.
- **Horas reales del usuario esa semana** (verificamos la promesa de pasividad con datos, como todo lo demás).
- Fallas abiertas > 7 días (deuda de guardia).

## Presupuesto

- Costos fijos: USD 0-50/mes (Apify plan dev + dominios; Cloudflare ~0).
- Capital total estimado hasta gate día 120: < USD 200 fuera de suscripciones de herramientas de IA ya existentes.
