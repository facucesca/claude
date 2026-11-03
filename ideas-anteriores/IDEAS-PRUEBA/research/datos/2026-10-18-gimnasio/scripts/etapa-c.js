export const meta = {
  name: 'gimnasio-etapa-c',
  description: 'Etapa C: programa de 30 días de lentes y etiquetado patrón×sector para la matriz (sin web), con control de uso',
  phases: [{ title: 'Control de uso' }, { title: 'Programa y matriz' }],
}
const S = args.scratch
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
const PROG = { type: 'object', properties: { dias: { type: 'array', minItems: 30, maxItems: 30, items: { type: 'object', properties: {
  dia: { type: 'number' }, lente: { type: 'string' }, libro: { type: 'string' }, donde_mirar: { type: 'string' }, ejercicio: { type: 'string' }, que_anotar: { type: 'string' }, pregunta: { type: 'string' },
}, required: ['dia', 'lente', 'libro', 'donde_mirar', 'ejercicio', 'que_anotar', 'pregunta'] } }, introduccion: { type: 'string' } }, required: ['dias', 'introduccion'] }
const TAGS = { type: 'object', properties: { etiquetas: { type: 'array', items: { type: 'object', properties: {
  id: { type: 'string' }, patrones: { type: 'array', minItems: 1, maxItems: 2, items: { type: 'string' } }, sector: { type: 'string' },
}, required: ['id', 'patrones', 'sector'] } } }, required: ['etiquetas'] }
const u = await uso('inicio')
if (!u || u.cinco_horas >= TOPE5H || u.semanal >= TOPESEM) return { motivo: `freno por uso: ${JSON.stringify(u)}` }
const [programa, tags] = await parallel([
  () => agent(`Trabajás para Facu (leé ${S}\\insumos\\contexto-facu.md y ${S}\\insumos\\bitacora-formato.md). Armá un PROGRAMA DE 30 DÍAS para entrenar el ojo de negocios con las lentes de sus libros. Material: ${S}\\salidas\\lentes-compactas.json (140 lentes de 10 libros: nombre, libro, qué mirar, pregunta generadora) y ${S}\\salidas\\lentes_maestras.json (las 12 que aparecen en 3 o más libros).
Reglas: un día = una lente (las 12 maestras tienen que estar, el resto elegí las más útiles y variadas, sin repetir libro dos días seguidos cuando se pueda). Cada día: dónde mirarla en la vida REAL de Facu (CEMEVA, la empresa de granos de su papá; la facultad de ingeniería industrial; su barrio; comercios donde compra; el transporte; su grupo de amigos; trámites; el campo; Mercado Libre), un ejercicio de 15-20 minutos concreto (observar, preguntar a alguien por la última vez que le pasó algo, contar una cola, anotar un parche casero, leer un ticket), qué anotar en la bitácora (formato de 5 líneas del archivo de bitácora) y la pregunta del día. Progresión: semana 1 mirar (parches, colas, desperdicios), semana 2 entender el trabajo y quién paga, semana 3 patrones e importación, semana 4 validar (Mom Test, monedas de compromiso, predicción y pérdida máxima) y el día 30 elegir 3 problemas para entrevistar. Introducción de 4-6 líneas. Nada inventado: no atribuyas a un libro algo que no esté en el material. Español rioplatense. Tu texto final NO lo lee un humano: devolvé solo el objeto estructurado.`, { label: 'programa-30-dias', phase: 'Programa y matriz', schema: PROG }),
  () => agent(`Tarea de clasificación, sin web. Archivo de entrada: ${S}\\salidas\\para-etiquetar.json, con tres listas: "patrones" (30 nombres de patrones de negocio), "sectores" (12 sectores) y "elementos" (ideas de negocio y empresas, cada una con id, título y una línea). Para CADA elemento devolvé: id (igual), patrones (1 o 2 nombres EXACTOS de la lista de patrones, el que mejor describe cómo hace plata y, si hay, uno secundario) y sector (1 nombre EXACTO de la lista de sectores). No inventes nombres fuera de las listas. Devolvé todos los elementos, sin saltear ninguno. Tu texto final NO lo lee un humano: devolvé solo el objeto estructurado.`, { label: 'etiquetar-matriz', phase: 'Programa y matriz', schema: TAGS }),
])
const fin = await uso('fin')
return { programa, tags, usos: [u, fin], motivo: 'completo' }
