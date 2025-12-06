import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import random

rolls = [random.randrange(1, 7) for i in range(600)]
outcome, frequency = np.unique(rolls, return_counts=True)
title = f'Rolling a six sided die {len(rolls)} times'
axes = plt.bar(x=outcome, height=frequency, color=('red','green','blue','magenta','yellow','grey'))
percen = frequency/len(rolls)
plt.xlabel('Outcome')
plt.ylabel('Frequency')
plt.bar_label(axes, labels=frequency, label_type='edge', padding=3)
plt.ylim([0, 150])
plt.title(title)
plt.show()
