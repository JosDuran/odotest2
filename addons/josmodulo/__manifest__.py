{
    'name': "My Modulo",
    'version': '15.0.4.0.0',
    'sequence': 1,

    'description': """
        Módulo CRM para la gestión de registro...
    """,

    'author': "Odoo",
    'website': "http://odoo.com",
    
    'category': 'Escuela de Conduccion',
    'license': 'LGPL-3',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'views/views.xml',
    ],
}