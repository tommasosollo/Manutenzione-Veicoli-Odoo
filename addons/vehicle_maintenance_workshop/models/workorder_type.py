from odoo import models, fields, api


class Workorder(models.Model):
    _name = "vehicle.workorder.type"
    _description = "Workorder Types Model"

    name = fields.Char(string="Nome")
    