"""
cluster analysis
"""
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA
from sklearn.cluster import KMeans
from sklearn.metrics import silhouette_score
from formatting import prepare_df
sns.set(style="whitegrid")

df1 = pd.read_csv('data/gdp_per_capita_1995_2024.csv')
df2 = pd.read_csv('data/gdp_1995_2024.csv')
df3 = pd.read_csv('data/life_expectacy_1995_2023.csv')
df4 = pd.read_csv('data/health_expenditure_2000_2022.csv')
df5 = pd.read_csv('data/infant_mortality_1995_2023.csv')
df6 = pd.read_csv('data/unemployment_1995_2024.csv')
df7 = pd.read_csv('data/population_growth_1995_2024.csv')

#Cluster analisis
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

def build_feature_table(dfs_dict, nations, method='latest'): #tabella finale
    """
    tabella cluster
    """
    features = pd.DataFrame(index=nations)
    for feat_name, df in dfs_dict.items():
        df_clean = prepare_df(df)
        df_clean = df_clean.reindex(columns=nations)
        if df_clean.empty:
            features[feat_name] = [None] * len(nations)
            continue
        if method == 'latest':
            latest_year = df_clean.index.max()
            values = df_clean.loc[latest_year]
        else:
            values = df_clean.mean(axis=0)
        features[feat_name] = values
    return features

def cluster_countries(
        dfs_dict,
        nations,
        method='latest',
        k_min=2,
        k_max=6,
        random_state=42,
        plot=True
        ):
    """
    cluster
    """
    # 1) build features
    feats = build_feature_table(dfs_dict, nations, method=method)
    # 2) mantieni copia originale (non scaled) per output numerico
    feats_orig = feats.copy()
    # 3) imputazione
    imputer = SimpleImputer(strategy='median')
    x_imputed = imputer.fit_transform(feats)
    # 4) scaling
    scaler = StandardScaler()
    x_scaled = scaler.fit_transform(x_imputed)
    # 5) scegliere k con silhouette
    best_k = None
    best_score = -1
    best_model = None
    for k in range(k_min, min(k_max, len(countries)-1) + 1):
        try:
            model = KMeans(
                n_clusters=k,
                random_state=random_state,
                n_init='auto'
            )
            labels = model.fit_predict(x_scaled)
            score = silhouette_score(x_scaled, labels)
        except ImportError:
            score = -1
        if score > best_score:
            best_score = score
            best_k = k
            best_model = model
    # === FIX: garantisce che best_model sia assegnato ===
    if best_model is None:
        raise RuntimeError(
            "Nessun clustering valido è stato trovato. "
            "Verificare che il dataset abbia abbastanza varianza e almeno 2 campioni."
        )
    labels = best_model.labels_
    # 6) PCA per visualizzazione 2D
    pca = PCA(n_components=2, random_state=random_state)
    x_pca = pca.fit_transform(x_scaled)
    # 7) prepara output numerico
    result_table = pd.DataFrame({
        'country': nations,
        'cluster': labels
    }).set_index('country')
    # aggiungi le features originali
    result_table = pd.concat([result_table, feats_orig], axis=1)
    # centroidi in spazio originale (inversa scaling + imputazione è approssimativa)
    centroids_scaled = best_model.cluster_centers_
    centroids_orig = scaler.inverse_transform(centroids_scaled)
    # creiamo DataFrame centroidi con colonne features
    centroids_df = pd.DataFrame(centroids_orig, columns=feats.columns)
    centroids_df.index.name = 'cluster'
    # 8) stampa sommario
    print("=== Cluster summary ===")
    print(f"Metodo feature: {method}")
    print(f"Numero paesi considerati: {len(nations)}")
    print(f"Cluster scelto (silhouette): k = {best_k}, silhouette = {best_score:.4f}")
    print("\nDimensione per cluster:")
    print(result_table['cluster'].value_counts().sort_index())
    print("\nCluster assignments (prima righe):")
    print(result_table.sort_values('cluster').head(20))
    print("\nCentroidi (valori approssimati nello spazio delle feature originali):")
    print(centroids_df)
    # 9) plot
    if plot:
        plt.figure(figsize=(9,6))
        sc = plt.scatter(x_pca[:,0], x_pca[:,1], c=labels, cmap='tab10', s=120, edgecolor='k')
        for i, country in enumerate(nations):
            plt.text(x_pca[i,0]+0.02, x_pca[i,1]+0.02, country, fontsize=10)
        plt.title(f'Clustering paesi (PCA 2D) - k={best_k} silhouette={best_score:.3f}')
        plt.xlabel('PCA 1')
        plt.ylabel('PCA 2')
        plt.grid(alpha=0.2)
        # legenda: numero cluster
        handles, _ = sc.legend_elements()
        plt.legend(handles, [f'cluster {i}' for i in range(best_k)], title='Cluster', loc='best')
        plt.tight_layout()
        plt.show()
    # ritorna oggetti utili
    return {
        'features_original': feats_orig,
        'features_imputed_scaled': x_scaled,
        'pca_2d': x_pca,
        'kmeans': best_model,
        'labels': labels,
        'result_table': result_table,
        'centroids': centroids_df,
        'silhouette': best_score,
        'method': method
    }

out = cluster_countries(
    dfs_dict=dfs,
    nations=countries,
    method='latest',  # oppure 'mean'
    k_min=2,
    k_max=6,
    plot=True
)
print("\nRisultati per paese:")
print(out['result_table'])
