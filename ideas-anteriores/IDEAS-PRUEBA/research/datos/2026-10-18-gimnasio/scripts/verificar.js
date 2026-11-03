export const meta = {
  name: 'verificar-ideas-gimnasio',
  description: 'Verificadores adversariales por lote: ¿existe en Argentina?, ¿existe afuera?, ¿es repetida?, puntajes ajustados',
  phases: [{ title: 'Verificar', detail: 'un agente por lote de ideas' }],
}
const S = args.scratch
const LOTES = args.lotes
const SCHEMA = { type: 'object', properties: {
  lote: { type: 'string' },
  verificaciones: { type: 'array', items: { type: 'object', properties: {
    id_tmp: { type: 'string' },
    veredicto: { type: 'string', enum: ['mantener', 'bajar', 'descartar'] },
    existe_en_argentina: { type: 'string', enum: ['no encontré nada', 'existe parcial', 'existe y compite', 'no verificado'] },
    evidencia_argentina: { type: 'string', description: 'qué buscaste (términos) y qué encontraste, con URLs y fecha 2026-10-18' },
    evidencia_afuera: { type: 'string', description: 'confirmación o corrección de las empresas citadas, con URLs' },
    es_repetida_del_registro: { type: 'string', description: 'id del registro si es el mismo problema y mismo cliente; vacío si no' },
    score_ajustado: { type: 'object', properties: { innovacion: { type: 'number' }, factibilidad_facu: { type: 'number' }, brecha_argentina: { type: 'number' }, por_que_ahora: { type: 'number' }, potencial: { type: 'number' } }, required: ['innovacion','factibilidad_facu','brecha_argentina','por_que_ahora','potencial'] },
    nota_para_facu: { type: 'string', description: '2-4 líneas: lo más importante que tiene que saber antes de enamorarse de esta idea' },
  }, required: ['id_tmp','veredicto','existe_en_argentina','evidencia_argentina','evidencia_afuera','es_repetida_del_registro','score_ajustado','nota_para_facu'] } },
}, required: ['lote','verificaciones'] }

phase('Verificar')
const out = await Promise.all(LOTES.map(l => agent(
`Sos un verificador escéptico e independiente. Trabajás para Facu (leé ${S}\\insumos\\contexto-facu.md). Tu lote de ideas está en ${S}\\salidas\\${l} (JSON). Para CADA idea del lote:
1) Intentá REFUTAR que "no existe en Argentina": buscá con WebSearch (cargalo con ToolSearch "select:WebSearch,WebFetch") al menos 2 consultas distintas en español (nombre genérico + "argentina", "app"/"plataforma" + el problema, Mercado Libre, startups argentinas). Reportá términos, resultados y URLs. Si existe, decí quién y qué tan parecido.
2) Confirmá o corregí las empresas citadas en existe_afuera (una búsqueda por empresa; si una cifra no se confirma, marcala "no verificado").
3) Mirá el campo sospechas_registro (ideas anteriores parecidas, con su decisión) y decidí si es la MISMA idea (mismo problema + mismo cliente) → es_repetida_del_registro = id. Parecida pero distinta → vacío y mencionalo en la nota.
4) Ajustá los 5 puntajes (1-10) con criterio propio: bajá innovación si existe; bajá brecha si hay jugador argentino; bajá factibilidad si requiere hardware caro, licencias, capital de trabajo o programar mucho; sé duro con el potencial.
5) Veredicto: mantener / bajar / descartar (descartar solo si es repetida del registro, si ya existe en Argentina casi igual, o si es inviable; ante la duda: bajar, no descartar).
6) nota_para_facu: 2-4 líneas honestas, en español rioplatense, con lo que más le sirve saber.
Nada inventado: toda afirmación nueva con URL y fecha de consulta 2026-10-18. Tu texto final NO lo lee un humano: devolvé solo el objeto estructurado.`,
  { label: `verif:${l}`, phase: 'Verificar', schema: SCHEMA }
)))
const ok = out.filter(Boolean)
log(`${ok.length}/${LOTES.length} lotes verificados · ${ok.reduce((n, r) => n + r.verificaciones.length, 0)} ideas`)
return { lotes: ok, faltaron: LOTES.filter((l, i) => !out[i]) }
