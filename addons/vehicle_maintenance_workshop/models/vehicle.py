from odoo import models, fields, api
from datetime import timedelta, datetime

class Vehicle(models.Model):

    _name = "vehicle.vehicle"
    _description = "Vehicle Model"

    targa = fields.Char(string="Targa", required=True, )

    marca = fields.Char(string="Marca", required=True)

    modello = fields.Char(string="Modello", required=True)

    anno = fields.Char(
            string='Anno Immatricolazione',
            default=lambda self: datetime.now().year,
            required=True
        )
    
    proprietario_id = fields.Many2one(
        "res.partner", 
        string="Propritario Veicolo",
        help="Collegamento al proprietario da res.partner",
        required=True
        )
    
    km_attuali = fields.Integer(string="Chilometri",
                                required=True)

    data_prox_revisione = fields.Date(string="Data Prossima Revisione",
                                      default= lambda self: fields.Date.today() + timedelta(days=365),
                                      store=True
                                      )

    _sql_constraints = [
        ('unique_targa', 'unique(targa)', 'La targa deve essere univoca!')
    ]
    