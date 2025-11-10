"""
correlazioni
"""
import pandas as pd

# Funzione per calcolare correlazioni per paese
def compute_country_correlations(df_x, df_y, name_x="X", name_y="Y"):
    """
    correlazioni totali
    """
    results = []
    for countries in df_x.columns.intersection(df_y.columns):
        x_vals = df_x[countries]
        y_vals = df_y[countries]
        valid_idx = x_vals.notna() & y_vals.notna()
        corr = x_vals[valid_idx].corr(y_vals[valid_idx]) if valid_idx.sum() > 1 else None
        results.append({
            'Country': countries,
            'X': name_x,
            'Y': name_y,
            'Pearson correlation': corr
        })
    return pd.DataFrame(results)

# Funzione per calcolare rolling correlation per tutti i paesi
def compute_rolling_correlation(df_x, df_y, window=15):
    """
    correlazione nel tempo
    """
    rolling = pd.DataFrame(index=df_x.index)
    for countries in df_x.columns.intersection(df_y.columns):
        x = df_x[countries]
        y = df_y[countries]
        rolling[countries] = x.rolling(window=window, min_periods=3).corr(y)
    return rolling
