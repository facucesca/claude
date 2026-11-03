# Proyecto: Clipper Semi-Auto — Plan de ejecución

**Aprobado:** 2026-09-03 · **Naturaleza:** experimento de cash-flow con gate de corte a la semana 8. NO es el proyecto principal (ese es `stack-de-datos`); consume ~30% de las horas del primer mes y después decide su propia vida con números.

## La pregunta que originó esto: "¿un bot que clipee y suba, o no?"

**Respuesta del estudio: sí se puede construir, pero el 100% automático gana $0.** La evidencia (informe `research/fuentes/2026-09-02-video-clipping.md`):

1. **Lo que SÍ se automatiza bien:** encontrar campañas, bajar el material fuente, detectar momentos clipeables, cortar, subtitular, formatear a 9:16, publicar (vía integración oficial) y trackear vistas/pagos. Eso es ~90% del trabajo.
2. **Lo que NO conviene automatizar al 100%:**
   - **La selección final del clip.** La plata = vistas × tarifa, y las vistas salen de la calidad del momento elegido y el hook. Un bot que sube todo lo que corta produce clips mediocres → ~0 vistas → $0. La mediana del clipper es USD 305 *de por vida* justamente porque la mayoría spamea sin criterio. **[Corrección 2026-10-08: USD 305 es un PROMEDIO (USD 2,58 M ÷ 8.466 personas que cobraron, Ascynd 2026-07-24), no una mediana. La mediana real no se publica y es bastante menor. Ver `research/fuentes/2026-10-08-L3-L8-A3-video-y-visualizacion.md`.]**
   - **El cumplimiento de reglas por campaña** (hashtags, créditos, ediciones prohibidas): incumplir = rechazo del pago *después* de acumular las vistas.
   - **La salud de la cuenta.** TikTok penaliza contenido no-original desde el 15/9/2025 (supresión del For You + strikes); multi-cuenta y APIs no oficiales = baneo. Las cuentas son el activo frágil del negocio.
3. **La solución de diseño: cola de aprobación.** El bot hace todo y te deja los mejores candidatos listos en Telegram; vos aprobás con un tap. Tu único trabajo: **15-30 min por día, o 2 bloques semanales.** Eso respeta la regla de oro de pasividad y multiplica el rendimiento por clip.

## Arquitectura del sistema

```
[1] SCANNER de campañas (Whop Content Rewards)
    scraping: presupuesto restante, tarifa/1k, velocidad de quema,
    reglas, historial de pago del dueño → ranking diario → Telegram
         ↓ (elegís campaña con un tap)
[2] INGESTA del material fuente de la campaña
         ↓
[3] CORTE automático: detección de momentos + subtítulos + 9:16 + hook
    (Higgsfield clipper ya conectado / API de herramienta de clipping)
         ↓
[4] COLA DE APROBACIÓN → te llegan N candidatos/día a Telegram
    [único paso humano: aprobar / descartar / editar título]
         ↓
[5] PUBLICACIÓN vía integración OFICIAL de TikTok (Higgsfield tiktok_publish)
    — nunca APIs no oficiales, nunca multi-cuenta —
         ↓
[6] SUBMISSION a la campaña + tracking de vistas y pagos → resumen diario
```

## Reglas duras (salen de la investigación, no se negocian)

- 1 sola cuenta por plataforma. Multi-cuenta = violación de ToS con detección activa.
- Solo campañas con >60% de presupuesto restante (regla comunitaria: pool agotado = vistas gratis).
- Transformación real en cada clip (recorte + subtítulos + hook ≠ repost con watermark).
- Checklist de reglas por campaña generado por el scanner y validado antes de publicar.
- Publicación únicamente por vías oficiales (Higgsfield/TikTok API oficial).

## Cronograma (dentro de las 10-15 h/semana totales, ~30% acá el primer mes)

### Semanas 1-2 — Scanner
- [ ] Scraper de campañas de Whop Content Rewards (+ Vyro/Ssemble si aportan volumen).
- [ ] Modelo de ranking: tarifa efectiva esperada, presupuesto restante, velocidad de quema, historial del owner.
- [ ] Alerta diaria a Telegram con top 5 campañas.
- [ ] Crear cuenta Whop y **verificar método de payout para Argentina** (pendiente del estudio; 10 minutos).

### Semanas 2-4 — Pipeline de clipeo
- [ ] Ingesta + corte automático + subtítulos + formato (probar primero el clipper de Higgsfield, ya conectado; fallback: API de clipping de terceros ~USD 10-30/mes).
- [ ] Cola de aprobación en Telegram (aprobar/descartar/editar con botones).
- [ ] Publicación vía TikTok oficial + submission a Whop + tracking.

### Semanas 4-8 — Operación del experimento
- [ ] Ritmo objetivo: 3-7 clips aprobados/día en campañas bien elegidas.
- [ ] Registrar por clip: campaña, vistas, acreditado, rechazos. Todo a AVANCE.md semanal.

## Gate de la semana 8 (decisión con números, sin nostalgia)

| Resultado | Decisión |
|---|---|
| ≥ USD 100 acumulados y ≤4 h/semana del usuario | Sigue como línea de cash; evaluar empaquetar el scanner |
| < USD 100 acumulados | Se mata el clipeo propio |
| Funcionó el scanner (independiente de lo anterior) | **Pivot a producto:** venderlo a los 8.400+ clippers activos (mercado demostrado) vía Whop — eso ya es semi-pasivo y entra al portfolio general |

## Expectativa honesta

Mediana del clipper: USD 305 de por vida. **[Corrección 2026-10-08: USD 305 es un PROMEDIO (USD 2,58 M ÷ 8.466 personas que cobraron, Ascynd 2026-07-24), no una mediana. La mediana real no se publica y es bastante menor. Ver `research/fuentes/2026-10-08-L3-L8-A3-video-y-visualizacion.md`.]** Con scanner + curaduría con criterio: USD 100-500/mes hacia las semanas 4-8 es el escenario razonable; USD 1.000+/mes es percentil alto. El valor real del experimento aunque el clipeo muera: (1) valida todo el circuito de cobro, (2) deja construido un scanner vendible, (3) alimenta el know-how de video del stack (Higgsfield).
