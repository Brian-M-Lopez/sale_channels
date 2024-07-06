from odoo import models, fields, _


class AccountMove(models.Model):
    _inherit = "account.move"

    sale_channel_id = fields.Many2one(comodel_name="sale.channel", string=_("Sale Channel"))
