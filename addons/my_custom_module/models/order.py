from odoo import api, models, fields
from datetime import datetime

class CustomOrder(models.Model):
    _name = 'custom.order'
    _description = 'Custom Order'

    name = fields.Char(string='Order Number', default='xxxxxxxxxxx', readonly= True)
    customer_name = fields.Char(string='Customer')
    order_date = fields.Date(string='Order Date')
    amount = fields.Float(string='Total Amount' ,readonly= True)

    state = fields.Selection([
        ('draft', 'Draft'),
        ('confirm', 'Confirmed'),
        ('done', 'Done')
    ], default='draft', string='Status', required=True)

    line_ids = fields.One2many(
        'custom.order.line',
        'order_id',
        string="Order Lines"
    )

    def action_confirm(self):
        self.state = 'confirm'

    def action_done(self):
        self.state = 'done'

    @api.model
    def create(self, vals):
        record = super(CustomOrder, self).create(vals)

        dt = datetime.today()
        date_str = dt.strftime('%Y%m%d')

        record.name = f"{date_str}-{record.id}"

        return record