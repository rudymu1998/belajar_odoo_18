from odoo import models, fields, api

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
    subtotal = fields.Float(
        string="Subtotal",
        compute="_compute_subtotal",
        store=True
    )


    @api.depends('qty', 'price')
    def _compute_subtotal(self):
        for record in self:
            record.subtotal = record.qty * record.price 

    @api.onchange('item_id')
    def _onchange_item_id(self):
        for rec in self:
            if rec.item_id:
                rec.price = rec.item_id.price