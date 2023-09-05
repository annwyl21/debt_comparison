class Calculator:
	def __init__(self):
		self.debt_list = []
	
	def add_debt_to_list(self, debt_instance):
		self.debt_list.append(debt_instance)
		print(self.debt_list)

	def get_debt_list(self):
		return self.debt_list
