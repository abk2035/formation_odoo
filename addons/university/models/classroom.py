from odoo import models, fields,api

class UniversityClassroom(models.Model):
    _name = "university.classroom"
    _rec_name = 'classroom_name'

    classroom_name = fields.Char(string='name')
    code = fields.Char()

    student_ids = fields.One2many(comodel_name='university.student', inverse_name='classroom_id')

    professor_ids = fields.Many2many(
        comodel_name='university.professor', 
        relation='professor_classroom_rel',
        column1='classroom_name',
        column2='f_name') 
    
   
    
    num_prof = fields.Integer(string="Number of Professors",compute="comp_prof")
    num_stu = fields.Integer(string="Number of Students",compute="comp_stu")

    def comp_prof(self) :
       self.num_prof = len(self.professor_ids)

    def comp_stu(self) :
       self.num_stu = len(self.student_ids)
    @api.onchange('subject_ids')
    def check_number_of_subject(self):
       if len(self.subject_ids)>3:
          return {'warning':{'title':'warning',
                             'message': 'the number of subjects must be less than 3'}}
       