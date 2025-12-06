# coding: utf-8
print('PyDev console: using IPython 8.6.0\n')

import sys; print('Python %s on %s' % (sys.version, sys.platform))
sys.path.extend(['C:\\Users\\pc\\PycharmProjects\\pythonProject', 'C:/Users/pc/PycharmProjects/pythonProject'])
import numpy as np
x = 2
y = 3
z = 4
a = np.exp(np.cos(2 * x) + 1) + 2 * x
b = np.log(x ** 2 + 1) + 2
r = a / b
r
a = (x + (y / z))
b = y ** 2
r = (a / b) - 1
r
r = np.arctan(x * np.tan(x ** (1 / 3))) 
r
get_ipython().run_line_magic('save', '')
get_ipython().run_line_magic('saveit', '')
get_ipython().run_line_magic('', 'save prog.py')
