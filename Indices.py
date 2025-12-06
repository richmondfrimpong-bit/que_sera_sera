a = [[77,68,86,73], [96,87,89,81], [70,90,86,81]]

for row in a:
    for item in row:
        print(item, end=" ")
    print()

for i, row in enumerate(a):
    for j, value in enumerate(row):
        print(f'a[{i}][{j}] = {value}', end=" ")
    print()