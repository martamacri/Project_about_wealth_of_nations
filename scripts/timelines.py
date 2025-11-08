"""
pil pro capite, aspettativa di vita, disoccupazione, mortalità infantile nel tempo
"""
import sys
import os
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from formatting import prepare_df
scripts_path = os.path.dirname(os.path.abspath(__file__))
if scripts_path not in sys.path:
    sys.path.insert(0, scripts_path)
sns.set(style="whitegrid")

# Caricamento CSV
df1 = pd.read_csv('data/gdp_per_capita_1995_2024.csv')
df3 = pd.read_csv('data/life_expectacy_1995_2023.csv')
df5 = pd.read_csv('data/infant_mortality_1995_2023.csv')
df6 = pd.read_csv('data/unemployment_1995_2024.csv')
# Pulizia e preparazione dei DataFrame
df1_clean = prepare_df(df1)
df3_clean = prepare_df(df3)
df5_clean = prepare_df(df5)
df6_clean = prepare_df(df6)

# Funzione per grafici nel tempo
def plot_indicator(df, title):
    """
    grafici
    """
    plt.figure(figsize=(15, 8))
    for paese in df.columns:
        plt.plot(df.index, df[paese], marker='o', label=paese)
    plt.xlabel('Year')
    plt.ylabel('Value')
    plt.title(title)
    plt.legend()
    plt.show()
plot_indicator(df1_clean, 'Evolution of GDP per capita over time by country')
plot_indicator(df3_clean, 'Evolution of life expectancy over time by country')
plot_indicator(df6_clean, 'Evolution of unemployment over time by country')
plot_indicator(df5_clean, 'Evolution of infant mortality over time by country')

# Funzione confronto pre e post crisi economica del 2008
def mean_pre_post(df):
    """
    confronto
    """
    df.index = pd.to_numeric(df.index, errors='coerce')  # forza indice numerico
    df_data = df.loc[(df.index >= 2000) & (df.index <= 2019)]
    pre = df_data.loc[(df_data.index >= 2000) & (df_data.index <= 2007)].mean()
    post = df_data.loc[(df_data.index >= 2009) & (df_data.index <= 2019)].mean()
    result = pd.DataFrame({
        'Mean 2000–2007': pre,
        'Mean 2009–2019': post
    })
    result['Δ % post/pre'] = (
    (result['Mean 2009–2019'] - result['Mean 2000–2007'])
    / result['Mean 2000–2007']
    * 100
    )
    return result.round(2)
gdp_per_capita_mean = mean_pre_post(df1_clean)
life_expectancy_mean = mean_pre_post(df3_clean)
unemployment_mean = mean_pre_post(df6_clean)
infant_mortality_mean = mean_pre_post(df5_clean)
print("GDP per capita:")
print(gdp_per_capita_mean)
print("\nLife expectancy:")
print(life_expectancy_mean)
print("\nUnemployment:")
print(unemployment_mean)
print("\nInfant mortality:")
print(infant_mortality_mean)
