# coding: utf-8
print('PyDev console: using IPython 8.6.0\n')

import sys; print('Python %s on %s' % (sys.version, sys.platform))
sys.path.extend(['C:\\Users\\pc\\PycharmProjects\\pythonProject', 'C:/Users/pc/PycharmProjects/pythonProject'])
get_ipython().run_line_magic('load', 'pydevconsole.py')
import numpy as np
grades = np.array([[86, 96, 70], [100, 87, 90]])
grades
grades.reshape(3,2)
grades
grades.resize(1, 6)
grades
grades.resize(2,3)
grades
flattened = grades.flatten()
flattened
grades
id(grades)
id(flattened)
grades[1, 2] *= 2
grades
flattened
raveled = grades.ravel()
raveled
id(grades)
id(raveled)
grades[1, 2] /= 2
grades
raveled
grades.T
grades1 = np.array([[94, 77, 90], [100, 81, 82]])
grades1
np.hstack((grades, grades1))
np.vstack((grades, grades1))
get_ipython().run_line_magic('save', 'pydevconsole.py')
get_ipython().run_line_magic('save', 'newguy.py')
index(grades1[0])
enumerate(grades1)
for i, row in enumerate(grades1):
    for j in row:
        print(i, j)
        
for i , row in enumerate(grades1):
    for j, column in enumerate(row):
        print(f'grades1{i}{j} = {column}', end=' ')
        print()
        
for i , row in enumerate(grades1):
    for j, column in enumerate(row):
        print(f'grades1{[i]}{[j]} = {column}', end=' ')
        print()
        
for i , row in enumerate(grades1):
    for j, column in enumerate(row):
        print(f'grades1{[i]}{[j]} = {column}', end=' ')
    print()
    
import pandas as pd
grades2 = pd.Series([87, 100, 94])
grades2
pd.Series(98.7, range(3))
grades2[0]
grades2.describe()
grades2.count()
grades2.mean()
grades2.min()
grade2.max()
grades2.max()
grades2.std()
grades2.median()
grades2.quantile(1)
scores = pd.Series([87, 100, 94], index=['kofi', 'yaw', 'kwaku'])
scores
scores1 = pd.Series({'kofi': 87, 'yaw': 100, 'kwaku': 94})
scores1
scores['kofi']
scores.yaw
scores.values()
scores.values
scores.keys()
hardware = pd.Series(['hammer', 'saw', 'wrench'])
hardware
hardware.str.contains('a')
hardware.str.upper()
hardware.str.count()
