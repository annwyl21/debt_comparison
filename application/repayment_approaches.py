from application.debt import Debt
from application.calculator import Calculator
# from debt import Debt
# from calculator import Calculator

class RepaymentApproaches:
	def __init__(self):
		self.debt_collection = []
		self.repayment = -1
		self.total_min_repayment = 0

		self.stack_time_years = ''
		self.snowball_time_years = ''
		self.avalanche_time_years = ''

		self._debt_dict = {}
	
	def get_repayment_commitment(self):
		return self.repayment
	
	def set_repayment_commitment(self, repayment):
		self.repayment = repayment

	def add_debt(self, debt_instance):
		self.debt_collection.append(debt_instance)
		self.total_min_repayment += debt_instance.get_repayment()
	
	def get_debt_collection(self):
		return self.debt_collection
	
	def get_debt_time(self):
		return self.stack_time_years
	
	def get_debt_dict(self):
		return self._debt_dict
	
	def get_total_min_repayment(self):
		return self.total_min_repayment
	
	def __str__(self):
		return f"Calculator Instance holds {len(self.debt_collection)} debts and a submitted Repayment Amount of £{self.repayment:.2f}.\nResults:\n{self.stack_time_years}\n{self._debt_dict}"
	
	def run_approaches(self):
		self._debt_dict['stack'] = self.stack()
		self._debt_dict['snowball'] = self.snowball()
		self._debt_dict['avalanche'] = self.avalanche()
	
	def stack(self):
		stack = self.stack_sorter()
		stack_instance = Calculator(stack, self.repayment)
		stack_instance.calculator()
		stack_results = stack_instance.get_debt_paid()
		time_months = stack_instance.get_month_count()
		self.stack_time_years = self.convert_months_to_years(time_months)
		return stack_results

	def stack_sorter(self):
		# organises the debts by interest rate (largest first)
		stack = self.debt_collection
		debt_stack = sorted(stack, key=lambda debt: debt._interest, reverse=True)
		return debt_stack
	
	def snowball(self):
		snowball = self.snowball_sorter()
		snowball_instance = Calculator(snowball, self.repayment)
		snowball_instance.calculator()
		snowball_results = snowball_instance.get_debt_paid()
		time_months = snowball_instance.get_month_count()
		self.snowball_time_years = self.convert_months_to_years(time_months)
		return snowball_results
	
	def snowball_sorter(self):
		# organises the debts by loan size (smallest first)
		snowball = self.debt_collection
		debt_snowball = sorted(snowball, key=lambda debt: debt._amount)
		return debt_snowball
	
	def avalanche(self):
		avalanche = self.avalanche_sorter()
		avalanche_instance = Calculator(avalanche, self.repayment)
		avalanche_instance.calculator()
		avalanche_results = avalanche_instance.get_debt_paid()
		time_months = avalanche_instance.get_month_count()
		self.avalanche_time_years = self.convert_months_to_years(time_months)
		return avalanche_results
	
	def avalanche_sorter(self):
		# organises the debts by loan size (largest first)
		avalanche = self.debt_collection
		debt_avalanche = sorted(avalanche, key=lambda debt: debt._amount, reverse=True)
		return debt_avalanche
	
	def convert_months_to_years(self, total_months):
		years = int(total_months/12)
		months = total_months - (years*12)
		return f"{years} years, {months} months"


if __name__ == '__main__':

	MrsTester = RepaymentApproaches()

	MrsTester.add_debt(Debt('Overdraft', 1000, 10, 100))
	MrsTester.add_debt(Debt('Bank Loan', 15000, 5, 250))
	MrsTester.add_debt(Debt('Credit Card', 2000, 50, 150))

	MrsTester.set_repayment_commitment(580)
	
	MrsTester.run_approaches()
	print(MrsTester)
