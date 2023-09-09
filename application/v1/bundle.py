class Bundle:
    def __init__(self):
        pass
   
    def debt_comparison_calc(self, debt_object1, debt_object2, debt_object3):
        stack = [debt_object1, debt_object2, debt_object3]
        debt_stack = sorted(stack, key=lambda debt: debt.get_interest(), reverse=True) # sorted by interest rate descending
        self.comparison_calc(debt_stack, 'stack')

        snowball = [debt_object1, debt_object2, debt_object3]
        snowball.sort(key = lambda debt: debt.get_amount())  # sorted by loan size ascending
        self.comparison_calc(snowball, 'snowball')

        avalanche = [debt_object1, debt_object2, debt_object3]
        avalanche.sort(key = lambda debt: debt.get_amount(), reverse=True)  # sorted by loan size descending
        self.comparison_calc(avalanche, 'avalanche')
        
    def comparison_calc(self, list_of_debts, comparison_type):
        num_of_months = 0
        extra_repayment = 0
        left_over = 0
        for debt in list_of_debts:
            balance = debt.get_amount()
            repayment = debt.get_repayment()
            try:
                while balance > 0:
                    if balance < repayment:
                        left_over = repayment - balance
                        balance = 0
                    balance = balance - repayment - extra_repayment - left_over
                    left_over = 0
                    num_of_months += 1
            except Exception as ex:
                raise ValueError("False argument in comparison_calc - maybe a repayment is zero")
            debt.set_comparison_type_months(num_of_months, comparison_type)
            extra_repayment += repayment
