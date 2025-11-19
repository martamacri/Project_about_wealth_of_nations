"""
Summary well-being index that summarises all well-being indices
(life expectancy, healthcare expenditure, infant mortality).
I normalise the data so that they all have the same order.
"""

def compute_wellbeing_index(life_df, health_df, infant_df):
    """
    Calculates a summary index of well-being by country and year
    based on life expectancy, healthcare expenditure and infant mortality.
    """
    countries_df = life_df.columns.intersection(health_df.columns)\
                               .intersection(infant_df.columns)
    common_years_df = life_df.index.intersection(health_df.index)\
                                 .intersection(infant_df.index)
    life_clean = life_df.loc[common_years_df, countries_df]
    health_clean = health_df.loc[common_years_df, countries_df]
    infant_clean = infant_df.loc[common_years_df, countries_df]

    # Reverse infant mortality (higher is better)
    infant_inv = infant_clean.max().max() - infant_clean

    # Min-max normalisation
    def minmax_normalize(df):
        return (df - df.min()) / (df.max() - df.min())

    life_norm = minmax_normalize(life_clean)
    health_norm = minmax_normalize(health_clean)
    infant_norm = minmax_normalize(infant_inv)

    # Composite well-being index (average of the three)
    wellbeing_index_df = (life_norm + health_norm + infant_norm) / 3

    return wellbeing_index_df, countries_df
