"""
Data cleansing and transformation.
"""
import pandas as pd

# Indicator 1: gdp per capita
df1 = pd.read_csv('data/gdp_per_capita_1995_2024.csv')
print(df1.head())
print(df1.info()) # number of rows, number of columns, type
# There are no null values in the data and they are all numbers
print(df1.describe()) # Descriptive statistics
# No pre-processing is needed

# Indicator 2: gdp
df2 = pd.read_csv('data/gdp_1995_2024.csv')
print(df2.head())
print(df2.info())
# There are no null values in the data and they are all numbers
print(df2.describe()) # Descriptive statistics
# No pre-processing is needed

# Indicator 3: life expextacy
df3 = pd.read_csv('data/life_expectacy_1995_2024.csv')
print(df3.head())
print(df3.info()) # They are all numbers, but there are missing values
print(df3.describe()) # Descriptive statistics
# There is a missing line
row_missing_count = df3.isnull().any(axis=1).sum() # Count of rows with at least one NaN value
print(row_missing_count) # One is missing
row = df3[df3.isnull().any(axis=1)] # Visualisation of the missing line
print(row) # I have no values for 2024
df3_clean = df3.dropna() # delete row with NaN
print(df3_clean.tail()) # tail returns the last 5 lines
df3_clean.to_csv("life_expectacy_1995_2023.csv", index=False)
print("\nSaved: life_expectacy_1995_2023.csv")

# Indicator 4: health expenditure
df4 = pd.read_csv('data/health_expenditure_1995_2024.csv')
print(df4.head())
print(df4.info()) # They are all numbers, but there are missing values
print(df4.describe()) # Descriptive statistics
# Many missing values
row_missing_count = df4.isnull().any(axis=1).sum() #Count of rows with at least one NaN value
print(row_missing_count) # 7 lines with missing values
row = df4[df4.isnull().any(axis=1)] #Visualisation of the missing line
print(row) # I don't have any figures for 1995 to 1999 or for 2023-2024
row_count = row.isnull().sum(axis=1) # count NaN for row
print(row_count) # I note that 2023 has some values
# I remove the values for the rows from 1995 to 1999 and 2024
years_drop = ['YR1995', 'YR1996', 'YR1997', 'YR1998', 'YR1999', 'YR2024']
df4_clean = df4[~df4['Year'].isin(years_drop)]
# Let's see if it's worth keeping the 2023 data
rows_with_missing = df4_clean[df4_clean.isnull().any(axis=1)] # Visualisation of the missing line now
print(rows_with_missing) # I don't have Brazil, Spain, Nigeria, the United States, or South Africa
print(df4_clean.head())
df4_clean = df4_clean[df4_clean['Year'] != 'YR2023']
print(df4_clean.tail()) # tail returns the last 5 lines
df4_clean.to_csv('health_expenditure_2000_2022.csv', index=False)
print("\nSaved: life_expectacy_2000_2022.csv")

# Indicator 5: Infant mortality
df5 = pd.read_csv('data/infant_mortality_1995_2024.csv')
print(df5.head())
print(df5.info()) # They are all numbers, but there are missing values
print(df5.describe()) # Descriptive statistics
# There is a missing line
row_missing_count = df5.isnull().any(axis=1).sum() #Count of rows with at least one NaN value
print(row_missing_count) # One is missing
row = df5[df5.isnull().any(axis=1)] # Visualisation of the missing line
print(row) # I have no values for 2024
df5_clean = df5.dropna()
print(df5_clean.tail()) # tail returns the last 5 lines
df5_clean.to_csv("infant_mortality_1995_2023.csv", index=False)
print("\nSaved: infant_mortality_1995_2023.csv")

# Indicator 6: Unemployment
df6 = pd.read_csv('data/unemployment_1995_2024.csv')
print(df6.head())
print(df6.info())
# There are no null values in the data and they are all numbers
print(df6.describe()) # Descriptive statistics
# No pre-processing is needed

# Indicator 7: Population growth
df7 = pd.read_csv('data/population_growth_1995_2024.csv')
print(df7.head())
print(df7.info())
# There are no null values in the data and they are all numbers
print(df7.describe()) # Descriptive statistics
# No pre-processing is needed
