import numpy as np
import pandas as pd
from sklearn.cluster import AgglomerativeClustering
from sklearn.metrics import silhouette_score, davies_bouldin_score, calinski_harabasz_score

Dowjones = pd.read_csv("dow_jones_index_update_ml.csv")
Dowjones_features = Dowjones.iloc[:, 0:-1]

# Keep only numeric columns
Dowjones_features_numeric = Dowjones_features.select_dtypes(include=[np.number])

# Handle missing values
Dowjones_features_numeric = Dowjones_features_numeric.fillna(0)

# Apply AgglomerativeClustering
agg = AgglomerativeClustering(n_clusters=3)
agg.fit(Dowjones_features_numeric)
labels = agg.labels_

# Print the cluster labels
print(labels)

# Use Dowjones_features_numeric for the evaluation metrics
print("Silhouette Score:", silhouette_score(Dowjones_features_numeric, labels, metric='euclidean'))
print("DBI:", davies_bouldin_score(Dowjones_features_numeric, labels))
print("Calinski_Harabasz:", calinski_harabasz_score(Dowjones_features_numeric, labels))

#This helps in stock grouping based on financial indicators.
