"""
Per capita GDP, life expectancy, unemployment, infant mortality over time
"""
import pandas as pd
import matplotlib.pyplot as plt

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

# Comparison of the situation before and after the 2008 economic crisis
def mean_pre_post(df):
    """
    Comparison by years
    Calculate and compare the mean values of a DataFrame between the two periods
    Calculate the percentage change from the first period to the second
    Returns: mean 2000-2007, mean 2009-2019, percentage to change
    """
    df.index = pd.to_numeric(df.index, errors='coerce') # Ensure the index
    df_data = df.loc[(df.index >= 2000) & (df.index <= 2019)]
    pre = df_data.loc[(df_data.index >= 2000) & (df_data.index <= 2007)].mean()
    post = df_data.loc[(df_data.index >= 2009) & (df_data.index <= 2019)].mean()
    result = pd.DataFrame({ # Combine the two periods into a new DataFrame
        'Mean 2000–2007': pre,
        'Mean 2009–2019': post
    })
    result['Δ % post/pre'] = ( # Calculate percentage change
    (result['Mean 2009–2019'] - result['Mean 2000–2007'])
    / result['Mean 2000–2007']
    * 100
    )
    return result.round(2)
