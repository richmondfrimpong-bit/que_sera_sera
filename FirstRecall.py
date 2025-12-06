import json
import csv
import pandas as pd



with open('Accounts.txt', mode='r') as recalling:
    print(f'{"Account Number":<15}{"Account Name":<15}{"Balance":>10}')
    for record in recalling:
        number, name, balance = record.split()
        print(f'{number:<15}{name:<15}{balance:>10}')



with open('myfirstcsv.csv', mode='r', newline='') as okgo:
    print(f'{"Number":<10}{"Name":<10}{"Balance":>10}')
    firsttry = csv.reader(okgo)
    for new in firsttry:
        num, accname, bal = new
        print(f'{num:<10}{accname:<10}{bal:>10}')

with open('mynewJ.json', mode='r') as keyopen:
    homie = json.dumps(json.load(keyopen), indent= 4)
    print(homie)

nextset = pd.read_csv("C:/Users/pc/PycharmProjects/We back again/myfirstcsv.csv")
print(nextset)
