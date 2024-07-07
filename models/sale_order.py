from odoo import models, fields, api, _
from odoo.exceptions import ValidationError


class SaleOrder(models.Model):
    _inherit = "sale.order"

    sale_channel_id = fields.Many2one(comodel_name="sale.channel", string=_("Sale Channel"), required=True)
    credit_type = fields.Selection(
        selection=[('no_limit', 'No Limit'), ('credit_avaiable', 'Credit Avaiable'), ('credit_bloqued', 'Credit Bloqued')],
        string=_("Credit Type"),
        default='no_limit',
        compute="_compute_credit_type",
        store=True
    )

    @api.onchange("sale_channel_id")
    def _oncahnge_sale_channel_id(self):
        if self.sale_channel_id and self.sale_channel_id.warehouse_id:
            self.warehouse_id = self.sale_channel_id.warehouse_id
    
    @api.depends("partner_id", "sale_channel_id", "amount_total")
    def _compute_credit_type(self):
        for rec in self:
            if rec.partner_id and rec.partner_id.user_credit_control and rec.sale_channel_id:
                credit_group = rec.env["credit.group"].search([("res_partner_id", "=", rec.partner_id.id), ("sale_channel_id", "=", rec.sale_channel_id.id)])
                if credit_group:
                    credit_avaiable = credit_group.credit_avaiable
                    if credit_avaiable > rec.amount_total:
                        rec.credit_type = 'credit_avaiable'
                    elif credit_avaiable < rec.amount_total:
                        rec.credit_type = 'credit_bloqued'

    def _prepare_invoice(self):
        invoice_vals = super(SaleOrder, self)._prepare_invoice()
        invoice_vals['sale_channel_id'] = self.sale_channel_id.id
        return invoice_vals
    
    def _action_confirm(self):
        res = super()._action_confirm()
        if self.credit_type == 'credit_bloqued':
            raise ValidationError(_("You can't confirm a Sale Order with bloqued credit!!"))
        else:
            return res
