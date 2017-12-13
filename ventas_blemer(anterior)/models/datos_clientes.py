# -*- coding: utf-8 -*-
from odoo import fields, models


class Datos_clientes(models.Model):
	_inherit = 'res.partner'

	x_blemer_vehiculos_cliente = fields.One2many('fleet.vehicle', 'x_blemer_cliente_vehiculo', "Vehículos del cliente")