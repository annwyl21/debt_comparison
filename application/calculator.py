# calculator holds the debts as dictionaries

class Calculator:
	def __init__(self):
		self.debt_list = []
		self.used_names = []
		self.total_min_repayment = 0
		self.total_repayment = 0
	
	def add_debt_to_list(self, debt_dictionary):
		self.debt_list.append(debt_dictionary)
		self.total_min_repayment += debt_dictionary['repayment']

	def get_debt_list(self):
		return self.debt_list
	
	def get_total(self):
		return self.total_min_repayment
	
	def set_total_repayment(self, repayment_commitment):
		self.total_repayment = repayment_commitment

	
	def stack_sorter(self):
		# organises the debts by interest rate (largest first)
		stack = self.debt_list
		debt_stack = sorted(stack, key=lambda debt: debt['interest'], reverse=True)
		print(debt_stack)

	def snowball_sorter(self):
		# organises the debts by loan size (smallest first)
		snowball = self.debt_list
		debt_snowball = sorted(snowball, key=lambda debt: debt['amount'])
		print(debt_snowball)
	
	def avalanche_sorter(self):
		# organises the debts by loan size (largest first)
		avalanche = self.debt_list
		debt_avalanche = sorted(avalanche, key=lambda debt: debt['amount'], reverse=True)
		print(debt_avalanche)
	
	def comparison_calc(self, repayment_method):
		# rewrite this so that you pay each debt, every month and put the left overs towards the stack etc
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
				raise ValueError("False argument in comparison_calc")
			debt.set_comparison_type_months(num_of_months, comparison_type)
            extra_repayment += repayment

if __name__ == '__main__':
	MrsTester = Calculator()
	MrsTester.add_debt_to_list({'identifier': 'test debt 1', 'amount': 1000, 'interest': 2, 'repayment': 100})
	MrsTester.add_debt_to_list({'identifier': 'test debt 2', 'amount': 5000, 'interest': 5, 'repayment': 250})
	MrsTester.stack_sorter()
	MrsTester.snowball_sorter()
	MrsTester.avalanche_sorter()
	

        # self.comparison_calc(avalanche, 'avalanche')
