from odoo import fields, models

class BarberAppointments(models.Model):
    _name = 'barber.appointments'
    _description = 'Main Barber Shop'

    name = fields.Char(string='Name')
