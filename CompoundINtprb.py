import decimal
investment = 1000
rate = decimal.Decimal('0.05')

for time in range(1,11):
    AV = investment * ((1+rate) ** time)
    print(f'The accumulated value at the end of year {time} is {AV:.2f}')
