# Python project about the wealth of nations
## Project proposal:
Dive into the intricate relationship between a country's economic prosperity and the well-being of its population. 
This project invites you to explore decades of global development data to uncover trends and correlations. 
You could analyze how indicators like GDP per capita relate to life expectancy, healthcare spending, or child mortality rates. 
Create compelling visualizations, such as time-series charts or global maps, to tell a story about global health and economics. 
The goal is to build an analytical project that reveals patterns in how nations thrive. 

## Indice:
1. Introduzione
2. Dati
3. Installazione
4. Analisi

## Introduzione
Il progetto analizza la relazione complessa tra la prosperità economica e il benessere della popolazione di alcuni paesi del mondo. 
Analizzando l'evoluzione dei dati attraverso gli ultimi anni per individuare tendenze e correlazioni significative.
L’obiettivo principale è capire come indicatori economici, come il PIL pro capite, siano associati a misure fondamentali di salute pubblica, tra cui l’aspettativa di vita, la spesa sanitaria e i tassi di mortalità infantile.
Infine verranno create visualizzazioni efficaci — come grafici temporali o mappe globali — per capire meglio il legame tra economia e salute nel mondo.
In sintesi, l’obiettivo è costruire un’analisi che metta in luce i modelli attraverso cui le nazioni prosperano.
Per svolgere il progetto, infine, è stato utilizzato Visual Studio Code (VS Code). Per questo motivo i codici e le spiegazioni fornite in questo file sono stati fatti in base alle funzionalità di questo software.

## Dati
I dati utilizzati nel progetto provengono dalla libreria Python 'wbgapi'. La libreria è costruita attraverso i dati della World Bank Open Data, ovvero una banca dati che mette a disposizione in modo gratuito alcuni dati riguardanti lo sviluppo globale.
Per utilizzare questa libreria, prima di utilizzare gli script del progetto, bisogna installarla attraverso il terminale di VS Code attraverso il seguente codice:
`python -m pip install wbgapi`.

Come detto prima 'wbgapi' è una libreria Python che permette di accedere in modo semplice e strutturato ai dati della World Bank.
Consente di scaricare indicatori economici, sociali e ambientali, esplorare metadati e organizzare i dati in DataFrame di Pandas per analisi e visualizzazioni.
È particolarmente utile per progetti di analisi dei dati globali e sviluppo internazionale, come in questo caso.

Per questo motivo all'interno della libreria troviamo un'ampia quantità di dati. 
Per limitare le analisi sono stati selezionati solo alcuni di esse, in base al luogo, al tempo e agli indicatori disponibili:
* Non utilizzo quindi tutti i paesi disponibili ma ne scelgo 10 diversi per livello di sviluppo economico, distribuiti in più aree geografiche e rappresentativi di modelli econdomici e sociali differenti:
  - Europa: Italia (ITA), Spagna (ESP), Germania (DEU), Svezia (SWE)
  - Nord America: Stati uniti (USA), Canada (CAN)
  - Sud America: Brasile (BRA), Cile (CHL)
  - Africa: Sudafica (ZAF), Nigeria (NGA)
* Prendo in analisi i dati dal 1995 al 2024 perchè i dati dei 2025 non sono ancora stati caricati. Ho un arco temporale di circa 30 anni che mi fa capire come sono cambiati gli indicatori scelti negli anni.
* Indicatori selezionati per le analisi:
  - 'GDP per capita': 'NY.GDP.PCAP.CD' --> ricchezza media per persona
  - 'GDP': 'NY.GDP.MKTP.CD' --> ricchezza totale di un paese
  - 'Life expectancy': 'SP.DYN.LE00.IN' --> media di anni di vita alla nascita
  - 'Health expenditure': 'SH.XPD.CHEX.PC.CD' --> spesa sanitaria per persona
  - 'Infant mortality': 'SH.DYN.MORT' --> tasso di mortalità infantile per 1000 nati vivi 
  - 'Unemployment': 'SL.UEM.TOTL.ZS' --> percentuale forza lavoro disoccupata
  - 'Population growth': 'SP.POP.GROW' --> percentuale di crescita annuale

## Installazione dati
Per installare i file, con all'interno i dati utilizzati, il primo codice da visionare è all'interno della cartella 'download data', separata dal resto degli script così non vengono scaricati troppi file csv all'interno della repository di GitHub.
Il primo codice utilizzato è 'data loader', codice che scarica i dati dalla libreria 'wbgapi' e li esporta in 7 file CSV divisi in base ai 7 indici selezionati. I dati sono strutturati con i paesi come colonne e gli anni come righe, e ovviamente i dati all'interno indicano il dato di quel determinato indicatore in quell'anno e in quel paese..
Purtroppo, l'idea iniziale era in un unico dataset tutti i dati di tutti gli indicatori ma questo non è stato possibile perchè i dati risulterebbero troppi e il codice genera errore.
Facedo partire il codice 'data_loader', quindi, si creano 7 file csv per i 7 indicatori con all'interno i dati dei 10 paesi e dei 30 anni considerati.

Prima di passare alle analisi vere e proprie faccio partire il codice 'preprocessing' con al suo interno analisi generali dei singoli dataset e il preprocesso per organizzare i dati in modo che possano essere utilizzati per le analisi successive.
Con questo processo notiamo che:
- Il dataset 'Life expectacy' ha 1 riga con valori mancanti: non ci sono valori per il 2024 quindi elimino questo anno in questo dataset.
- Il dataset 'Health expenditure' ha 7 righe con all'interno valori mancanti: non ci sono i valori dal 1995 al 1999 e del 2024, invece i valori del 2023 ci sono solo per alcuni paesi (5 su 10). Le 6 righe senza dati le elimino, invece per il 2023 capisco se ha senso tenerlo. Alla fine elimino anche il 2023 perchè per le analisi che andrò a svolgere non ha senso tentare un imputazione dei valori mancanti.
- Il dataset 'Infant mortality' ha 1 riga con valori mancanti: non ci sono valori per il 2024 quindi elimino questo anno in questo dataset.

Quindi i 3 dataset con valori nulli sono stati sistemati per le analisi future. Questi dataset vengono scaricati nella nuova versione in formato CSV. Per comodità la versione precedente di questi dati vengono elimiti dalla cartella 'data'.

## Analisi 
L’obiettivo di questo progetto è, quindi, esplorare la relazione tra ricchezza economica e benessere sociale, analizzando la storia della salute e dell’economia a livello globale.
Attraverso lo studio di tendenze e correlazioni dello sviluppo globale in tutti i Paesi selezionati, il progetto mira a identificare i principali modelli di sviluppo delle nazioni.
Le analisi comprendono correlazioni, trend temporali e confronti geografici, tutte implementate all’interno di funzioni nella cartella 'script'.
Per ottenere i risultati e visualizzare l’output, è necessario eseguire il codice Python principale contenuto nel file 'main.py', che si trova al di fuori della cartella 'script'.
In sintesi, si tratta di un progetto di data analysis socio-economica volto a comprendere come l’economia influenzi il benessere delle popolazioni nel tempo e nello spazio.

Le analisi svolte sono:
* Temporali:
  - Pil pro capite nel tempo
  - Aspettativa di vita nel tempo
  - Disoccupazione nel tempo
  - Mortalità infantile nel tempo
  - Confronto pre e post crisi economica del 2008: pil pro capite medio, aspettativa di vita, disoccupazione e mortalità infantile suddivisi in 2000-2007 e 2009-2019
* Correlazioni:
  - Pil pro capite vs aspettativa di vita
  - Disoccupazione vs aspettativa di vita
  - Pil pro capite vs spesa sanitaria pro capite
  - Pil pro capite vs tassi di mortalità infantile
  - Spesa sanitaria pro capite vs mortalità infantile
  - Cambia nel tempo questa correlazione? serie temporale dei paesi
* Regressione lineare: per vedere quanto influiscono le variabili GDP_per_capita, Health_expenditure e Infant_mortality, sulla variabile Life_expectancy. L'output è composto dai coefficienti di regressione e il grafico scatter plot della regressione
* Creazione di un indice sintetico di benessere che riassume tutti gli indici di benessere (aspettativa di vita, spesa sanitaria, mortalità infantile)
* Cluster analisis: raggruppa i paesi in base ai loro indicatori economici e sanitari
* Visualizzazioni globali:
  - Grafici vari:
    - Andamento nel tempo dei vari indicatori per paese e
    - Andamente nel tempo dei vari indicatori per continente)
  - Mappa mondiale che rappresenta la crescita annuale
  - Mappa mondiale che rappresenta il pil generale
  - Mappa mondiale che rappresenta l'aspettativa di vita


