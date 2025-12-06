from decimal import Decimal
from commissionemployee import CommissionEmployee
from salariedcommissionemployee import SalariedCommissionEmployee


newcommission = CommissionEmployee('James', 'Brown','555-222-333', Decimal('2000'), Decimal('0.05'))
salaryguy = SalariedCommissionEmployee('Martin', 'Luther', '333-444-555',Decimal('5000'), Decimal('0.07'), Decimal('4000'))

s = [newcommission, salaryguy]
for employee in s:
    print(f'{employee}\n')
