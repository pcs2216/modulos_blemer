# -*- coding: utf-8 -*-
from odoo import api, fields, models


class Datos_ventas(models.Model):
    _inherit = 'sale.order'

    x_blemer_remision_id = fields.Many2one('blemer.remisiones',
        string='Remisión Origen : ',
        ondelete='set null',        
        readonly=True,        
    )
    
    