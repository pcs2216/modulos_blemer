# -*- coding: utf-8 -*-
from odoo import fields, models


class Datos_vehiculos(models.Model):
	_inherit = 'fleet.vehicle'
	
	x_blemer_cliente_vehiculo = fields.Many2one('res.partner', "Dueño del vehículo")
	x_blemer_tipo_vehiculo = fields.Char("Tipo de vehículo")