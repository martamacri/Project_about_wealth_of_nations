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
libreria con vari dataset... come ci accedo? guarda il link del testo del progetto per capire
.............

prendo in analisi i dati dal 2000 al 2023 perchè i dati del 2024/2025 non sono completi 
indicatori scaricati per le analisi:
-'GDP per capita': 'NY.GDP.PCAP.CD' --> ricchezza media per persona
-'GDP': 'NY.GDP.MKTP.CD' --> ricchezza totale di un paese
-'Life expectancy': 'SP.DYN.LE00.IN' --> media di anni di vita alla nascita
-'Health expenditure': 'SH.XPD.CHEX.PC.CD' --> spesa sanitaria per persona
-'Infant mortality': 'SH.DYN.MORT' --> tasso di mortalità infantile per 1000 nati vivi 
-'Education': 'SE.ADT.LITR.ZS' --> percentuale di adulti alfabetizzati 
-'Population growth': 'SP.POP.GROW' --> percentuale di crescita annuale 

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
