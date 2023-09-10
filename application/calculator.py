import math
from debt import Debt


# calculator holds the debts as dictionaries

class Calculator:
	def __init__(self):
		self.debt_list = []
		# self.used_names = []
		self.total_min_repayment = 0
		self.total_repayment = 0
		self.max_stack = ''
		self.max_snowball = ''
		self.max_avalanche = ''
		self.stack_detail = []
		self.snowball_detail = []
		self.avalanche_detail = []
	
	def add_debt_to_list(self, debt_instance):
		self.debt_list.append(debt_instance)
		self.total_min_repayment += debt_instance.get_repayment()
		return self.debt_list, self.total_min_repayment

	def get_debt_list(self):
		return self.debt_list
	
	def get_total(self):
		return self.total_min_repayment
	
	def get_total_repayment(self):
		return self.total_repayment
	
	def get_max_stack(self):
		return self.max_stack
	
	def get_max_snowball(self):
		return self.max_snowball
	
	def get_max_avalanche(self):
		return self.max_avalanche
	
	def get_stack_detail(self):
		return self.stack_detail
	
	def set_total_repayment(self, repayment_commitment):
		if repayment_commitment > self.total_min_repayment:
			self.total_repayment = repayment_commitment
		else:
			self.total_repayment = self.total_min_repayment
	
	def stack_sorter(self):
		# organises the debts by interest rate (largest first)
		stack = self.debt_list
		debt_stack = sorted(stack, key=lambda debt: debt.get_interest(), reverse=True)
		for debt in debt_stack:
			self.stack_detail.append(debt.get_identifier())
		return debt_stack

	def snowball_sorter(self):
		# organises the debts by loan size (smallest first)
		snowball = self.debt_list
		debt_snowball = sorted(snowball, key=lambda debt: debt.get_amount())
		for debt in debt_snowball:
			self.snowball_detail.append(debt.get_identifier())
		return debt_snowball
	
	def avalanche_sorter(self):
		# organises the debts by loan size (largest first)
		avalanche = self.debt_list
		debt_avalanche = sorted(avalanche, key=lambda debt: debt.get_amount(), reverse=True)
		for debt in debt_avalanche:
			self.avalanche_detail.append(debt.get_identifier())
		return debt_avalanche

	def stack_time(self):
		# find when all debts have been repaid
		stack = self.debt_list
		debt_stack = sorted(stack, key=lambda debt: debt.get_stack_months(), reverse=True)
		last_debt = debt_stack[0]
		self.max_stack = last_debt.get_stack_years()

	def snowball_time(self):
		snowball = self.debt_list
		debt_snowball = sorted(snowball, key=lambda debt: debt.get_snowball_months(), reverse=True)
		last_debt = debt_snowball[0]
		self.max_snowball = last_debt.get_snowball_years()
	
	def avalanche_time(self):
		avalanche = self.debt_list
		debt_avalanche = sorted(avalanche, key=lambda debt: debt.get_avalanche_months(), reverse=True)
		last_debt = debt_avalanche[0]
		self.max_avalanche = last_debt.get_avalanche_years()
	
	def comparison_calc(self, repayment_method):
		# rewrite this so that you pay each debt, every month and put the left overs towards the stack etc
		if repayment_method == 'stack':
			my_debt_list = self.stack_sorter()
		elif repayment_method == 'snowball':
			my_debt_list = self.snowball_sorter()
		else:
			my_debt_list = self.avalanche_sorter()
		
		# cycle through the debts until they are paid and handle the extra repayments
		for my_debt in my_debt_list[:-1]: # until all the debts are paid
			while my_debt.get_balance() >0:
				repayment = self.total_repayment
				for debt in my_debt_list:
					current_balance = debt.get_balance()
					minimum_repayment = debt.get_repayment()
					if current_balance > minimum_repayment:
						debt.set_balance(minimum_repayment) # pay off the minimum balance
						repayment = repayment - minimum_repayment # reduce the monthly repayment by paid amount
						if repayment_method == 'stack':
							debt.set_stack_months()
						elif repayment_method == 'snowball':
							debt.set_snowball_months()
						else:
							debt.set_avalanche_months()
						# add 1 to the count of months

					else:
						final_payment = current_balance
						debt.set_balance(final_payment)
						repayment - final_payment
				# add a 2nd for loop to check the balance and pay the extra money towards each debt in turn
				for index in range(len(my_debt_list)-1):
					debt_to_check = my_debt_list[index]
					debt_balance = debt_to_check.get_balance()
					if debt_balance > 0:
						debt_to_check.set_balance(repayment)
						repayment = 0 # handle the extra money, the pennies left etc
		self.debt_list = my_debt_list
		return my_debt_list
	
	def debt_free(self):
		# how long to pay all debts
		self.stack_time()
		self.snowball_time()
		self.avalanche_time()


if __name__ == '__main__':


	MrsTester = Calculator()

	MrsTester.add_debt_to_list(Debt('test debt 1', 1000, 2, 100))
	MrsTester.add_debt_to_list(Debt('test debt 2', 15000, 50, 250))

	# test sorter
	print(MrsTester.stack_sorter())
	print(MrsTester.snowball_sorter())
	print(MrsTester.avalanche_sorter())

	MrsTester.set_total_repayment(350) # Mrs Tester decides how much she can afford, not alot it is just the minimum balance required!

	# test comparisoncalc
	# DEBUG FROM HERE
	debts_paid = MrsTester.comparison_calc('stack')
	more_paid = MrsTester.comparison_calc('snowball')
	alternative_paid = MrsTester.comparison_calc('avalanche')
	for debt in debts_paid:
		print(debt['identifier'], debt['stack_approach'])
	
	# results = MrsTester.get_debt_list()
	# print(results)	

	# MrsTester.add_years()
	# print(f"If Mrs Tester paid off {MrsTester.get_total_repayment()} each month")

	# MrsTester.debt_free()
	# print(MrsTester.get_max_stack())
	# print(MrsTester.get_max_snowball())
	# print(MrsTester.get_max_avalanche())
