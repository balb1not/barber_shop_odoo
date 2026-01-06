from odoo import fields, models

class MainBarberShop(models.Model):
    _name = 'main.barber.shop'
    _description = 'Main Barber Shop'

    name = fields.Char(string='Name')
