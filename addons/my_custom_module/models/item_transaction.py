from odoo import models, fields

class ItemTransaction(models.Model):
    _name = 'custom.item.transaction'
    _description = 'Item Transaction'

    item_id = fields.Many2one(
        'custom.item',
        string="Item"
    )
    order_id = fields.Many2one(
        'custom.order',
        string="Order"
    )
    qty_taken = fields.Float(
        string="Qty Taken"
    )
    balance_qty = fields.Float(
        string="Balance Qty"
    )
    transaction_date = fields.Datetime(
        string="Transaction Date",
        default=fields.Datetime.now
    )