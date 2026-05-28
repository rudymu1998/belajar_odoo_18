from odoo import models, fields

class CustomItem(models.Model):
    _name = 'custom.item'
    _description = 'Custom Item'

    name = fields.Char(
        string="Item Name",
        required=True
    )
    price = fields.Float(
        string="Price", 
        required=True
    )
    qty = fields.Integer(
        string="Stock Qty",
        required=True
    )