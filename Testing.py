from FirstClass import Account
from decimal import Decimal
from SecondClass import Degree
from ThirdClass import Time


new = Account("James", Decimal('1000'))
print(new.name)
print(new.balance)
new.deposit(Decimal('500'))
print(new.balance)

Thisguy = Degree("Solomon Mensah",69.22,"Second Class Upper")
print(Thisguy.name)
print(Thisguy.degree)
print(Thisguy.CWA)
Thisguy.rename('Mensah Solomon Ohyiram')
print(Thisguy.name)

ttesting = Time(hour=6, minute=30)
print(ttesting)