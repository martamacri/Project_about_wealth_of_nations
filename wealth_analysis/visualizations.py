# Funzioni per grafici e mappe
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import cartopy.crs as ccrs
import cartopy.feature as cfeature
from matplotlib.animation import FuncAnimation
import warnings
warnings.filterwarnings("ignore")

df1 = pd.read_csv('data/gdp_per_capita_1995_2024.csv')
df2 = pd.read_csv('data/gdp_1995_2024.csv')
df3 = pd.read_csv('data/life_expectacy_1995_2023.csv')
df4 = pd.read_csv('data/health_expenditure_2000_2022.csv')
df5 = pd.read_csv('data/infant_mortality_1995_2023.csv')
df6 = pd.read_csv('data/unemployment_1995_2024.csv')
df7 = pd.read_csv('data/population_growth_1995_2024.csv')

sns.set(style="whitegrid")

# Andamento nel tempo dei vari indicatori per paese
def plot_time_series(df, title, figsize=(15,8), marker='o'):
    df = df.dropna(how='all')
    Years = df.iloc[:, 0].astype(str).str.extract(r'(\d+)')[0].astype(int)
    df = df.iloc[:, 1:]
    min_len = min(len(Years), len(df))
    Years = Years.iloc[:min_len]
    df = df.iloc[:min_len, :]
    plt.figure(figsize=figsize)
    for paese in df.columns:
        plt.plot(Years, df[paese], marker=marker, label=paese)
    plt.xlabel('Year')
    plt.ylabel('Value')
    plt.title(title)
    plt.legend()
    plt.show()
plot_time_series(df1, 'Evolution of GDP per capita over time by country')
plot_time_series(df2, 'Evolution of GDP over time by country')
plot_time_series(df3, 'Evolution of life expectancy over time by country')
plot_time_series(df4, 'Evolution of health expenditure over time by country')
plot_time_series(df5, 'Evolution of infant mortality over time by country')
plot_time_series(df6, 'Evolution of unemployment over time by country')
plot_time_series(df7, 'Evolution of population growth over time by country')

# Andamento nel tempo dei vari indicatori per continente
continents_dict = {
    'Europa': ['ITA', 'ESP', 'DEU', 'SWE'],
    'Nord America': ['USA', 'CAN'],
    'Sud America': ['BRA', 'CHL'],
    'Africa': ['ZAF', 'NGA']
}
def plot_by_continent(df, title):
    df = df.dropna(how='all')
    Years = df.iloc[:, 0].astype(str).str.extract(r'(\d+)')[0].astype(int)
    df = df.iloc[:, 1:]
    df.index = Years
    df_continent = pd.DataFrame({
        continent: df[countries].mean(axis=1)
        for continent, countries in continents_dict.items()
    })
    plt.figure(figsize=(15, 8))
    for continent in df_continent.columns:
        plt.plot(df_continent.index, df_continent[continent],
                 marker='o', label=continent)
    plt.xlabel('Year')
    plt.ylabel('Mean value')
    plt.title(title)
    plt.legend(title='Continents')
    plt.show()
plot_by_continent(df1, 'Evolution of GDP per capita over time by continent')
plot_by_continent(df2, 'Evolution of GDP over time by continent')
plot_by_continent(df3, 'Evolution of life expectancy over time by continent')
plot_by_continent(df4, 'Evolution of health expenditure over time by continent')
plot_by_continent(df5, 'Evolution of infant mortality over time by continent')
plot_by_continent(df6, 'Evolution of unemployment over time by continent')
plot_by_continent(df7, 'Evolution of population growth over time by continent')

# La correlazione tra il pil pro capite e l'aspettativa di vita cambia nel tempo? per ogni paese (serie temporale)
def prepare_df(df):
    df = df.dropna(how='all')
    Years = df.iloc[:, 0].astype(str).str.extract(r'(\d+)')[0].astype(int)
    df_data = df.iloc[:, 1:]
    df_data.index = Years
    return df_data
pil = prepare_df(df1)
life = prepare_df(df3)
window = 15
countries = pil.columns  
common_years = pil.index.intersection(life.index)  
rolling_corr = pd.DataFrame(index=common_years)
for country in countries:
    x = pil.loc[common_years, country]
    y = life.loc[common_years, country]
    corr = (
        x.rolling(window=window, min_periods=3)
         .corr(y)
    )
    rolling_corr[country] = corr
plt.figure(figsize=(14, 8))
for country in rolling_corr.columns:
    plt.plot(rolling_corr.index, rolling_corr[country], label=country)
plt.title(f"Mobile correlation ({window} years) between GDP per capita and life expectancy")
plt.xlabel("Year")
plt.ylabel("Pearson's correlation")
plt.legend()
plt.grid(True)
plt.show()

# mappe mondiali crescita annuale (crescita popolazione, pil e aspettativa di vita)
coords = {
    'ITA': (12.5, 42.8), 'ESP': (-3.7, 40.4), 'DEU': (10.5, 51.2), 'SWE': (18.0, 59.3),
    'USA': (-98.0, 39.8), 'CAN': (-106.3, 56.1), 'BRA': (-51.9, -14.2), 
    'CHL': (-70.7, -33.4), 'ZAF': (24.7, -29.0), 'NGA': (8.7, 9.1)
}
def melt_indicator(df, indicator_name):
    df_copy = df.copy()
    if not df_copy.index.astype(str).str.startswith('YR').any():
        year_col = [c for c in df_copy.columns if 'YR' in str(c).upper()]
        if year_col:
            df_copy = df_copy.set_index(year_col[0])
    df_copy.index = df_copy.index.astype(str).str.replace('YR','').astype(int)
    df_copy = df_copy.loc[:, df_copy.columns.str.fullmatch(r'[A-Z]{3}')]
    df_long = df_copy.rename_axis('year').reset_index().melt(
        id_vars='year', var_name='country', value_name=indicator_name
    )
    df_long[indicator_name] = pd.to_numeric(df_long[indicator_name], errors='coerce')
    return df_long
def animate_indicator(df_long, indicator_name, cmap='viridis', save=False):
    years = sorted(df_long['year'].unique())
    vmin, vmax = df_long[indicator_name].min(), df_long[indicator_name].max()
    fig = plt.figure(figsize=(12,6))
    ax = plt.axes(projection=ccrs.PlateCarree())
    ax.set_global()
    ax.add_feature(cfeature.LAND, facecolor='lightgray')
    ax.add_feature(cfeature.OCEAN, facecolor='lightblue')
    ax.add_feature(cfeature.BORDERS, linestyle=':')
    ax.set_title(f"{indicator_name}", fontsize=14)
    cmap_obj = plt.cm.get_cmap(cmap)
    norm = plt.Normalize(vmin=vmin, vmax=vmax)
    scatters = {}
    for c, (lon, lat) in coords.items():
        scatters[c] = ax.scatter(lon, lat, color='gray', s=200, edgecolor='k', transform=ccrs.PlateCarree())
    sm = plt.cm.ScalarMappable(cmap=cmap_obj, norm=norm)
    sm.set_array([])
    cbar = plt.colorbar(sm, ax=ax, orientation='vertical', fraction=0.046, pad=0.04)
    cbar.set_label(indicator_name)
    def update(year):
        ax.set_title(f"{indicator_name} – anno {year}", fontsize=14)
        df_year = df_long[df_long['year'] == year]
        for _, row in df_year.iterrows():
            val = row[indicator_name]
            color = cmap_obj(norm(val))
            scatters[row['country']].set_color(color)
        return scatters.values()
    anim = FuncAnimation(fig, update, frames=years, blit=False, repeat=False)
    if save:
        anim.save(f"{indicator_name.replace(' ', '_')}.gif", writer='pillow', fps=2)
    else:
        plt.show()
ind_pil = melt_indicator(df2, 'GDP')
ind_life = melt_indicator(df3, 'Life expectancy')
ind_growth = melt_indicator(df7, 'Population growth')
animate_indicator(ind_pil, 'GDP', cmap='plasma')
animate_indicator(ind_life, 'Life expectancy', cmap='viridis')
animate_indicator(ind_growth, 'Population growth', cmap='coolwarm')