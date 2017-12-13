from odoo import api, fields, models


class Test_escribir(models.Model):
	_inherit = 'mail.followers'

	subtype_ids = fields.Many2many('mail.message.subtype', default='get_taxes')

	@api.model
	def get_taxes(self):
		return self.env['mail.message.subtype'].search('id','=',1)