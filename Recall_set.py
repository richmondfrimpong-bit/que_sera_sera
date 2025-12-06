def sqrt(x):
    return x ** (1/2)

a = int(input('Enter the value of a:'))
b = int(input('Enter the value of b:'))
c = int(input('Enter the value of c:'))

root1 = (-b + sqrt(b**2 - 4*a*c))/2*a
root2 = (-b - sqrt(b**2 - 4*a*c))/2*a

print('The roots of the quadratic are:',root1,'and', root2)
