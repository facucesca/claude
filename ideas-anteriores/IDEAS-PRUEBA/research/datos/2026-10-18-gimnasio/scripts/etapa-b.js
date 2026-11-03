export const meta = {
  name: 'gimnasio-etapa-b',
  description: 'Etapa B: fichas a fondo de las mejores ideas (quién lo intentó, regulación, números, entrevistas, experimento), con control de uso',
  phases: [{ title: 'Control de uso' }, { title: 'Fichas a fondo' }],
}
const S = args.scratch
const TANDA = args.tanda || 6
const TOPE5H = args.tope5h || 70
const TOPESEM = args.topeSemanal || 30
const USO = { type: 'object', properties: { cinco_horas: { type: 'number' }, semanal: { type: 'number' } }, required: ['cinco_horas', 'semanal'] }
async function uso(tag) {
  for (let k = 0; k < 2; k++) {
    const r = await agent(`Tarea mecánica, sin nada más: cargá la herramienta con ToolSearch "select:mcp__ccd_session_mgmt__get_usage", llamala con session_id "self" y devolvé el percentUsed de la ventana "5-hour limit" como cinco_horas y el de "Weekly · all models" como semanal.`,
      { label: `uso:${tag}`, phase: 'Control de uso', schema: USO, model: 'haiku', effort: 'low' })
    if (r) return r
  }
  return null
}
const FICHA = { type: 'object', properties: {
  id_tmp: { type: 'string' }, titulo: { type: 'string' },
  resumen: { type: 'string', description: '5 líneas: qué es, para quién, quién paga, la vuelta de tuerca y por qué ahora' },
  quien_lo_intento: { type: 'string', description: 'quién lo intentó en Argentina o LatAm, qué pasó y por qué (con fuente); si no apareció nadie, qué buscaste' },
  competencia_argentina: { type: 'string', description: 'quién existe hoy, qué cobra si es público, qué hace bien y qué hueco deja, con URLs' },
  regulacion: { type: 'string', description: 'normas que aplican, leídas en la fuente (InfoLEG, Boletín Oficial, organismo), con URL; qué permite y qué prohíbe; "no aplica" si no hay' },
  numeros_unidad: { type: 'string', description: 'ticket, comisión o abono, costos por operación (IA, WhatsApp, cobro con Mercado Pago u otro, con fuente de las tarifas) y margen por operación; todo lo que sea estimación, marcado como tal con el razonamiento' },
  tamano_mercado: { type: 'string', description: 'cuántos clientes potenciales hay en Argentina y en la primera ciudad, con fuente (INDEC, cámaras, organismos); si no hay dato, decirlo' },
  a_quien_entrevistar: { type: 'string', description: '3-5 perfiles concretos y dónde encontrarlos (lugares, grupos, cámaras, ferias, foros)' },
  guion_entrevista: { type: 'array', minItems: 8, maxItems: 10, items: { type: 'string' }, description: 'preguntas estilo Mom Test: sobre lo que pasó la última vez, lo que gastó y lo que hace hoy; nada de "¿usarías...?"' },
  experimento: { type: 'object', properties: { hipotesis: { type: 'string' }, prediccion: { type: 'string', description: 'número concreto que esperás ver' }, perdida_maxima: { type: 'string', description: 'en USD, menos de 200' }, duracion: { type: 'string' }, pasos: { type: 'array', items: { type: 'string' } }, criterio_sigue: { type: 'string' }, criterio_corta: { type: 'string' } }, required: ['hipotesis', 'prediccion', 'perdida_maxima', 'duracion', 'pasos', 'criterio_sigue', 'criterio_corta'] },
  variantes: { type: 'array', minItems: 5, maxItems: 5, items: { type: 'string' }, description: '5 formas de retorcerla: otro cliente, otro cobro, otro país, otro activo, sacar o poner un humano' },
  riesgos: { type: 'array', items: { type: 'string' } },
  veredicto: { type: 'string', description: '2-3 líneas: vale la pena probarla, probarla solo si..., o no; y por qué' },
  fuentes: { type: 'array', items: { type: 'string' } },
}, required: ['id_tmp', 'titulo', 'resumen', 'quien_lo_intento', 'competencia_argentina', 'regulacion', 'numeros_unidad', 'tamano_mercado', 'a_quien_entrevistar', 'guion_entrevista', 'experimento', 'variantes', 'riesgos', 'veredicto', 'fuentes'] }
const prompt = id => `Sos un investigador de negocios escéptico y práctico. Trabajás para Facu (leé ${S}\\insumos\\contexto-facu.md). Tu idea está en ${S}\\salidas\\ficha-${id}.json: la ficha completa con lo que dijo el generador, el juez y el verificador web.
OBJETIVO: convertirla en una FICHA A FONDO que Facu pueda usar para decidir si la prueba y cómo, en dos semanas y con menos de USD 200. No repitas lo que ya dice la ficha: profundizá donde está flojo.
HERRAMIENTAS: ToolSearch "select:WebSearch,WebFetch". PRESUPUESTO: hasta 8 búsquedas y 5 lecturas de página en total. Mandá varias búsquedas en paralelo en un mismo mensaje. Si WebSearch avisa que se agotó el cupo, respetá el límite: no lo esquives con otros buscadores ni feeds; seguí solo con WebFetch de páginas concretas que ya conozcas (las fuentes de la ficha, sitios de empresas u organismos) y marcá como "no verificado" lo que no pudiste confirmar. Nunca intentes resolver un captcha.
PRIORIDADES (en este orden): 1) quién lo intentó en Argentina o LatAm y qué le pasó (cierres, pivotes, notas de prensa); 2) la competencia argentina de hoy, con precios si son públicos; 3) la regulación leída en la fuente, si la idea depende de una norma; 4) números de unidad y tamaño de mercado con fuente; 5) entrevistas y experimento.
EL EXPERIMENTO: tiene que medir lo que la gente HACE (seña, pre-compra, contrato firmado, tiempo cedido), no lo que dice. Escribí la predicción en números ANTES de correrlo (Ries), la pérdida máxima (Hvidkjaer) y los criterios de seguir o cortar. Pensalo para alguien de 22 años, sin programar, con Claude y no-code, que no quiere mostrar la cara en redes.
Nada inventado: toda cifra con URL; las estimaciones propias, marcadas como "estimación" con el razonamiento. Español rioplatense, claro. Fecha de consulta: 2026-10-19. Tu texto final NO lo lee un humano: devolvé solo el objeto estructurado.`
const usos = []; const fichas = []; const fallidos = []; const intentos = {}
let pendientes = [...args.ideas]; let motivo = 'completo'
while (pendientes.length) {
  const u = await uso(`tanda-${usos.length + 1}`)
  usos.push({ momento: `antes de la tanda ${usos.length + 1}`, ...(u || { error: 'sin lectura' }) })
  if (!u) { motivo = 'no se pudo leer el uso: freno por seguridad'; break }
  if (u.cinco_horas >= TOPE5H || u.semanal >= TOPESEM) { motivo = `tope alcanzado (5 h: ${u.cinco_horas}%, semanal: ${u.semanal}%)`; break }
  const tanda = pendientes.slice(0, TANDA); pendientes = pendientes.slice(TANDA)
  log(`tanda ${usos.length}: ${tanda.join(', ')} · 5 h ${u.cinco_horas}% · semanal ${u.semanal}%`)
  const out = await parallel(tanda.map(id => () => agent(prompt(id), { label: `ficha:${id}`, phase: 'Fichas a fondo', schema: FICHA })))
  out.forEach((r, k) => {
    const id = tanda[k]
    if (r) { fichas.push(r); return }
    intentos[id] = (intentos[id] || 0) + 1
    if (intentos[id] < 2) pendientes.push(id); else fallidos.push(id)
  })
}
const fin = await uso('fin'); usos.push({ momento: 'final', ...(fin || { error: 'sin lectura' }) })
log(`${fichas.length} fichas · pendientes ${pendientes.length} · ${motivo}`)
return { fichas, pendientes, fallidos, motivo, usos }
