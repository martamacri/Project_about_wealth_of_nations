# Funzioni per grafici e mappe
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df1 = pd.read_csv('data/gdp_per_capita_1995_2024.csv')
df2 = pd.read_csv('data/gdp_1995_2024.csv')
df3 = pd.read_csv('data/life_expectacy_1995_2023.csv')
df4 = pd.read_csv('data/health_expenditure_2000_2022.csv')
df5 = pd.read_csv('data/infant_mortality_1995_2023.csv')
df6 = pd.read_csv('data/unemployment_1995_2024.csv')
df7 = pd.read_csv('data/population_growth_1995_2024.csv')

# Andamento nel tempo dei vari indicatori per paese
# Gdp pro capite
sns.set(style="whitegrid")
df1 = df1.dropna(how='all')
Years = df1.iloc[:, 0].astype(str).str.extract(r'(\d+)')[0].astype(int)
df1 = df1.iloc[:, 1:]
min_len = min(len(Years), len(df1))
Years = Years.iloc[:min_len]
df1 = df1.iloc[:min_len, :]
plt.figure(figsize=(15, 8))
for paese in df1.columns:
    plt.plot(Years, df1[paese], marker='o', label=paese)
plt.xlabel('Year')
plt.ylabel('Value')
plt.title('Evolution of gdp per capita over time by country')
plt.legend()
plt.show()
# Gdp
sns.set(style="whitegrid")
df2 = df2.dropna(how='all')
Years = df2.iloc[:, 0].astype(str).str.extract(r'(\d+)')[0].astype(int)
df2 = df2.iloc[:, 1:]
min_len = min(len(Years), len(df2))
Years = Years.iloc[:min_len]
df2 = df2.iloc[:min_len, :]
plt.figure(figsize=(15, 8))
for paese in df2.columns:
    plt.plot(Years, df2[paese], marker='o', label=paese)
plt.xlabel('Year')
plt.ylabel('Value')
plt.title('Evolution of gdp over time by country')
plt.legend()
plt.show()
# Life expectacy
df3 = df3.dropna(how='all')
Years = df3.iloc[:, 0].astype(str).str.extract(r'(\d+)')[0].astype(int)
df3 = df3.iloc[:, 1:]
min_len = min(len(Years), len(df3))
Years = Years.iloc[:min_len]
df3 = df3.iloc[:min_len, :]
plt.figure(figsize=(15, 8))
for paese in df3.columns:
    plt.plot(Years, df3[paese], marker='o', label=paese)
plt.xlabel('Year')
plt.ylabel('Value')
plt.title('Evolution of life expextacy over time by country')
plt.legend()
plt.show()
# Health expenditure
df4 = df4.dropna(how='all')
Years = df4.iloc[:, 0].astype(str).str.extract(r'(\d+)')[0].astype(int)
df4 = df4.iloc[:, 1:]
min_len = min(len(Years), len(df4))
Years = Years.iloc[:min_len]
df4 = df4.iloc[:min_len, :]
plt.figure(figsize=(15, 8))
for paese in df4.columns:
    plt.plot(Years, df4[paese], marker='o', label=paese)
plt.xlabel('Year')
plt.ylabel('Value')
plt.title('Evolution of health expenditure over time by country')
plt.legend()
plt.show()
# Infant mortality
df5 = df5.dropna(how='all')
Years = df5.iloc[:, 0].astype(str).str.extract(r'(\d+)')[0].astype(int)
df5 = df5.iloc[:, 1:]
min_len = min(len(Years), len(df5))
Years = Years.iloc[:min_len]
df5 = df5.iloc[:min_len, :]
plt.figure(figsize=(15, 8))
for paese in df5.columns:
    plt.plot(Years, df5[paese], marker='o', label=paese)
plt.xlabel('Year')
plt.ylabel('Value')
plt.title('Evolution of infant mortality over time by country')
plt.legend()
plt.show()
# Unemployment
df6 = df6.dropna(how='all')
Years = df6.iloc[:, 0].astype(str).str.extract(r'(\d+)')[0].astype(int)
df6 = df6.iloc[:, 1:]
min_len = min(len(Years), len(df6))
Years = Years.iloc[:min_len]
df6 = df6.iloc[:min_len, :]
plt.figure(figsize=(15, 8))
for paese in df6.columns:
    plt.plot(Years, df6[paese], marker='o', label=paese)
plt.xlabel('Year')
plt.ylabel('Value')
plt.title('Evolution of unemployment over time by country')
plt.legend()
plt.show()
# Population growth
df7 = df7.dropna(how='all')
Years = df7.iloc[:, 0].astype(str).str.extract(r'(\d+)')[0].astype(int)
df7 = df7.iloc[:, 1:]
min_len = min(len(Years), len(df7))
Years = Years.iloc[:min_len]
df7 = df7.iloc[:min_len, :]
plt.figure(figsize=(15, 8))
for paese in df7.columns:
    plt.plot(Years, df7[paese], marker='o', label=paese)
plt.xlabel('Year')
plt.ylabel('Value')
plt.title('Evolution of population growth over time by country')
plt.legend()
plt.show()

# Andamento nel tempo dei vari indicatori per continente
continenti = {
    'Europa': ['ITA', 'ESP', 'DEU', 'SWE'],
    'Nord America': ['USA', 'CAN'],
    'Sud America': ['BRA', 'CHL'],
    'Afica': ['ZAF', 'NGA']
}