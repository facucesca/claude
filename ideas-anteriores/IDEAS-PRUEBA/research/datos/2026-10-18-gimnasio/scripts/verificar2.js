export const meta = {
  name: 'verificar-ideas-argentina',
  description: 'Verifica en la web si cada idea ya existe en Argentina, por tandas, con control de uso entre tandas',
  phases: [{ title: 'Control de uso', detail: 'chequeo barato antes de cada tanda' }, { title: 'Verificar', detail: 'un agente por lote de 5 ideas' }],
}
const S = args.scratch
const LOTES = args.lotes
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

const SCHEMA = { type: 'object', properties: {
  lote: { type: 'string' },
  verificaciones: { type: 'array', items: { type: 'object', properties: {
    id_tmp: { type: 'string' },
    existe_en_argentina: { type: 'string', enum: ['existe y compite', 'existe parcial', 'no encontré nada', 'no verificado'] },
    competidores_argentina: { type: 'array', items: { type: 'object', properties: { nombre: { type: 'string' }, url: { type: 'string' }, que_hace: { type: 'string' }, parecido: { type: 'string', enum: ['casi igual', 'parecido', 'solo una parte'] } }, required: ['nombre', 'url', 'que_hace', 'parecido'] } },
    intentos_previos: { type: 'string', description: 'quién lo intentó en Argentina o LatAm y cerró o pivoteó, cuándo y por qué, con fuente; vacío si no encontraste' },
    evidencia_argentina: { type: 'string', description: 'búsquedas hechas (textuales) y qué salió' },
    evidencia_afuera: { type: 'string', description: 'correcciones a lo dicho de empresas de afuera, o "sin cambios"' },
    score_ajustado: { type: 'object', properties: { innovacion: { type: 'number' }, factibilidad_facu: { type: 'number' }, brecha_argentina: { type: 'number' }, por_que_ahora: { type: 'number' }, potencial: { type: 'number' } }, required: ['innovacion', 'factibilidad_facu', 'brecha_argentina', 'por_que_ahora', 'potencial'] },
    veredicto: { type: 'string', enum: ['mantener', 'bajar', 'descartar'] },
    nota_para_facu: { type: 'string' },
    busquedas_hechas: { type: 'number' },
    fuentes: { type: 'array', items: { type: 'string' } },
  }, required: ['id_tmp', 'existe_en_argentina', 'competidores_argentina', 'intentos_previos', 'evidencia_argentina', 'evidencia_afuera', 'score_ajustado', 'veredicto', 'nota_para_facu', 'busquedas_hechas', 'fuentes'] } },
}, required: ['lote', 'verificaciones'] }

const prompt = l => `Sos un verificador escéptico. Trabajás para Facu (leé ${S}\\insumos\\contexto-facu.md). Tu lote está en ${S}\\salidas\\${l}: un JSON con ideas; cada una trae lo que dijo el generador y la nota y los puntajes de un juez que NO tuvo búsqueda web.
OBJETIVO: averiguar si cada idea YA EXISTE EN ARGENTINA (o algo muy parecido para el mismo cliente) y si alguien lo intentó y cerró. Es la debilidad número uno del trabajo anterior: la idea mejor puntuada decía "no encontré nada" y una sola búsqueda encontró TuMango, una app argentina que ya renegocia facturas de internet y celular (iProfesional, 2026-09-07).
HERRAMIENTAS: cargá con ToolSearch "select:WebSearch,WebFetch". PRESUPUESTO por idea: hasta 3 búsquedas y hasta 2 lecturas de página; apuntá a 2 búsquedas y 1 lectura en promedio. AHORRÁ TURNOS: mandá las búsquedas de varias ideas en paralelo en un mismo mensaje (por ejemplo, la primera búsqueda de todas las ideas juntas), nunca una por mensaje.
CÓMO BUSCAR: en español y como buscaría un argentino: nombre genérico del servicio + "argentina", "app"/"plataforma"/"startup" + el problema, y el nombre de la empresa de afuera + "argentina". Si WebSearch falla o dice que se agotó el cupo, usá como respaldo WebFetch sobre el feed público de Google Noticias: https://news.google.com/rss/search?q=PALABRAS+UNIDAS+CON+MAS&hl=es-419&gl=AR&ceid=AR:es-419 . No uses otros buscadores por WebFetch (piden captcha) y nunca intentes resolver un captcha.
PARA CADA IDEA devolvé:
- existe_en_argentina: "existe y compite" (alguien que opera en Argentina hace casi lo mismo para el mismo cliente), "existe parcial" (alguien hace una parte), "no encontré nada" (buscaste bien y no apareció; decí qué buscaste) o "no verificado" (no pudiste buscar).
- competidores_argentina con nombre, URL, qué hace y qué tan parecido; intentos_previos si alguien lo intentó y cerró o pivoteó (con fuente).
- evidencia_argentina con las búsquedas textuales y qué salió; evidencia_afuera solo si algo del generador figura "no verificado" o te parece dudoso (si no, "sin cambios": no gastes búsquedas en lo que ya tiene fuente).
- score_ajustado 1-10, partiendo del juez: si existe y compite, brecha_argentina ≤ 3 e innovacion ≤ 5; si existe parcial, brecha ≤ 6; si no encontraste nada después de 2-3 búsquedas bien hechas, podés subir brecha hasta 8. No toques factibilidad ni potencial salvo con un dato nuevo (decilo en la nota).
- veredicto: "descartar" solo si existe en Argentina casi igual y activo; "bajar" si apareció competencia o un intento fallido; "mantener" si no.
- nota_para_facu: 2-4 líneas en español rioplatense, con el competidor o el hueco concreto. fuentes: todas las URLs usadas. busquedas_hechas: cuántas búsquedas hiciste en total para esa idea.
Nada inventado: si no lo viste en una fuente, no lo afirmes. Fecha de consulta: 2026-10-19. Tu texto final NO lo lee un humano: devolvé solo el objeto estructurado.`

const usos = []; const hechos = []; const fallidos = []; const intentos = {}
let pendientes = [...LOTES]; let motivo = 'completo'
while (pendientes.length) {
  const u = await uso(`antes-${hechos.length}`)
  usos.push({ momento: `antes de la tanda ${usos.length + 1}`, ...(u || { error: 'sin lectura' }) })
  if (!u) { motivo = 'no se pudo leer el uso: freno por seguridad'; break }
  if (u.cinco_horas >= TOPE5H || u.semanal >= TOPESEM) { motivo = `tope alcanzado (5 h: ${u.cinco_horas}%, semanal: ${u.semanal}%)`; break }
  const tanda = pendientes.slice(0, TANDA); pendientes = pendientes.slice(TANDA)
  log(`tanda de ${tanda.length} lotes · uso 5 h ${u.cinco_horas}% · semanal ${u.semanal}%`)
  const res = await parallel(tanda.map(l => () => agent(prompt(l), { label: `verif:${l}`, phase: 'Verificar', schema: SCHEMA })))
  res.forEach((r, k) => {
    const l = tanda[k]
    if (r) { hechos.push(r); return }
    intentos[l] = (intentos[l] || 0) + 1
    if (intentos[l] < 2) pendientes.push(l); else fallidos.push(l)
  })
}
const fin = await uso('fin')
usos.push({ momento: 'final', ...(fin || { error: 'sin lectura' }) })
log(`${hechos.length} lotes verificados · pendientes: ${pendientes.length} · ${motivo}`)
return { lotes: hechos, pendientes, fallidos, motivo, usos }
