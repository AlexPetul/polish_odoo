# -*- encoding: utf-8 -*-

{
    'name': 'PolishTest',
    'version': '1.0',
    'category': 'Tools',
    'summary': 'Base utils.',
    'description': """
               Test module.
    """,
    'depends': ['base'],
    'data': [
        'security/ir.model.access.csv',
        'views/polish_test_views.xml',
    ],
    'installable': True,
}
