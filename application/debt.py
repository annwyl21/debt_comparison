class Debt:
    def __init__(self, amount, interest, repayment):
        self._amount = amount
        self._interest = interest
        self._repayment = repayment

        if self._amount:
            self._amount = int(self._amount)
        else:
            self._amount = 0

        if self._interest:
            self._interest = int(self._interest)
        else:
            self._interest = 5
        
        if self._repayment:
            self._repayment = int(self._repayment)
        else:
            self._repayment = 10
            # entering a repayment of zero will break our debt calculators 
            # (there is a while loop that continues until a loan amount is paid - reaches a zero value, if repayment = 0 it creates an infinite loop) 
            # so we have a default repayment of 10
        
    def get_amount(self):
        return self._amount
      
    def get_interest(self):
        return self._interest
       
    def get_repayment(self):
        return self._repayment
    
    def get_stack_months(self):
        return self._stack_months
    
    def get_stack_years(self):
        return self._stack_years
    
    def get_snowball_months(self):
        return self._snowball_months
    
    def get_snowball_years(self):
        return self._snowball_years
    
    def get_avalanche_months(self):
        return self._avalanche_months
    
    def get_avalanche_years(self):
        return self._avalanche_years
    
    def get_debt_list(self):
        return [self._amount, self._interest, self._repayment]

    def set_stack_months(self, months):
        self._stack_months = months
        self._stack_years = int(months/12)
    
    def set_snowball_months(self, months):
        self._snowball_months = months
        self._snowball_years = int(months/12)
    
    def set_avalanche_months(self, months):
        self._avalanche_months = months
        self._avalanche_years = int(months/12)
    
    def set_comparison_type_months(self, num_of_months, comparison_type):
        if comparison_type == 'stack':
            self.set_stack_months(num_of_months)
        elif comparison_type == 'snowball':
            self.set_snowball_months(num_of_months)
        elif comparison_type == 'avalanche':
            self.set_avalanche_months(num_of_months)
        else:
            raise "I don't know the comparison_type"
        # if all the conditions fail then raise an exception
    
    def comparison_dict(self):
        return {
            'amount': self._amount,
            'interest': self._interest,
            'repayment': self._repayment,
            'stack_paid_months': self._stack_months,
            'stack_paid_years': self._stack_years,
            'snowball_paid_months': self._snowball_months,
            'snowball_paid_years': self._snowball_years,
            'avalanche_paid_months': self._avalanche_months,
            'avalanche_paid_years': self._avalanche_years
        }
    
    