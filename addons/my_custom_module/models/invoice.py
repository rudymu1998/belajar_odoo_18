from odoo import models, fields
from datetime import datetime

class CustomInvoice(models.Model):
    _name = 'custom.invoice'
    _description = 'Custom Invoice'

    name = fields.Char(
        string="Invoice Number",
        readonly=True
    )

    order_id = fields.Many2one(
        'custom.order',
        string="Order"
    )

    customer_name = fields.Char(
        string="Customer"
    )

    amount = fields.Float(
        string="Amount"
    )

    invoice_date = fields.Date(
        string="Invoice Date",
        default=fields.Date.today
    )

    state = fields.Selection([
        ('draft', 'Draft'),
        ('paid', 'Paid')
    ], default='draft', string="Status")