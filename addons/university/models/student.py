from odoo import models, fields, api

class UniversityStudent(models.Model):
    _name = "university.student"

    f_name = fields.Char('First name')
    l_name = fields.Char('Last name')
    sexe = fields.Selection([('male','Male'),('female','Female')])
    identity_card = fields.Char('Identity card')
    address = fields.Text('Adresse')
    birthday = fields.Date('birthday')
    registration_date = fields.Date('registration Date')  
    email = fields.Char()
    phone = fields.Char()
    active = fields.Boolean('Active',default=True)

    department_id = fields.Many2one(comodel_name='university.department')
    classroom_id = fields.Many2one(comodel_name='university.classroom')

    subject_ids = fields.Many2many(commodel_name='university.subject',
                                    relation='student_subject_rel',
                                    column1='f_name',
                                    column2='name' )
    
    def name_get(self):
        result = []
        for student in self :
            name = '['+student.classroom_id + classroom_name +']'+ student.f_name + ' ' + student.l_name
            result.append((student.id,name))

        return result
    @api.constrains('registration_date', 'birthday')
    def check_dates(self):
        if self.birthday > self.registration_date :
            raise ValueError('The birthday must be inferior than the registration date')
    
    def custom_function(self):
        for rec in self:
            rec.f_name = rec.f_name.upper()
            print("Custom function executed for student:", rec.f_name, rec.l_name)
    
    def unlink(self):
        # Désactive simplement l'enregistrement au lieu de le supprimer
        self.write({'active': False})
        # Retourne True pour indiquer que l'opération est réussie
        return True