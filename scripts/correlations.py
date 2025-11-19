"""
Correlations between indicators
"""
import pandas as pd

# Function to calculate correlations by country
def compute_country_correlations(df_x, df_y, name_x="X", name_y="Y"):
    """
    Total correlations
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

# Function to calculate rolling correlation for all countries
def compute_rolling_correlation(df_x, df_y, window=15):
    """
    Correlation over time
    """
    rolling = pd.DataFrame(index=df_x.index)
    for countries in df_x.columns.intersection(df_y.columns):
        x = df_x[countries]
        y = df_y[countries]
        rolling[countries] = x.rolling(window=window, min_periods=3).corr(y)
    return rolling
