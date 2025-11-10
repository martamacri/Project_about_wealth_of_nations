"""
indicatore di benessere
"""
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
