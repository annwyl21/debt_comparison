# holds each debt instance and adds information as the debt scenarios are executed
import math

class Debt:
	
	def __init__(self, identifier, amount, interest, repayment):
		self.identifier = identifier
		self._amount = amount
		self._interest = interest
		self._repayment = repayment

		self._balance = amount
		
		# STACK specific
		self.stack_months = 0
		self.stack_years = ''
		self.stack_repayments_list = []

		# SNOWBALL specific
		self.snowball_months = 0
		self.snowball_years = ''
		self.snowball_repayments_list = []

		# AVALANCHE specific
		self.avalanche_months = 0
		self.avalanche_years = ''
		self.avalanche_repayments_list = []

	def get_repayment(self):
		return self._repayment
	
	def get_interest(self):
		return self._interest
	
	def get_identifier(self):
		return self.identifier
	
	def get_amount(self):
		return self._amount
	
	def get_balance(self):
		return self._balance
	
	def set_balance(self, repayment):
		self._balance = self._balance - repayment
	
	def set_stack_months(self):
		self.stack_months +=1
	
	def get_stack_months(self):
		return self.stack_months
	
	def get_stack_years(self):
		return self.stack_years

	def set_snowball_months(self):
		self.snowball_months +=1

	def get_snowball_months(self):
		return self.stack_months
	
	def get_snowball_years(self):
		return self.stack_years

	def set_avalanche_months(self):
		self.avalanche_months +=1
	
	def get_avalanche_months(self):
		return self.avalanche_months
	
	def get_avalanche_years(self):
		return self.avalanche_years
	
	def add_years(self):
			# stack
			stack_years = math.ceil(self.stack_months/12)
			stack_months = self.stack_months - (stack_years*12)
			self.stack_years = f"{stack_years} years, {stack_months} months"

			# snowball
			snowball_years = math.ceil(self.snowball_months/12)
			snowball_months = self.snowball_months - (snowball_years*12)
			self.snowball_years = f"{snowball_years} years, {snowball_months} months"
			
			# avalanche
			avalanche_years = math.ceil(self.avalanche_months/12)
			avalanche_months = self.avalanche_months - (avalanche_years*12)
			self.avalanche_years = f"{avalanche_years} years, {avalanche_months} months"
	

	