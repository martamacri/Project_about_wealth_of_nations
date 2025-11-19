"""
Module for downloading and managing economic data from the World Bank
"""
import wbgapi as wb
import pandas as pd

# To see all indicators in the library
# for indicator in wb.series.list():
#    print(indicator['id'], "-", indicator['value'])
# There are so many, so just choose a few.
# To see all the countries in the library.
# for country in wb.economy.list():
#    print(country['id'], "-", country['value'])
# But there are so many even in this case, choose only a few.

# I download the CSV files indicator by indicator.

# Indicator 1: GDP per capita, current US$
GPD_PC = 'NY.GDP.PCAP.CD'
countries = ['ITA', 'ESP', 'DEU', 'SWE', 'USA', 'CAN', 'BRA', 'CHL', 'ZAF', 'NGA']
years = range(1995, 2025)
df1 = wb.data.DataFrame(GPD_PC, countries, time=years)
df1 = df1.T
df1.index.name = 'Year'
df1 = df1.apply(pd.to_numeric, errors='coerce')
print(df1.head())
df1.to_csv('gdp_per_capita_1995_2024.csv', float_format='%.2f')
print("\nSaved: gdp_per_capita_1995_2024.csv")

# Indicator 2: GDP
GPD = 'NY.GDP.MKTP.CD'
countries = ['ITA', 'ESP', 'DEU', 'SWE', 'USA', 'CAN', 'BRA', 'CHL', 'ZAF', 'NGA']
years = range(1995, 2025)
df2 = wb.data.DataFrame(GPD, countries, time=years)
df2 = df2.T
df2.index.name = 'Year'
df2 = df2.apply(pd.to_numeric, errors='coerce')
print(df2.head())
df2.to_csv('gdp_1995_2024.csv', float_format='%.2f')
print("\nSaved: gdp_1995_2024.csv")

# Indicator 3: Life expectancy
LIFE = 'SP.DYN.LE00.IN'
countries = ['ITA', 'ESP', 'DEU', 'SWE', 'USA', 'CAN', 'BRA', 'CHL', 'ZAF', 'NGA']
years = range(1995, 2025)
df3 = wb.data.DataFrame(LIFE, countries, time=years)
df3 = df3.T
df3.index.name = 'Year'
df3 = df3.apply(pd.to_numeric, errors='coerce')
print(df3.head())
df3.to_csv('life_expectacy_1995_2024.csv', float_format='%.2f')
print("\nSaved: life_expectacy_1995_2024.csv")

# Indicator 4: Health expenditure
HEALTH = 'SH.XPD.CHEX.PC.CD'
countries = ['ITA', 'ESP', 'DEU', 'SWE', 'USA', 'CAN', 'BRA', 'CHL', 'ZAF', 'NGA']
years = range(1995, 2025)
df4 = wb.data.DataFrame(HEALTH, countries, time=years)
df4 = df4.T
df4.index.name = 'Year'
df4 = df4.apply(pd.to_numeric, errors='coerce')
print(df4.head())
df4.to_csv('health_expenditure_1995_2024.csv', float_format='%.2f')
print("\nSaved: health_expenditure_1995_2024.csv")

# Indicator 5: Infant mortality
INFANT = 'SH.DYN.MORT'
countries = ['ITA', 'ESP', 'DEU', 'SWE', 'USA', 'CAN', 'BRA', 'CHL', 'ZAF', 'NGA']
years = range(1995, 2025)
df5 = wb.data.DataFrame(INFANT, countries, time=years)
df5 = df5.T
df5.index.name = 'Year'
df5 = df5.apply(pd.to_numeric, errors='coerce')
print(df5.head())
df5.to_csv('infant_mortality_1995_2024.csv', float_format='%.2f')
print("\nSaved: infant_mortality_1995_2024.csv")

# Indicator 6: Unemployment
UNEMP = 'SL.UEM.TOTL.ZS'
countries = ['ITA', 'ESP', 'DEU', 'SWE', 'USA', 'CAN', 'BRA', 'CHL', 'ZAF', 'NGA']
years = range(1995, 2025)
df6 = wb.data.DataFrame(UNEMP, countries, time=years)
df6 = df6.T
df6.index.name = 'Year'
df6 = df6.apply(pd.to_numeric, errors='coerce')
print(df6.head())
df6.to_csv('unemployment_1995_2024.csv', float_format='%.2f')
print("\nSaved: unemployment_1995_2024.csv")

# Indicator 7: Population growth
POP = 'SP.POP.GROW'
countries = ['ITA', 'ESP', 'DEU', 'SWE', 'USA', 'CAN', 'BRA', 'CHL', 'ZAF', 'NGA']
years = range(1995, 2025)
df7 = wb.data.DataFrame(POP, countries, time=years)
df7 = df7.T
df7.index.name = 'Year'
df7 = df7.apply(pd.to_numeric, errors='coerce')
print(df7.head())
df7.to_csv('population_growth_1995_2024.csv', float_format='%.2f')
print("\nSaved: population_growth_1995_2024.csv")
