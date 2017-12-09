# -*- coding: utf-8 -*-
from odoo import fields, models


class Add_comercial_name(models.Model):
	_inherit = 'res.partner'

	x_blemer_comercial_name = fields.Char(string="Nombre comercial")