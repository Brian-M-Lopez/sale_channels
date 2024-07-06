from odoo import models, fields, _

class SaleChannel(models.Model):
    _name = "sale.channel"

    name = fields.Char(string=_("Name"), required=True)
    code = fields.Char(string=_("Code"), default=lambda self: self.env['ir.sequence'].next_by_code('sale.channel'), readonly=True)
    deposit = fields.Many2one(comodel_name="stock.warehouse", string=_("Deposit"))
    invoice_journal_id = fields.Many2one(comodel_name="account.journal", string=_("Invoice Journal"))