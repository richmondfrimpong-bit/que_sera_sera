from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
import pandas as pd
from sklearn.metrics import r2_score, mean_squared_error
import numpy as np


class PVLinearRegression:
    def __init__(self, dataset):
        self._dataset = dataset
        X_train, X_test, y_train, y_test = train_test_split(dataset.data, dataset.target,random_state=78)

        model = LinearRegression()
        model.fit(X_train, y_train)
        predicted = model.predict(X=X_test)
        expected = y_test
        datFR = pd.DataFrame(dataset.data, columns=dataset.feature_names)
        ray = []
        for item in datFR.columns:
            if item not in dataset.target_names:
                ray.append(round(float(datFR.get(item).std()),6))
        conf_low = []
        conf_upper = []
        for combo in zip(model.coef_, ray):
            esti, stad_dev = combo
            conf_low.append(round(float(esti - 1.96 * (stad_dev / np.sqrt(len(dataset.target)))), 6))
            conf_upper.append(round(float(esti + 1.96 * (stad_dev / np.sqrt(len(dataset.target)))), 6))
        dict = {'Variable':[x for x in dataset.feature_names],
                'Estimate': [y for y in model.coef_],
                'Std': [st for st in ray],
                'Conf_lower(0.05)': [conf for conf in conf_low],
                'Conf_upper(0.05)': [confu for confu in conf_upper]
                }
        print(f'==========================================\n'
         f'|| Shape of train data: {X_train.shape}      ||\n' +
         f'==========================================\n' +
         f'|| Shape of test data: {X_test.shape}        ||\n' +
         f'==========================================\n' +
         f'|| R-Squared: {r2_score(y_true=expected, y_pred=predicted)}        ||\n' +
         f'==========================================\n'
         f'|| MSE: {mean_squared_error(y_true=expected, y_pred=predicted)}              ||\n' +
         f'==========================================\n' +
         f'|| RMSE: {np.sqrt(mean_squared_error(y_true=expected, y_pred=predicted))}              ||\n' +
         f'==========================================')

        par_datF = pd.DataFrame(dict, columns=['Variable', 'Estimate', 'Std', 'Conf_lower(0.05)', 'Conf_upper(0.05)'])
        print(par_datF)
        print(f'Intercept  {model.intercept_}')

class PVLinearRegDatF:
    def __init__(self, dataframe, dependent):
        independent = pd.DataFrame(dataframe)
        independent = independent.drop(dependent, axis=1)

        X_train, X_test, y_train, y_test = train_test_split(independent, dataframe.get(dependent).values, random_state=78)

        model = LinearRegression()
        model.fit(X_train, y_train)
        predicted = model.predict(X=X_test)
        expected = y_test
        ray = []
        for item in dataframe.columns:
            if item in independent.columns:
                ray.append(round(float(dataframe.get(item).std()),6))
        conf_low = []
        conf_upper = []
        for combo in zip(model.coef_, ray):
            esti, stad_dev = combo
            conf_low.append(round(float(esti - 1.96 * (stad_dev / np.sqrt(len(dataframe.get(dependent))))), 6))
            conf_upper.append(round(float(esti + 1.96 * (stad_dev / np.sqrt(len(dataframe.get(dependent))))), 6))
        diction_ary = {'Variable': [x for x in independent.columns],
                    'Estimate': [y for y in model.coef_],
                       'std': [st for st in ray],
                       'Conf_lower(0.05)': [conf for conf in conf_low],
                       'Conf_upper(0.05)': [confu for confu in conf_upper]}

        print(f'==========================================\n'
              f'|| Shape of train data: {X_train.shape}         ||\n' +
              f'==========================================\n' +
              f'|| Shape of test data: {X_test.shape}          ||\n' +
              f'==========================================\n' +
              f'|| R-Squared: {r2_score(y_true=expected, y_pred=predicted)}     ||\n' +
              f'==========================================\n'
              f'|| MSE: {mean_squared_error(y_true=expected, y_pred=predicted)}               ||\n' +
              f'==========================================\n' +
              f'|| RMSE: {np.sqrt(mean_squared_error(y_true=expected, y_pred=predicted))}               ||\n' +
              f'==========================================')

        par_datF = pd.DataFrame(diction_ary, columns=['Variable', 'Estimate','std',
                                                      'Conf_lower(0.05)', 'Conf_upper(0.05)'])
        print(par_datF)
        print(f'Intercept  {model.intercept_}')






