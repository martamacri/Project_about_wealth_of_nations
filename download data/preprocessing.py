"""Pulizia e trasformazioni dei dati
"""
import pandas as pd

# Indicator 1: gdp per capita
df1 = pd.read_csv('data/gdp_per_capita_1995_2024.csv')
print(df1.head())
print(df1.info()) #non ci sono valori nulli nei dati e sono tutti numeri
print(df1.describe()) #statistiche descrittive
# non serve un preprocesso

# Indicator 2: gdp
df2 = pd.read_csv('data/gdp_1995_2024.csv')
print(df2.head())
print(df2.info()) #non ci sono valori nulli nei dati e sono tutti numeri
print(df2.describe()) #statistiche descrittive
# non serve un preprocesso

# Indicator 3: life expextacy
df3 = pd.read_csv('data/life_expectacy_1995_2024.csv')
print(df3.head())
print(df3.info()) #sono tutti numeri ma ci sono valori mancanti
print(df3.describe()) #statistiche descrittive
# c'è una riga mancante
row_missing_count = df3.isnull().any(axis=1).sum()
print(row_missing_count) #si ne manca una
row = df3[df3.isnull().any(axis=1)]
print(row) # non ho valori per il 2024
df3_clean = df3.dropna()
print(df3_clean.tail())
df3_clean.to_csv("life_expectacy_1995_2023.csv", index=False)
print("\nSalvato: life_expectacy_1995_2023.csv")

# Indicator 4: health expenditure
df4 = pd.read_csv('data/health_expenditure_1995_2024.csv')
print(df4.head())
print(df4.info()) #sono tutti numeri ma ci sono valori mancanti
print(df4.describe())
# molti valori mancanti
row_missing_count = df4.isnull().any(axis=1).sum()
print(row_missing_count) # 7 righe con valori mancanti
row = df4[df4.isnull().any(axis=1)]
print(row) # non ho valori dal 1995 al 1999 e per il 2023-2024
row_count = row.isnull().sum(axis=1)
print(row_count) # noto che il 2023 ha alcuni valori
# tolgo i valori delle righe dal 1995 al 1999 e il 2024
years_drop = ['YR1995', 'YR1996', 'YR1997', 'YR1998', 'YR1999', 'YR2024']
df4_clean = df4[~df4['Year'].isin(years_drop)]
rows_with_missing = df4_clean[df4_clean.isnull().any(axis=1)]
print(rows_with_missing)
print(df4_clean.head())
# vediamo se vale la pena tenere i dati del 2023
rows_with_missing = df4_clean[df4_clean.isnull().any(axis=1)]
print(rows_with_missing) # non ho brasile, spagna, nigeria, stati uniti e sudafrica
df4_clean = df4_clean[df4_clean['Year'] != 'YR2023']
print(df4_clean.tail())
df4_clean.to_csv('health_expenditure_2000_2022.csv', index=False)
print("\nSalvato: life_expectacy_2000_2022.csv")

# Indicator 5: Infant mortality
df5 = pd.read_csv('data/infant_mortality_1995_2024.csv')
print(df5.head())
print(df5.info())
print(df5.describe())
# c'è una riga mancante
row_missing_count = df5.isnull().any(axis=1).sum()
print(row_missing_count) # si ne manca una
row = df5[df5.isnull().any(axis=1)]
print(row) # non ho valori per il 2024
df5_clean = df5.dropna()
print(df5_clean.tail())
df5_clean.to_csv("infant_mortality_1995_2023.csv", index=False)
print("\nSalvato: infant_mortality_1995_2023.csv")

# Indicator 6: Unemployment
df6 = pd.read_csv('data/unemployment_1995_2024.csv')
print(df6.head())
print(df6.info())
print(df6.describe())
# non serve preprocesso

# Indicator 7: Population growth
df7 = pd.read_csv('data/population_growth_1995_2024.csv')
print(df7.head())
print(df7.info())
print(df7.describe())
# non serve preprocesso
