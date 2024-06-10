# Documentazione del progetto Tris

## Introduzione
Il progetto Tris è un'implementazione del gioco del Tris (o Tic Tac Toe) in Python utilizzando la libreria grafica Tkinter per la realizzazione di un'interfaccia utente (GUI). Il gioco può essere giocato sia contro un avversario umano che contro un'intelligenza artificiale (IA).

## Struttura del progetto
Il progetto è diviso in due file principali:

- **tris_GUI.py**: Questo file contiene il codice per l'interfaccia utente del gioco. Utilizza la libreria Tkinter per creare una finestra di gioco interattiva dove l'utente può giocare contro l'IA.
- **tris_logic_AI.py**: Questo file contiene la logica di gioco e l'algoritmo utilizzato dall'IA per prendere decisioni.

## Moduli e classi

### Modulo tris_GUI.py

#### TrisGUI
Questa classe gestisce l'interfaccia grafica del gioco. Si occupa di inizializzare la finestra di gioco, gestire i click sui pulsanti e aggiornare la GUI in base alle mosse effettuate dai giocatori.

### Modulo tris_logic_AI.py

#### Tris
Questa classe gestisce la logica del gioco. Si occupa di tenere traccia dello stato della tavola di gioco, determinare il vincitore e verificare la validità delle mosse.

#### AIPlayer
Questa classe rappresenta l'IA del gioco. Utilizza l'algoritmo Minimax con potatura alfa-beta per prendere decisioni sulle mosse migliori da effettuare.

#### HumanPlayer
Questa classe rappresenta il giocatore umano. Permette all'utente di inserire la propria mossa tramite input da tastiera.

## Algoritmo Minimax con potatura alfa-beta
L'IA utilizza l'algoritmo Minimax con potatura alfa-beta per decidere la mossa migliore da effettuare. L'algoritmo esplora l'albero delle possibili mosse fino a una certa profondità, valutando ogni mossa possibile e cercando di massimizzare il suo punteggio mentre minimizza quello dell'avversario. La potatura alfa-beta aiuta a ridurre il numero di rami dell'albero esplorati, migliorando le prestazioni dell'algoritmo.

## Utilizzo
Per giocare al Tris, eseguire il modulo `tris_GUI.py`. Si aprirà una finestra di gioco dove è possibile selezionare le mosse cliccando sui pulsanti. Il gioco può essere giocato sia contro un avversario umano che contro l'IA.

## Esecuzione del gioco
Per avviare una partita predefinita tra un giocatore umano e l'IA, eseguire il modulo `tris_logic_AI.py`. Verrà stampata la tavola di gioco e l'utente sarà invitato a inserire la propria mossa tramite input da tastiera.

## Conclusioni
Il progetto Tris offre un'implementazione completa del classico gioco del Tris in Python, con la possibilità di giocare contro un avversario umano o contro un'intelligenza artificiale. Utilizzando un approccio modulare, il progetto è organizzato in modo efficiente e offre una buona base per ulteriori sviluppi e personalizzazioni.
