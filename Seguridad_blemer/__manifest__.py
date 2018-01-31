# -*- coding: utf-8 -*-
{
    'name': "BLEMER Accesos y Seguridad",

    'summary': """
    Agregar permisos de acceso sobre los modelos de remisones
    """,

    'description': """
        Permisos
    """,

    'author': "Soluciones4g",
    'website': "http://www.soluciones4g.com",

    # Categories can be used to filter modules in modules listing
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base','ventas_blemer'],

    # always loaded
    'data': [
        'security/blemer_grupos.xml',
        'security/ir.model.access.csv',
    ],
    'installable':True,
    'auto_install':False,
}
