import matplotlib.pyplot as plt
from sklearn.datasets import fetch_california_housing
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
import seaborn as sns
from sklearn.metrics import r2_score
from sklearn.metrics import mean_squared_error
from sklearn.model_selection import KFold
from sklearn.model_selection import cross_val_score
from sklearn.linear_model import Lasso
from sklearn.linear_model import Ridge
from sklearn.linear_model import ElasticNet
from sklearn.manifold import TSNE


califor_set = fetch_california_housing()
print(califor_set.DESCR)
print(califor_set.feature_names)
pd.set_option('display.precision', 4)
pd.set_option('display.max_columns', 9)
pd.set_option('display.width', None)

califor_datF = pd.DataFrame(califor_set.data, columns=califor_set.feature_names)
califor_datF['MedVal'] = pd.Series(califor_set.target)
print(califor_datF.head(5))
print(califor_datF.tail(5))
tsne = TSNE(n_components=2, random_state= 13)
new_red = tsne.fit_transform(califor_set.data)
plt.scatter(new_red[:,0], new_red[:,1], c=califor_set.target, cmap='nipy_spectral_r')
plt.show()


X_train, X_test, y_train, y_test = train_test_split(califor_set.data, califor_set.target, random_state= 120)
multi_reg = LinearRegression()
multi_reg.fit(X=X_train, y=y_train)
for i, est in enumerate(califor_set.feature_names):
    print(f'{est} : {multi_reg.coef_[i]}')
print(f'Intercept: {multi_reg.intercept_}')
pred = multi_reg.predict(X=X_test)
exp = y_test
print(f'R-squared: {r2_score(exp, pred)}')
print(f'Mean Squared Error: {mean_squared_error(exp, pred)}')

predicted = pd.Series(multi_reg.predict(X=X_test))
expected = pd.Series(y_test)
dat = pd.DataFrame()
dat['Predicted'] = predicted
dat['Expected'] = expected
sns.scatterplot(data=dat, x='Expected', y='Predicted', hue='Expected', palette='cool', legend=False)
start = min(expected.min(), predicted.min())
end = max(expected.max(), predicted.max())
plt.xlim(0,7)
plt.ylim(0,7)
plt.plot([start, end], [start, end], 'k--')
plt.show()

lasso = Lasso()
ridge = Ridge()
elastic = ElasticNet()
estas = [lasso, ridge, elastic, multi_reg]
for esti in estas:
    kfold = KFold(n_splits=10, shuffle=True, random_state=12)
    score = cross_val_score(estimator=esti, X=X_train, y=y_train, cv=kfold, scoring='r2')
    print(f'{esti} : Mean of r2 is {score.mean()}')





