export const meta = {
  name: 'gimnasio-etapa-a',
  description: 'Etapa A: verificar en Argentina las ideas restantes, re-verificar el contraste y rehacer 4 ángulos flojos, con control de uso entre tandas',
  phases: [{ title: 'Control de uso' }, { title: 'Verificar ideas' }, { title: 'Verificar contraste' }, { title: 'Generar 2.ª pasada' }, { title: 'Juzgar nuevas' }],
}
const S = args.scratch
const TANDA = args.tanda || 6
const TOPE5H = args.tope5h || 70
const TOPESEM = args.topeSemanal || 30
const RESPALDO = `Si WebSearch avisa que se agotó el cupo, respetá el límite: no lo esquives con otros buscadores ni feeds; seguí solo con WebFetch de páginas concretas que ya conozcas (sitios de empresas u organismos) y marcá como "no verificado" lo que no pudiste confirmar. Nunca intentes resolver un captcha.`
const AHORRO = `AHORRÁ TURNOS: mandá las búsquedas de varios elementos en paralelo en un mismo mensaje, nunca una por mensaje.`

const USO = { type: 'object', properties: { cinco_horas: { type: 'number' }, semanal: { type: 'number' } }, required: ['cinco_horas', 'semanal'] }
async function uso(tag) {
  for (let k = 0; k < 2; k++) {
    const r = await agent(`Tarea mecánica, sin nada más: cargá la herramienta con ToolSearch "select:mcp__ccd_session_mgmt__get_usage", llamala con session_id "self" y devolvé el percentUsed de la ventana "5-hour limit" como cinco_horas y el de "Weekly · all models" como semanal.`,
      { label: `uso:${tag}`, phase: 'Control de uso', schema: USO, model: 'haiku', effort: 'low' })
    if (r) return r
  }
  return null
}

const SCORE = { type: 'object', properties: { innovacion: { type: 'number' }, factibilidad_facu: { type: 'number' }, brecha_argentina: { type: 'number' }, por_que_ahora: { type: 'number' }, potencial: { type: 'number' } }, required: ['innovacion', 'factibilidad_facu', 'brecha_argentina', 'por_que_ahora', 'potencial'] }
const COMP = { type: 'array', items: { type: 'object', properties: { nombre: { type: 'string' }, url: { type: 'string' }, que_hace: { type: 'string' }, parecido: { type: 'string', enum: ['casi igual', 'parecido', 'solo una parte'] } }, required: ['nombre', 'url', 'que_hace', 'parecido'] } }
const EXISTE = { type: 'string', enum: ['existe y compite', 'existe parcial', 'no encontré nada', 'no verificado'] }

// ---------- verificación de ideas (mismo contrato que verificar2.js) ----------
const VSCHEMA = { type: 'object', properties: { lote: { type: 'string' }, verificaciones: { type: 'array', items: { type: 'object', properties: {
  id_tmp: { type: 'string' }, existe_en_argentina: EXISTE, competidores_argentina: COMP, intentos_previos: { type: 'string' }, evidencia_argentina: { type: 'string' }, evidencia_afuera: { type: 'string' },
  score_ajustado: SCORE, veredicto: { type: 'string', enum: ['mantener', 'bajar', 'descartar'] }, nota_para_facu: { type: 'string' }, busquedas_hechas: { type: 'number' }, fuentes: { type: 'array', items: { type: 'string' } },
}, required: ['id_tmp', 'existe_en_argentina', 'competidores_argentina', 'intentos_previos', 'evidencia_argentina', 'evidencia_afuera', 'score_ajustado', 'veredicto', 'nota_para_facu', 'busquedas_hechas', 'fuentes'] } } }, required: ['lote', 'verificaciones'] }
const vprompt = l => `Sos un verificador escéptico. Trabajás para Facu (leé ${S}\\insumos\\contexto-facu.md). Tu lote está en ${S}\\salidas\\${l}: un JSON con ideas; cada una trae lo que dijo el generador y la nota y los puntajes de un juez que NO tuvo búsqueda web.
OBJETIVO: averiguar si cada idea YA EXISTE EN ARGENTINA (o algo muy parecido para el mismo cliente) y si alguien lo intentó y cerró. En la primera pasada la idea mejor puntuada decía "no encontré nada" y una sola búsqueda encontró TuMango, una app argentina que ya renegocia facturas (iProfesional, 2026-09-07).
HERRAMIENTAS: ToolSearch "select:WebSearch,WebFetch". PRESUPUESTO por idea: hasta 3 búsquedas y 2 lecturas de página; apuntá a 2 búsquedas y 1 lectura. ${AHORRO} Buscá en español como buscaría un argentino (servicio genérico + "argentina", "app"/"plataforma"/"startup" + el problema, empresa de afuera + "argentina"). ${RESPALDO}
PARA CADA IDEA: existe_en_argentina ("existe y compite": alguien que opera en Argentina hace casi lo mismo para el mismo cliente; "existe parcial": alguien hace una parte; "no encontré nada": buscaste bien y no apareció, decí qué buscaste; "no verificado": no pudiste buscar). competidores_argentina con URL. intentos_previos (quién lo intentó y cerró o pivoteó, con fuente; vacío si nada). evidencia_argentina con búsquedas textuales y resultados. evidencia_afuera solo si algo figura "no verificado" o es dudoso (si no, "sin cambios"). score_ajustado partiendo del juez: si existe y compite, brecha ≤ 3 e innovación ≤ 5; si existe parcial, brecha ≤ 6; si no encontraste nada tras 2-3 búsquedas bien hechas, podés subir brecha hasta 8; no toques factibilidad ni potencial sin un dato nuevo. veredicto: "descartar" solo si existe casi igual y activo en Argentina; "bajar" si apareció competencia o un intento fallido; si no, "mantener". nota_para_facu de 2-4 líneas en rioplatense con el competidor o el hueco concreto. fuentes y busquedas_hechas.
Nada inventado. Fecha de consulta: 2026-10-19. Tu texto final NO lo lee un humano: devolvé solo el objeto estructurado.`

// ---------- verificación del contraste ----------
const CSCHEMA = { type: 'object', properties: { lote: { type: 'string' }, empresas: { type: 'array', items: { type: 'object', properties: {
  clave: { type: 'string' }, existe_en_argentina: EXISTE, competidores_argentina: COMP, detalle: { type: 'string', description: 'búsquedas hechas y qué salió, con URLs' },
  importabilidad_ajustada: { type: 'number' }, nota: { type: 'string', description: '1-3 líneas para Facu' }, busquedas_hechas: { type: 'number' },
}, required: ['clave', 'existe_en_argentina', 'competidores_argentina', 'detalle', 'importabilidad_ajustada', 'nota', 'busquedas_hechas'] } } }, required: ['lote', 'empresas'] }
const cprompt = l => `Sos un verificador escéptico. Trabajás para Facu (leé ${S}\\insumos\\contexto-facu.md). Tu lote está en ${S}\\salidas\\${l}: empresas exitosas de afuera; para cada una, otro agente dijo si existe algo equivalente en Argentina, muchas veces sin poder buscar ("no verificado").
OBJETIVO: confirmar con búsquedas reales si en Argentina existe algo equivalente (misma función para el mismo cliente), quién es y qué tan parecido. HERRAMIENTAS: ToolSearch "select:WebSearch,WebFetch". PRESUPUESTO: hasta 2 búsquedas y 1 lectura por empresa. ${AHORRO} Buscá el nombre de la empresa + "argentina", y la función en español + "argentina" ("app para ...", "plataforma de ..."). ${RESPALDO}
Para cada empresa: clave (copiá la del archivo), existe_en_argentina, competidores_argentina con URL, detalle (búsquedas textuales y resultados), importabilidad_ajustada 1-10 (bajala si hay jugador local fuerte, subila si confirmaste que no hay nada y el modelo encaja con Facu), nota de 1-3 líneas en rioplatense. Nada inventado. Fecha de consulta: 2026-10-19. Tu texto final NO lo lee un humano: devolvé solo el objeto estructurado.`

// ---------- segunda pasada de 4 ángulos ----------
const GSCHEMA = { type: 'object', properties: { angulo: { type: 'string' }, ideas: { type: 'array', minItems: 6, maxItems: 10, items: { type: 'object', properties: {
  titulo: { type: 'string' }, una_linea: { type: 'string' }, problema: { type: 'string' }, cliente_que_paga: { type: 'string' }, modelo_de_cobro: { type: 'string' },
  vuelta_de_tuerca: { type: 'string' }, componentes_que_combina: { type: 'array', items: { type: 'string' } }, por_que_ahora: { type: 'string' }, que_hace_la_ia: { type: 'string' },
  existe_afuera: { type: 'array', items: { type: 'object', properties: { empresa: { type: 'string' }, pais: { type: 'string' }, dato: { type: 'string' }, fuente: { type: 'string' } }, required: ['empresa', 'pais', 'dato', 'fuente'] } },
  existe_en_argentina: EXISTE, competidores_argentina: COMP, detalle_argentina: { type: 'string' }, huevo_gallina: { type: 'string' },
  palancas_para_retorcerla: { type: 'array', minItems: 3, maxItems: 3, items: { type: 'string' } }, patron: { type: 'string' }, lente: { type: 'string' }, riesgos: { type: 'string' },
  primer_experimento_barato: { type: 'string' }, score: SCORE, referencia_registro: { type: 'string' }, chequeo_registro: { type: 'string' },
}, required: ['titulo', 'una_linea', 'problema', 'cliente_que_paga', 'modelo_de_cobro', 'vuelta_de_tuerca', 'componentes_que_combina', 'por_que_ahora', 'que_hace_la_ia', 'existe_afuera', 'existe_en_argentina', 'competidores_argentina', 'detalle_argentina', 'huevo_gallina', 'palancas_para_retorcerla', 'patron', 'lente', 'riesgos', 'primer_experimento_barato', 'score', 'referencia_registro', 'chequeo_registro'] } },
  descartadas_por_repetidas: { type: 'array', items: { type: 'string' } } }, required: ['angulo', 'ideas', 'descartadas_por_repetidas'] }
const ANGULOS = [
  { key: 'oficios-2', motivo: 'en la primera pasada de OFICIOS sobrevivieron 2 de 12: el resto repetía el registro (club de compras de oficios, cuotas para la reparación, el plomero viene al edificio el jueves) o se duplicaba', foco: 'la capa que falta alrededor de los oficios en Argentina, sin repetir el "Uber de oficios" (Zolvers, HomeSolution, Timbrit ya existen): por ejemplo la formación corta con colocación garantizada, el seguro por trabajo, la garantía de obra que se transfiere con la casa, los materiales que llegan al pie de obra a la hora justa, el diagnóstico en vivo por video, el mantenimiento de PyMEs con varios oficios bajo un abono, los oficios para segmentos que hoy desconfían (mujeres que viven solas, adultos mayores), y los oficios rurales. Verificá cada una contra el índice y el registro antes de proponerla.' },
  { key: 'importar-2', motivo: 'en la primera pasada de IMPORTAR (YC, a16z) sobrevivieron 3 de 12: casi todas eran la misma idea que otro ángulo o repetían el registro', foco: 'buscá en la web lanzamientos de 2025-2026 de Y Combinator (lotes 2025 y 2026), Product Hunt, la lista Marketplace 100 de a16z y fondos de LatAm (Kaszek, Monashees), y elegí modelos de intermediación o de paquete integrado con tracción verificable que NO estén en el índice ni en el registro. Para cada uno: la fuente del original, si existe en Argentina (buscalo) y la versión argentina con una vuelta real, no una copia.' },
  { key: 'tendencias-2', motivo: 'en la primera pasada de TENDENCIAS 2026 sobrevivieron 3 de 11: varias eran crypto o pagos ya investigados, o repetían el registro', foco: 'cambios de 2025-2026 en Argentina y en tecnología, cada uno con fuente (norma, organismo o nota): por ejemplo el fin del cepo para personas, el régimen de courier y las importaciones, el QR interoperable y las transferencias 3.0, el crédito hipotecario, las billeteras y open finance, la desregulación de profesiones y actividades, los modelos de voz en español rioplatense, los agentes que usan la computadora y el comercio agéntico. Proponé solo plataformas web que sean posibles RECIÉN ahora gracias a ese cambio. Nada de crypto, x402 ni bots de trading.' },
  { key: 'un-jugador-2', motivo: 'en la primera pasada de MODO UN SOLO JUGADOR sobrevivieron 4 de 12: muchas eran la misma idea que otro ángulo (cocinas por hora, techos solares, drones, lanchas, sobrantes industriales, piezas de chapa)', foco: 'herramientas web gratis o baratas con Claude que un solo lado usa solo (cotizador, calculadora, generador de documentos, verificador, organizador) en pares de dos lados que hoy no tienen plataforma en Argentina, y que después encienden un marketplace. Elegí lados distintos a los del índice. En cada una, decí cuál es la herramienta de un jugador y en qué momento se prende el segundo lado.' },
]
const gprompt = a => `Trabajás para Facu (leé ${S}\\insumos\\contexto-facu.md). SEGUNDA PASADA de un ángulo que rindió poco: ${a.motivo}.
ANTES DE GENERAR: leé COMPLETO ${S}\\salidas\\indice-titulos.txt (las 191 ideas generadas el 2026-10-18 con su ángulo) y, para cada idea candidata, hacé grep de 2-3 palabras clave en ${S}\\insumos\\exclusion-registro.tsv (1.402 ideas anteriores con la decisión de Facu). No propongas nada que ya esté en ninguno de los dos (mismo problema y mismo cliente), ni algo parecido a una fila con decisión NO, DESCARTADA o SALIO-parecida-a-NO. Variante de una ELEGIDA: vale solo con una vuelta clara, marcando el id en referencia_registro.
FOCO: ${a.foco}
VERIFICACIÓN: ToolSearch "select:WebSearch,WebFetch". Para cada idea, hasta 2 búsquedas para ver si ya existe en Argentina y quién (completá existe_en_argentina y competidores_argentina con URL), y lo necesario para fundar el "por qué ahora" (máximo 6 búsquedas en total para eso). ${AHORRO} ${RESPALDO}
Las ideas tienen que poder lanzarse como página web o plataforma, con Claude y automatizaciones haciendo una parte central; vuelta de tuerca explícita, no lo obvio. Nada inventado: cada empresa o cifra con URL; si no la verificaste, "no verificado". Puntajes 1-10 con criterio duro (innovación, factibilidad para Facu, brecha en Argentina, por qué ahora, potencial). Devolvé entre 6 y 10 ideas: mejor 6 buenas que 10 flojas. Fecha de consulta: 2026-10-19. Español rioplatense. Tu texto final NO lo lee un humano: devolvé solo el objeto estructurado.`

const JSCHEMA = { type: 'object', properties: { juicios: { type: 'array', items: { type: 'object', properties: {
  id_tmp: { type: 'string' }, estado_registro: { type: 'string', enum: ['nueva', 'parecida', 'repetida'] },
  parecidas_confirmadas: { type: 'array', items: { type: 'object', properties: { id: { type: 'string' }, nombre: { type: 'string' }, decision: { type: 'string' }, relacion: { type: 'string' } }, required: ['id', 'nombre', 'decision', 'relacion'] } },
  duplicada_de: { type: 'string' }, veredicto: { type: 'string', enum: ['mantener', 'bajar', 'descartar'] }, score_ajustado: SCORE, nota_para_facu: { type: 'string' },
}, required: ['id_tmp', 'estado_registro', 'parecidas_confirmadas', 'duplicada_de', 'veredicto', 'score_ajustado', 'nota_para_facu'] } } }, required: ['juicios'] }

// ---------- orquestación con control de uso ----------
const tareas = [
  ...args.vlotes.map(l => ({ tipo: 'verif', id: l })),
  ...args.clotes.map(l => ({ tipo: 'contraste', id: l })),
  ...(args.sinGen ? [] : ANGULOS.map(a => ({ tipo: 'gen', id: a.key, a }))),
]
const usos = []; const res = { verif: [], contraste: [], gen: [] }; const fallidos = []; const intentos = {}
let pendientes = [...tareas]; let motivo = 'completo'
function correr(t) {
  if (t.tipo === 'verif') return agent(vprompt(t.id), { label: `verif:${t.id}`, phase: 'Verificar ideas', schema: VSCHEMA })
  if (t.tipo === 'contraste') return agent(cprompt(t.id), { label: `contraste:${t.id}`, phase: 'Verificar contraste', schema: CSCHEMA })
  return agent(gprompt(t.a), { label: `gen:${t.id}`, phase: 'Generar 2.ª pasada', schema: GSCHEMA })
}
while (pendientes.length) {
  const u = await uso(`tanda-${usos.length + 1}`)
  usos.push({ momento: `antes de la tanda ${usos.length + 1}`, ...(u || { error: 'sin lectura' }) })
  if (!u) { motivo = 'no se pudo leer el uso: freno por seguridad'; break }
  if (u.cinco_horas >= TOPE5H || u.semanal >= TOPESEM) { motivo = `tope alcanzado (5 h: ${u.cinco_horas}%, semanal: ${u.semanal}%)`; break }
  const tanda = pendientes.slice(0, TANDA); pendientes = pendientes.slice(TANDA)
  log(`tanda ${usos.length}: ${tanda.map(t => t.id).join(', ')} · 5 h ${u.cinco_horas}% · semanal ${u.semanal}%`)
  const out = await parallel(tanda.map(t => () => correr(t)))
  out.forEach((r, k) => {
    const t = tanda[k]
    if (r) { res[t.tipo].push(t.tipo === 'gen' ? { key: t.id, ...r } : r); return }
    intentos[t.id] = (intentos[t.id] || 0) + 1
    if (intentos[t.id] < 2) pendientes.push(t); else fallidos.push(t.id)
  })
}
// juez de las nuevas (sin web)
let juicios = null
const compact = []
res.gen.forEach((g, gi) => (g.ideas || []).forEach((i, k) => compact.push({ id_tmp: `P${gi + 1}-${k + 1}`, angulo: g.key, titulo: i.titulo, una_linea: i.una_linea, problema: i.problema, cliente_que_paga: i.cliente_que_paga, existe_en_argentina: i.existe_en_argentina, competidores: (i.competidores_argentina || []).map(c => c.nombre).join(', '), score: i.score, referencia_registro: i.referencia_registro })))
if (compact.length && motivo === 'completo') {
  const u = await uso('juez'); usos.push({ momento: 'antes del juez', ...(u || { error: 'sin lectura' }) })
  if (u && u.cinco_horas < TOPE5H && u.semanal < TOPESEM) {
    juicios = await agent(`Sos un juez escéptico. Trabajás para Facu (leé ${S}\\insumos\\contexto-facu.md). Abajo van ${compact.length} ideas NUEVAS de una segunda pasada (JSON). Compará cada una contra (a) el índice de las 191 ideas anteriores de esta investigación en ${S}\\salidas\\indice-titulos.txt (leelo completo) y (b) el registro de 1.402 ideas en ${S}\\insumos\\exclusion-registro.tsv (grep de palabras clave por idea). NO uses búsqueda web.
Para cada idea: estado_registro "repetida" si es el mismo problema para el mismo cliente que una fila del registro, o parecida a una fila con decisión NO, DESCARTADA o SALIO-parecida-a-NO (regla de Facu: "no quiero volver a rechazar"; ante la duda, repetida); "parecida" si comparte cliente o problema vecino con una ELEGIDA pero trae una vuelta clara; si no, "nueva". duplicada_de: si es la misma que una del índice (poné su id, por ejemplo N036) o que otra nueva (su id_tmp). score_ajustado: corregí lo inflado (si existe y compite en Argentina, brecha ≤ 3 e innovación ≤ 5; si hace falta hardware caro, licencia financiera o capital de trabajo, factibilidad ≤ 4; potencial 9-10 solo si escala fuera de Argentina). veredicto: descartar si es repetida, duplicada o inviable; bajar si los puntajes bajaron más de 2 puntos en promedio; si no, mantener. nota_para_facu de 2-4 líneas en rioplatense.
Nada inventado. Tu texto final NO lo lee un humano: devolvé solo el objeto estructurado.

IDEAS NUEVAS:
${JSON.stringify(compact)}`, { label: 'juez:nuevas', phase: 'Juzgar nuevas', schema: JSCHEMA })
  }
}
const fin = await uso('fin'); usos.push({ momento: 'final', ...(fin || { error: 'sin lectura' }) })
log(`ideas verificadas: ${res.verif.length} lotes · contraste: ${res.contraste.length} lotes · generadores: ${res.gen.length} · pendientes: ${pendientes.length} · ${motivo}`)
return { verif: res.verif, contraste: res.contraste, gen: res.gen, compact, juicios, pendientes: pendientes.map(t => t.id), fallidos, motivo, usos }
