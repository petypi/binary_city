# -*- coding: utf-8 -*-
import re
from odoo import api, fields, models, _
from odoo.exceptions import UserError

class BinaryCityClient(models.Model):
    _name = "binary.city.client"
    _description = "Binary City"
    _inherit = ["mail.thread", "mail.activity.mixin"]
    _order = 'priority desc, id desc'

    code = fields.Char("Code")
    name = fields.Char("Name", required=True)
    num_contacts = fields.Integer("Number of Contacts",required=True)
    priority = fields.Integer("Priority")
    contacts_ids = fields.One2many("binary.city.contact","client_id", string="Contact",required=True)

    @api.model
    def create(self, vals):
        vals['name'] = self.env['ir.sequence'].next_by_code('client.seq')
        return super(BinaryCityClient, self).create(vals)





class BinarycityContacts(models.Model):
    _name = "binary.city.contact"
    _description = "Binary City"
    _inherit = ["mail.thread", "mail.activity.mixin"]
    _order = 'priority desc, id desc'
    
    surname = fields.Char("Surname",required=True)
    name = fields.Char("Name",required=True)
    email_id = fields.Char("Email Address")
    num_clients_linked = fields.Integer("Number of Clients Linked",required=True)
    priority = fields.Integer("Priority")
    client_id = fields.Many2one("binary.city.client", string="Client")

    @api.onchange('email_id')
    def validate_mail(self):
        if self.email_id:
            match = re.match('^[_a-z0-9-]+(\.[_a-z0-9-]+)*@[a-z0-9-]+(\.[a-z0-9-]+)*(\.[a-z]{2,4})$', self.email_id)
            if match == None:
                raise UserError('Not a valid E-mail ID')