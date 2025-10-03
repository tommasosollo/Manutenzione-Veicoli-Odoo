<h2>Progetto: Gestione Officine di Manutenzione Veicoli</h2>


<h2>Funzionalità principali</h2>


<br>Anagrafica Veicoli</br>


Modello <br>vehicle.vehicle</br> con:

Targa, marca, modello, anno
Proprietario (link a res.partner)
Km attuali, data prossima revisione
Smart button collegati a interventi fatti e fatture.


<br>Gestione Interventi / Ordini di Lavoro</br>


Modello <br>vehicle.workorder</br> con:

Tipo di intervento (tagliando, freni, cambio olio, ecc.)
Stato: bozza → confermato → in corso → completato → fatturato
Ricambi usati (collegamento a prodotti di magazzino)
Ore lavorate (timesheet semplificato)
Collegamento automatico con stock per scalare i ricambi usati.


<br>Piani di Manutenzione Preventiva</br>

Possibilità di schedulare interventi periodici (es. ogni 20.000 km o ogni 12 mesi).
Notifica automatica via email/SMS al cliente.


<br>Integrazione con Magazzino</br>

Ricambi gestiti come prodotti con quantità a magazzino.
Movimenti automatici quando un intervento viene completato.
Avvisi quando un ricambio va sotto la scorta minima.


<br>Fatturazione Automatica</br>

Generazione fattura dal workorder → righe di manodopera + ricambi.

<br>Collegamento a contabilità Odoo standard.</br>

<br>Dashboard e Report</br>

Ore di lavoro per meccanico.
Margine sugli interventi (ricambi + manodopera).
Scadenze prossime revisioni e tagliandi.
KPI su clienti più attivi.

<br>Ruoli di Sicurezza</br>

Capo officina → tutto
Meccanico → vede solo i suoi ordini di lavoro, può inserire ore e ricambi
Amministrazione → fatturazione e contabilità