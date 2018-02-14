# -*- coding: utf-8 -*-
from odoo import api, fields, models


class Remisiones_lines(models.Model):
	_name = 'blemer.remisiones.lines'

	
	x_parent_id = fields.Many2one('res.partner',ondelete='set null', default= lambda  self: self.env.context.get('x_parent_id'))
	
	name = fields.Many2one('product.product', string="Producto", required=True)
	x_cantidad_line = fields.Float("Cantidad", required=True, default=1.00)
	x_unidad_de_medida = fields.Many2one(
	    'product.uom', string="Unidad de medida", related='name.uom_id', readonly=True)
	x_remision_id = fields.Many2one('blemer.remisiones')
	
	"""@api.onchange('x_unidad_de_medida')
	def _onchange_project_ids(self):
		domain = {}
		product_list = []
		print("xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx test_final")
		partner_obj = self.env['product.product'].search([('seller_ids.name.id', '=', self.env.context.get('x_parent_id'))])
		for partner_ids in partner_obj:
			product_list.append(partner_ids.id)
			# to assign parter_list value in domain
		domain = {'name': [('id', '=', product_list)]}
		return {'domain': domain}"""