from sklearn.datasets import load_iris
from sklearn.manifold import TSNE
import matplotlib.pyplot as plt
from sklearn.decomposition import PCA
import pandas as pd
import seaborn as sns
from sklearn.cluster import KMeans
from sklearn.cluster import AgglomerativeClustering
from sklearn.cluster import SpectralClustering
from sklearn.cluster import DBSCAN
from sklearn.cluster import MeanShift
import numpy as np

pd.set_option('display.max_columns', 5)
pd.set_option('display.width', None)
pd.set_option('display.precision', 2)

iris = load_iris()
print(iris.DESCR)
print(iris.data.shape)
print(iris.target.shape)
iris_datF = pd.DataFrame(iris.data, columns=iris.feature_names)
print(iris_datF.describe())
iris_datF['species'] = [iris.target_names[i] for i in iris.target]
print(iris_datF)

tsne = TSNE(n_components=2, random_state=13)
reduct = tsne.fit_transform(iris.data)
plt.scatter(reduct[:,0], reduct[:,1], c=iris.target, cmap='nipy_spectral_r')
plt.show()

pca = PCA(n_components=2, random_state= 147)
reduced = pca.fit_transform(iris.data)
plt.scatter(reduced[:,0], reduced[:,1], c=iris.target, cmap='nipy_spectral_r')
plt.show()

sns.pairplot(iris_datF, hue='species', vars=iris_datF.columns[0:4])
plt.show()

est = {'KMeans' :KMeans(n_clusters=3, random_state=123),
       'SpectralClustering': SpectralClustering(n_clusters=3, random_state=123),
       'AgglomerativeClustering': AgglomerativeClustering(n_clusters=3),
       'DBSCAN': DBSCAN(),'MeanShift':MeanShift()}
for est_name, estimator in est.items():
    lab = estimator.fit(iris.data)
    print(f'\n{est_name}:')
    for i in range(0, 101, 50):
        print(f'{i} - {i + 50}')
        labels, counts = np.unique(estimator.labels_[i:i+50], return_counts=True)
        for x, y in zip(labels, counts):
            print(f'label = {x}, count = {y}')







