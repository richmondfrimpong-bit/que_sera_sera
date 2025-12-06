import pandas as pd
from scipy import stats
from matplotlib import pyplot as plt
import seaborn as sns


nextset = pd.read_csv('C:/Users/pc/Downloads/airbnb_small.csv')
print(nextset.columns)


new_reg = stats.linregress(x= nextset.rating, y= nextset.price)
new_graph = sns.regplot(x= nextset.rating, y= nextset.price)
print(new_reg)
plt.show()