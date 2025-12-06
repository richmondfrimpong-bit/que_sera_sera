from decimal import Decimal


class Account:
    """Meant to display account balance and account Name"""
    def __init__(self,name,balance):
        if balance < Decimal('0.00'):
            raise ValueError('Account balance has to be positive')

        self.name = name
        self.balance = balance

    def deposit(self, amount):
        if amount < Decimal('0.00'):
            raise ValueError('Deposit cannot be less than zero')

        self.balance += amount
