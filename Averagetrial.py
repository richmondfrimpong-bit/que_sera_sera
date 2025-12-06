values = []
a = 10
while a > 0:
    x = int(input('Enter Score:'))
    a -= 1
    values.append(x)

m = sum(values)/10
print('The average of the scores is:',m)