from odoo import api, fields, models, _


class User(models.Model):
    _inherit = "res.users"

    bank_id = fields.Many2one("dm.bank", string="Bank Name")

class WbPartner(models.Model):
    _inherit = "res.partner"

    bank_id = fields.Many2one("dm.bank", string="Bank Name",
                                 default=lambda lm:lm.env.user.bank_id and lm.env.user.bank_id.id or False
                                 )
    balance = fields.Float("Balance", compute="_get_final_bank_balance")

    def _get_final_bank_balance(self):
        tran_obj = self.env['dm.bank.transactions']
        for record in self:
            all_transactions = tran_obj.search([('bank_id','=',record.bank_id.id),
                                                ('name','=', record.id),
                                                ('state','=','done')])
            all_deposit = sum(all_transactions.filtered(lambda lm:lm.tran_state == 'deposit').mapped("balance"))
            all_withdraw = sum(all_transactions.filtered(lambda lm:lm.tran_state == 'withdraw').mapped("balance"))
            record.balance = (all_deposit - all_withdraw) or 0.00

    def redirect_to_transaction(self):

        return {
            "name": _("Transaction History"),
            "view_mode":"tree",
            "res_model":"dm.bank.transactions",
            "view_id": self.env.ref("deposit_management.dm_bank_transactions_tree_view").id,
            "type": 'ir.actions.act_window',
            'domain':[('name','=',self.id)]
        }