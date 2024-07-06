from odoo import models, fields, api, _
from odoo.exceptions import ValidationError



class CreditGroup(models.Model):
    _name = "credit.group"

    _sql_constraints = [
        ('unique_credit_code', 'unique(code)', 'This credit code is already used!!'),
        ('unique_sale_channel_id', 'unique(sale_channel_id)', 'This Sale Channel is already used!!'),
    ]
    @api.constrains('code')
    def _avoid_n026_credit_code(self):
        if "026" in self.code:
            raise ValidationError(_("You can not include the string '026' for the code!!"))

    name = fields.Char(string=_("Name"))
    code = fields.Char(string=_("Code"), required=True)
    sale_channel_id = fields.Many2one(comodel_name="sale.channel", string=_("Sale Channel"), required=True)
    company_id = fields.Many2one(comodel_name='res.company', string='Company',
                                 store=True, readonly=True,
                                 default=lambda x: x.env.company)
    company_currency_id = fields.Many2one(string='Company Currency', readonly=True, related='company_id.currency_id')
    global_credit = fields.Monetary(string=_("Global Credit"), currency_field='company_currency_id')
    # TODO Add copmute method for used_credit
    used_credit = fields.Monetary(string=_("Used Credit"), currency_field='company_currency_id', compute="_compute_used_credit", store=True)
    credit_avaiable = fields.Monetary(string=_("Credit Avaiable"), currency_field='company_currency_id', compute="_compute_credit_avaiable", store=True)

    res_partner_id = fields.Many2one(comodel_name="res.partner")

    @api.depends("used_credit")
    def _compute_credit_avaiable(self):
        for rec in self:
            rec.credit_avaiable = rec.global_credit - rec.used_credit

    def _compute_used_credit(self):
        for rec in self:
            so_total = 0
            inv_total = 0
            sale_orders = self.env["sale.order"].search([("sale_channel_id", "=", rec.sale_channel_id.id), ("state", "=", "sale"), ("invoice_status", "!=", "invoiced")])
            invoices = self.env["account.move"].search([("sale_channel_id", "=", rec.sale_channel_id.id),("payment_state", "=", "not_paid")])
            so_with_credit = sale_orders.filtered(lambda x: rec.id in x.partner_id.credit_group_ids)
            inv_with_credit = invoices.filtered(lambda x: rec.id in x.partner_id.credit_group_ids)
            if so_with_credit:
                so_total = sum([x.amount_total for x in so_with_credit])
            if inv_with_credit:
                inv_total = sum([x.amount_total for x in inv_with_credit])
            rec.used_credit += so_total + inv_total