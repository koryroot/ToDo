# -*- coding: utf-8 -*-

from odoo import api, fields, models


class task(models.Model):
    _name = 'task.task'
    _description = 'New Description'

    name = fields.Char(string='Name')
    body = fields.Html(string='Body')
    state = fields.Selection(string='State', selection=[('draft', 'Draft'), ('progress', 'Progress'),('confirmed', 'Confirmed'),('done', 'Done')])
    
    

