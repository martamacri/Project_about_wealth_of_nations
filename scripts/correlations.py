"""
correlazioni
"""
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from formatting import prepare_df
sns.set(style="whitegrid")

df1 = pd.read_csv('data/gdp_per_capita_1995_2024.csv')
df3 = pd.read_csv('data/life_expectacy_1995_2023.csv')
df4 = pd.read_csv('data/health_expenditure_2000_2022.csv')
df5 = pd.read_csv('data/infant_mortality_1995_2023.csv')
df6 = pd.read_csv('data/unemployment_1995_2024.csv')
# Pulizia e preparazione dei DataFrame
pil = prepare_df(df1)
life = prepare_df(df3)
health = prepare_df(df4)
unemp = prepare_df(df5)
infant_mort = prepare_df(df6)

# Lista delle comparazioni
comparisons = [
    ("GDP per capita", pil, "Life expectancy", life),
    ("Unemployment", unemp, "Life expectancy", life),
    ("GDP per capita", pil, "Health expenditure", health),
    ("GDP per capita", pil, "Infant mortality", infant_mort),
    ("Health expenditure", health, "Infant mortality", infant_mort)
]

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

# Calcolo delle correlazioni
corr_df_list = [compute_country_correlations(df_x, df_y, name_x, name_y)
                for name_x, df_x, name_y, df_y in comparisons]
corr_df = pd.concat(corr_df_list, ignore_index=True)
print(corr_df)

# Correlazione mobile tra PIL pro capite e aspettativa di vita
WINDOW = 15
rolling_corr = compute_rolling_correlation(pil, life, window=WINDOW)

# Plot della correlazione mobile
plt.figure(figsize=(14, 8))
for country in rolling_corr.columns:
    plt.plot(rolling_corr.index, rolling_corr[country], label=country)
plt.title(f"Rolling correlation ({WINDOW} years) between GDP per capita and life expectancy")
plt.xlabel("Year")
plt.ylabel("Pearson's correlation")
plt.legend()
plt.grid(True)
plt.show()
