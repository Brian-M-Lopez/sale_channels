from odoo import models, fields, api, _


class SaleOrder(models.Model):
    _inherit = "sale.order"

    sale_channel_id = fields.Many2one(comodel_name="sale.channel", string=_("Sale Channel"), required=True)

    @api.onchange("sale_channel_id")
    def _oncahnge_sale_channel_id(self):
        if self.sale_channel_id and self.sale_channel_id.warehouse_id:
            self.warehouse_id = self.sale_channel_id.warehouse_id