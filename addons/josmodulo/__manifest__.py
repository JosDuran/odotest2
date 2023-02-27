# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.
{
    'name' : 'Demo Module',
    'version' : '1.2',
    'summary': 'Digitalchina Demo Module',
    'sequence': -100,
    'description': """DEMO Module""",
    'category': 'Productivity/Demo',
    'website': 'https://www.digitalchina.com',
    'images' : [],
    'depends' : ['sale'],
    'data': [
        'security/ir.model.access.csv',
        'views/foo.xml',
        'views/sale.xml',
    ],
    'demo': [],
    'qweb': [],
    'installable': True,
    'application': True,
    'auto_install': False
}
