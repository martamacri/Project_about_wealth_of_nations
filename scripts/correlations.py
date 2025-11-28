"""
Correlations between indicators
"""
import pandas as pd

# Function to calculate correlations by country
def compute_country_correlations(df_x, df_y, name_x="X", name_y="Y"):
    """
    Compute Pearson correlations between two datasets for each country
    Return a summary table with correlations for all countries
    Parameters: df x, df y. Two datasets about two different indicators
    Returns: country, x, y, correlation
    """
    results = []
    for countries in df_x.columns.intersection(df_y.columns): # Loop over countries
        x_vals = df_x[countries]
        y_vals = df_y[countries]
        valid_idx = x_vals.notna() & y_vals.notna() #identify valid values
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
    Compute rolling Pearson correlation over time for multiple countries
    Useful to see how correlations evolve over time
    Window: numbers of years
    Returns dataset where each cell contains the rolling correlation at that year for the country
    """
    rolling = pd.DataFrame(index=df_x.index) # Create an empty DataFrame
    for countries in df_x.columns.intersection(df_y.columns): # Loop over countries
        x = df_x[countries]
        y = df_y[countries]
        rolling[countries] = x.rolling(window=window, min_periods=3).corr(y)
        # min_periods=3 ensures at least 3 valid observations are needed for correlation
    return rolling
