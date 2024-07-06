from odoo import models, fields, api, _


class SaleOrder(models.Model):
    _inherit = "sale.order"

    sale_channel_id = fields.Many2one(comodel_name="sale.channel", string=_("Sale Channel"), required=True)
    credit_type = fields.Selection(
        selection=[('no_limit', 'No Limit'), ('credit_avaiable', 'Credit Avaiable'), ('credit_bloqued', 'Credit Bloqued')],
        string=_("Credit Type"),
        default='no_limit',
        compute="_compute_credit_type"
    )

    @api.onchange("sale_channel_id")
    def _oncahnge_sale_channel_id(self):
        if self.sale_channel_id and self.sale_channel_id.warehouse_id:
            self.warehouse_id = self.sale_channel_id.warehouse_id
    
    @api.depends("partner_id", "sale_channel_id")
    def _compute_credit_type(self):
        if self.partner_id and self.partner_id.user_credit_control and self.sale_channel_id:
            credit_group = self.env["credit.group"].search([("partner_id", "=", self.res_partner), ("sale_channel_id", "=", self.sale_channel_id)])
            if credit_group:
                pass

    def _prepare_invoice(self):
        invoice_vals = super(SaleOrder, self)._prepare_invoice()
        invoice_vals['sale_channel_id'] = self.sale_channel_id.id
        return invoice_vals