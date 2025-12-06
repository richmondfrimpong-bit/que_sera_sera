# coding: utf-8
print('PyDev console: using IPython 8.6.0\n')

import sys; print('Python %s on %s' % (sys.version, sys.platform))
sys.path.extend(['C:\\Users\\pc\\PycharmProjects\\pythonProject', 'C:/Users/pc/PycharmProjects/pythonProject'])
import numpy as np
numbers = np.arange(1, 6)
numbers
numbers * 2
numbers ** 3
numbers
numbers += 10
numbers
get_ipython().run_line_magic('save', '')
get_ipython().run_line_magic('save', 'Python Console')
numbers1 = np.linspace(1.1, 5.5, 5)
numbers1
numbers * numbers1
numbers >= 13
numbers1 < numbers
numbers == numbers41
numbers == numbers1
numbers == numbers
get_ipython().run_line_magic('save', 'pydevconsole.py')
grades = np.array([[87, 96, 70], [100, 87, 90], [94, 77, 90], [100, 81, 82]])
grades
grades.sum()
grades.min()
grades.max()
grades.var()
grades.std()
grades.mean()
grades.mean(axis=0)
grades.mean(axis=1)
get_ipython().run_line_magic('save', 'pydevconsole.py')
number = np.array(arange(1,5)) ** 2
number = np.array(np.arange(1, 6)) ** 2
np.sqrt(number)
np.add(number, numbers1)
np.multiply(number, 10)
numb = np.array(np.arange(1, 7))
numb.reshape(2, 3)
np.multiply(numb, numbers)
num = np.arange(1,4)
np.multiply(numb, num)
np.array([2, 4, 6])
num = np.array([2, 4, 6])
np.multiply(numb, num)
get_ipython().run_line_magic('save', 'pydevconsole.py')
np.multiply(num, numb)
grades[0, 1]
v = np.arange(1, 7)
type(v)
grades[1]
grades[0:2]
grades
grades[1, 3]
grades[1:3]
grades[0:1]
grades[[1, 3]]
grades[[1, 3]]
grades[[1, 2, 3]]
grades[:,0]
grades[:, 0:3]
grades[:, 1:3]
grades[:, [1, 2]]
grades[:, [0, 2]]
