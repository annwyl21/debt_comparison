from flask import render_template, request
from random import randint
import math
from application import app
from application.debt import Debt
from application.bundle import Bundle
from application.calculator import Calculator
from application.forms import ComparisonForm
from application.debt_entry_form import DebtEntryForm
from application.repayment_form import RepaymentForm


bundle = Bundle()
calculateDebt = Calculator()

@app.route('/')
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
            calculateDebt.add_debt_to_list({'identifier': identifier, 'amount': amount, 'interest': interest_rate, 'repayment': min_repayment})
            return render_template('next.html', form=form, message=error)
            
    return render_template('debt_form.html', form=form, message=error)

@app.route('/debt_summary', methods=['GET', 'POST'])
def debt_summary():
    list_of_debt_dicts = calculateDebt.get_debt_list()
    total = calculateDebt.get_total()
    error = ''
    form = RepaymentForm()

    if request.method == 'POST':
        repayment_commitment = form.repayment_commitment.data

        if repayment_commitment < total:
            error = 'Please enter a number larger than your required minimum repayment total'
        
        else:
            calculateDebt.set_total_repayment(repayment_commitment)
            calculateDebt.comparison_calc('stack_approach')
            calculateDebt.comparison_calc('snowball_approach')
            calculateDebt.comparison_calc('avalanche_approach')
            results = calculateDebt.get_debt_list()
            return render_template('results.html', debt_list=results)
        
    return render_template('debt_summary.html', debts=list_of_debt_dicts, total=total, form=form, error=error)
