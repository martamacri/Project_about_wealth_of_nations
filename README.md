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
-Asia: Sudafica (ZAF), Nigeria (NGA)

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

Analisi da svolgere:
obiettivo --> relazione tra ricchezza economica e benessere sociale --> storia della salute e dell'economia globali
tendenze e correlazioni dello sviluppo globale --> tutti i paesi --> modelli di sviluppo delle nazioni 
Esempi:
-Pil pro capite vs aspettativa di vita --> pil alto = aspettativa di vita più lunga? cambia nel tempo questa correlazione? (prendi un paese con il pil alto, uno medio e uno basso e fai serie temporale)
-Mappa modiale che rappresenta il pil generale
-Mappa modiale che rappresenta l'aspettativa di vita
-Spesa sanitaria pro capite vs mortalità infantile --> più è alta, meno bambini muoiono?
-Pil pro capite vs spesa sanitaria pro capite
-Pil pro capite vs tassi di mortalità infantile 
(-cluster analisis: raggruppa i paesi in base ai loro indicatori economici e sanitari e vedi se i gruppi sono paragonabili a quelli che 'si conoscono già')
