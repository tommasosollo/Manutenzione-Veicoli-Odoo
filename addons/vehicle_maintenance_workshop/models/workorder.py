from odoo import models, fields, api
from odoo.exceptions import ValidationError, UserError


class Workorder(models.Model):
    _name = "vehicle.workorder"
    _description = "Workorders Model"
    _inherit = ['mail.thread']

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
        string="Tipologie Interventi",
        tracking=True
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
        string="Stato",
        tracking=True
    )

    ricambi_usati_ids = fields.One2many(
        "workorder.ricambio",
        "workorder_id",
        string="Ricambi Usati",
        tracking=True
    )

    ore_lavorate = fields.Integer(string="Ore Lavorate", tracking=True)

    fattura_id = fields.Many2one('account.move', string="Fattura Generata", readonly = True)

    cliente_id = fields.Many2one(
        "res.partner",
        string="Cliente",
        related="vehicle_id.proprietario_id",
        store=True
    )


    costo_totale = fields.Float(
        string="Costo Totale",
        compute="_compute_costo_totale"
    )

    @api.depends("ricambi_usati_ids.subtotal", "ore_lavorate")
    def _compute_costo_totale(self):
        # Recupera il prodotto Ore Lavoro
        ore_lavoro_product = self.env['product.product'].search([('name', '=', 'Ore Lavoro')], limit=1)
        costo_manodopera_unitario = ore_lavoro_product.standard_price if ore_lavoro_product else 20 

        for rec in self:
            costo_ricambi = sum(line.subtotal for line in rec.ricambi_usati_ids)
            costo_manodopera = rec.ore_lavorate * costo_manodopera_unitario
            rec.costo_totale = costo_ricambi + costo_manodopera

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

    def action_cancella(self):
        for rec in self:
            rec.stato='cancellato'

    # Crea fattura in automatico
    def action_fatturato(self):
        for rec in self:
            if rec.stato == 'fatturato':
                continue
            
            # Imposta lo stato a fatturato
            rec.stato = 'fatturato'

            # Verifica che ci siano dati da fatturare
            if not rec.ricambi_usati_ids and rec.ore_lavorate == 0:
                raise UserError("Non ci sono ore di lavoro o ricambi da fatturare.")
            
            journal = self.env['account.journal'].search([
                ('type', '=', 'sale'),
                ('company_id', '=', self.env.company.id)
            ], limit=1)

            if not journal:
                self.env['account.journal'].create({
                    'name': 'Vendite',
                    'code': 'VEN',
                    'type': 'sale',
                    'company_id': self.env.company.id,
                })

            # Creo la fattura (account.move)
            invoice_vals = {
                'move_type': 'out_invoice',
                'partner_id': rec.cliente_id.id if rec.cliente_id else False,
                'invoice_origin': rec.reference,
                'invoice_line_ids': [],
            }

            # Linee prodotti (ricambi usati)
            for r in rec.ricambi_usati_ids:
                line_vals = (0, 0, {
                    'product_id': r.product_id.id,
                    'quantity': r.quantita,
                    'price_unit': r.costo,
                    'name': r.product_id.name,
                })
                invoice_vals['invoice_line_ids'].append(line_vals)

            # Linea ore di lavoro
            if rec.ore_lavorate > 0:
                service_product = self.env['product.product'].search([('name', '=', 'Ore Lavoro')], limit=1)
                if not service_product:
                    raise UserError("Creare un prodotto di tipo Servizio chiamato 'Ore Lavoro'.")
                line_vals = (0, 0, {
                    'product_id': service_product.id,
                    'quantity': rec.ore_lavorate,
                    'price_unit': service_product.standard_price, # prezzo a caso, da cambiare possibilmente  
                    'name': service_product.name,
                })
                invoice_vals['invoice_line_ids'].append(line_vals)

            # Creo la fattura
            invoice = self.env['account.move'].create(invoice_vals)

            rec.fattura_id = invoice.id


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

    
    quantita_rimasta = fields.Integer(
        string="Quantità Rimasta",
        compute="_compute_quantita_rimasta",
        store=False
    )

    @api.depends('product_id.quantita_totale', 'quantita', 'product_id.quantita_utilizzata_ids')
    def _compute_quantita_rimasta(self):
        for rec in self:
            used = sum(i.quantita for i in rec.product_id.quantita_utilizzata_ids if i != rec)
            rec.quantita_rimasta = rec.product_id.quantita_totale - used - rec.quantita

            
    
    @api.constrains('quantita')
    def _check_quantita(self):
        for rec in self:
            # compute remaining quantity dynamically
            used = sum(i.quantita for i in rec.product_id.quantita_utilizzata_ids if i != rec)
            remaining = rec.product_id.quantita_totale - used
            if rec.quantita > remaining:
                raise ValidationError(
                    f"Non ci sono abbastanza pezzi in magazzino! Quantità disponibile: {remaining}"
                )
            if rec.quantita < 0:
                raise ValidationError("La quantità non può essere negativa!")

    