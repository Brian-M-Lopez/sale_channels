from odoo import models, fields, _

class SaleChannel(models.Model):
    _name = "sale.channel"

    name = fields.Char(string=_("Name"))
    deposit = fields.Many2one(comodel_name="stock.warehouse", string=_("Deposit"))
    invoice_journal_id = fields.Many2one(comodel_name="account.journal", string=_("Invoice Journal"))
    # TODO add field for secuence (Python and XML view)
