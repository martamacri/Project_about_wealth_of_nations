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

sns.set(style="whitegrid")

# pil pro capite, aspettativa di vita, disoccupazione, mortalità infantile nel tempo
def plot_indicator(df, title):
    df = df.dropna(how='all')
    Years = df.iloc[:, 0].astype(str).str.extract(r'(\d+)')[0].astype(int)
    df = df.iloc[:, 1:]
    min_len = min(len(Years), len(df))
    Years = Years.iloc[:min_len]
    df = df.iloc[:min_len, :]
    plt.figure(figsize=(15, 8))
    for paese in df.columns:
        plt.plot(Years, df[paese], marker='o', label=paese)
    plt.xlabel('Year')
    plt.ylabel('Value')
    plt.title(title)
    plt.legend()
    plt.show()
plot_indicator(df1, 'Evolution of GDP per capita over time by country')
plot_indicator(df3, 'Evolution of life expectancy over time by country')
plot_indicator(df6, 'Evolution of unemployment over time by country')
plot_indicator(df5, 'Evolution of infant mortality over time by country')

# confronto pre e post crisi economica del 2008 (2000-2007 vs 2009-2019)
def mean_pre_post(df):
    df = df.dropna(how='all')
    Years = df.iloc[:, 0].astype(str).str.extract(r'(\d+)')[0].astype(int)
    df_data = df.iloc[:, 1:]
    min_len = min(len(Years), len(df_data))
    Years = Years.iloc[:min_len]
    df_data = df_data.iloc[:min_len, :]
    df_data = df_data[Years.between(2000, 2019)]
    Years = Years[Years.between(2000, 2019)]
    pre = df_data[Years.between(2000, 2007)].mean()
    post = df_data[Years.between(2009, 2019)].mean()
    result = pd.DataFrame({
        'Mean 2000–2007': pre,
        'Mean 2009–2019': post
    })
    result['Δ % post/pre'] = (result['Mean 2009–2019'] - result['Mean 2000–2007']) / result['Mean 2000–2007'] * 100
    return result.round(2)
gdp_per_capita_mean = mean_pre_post(df1)
life_expectancy_mean = mean_pre_post(df3)
unemployment_mean = mean_pre_post(df6)
infant_mortality_mean = mean_pre_post(df5)
print("GDP per capita:")
print(gdp_per_capita_mean)
print("\nLife expectancy:")
print(life_expectancy_mean)
print("\nUnemployment:")
print(unemployment_mean)
print("\nInfant mortality:")
print(infant_mortality_mean)