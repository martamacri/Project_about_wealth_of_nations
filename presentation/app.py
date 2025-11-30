"""
Web application for my project about the nations
"""
import sys
import os
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
print("Project root:", project_root)  # debug

if project_root not in sys.path:
    sys.path.insert(0, project_root)

try:
    from scripts.formatting import prepare_df
    from scripts.timelines import plot_indicator, mean_pre_post
    from scripts.correlations import compute_country_correlations, compute_rolling_correlation
    from scripts.regression import regression_life_expectancy
    from scripts.wellness_indicator import compute_wellbeing_index
    from scripts.cluster_analysis import cluster_countries
    from scripts.visualizations import plot_by_continent, melt_indicator, animate_indicator
    print("Imports OK")
except ModuleNotFoundError as e:
    print("Errore import:", e)
    st.error(f"Errore import: {e}")
    st.stop()

sns.set(style="whitegrid")
st.set_page_config(page_title="Wealth of Nations Dashboard", layout="wide")
st.title("Wealth of Nations Dashboard")

@st.cache_data
def load_data():
    """
    read data
    """
    df1 = pd.read_csv(os.path.join(project_root, 'data/gdp_per_capita_1995_2024.csv'))
    df2 = pd.read_csv(os.path.join(project_root, 'data/gdp_1995_2024.csv'))
    df3 = pd.read_csv(os.path.join(project_root, 'data/life_expectacy_1995_2023.csv'))
    df4 = pd.read_csv(os.path.join(project_root, 'data/health_expenditure_2000_2022.csv'))
    df5 = pd.read_csv(os.path.join(project_root, 'data/infant_mortality_1995_2023.csv'))
    df6 = pd.read_csv(os.path.join(project_root, 'data/unemployment_1995_2024.csv'))
    df7 = pd.read_csv(os.path.join(project_root, 'data/population_growth_1995_2024.csv'))
    return df1, df2, df3, df4, df5, df6, df7

df1, df2, df3, df4, df5, df6, df7 = load_data()

gdp_pc = prepare_df(df1)
gdp = prepare_df(df2)
life = prepare_df(df3)
health = prepare_df(df4)
infant_mort = prepare_df(df5)
unemp = prepare_df(df6)
pop = prepare_df(df7)

# Sidebar
st.sidebar.title("Sezioni")
section = st.sidebar.radio("Vai a:", [
    "Evolution",
    "Correlations",
    "Rolling Correlation",
    "Linear Regression",
    "Well-being Index",
    "Cluster Analysis"
])

if section == "Evolution":
    st.header("Evolution of Indicators")

    # Selezione indicatore
    indicator = st.selectbox("Seleziona indicatore",
                             ["GDP per capita",
                              "Life expectancy",
                              "Unemployment",
                              "Infant mortality"])

    # Scegli se plot per paesi o continenti
    view_type = st.radio("Visualizza per:", ["Paesi", "Continenti"])

    # Bottone per il plot
    if st.button("Plot Evolution"):
        plt.figure(figsize=(12,6))

        # Seleziona i dati in base all'indicatore
        if indicator == "GDP per capita":
            df = gdp_pc
        elif indicator == "Life expectancy":
            df = life
        elif indicator == "Unemployment":
            df = unemp
        elif indicator == "Infant mortality":
            df = infant_mort

        # Plot per paesi o continenti
        if view_type == "Paesi":
            st.subheader(f"{indicator} for all countries")
            plot_indicator(df, f"Evolution of {indicator} over time by country")
        else:  # Continenti
            st.subheader(f"{indicator} for all continents")
            plot_by_continent(df, f"Evolution of {indicator} over time by continent")

        st.pyplot(plt.gcf())

# Correlations
elif section == "Correlations":
    st.header("Country Correlations")
    comparisons = [
        ("GDP per capita", gdp_pc, "Life expectancy", life),
        ("Unemployment", unemp, "Life expectancy", life),
        ("GDP per capita", gdp_pc, "Health expenditure", health),
        ("GDP per capita", gdp_pc, "Infant mortality", infant_mort),
        ("Health expenditure", health, "Infant mortality", infant_mort)
    ]
    corr_df_list = [compute_country_correlations(df_x, df_y, name_x, name_y)
                    for name_x, df_x, name_y, df_y in comparisons]
    corr_df = pd.concat(corr_df_list, ignore_index=True)
    st.dataframe(corr_df)

# ----------------------------
# Rolling Correlation
# ----------------------------
elif section == "Rolling Correlation":
    st.header("Rolling correlation between GDP per capita and Life expectancy")
    window = st.slider("Window size (years)", min_value=5, max_value=30, value=15)
    rolling_corr = compute_rolling_correlation(gdp_pc, life, window=window)
    plt.figure(figsize=(14,8))
    for country in rolling_corr.columns:
        plt.plot(rolling_corr.index, rolling_corr[country], label=country)
    plt.title(f"Rolling correlation ({window} years)")
    plt.xlabel("Year")
    plt.ylabel("Pearson's correlation")
    plt.legend()
    plt.grid(True)
    st.pyplot(plt.gcf())

# ----------------------------
# Linear Regression
# ----------------------------
elif section == "Linear Regression":
    st.header("Linear regression of Life Expectancy")
    model_df, data_df = regression_life_expectancy(gdp_pc, life, health, infant_mort)
    st.text(model_df.summary())

# ----------------------------
# Well-being Index
# ----------------------------
elif section == "Well-being Index":
    st.header("Well-being Index")
    wellbeing_index, countries = compute_wellbeing_index(life, health, infant_mort)
    st.subheader("Average evolution over time")
    plt.figure(figsize=(12,6))
    wellbeing_index.mean(axis=1).plot()
    plt.title("Summary index of average well-being over time")
    plt.xlabel("Year")
    plt.ylabel("Well-being index")
    plt.grid(True)
    st.pyplot(plt.gcf())

    st.subheader("Ranking of countries by average index")
    mean_wellbeing = wellbeing_index.mean(axis=0)
    rank = mean_wellbeing.sort_values(ascending=False)
    st.dataframe(rank)

# ----------------------------
# Cluster Analysis
# ----------------------------
elif section == "Cluster Analysis":
    st.header("Cluster analysis of selected countries")
    dfs = {
        'GDP_per_capita': df1,
        'GDP': df2,
        'Life_expectancy': df3,
        'Health_expenditure': df4,
        'Infant_mortality': df5,
        'Unemployment': df6,
        'Population_growth': df7
    }
    countries = ['ITA', 'ESP', 'DEU', 'SWE', 'USA', 'CAN', 'BRA', 'CHL', 'ZAF', 'NGA']
    results = cluster_countries(
        dfs_dict=dfs,
        nations=countries,
        method='latest',
        k_min=2,
        k_max=6,
        plot=True,
        prepare_func=prepare_df
    )
    st.subheader("Cluster results per country")
    st.dataframe(results['result_table'])
