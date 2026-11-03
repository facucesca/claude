export const meta = {
  name: 'juez-ideas-gimnasio',
  description: 'Jueces por lote: repetidas contra el registro, duplicadas entre sí, puntajes inflados, nota honesta para Facu (sin web)',
  phases: [{ title: 'Juzgar', detail: 'un agente por lote' }],
}
const S = args.scratch
const LOTES = args.lotes
const SCHEMA = { type: 'object', properties: {
  lote: { type: 'string' },
  juicios: { type: 'array', items: { type: 'object', properties: {
    id_tmp: { type: 'string' },
    estado_registro: { type: 'string', enum: ['nueva', 'parecida', 'repetida'] },
    parecidas_confirmadas: { type: 'array', items: { type: 'object', properties: { id: { type: 'string' }, nombre: { type: 'string' }, decision: { type: 'string' }, relacion: { type: 'string' } }, required: ['id','nombre','decision','relacion'] } },
    duplicada_de: { type: 'string', description: 'id_tmp de otra idea del mismo lote o de sospechas_internas que es la misma; vacío si no' },
    veredicto: { type: 'string', enum: ['mantener', 'bajar', 'descartar'] },
    score_ajustado: { type: 'object', properties: { innovacion: { type: 'number' }, factibilidad_facu: { type: 'number' }, brecha_argentina: { type: 'number' }, por_que_ahora: { type: 'number' }, potencial: { type: 'number' } }, required: ['innovacion','factibilidad_facu','brecha_argentina','por_que_ahora','potencial'] },
    nota_para_facu: { type: 'string', description: '2-4 líneas honestas: lo más importante antes de enamorarse; incluir si la existencia en Argentina quedó sin verificar' },
  }, required: ['id_tmp','estado_registro','parecidas_confirmadas','duplicada_de','veredicto','score_ajustado','nota_para_facu'] } },
}, required: ['lote','juicios'] }

phase('Juzgar')
const out = await Promise.all(LOTES.map(l => agent(
`Sos un juez escéptico. Trabajás para Facu (leé ${S}\\insumos\\contexto-facu.md). Tu lote está en ${S}\\salidas\\${l} (JSON con ideas; cada una trae sospechas_registro = filas parecidas del registro de 1.402 ideas anteriores con la decisión de Facu, y sospechas_internas = otras ideas nuevas parecidas). El índice de TODAS las ideas nuevas (id, ángulo, título, una línea) está en ${S}\salidas\indice-titulos.txt: leelo completo primero, porque varias ideas se repiten entre ángulos (por ejemplo cocinas habilitadas por hora, techos para paneles solares, uniformes como servicio, lanchas paradas) y tenés que marcar duplicada_de con el id_tmp de la mejor versión aunque esté en otro lote (regla: sobrevive la de id_tmp más bajo salvo que otra sea claramente más completa; si la tuya es la que sobrevive, dejá duplicada_de vacío). NO uses búsqueda web (el cupo está agotado): juzgá con lo que hay en el archivo y con el registro completo en ${S}\\insumos\\exclusion-registro.tsv (podés hacer grep de palabras clave para cada idea).
Para CADA idea del lote:
1) estado_registro: "repetida" si es el MISMO problema para el MISMO tipo de cliente que una fila del registro (aunque antes estuviera planteada distinto, por ejemplo como servicio), o si es parecida a una fila con decisión NO / DESCARTADA / SALIO-parecida-a-NO. "parecida" si comparte cliente o problema vecino con una fila ELEGIDA pero trae una vuelta nueva clara (anotá la fila en parecidas_confirmadas con la relación). "nueva" si no hay nada igual. Regla de Facu: "no quiero volver a rechazar", así que ante duda entre parecida-a-NO y nueva, es repetida.
2) duplicada_de: si dos ideas nuevas son la misma, dejá viva la mejor (más completa, mejor puntuada) y marcá la otra con su id_tmp.
3) score_ajustado: corregí puntajes inflados. Si existe_en_argentina dice "existe y compite", brecha_argentina ≤ 3 e innovación ≤ 5. Si dice "no verificado", brecha_argentina ≤ 6. Si requiere hardware caro, licencias financieras, capital de trabajo o custodia de fondos, factibilidad_facu ≤ 4. Sé duro con potencial: 9-10 solo si el mercado es claramente grande y la plataforma puede escalar fuera de Argentina.
4) veredicto: descartar si es repetida, duplicada o inviable; bajar si los puntajes bajaron más de 2 puntos en promedio; si no, mantener.
5) nota_para_facu: 2-4 líneas en español rioplatense con lo que más le sirve saber, incluyendo si la ausencia en Argentina quedó sin verificar (los generadores tuvieron cupo de búsqueda limitado el 2026-10-18).
Nada inventado: no agregues empresas ni cifras que no estén en el archivo o en el registro. Tu texto final NO lo lee un humano: devolvé solo el objeto estructurado.`,
  { label: `juez:${l}`, phase: 'Juzgar', schema: SCHEMA, model: 'opus' }
)))
const ok = out.filter(Boolean)
log(`${ok.length}/${LOTES.length} lotes juzgados · ${ok.reduce((n, r) => n + r.juicios.length, 0)} ideas`)
return { lotes: ok, faltaron: LOTES.filter((l, i) => !out[i]) }
