from odoo import api, fields, models, _


class Bank(models.Model):
    _name = "dm.bank"
    _description = "DM Bank Model"

    name = fields.Char("Bank Name", required=True)
    code = fields.Char("Code", default="/", required=True)
    partner_id = fields.Many2one("res.partner", string="Partner")
    balance = fields.Float("Balance", compute="_get_final_bank_balance")

    @api.model
    def create(self, vals):
        vals['code'] = self.env['ir.sequence'].next_by_code("dm.bank")
        #Auto generate sequence for the bank profile.
        return super(Bank, self).create(vals)
    
    def _get_final_bank_balance(self):
        tran_obj = self.env['dm.bank.transactions']
        for record in self:
            all_transactions = tran_obj.search([('bank_id','=',record.id),('state','=','done')])
            all_deposit = sum(all_transactions.filtered(lambda lm:lm.tran_state == 'deposit').mapped("balance"))
            all_withdraw = sum(all_transactions.filtered(lambda lm:lm.tran_state == 'withdraw').mapped("balance"))
            record.balance = (all_deposit - all_withdraw) or 0.00
    
    _sql_constraints = [
        ('unique_dm_bank', 'unique(name)', 'Please provide unique bank name.'),
    ]