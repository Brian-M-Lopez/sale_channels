from odoo import models, fields, _


class ResPartner(models.Model):
    _inherit = "res.partner"

    user_credit_control = fields.Boolean(string=_("User has credit control?"))
    credit_group_ids = fields.One2many(comodel_name="credit.group", inverse_name="res_partner_id", string=_("Credits"))
