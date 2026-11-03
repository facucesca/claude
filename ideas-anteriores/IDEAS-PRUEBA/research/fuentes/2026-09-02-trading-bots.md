# Informe fuente: Trading algorítmico y finanzas automatizadas (2026-09-02)

> Informe crudo del agente de investigación #2. Análisis informativo/educativo, NO consejo financiero ni impositivo.

**Contexto de mercado verificado (crítico):** 2026 es un año bajista. ETH ~USD 1.885 (-37% en el año), SOL ~USD 103, BTC gran parte del año en USD 60-75k. Funding rates de BTC **negativos durante rachas récord** (46 días consecutivos de funding promedio negativo a abril 2026, la racha más larga desde nov 2022). Esto degrada casi todas las estrategias long-biased y de carry que se venden como "pasivas".

---

## 0. La base empírica: ¿cuánta gente pierde?

- **Brasil (Chague & Giovannetti, FGV, 2013-2017, futuros mini-Ibovespa):** de 19.646 day traders, entre los 1.551 que persistieron >300 días, **97% perdió neto de comisiones**. Solo 1,1% ganó más que el salario mínimo brasileño. **Sin efecto aprendizaje.**
- **Taiwán (Barber, Lee, Liu & Odean; 3.700M transacciones, 1992-2006):** <1% de day traders con retornos positivos persistentes netos. Supervivencia: 44% al año, 15% a los 3 años.
- **EE.UU. (Barber & Odean 2000):** quintil más activo subperformó ~6,5 pp anuales.
- **Agregado:** ~30 estudios en 8 países: tasa de fracaso **70-97%**.
- **Regulatorio (obligatorio por ley):** brokers CFD europeos publican % real de cuentas perdedoras: rango histórico **74-89%**; 2025-2026: 51-84% según broker (eToro ~51-61%).
- **Polymarket (análisis on-chain de 95M transacciones):** solo **0,51% de wallets ganó > USD 1.000**; ~92% en cero o negativo.

**Implicancia:** el riesgo direccional tiene, para el participante mediano, valor esperado negativo tras costos. La automatización automatiza la ejecución, no el edge.

Fuentes: tradicted.com (papers Brasil/Taiwán) · bananafarmer.app (30 estudios) · esma.europa.eu (medidas CFD) · etoro.com/customer-service/general-risk-disclosure (2025-26).

---

## Veredictos por estrategia (matemática con USD 500-1.000)

### Grid/DCA bots (Pionex, 3Commas) — 3/10
Sin mediana documentada de resultados de usuarios (ninguna plataforma publica P&L agregado — eso ya dice algo). El grid gana en lateral y **pierde cuando el precio sale de la banda** (exactamente 2026: ETH -37%). El "grid profit" de las apps es bruto y esconde pérdida no realizada del inventario. 3Commas $20-99/mes se come 5-24% anual de USD 500 — descartado. Es trading direccional disfrazado; revisar banda/par semanalmente. Pionex no verificado como PSAV ante CNV; alternativa: grid bots nativos de Binance (registrado).

### Arbitraje de funding rate / delta-neutral — 2/10 con este capital
2024-2025: 8-18% APY en buenos períodos. **2026: dado vuelta** — funding negativo récord, APY comprimido a un dígito (Ethena como proxy). Matemática con USD 500 (USD 250 por pata) a 8% APY optimista: **USD 40/año = 3,30/mes**; fees round-trip ~0,28% del notional. La fuente más honesta del sector: **inviable bajo USD 5.000; mínimo razonable USD 10.000-25.000** (USD 800-2.000/año en año bueno). Monitoreo de delta/funding obligatorio: 2-5 h/semana. Riesgos: funding negativo sostenido, contraparte en ambas patas (precedente FTX), liquidación en squeezes. Variante tercerizada: sUSDe de Ethena (dígito alto Q2 2026) con riesgo protocolo/depeg — es un rendimiento, no un negocio: 4/10.

### Arbitraje triangular / cross-exchange — 1/10
Muerto para retail en su forma pura: HFT (Jump, Wintermute) captura todo en milisegundos con colocation. Spreads residuales (0,1-2%) solo en estrés/exchanges chicos ilíquidos donde el riesgo de retiro supera el spread. Con latencia doméstica desde Argentina (100-200ms), probabilidad ~nula. El bot es fácil de programar — por eso no funciona: todos lo tienen.

### Copy trading — 2/10
eToro publica que ~51-61% de sus cuentas retail CFD pierden (disclosure legal, rangos hasta 67-84% por jurisdicción). Sin evidencia de que los copiadores le ganen a la mediana. **Conflicto estructural documentado** (CHI 2024 "Stranger Danger"): el líder cobra por volumen/AUM copiado, no por resultado del copiador → incentivo a estrategias que parecen rentables (martingala, alta win rate) hasta que explotan. eToro no opera CFDs con residentes argentinos; queda copy de exchanges cripto. Es lo único genuinamente pasivo del rubro — pasivamente negativo en mediana.

### Market making retail (Hummingbot) — 2/10
Software legítimo y activo, pero sin evidencia pública de que el operador retail mediano gane. Modos de fracaso documentados por el propio proyecto: riesgo de inventario y selección adversa. Patrón comunitario: "makers que ganaron spreads durante semanas y los devolvieron en un día de tendencia". 5-10+ h/semana. Con USD 500: spread 0,1% sobre rotación de USD 500 = USD 0,50 por vuelta; un día malo de inventario = -10%.

### DIY Freqtrade + Claude Code — 3/10 como ingreso; 7/10 como educación
Freqtrade muy vivo (54k estrellas, spot y futuros). README explícito: "for educational purposes only". Problema #1 documentado: **overfitting** — equity curves perfectas en backtest que mueren en vivo (existe strat.ninja, tracker independiente que detecta lookahead bias — que esas herramientas sean necesarias ES el dato). Consenso comunitario: la enorme mayoría de estrategias públicas no son rentables en vivo tras fees; las rentables no se comparten. Claude Code acelera escribir la estrategia 10x; no da un edge que 500.000 personas con las mismas herramientas no tengan. Pipeline serio: semanas de armado + dry-run 1-3 meses + horas semanales permanentes.

### Staking y nodos — delegado 4/10; validador propio 0/10
- ETH: 2,8-4% APY nativo. SOL delegado: 6-7% nominal pero inflación ~5-6% → **real ~1-2%**. Restaking real: 4-7% (los "10-20%" son loops apalancados).
- USD 500 en SOL = USD 30-35/año nominales; en stETH ≈ USD 15-19/año. Es interés sobre un activo volátil, no un ingreso (staker ETH 2026: +3% yield, -37% precio).
- **Validador propio:** ETH exige 32 ETH ≈ USD 60.000+. SOL: vote fees ~USD 40-50k/año + hosting USD 800-1.400/mes → breakeven ~200.000 SOL delegados (~USD 20M). Institucional, no retail.

### Mercados de predicción (Polymarket/Kalshi) — 3/10
Único ángulo con evidencia académica de profits extraíbles (USD 40M+ de arbitraje en Polymarket abr-2024→abr-2025, paper IMDEA), **ya arbitrado**: duración media de oportunidades cayó de 12,3s (2024) a **2,7s (2026)**, 73% capturado por bots sub-100ms. Retail viable según el análisis más honesto: arb cross-platform Kalshi-Polymarket (5-15% anual, capital USD 5-50k) y especialización de dominio (15-30% — trabajo de análisis, no pasivo). **Kalshi es solo EE.UU. (CFTC)** → la pata cross-platform no está disponible legalmente desde Argentina.

### Rulo/arb dólar cripto local — 2/10
Spreads chicos e intermitentes post-unificación cambiaria; BCRA intervino contra rulos; ARCA ve todo (RG 5804/2025). Micro-oportunidad manual ocasional, no bot de ingreso.

---

## Riesgos estructurales y operatoria desde Argentina

**Exchanges (casos con fecha):** Bybit 21-feb-2025: **USD 1.400-1.500M robados** (Lazarus) — ni el cold storage institucional es garantía. WazirX jul-2024: USD 234,9M, usuarios con quita. 2024: ~USD 2.200M drenados; 2026 lleva ~USD 2.100M. FTX (nov-2022) sigue siendo el template de insolvencia: tus fondos son un crédito en un concurso.

**API keys:** sin permiso de retiro, whitelist de IP, keys separadas por bot, jamás en un repo. Vector histórico: key filtrada usada para "trade contra sí mismo" en pares ilíquidos.

**Regulación AR (verificado 2025-2026):** registro **PSAV obligatorio** (CNV; RG 994 mar-2024 + RG 1058 mar-2025; plazos vencidos jul-sep-2025). Registrados verificados: Binance, Lemon, Ripio, Buenbit, Belo, SatoshiTango, Bitso (verificar en registro público CNV). Bybit/OKX/Bitget: sin confirmar.

**Impuestos (panorama, consultar contador):** Ganancias renta cedular **5% fuente AR / 15% extranjera**; Bienes Personales sobre tenencia al 31-dic; IIBB según provincia; **RG 5804/2025: desde may-2026 exchanges reportan movimientos mensualmente a ARCA**. El anonimato operativo local no existe.

---

## Tabla final

| Estrategia | Veredicto | Ingreso realista año 1 con USD 500-1.000 |
|---|---|---|
| Staking delegado / liquid | 4/10 | USD 15-70 (interés, no ingreso; riesgo precio) |
| sUSDe / delta-neutral tercerizado | 4/10 | USD 35-90 (riesgo protocolo) |
| Grid/DCA bots | 3/10 | Mediana probable ≤ 0 en USD en mercado 2026 |
| DIY Freqtrade | 3/10 (7/10 educativo) | Mediana esperada negativa |
| Prediction markets | 3/10 | Requiere USD 5k+ y es trabajo |
| Funding rate arb manual | 2/10 | USD 0-40; inviable bajo USD 5-10k |
| Copy trading | 2/10 | Mediana negativa; conflicto estructural |
| Market making | 2/10 | Centavos/día; cola de riesgo grande |
| Rulo dólar cripto | 2/10 | Comprimido, intermitente |
| Arbitraje triangular | 1/10 | ~0 |
| Validador propio | 0/10 | Requiere USD 60k-20M |

**Las cinco verdades del dominio:**
1. **La matemática del capital chico es implacable:** aun regalando 15% anual, USD 1.000 → USD 12,50/mes. El problema no es la estrategia, es el numerador.
2. **La evidencia sobre trading activo es de las más robustas de las finanzas empíricas:** 70-97% pierde, sin efecto aprendizaje.
3. **Todo "truco" ya fue arbitrado y 2026 lo empeoró.** La IA que te deja programar el bot en una tarde se la dio a cien mil más.
4. **Quien cobra seguro es el que vende la pala.** Casi todas las fuentes optimistas venden algo; casi todas las fuentes con datos duros (reguladores, académicos, on-chain) apuntan al revés. Ese gradiente es el dato.
5. **Lo único con valor esperado claramente positivo es la habilidad del usuario, no su capital.** Saber construir bots/pipelines/automatización tiene mercado real (servicio, producto, empleo remoto USD) con retornos que ningún bot con USD 500 va a igualar.

Si igual se quiere exposición: staking delegado o sUSDe con fracción descartable (como *yield*, conociendo los riesgos), Freqtrade en dry-run como educación meses antes de un peso real, exchange PSAV registrado, API keys sin retiro, todo declarado.

Fuentes completas: papers FGV/Berkeley vía tradicted.com · ESMA · eToro disclosure · CHI 2024 (dl.acm.org/doi/10.1145/3613904.3642715) · hummingbot.org/blog (inventory risk) · github.com/freqtrade · strat.ninja · pistachio.fi / spotedcrypto.com / helius.dev / thegoodshell.com (staking/validadores) · 1023jack.com + paper IMDEA (Polymarket) · CoinDesk 16-abr-2026 + Phemex (funding negativo) · Wikipedia/Crystal Intelligence (hackeos Bybit/WazirX) · CNV registro PSAV · Allende & Brea (RG 1058) · criptoinforme.com / youhodler.ar (impuestos 2026).
