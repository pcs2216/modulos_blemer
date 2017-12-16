# -*- coding: utf-8 -*-
{
    'name': "Plantilla para envío de email Blemer",

    'summary': """
        Envío de email
        """,

    'description': """
        Modulo para envíar remisiones via correo electronico
    """,

    'author': "Soluciones4g",
    'website': "http://www.soluciones4g.com",

    # Categories can be used to filter modules in modules listing
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base','mail', 'ventas_blemer'],

    # always loaded
    'data': [
        'views/reporte_remison.xml',
        #'views/reporte_remison2.xml',
        'views/plantilla_remision.xml',
        'views/remision_vista.xml',
        #'views/blemer_automated_action.xml',        
        #'views/definicion_remisiones_view.xml',
    ],
    'installable': True,
    'auto_install': False,
}
