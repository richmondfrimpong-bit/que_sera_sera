import math
import random
import numpy as np

x = [item for item in range(1, 6)]
Y = x.reverse()
for i in range(0, 5, 1):
    print(*x[i:9-i], end=' ')
    print()

for i in range(0, 5):
    print(x[i]*10)

for i in range(10, 0, -1):
    i *= -1
    print(i)
print('Done!')


def isprime(x):
    y = [test for test in range(2, x-1)]
    k = 0
    for i in y:
        if x % 2 == 1:
            if type(x/i) == int:
                continue
            else:
                k = x
    return k


for i in range(25, 51):
    print(isprime(i), end=' ')


