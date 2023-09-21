# from application.debt import Debt
# from application.calculator import Calculator
from debt import Debt
from calculator import Calculator

class RepaymentApproaches:
	def __init__(self, debt_collection, repayment):
		self.debt_collection = debt_collection
		self.repayment = repayment

		self.stack_time_years = ''
		self.snowball_time_years = ''
		self.avalanche_time_years = ''

		self._debt_dict = {}
		self._months_data = []
		self._years_data = []
	
	def get_repayment_commitment(self):
		return self.repayment
	
	def __str__(self):
		return f"Calculator Instance holds {len(self.debt_collection)} debts and a submitted Repayment Amount of £{self.repayment:.2f}.\nRepayment Approach Results: {self._debt_dict}"
	
	def run_approaches(self):
		self.stack()
		self.snowball()
		self.avalanche()
	
	def stack(self):
		stack = self.stack_sorter()
		stack_instance = Calculator(stack, self.repayment)
		stack_instance.calculator()
		for debt in stack:
			self._months_data.append(debt.get_month_paid())
			years = self.convert_months_to_years(debt.get_month_paid())
			self._years_data.append(years)
		self._debt_dict['stack_months'] = self._months_data
		self._debt_dict['stack_years'] = self._years_data
		time_months = stack_instance.get_month_count()
		self.stack_time_years = self.convert_months_to_years(time_months)

	def stack_sorter(self):
		# organises the debts by interest rate (largest first)
		stack = self.debt_collection
		debt_stack = sorted(stack, key=lambda debt: debt._interest, reverse=True)
		return debt_stack
	
	def snowball(self):
		snowball = self.snowball_sorter()
		snowball_instance = Calculator(snowball, self.repayment)
		snowball_instance.calculator()
		for debt in snowball:
			self._months_data.append(debt.get_month_paid())
			years = self.convert_months_to_years(debt.get_month_paid())
			self._years_data.append(years)
		self._debt_dict['snowball_months'] = self._months_data
		self._debt_dict['snowball_years'] = self._years_data
		time_months = snowball_instance.get_month_count()
		self.snowball_time_years = self.convert_months_to_years(time_months)
	
	def snowball_sorter(self):
		# organises the debts by loan size (smallest first)
		snowball = self.debt_collection
		debt_snowball = sorted(snowball, key=lambda debt: debt._amount)
		return debt_snowball
	
	def avalanche(self):
		avalanche = self.avalanche_sorter()
		avalanche_instance = Calculator(avalanche, self.repayment)
		avalanche_instance.calculator()
		for debt in avalanche:
			self._months_data.append(debt.get_month_paid())
			years = self.convert_months_to_years(debt.get_month_paid())
			self._years_data.append(years)
		self._debt_dict['avalanche_months'] = self._months_data
		self._debt_dict['avalanche_years'] = self._years_data
		time_months = avalanche_instance.get_month_count()
		self.avalanche_time_years = self.convert_months_to_years(time_months)
	
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

	debt1 = (Debt('Overdraft', 1000, 10, 100))
	debt2 = (Debt('Bank Loan', 15000, 5, 250))
	debt3 = (Debt('Credit Card', 2000, 50, 150))

	debt_list = [debt1, debt2, debt3]
	repayment_commitment = 580
	
	MrsTester = RepaymentApproaches(debt_list, repayment_commitment)
	MrsTester.run_approaches()
	print(MrsTester)
	

	