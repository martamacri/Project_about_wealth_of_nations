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

sns.set(style="whitegrid")

# Andamento nel tempo dei vari indicatori per paese
def plot_time_series(df, title, figsize=(15,8), marker='o'):
    df = df.dropna(how='all')
    Years = df.iloc[:, 0].astype(str).str.extract(r'(\d+)')[0].astype(int)
    df = df.iloc[:, 1:]
    min_len = min(len(Years), len(df))
    Years = Years.iloc[:min_len]
    df = df.iloc[:min_len, :]
    plt.figure(figsize=figsize)
    for paese in df.columns:
        plt.plot(Years, df[paese], marker=marker, label=paese)
    plt.xlabel('Year')
    plt.ylabel('Value')
    plt.title(title)
    plt.legend()
    plt.show()
plot_time_series(df1, 'Evolution of GDP per capita over time by country')
plot_time_series(df2, 'Evolution of GDP over time by country')
plot_time_series(df3, 'Evolution of life expectancy over time by country')
plot_time_series(df4, 'Evolution of health expenditure over time by country')
plot_time_series(df5, 'Evolution of infant mortality over time by country')
plot_time_series(df6, 'Evolution of unemployment over time by country')
plot_time_series(df7, 'Evolution of population growth over time by country')

# Andamento nel tempo dei vari indicatori per continente
continents_dict = {
    'Europa': ['ITA', 'ESP', 'DEU', 'SWE'],
    'Nord America': ['USA', 'CAN'],
    'Sud America': ['BRA', 'CHL'],
    'Africa': ['ZAF', 'NGA']
}
def plot_by_continent(df, title):
    df = df.dropna(how='all')
    Years = df.iloc[:, 0].astype(str).str.extract(r'(\d+)')[0].astype(int)
    df = df.iloc[:, 1:]
    df.index = Years
    df_continent = pd.DataFrame({
        continent: df[countries].mean(axis=1)
        for continent, countries in continents_dict.items()
    })
    plt.figure(figsize=(15, 8))
    for continent in df_continent.columns:
        plt.plot(df_continent.index, df_continent[continent],
                 marker='o', label=continent)
    plt.xlabel('Year')
    plt.ylabel('Mean value')
    plt.title(title)
    plt.legend(title='Continents')
    plt.show()
plot_by_continent(df1, 'Evolution of GDP per capita over time by continent')
plot_by_continent(df2, 'Evolution of GDP over time by continent')
plot_by_continent(df3, 'Evolution of life expectancy over time by continent')
plot_by_continent(df4, 'Evolution of health expenditure over time by continent')
plot_by_continent(df5, 'Evolution of infant mortality over time by continent')
plot_by_continent(df6, 'Evolution of unemployment over time by continent')
plot_by_continent(df7, 'Evolution of population growth over time by continent')