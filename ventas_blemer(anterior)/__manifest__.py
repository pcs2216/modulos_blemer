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

    # Categories can be used to filter modules in modules listing
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base','product','stock','sale','mail','fleet'],

    # always loaded
    'data': [
        'views/definicion_remisiones_view.xml',
        'views/datosextras_vehiculos_view.xml',
        'views/datosextras_clientes_view.xml',
    ],
    'installable':True,
    'auto_install':False,
}
