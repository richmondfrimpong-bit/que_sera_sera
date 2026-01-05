from sklearn.datasets import load_digits
import matplotlib.pyplot as plt


digit = load_digits()
print(digit.DESCR)
print(digit.target[::100])
print(digit.data.shape)
print(digit.target.shape)
print(digit.images[13])
print(plt.subplots(nrows=4, ncols=6, figsize=(6,4)))