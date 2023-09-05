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
		if repayment_method == 'stack_approach':
			self.stack_sorter()
		elif repayment_method == 'snowball_approach':
			self.snowball_sorter()
		else:
			self.avalanche_sorter()

		for debt in self.debt_list:
			# add a balance to deplete
			debt['balance'] = debt['amount']
			# add a key to store the number of months to repay using each method
			debt[repayment_method] = 0
		
		# calculate the extra money put towards debt repayment
		extra_repayment = self.total_repayment-self.total_min_repayment

		# cycle through the debts until they are paid and handle the extra repayments
		# creates an infinite loop at the moment
		while self.debt_list[-1]['balance'] > 0:
			repayment = self.total_repayment
			for debt in self.debt_list:
				print(debt['balance'])
				if debt['balance'] > debt['repayment']:
					debt['balance'] -= debt['repayment'] # pay off the minimum balance
					repayment -= debt['repayment'] # reduce the monthly repayment by paid amount
					debt[repayment_method] += 1 # add 1 to the count of months
					debt['balance'] -= repayment
					repayment = 0 # handle the extra money
				else:
					final_payment = debt['balance']
					debt['balance'] - final_payment
					repayment - final_payment
				print(debt['balance'])

if __name__ == '__main__':
	MrsTester = Calculator()
	MrsTester.add_debt_to_list({'identifier': 'test debt 1', 'amount': 1000, 'interest': 2, 'repayment': 100})
	MrsTester.add_debt_to_list({'identifier': 'test debt 2', 'amount': 5000, 'interest': 5, 'repayment': 250})

	# test sorter
	MrsTester.stack_sorter()
	MrsTester.snowball_sorter()
	MrsTester.avalanche_sorter()

	# test comparisoncalc
	MrsTester.comparison_calc('stack_approach')

