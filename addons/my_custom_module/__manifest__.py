{
    'name': 'My Custom Module',
    'version': '1.0',
    'depends': ['base'],
    'data': [
        'security/ir.model.access.csv',
        'views/order_views.xml',
        'views/item_views.xml',
    ],
    'installable': True,
    'application': True,
}