@api.one
def generate_record_name(self):
	vals = {
	#'name': self.x_name,
	#'state': 'invoice_exept',
	'date_order': self.x_today,
	'date_create': self.x_today,
	#'date_confirm': self.date_confirm,
	#'user_id': self.user_id,
	'partner_id': self.x_cliente.id,
	'order_policy': 'manual',
	#'order_line':[1],
	#'product_id' : [4533]
	}

res = self.env['sale.order'].create(vals)

aux = [5, 3]
i = 0
for n in aux:
	vals_line = {
	'order_id': res.id,
	'product_id': self.x_productos.id,
	'product_uom_qty': aux[i],
	'product_uom': self.x_productos.uom_id.id,
	}
	i = i + 1

res_line = self.env['sale.order.line'].create(vals_line)

return res




<header>
<button name="generate_record_name" string="Confirmar venta" type="object" class="oe_highlight" invisible= "[('x_state','not in',('draft'))]"/>
<!--button name="draft" type="workflow" string="Reset to draft" states="confirmed,done"/><button name="confirm" type="workflow" string="Confirm" states="draft" class="oe_highlight"/-->
<field name="x_state" widget="statusbar"/>
</header>

<button name="generate_record_name" string="Confirmar venta" type="object" class="oe_highlight"  invisible= "[('x_state','not in',('draft'))]"/>