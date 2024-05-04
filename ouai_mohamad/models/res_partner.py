from odoo import models, fields

class ResPartner(models.Model):
    _inherit = 'res.partner'

    emails = fields.Many2many('res.partner.email', string="Emails")
    mobiles = fields.Many2many('res.partner.mobile', string="Mobiles")

class ResPartnerEmail(models.Model):
    _name = 'res.partner.email'

    name = fields.Char(string="Email")

class ResPartnerMobile(models.Model):
    _name = 'res.partner.mobile'

    name = fields.Char(string="Mobile")
