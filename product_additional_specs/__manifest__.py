# -*- coding: utf-8 -*-
{
    'name': 'Product Additional Specs',
    'version': '15.0.1.0.0',
    'category': 'Tools',
    'summary': 'Product additional specs',
    'description': '''
    Product additional specs
''',
    'license': 'AGPL-3',
    'author': 'Xtendoo',
    'depends': [
        'product',
        'mail',
    ],
    'data': [
        'security/security.xml',
        'security/ir.model.access.csv',
        'views/product_template_view.xml',
    ],
    'application': True,
}
