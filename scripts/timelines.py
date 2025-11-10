"""
pil pro capite, aspettativa di vita, disoccupazione, mortalità infantile nel tempo
"""
import pandas as pd
import matplotlib.pyplot as plt

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

# Funzione confronto pre e post crisi economica del 2008
def mean_pre_post(df):
    """
    confronto
    """
    df.index = pd.to_numeric(df.index, errors='coerce')  # forza indice numerico
    df_data = df.loc[(df.index >= 2000) & (df.index <= 2019)]
    pre = df_data.loc[(df_data.index >= 2000) & (df_data.index <= 2007)].mean()
    post = df_data.loc[(df_data.index >= 2009) & (df_data.index <= 2019)].mean()
    result = pd.DataFrame({
        'Mean 2000–2007': pre,
        'Mean 2009–2019': post
    })
    result['Δ % post/pre'] = (
    (result['Mean 2009–2019'] - result['Mean 2000–2007'])
    / result['Mean 2000–2007']
    * 100
    )
    return result.round(2)
