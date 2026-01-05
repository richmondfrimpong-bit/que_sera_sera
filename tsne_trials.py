import matplotlib.pyplot as plt
from sklearn.datasets import load_digits
import seaborn as sns
from sklearn.manifold import TSNE

digit = load_digits()
tsne = TSNE(n_components=2, random_state= 12)
reduc_set = tsne.fit_transform(digit.data)
dots = plt.scatter(reduc_set[:,0], reduc_set[:,1], c=digit.target, cmap='nipy_spectral_r')
colorbar = plt.colorbar(dots)
plt.show()