a = int(input('Enter the first number:'))
b = int(input('Enter the second number:'))

if a == b:
    print("The numbers are equal")
elif a > b:
    print("The first number is greater than the second")
elif a < b:
    print("The second number is the greatest")
elif a >= b:
    print("The first number is either greater or equal to the second")
elif a <= b:
    print("The second number is either greater or equal to the first")
else:
    print("The numbers a definitely not equal")

