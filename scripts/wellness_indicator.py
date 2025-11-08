"""
indicatore di benessere
"""
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from formatting import prepare_df
sns.set(style="whitegrid")

df1 = pd.read_csv('data/gdp_per_capita_1995_2024.csv')
df3 = pd.read_csv('data/life_expectacy_1995_2023.csv')
df4 = pd.read_csv('data/health_expenditure_2000_2022.csv')
df5 = pd.read_csv('data/infant_mortality_1995_2023.csv')

pil = prepare_df(df1)
life = prepare_df(df3)
health = prepare_df(df4)
infant_mort = prepare_df(df5)

#indice sintetico di benessere che riassume tutti gli indici di benessere
#(aspettativa di vita, spesa sanitaria, mortalità infantile)
#normalizzo i dati che devono avere tutti lo stesso ordine
def compute_wellbeing_index(life_df, health_df, infant_df):
    """
    Calcola un indice sintetico di benessere per paese e anno
    basato su aspettativa di vita, spesa sanitaria e mortalità infantile.
    """
    countries_df = life_df.columns.intersection(health_df.columns)\
                               .intersection(infant_df.columns)
    common_years_df = life_df.index.intersection(health_df.index)\
                                 .intersection(infant_df.index)
    life_clean = life_df.loc[common_years_df, countries_df]
    health_clean = health_df.loc[common_years_df, countries_df]
    infant_clean = infant_df.loc[common_years_df, countries_df]

    # Inverti mortalità infantile (più alto è meglio)
    infant_inv = infant_clean.max().max() - infant_clean

    # Normalizzazione min-max
    def minmax_normalize(df):
        return (df - df.min()) / (df.max() - df.min())

    life_norm = minmax_normalize(life_clean)
    health_norm = minmax_normalize(health_clean)
    infant_norm = minmax_normalize(infant_inv)

    # Indice sintetico di benessere (media dei tre)
    wellbeing_index_df = (life_norm + health_norm + infant_norm) / 3

    return wellbeing_index_df, countries_df

# Calcolo dell'indice
wellbeing_index, countries = compute_wellbeing_index(life, health, infant_mort)

# Evoluzione media nel tempo
plt.figure(figsize=(12, 6))
wellbeing_index.mean(axis=1).plot()
plt.title("Summary index of average well-being over time")
plt.xlabel("Year")
plt.ylabel("Well-being index")
plt.grid(True)
plt.show()

# Classifica dei paesi per indice medio
mean_wellbeing = wellbeing_index.mean(axis=0)
rank = mean_wellbeing.sort_values(ascending=False)
print("Ranking of countries by average well-being index:")
print(rank)

# Confronto con PIL medio
common_years = wellbeing_index.index.intersection(pil.index)
gdp_mean = pil.loc[common_years, countries].mean()
plt.figure(figsize=(10, 6))
plt.scatter(gdp_mean, mean_wellbeing)
for country in countries:
    plt.text(gdp_mean[country], mean_wellbeing[country], country, fontsize=8)
plt.xlabel("Average GDP per capita")
plt.ylabel("Average well-being index")
plt.title("Relationship between GDP per capita and well-being index")
plt.grid(True)
plt.show()

# Correlazione
corr = gdp_mean.corr(mean_wellbeing)
print(f"Pearson correlation between average GDP per capita and well-being index: {corr:.3f}")
