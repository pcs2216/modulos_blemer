# -*- coding: utf-8 -*-
from odoo import api, fields, models


class Datos_ventas(models.Model):
	_name = 'blemer.remisiones'
	_inherit = 'mail.thread'

	name = fields.Char("Remisión", required=True)
	x_blemer_cliente = fields.Many2one('res.partner', "Cliente: ", required=True)
	x_blemer_proveedor = fields.Many2one('res.partner', "Proveedor: ", required=True)
	x_blemer_remision_lines = fields.One2many('blemer.remisiones.lines', 'x_remision_id', string="Productos", required=True)
	x_blemer_fecha_remision = fields.Datetime("Fecha y hora: ", required=True,default=fields.Datetime.now)
	x_blemer_vehiculos = fields.Many2one('fleet.vehicle', string="Placas: ", required=True)
	x_blemer_vehiculo_conductor = fields.Char("Conductor: ", required=True)
	x_blemer_entrego = fields.Char(string="Entregó: ", required=True)
	x_blemer_quien_elaboro = fields.Many2one('res.partner', string="Quien Elaboró: ", required=True)
	x_blemer_aprobo = fields.Char(string="Aprobó: ", required=True)	
	x_blemer_bascula = fields.Char(string='Ticket de báscula: ')
	

	state = fields.Selection([
         ('draft', 'Borrador'),
         ('confirmed', 'Confirmada'),
         ('done', 'Hecha'),
         ], default='draft', readonly=True)


	@api.multi
	def asignar_borrador(self):
		self.state = 'draft'

	@api.multi
	def asignar_confirmado(self):
		self.state = 'confirmed'

	@api.multi
	def generar_seguidores(self):
		try:
			for record in self:
				numero_de_seguidores = len(record.message_follower_ids)
				if record.x_blemer_cliente != False and record.x_blemer_proveedor != False:
					print ("**************** Primer IF") 
					if numero_de_seguidores != 3:
						print ("**************** segundo IF") 
						id_cliente = record.x_blemer_cliente.id
						id_proveedor = record.x_blemer_proveedor.id
						modelo = "blemer.remisiones"
						id_registro = record.id
						ids_subtipo = [1]
						#Datos Usuario
						ids_subtipos_admin = [1,2,3]
						id_usuario = record.create_uid.id

						valores_usuario = {
						'res_model': modelo,
						'partner_id': id_usuario,
						'res_id': id_registro,
						'subtype_ids': [(6, 0,ids_subtipos_admin)],
						}

						valores_cliente = {
						'res_model': modelo,
						'partner_id': id_cliente,
						'res_id': id_registro,
						'subtype_ids': [(6, 0,ids_subtipo)],
						}

						valores_proveedor = {
						'res_model': modelo,
						'partner_id': id_proveedor,
						'res_id': id_registro,
						'subtype_ids': [(6, 0, ids_subtipo)],
						}

						ejecutar_cliente = record.env['mail.followers'].create(valores_cliente)
						print ("**************** ejecutar n1 ****************")
						ejecutar_proveedor = record.env['mail.followers'].create(valores_proveedor)
						print ("**************** ejecutar n2 ****************")
						ejecutar_usuario = record.env['mail.followers'].create(valores_usuario)
						print ("**************** ejecutar n3 ****************")
		except Exception as e:
			print ("******************* Exception ******", e)

	#Generar una orden de venta
	@api.one
	def generar_orden_venta(self):
		vals_orden_venta = {
		'note': self.name,
		'date_order': self.x_blemer_fecha_remision,
		'partner_id': self.x_blemer_cliente.id,
		}
		res = self.env['sale.order'].create(vals_orden_venta)

		aux = self.x_blemer_remision_lines 
		for lineas_venta in aux:
			vals_line = {
			'order_id': res.id,
			'product_id': lineas_venta.name.id,
			'product_uom_qty': lineas_venta.x_cantidad_line,
			} 
			res_line = self.env['sale.order.line'].create(vals_line)
		self.state = 'done'

		return res, res_line
	
	
	@api.onchange('x_blemer_proveedor')
	def onchange_x_proveedor (self):
		print("*************************it's working")
		self.x_blemer_quien_elaboro=''
		self.x_blemer_remision_lines=[]