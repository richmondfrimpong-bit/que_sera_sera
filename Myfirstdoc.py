with open('Accounts.txt', mode='r') as Accounts:
    print(f'{"Account":<10}{"Name":<10}{"Balance":>10}')
    for record in Accounts:
        number, name, balance = record.split()
        print(f'{number:<10}{name:<10}{balance:>10}')