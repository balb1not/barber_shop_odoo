# -*- coding: utf-8 -*-

{
    'name': "Barber Shop",
    'summary': " Barber Shop ",
    'description': """ 
        Module to a barbershop appointments 
    """,
    'author': "Frederico",
    'version': '0.1',
    'depends': ['base'],

    'data':[
        'security/ir.model.access.csv',
        'views/appointments_bs_views.xml',
        'views/menu_views.xml'
    ],
}