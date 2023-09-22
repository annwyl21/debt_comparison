from flask import render_template, request
from application import app
from application.debt import Debt
from application.repayment_approaches import RepaymentApproaches
from application.debt_entry_form import DebtEntryForm
from application.repayment_form import RepaymentForm
import math

calculateDebt = RepaymentApproaches()

@app.route('/')
@app.route('/index')
def index():
	return render_template('index.html')

@app.route('/debt_form', methods=['GET', 'POST'])
def debt_entry():
	error = ''
	form = DebtEntryForm()

	if request.method == 'POST':
		identifier = form.identifier.data
		amount = form.amount.data
		min_repayment = form.min_repayment.data
		interest_rate = form.interest_rate.data

		if not identifier or not amount or not min_repayment or not interest_rate:
			error = 'Please enter a debt name, amount, interest rate and minimum repayment, calculations and results set are based on the data supplied'
		
		else:
			#calculate monthly interest amount on a debt
			suggested_min_repayment = math.ceil((amount * (interest_rate/100)) /12)
			if min_repayment <= suggested_min_repayment:
				error = 'Minimum Repayment entered does not appear to cover interest on debt, please re-enter'
			calculateDebt.add_debt(Debt(identifier, amount, interest_rate, min_repayment))
			return render_template('next.html', form=form, message=error)
			
	return render_template('debt_form.html', form=form, message=error)

@app.route('/debt_summary', methods=['GET', 'POST'])
def debt_summary():
	debt_obj_list = calculateDebt.get_debt_collection()
	total_min_repayment = calculateDebt.get_total_min_repayment()
	error = ''
	form = RepaymentForm()

	if request.method == 'POST':
		repayment_commitment = form.repayment_commitment.data

		if repayment_commitment < total_min_repayment:
			error = 'Please enter a number larger than your required minimum repayment total'
		
		else:
			calculateDebt.set_repayment_commitment(repayment_commitment)
			calculateDebt.run_approaches()
			
			return render_template('results.html', results=calculateDebt)
		  
	return render_template('debt_summary.html', debt_obj_list=debt_obj_list, total_min_repayment=total_min_repayment, form=form, error=error)

@app.route('/<approach>')
def debt_details(approach):
		approach = approach
		title = f"{approach} repayment approach"
		return render_template('debt_detail.html', results=calculateDebt, title=title, approach=approach)

	
	