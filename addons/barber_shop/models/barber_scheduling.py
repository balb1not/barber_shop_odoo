from odoo import fields, models

class BarberScheduling(models.Model):
    _name = 'barber.scheduling'
    _description = 'Scheduling Module'

    name = fields.Char(string='Name')
    customer_id = fields.Many2one('res.partner', string="Client")
    barber_id = fields.Many2one('barber.barber', string="Barber")
    service_ids = fields.Many2many('barber.services', string="Barber Services")
    start_time = fields.Float(string="Start Time")