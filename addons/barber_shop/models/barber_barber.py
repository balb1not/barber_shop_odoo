from odoo import fields,models


class BarberBarber(models.Model):

    _name = "barber.barber"
    _description = "Module related to the barbers of the barber shop."

    name = fields.Char(string='Name')
    active = fields.Boolean(string="Active",default=True)

    