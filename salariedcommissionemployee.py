from decimal import Decimal
from commissionemployee import CommissionEmployee

class SalariedCommissionEmployee(CommissionEmployee):
    def __init__(self, firstname, secondname, ssn, grossSales, commrate, basepay):
        super().__init__(firstname, secondname, ssn, grossSales, commrate)
        self._basepay = basepay

    @property
    def basepay(self):
        return self._basepay

    @property
    def earnings(self):
        return super().earnings + self.basepay

    @basepay.setter
    def basepay(self, pay):
        """To set base pay"""
        if pay < Decimal('0.00'):
            raise ValueError('Base pay cannot be less than zero')
        self.basepay = pay

    def __repr__(self):
        return ('Salaried Commission Employee:\n' + super().__repr__() +
                f'\nBase Salary: {self.basepay}')

