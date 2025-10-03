<h2>Progetto: Gestione Officine di Manutenzione Veicoli</h2>


<h2>Funzionalità principali</h2>


<h3>Anagrafica Veicoli</h3>


Modello <b>vehicle.vehicle</b> con: <br>

Targa, marca, modello, anno <br>
Proprietario (link a res.partner) <br>
Km attuali, data prossima revisione <br>
Smart h3utton collegati a interventi fatti e fatture. <br>


<h3>Gestione Interventi / Ordini di Lavoro</h3>


Modello <b>vehicle.workorder</b> con: <br>

Tipo di intervento (tagliando, freni, cambio olio, ecc.) <br>
Stato: bozza → confermato → in corso → completato → fatturato <br>
Ricambi usati (collegamento a prodotti di magazzino) <br>
Ore lavorate (timesheet semplificato) <br>
Collegamento automatico con stock per scalare i ricambi usati. <br>


<h3>Piani di Manutenzione Preventiva</h3>

Possibilità di schedulare interventi periodici (es. ogni 20.000 km o ogni 12 mesi). <br>
Notifica automatica via email/SMS al cliente. <br>


<h3>Integrazione con Magazzino</h3>

Ricambi gestiti come prodotti con quantità a magazzino. <br>
Movimenti automatici quando un intervento viene completato. <br>
Avvisi quando un ricambio va sotto la scorta minima. <br>


<h3>Fatturazione Automatica</h3>

Generazione fattura dal workorder → righe di manodopera + ricambi. <br>

<h3>Collegamento a contabilità Odoo standard.</h3>

<h3>Dashboard e Report</h3>

Ore di lavoro per meccanico. <br>
Margine sugli interventi (ricambi + manodopera). <br>
Scadenze prossime revisioni e tagliandi. <br>
KPI su clienti più attivi. <br>

<h3>Ruoli di Sicurezza</h3>

Capo officina → tutto <br>
Meccanico → vede solo i suoi ordini di lavoro, può inserire ore e ricambi <br>
Amministrazione → fatturazione e contabilità <br>