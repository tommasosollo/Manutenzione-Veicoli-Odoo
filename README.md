<h2>Progetto: Gestione Officine di Manutenzione Veicoli</h2>


<h2>Funzionalità principali</h2>


<h3>Anagrafica Veicoli</h3>


Modello <b>vehicle.vehicle</b> con:

Targa, marca, modello, anno 

Proprietario (link a res.partner)
Km attuali, data prossima revisione
Smart h3utton collegati a interventi fatti e fatture.


<h3>Gestione Interventi / Ordini di Lavoro</h3>


Modello <b>vehicle.workorder</b> con:

Tipo di intervento (tagliando, freni, cambio olio, ecc.)
Stato: bozza → confermato → in corso → completato → fatturato
Ricambi usati (collegamento a prodotti di magazzino)
Ore lavorate (timesheet semplificato)
Collegamento automatico con stock per scalare i ricambi usati.


<h3>Piani di Manutenzione Preventiva</h3>

Possibilità di schedulare interventi periodici (es. ogni 20.000 km o ogni 12 mesi).
Notifica automatica via email/SMS al cliente.


<h3>Integrazione con Magazzino</h3>

Ricambi gestiti come prodotti con quantità a magazzino.
Movimenti automatici quando un intervento viene completato.
Avvisi quando un ricambio va sotto la scorta minima.


<h3>Fatturazione Automatica</h3>

Generazione fattura dal workorder → righe di manodopera + ricambi.

<h3>Collegamento a contabilità Odoo standard.</h3>

<h3>Dashboard e Report</h3>

Ore di lavoro per meccanico.
Margine sugli interventi (ricambi + manodopera).
Scadenze prossime revisioni e tagliandi.
KPI su clienti più attivi.

<h3>Ruoli di Sicurezza</h3>

Capo officina → tutto
Meccanico → vede solo i suoi ordini di lavoro, può inserire ore e ricambi
Amministrazione → fatturazione e contabilità