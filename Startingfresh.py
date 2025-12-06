import json

with open('new_accounts.txt', mode='w') as new_accounts:
    new_accounts.write('100 James 25000\n')
    new_accounts.write('200 Martin 45000\n')
    new_accounts.write('300 Gordon 65000\n')
    new_accounts.write('400 kelvin 78200\n')
    new_accounts.write('500 Hoguth 45500\n')
    new_accounts.write('600 knight 48963')

with open('new_accounts.txt', mode='r') as new_accounts:
    print(f'{"Account Number":<15}{"Account Name":^15}{"Balance":>10}')
    for record in new_accounts:
        acc_no, name, acc_bal = record.split()
        print(f'{acc_no:^15}{name:^15}{acc_bal:>10}')



mynewdict = {'branch_Accounts':[{'account_no':100, 'name':'James', 'Balance':25000},
                                {'account_no':200, 'name':'Martin', 'Balance':45000},
                                {'account_no':300, 'name':'Gordon', 'Balance':65000},
                                {'account_no':400, 'name':'Kelvin', 'Balance':78200},
                                {'account_no':500, 'name':'Hoguth', 'Balance':45500},
                                {'account_no':600, 'name':'Knight', 'Balance':48963}]}


with open('mynewJ.json',mode='w') as newset:
    json.dump(mynewdict,newset)



with open('mynewJ.json',mode='r') as newset:
    letsdisplay = json.dumps(json.load(newset), indent=4)
    print(letsdisplay)




