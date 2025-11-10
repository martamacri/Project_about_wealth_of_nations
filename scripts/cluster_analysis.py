"""
Cluster analysis generica.
"""
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA
from sklearn.cluster import KMeans
from sklearn.metrics import silhouette_score
sns.set(style="whitegrid")

def build_feature_table(dfs_dict, nations, method='latest', prepare_func=None):
    """
    Costruisce una tabella con feature per ogni nazione.
    """
    features = pd.DataFrame(index=nations)
    for feat_name, df in dfs_dict.items():
        df_clean = prepare_func(df) if prepare_func else df.copy()
        df_clean = df_clean.reindex(columns=nations)
        if df_clean.empty:
            features[feat_name] = [None] * len(nations)
            continue
        if method == 'latest':
            values = df_clean.loc[df_clean.index.max()]
        else:
            values = df_clean.mean(axis=0)
        features[feat_name] = values
    return features

def cluster_countries(dfs_dict,
                      nations,
                      method='latest',
                      k_min=2,
                      k_max=6,
                      random_state=42,
                      plot=True,
                      prepare_func=None):
    """
    Esegue clustering sui paesi usando feature costruite dai DataFrame.
    """
    feats = build_feature_table(dfs_dict, nations, method=method, prepare_func=prepare_func)
    feats_orig = feats.copy()
    imputer = SimpleImputer(strategy='median')
    x_imputed = imputer.fit_transform(feats)
    scaler = StandardScaler()
    x_scaled = scaler.fit_transform(x_imputed)
    best_k = None
    best_score = -1
    best_model = None
    for k in range(k_min, min(k_max, len(nations)-1) + 1):
        model = KMeans(n_clusters=k, random_state=random_state, n_init='auto')
        labels = model.fit_predict(x_scaled)
        score = silhouette_score(x_scaled, labels)
        if score > best_score:
            best_score = score
            best_k = k
            best_model = model
    if best_model is None:
        raise RuntimeError("Nessun clustering valido trovato")
    labels = best_model.labels_
    pca = PCA(n_components=2, random_state=random_state)
    x_pca = pca.fit_transform(x_scaled)
    result_table = pd.DataFrame({'country': nations, 'cluster': labels}).set_index('country')
    result_table = pd.concat([result_table, feats_orig], axis=1)
    centroids_orig = scaler.inverse_transform(best_model.cluster_centers_)
    centroids_df = pd.DataFrame(centroids_orig, columns=feats.columns)
    centroids_df.index.name = 'cluster'
    if plot:
        plt.figure(figsize=(9,6))
        sc = plt.scatter(x_pca[:,0], x_pca[:,1], c=labels, cmap='tab10', s=120, edgecolor='k')
        for i, country in enumerate(nations):
            plt.text(x_pca[i,0]+0.02, x_pca[i,1]+0.02, country, fontsize=10)
        plt.title(f'Clustering paesi (PCA 2D) - k={best_k} silhouette={best_score:.3f}')
        plt.xlabel('PCA 1')
        plt.ylabel('PCA 2')
        plt.grid(alpha=0.2)
        handles, _ = sc.legend_elements()
        plt.legend(handles, [f'cluster {i}' for i in range(best_k)], title='Cluster', loc='best')
        plt.tight_layout()
        plt.show()
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
