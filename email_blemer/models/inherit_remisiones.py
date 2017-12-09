# -*- coding: utf-8 -*-
from odoo import fields, models, api


class tos_clientes(models.Model):
    _inherit = 'blemer.remisiones'

    @api.multi
    def send_mail_template_1(self):
        print("********************** entrando")
        template = self.env.ref('email_blemer.blemer_remision_email_template')
        if template:
            self.env['mail.template'].browse(template.id).send_mail(self.id)
