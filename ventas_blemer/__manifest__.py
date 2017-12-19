# -*- coding: utf-8 -*-
{
    'name': "Remisiones Blemer",

    'summary': """
        Generación de remisiones
        """,

    'description': """
        Modulo para las remisiones de blemer
    """,

    'author': "Soluciones4g",
    'website': "http://www.soluciones4g.com",

    'category': 'Uncategorized',
    'version': '0.1',

    'depends': ['base', 'product', 'stock', 'sale', 'mail', 'fleet'],

    'data': [
        'views/definicion_remisiones_view.xml',
        'views/datosextras_vehiculos_view.xml',
        'views/datosextras_clientes_view.xml',
        'views/sale_order_inherit.xml',
        #'views/plantilla_remision.xml',
        #'views/remision_vista.xml',
    ],
    'installable': True,
    'auto_install': False,
}
