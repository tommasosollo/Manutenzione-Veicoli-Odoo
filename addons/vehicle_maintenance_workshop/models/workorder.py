from odoo import models, fields, api


class Workorder(models.Model):
    _name = "vehicle.workorder"
    _description = "Workorders Model"

    reference = fields.Char(string="N. Intervento", default="New")

    vehicle_id = fields.Many2one(
        "vehicle.vehicle",
        string = "Veicolo",
        required=True
    )

    tipo_intervento_ids = fields.Many2many(
        "vehicle.workorder.type",
        "rel_vehicle_workorder_type",
        "workorder_id",
        "workorder_type_id",
        string="Tipologie Interventi"
    )

    stato = fields.Selection(
        [
            ("bozza", "Bozza"),
            ("confermato", "Confermato"),
            ("in_corso", "In Corso"),
            ("completato", "Completato"),
            ("fatturato", "Fatturato"),
            ("cancellato", "Cancellato")
        ],
        default="bozza",
        string="Stato"
    )

    ricambi_usati_ids = fields.One2many(
        "workorder.ricambio",
        "workorder_id",
        string="Ricambi Usati"
    )

    ore_lavorate = fields.Integer(string="Ore Lavorate")

    costo_totale = fields.Float(
        string="Costo Totale",
        compute="_compute_costo_totale"
    )

    @api.depends("ricambi_usati_ids.subtotal")
    def _compute_costo_totale(self):
        for rec in self:
            rec.costo_totale = sum(line.subtotal for line in rec.ricambi_usati_ids) + rec.ore_lavorate * 20 # estrarre costo manodopera

    # Metodi generali

    @api.model_create_multi
    def create(self, vals_list):
        for vals in vals_list:
            if not vals.get('reference') or vals['reference'] == 'New':
                vals['reference'] = self.env['ir.sequence'].next_by_code('vehicle.workorder')
        return super().create(vals_list)

    def _compute_display_name(self):
        for rec in self:
            rec.display_name = f"[{rec.reference}] {rec.vehicle_id.targa}"

    def action_conferma(self):
        for rec in self:
            rec.stato='confermato'

    def action_in_corso(self):
        for rec in self:
            rec.stato='in_corso'

    def action_completato(self):
        for rec in self:
            rec.stato='completato'

    def action_fatturato(self):
        for rec in self:
            rec.stato='fatturato'

    def action_cancella(self):
        for rec in self:
            rec.stato='cancellato'


class WorkorderRicambio(models.Model):
    _name = "workorder.ricambio"
    _description = "Ricambi Usati in Workorder"

    workorder_id = fields.Many2one("vehicle.workorder", required=True, ondelete="cascade", string="Intervento")
    product_id = fields.Many2one("product.product", string="Prodotto", required=True)
    quantita = fields.Integer(string="Quantità", default=1)

    costo = fields.Float(
        string="Costo Unitario",
        related="product_id.standard_price",
        store=True,
        readonly=False  # così lo puoi modificare se serve
    )

    subtotal = fields.Float(
        string="Totale Riga",
        compute="_compute_subtotal",
        store=True
    )

    @api.depends("costo", "quantita")
    def _compute_subtotal(self):
        for rec in self:
            rec.subtotal = rec.costo * rec.quantita