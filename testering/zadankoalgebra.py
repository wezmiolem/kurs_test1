import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.datasets import load_iris
from sklearn.metrics.pairwise import euclidean_distances

iris = load_iris()
data = iris.data


np.random.seed(42)
indices = np.random.choice(data.shape[0], size=10, replace=False)
sample_data = data[indices]

print(sample_data)

dist_matrix = euclidean_distances(sample_data, sample_data)

plt.figure(figsize=(10, 8))
sns.heatmap(dist_matrix, 
            annot=True, 
            fmt=".2f", 
            cmap="YlGnBu", 
            xticklabels=indices, 
            yticklabels=indices)

plt.title("Heatmap of Euclidean Distances (10 Random Iris Samples)")
plt.xlabel("Observation Index")
plt.ylabel("Observation Index")
plt.show()