from odoo import models, fields

class CustomOrderLine(models.Model):
    _name = 'custom.order.line'
    _description = 'Custom Order Line'

    order_id = fields.Many2one(
        'custom.order',
        string="order"
    )

    item_id = fields.Many2one(
        'custom.item',
        string="Item"
    )

    qty = fields.Integer(
        string="Qty",
        default=1
    )

    price = fields.Float(
        string="Price"
    )