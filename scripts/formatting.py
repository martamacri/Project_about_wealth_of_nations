"""
Formatting datasets
"""
def prepare_df(df, df0=None):
    """
    Prepara un DataFrame:
    - rimuove righe vuote
    - estrae gli anni dalla prima colonna e li mette come indice
    - se viene passato df2, mantiene solo le righe (anni) comuni a entrambi
    """
    df = df.dropna(how='all')
    years = df.iloc[:, 0].astype(str).str.extract(r'(\d+)')[0].astype(int)
    df_data = df.iloc[:, 1:]
    df_data.index = years

    if df0 is not None:
        # Prepara anche df0 nello stesso modo (solo anni come indice)
        df0_clean = df0.dropna(how='all')
        years0 = df0_clean.iloc[:, 0].astype(str).str.extract(r'(\d+)')[0].astype(int)
        df0_data = df0_clean.iloc[:, 1:]
        df0_data.index = years0

        # Trova gli anni comuni
        common_years = df_data.index.intersection(df0_data.index)

        # Mantieni solo gli anni comuni in entrambi
        df_data = df_data.loc[common_years]
        df0_data = df0_data.loc[common_years]

        return df_data, df0_data

    return df_data
