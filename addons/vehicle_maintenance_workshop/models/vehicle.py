from odoo import models, fields, api
from datetime import datetime

class Vehicle(models.Model):

    _name = "vehicle.vehicle"
    _description = "Vehicle Model"

    targa = fields.Char(string="Targa", required=True)

    marca = fields.Char(string="Marca", required=True)

    modello = fields.Char(string="Modello", required=True)

    anno = fields.Char(
            string='Anno Immatricolazione',
            default=lambda self: datetime.now().year,
            required=True
        )
    
    proprietario_id = fields.Many2One(
        "res.partner", 
        string="Propritario Veicolo",
        help="Collegamento al proprietario da res.partner",
        required=True
        )
    
    km_attuali = fields.Integer(string="Chilometri",
                                required=True)

    data_prox_revisione = fields.Date(string="Data Prossima Revisione",
                                      default="_compute_prox_revisione")
    
    def _compute_prox_revisione(self):
        # usare piani di manutenzione preventiva per calcolare prox revisione
        pass
    