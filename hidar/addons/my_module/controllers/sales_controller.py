from odoo import http
from odoo.http import request
import json

class SalesController(http.Controller):
    
    @http.route('/sales/data', auth='public', type='http', methods=['GET'], csrf=False)
    def get_sales_data(self, **kwargs):
        SalesOrder = request.env['sale.order']
        sales_orders = SalesOrder.search([])
        
        sales_data = []
        for order in sales_orders:
            sales_data.append({
                'id': order.id,
                'name': order.name,
                'partner_id': order.partner_id.id,
                'partner_name': order.partner_id.name,
                'amount_total': order.amount_total,
                'date_order': order.date_order,
            })
        
        return request.make_response(
            json.dumps(sales_data),
            headers={'Content-Type': 'application/json'}
        )
