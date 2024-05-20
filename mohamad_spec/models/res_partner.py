from odoo import models, fields , api
import random
import logging
logger = logging.getLogger()
class ResPartner(models.Model):
    _inherit = 'res.partner'

    emails = fields.Many2many('res.partner.email', string="Emails", store=True)
    mobiles = fields.Many2many('res.partner.mobile', string="Mobiles", store=True)
    regions = fields.Many2many('res.partner.region', string="Regions", store=True)

class ResPartnerEmail(models.Model):
    _name = 'res.partner.email'
    name = fields.Char(string="Email")
    color = fields.Integer(string="Color")
    @api.model
    def create(self, vals):
        if 'color' not in vals:
            vals['color'] = random.randint(1, 11) 
        return super(ResPartnerEmail, self).create(vals)

class ResPartnerMobile(models.Model):
    _name = 'res.partner.mobile'
    name = fields.Char(string="Mobile")
    color = fields.Integer(string="Color")
    # donner un couleur au hasard pour chaque region
    @api.model
    def create(self, vals):
        if 'color' not in vals:
            vals['color'] = random.randint(1, 11) 
        return super(ResPartnerMobile, self).create(vals)

class ResPartnerregion(models.Model):
    _name = 'res.partner.region'
    name = fields.Char(string="region")
    color = fields.Integer(string="Color")
    # donner un couleur au hasard pour chaque region
    @api.model
    def create(self, vals):
        if 'color' not in vals:
            vals['color'] = random.randint(1, 11) 
        return super(ResPartnerregion, self).create(vals)