from odoo import fields,models

class BarberServices(models.Model):
    _name = 'barber.services'
    _description = 'Barber Services'

    
    name = fields.Char(string='Service Name')
    price = fields.Float(string='Price', digits=(10, 2))
    duration = fields.Float(string='Duration')