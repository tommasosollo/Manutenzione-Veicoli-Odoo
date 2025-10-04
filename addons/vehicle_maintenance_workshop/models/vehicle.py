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
    
    data_ultima_revisione = fields.Date(string="Data Ultima Revisione",
                                        default = False,
                                        store = True)

    def _compute_prox_revisione(self):
        if self.data_ultima_revisione:
            retval = self.data_ultima_revisione + timedelta(days=365)
        else:
            retval = fields.Date.today() + timedelta(days=365)
        return retval
    
    data_prox_revisione = fields.Date(string="Data Prossima Revisione",
                                      default = _compute_prox_revisione,
                                      store=True
                                      )
    
    _sql_constraints = [
        ('unique_targa', 'unique(targa)', 'La targa deve essere univoca!')
    ]
    

    # Metodi generali

    def _compute_display_name(self):
        for rec in self:
            rec.display_name = f"[{rec.targa}] {rec.marca} {rec.modello}"