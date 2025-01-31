import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.cluster import DBSCAN
from sklearn.metrics import calinski_harabasz_score, davies_bouldin_score, silhouette_score

X = pd.read_csv("dow_jones_index_ml.csv")
X.head()

X = X.select_dtypes(include=[np.number])  # Keep only numeric columns
# Replace invalid values with a default
X = X.apply(pd.to_numeric, errors='coerce')  # Convert all columns to numeric
X = X.fillna(0)  # Replace NaN with 0

# Drop rows with NaN values
X = X.dropna()

#DSCAN Clustering
dbscan = DBSCAN(eps=0.4, min_samples=10)
dbscan.fit(X)
labels = dbscan.labels_
print(labels)

# Adjust eps and min_samples
dbscan = DBSCAN(eps=0.2, min_samples=5)  
dbscan.fit(X)
labels = dbscan.labels_
unique_labels = np.unique(labels)
print("Unique labels:", unique_labels)

# Evaluating Clustering Performance
if len(np.unique(labels)) > 1:  
    print("Silhouette Score:", silhouette_score(X, labels, metric='euclidean'))
    print("DBI:", davies_bouldin_score(X, labels))
    print("Calinski_Harabasz:", calinski_harabasz_score(X, labels))
else:
    print("DBSCAN did not find more than one cluster.")

#Visualizing the Clusters
plt.scatter(X.iloc[:, 0], X.iloc[:, 1], c=labels)
plt.title("DBSCAN Clustering")
plt.show()

# This helps in stock market pattern Identification
