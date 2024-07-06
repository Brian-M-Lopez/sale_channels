{
    'name': 'Sale Channel - Calyx',
    'version': '15.0.1.0',
    'summary': 'Sale channels Management for Calyx',
    'description': """
        Sale channels Management for Calyx
    """,
    'category': 'Sales',
    'author': 'Brian Lopez',
    'depends': ['sale_stock', 'account'],
    'data': [
        'security/ir.model.access.csv',
        'data/sale_channel_sequence.xml',
        'views/sale_channel_view.xml',
        'views/sale_order_view.xml',
        'views/stock_picking_view.xml',
        'views/account_move_view.xml',
        'views/credit_group.xml',
        'views/res_partner.xml',
    ],
    'installable': True,
    'auto_install': False,
    'license': 'LGPL-3',
}
