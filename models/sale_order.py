from odoo import models, fields, _


class SaleOrder(models.Model):
    _inherit = "sale.order"

    sale_channel_id = fields.Many2one(comodel_name="sale.channel", string=_("Sale Channel"), required=True)