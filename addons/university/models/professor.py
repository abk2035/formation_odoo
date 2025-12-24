from odoo import models, fields,api

class UniversityProfessor(models.Model):
    _name = "university.professor"

    f_name = fields.Char('First name')
    l_name = fields.Char('Last name')
    sexe = fields.Selection([('male','Male'),('female','Female')])
    identity_card = fields.Char('Identity card')
    address = fields.Text('Adresse')
    birthday = fields.Date('birthday')
    inscription_date = fields.Datetime('Date of inscription')  
    email = fields.Char()
    phone = fields.Char()
    active = fields.Boolean('Active',default=True)

    department_id = fields.Many2one(comodel_name='university.department')
    subject_id = fields.Many2one(comodel_name='university.subject')

    classroom_ids = fields.Many2many(
        comodel_name='university.classroom',
        relation='professor_classroom_rel',
        column1='f_name',
        column2='classroom_name')
    
    
    def name_get(self):
        result = []
        for prof in self :
            name = '['+prof.department_id + department_name +']'+ prof.f_name + ' ' + prof.l_name
            result.append((prof.id,name))

        return result