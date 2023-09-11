from flask import render_template, request
from random import randint
import math
from application import app
from application.debt import Debt
from application.v1.bundle import Bundle
from application.calculator import Calculator
from application.v1.forms import ComparisonForm
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
            calculateDebt.add_debt_to_list(Debt(identifier, amount, interest_rate, min_repayment))
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
            calculateDebt.comparison_calc('stack')
            calculateDebt.comparison_calc('snowball')
            calculateDebt.comparison_calc('avalanche')
            results = calculateDebt.add_years()
            for debt in debt_list
                debt.add years()
            calculateDebt.debt_free()
            repay = calculateDebt.get_total_repayment()
            stack = calculateDebt.get_max_stack()
            snowball = calculateDebt.get_max_snowball()
            avalanche = calculateDebt.get_max_avalanche()
            stack_list = calculateDebt.get_stack_detail()
            snowball_list = calculateDebt.get_snowball_detail()
            avalanche_list = calculateDebt.get_avalanche_detail()
            return render_template('results.html', debt_list=results, repay=repay, stack=stack, snowball=snowball, avalanche=avalanche, stack_list = stack_list, snowball_list=snowball_list, avalanche_list=avalanche_list)
        
    return render_template('debt_summary.html', debts=list_of_debt_dicts, total=total, form=form, error=error)
