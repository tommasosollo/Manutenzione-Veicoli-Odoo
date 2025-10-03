<h2>Progetto: Gestione Officine di Manutenzione Veicoli</h2>


<h2>Funzionalità principali</h2>


<h4>Anagrafica Veicoli</h4>


Modello <b>vehicle.vehicle</b> con:

Targa, marca, modello, anno
Proprietario (link a res.partner)
Km attuali, data prossima revisione
Smart h4utton collegati a interventi fatti e fatture.


<h4>Gestione Interventi / Ordini di Lavoro</h4>


Modello <b>vehicle.workorder</b> con:

Tipo di intervento (tagliando, freni, cambio olio, ecc.)
Stato: bozza → confermato → in corso → completato → fatturato
Ricambi usati (collegamento a prodotti di magazzino)
Ore lavorate (timesheet semplificato)
Collegamento automatico con stock per scalare i ricambi usati.


<h4>Piani di Manutenzione Preventiva</h4>

Possibilità di schedulare interventi periodici (es. ogni 20.000 km o ogni 12 mesi).
Notifica automatica via email/SMS al cliente.


<h4>Integrazione con Magazzino</h4>

Ricambi gestiti come prodotti con quantità a magazzino.
Movimenti automatici quando un intervento viene completato.
Avvisi quando un ricambio va sotto la scorta minima.


<h4>Fatturazione Automatica</h4>

Generazione fattura dal workorder → righe di manodopera + ricambi.

<h4>Collegamento a contabilità Odoo standard.</h4>

<h4>Dashboard e Report</h4>

Ore di lavoro per meccanico.
Margine sugli interventi (ricambi + manodopera).
Scadenze prossime revisioni e tagliandi.
KPI su clienti più attivi.

<h4>Ruoli di Sicurezza</h4>

Capo officina → tutto
Meccanico → vede solo i suoi ordini di lavoro, può inserire ore e ricambi
Amministrazione → fatturazione e contabilità