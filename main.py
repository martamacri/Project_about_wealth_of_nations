"""
Main code
"""
import sys
import os
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

from scripts.formatting import prepare_df
from scripts.timelines import plot_indicator, mean_pre_post
from scripts.correlations import compute_country_correlations, compute_rolling_correlation
from scripts.regression import regression_life_expectancy
from scripts.wellness_indicator import compute_wellbeing_index
from scripts.cluster_analysis import cluster_countries
from scripts.visualizations import plot_by_continent, melt_indicator, animate_indicator

scripts_path = os.path.dirname(os.path.abspath(__file__))
if scripts_path not in sys.path:
    sys.path.insert(0, scripts_path)
sns.set(style="whitegrid")

df1 = pd.read_csv('data/gdp_per_capita_1995_2024.csv')
df2 = pd.read_csv('data/gdp_1995_2024.csv')
df3 = pd.read_csv('data/life_expectacy_1995_2023.csv')
df4 = pd.read_csv('data/health_expenditure_2000_2022.csv')
df5 = pd.read_csv('data/infant_mortality_1995_2023.csv')
df6 = pd.read_csv('data/unemployment_1995_2024.csv')
df7 = pd.read_csv('data/population_growth_1995_2024.csv')

gdp_pc = prepare_df(df1)
gdp = prepare_df(df2)
life = prepare_df(df3)
health = prepare_df(df4)
infant_mort = prepare_df(df5)
unemp = prepare_df(df6)
pop = prepare_df(df7)

# Evolution over time by country
plot_indicator(gdp_pc, 'Evolution of GDP per capita over time by country')
plot_indicator(life, 'Evolution of life expectancy over time by country')
plot_indicator(unemp, 'Evolution of unemployment over time by country')
plot_indicator(infant_mort, 'Evolution of infant mortality over time by country')

# Evolution over time by continent
plot_by_continent(gdp_pc, 'Evolution of GDP per capita over time by continent')
plot_by_continent(life, 'Evolution of life expectancy over time by continent')
plot_by_continent(unemp, 'Evolution of unemployment over time by continent')
plot_by_continent(infant_mort, 'Evolution of infant mortality over time by continent')

# Pre-post 2008
gdp_per_capita_mean = mean_pre_post(gdp_pc)
life_expectancy_mean = mean_pre_post(life)
unemployment_mean = mean_pre_post(unemp)
infant_mortality_mean = mean_pre_post(infant_mort)
print("GDP per capita:")
print(gdp_per_capita_mean)
print("\nLife expectancy:")
print(life_expectancy_mean)
print("\nUnemployment:")
print(unemployment_mean)
print("\nInfant mortality:")
print(infant_mortality_mean)

# Calculation of correlations
comparisons = [
    ("GDP per capita", gdp_pc, "Life expectancy", life),
    ("Unemployment", unemp, "Life expectancy", life),
    ("GDP per capita", gdp_pc, "Health expenditure", health),
    ("GDP per capita", gdp_pc, "Infant mortality", infant_mort),
    ("Health expenditure", health, "Infant mortality", infant_mort)
]

corr_df_list = [compute_country_correlations(df_x, df_y, name_x, name_y)
                for name_x, df_x, name_y, df_y in comparisons]
corr_df = pd.concat(corr_df_list, ignore_index=True)
print(corr_df)

# Mobile correlation between GDP per capita and life expectancy
WINDOW = 15
rolling_corr = compute_rolling_correlation(gdp_pc, life, window=WINDOW)

# Mobile correlation plot
plt.figure(figsize=(14, 8))
for country in rolling_corr.columns:
    plt.plot(rolling_corr.index, rolling_corr[country], label=country)
plt.title(f"Rolling correlation ({WINDOW} years) between GDP per capita and life expectancy")
plt.xlabel("Year")
plt.ylabel("Pearson's correlation")
plt.legend()
plt.grid(True)
plt.show()

# Linear regression
model_df, data_df = regression_life_expectancy(gdp_pc, life, health, infant_mort)
print(model_df.summary())

# Wellness indicator
# Calculation of the index
wellbeing_index, countries = compute_wellbeing_index(life, health, infant_mort)

# Average evolution over time
plt.figure(figsize=(12, 6))
wellbeing_index.mean(axis=1).plot()
plt.title("Summary index of average well-being over time")
plt.xlabel("Year")
plt.ylabel("Well-being index")
plt.grid(True)
plt.show()

# Ranking of countries by average index
mean_wellbeing = wellbeing_index.mean(axis=0)
rank = mean_wellbeing.sort_values(ascending=False)
print("Ranking of countries by average well-being index:")
print(rank)

# Comparison with average GDP per capita
common_years = wellbeing_index.index.intersection(gdp_pc.index)
gdp_mean = gdp_pc.loc[common_years, countries].mean()
plt.figure(figsize=(10, 6))
plt.scatter(gdp_mean, mean_wellbeing)
for country in countries:
    plt.text(gdp_mean[country], mean_wellbeing[country], country, fontsize=8)
plt.xlabel("Average GDP per capita")
plt.ylabel("Average well-being index")
plt.title("Relationship between GDP per capita and well-being index")
plt.grid(True)
plt.show()

# Correlation
corr = gdp_mean.corr(mean_wellbeing)
print(f"Pearson correlation between average GDP per capita and well-being index: {corr:.3f}")

# Cluster analysis
dfs = {
    'GDP_per_capita': df1,
    'GDP': df2,
    'Life_expectancy': df3,
    'Health_expenditure': df4,
    'Infant_mortality': df5,
    'Unemployment': df6,
    'Population_growth': df7
}
countries = ['ITA', 'ESP', 'DEU', 'SWE', 'USA', 'CAN', 'BRA', 'CHL', 'ZAF', 'NGA']
results = cluster_countries(
    dfs_dict=dfs,
    nations=countries,
    method='latest',
    k_min=2,
    k_max=6,
    plot=True,
    prepare_func=prepare_df
)
print("\nRisultati per paese:")
print(results['result_table'])

# Visualizations
ind_pil = melt_indicator(df2, 'GDP')
ind_life = melt_indicator(df3, 'Life expectancy')
ind_growth = melt_indicator(df7, 'Population growth')
animate_indicator(ind_pil, 'GDP', cmap='plasma')
animate_indicator(ind_life, 'Life expectancy', cmap='viridis')
animate_indicator(ind_growth, 'Population growth', cmap='coolwarm')
