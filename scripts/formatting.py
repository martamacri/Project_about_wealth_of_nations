"""
Formatting datasets
"""
def prepare_df(df, df0=None):
    """
    Prepare a DataFrame:
    - remove empty rows
    - extract the years from the first column and put them as an index
    - if a second dataset df0 is passed, keep only the rows (years) common to both

    Parameters:
    - df: The main DataFrame to prepare
    - df0: A second DataFrame to align with df by common years

    Returns:
    - If df0 is None: returns the cleaned df with years as index
    - If df0 is provided: returns a tuple of two DataFrames containing only rows with years common to both
    """
    df = df.dropna(how='all') # Remove rows where all values are NaN
    years = df.iloc[:, 0].astype(str).str.extract(r'(\d+)')[0].astype(int)
    # Extract year from the first column using regex, convert to integer and keep only other columns
    df_data = df.iloc[:, 1:]
    df_data.index = years # Set the extracted years as the index

    if df0 is not None:
        # Prepare df0 in the same way (only years as index)
        df0_clean = df0.dropna(how='all')
        years0 = df0_clean.iloc[:, 0].astype(str).str.extract(r'(\d+)')[0].astype(int)
        df0_data = df0_clean.iloc[:, 1:]
        df0_data.index = years0

        # Find the common years
        common_years = df_data.index.intersection(df0_data.index)

        # Keep only the years common to both
        df_data = df_data.loc[common_years]
        df0_data = df0_data.loc[common_years]

        return df_data, df0_data

    return df_data
