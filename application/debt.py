# holds each debt instance and adds information as the debt scenarios are executed
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
		return f"Details of Debt Entered:\nDebt ID: {self.identifier}\nDebt Amount: {self._amount}, Interest: {self._interest}, Minimum Monthly Repayment: {self._repayment}\nDebt Balance Tracked as each approach is applied {self._balance}"
	
	def reset_balance(self):
		self._balance = self._amount

	def set_balance(self, repayment):
		self._balance = self._balance - repayment

	def get_balance(self):
		return self._balance
		
	def set_month_paid(self, months):
		self.get_month_paid = months

	def get_month_paid(self):
		return self._month_paid

if __name__ == '__main__':
	debt1 = Debt('overdraft', 2000, 3, 80)
	print(debt1)
