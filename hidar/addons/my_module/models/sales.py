# models/sales.py
from odoo import models, fields

class SaleOrder(models.Model):
    _inherit = 'sale.order'

    # Add custom fields or methods if necessary
