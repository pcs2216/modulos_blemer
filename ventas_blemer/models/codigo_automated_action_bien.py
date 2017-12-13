# Available variables:
#  - env: Odoo Environment on which the action is triggered
#  - model: Odoo Model of the record on which the action is triggered; is a void recordset
#  - record: record on which the action is triggered; may be be void
#  - records: recordset of all records on which the action is triggered in multi-mode; may be void
#  - time, datetime, dateutil, timezone: useful Python libraries
#  - log: log(message, level='info'): logging function to record debug information in ir.logging table
#  - Warning: Warning Exception to use with raise
# To return an action, assign: action = {...}
numero_de_seguidores = len(record.message_follower_ids)
if record.x_blemer_cliente != False and record.x_blemer_proveedor != False:
  #print ("**************** Primer IF")
  if True:
    #print ("**************** segundo IF")
    id_cliente = record.x_blemer_cliente.id
    id_proveedor = record.x_blemer_proveedor.id
    modelo = "blemer.remisiones"
    id_registro = record.id
    ids_subtipo = [1]
    valores_cliente = {
    'res_model': modelo,
    'partner_id': id_cliente,
    'res_id': id_registro,
    'subtype_ids': [(6, 0,ids_subtipo)],
    }
    valores_proveedor = {'res_model': modelo,'partner_id': id_proveedor,'res_id': id_registro,'subtype_ids': [(6, 0, ids_subtipo)]}
    ejecutar_cliente = record.env['mail.followers'].create(valores_cliente)
    #print ("**************** ejecutar n1 ****************")
    ejecutar_proveedor = record.env['mail.followers'].create(valores_proveedor)
    #print ("**************** ejecutar n2 ****************")