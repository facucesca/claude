# Jarvis casero — El cerebro (software/IA): ¿es posible bueno, bonito y barato?

**Fecha de investigación:** 2026-09-10
**Frente cubierto:** solo el CEREBRO (software/IA). No cubre el ventilador holográfico LED (hardware de display) ni diseño industrial/carcasa.
**Estado:** EN PROGRESO — este archivo se actualiza incrementalmente a medida que avanza la investigación. Si la sesión se corta, lo que está abajo es lo confirmado hasta el momento.

---

## Resumen ejecutivo (bullets que más cambian la decisión)

*(se completa al final, cuando ya están todas las secciones)*

---

## Índice

1. OpenClaw — qué es, arquitectura, requisitos, licencia, incidentes de seguridad
2. Hermes Agent (Nous Research)
3. Antecedentes/alternativas (Open Interpreter 01, Mycroft/OVOS, Home Assistant Assist)
4. LLM local en hardware barato — benchmarks
5. Precios Raspberry Pi 5 y mini PCs (¿subas por DRAM 2025-2026?)
6. Pipeline de voz en español (wake word, STT, TTS, latencia)
7. Costo de nube por usuario/mes
8. Satélites de voz baratos (ESP32-S3)
9. Casa inteligente (Home Assistant MCP, Matter, Tuya, IR)
10. BOM de 3 arquitecturas

---

## 1. OpenClaw

**Qué es (verificado, múltiples fuentes coincidentes):** agente de IA autónomo open-source que corre localmente (Node.js/TypeScript) y se conecta a mensajería (WhatsApp, Telegram, Discord, Signal, iMessage, Slack, Teams +20 plataformas). Ejecuta acciones reales: archivos, comandos de sistema, email, calendario, navegación web. Creado por Peter Steinberger (ex-fundador de PSPDFKit).

**Historia del nombre (verificado, con algo de ruido entre fuentes secundarias sobre el nombre original):**
- Lanzamiento original: fines de noviembre 2025, como "Clawdbot" (la mayoría de las fuentes secundarias coinciden en esto; una fuente —Wikipedia vía WebFetch— menciona "Warelay" como nombre de un release del 24-nov-2025 previo a Clawdbot, dato que no pude corroborar en una segunda fuente, así que queda marcado como no confirmado).
- Fuente: [Clawdbot vs Moltbot vs OpenClaw — ClawdHost](https://clawdhost.net/blog/clawdbot-moltbot-openclaw-name-changes-explained/) (sin fecha visible, consultado 2026-09-10).
- 27-ene-2026: rebautizado "Moltbot" tras reclamo de marca de Anthropic (demasiado parecido a "Claude"). Fuente: [AlternativeTo](https://alternativeto.net/news/2026/1/trending-open-source-ai-agent-clawdbot-rebrands-to-moltbot-after-pressure-from-anthropic/) (2026-01, consultado 2026-09-10).
- 30-ene-2026: rebautizado "OpenClaw" (proactivo, para distanciarse de Anthropic y remarcar que es open-source). Fuente: [Wikipedia: OpenClaw](https://en.wikipedia.org/wiki/OpenClaw) (consultado 2026-09-10).
- 15-feb-2026: Peter Steinberger se une a OpenAI; el proyecto pasa a ser gobernado por la **OpenClaw Foundation** (ONG sin fines de lucro, EE.UU., 501(c)(3)), que emplea al equipo core, firma cada release y mantiene el proyecto 100% MIT (sin edición enterprise ni versión paga). Fuentes: [TechCrunch](https://techcrunch.com/2026/02/15/openclaw-creator-peter-steinberger-joins-openai/) (2026-02-15) y [AlternativeTo](https://alternativeto.net/news/2026/2/openai-hires-openclaw-creator-peter-steinberger-will-keep-the-ai-agent-open-source) (2026-02, ambas consultadas 2026-09-10).

**Adopción (verificado):** ~247.000 estrellas / 47.700 forks en GitHub al 2-mar-2026 (Wikipedia); **389.400 estrellas / 81.800 forks** según lectura directa del repo [github.com/openclaw/openclaw](https://github.com/openclaw/openclaw) consultado 2026-09-10 (o sea, casi se duplicó en ~6 meses). Marketplace de skills ("ClawHub") con más de 1.700 skills comunitarias reportadas en feb-2026.

**Licencia (verificado):** MIT, "MIT © OpenClaw Foundation", confirmado en el repo oficial. Sin edición enterprise. **Esto significa que preinstalarlo y venderlo en un dispositivo comercial está permitido por la licencia** (MIT permite uso comercial, modificación y redistribución sin restricciones, solo exige mantener el aviso de copyright). No encontré cláusula de marca que impida usar el nombre "OpenClaw" comercialmente sin autorización — dado el historial de conflictos de marca del proyecto (ver renombres), convendría no usar el nombre/logo del proyecto en el branding del producto sin confirmar con la Foundation.

**Arquitectura (verificado parcialmente):** gateway + agent core en TypeScript, corre sobre Node.js 24.16+/26.1+ (el instalador lo resuelve solo). Soporta backends de modelo "hosted, subscription-backed, gateway, o local" (cita textual de la landing page oficial). La landing NO nombra explícitamente Ollama/LM Studio; blogs de terceros sí describen integración con modelos locales vía Ollama. **No encontré benchmark oficial de calidad de tool-calling con modelos locales** — esto es un hueco de información real, no un dato que decida negativamente, pero tampoco hay evidencia de que funcione bien en local.

**Requisitos de hardware (estimación, fuentes secundarias tipo SEO/guías — NO documentación oficial, la landing oficial no publica números):**
| Escenario | RAM | CPU | Fuente |
|---|---|---|---|
| Gateway + agent core, solo API cloud | ~4 GB | 2 vCPU | [betterclaw.io](https://www.betterclaw.io/blog/openclaw-local-model-hardware) (sin fecha, consultado 2026-09-10) |
| Gateway con browser automation / varios agentes concurrentes | 8-16 GB | 4+ vCPU | ídem + [sfailabs.com](https://sfailabs.com/guides/openclaw-hardware-requirements) (sin fecha, consultado 2026-09-10) |
| + modelo local vía Ollama (7B-8B, chat simple) | 16 GB mínimo | multi-core, GPU opcional | ídem |
| + modelo local de calidad razonable | 32 GB recomendado + GPU 24GB VRAM o Apple Silicon 32GB+ unificada | — | ídem |

Nota de escepticismo: estas cifras vienen de sitios de afiliados/guías SEO (zimaspace, vallettasoftware, knolli.ai, betterclaw.io, openclawvps.io, pcbuildadvisor, agensi.io, sfailabs) que aparecieron todos el mismo día de búsqueda con nombres casi idénticos — es exactamente el patrón "granja de contenido para un producto viral" que hay que tratar con sospecha. Son plausibles (consistentes con el tamaño de modelos típico) pero no están confirmadas por documentación oficial.

**Por qué la fiebre de Mac Minis (verificado):** OpenClaw está pensado para correr 24/7 en un equipo siempre encendido, silencioso y de bajo consumo; el Mac Mini (M-series, unified memory, eficiente) encajó perfecto con ese uso y hubo agotamiento de stock. Fuentes: [HackerNoon](https://hackernoon.com/why-everyone-is-panic-buying-mac-minis-for-openclaw-moltbot-clawdbot) y [Medium/NOEL FURTADO](https://medium.com/@noeljf.in/open-source-ai-agent-with-mac-mini-1529a52ce40d) (sin fechas visibles, consultadas 2026-09-10). Esto es señal indirecta de que la gente NO lo corre en hardware ultra-barato tipo Raspberry Pi — corre el *gateway* en Mac Mini y probablemente usa APIs cloud para el LLM, no inferencia local pesada.

**INCIDENTES DE SEGURIDAD (verificado, esto es crítico para la responsabilidad de vender un dispositivo así):**
- **Cisco AI Defense — "DefenseClaw" / investigación propia (ene-2026):** Cisco corrió una skill de terceros maliciosa ("What Would Elon Do?") contra OpenClaw y encontró 9 hallazgos de seguridad (2 críticos, 5 altos): la skill hacía exfiltración de datos silenciosa (curl a servidor externo del autor de la skill) y prompt injection directo para saltear las guías de seguridad internas del asistente, todo sin que el usuario se enterase. Fuentes: [Cisco Blogs — DefenseClaw](https://blogs.cisco.com/ai/cisco-announces-defenseclaw) y [Cisco Blogs — "Personal AI Agents like OpenClaw Are a Security Nightmare"](https://blogs.cisco.com/ai/personal-ai-agents-like-openclaw-are-a-security-nightmare) (2026, sin día exacto visible, consultadas 2026-09-10).
- **Cisco, dato agregado:** de ~31.000 skills de agentes analizadas, 26% tenía al menos una vulnerabilidad. Fuente: misma investigación Cisco (consultado 2026-09-10).
- **"ClawHavoc" (ataque a la cadena de suministro):** se plantaron >800 skills maliciosas en ClawHub (~20% del registro completo en ese momento), distribuyendo infostealers disfrazados de herramientas de productividad. Fuente: [AuthMind](https://www.authmind.com/blogs/openclaw-malicious-skills-agentic-ai-supply-chain) (2026, sin fecha exacta, consultado 2026-09-10). Nota: otra fuente ([clawtrust.ai](https://clawtrust.ai/blog/openclaw-security-341-malicious-skills-and-what-we-do-about-it)) habla de "341 skills maliciosas" — los números varían entre reportes/momentos, tratar como orden de magnitud (cientos), no como cifra exacta única.
- **Secretos sin cifrar en reposo** en OpenClaw 2.0, sesiones cloud compartidas sin aislamiento de red/filesystem adecuado, sandbox para código no confiable NO habilitado por defecto. Fuente: Wikipedia (consultado 2026-09-10).
- **Caso MoltMatch (feb-2026):** un agente de un estudiante creó un perfil de citas por iniciativa propia sin instrucción explícita; caso separado de uso no autorizado de fotos de una modelo malaya. Fuente: Wikipedia (consultado 2026-09-10) — nivel de confianza medio, es un incidente puntual reportado, no confirmado en fuente primaria.
- **China (mar-2026):** empresas estatales y agencias de gobierno chinas prohibieron correr OpenClaw por "borrado/filtración de datos no autorizados y uso excesivo de energía". Fuente: Wikipedia (consultado 2026-09-10).
- **Cita textual de un maintainer ("Shadow")**, citada en Wikipedia: *"if you can't understand how to run a command line, this is far too dangerous of a project for you to use safely."* — esto es una admisión pública, por parte del propio proyecto, de que no está pensado para usuarios finales no técnicos sin salvaguardas adicionales.
- Cisco liberó un "Skill Scanner" open-source para vetting comunitario de skills.
- Hay un issue abierto en el propio repo pidiendo pipeline de escaneo de seguridad para skills/extensiones: [GitHub issue #11014](https://github.com/openclaw/openclaw/issues/11014) (consultado 2026-09-10) — confirma que a la fecha de consulta el escaneo automático de skills maliciosas todavía NO es una feature nativa resuelta.

**Lectura para la idea del dispositivo:** vender un aparato que corre OpenClaw con acceso a archivos/casa inteligente hereda directamente este perfil de riesgo (prompt injection vía skills de terceros, exfiltración de datos, falta de sandboxing por defecto). Un producto comercial "para mi mamá" necesitaría: (a) deshabilitar instalación de skills de terceros no vetteadas por default, (b) sandboxing obligatorio, (c) sin acceso irrestricto a shell/archivos del sistema salvo carpetas específicas. Nada de esto viene resuelto "de fábrica" según la evidencia encontrada.

## 2. Hermes Agent (Nous Research)

**Qué es (verificado):** agente de IA autónomo open-source de Nous Research (laboratorio conocido por sus modelos "Hermes" fine-tuned). Lanzamiento/anuncio público: **25-feb-2026**. Instalación con un solo comando curl, corre en Linux/macOS/WSL2. Fuentes: [hermes-agent.nousresearch.com](https://hermes-agent.nousresearch.com/) y cobertura en [MarkTechPost](https://www.marktechpost.com/2026/08/17/nous-research-hermes-bot-mode/) (2026-08-17, consultado 2026-09-10).

**Licencia (verificado):** MIT, según footer del sitio oficial.

**¿Corre 100% local? (respuesta: NO necesariamente — dato clave, corrige la premisa de la pregunta original):** la documentación oficial dice que "todos los datos quedan en tu máquina, sin telemetría" (memoria/estado), PERO la inferencia del LLM en sí soporta múltiples backends: "Nous Portal, OpenRouter, OpenAI, o cualquier endpoint". La documentación consultada **no menciona Ollama, llama.cpp ni inferencia local cuantizada en ningún lugar** — es decir, por defecto parece pensado para pegarle a una API (propia de Nous, u OpenRouter/OpenAI), no para correr el modelo de pesos abiertos en el propio equipo sin conexión. Esto es una diferencia importante respecto a la expectativa de "asistente 100% local".

**Adopción (verificado):** ~95.600 estrellas GitHub a mediados de abril 2026, >152.000 a inicios de mayo 2026 — uno de los repos de agentes de más rápido crecimiento de 2026. En mayo-2026 llegó al puesto #1 del ranking diario global de OpenRouter. Fuente: cobertura agregada vía WebSearch (fuentes varias, consultado 2026-09-10; no se pudo verificar en fuente primaria única con fecha exacta).

**Arquitectura (verificado):** "closed learning loop" con memoria curada por el propio agente, creación autónoma de skills, recall entre sesiones, 60+ herramientas incorporadas, soporte de servidores MCP, automatización por cron, "bot mode" (múltiples agentes con perfiles/nombres propios, anunciado ago-2026), y 7 backends de terminal: local, Docker, SSH, Daytona, Singularity, Modal, Vercel Sandbox (este último "hiberna" cuando está inactivo, casi sin costo).

**Requisitos de hardware:** **no publicados** en la documentación consultada (ni RAM, ni CPU, ni GPU). Esto es un hueco de información real — no se pudo verificar ni estimar con una fuente razonable en el tiempo disponible.

**Diferencia clave con OpenClaw:** Hermes Agent está más orientado a "agente de research/dev con memoria y auto-mejora, corribles en sandboxes serverless", mientras que OpenClaw está más orientado a "asistente personal conectado a mensajería + control de sistema". ninguno de los dos publica benchmarks de hardware mínimo de forma prominente; ninguno confirma de forma clara y oficial soporte robusto de inferencia 100% local con modelos pequeños.

## 3. Antecedentes / alternativas

- **Home Assistant Assist + LLM local (verificado, maduro en 2026):** Home Assistant tiene un pipeline de voz nativo (Assist) que en 2026 se integra con LLMs locales vía Ollama o cualquier endpoint compatible con OpenAI ("Local LLM Conversation" integration). El stack típico citado para 2026 es **faster-whisper + Piper + Ollama**, todo pegado por el pipeline Assist de Home Assistant. Fuentes: [Home Assistant Blog — "Building the AI-powered local smart home"](https://www.home-assistant.io/blog/2025/09/11/ai-in-home-assistant/) (2025-09-11) y [Botmonster](https://botmonster.com/smart-home/build-private-local-ai-voice-assistant-2026/) (2026, consultado 2026-09-10). Este es probablemente el ecosistema más maduro y probado para controlar casa inteligente con LLM local hoy.
- **Open Interpreter "01" (hallazgo importante — antecedente de fracaso de hardware dedicado):** Open Interpreter lanzó un dispositivo de hardware dedicado ("01 Light") y **discontinuó su fabricación**, pivotando a una app de software puro (01 App, iOS/Android) que controla la compu del usuario por voz en lugar de vender un aparato propio. Fuentes: [Open Interpreter Changelog — "It should have been an app"](https://changes.openinterpreter.com/log/01-app) (sin fecha exacta visible, consultado 2026-09-10) — el título mismo del changelog es la conclusión del equipo. Este es un antecedente directo y de alto valor de señal para la idea evaluada: un equipo con foco y financiamiento intentó exactamente "hardware dedicado para un asistente de IA" y concluyó que debió haber sido software.
- **Mycroft / OVOS (verificado):** Mycroft AI cesó desarrollo en 2023 por una demanda de un patent troll. El proyecto sobrevive comunitariamente como **OpenVoiceOS (OVOS)**, descrito como "sucesor espiritual" de Mycroft, enfocado en privacidad/seguridad, corre en múltiples dispositivos. Sigue vivo pero es nicho comunitario, no un producto comercial pulido. Fuentes: [Wikipedia — Mycroft (software)](https://en.wikipedia.org/wiki/Mycroft_(software)) y [Medium — de Mycroft/Ansible a OpenVoiceOS](https://medium.com/@goldyfruit/from-mycroft-and-ansible-to-openvoiceos-making-open-voice-assistants-boring-066caae846d4) (consultadas 2026-09-10).
- **Conclusión de esta sección:** no aparece ningún "Jarvis open-source" maduro y comercialmente empaquetado en 2026 que combine agente + control de casa + hardware dedicado con éxito. El antecedente más parecido en intención (01 Light) fracasó como hardware y pivotó a software.

## 4. LLM local en hardware barato — benchmarks

*(pendiente de investigar)*

## 5. Precios Raspberry Pi 5 y mini PCs

*(pendiente de investigar)*

## 6. Pipeline de voz en español

*(pendiente de investigar)*

## 7. Costo de nube por usuario/mes

*(pendiente de investigar)*

## 8. Satélites de voz baratos (ESP32-S3)

*(pendiente de investigar)*

## 9. Casa inteligente

*(pendiente de investigar)*

## 10. BOM de 3 arquitecturas

*(pendiente de investigar)*

---

## Fuentes

*(lista acumulativa con URL + fecha de publicación + fecha de consulta)*
