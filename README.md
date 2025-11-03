# Python project about the wealth of nations
## Project proposal:
Dive into the intricate relationship between a country's economic prosperity and the well-being of its population. 
This project invites you to explore decades of global development data to uncover trends and correlations. 
You could analyze how indicators like GDP per capita relate to life expectancy, healthcare spending, or child mortality rates. 
Create compelling visualizations, such as time-series charts or global maps, to tell a story about global health and economics. 
The goal is to build an analytical project that reveals patterns in how nations thrive. 

come installare:
python -m pip install wbgapi --> nel terminale: ci serve la libreria wbgabi dove all'interno ci sono i dati
importi la libreria nel codice data_loader
come leggo i dati?
la libreria wbgabi è costruita attraverso i dati della World Bank Open Data: Free and open access to global development data
libreria con vari dataset... come ci accedo? 
bisogna decidere quali paesi e quali indicatori voglio perchè se no sono troppi e i paesi più piccoli potrebbero non avere tutti i dati disponibili.

Dati selezionati:
Non utilizzo quindi tutti i paesi disponibili ma ne scelgo 10 diversi per livello di sviluppo economico, distribuiti in più aree geografiche e rappresentativi di modelli econdomici e sociali differenti:
-Europa: Italia (ITA), Spagna (ESP), Germania (DEU), Svezia (SWE)
-Nord America: Stati uniti (USA), Canada (CAN)
-Sud America: Brasile (BRA), Cile (CHL)
-Africa: Sudafica (ZAF), Nigeria (NGA)

prendo in analisi i dati dal 1995 al 2024 perchè i dati dei 2025 non sono ancora stati caricati. Ho un arco temporale di 30 anni che mi fa capire come sono cambiati gli indicatori scelti negli anni.

indicatori scaricati per le analisi:
-'GDP per capita': 'NY.GDP.PCAP.CD' --> ricchezza media per persona
-'GDP': 'NY.GDP.MKTP.CD' --> ricchezza totale di un paese
-'Life expectancy': 'SP.DYN.LE00.IN' --> media di anni di vita alla nascita
-'Health expenditure': 'SH.XPD.CHEX.PC.CD' --> spesa sanitaria per persona
-'Infant mortality': 'SH.DYN.MORT' --> tasso di mortalità infantile per 1000 nati vivi 
-'Unemployment': 'SL.UEM.TOTL.ZS' --> percentuale forza lavoro disoccupata
-'Population growth': 'SP.POP.GROW' --> percentuale di crescita annuale 

purtroppo non posso caricare in un unico dataset tutti i dati di tutti gli indicatori perchè i dati risulterebbero troppi e il codice non parte.
Facedo partire il codice data_loader si creano 7 file csv per i 7 indicatori con all'interno i dati dei 10 paesi e dei 30 anni considerati.
I file sono composti dagli anni come righe e dai paesi come colonne, e ovviamente i dati all'interno indicano il dato di quel determinato indicatore in quell'anno e in quel paese.

Prima di passare alle analisi vere e proprie faccio partire il codice preprocessing con al suo interno analisi generali dei singoli dataset e il preprocesso per organizzare i dati in modo che possano essere utilizzati per le analisi successive.
Con questo processo notiamo che:
-Il dataset 'Life expectacy' ha 1 riga con valori mancanti: non ci sono valori per il 2024 quindi elimino questo anno in questo dataset
-Il dataset 'Health expenditure' ha 7 righe con all'interno valori mancanti: non ci sono i valori dal 1995 al 1999 e del 2024, invece i valori del 2023 ci sono solo per alcuni paesi (5 su 10). Le 6 righe senza dati le elimino, invece per il 2023 capisco se ha senso tenerlo. Alla fine elimino anche il 2023 perchè per le analisi che andrò a svolgere non ha senso tentare un imputazione.
-Il dataset 'Infant mortality' ha 1 riga con valori mancanti: non ci sono valori per il 2024 quindi elimino questo anno in questo dataset
Quindi ho sistemato i 3 dataset con valori nulli per le analisi future.

Analisi da svolgere:
obiettivo --> relazione tra ricchezza economica e benessere sociale --> storia della salute e dell'economia globali
tendenze e correlazioni dello sviluppo globale --> tutti i paesi --> modelli di sviluppo delle nazioni 
ANALISI DI CORRELAZIONE + TREND TEMPORALI + CONFRONTI GEOGRAFICI

## Data analysis socio-economica

Analisi:
-Analisi generali: describe nel preprocesso (media, varianza, ...) OK

-Pil pro capite nel tempo OK
-Aspettativa di vita nel tempo OK
-Disoccupazione nel tempo OK
-Mortalità infantile nel tempo OK
-confronto pre e post crisi economica del 2008: pil pro capite medio (2000-2007 vs 2009-2019 così lasci perdere il covid) + aspettativa di vita, disoccupazione, mortalità infantile OK

-Pil pro capite vs aspettativa di vita --> pil alto = aspettativa di vita più lunga? --> correlazione di pearson OK
-Disoccupazione vs aspettativa di vita OK
-Pil pro capite vs spesa sanitaria pro capite OK
-Pil pro capite vs tassi di mortalità infantile OK
-Spesa sanitaria pro capite vs mortalità infantile --> più è alta, meno bambini muoiono? OK

-cambia nel tempo questa correlazione? (serie temporale dei paesi) OK

+
-regressione lineare --> Life_expectancy ~ GDP_per_capita + Health_expenditure + Infant_mortality --> scatter plot della regressione OK
-creare un indice sintetico di benessere che riassume tutti gli indici di benessere (aspettativa di vita, spesa sanitaria, mortalità infantile OK
-cluster analisis: raggruppa i paesi in base ai loro indicatori economici e sanitari (Commento: vedi se i gruppi sono paragonabili a quelli che 'si conoscono già' che potrebbero non essere uguali a quelli territoriali) OK

Visualizzazioni globali: --> si possono animare per vedere l'evoluzione?
-grafici vari indicatore per indicatore --> andamento nel tempo dei vari indicatori (linee per paese e media per continente) --> grafico linee OK
-correlazione tra il pil pro capite e l'aspettativa di vita cambia nel tempo? per ogni paese (serie temporale) OK
-Mappa mondiale che rappresenta la crescita annuale OK
-Mappa mondiale che rappresenta il pil generale OK
-Mappa mondiale che rappresenta l'aspettativa di vita OK
