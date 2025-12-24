from odoo import models, fields

class UniversitySubject(models.Model):
    _name = "university.subject"


    name = fields.Char()
    code = fields.Char()

    department_id = fields.Many2one(comodel_name='university.department')

    classroom_ids = fields.Many2many(
        comodel_name='university.classroom',
        relation='classroom_subject_rel',
        column1='name',
        column2='classroom_name')
    
    professor_ids = fields.One2many(comodel_name='university.professor',inverse_name='subject_id')

    student_ids = fields.Many2many(
        comodel_name='university.student',
        relation='student_subject_rel',
        column1='name', 
        column2='f_name')