# -*- coding: utf-8 -*-
from odoo import api, fields, models


class Datos_ventas(models.Model):
    _name = 'blemer.remisiones'
    _inherit = 'mail.thread'

    name = fields.Char("Remisión")

    x_blemer_cliente = fields.Many2one(
        'res.partner', "Cliente: ", required=True)
    x_blemer_proveedor = fields.Many2one(
        'res.partner', "Proveedor: ", required=True)
    x_blemer_remision_lines = fields.One2many(
        'blemer.remisiones.lines', 'x_remision_id', string="Productos")
    x_blemer_fecha_remision = fields.Datetime("Fecha y hora : ")
    x_blemer_vehiculos = fields.Many2one('fleet.vehicle', string="Placas: ")
    x_blemer_vehiculo_conductor = fields.Char("Conductor: ")

    message_follower_ids = fields.One2many(
        'mail.followers', 'res_id', compute='add_follower_id')

    state = fields.Selection([
        ('draft', 'Borrador'),
        ('confirmed', 'Confirmada'),
        ('done', 'Hecha'),
    ], default='draft', readonly=True)

    @api.multi
    def add_follower_id(self):
        for record in self:
            # record.message_follower_ids.append(x_blemer_cliente.id)
            record.write({'message_follower_ids': [
                         (6, 0, record.x_blemer_cliente.id)]})
            print ("******************************",
                   record.x_blemer_cliente.id)

    @api.multi
    def asignar_borrador(self):
        self.state = 'draft'

    @api.multi
    def asignar_confirmado(self):
        self.state = 'confirmed'

    @api.one
    @api.depends('x_blemer_vehiculos')
    def _get_datos_vehiculos(self):
        for record in self:
            record.x_blemer_placas_vehiculo = record.x_blemer_vehiculos.license_plate
            record.x_blemer_tipo_vehiculo = record.x_blemer_vehiculos.x_blemer_tipo_vehiculo

    # Generar una orden de venta
    @api.one
    def generar_orden_venta(self):
        vals_orden_venta = {
            'note': self.name,
            #'state': 'invoice_exept',
            'date_order': self.x_blemer_fecha_remision,
            #'date_create': self.x_blemer_fecha_remision,
            #'date_confirm': self.date_confirm,
            #'user_id': self.user_id.id,
            'partner_id': self.x_blemer_cliente.id,
            #'order_policy': 'manual',
            #'order_line':[1],
            #'product_id' : [4533]
        }
        res = self.env['sale.order'].create(vals_orden_venta)
        print ("**************************** res_id", res.id)
        #self.state = 'done'
		
        aux = self.x_blemer_remision_lines        
        for n in aux:
            vals_line = {
                'order_id':  res.id,
                'product_id':  n.name.id,
                'product_uom_qty': n.x_cantidad_line,
            }            
            res_line = self.env['sale.order.line'].create(vals_line)
		
        return res,res_line
