"""
Module for performing linear regressions on life expectancy
using GDP per capita, health expenditure and infant mortality.
It also produces a scatterplot with linear regression for GDP per capita.
"""

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import statsmodels.api as sm

sns.set(style="whitegrid")

def regression_life_expectancy(pil_df, life_df, health_df, infant_mort_df):
    """
    Performs a linear regression on Life Expectancy using:
    - GDP per capita
    - Health Expenditure
    - Infant Mortality

    Combine multiple country-level datasets, align them by country and year,
    build a panel-style dataset, and fit an OLS regression model where 
    Life Expectancy is the dependent variable.

    Returns: coefficient, plot
    """

    # Find common countries and years (not necessary, but to be sure)
    countries = pil_df.columns.intersection(life_df.columns) \
                              .intersection(health_df.columns) \
                              .intersection(infant_mort_df.columns)

    common_years = pil_df.index.intersection(life_df.index) \
                               .intersection(health_df.index) \
                               .intersection(infant_mort_df.index)

    # Builds datasets with year-country rows
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

    dataset = pd.concat(data_rows, ignore_index=True).dropna() # Concatenate all countries into one panel dataset

    # Linear regression
    x = dataset[['GDP_per_capita', 'Health_expenditure', 'Infant_mortality']]
    y = dataset['Life_expectancy']

    x = sm.add_constant(x) # Add constant term for intercept in regression
    model = sm.OLS(y, x).fit()

    # Plot
    plt.figure(figsize=(10, 6))
    sns.scatterplot( # Scatter plot
        x='GDP_per_capita',
        y='Life_expectancy',
        data=dataset,
        hue='Country',
        alpha=0.7
    )
    sns.regplot( # Add regression line
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
