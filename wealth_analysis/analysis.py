# Analisi statistiche e correlazioni
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

#EDA
print(df1.describe())

sns.set(style="whitegrid")
df1 = pd.read_csv('data/gdp_per_capita_1995_2024.csv')
df1 = df1.dropna(how='all')
Years = df1.iloc[:, 0].astype(str).str.extract('(\d+)')[0].astype(int)
df1 = df1.iloc[:, 1:]
min_len = min(len(Years), len(df1))
Years = Years.iloc[:min_len]
df1 = df1.iloc[:min_len, :]
plt.figure(figsize=(15, 8))
for paese in df1.columns:
    plt.plot(Years, df1[paese], marker='o', label=paese)
plt.xlabel('Year')
plt.ylabel('Value')
plt.title('Evolution over time by country')
plt.legend()
plt.show()

#print(df2.describe())
#print(df3.describe())
#print(df4.describe())
#print(df5.describe())
#print(df6.describe())
#print(df7.describe())