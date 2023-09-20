# from application.debt import Debt
from debt import Debt

class Calculator:
	def __init__(self, debt_list, repayment):
		self._debt_list = debt_list
		self._total_balance = 0
		self._total_min_repayment = 0
		self._total_repayment = repayment
		self._month_count = 0

	def get_total_balance(self):
		return self._total_balance

	def get_total_min_repayment(self):
		return self._total_min_repayment

	def __str__(self):
		return f"Calculator Instance holds {len(self._debt_list)} debts and a submitted Repayment Amount of £{self._total_repayment:.2f}\nValues Subsequently calculated and tracked:\nTotal Debt Balance: £{self._total_balance:,.2f}\nTotal Minimum Repayment: {self._total_min_repayment}\nTotal Month Count: {self._month_count}"
	
	def set_balance_repayment(self):
		for debt in self._debt_list:
			self._total_balance += debt.get_amount()
			self._total_min_repayment += debt.get_repayment()
	
	def calculator(self):
		# set balance and repayment as sum of debt balances/ repayments in list of debt objects
		self.set_balance_repayment()
		# reset the balance of each debt object
		for debt in self._debt_list:
			debt.reset_balance()
		
		print('Month Count:', self._month_count)
		print('Total Debt Balance:', self._total_balance)
		print('Total Minimum Repayment Required:', self._total_min_repayment)

		# cycle through the debts until total debt balance = 0
		while self._total_balance > 0:
			repayment = self._total_repayment
			self._month_count += 1
			print('Month Count:', self._month_count)
			print('Total Debt Balance:', self._total_balance)
			
			for each_debt in self._debt_list: 
				current_balance = each_debt.get_balance()
				minimum_repayment = each_debt.get_repayment()

				# REPAY THE MIN BALANCE EACH MONTH
				# for debt in my_debt_list:
				if current_balance > minimum_repayment:
					each_debt.set_balance(minimum_repayment)
					# pay off the minimum balance

					repayment = repayment - minimum_repayment 
					# reduce the monthly repayment by paid amount

					# decrease the total debt balance by the repayment
					self._total_balance -= minimum_repayment

				else:
					final_payment = current_balance
					# pay the final balance and reduce the available repayment amount by the final payment
					each_debt.set_balance(final_payment)
					repayment -= final_payment

					# decrease the total debt balance by the repayment
					self._total_balance -= final_payment
				
				# collect repayment schedule data
				print(each_debt.get_identifier(), each_debt.get_balance())
				
			# USE EXTRA MONEY TO FOLLOW REPAYMENT APPROACH (stack, snowball, avalanche)
			# add a 2nd for loop to check the balances and pay any extra money each month towards the debts in turn according to their order in the list sorted by repayment approach
			for index in range(len(self._debt_list)):
				debt_to_check = self._debt_list[index-1]
				debt_balance = debt_to_check.get_balance()
				if debt_balance > 0:
					if repayment > debt_balance:
						debt_to_check.set_balance(debt_balance)
						# pay debt in full and put the remainder towards the next debt
						self._total_balance -= debt_balance

						# Note where the extra money goes
						print(f'Extra Repayment: {debt_to_check.get_identifier()}, {debt_to_check.get_balance()}, {debt_balance}')

						repayment -= debt_balance

					else:
						debt_to_check.set_balance(repayment)
					# decrease the debt balance by the repayment (above)
					# and reduce the total balance (below)
						self._total_balance -= repayment

						# Note where the extra money goes
						print(f'Extra Repayment: {debt_to_check.get_identifier()}, {debt_to_check.get_balance()}, {repayment}')

						repayment -= repayment
					

if __name__ == '__main__':

	debt1 = (Debt('test debt 1', 1000, 2, 100))
	debt2 = (Debt('test debt 2', 15000, 50, 250))
	debt3 = (Debt('test debt 3', 2000, 5, 150))

	debt_list = [debt1, debt2, debt3]
	repayment_commitment = 580

	MrsTester = Calculator(debt_list, repayment_commitment)
	print(MrsTester)

	MrsTester.calculator()
	
	
	