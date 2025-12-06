#Exercise 1
x = [item for item in range(1, 6)]
for i in range(0, 5):
    print(*x[0:i+1], end=' ')
    print()
#Exercise 2
x = int(input('Enter a number:'))
M = 0
for i in range(0, x+1):
    M += i
print(f'The total sum is {M}')
#Exercise 3
Y = int(input('Enter the value:'))
for i in range(1,13):
    outcome = Y * i
    print(f'{Y} x {i} = {outcome}')
#Exercise 4
numbers = [12, 75, 150, 180, 145, 525, 50]
for i in range(0,7):
    if numbers[i] > 150:
        continue
    elif numbers[i] > 500:
        break
    elif numbers[i] % 5 == 0:
        print(numbers[i], end=' ')

#Exercise 5
J = '75869000'
k = 0
for letter in J:
    k += 1
print(f'The total number of digits in {J} is {k}')

#Exercise 6
x = [item for item in range(1, 6)]
for i in range(0, 5):
    print(*x[0:i+1], end=' ')
    print()
