import random
from random import randrange

x = 5
t = 0
while x > 0:
    x = x - 1
    score = int(input('Enter student score:'))

    if score >= 70:
        grade = 'A'
        print('Student Grade:',grade)
    elif score >= 60:
        grade = 'B'
        print('Student Grade:',grade)
    elif score >= 50:
        grade = 'C'
        print('Student Grade:',grade)
    elif score >= 40:
        grade = 'D'
        print('Student Grade:',grade)
    else:
        grade = 'Fail'
        print('Student Grade:',grade)

m = list([1,2,3,4,5,6])
for k in m:
    y = k ** 2
    print('The square of', k, 'is', y)


