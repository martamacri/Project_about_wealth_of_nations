"""Funzioni per grafici e mappe
"""
import pandas as pd
import matplotlib.pyplot as plt
import cartopy.crs as ccrs
import cartopy.feature as cfeature
from matplotlib.animation import FuncAnimation

# Funzione per grafici nel tempo
def plot_indicator(df, title):
    """
    grafici
    """
    plt.figure(figsize=(15, 8))
    for paese in df.columns:
        plt.plot(df.index, df[paese], marker='o', label=paese)
    plt.xlabel('Year')
    plt.ylabel('Value')
    plt.title(title)
    plt.legend()
    plt.show()

# Andamento nel tempo dei vari indicatori per continente
continents_dict = {
    'Europa': ['ITA', 'ESP', 'DEU', 'SWE'],
    'Nord America': ['USA', 'CAN'],
    'Sud America': ['BRA', 'CHL'],
    'Africa': ['ZAF', 'NGA']
}
def plot_by_continent(df, title):
    """
    grafico per continenti
    """
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

# mappe mondiali crescita annuale (crescita popolazione, pil e aspettativa di vita)
coords = {
    'ITA': (12.5, 42.8), 'ESP': (-3.7, 40.4), 'DEU': (10.5, 51.2), 'SWE': (18.0, 59.3),
    'USA': (-98.0, 39.8), 'CAN': (-106.3, 56.1), 'BRA': (-51.9, -14.2), 
    'CHL': (-70.7, -33.4), 'ZAF': (24.7, -29.0), 'NGA': (8.7, 9.1)
} #coordinate approssimative dei paesi

def melt_indicator(df, indicator_name):
    """
    mappe mondiali
    """
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
    """
    animazione
    """
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
        scatters[c] = ax.scatter(lon,
                                 lat,
                                 color='gray',
                                 s=200,
                                 edgecolor='k',
                                 transform=ccrs.PlateCarree())
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
