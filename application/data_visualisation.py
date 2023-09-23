from matplotlib import pyplot as plt
import matplotlib.colors as mcolors
import numpy as np
from application.debt import Debt
#from debt import Debt

class Graphs:
	def __init__(self, debt_collection, debt_dict):
		self.debt_collection = debt_collection
		self.debt_dict = debt_dict
	
	def create_pie(self):
		debt_figures = []
		debt_names = []
		debt_labels = []
		for debt_obj in self.debt_collection:
			debt_names.append(debt_obj.get_identifier())
			apr = debt_obj.get_interest()
			name = f"APR{apr}%"
			debt_labels.append(name)
			debt_figures.append(debt_obj.get_amount())
		self.debt_pie(debt_figures, debt_names, debt_labels)
	
	def debt_pie(self, debt_figures, debt_names, debt_labels):
		plt.switch_backend('Agg') # this changes where the computer generates the chart because that causes a problem on the Mac but not on windows
		plt.figure(figsize=(3,2))
		orange_shades = ['#f66218', '#e43e26', '#f78c4a', '#eb5940', '#d4460e', '#f8a57d', '#c62f16', '#f26c51', '#d14113']
		wedges, texts = plt.pie(debt_figures, labels=debt_names, labeldistance=0.5, colors=orange_shades)
		plt.axis('equal')
		colour_rgb = (69/255, 68/255, 68/255)
		for text in texts:
			text.set_color(colour_rgb)
		plt.title('Debt Summary', loc='left', color=colour_rgb)
		# plt.legend(labels=debt_labels, loc="upper right")
		plt.savefig('application/static/images/debt_pie.png', transparent=True)
		return 'pie chart created'
	
	def create_bar(self):
		debt_name = []
		paid_months = []
		for approach, result in self.debt_dict.items():
			if approach == 'stack':
				for debt, paid in result.items():
					debt_name.append(debt)
					paid_months.append(paid)
					self.debt_bar(debt_name, paid_months)
					plt.savefig('application/static/images/debt_bar_stack.png', transparent=True)
			elif approach == 'snowball':
				for debt, paid in result.items():
					debt_name.append(debt)
					paid_months.append(paid)
					self.debt_bar(debt_name, paid_months)
					plt.savefig('application/static/images/debt_bar_snowball.png', transparent=True)
			else:
				for debt, paid in result.items():
					debt_name.append(debt)
					paid_months.append(paid)
					self.debt_bar(debt_name, paid_months)
					plt.savefig('application/static/images/debt_bar_avalanche.png', transparent=True)
	
	def debt_bar(self, debt_name, paid):
		plt.figure(figsize=(3,2))
		cmap = mcolors.LinearSegmentedColormap.from_list('custom_orange', ['#FFDAB9', '#e43e26'])
		norm = plt.Normalize(min(paid), max(paid))
		colors = cmap(norm(paid))
		bars = plt.barh(debt_name, paid, color=colors)
		colour_rgb = (69/255, 68/255, 68/255)
		ax = plt.gca()
		ax.spines['top'].set_visible(False)
		ax.spines['right'].set_visible(False)
		ax.spines['left'].set_color(colour_rgb)
		ax.spines['bottom'].set_color(colour_rgb)
		for bar, label in zip(bars, debt_name):
			width = bar.get_width()
			plt.text(0.5,
			bar.get_y() + bar.get_height()/2,  # y position (centered in the bar)
			label,  # text value
			va='center',  # vertical alignment
			ha='left',   # horizontal alignment
			color=colour_rgb)  # text color
		plt.yticks([])
		plt.xticks(color=colour_rgb)
		plt.xlabel('Debt paid in full (months)', color=colour_rgb)
		
	

if __name__ == '__main__':

	overdraft = (Debt('Overdraft', 1000, 10, 100))
	loan = (Debt('Bank Loan', 15000, 5, 250))
	creditcard = (Debt('Credit Card', 2000, 50, 150))

	debt_collection = [overdraft, loan, creditcard]
	debt_dict = {'stack': {'Overdraft': 6}, 'snowball': {'Overdraft': 6}, 'avalanche': {'Overdraft': 6}}

	graph = Graphs(debt_collection, debt_dict)
	graph.create_pie()
	graph.create_bar()
