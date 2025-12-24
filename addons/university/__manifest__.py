# -*- coding: utf-8 -*-
{
    'name': 'University',
    'version': '1.0',
    'summary': 'University summary',
    'description': 'Longer University description',
    'license': 'LGPL-3',
    'author': 'Abk',
    'category': 'Project management',
    'depends': ['base'],
    'data': [
        'views/student_views.xml',
        'views/professor_views.xml',
        'views/department_views.xml',
        'views/subject_views.xml',
        'views/classroom_views.xml',

       

        # Add for access control for the defined models
        'security/ir.model.access.csv',
    ],
    'assets': {
        'web.assets_frontend': [
            # CSS files
            # 'hustle_website/static/src/css/global.css',

            # JS files
            # 'hustle_website/static/src/js/counter.js',
        ],
    },
    'installable': True,
    'application': True,
}