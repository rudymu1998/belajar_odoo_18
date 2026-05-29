from odoo import api, models, fields
from datetime import datetime

class CustomOrder(models.Model):
    _name = 'custom.order'
    _description = 'Custom Order'

    name = fields.Char(
        string='Order Number', 
        default='xxxxxxxxxxx', 
        readonly= True
    )
    customer_name = fields.Char(
        string='Customer'
    )
    order_date = fields.Date(
        string='Order Date'
    )
    amount = fields.Float(
        string='Total Amount',
        compute='_compute_amount',
        store=True,
        readonly= True
    )
    state = fields.Selection(
        [('draft', 'Draft'),
        ('confirm', 'Confirmed'),
        ('done', 'Done')], 
        default='draft', 
        string='Status', 
        required=True
    )
    line_ids = fields.One2many(
        'custom.order.line',
        'order_id',
        string="Order Lines"
    )

    def action_confirm(self):
        print("Confirming order...")
        for rec in self:

            for line in rec.line_ids:

                item = line.item_id

                # kurangi stock
                item.qty -= line.qty

                # create transaction
                self.env['custom.item.transaction'].create({
                    'item_id': item.id,
                    'order_id': rec.id,
                    'qty_taken': line.qty,
                    'balance_qty': item.qty
                })

            rec.state = 'confirm'

    def action_done(self):

        for rec in self:

            invoice = self.env['custom.invoice'].create({
                'name': f"INV-{rec.name}",
                'order_id': rec.id,
                'customer_name': rec.customer_name,
                'amount': rec.amount
            })

            rec.state = 'done'

    @api.depends('line_ids.subtotal')
    def _compute_amount(self):
        for rec in self:
            rec.amount = sum(rec.line_ids.mapped('subtotal'))

    @api.model
    def create(self, vals):
        record = super(CustomOrder, self).create(vals)

        dt = datetime.today()
        date_str = dt.strftime('%Y%m%d')

        record.name = f"{date_str}-{record.id}"

        return record