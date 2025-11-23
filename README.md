# Python project about the wealth of nations
## Project proposal
Dive into the intricate relationship between a country's economic prosperity and the well-being of its population. 
This project invites you to explore decades of global development data to uncover trends and correlations. 
You could analyze how indicators like GDP per capita relate to life expectancy, healthcare spending, or child mortality rates. 
Create compelling visualizations, such as time-series charts or global maps, to tell a story about global health and economics. 
The goal is to build an analytical project that reveals patterns in how nations thrive. 

## Index
1. [Introduction](#introduction)
2. [Data](#data)
3. [Installation](#installation-data)
4. [Analysis](#analysis)
5. [Conclusion](#conclusion)

## Introduction
The project analyses the complex relationship between economic prosperity and the well-being of the population in certain countries around the world. 
It analyses data trends over recent years to identify significant correlations and patterns.
The main objective is to understand how economic indicators, such as GDP per capita, are associated with key public health measures, including life expectancy, health expenditure and infant mortality rates.
In addition, effective visualisations, such as time series graphs or global maps, will be created to better understand the connection between economics and health around the world.
In summary, the goal is to build an analysis that highlights the patterns through which nations prosper.
To carry out the project, Visual Studio Code (VS Code) was used. For this reason, the codes and explanations provided in this file were based on the functionality of this software.

## Data
The data used in the project comes from the Python library 'wbgapi'. The library is built using data from World Bank Open Data, a database that provides free access to data on global development.
To use this library, before using the project scripts, you must install it in the terminal of VS Code using the following code:
```python -m pip install wbgapi```.

As previously mentioned, 'wbgapi' is a Python library that provides simple and structured access to World Bank data.
It allows you to download economic, social and environmental indicators, explore metadata and organise data in Pandas DataFrames for analysis and visualisation.
It is particularly useful for global data analysis and international development projects, as in this case.

For this reason, the library contains a large amount of data.
To limit the analysis, only some of them were selected, based on location, time and available indicators:
* Not all available countries are used, but 10 have been selected. These are countries that differ in terms of economic development, are spread across multiple geographical areas and represent different economic and social models:
  - Europe: Italy (ITA), Spain (ESP), Germany (DEU), Sweden (SWE)
  - North America: United States (US), Canada (CAN)
  - South America: Brazil (BRA), Chile (CHL)
  - Africa: South Africa (ZAF), Nigeria (NGA)
* Data from 1995 to 2024 has been selected because the data for 2025 has not yet been uploaded for all indicators. This gives a time period of about 30 years, which shows how the selected indicators have changed over the years.
* Selected indicators for analysis:
  - 'GDP per capita': 'NY.GDP.PCAP.CD' that represents the average wealth per person
  - 'GDP': 'NY.GDP.MKTP.CD' that represents the total wealth of a country
  - 'Life expectancy': 'SP.DYN.LE00.IN' that represents the average number of years of life from birth
  - 'Health expenditure': 'SH.XPD.CHEX.PC.CD' that represents the average healthcare expenditure per person
  - 'Infant mortality': 'SH.DYN.MORT' that represents the infant mortality rate per 1000 live births
  - 'Unemployment': 'SL.UEM.TOTL.ZS' that represents the percentage of the workforce that is unemployed
  - 'Population growth': 'SP.POP.GROW' that represents the annual growth rate

## Installation data
To install the files containing the data used, the first code to view is in the 'download data' folder, which is separate from the rest of the scripts so that too many CSV files are not downloaded into the GitHub repository.
The first code used is 'data_loader', which downloads the data from the 'wbgapi' library and exports it into seven CSV files divided according to the seven selected indices. The data is structured with countries as columns and years as rows, and obviously the data inside indicates the data for that particular indicator in that year and in that country.
Unfortunately, the initial idea was to have all the data for all the indicators in a single dataset, but this was not possible because there would be too much data and the code would generate an error.
When the 'data_loader' code is run, 7 CSV files are created for the 7 indicators, containing the data for the 10 countries and 30 years considered.

Before moving on to the actual analyses, we need to run the 'preprocessing' code, which includes general analyses of the individual datasets and the related cleaning, useful for organising the data in a way that can be used for the following analyses.
With this process, we note that:
- The 'Life expectancy' dataset has 1 row with missing values: there are no values for 2024, so it is deleted from this dataset.
- The 'Health expenditure' dataset has seven rows with missing values: there are no values from 1995 to 1999 and for 2024, while the values for 2023 are only available for some countries (five out of ten). The 6 rows without data are deleted immediately, but for 2023, I understand if it makes sense to keep them. In the end, the 2023 is also deleted because for the analyses that will be carried out, it does not make sense to attempt to impute the missing values.
- The 'Infant mortality' dataset has 1 row with missing values: there are no values for 2024, so it is removed from this dataset.

The three datasets with null values were then fixed for future analysis. These datasets are downloaded in the new version in CSV format. For convenience, the previous version of these data is deleted from the 'data' folder.

## Analysis 
The goal of this project is to explore the relationship between economic wealth and social well-being by analysing the history of health and economics at a global level.
By investigating trends and correlations in global development across all selected countries, the project attempts to identify key patterns in national development.
The analyses include correlations, temporal trends and geographical comparisons, all implemented within functions in the 'script' folder.
To obtain the results and view the output, it is necessary to run the main Python code contained in the 'main.py' file, which is located outside the 'script' folder.
In summary, this is a socio-economic data analysis project designed to understand how the economy influences the well-being of populations over time and space.

The analyses conducted are:
* Time series analysis:
  - Per capita GDP over time
  - Life expectancy over time
  - Unemployment over time
  - Infant mortality over time
  - Comparison before and after the 2008 economic crisis: average GDP per capita, life expectancy, unemployment and infant mortality split into 2000-2007 and 2009-2019
* Correlations:
  - GDP per capita vs life expectancy
  - Unemployment vs life expectancy
  - GDP per capita vs healthcare expenditure per capita
  - GDP per capita vs infant mortality rates
  - Healthcare expenditure per capita vs infant mortality
  - Does this correlation change over time? Time series for countries
* Linear regression: to see how much the variables GDP per capita, health expenditure and infant mortality affect the variable life expectancy. The output consists of the regression coefficients and the scatter plot graph of the regression.
* Creation of a synthetic well-being index that summarises all well-being indices (life expectancy, healthcare expenditure, infant mortality).
* Cluster analysis: groups countries according to their economic and health indicators.
* Global visualizations:
  - Various charts:
    - Trends over time for various indicators by country
    - Trends over time for various indicators by continent
  - World map showing annual growth
  - World map showing overall GDP
  - World map showing life expectancy

## Conclusion
The project provides tools and visualisations to understand how the economy and public health are related over time and space.

A Jupiter notebook has been created in the 'presentation' folder to visualise the codes used with their outputs. In addition, comments have been added to the outputs to achieve the goal of this project.

From the temporal analysis, we can see that per capita GDP has increased in almost all countries over the last 20 years, except in Nigeria and South Africa, where it has remained constant.
Furthermore, there is a clear difference between the life expectancy of all countries and that of African countries, which, despite having increased in recent years, is still significantly lower than that of other continents.
South Africa has the highest unemployment rate. The other countries, on the other hand, all remain constant between 5 and 15 per cent.
Infant mortality per 1,000 live births is between 0 and 25 per thousand in all countries except Nigeria and South Africa. In Nigeria, despite the rate having halved, it still stands at 100 per thousand.

The correlations paint a very consistent picture: GDP per capita, health expenditure and health indicators are strongly interconnected. In almost all countries, higher GDP per capita is associated with higher life expectancy, higher health expenditure and lower infant mortality, with often very strong relationships.
In contrast, unemployment has lower and more variable correlations, indicating that its connection to health is not linear and depends on the specific context. Overall, it is clear that economic development and health investments are associated with better health outcomes.

The linear regression shows that life expectancy increases with per capita GDP and, above all, decreases when infant mortality is high. The model explains the data well, but some effects on individual variables may be confused by the strong correlation between GDP and health expenditure.
