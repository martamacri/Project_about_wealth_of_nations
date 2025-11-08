"""
Modulo per eseguire regressioni lineari sulla Life Expectancy
utilizzando GDP per capita, Health Expenditure e Infant Mortality.
Produce anche scatterplot con regressione lineare per GDP per capita.
"""
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import statsmodels.api as sm
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

# regressione lineare --> Life_expectancy ~ GDP_per_capita + Health_expenditure + Infant_mortality
def regression_life_expectancy(pil_df, life_df, health_df, infant_mort_df):
    """
    Esegue una regressione lineare su Life Expectancy usando GDP per capita,
    Health Expenditure e Infant Mortality, e produce uno scatterplot con la 
    regressione lineare per GDP per capita.
    """
    # Trova paesi e anni comuni
    countries = pil.columns.intersection(life_df.columns)\
                          .intersection(health_df.columns)\
                          .intersection(infant_mort_df.columns)
    common_years = pil.index.intersection(life_df.index)\
                            .intersection(health_df.index)\
                            .intersection(infant_mort_df.index)
    # Costruzione del dataset per regressione
    data_rows = []
    for country in countries:
        df_country = pd.DataFrame({
            'Country': country,
            'Year': common_years,
            'GDP_per_capita': pil_df.loc[common_years, country],
            'Health_expenditure': health_df.loc[common_years, country],
            'Infant_mortality': infant_mort_df.loc[common_years, country],
            'Life_expectancy': life_df.loc[common_years, country]
        })
        data_rows.append(df_country)
    dataset = pd.concat(data_rows, ignore_index=True)
    dataset = dataset.dropna()  # rimuove eventuali valori NA
    # Regressione lineare
    x = dataset[['GDP_per_capita', 'Health_expenditure', 'Infant_mortality']]
    y = dataset['Life_expectancy']
    x = sm.add_constant(x)
    model = sm.OLS(y, x).fit()
    # Plot
    plt.figure(figsize=(10, 6))
    sns.scatterplot(x='GDP_per_capita', y='Life_expectancy', data=dataset, hue='Country', alpha=0.7)
    sns.regplot(x='GDP_per_capita', y='Life_expectancy', data=dataset, scatter=False, color='black')
    plt.title('Relationship between GDP per capita and life expectancy')
    plt.xlabel('GDP per capita')
    plt.ylabel('Life expectancy')
    plt.grid(True)
    plt.show()
    return model, dataset

# Esempio di chiamata
model_df, data_df = regression_life_expectancy(pil, life, health, infant_mort)
print(model_df.summary())
