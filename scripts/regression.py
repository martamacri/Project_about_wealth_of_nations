"""
Modulo per eseguire regressioni lineari sulla Life Expectancy
utilizzando GDP per capita, Health Expenditure e Infant Mortality.
Produce anche uno scatterplot con regressione lineare per GDP per capita.
"""

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import statsmodels.api as sm

sns.set(style="whitegrid")

def regression_life_expectancy(pil_df, life_df, health_df, infant_mort_df):
    """
    Esegue una regressione lineare su Life Expectancy usando:
    - GDP per capita
    - Health Expenditure
    - Infant Mortality
    """

    # Trova paesi e anni comuni
    countries = pil_df.columns.intersection(life_df.columns) \
                              .intersection(health_df.columns) \
                              .intersection(infant_mort_df.columns)

    common_years = pil_df.index.intersection(life_df.index) \
                               .intersection(health_df.index) \
                               .intersection(infant_mort_df.index)

    # Costruisce dataset con righe anno-paese
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

    dataset = pd.concat(data_rows, ignore_index=True).dropna()

    # Regressione lineare
    x = dataset[['GDP_per_capita', 'Health_expenditure', 'Infant_mortality']]
    y = dataset['Life_expectancy']

    x = sm.add_constant(x)
    model = sm.OLS(y, x).fit()

    # Plot
    plt.figure(figsize=(10, 6))
    sns.scatterplot(
        x='GDP_per_capita',
        y='Life_expectancy',
        data=dataset,
        hue='Country',
        alpha=0.7
    )
    sns.regplot(
        x='GDP_per_capita',
        y='Life_expectancy',
        data=dataset,
        scatter=False,
        color='black'
    )

    plt.title('Relationship between GDP per capita and life expectancy')
    plt.xlabel('GDP per capita')
    plt.ylabel('Life expectancy')
    plt.grid(True)
    plt.show()

    return model, dataset
