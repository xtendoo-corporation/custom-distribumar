# -*- coding: utf-8 -*-
{
    'name': 'Purchase pending received',
    'version': '15.0.1.0.0',
    'category': 'Tools',
    'summary': 'Purchase pending received',
    'description': '''
    Purchase pending received
''',
    'license': 'AGPL-3',
    'author': 'Xtendoo',
    'depends': [
        'purchase',
        'purchase_reception_status',
    ],
    'data': [
        'views/sale_order_views.xml',
    ],
    'application': True,
}
