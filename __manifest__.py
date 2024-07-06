{
    'name': 'Sale Channel - Calyx',
    'version': '15.0.1.0',
    'summary': 'Sale channels Management for Calyx',
    'description': """
        Sale channels Management for Calyx
    """,
    'category': 'Sales',
    'author': 'Brian Lopez',
    'depends': ['stock', 'sale'],
    'data': [
        'security/ir.model.access.csv',
        'data/sale_channel_sequence.xml',
        'views/sale_channel_view.xml',
        'views/sale_order_view.xml',
    ],
    'installable': True,
    'auto_install': False,
    'license': 'LGPL-3',
}
