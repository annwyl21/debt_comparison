# holds each debt instance and adds information as the debt scenarios are executed
import math
class Debt:
	
	def __init__(self, identifier, amount, interest, repayment):
		self.identifier = identifier
		self._amount = amount
		self._interest = interest
		self._repayment = repayment

		self._balance = amount
		self._month_paid = -1

	def get_identifier(self):
		return self.identifier

	def get_amount(self):
		return self._amount

	def get_interest(self):
		return self._interest
		
	def get_repayment(self):
		return self._repayment
	
	def __str__(self):
		return f"Details of Debt Entered...\n\tDebt ID: {self.identifier}\n\tDebt Amount £{self._amount:,.2f}, APR: {self._interest}%, Minimum Monthly Repayment £{self._repayment:,.2f}\n\tDebt Balance Tracked as each approach is applied £{self._balance:,.2f}"
	
	def reset_balance(self):
		self._balance = self._amount

	def set_balance(self, repayment):
		self._balance = self._balance - repayment
		return self._balance

	def get_balance(self):
		return self._balance
		
	def set_month_paid(self, months):
		self.get_month_paid = months

	def get_month_paid(self):
		return self._month_paid
	
	def add_interest(self):
		outstanding_balance = self._balance
		apr = self._interest/100
		#calculate monthly interest amount on a debt
		monthly_interest_amount = math.ceil((outstanding_balance * apr) /12)
		if monthly_interest_amount > outstanding_balance:
			raise ValueError()
		# add that interest on to the total balance
		self._balance = self._balance + monthly_interest_amount

		return monthly_interest_amount

if __name__ == '__main__':
	debt1 = Debt('overdraft', 1000, 10, 100)
	print(debt1)

	debt1.add_interest()
	print(debt1)
	
