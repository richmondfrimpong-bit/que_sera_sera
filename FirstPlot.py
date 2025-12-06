import matplotlib.pyplot as plt
import seaborn as sns
import random
import numpy as np

rows = [random.randrange(1,7) for i in range(601)]
title = f'Rolling a die {len(rows)} times'
outcome , frequency = np.unique(rows, return_counts=True)
sns.set_style("whitegrid")
axes = sns.barplot(x= outcome, y= frequency, palette='bright')
axes.set_title(title)
axes.set(xlabel='OUTCOME',ylabel='Frequency')
plt.show()
