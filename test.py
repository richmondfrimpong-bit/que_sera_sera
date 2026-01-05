from sklearn.datasets import fetch_california_housing
import pandas as pd
from pretty_view import PVLinearRegression

x = PVLinearRegression(fetch_california_housing())
print(x)
#y = fetch_california_housing()
#dat = pd.DataFrame(y,columns=[])
#print(fetch_california_housing().items())