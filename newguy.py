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
