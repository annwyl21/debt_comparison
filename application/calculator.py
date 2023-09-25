from application.debt import Debt
#from debt import Debt
import math

class Calculator:
	def __init__(self, debt_list, repayment):
		self._debt_list = debt_list
		self._total_balance = 0
		self._total_min_repayment = 0
		self._total_repayment = repayment
		self._month_count = -1
		self._repayments_list = []
		self._debt_paid = {}
		self._repayments_made = 0

	def get_total_balance(self):
		return self._total_balance

	def get_total_min_repayment(self):
		return self._total_min_repayment
	
	def get_repayments_made(self):
		return self.get_total_repayments
	
	def reset_repayments_made(self):
		self.total_repayments = 0
	
	def get_month_count(self):
		return self._month_count
	
	def set_month_count(self):
		self._month_count += 1
		return self._month_count
	
	def get_repayments_list(self):
		# a list detailing where extra repayments were made
		# only holds 1 approach at a time
		# data for all 3 approaches is held in repayment approaches class
		return self._repayments_list
	
	def get_debt_paid(self):
		# holds the debt_id and the number of repayments to clear
		# using the last approach fed through the calculator
		# repayment approaches holds data for all the debts
		return self._debt_paid

	def __str__(self):
		return f"Calculator Instance holds {len(self._debt_list)} debts and a submitted Repayment Amount of £{self._total_repayment:.2f}\nValues Subsequently calculated and tracked:\n\tTotal Debt Balance: £{self._total_balance:,.2f}\n\tTotal Minimum Repayment: {self._total_min_repayment}\n\tTotal Month Count: {self._month_count}\nRepayments Data Returned:\n\t{self.print_repayments()}, {self._debt_paid}"
	
	def print_repayments(self):
		for month in self._repayments_list:
			print(month)
		return f"printed"
	
	def set_balance_repayment(self):
		for debt in self._debt_list:
			self._total_balance += debt.get_amount()
			self._total_min_repayment += debt.get_repayment()
	
	def add_interest_to_total_balance(self, debt_instance):
		# add interest to the debt
		monthly_interest_applied = debt_instance.add_interest()
		# increase the debt total by the extra monthly interest
		self._total_balance += monthly_interest_applied
		return self._total_balance

	
	def calculator(self):
		# set balance and repayment as sum of debt balances/ repayments in list of debt objects
		self._month_count = 0
		self.set_balance_repayment()
		# reset the balance of each debt object
		for debt_obj in self._debt_list:
			debt_obj.reset_balance()

		self._repayments_list.append(['Month', self._total_balance, 'Targeted Debt', 'Extra Repayment'])
		

		# cycle through the debts until total debt balance = 0
		while self._total_balance > 0:
			repayment = self._total_repayment
			# add interest or record any paid debts
			for d in self._debt_list:
				if d.get_balance() == 0 and (d.get_identifier() not in self._debt_paid):
					self._debt_paid[d.get_identifier()] = self._month_count
				else:
					# add interest to the debt
					self.add_interest_to_total_balance(d)
			# increase the month count
			self.set_month_count()
			
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

					# increase total paid
					self._repayments_made += minimum_repayment

				else:
					final_payment = current_balance
					# pay the final balance and reduce the available repayment amount by the final payment
					each_debt.set_balance(final_payment)
					repayment -= final_payment

					# decrease the total debt balance by the repayment
					self._total_balance -= final_payment

					# increase total paid
					self._repayments_made += final_payment
				
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

						# increase total paid
						self._repayments_made += debt_balance

						# Note where the extra money goes
						if repayment > 0:
							self._repayments_list.append([self._month_count, self._total_balance, debt_to_check.get_identifier(), repayment])

						repayment -= debt_balance

						# increase total paid
						self._repayments_made += debt_balance

					else:
						debt_to_check.set_balance(repayment)
					# decrease the debt balance by the repayment (above)
					# and reduce the total balance (below)
						self._total_balance -= repayment

						# increase total paid
						self._repayments_made += repayment

						# Note where the extra money goes
						if repayment > 0:
							self._repayments_list.append([self._month_count, self._total_balance, debt_to_check.get_identifier(), repayment])

						repayment -= repayment


		# add last debt to paid list
		for d in self._debt_list:
			if d.get_identifier() not in self._debt_paid:
				self._debt_paid[d.get_identifier()] = self._month_count
		
		return self._repayments_list 

if __name__ == '__main__':

	debt1 = (Debt('Smallest Debt', 1000, 2, 50))
	debt2 = (Debt('Largest Debt', 5000, 5, 150))
	debt3 = (Debt('Highest Interest', 2500, 15, 250))

	debt_list = [debt1, debt2, debt3]
		# REPAYMENT COMMITMENT MUST BE ENTERED BELOW AND MUST COVER INTEREST ON DEBT
	repayment_commitment = 500

	MrsTester = Calculator(debt_list, repayment_commitment)
	MrsTester.calculator()
	
	print(MrsTester)

	
	