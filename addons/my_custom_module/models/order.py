from odoo import models, fields

class CustomOrder(models.Model):
    _name = 'custom.order'
    _description = 'Custom Order'

    name = fields.Char(string='Order Number', required=True)
    customer_name = fields.Char(string='Customer')
    order_date = fields.Date(string='Order Date')
    amount = fields.Float(string='Total Amount')

    state = fields.Selection([
        ('draft', 'Draft'),
        ('confirm', 'Confirmed'),
        ('done', 'Done')
    ], default='draft', string='Status')

    def action_confirm(self):
        self.state = 'confirm'

    def action_done(self):
        self.state = 'done'