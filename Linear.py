import pandas as pd
from scipy import stats
import seaborn as sns
from matplotlib import pyplot as plt


newset = pd.read_csv('C:/Users/pc/Downloads/data.csv')

newset.columns = ['Date', 'Value']
newset.Date = newset.Date.floordiv(100)

linear_regress = stats.linregress(x= newset.Date, y= newset.Value)
print(linear_regress)

prediction = linear_regress.slope * 2026 + linear_regress.intercept
print(f'The prediction for 2026 is {prediction}')

print(newset.head())


axes = sns.regplot(x=newset.Date, y=newset.Value)
plt.show()