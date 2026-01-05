import matplotlib.pyplot as plt
from sklearn.datasets import load_digits

digit = load_digits()

figure, axes = plt.subplots(nrows=4, ncols=6, figsize=(6,4))

for item in zip(axes.ravel(), digit.images, digit.target):
    axes, image, target = item
    axes.imshow(image)
    axes.set_xticks([])
    axes.set_yticks([])
    axes.set_title(target)
plt.tight_layout()
plt.show()


