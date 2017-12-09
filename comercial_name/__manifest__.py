# -*- coding: utf-8 -*-
{
    'name': "Agregar nombre comercial",

    'summary': """
    Agregar nombre comercial a los clientes
    """,

    'description': """
        Agregar campo relacionado con la razon social
    """,

    'author': "Soluciones4g",
    'website': "http://www.soluciones4g.com",

    # Categories can be used to filter modules in modules listing
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        'views/add_comercial_name_view.xml',
    ],
    'installable':True,
    'auto_install':False,
}
