# -*- coding: utf-8 -*-
from odoo import api, fields, models


class Datos_ventas(models.Model):
    _inherit = 'sale.order'

    x_blemer_remision_id = fields.Many2one('blemer.remisiones',
                                           string='Remisión Origen : ',
                                           ondelete='set null',
                                           readonly=True,
                                           )


class Datos_ventas(models.Model):
    _inherit = 'purchase.order'

    x_blemer_remision_ref = fields.Many2one('blemer.remisiones',
                                            string='Remisión Origen : ',
                                            ondelete='set null',
                                            readonly=True,
                                            #compute='depends_origin',
                                            #default=lambda self: self.env['blemer.remisiones'].search([('x_blemer_saleOrder.name','=',self.origin)])
                                            )
    """
    @api.depends('origin')
    def depends_origin(self):
        if self.origin:
            print("xxxxxxx", self.origin)
            self.x_blemer_remision_ref = self.env['blemer.remisiones'].search(
                [('x_blemer_saleOrder.name', '=', self.origin)])
    """