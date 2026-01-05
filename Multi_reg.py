from sklearn.datasets import fetch_california_housing
import pandas as pd
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt
import numpy as np
from pretty_view import PVLinearRegression


california_set = fetch_california_housing()
print(california_set.DESCR)
print(california_set.feature_names)

pd.set_option('display.precision', 2)
pd.set_option('display.max_columns', 9)
pd.set_option('display.width', None)

california_datF = pd.DataFrame(california_set.data, columns=california_set.feature_names)
california_datF['MedHouseValue'] = pd.Series(california_set.target)

print(california_datF.head(5))

sample_datF = california_datF.sample(frac=0.1, random_state=11)
sns.pairplot(sample_datF, hue='MedHouseValue',vars=sample_datF.columns[[6,7,8]])
for feature in california_set.feature_names:
    sns.scatterplot(data=sample_datF, x=feature, y='MedHouseValue', hue='MedHouseValue', palette='cool')
plt.show()

X_train, X_test, y_train, y_test = train_test_split(california_set.data, california_set.target, random_state=15)
mult_regress = LinearRegression()
mult_regress.fit(X=X_train, y= y_train)

for i, name in enumerate(california_set.feature_names):
    print(f'{name} : {mult_regress.coef_[i]}')
print(f'Intercept: {mult_regress.intercept_}')

predicted = pd.Series(mult_regress.predict(X_test))
expected = pd.Series(y_test)
dat  = pd.DataFrame()
dat['Predicted'] = predicted
dat['Expected'] = expected
sns.scatterplot(data=dat, x='Expected', y='Predicted', hue='Expected', palette='cool')
start = min(expected.min(), predicted.min())
end = max(expected.max(), predicted.max())
plt.xlim(start,end)
plt.ylim(start,end)
plt.plot([start,end], [start,end], 'k--')
plt.show()






