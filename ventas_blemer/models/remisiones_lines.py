# -*- coding: utf-8 -*-
from odoo import api, fields, models


class Remisiones_lines(models.Model):
	_name = 'blemer.remisiones.lines'

	name = fields.Many2one('product.product', string="Producto")
	x_cantidad_line = fields.Integer("Cantidad")
	x_unidad_de_medida = fields.Many2one('product.uom', string="Unidad de medida")
	x_remision_id = fields.Many2one('blemer.remisiones')