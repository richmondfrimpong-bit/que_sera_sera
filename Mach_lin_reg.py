import pandas as pd
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split


my_set = pd.read_csv('C:/Users/pc/Downloads/data.csv')
my_set.columns = ['Date', 'Value']
my_set.Date = my_set.Date.floordiv(100)
print(my_set.head(5))

X_train, X_test, y_train, y_test = train_test_split(my_set.Date.values.reshape(-1,1), my_set.Value.values, random_state=11)
lin_reg = LinearRegression()
lin_reg.fit(X_train, y_train)
print(lin_reg.coef_)
print(lin_reg.intercept_)

x = [min(my_set.Date.values.reshape(-1,1)), max(my_set.Date.values.reshape(-1,1))]
y = lin_reg.predict(x)

predicted = lin_reg.predict(X=X_test)
expected = y_test
for predic, expect in zip(predicted, expected):
    print(f'Prediction = {predic:.2f}  ->  Expected = {expect}')

sns.scatterplot(my_set, x=my_set.Date, y=my_set.Value, hue='Value', palette='winter', legend=False)
plt.ylim(10,70)
plt.plot(x, y)
plt.show()


