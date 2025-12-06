import csv
import json
import pandas as pd



with open('myfirstcsv.csv', mode='w', newline='') as newcsv:
    myenter = csv.writer(newcsv)
    myenter.writerow([500,'James',4500])
    myenter.writerow([200, 'David', 5500])
    myenter.writerow([300, 'Hudson', 6500])
    myenter.writerow([900, 'Herty', 6300])


with open('myfirstcsv.csv', mode='r', newline='') as newset:
    print(f'{"Account":<10}{"Name":<10}{"Balance":>10}')
    mynewset = csv.reader(newset)
    for record in mynewset:
        acc, name, balance = record
        print(f'{acc:<10}{name:<10}{balance:>10}')


with open('Accounts.txt', mode='r') as thisguy:
    print(f'{"Account":<10}{"Name":<10}{"Balance":>10}')
    for record1 in thisguy:
        account, Name, Bal = record1.split()
        print(f'{account:<10}{Name:<10}{Bal:>10}')



with open('mynewJ.json', mode='r') as letstry:
    letsgo = json.dumps(json.load(letstry), indent=4)
    print(letsgo)



firstimport = pd.read_csv('https://vincentarelbundock.github.io/Rdatasets/csv/tidyr/household.csv')
print(firstimport)

men = (firstimport.name_child1 == 'Mark').describe()
print(men)

