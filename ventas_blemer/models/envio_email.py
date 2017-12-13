from odoo import api, models, fields

class Envio_email(models.Model):
	_inherit = 'blemer.remisiones'

	@api.multi
	def send_mail_template_1(self):
		template = self.env.ref('ventas_blemer.blemer_remision_email_template')
		if template:
			self.env['mail.template'].browse(template.id).send_mail(self.id)