from odoo import models, fields, api, _

class SaleChannel(models.Model):
    _name = "sale.channel"
    _inherit = ['mail.thread']

    name = fields.Char(string=_("Name"), required=True)
    code = fields.Char(string=_("Code"), default=lambda self: _('New'), readonly=True)
    warehouse_id = fields.Many2one(comodel_name="stock.warehouse", string=_("Deposit"))
    invoice_journal_id = fields.Many2one(comodel_name="account.journal", string=_("Invoice Journal"))

    @api.model
    def create(self, vals):
        if vals.get('code', _('New')) == _('New'):
            vals['code'] = self.env['ir.sequence'].next_by_code('sale.channel') or _('New')
        res = super(SaleChannel, self).create(vals)
        return res