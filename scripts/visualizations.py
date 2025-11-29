"""
Functions for graphs and maps
"""
import pandas as pd
import matplotlib.pyplot as plt
import cartopy.crs as ccrs
import cartopy.feature as cfeature
from matplotlib.animation import FuncAnimation

# Function for graphs over time
def plot_indicator(df, title):
    """
    Graphs over time
    Plot the values of an indicator over time for multiple countries
    Create a line plot showing the evolution of values in the DataFrame over the years
    """
    plt.figure(figsize=(15, 8))
    for paese in df.columns: # Loop over each column
        plt.plot(df.index, df[paese], marker='o', label=paese)
    plt.xlabel('Year')
    plt.ylabel('Value')
    plt.title(title)
    plt.legend()
    plt.show()

# Trends over time for various indicators by continent
continents_dict = {
    'Europe': ['ITA', 'ESP', 'DEU', 'SWE'],
    'North America': ['USA', 'CAN'],
    'South America': ['BRA', 'CHL'],
    'Africa': ['ZAF', 'NGA']
}
def plot_by_continent(df, title):
    """
    Graph by continent
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

# World maps showing annual growth (population growth, GDP and life expectancy)
coords = {
    'ITA': (12.5, 42.8), 'ESP': (-3.7, 40.4), 'DEU': (10.5, 51.2), 'SWE': (18.0, 59.3),
    'USA': (-98.0, 39.8), 'CAN': (-106.3, 56.1), 'BRA': (-51.9, -14.2), 
    'CHL': (-70.7, -33.4), 'ZAF': (24.7, -29.0), 'NGA': (8.7, 9.1)
} # Approximate coordinates of countries

def melt_indicator(df, indicator_name):
    """
    World maps
    Convert a wide-format indicator DataFrame into a long-format table with columns
    Returns:
    A long-format DataFrame with columns:
    - 'year' (int)
    - 'country' (str, ISO-3 code)
    - indicator_name (float)
    """
    df_copy = df.copy()
    if not df_copy.index.astype(str).str.startswith('YR').any():
        year_col = [c for c in df_copy.columns if 'YR' in str(c).upper()]
        if year_col:
            df_copy = df_copy.set_index(year_col[0])
    df_copy.index = df_copy.index.astype(str).str.replace('YR','').astype(int)
    # Convert from wide to long format:
    df_long = df_copy.rename_axis('year').reset_index().melt(
        id_vars='year', var_name='country', value_name=indicator_name
    )
    return df_long

def animate_indicator(df_long, indicator_name, cmap='viridis', save=False):
    """
    Create an animated world visualization of an indicator over time.
    The function takes a long-format DataFrame containing (year, country, value)
    and generates an animation in which each country is represented as a dot on
    a world map.
    The color of each dot changes according to the indicator's value for that year.
    Displays the animation or saves it as a GIF.
    """
    years = sorted(df_long['year'].unique()) # Extract available years
    vmin, vmax = df_long[indicator_name].min(), df_long[indicator_name].max() # Get min max for normalization
    fig = plt.figure(figsize=(12,6)) # Prepare the figure and world map
    ax = plt.axes(projection=ccrs.PlateCarree())
    ax.set_global()
    ax.add_feature(cfeature.LAND, facecolor='lightgray') # Add map features
    ax.add_feature(cfeature.OCEAN, facecolor='lightblue')
    ax.add_feature(cfeature.BORDERS, linestyle=':')
    ax.set_title(f"{indicator_name}", fontsize=14)
    cmap_obj = plt.cm.get_cmap(cmap) # Prepare colormap and normalization
    norm = plt.Normalize(vmin=vmin, vmax=vmax)
    scatters = {} # Create scatter dots for each country
    for c, (lon, lat) in coords.items():
        scatters[c] = ax.scatter(lon,
                                 lat,
                                 color='gray',
                                 s=200, # dot's size
                                 edgecolor='k',
                                 transform=ccrs.PlateCarree())
    sm = plt.cm.ScalarMappable(cmap=cmap_obj, norm=norm) # Add a colorbar legend
    sm.set_array([])
    cbar = plt.colorbar(sm, ax=ax, orientation='vertical', fraction=0.046, pad=0.04)
    cbar.set_label(indicator_name)
    def update(year): # Update function executed once per frame (year)
        ax.set_title(f"{indicator_name} – anno {year}", fontsize=14)
        df_year = df_long[df_long['year'] == year]
        for _, row in df_year.iterrows(): # Update each dot's color with the indicator value for the given year
            val = row[indicator_name]
            color = cmap_obj(norm(val))
            scatters[row['country']].set_color(color)
        return scatters.values()
    anim = FuncAnimation(fig, update, frames=years, blit=False, repeat=False) # Create animation
    if save: # Display the animation
        anim.save(f"{indicator_name.replace(' ', '_')}.gif", writer='pillow', fps=2)
    else:
        plt.show()
