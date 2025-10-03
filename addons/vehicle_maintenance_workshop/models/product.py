from odoo import models, fields, api

class ProductProduct(models.Model):
    _inherit = "product.product"  # eredita il modello esistente

    
    quantita_totale = fields.Integer(string="Quantita Totale", default = 0)
    
    quantita_rimasta = fields.Integer(string="Quantità Rimasta", compute="_compute_quantita_rimasta", store=False)

    quantita_utilizzata_ids = fields.One2many(
        "workorder.ricambio",
        "product_id",
        string="Quantita Utilizzata"
    )

    @api.depends("quantita_utilizzata_ids.quantita")
    def _compute_quantita_rimasta(self):
        for rec in self:
            rec.quantita_rimasta = rec.quantita_totale - sum(i.quantita for i in rec.quantita_utilizzata_ids)