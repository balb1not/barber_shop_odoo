# -*- coding: utf-8 -*-

{
    'name': "Barber Shop",
    'summary': " Barber Shop ",
    'description': """ 
        Module to a barbershop appointments 
    """,
    'author': "Frederico",
    'version': '0.1',
    'depends': ['base', 'muk_web_theme'],

    'data':[
        'security/ir.model.access.csv',
        'views/barber_scheduling_views.xml',
        'views/barber_services_views.xml',
        'views/barber_barber.xml',
        'views/menu_views.xml'
    ],
}