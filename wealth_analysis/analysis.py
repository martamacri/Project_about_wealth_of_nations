# Analisi statistiche e correlazioni
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import statsmodels.api as sm

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

# correlazioni per ogni paese
def prepare_df(df):
    df = df.dropna(how='all')
    Years = df.iloc[:, 0].astype(str).str.extract(r'(\d+)')[0].astype(int)
    df_data = df.iloc[:, 1:]
    df_data.index = Years
    return df_data
pil = prepare_df(df1)
life = prepare_df(df3)
health = prepare_df(df4)
unemp = prepare_df(df6)
infant_mort = prepare_df(df5)
comparisons = [
    ('GDP per capita', pil, 'Life expectancy', life),
    ('Unemployment', unemp, 'Life expectancy', life),
    ('GDP per capita', pil, 'Health expenditure', health),
    ('GDP per capita', pil, 'Infant mortality', infant_mort),
    ('Health expenditure', health, 'Infant mortality', infant_mort)
]
results = []
for name_x, df_x, name_y, df_y in comparisons:
    countries = df_x.columns.intersection(df_y.columns)
    common_years = df_x.index.intersection(df_y.index)
    for country in countries:
        x_vals = df_x.loc[common_years, country]
        y_vals = df_y.loc[common_years, country]
        valid_idx = x_vals.notna() & y_vals.notna()
        if valid_idx.sum() > 1:
            corr = x_vals[valid_idx].corr(y_vals[valid_idx])
        else:
            corr = None
        results.append({
            'Country': country,
            'X': name_x,
            'Y': name_y,
            'Pearson correlation': corr
        })
corr_df = pd.DataFrame(results)
print(corr_df)

# La correlazione tra il pil pro capite e l'aspettativa di vita cambia nel tempo? per ogni paese (serie temporale)
window = 15
countries = pil.columns  
common_years = pil.index.intersection(life.index)  
rolling_corr = pd.DataFrame(index=common_years)
for country in countries:
    x = pil.loc[common_years, country]
    y = life.loc[common_years, country]
    corr = (
        x.rolling(window=window, min_periods=3)
         .corr(y)
    )
    rolling_corr[country] = corr
plt.figure(figsize=(14, 8))
for country in rolling_corr.columns:
    plt.plot(rolling_corr.index, rolling_corr[country], label=country)
plt.title(f"Mobile correlation ({window} years) between GDP per capita and life expectancy")
plt.xlabel("Year")
plt.ylabel("Pearson's correlation")
plt.legend()
plt.grid(True)
plt.show()

# regressione lineare --> Life_expectancy ~ GDP_per_capita + Health_expenditure + Infant_mortality
common_years = pil.index.intersection(life.index).intersection(health.index).intersection(infant_mort.index)
data = pd.DataFrame({
    'Country': [c for c in countries for _ in common_years],
    'Year': list(common_years) * len(countries),
    'GDP_per_capita': pd.concat([pil.loc[common_years, c] for c in countries], ignore_index=True),
    'Health_expenditure': pd.concat([health.loc[common_years, c] for c in countries], ignore_index=True),
    'Infant_mortality': pd.concat([infant_mort.loc[common_years, c] for c in countries], ignore_index=True),
    'Life_expectancy': pd.concat([life.loc[common_years, c] for c in countries], ignore_index=True),
})
X = data[['GDP_per_capita', 'Health_expenditure', 'Infant_mortality']]
y = data['Life_expectancy']
X = sm.add_constant(X) 
model = sm.OLS(y, X).fit()
print(model.summary()) #coefficient 
plt.figure(figsize=(10, 6))
sns.scatterplot(x='GDP_per_capita', y='Life_expectancy', data=data, hue='Country', alpha=0.7)
sns.regplot(x='GDP_per_capita', y='Life_expectancy', data=data, scatter=False, color='black')
plt.title('Relationship between GDP per capita and life expectancy')
plt.xlabel('GDP per capita')
plt.ylabel('Life expectancy')
plt.grid(True)
plt.show()

#indice sintetico di benessere che riassume tutti gli indici di benessere (aspettativa di vita, spesa sanitaria, mortalità infantile)
#normalizzo i dati che devono avere tutti lo stesso ordine
infant_inv = infant_mort.max().max() - infant_mort
def minmax_normalize(df):
    return (df - df.min()) / (df.max() - df.min())
life_norm = minmax_normalize(life)
health_norm = minmax_normalize(health)
infant_norm = minmax_normalize(infant_inv)
#evoluzione nel tempo
wellbeing_index = (life_norm + health_norm + infant_norm) / 3
wellbeing_index.mean(axis=1).plot(figsize=(12,6))
plt.title("Summary index of average well-being over time")
plt.xlabel("Year")
plt.ylabel("Well-being index")
plt.show()
#classifica dei paesi per indice medio
mean_wellbeing = wellbeing_index.mean(axis=0)
rank = mean_wellbeing.sort_values(ascending=False)
print(rank)
#pil vs benessere
common_years = wellbeing_index.index.intersection(pil.index)
gdp_mean = pil.loc[common_years].mean()
plt.figure(figsize=(10,6))
plt.scatter(gdp_mean, mean_wellbeing)
for country in countries:
    plt.text(gdp_mean[country], mean_wellbeing[country], country, fontsize=8)
plt.xlabel("Average GDP per capita")
plt.ylabel("Average well-being index")
plt.title("Relationship between GDP per capita and well-being index")
plt.grid(True)
plt.show()
corr = gdp_mean.corr(mean_wellbeing)
print(f"Pearson correlation between average GDP per capita and well-being index: {corr:.3f}")