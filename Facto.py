def factorial(x):
    for k in range(x,1,-1):
        x *= (k-1)
    return x

print(f'The factorial of m is {factorial(6)}')

