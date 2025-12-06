from decimal import Decimal

class CommissionEmployee:
    def __init__(self, first_name, second_name, ssn, gross_sales, comm_rate):
        self._first_name = first_name
        self._second_name = second_name
        self._ssn = ssn
        self._gross_sales = gross_sales
        self._comm_rate = comm_rate

    @property
    def first_name(self):
        return self._first_name

    @property
    def second_name(self):
        return self._second_name

    @property
    def ssn(self):
        return self._ssn

    @property
    def gross_sales(self):
        return self._gross_sales

    @property
    def comm_rate(self):
        return self._comm_rate

    @comm_rate.setter
    def comm_rate(self, rate):
        """To set the rate of commission"""
        if not (0 < rate <= 1):
            raise ValueError('Commission has to be between 0 and 1')
        self.comm_rate = rate

    @property
    def earnings(self):
        return self.gross_sales * self.comm_rate

    def __repr__(self):
        return ('Commission Employee:' + f'Name: {self.first_name} {self.second_name}\n'+
                f'SSN: {self.ssn}\n'+
                f'Gross Sales: {self.gross_sales}\n'+
                f'Commission rate: {self.comm_rate}\n'+
                f'Earnings: {self.earnings}')