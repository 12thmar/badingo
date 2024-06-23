from odoo import http
from odoo.http import request
import json
import logging
from datetime import datetime

_logger = logging.getLogger(__name__)

class SalesAPIController(http.Controller):

    def _serialize_date(self, date_obj):
        if isinstance(date_obj, datetime):
            return date_obj.strftime('%Y-%m-%d %H:%M:%S')
        return date_obj

    @http.route('/api/sales', type='http', auth='public', methods=['GET'], csrf=False)
    def get_sales(self, **kwargs):
        _logger.info("Sales API called")
        SaleOrder = request.env['sale.order'].sudo()
        sales = SaleOrder.search([])
        sales_data = []
        for sale in sales:
            sales_data.append({
                'id': sale.id,
                'name': sale.name,
                'date_order': self._serialize_date(sale.date_order),
                'amount_total': sale.amount_total,
                'customer': sale.partner_id.name,
            })
        return request.make_response(json.dumps(sales_data),
                                     headers={'Content-Type': 'application/json'})

    @http.route('/api/sales/make_sale', type='json', auth='public', methods=['POST'], csrf=False)
    def make_sale(self, **kwargs):
        _logger.info("Make Sale API called")
        
        # Extract required fields from the request
        customer_id = kwargs.get('customer_id')
        products = kwargs.get('products')  # List of product tuples (product_id, quantity)
        
        if not customer_id or not products:
            return request.make_response(json.dumps({'error': 'Missing customer_id or products'}), 
                                         headers={'Content-Type': 'application/json'})

        try:
            SaleOrder = request.env['sale.order'].sudo()
            SaleOrderLine = request.env['sale.order.line'].sudo()
            ProductProduct = request.env['product.product'].sudo()

            # Create a new sale order
            sale_order = SaleOrder.create({
                'partner_id': customer_id,
                'date_order': datetime.now(),
            })

            # Add products to the sale order
            for product_id, quantity in products:
                product = ProductProduct.browse(product_id)
                if product:
                    SaleOrderLine.create({
                        'order_id': sale_order.id,
                        'product_id': product.id,
                        'product_uom_qty': quantity,
                        'price_unit': product.lst_price,
                    })
                    # Update product quantity in inventory
                    product.qty_available -= quantity

            return request.make_response(json.dumps({'success': 'Sale created successfully', 'order_id': sale_order.id}),
                                         headers={'Content-Type': 'application/json'})
        except Exception as e:
            _logger.error(f"Error creating sale: {e}")
            return request.make_response(json.dumps({'error': str(e)}),
                                         headers={'Content-Type': 'application/json'})
