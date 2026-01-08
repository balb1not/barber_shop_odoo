from odoo import fields, models, api

class BarberScheduling(models.Model):
    _name = 'barber.scheduling'
    _description = 'Scheduling Module'

    name = fields.Char(string='Name')
    customer_id = fields.Many2one('res.partner', string="Client")
    barber_id = fields.Many2one('barber.barber', string="Barber")
    service_ids = fields.Many2many('barber.services', string="Barber Services")
    start_time = fields.Float(string="Start Time")

    total_amount = fields.Float(string='Total Amount', compute='_compute_total_amount', store=True)

    @api.depends('service_ids.price')
    def _compute_total_amount(self):
        for rec in self:
            rec.total_amount = sum(service.price for service in rec.service_ids)
            
    @api.model
    def create(self, vals_list):
        vals_list['name'] = self.env['ir.sequence'].next_by_code('seq.scheduling')
        return super(BarberScheduling, self).create(vals_list)

    