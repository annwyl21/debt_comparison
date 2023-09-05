from flask import render_template, request
from random import randint
from application import app
from application.debt import Debt
from application.bundle import Bundle
from application.calculator import Calculator
from application.forms import ComparisonForm
from application.debt_entry_form import DebtEntryForm

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
            return render_template('next.html')
            
    return render_template('debt_form.html', form=form, message=error)

@app.route('/debt_summary')
def debt_summary():
    list_of_debt_dicts = calculateDebt.get_debt_list()
    total = calculateDebt.get_total()
    error = ''
    form = DebtEntryForm()

    if request.method == 'POST':
        repayment_commitment = form.repayment_commitment.data

        if repayment_commitment < total:
            error = 'Please enter a number larger than your required minimum repayment total'
        
        else:
            return render_template('results.html')
    return render_template('debt_summary.html', debts=list_of_debt_dicts, total=total)

@app.route('/results')
def results():
            
#             # UNPARCEL THE DEBTS, WIZARD THEM AND SEND BACK THE DATA

#             # send the debt objects into the comparison calc to find out how long each debt takes to pay off using each debt repayment approach (stack, snowball, avalanche)
#             bundle.debt_comparison_calc(debt_object1, debt_object2, debt_object3)

#             #sort the objects ready for display on the page
#             nested_list = [debt_object1, debt_object2, debt_object3]
#             order_list = [1, 2, 3]

#             stack_approach = sorted(nested_list, key=lambda debt_object: debt_object.get_interest(), reverse=True) # sort the debt objects, largest interest rate first
#             stack_dict = {order:debt_object for order, debt_object in zip(order_list, stack_approach)}

#             snowball_approach = sorted(nested_list, key=lambda debt_object: debt_object.get_amount())  # sorted by loan size ascending
#             snowball_dict = {order:debt_object for order, debt_object in zip(order_list, snowball_approach)}

#             avalanche_approach = sorted(nested_list, key=lambda debt_object: debt_object.get_amount(), reverse=True)  # sorted by loan size descending
#             avalanche_dict = {order:debt_object for order, debt_object in zip(order_list, avalanche_approach)}
#             # uses a dictionary to hold the order to avoid an object refernce problem
#             # In Python 3.6, the built-in dict class now keeps its items ordered as well


# @app.route('/debt_comparison_form', methods=['GET', 'POST'])
# def debt_comparison():
#     error = ''
#     form = ComparisonForm()
#     if request.method == 'POST':
#         debt1_amount = form.debt1_amount.data
#         min1_repayment = form.debt1_repayment.data
#         debt1_interest = form.debt1_interest.data

#         debt2_amount = form.debt2_amount.data
#         min2_repayment = form.debt2_repayment.data
#         debt2_interest = form.debt2_interest.data

#         debt3_amount = form.debt3_amount.data
#         min3_repayment = form.debt3_repayment.data
#         debt3_interest = form.debt3_interest.data

#         if not debt1_amount or not min1_repayment or not debt1_interest:
#             error = 'Please enter a debt amount, minimum repayment and rate of interest'
#         else:
#             # at the moment this only works if you enter all 3 debts, it needs a conditional and some more code to make it work if just 2 debts are entered          
#             debt_object1 = Debt(debt1_amount, debt1_interest, min1_repayment)
#             debt_object2 = Debt(debt2_amount, debt2_interest, min2_repayment)
#             debt_object3 = Debt(debt3_amount, debt3_interest, min3_repayment)
            
#             # send the debt objects into the comparison calc to find out how long each debt takes to pay off using each debt repayment approach (stack, snowball, avalanche)
#             bundle.debt_comparison_calc(debt_object1, debt_object2, debt_object3)

#             #sort the objects ready for display on the page
#             nested_list = [debt_object1, debt_object2, debt_object3]
#             order_list = [1, 2, 3]

#             stack_approach = sorted(nested_list, key=lambda debt_object: debt_object.get_interest(), reverse=True) # sort the debt objects, largest interest rate first
#             stack_dict = {order:debt_object for order, debt_object in zip(order_list, stack_approach)}

#             snowball_approach = sorted(nested_list, key=lambda debt_object: debt_object.get_amount())  # sorted by loan size ascending
#             snowball_dict = {order:debt_object for order, debt_object in zip(order_list, snowball_approach)}

#             avalanche_approach = sorted(nested_list, key=lambda debt_object: debt_object.get_amount(), reverse=True)  # sorted by loan size descending
#             avalanche_dict = {order:debt_object for order, debt_object in zip(order_list, avalanche_approach)}
#             # uses a dictionary to hold the order to avoid an object refernce problem
#             # In Python 3.6, the built-in dict class now keeps its items ordered as well

#             return render_template('results.html', stack_dict=stack_dict, snowball_dict=snowball_dict, avalanche_dict=avalanche_dict)

#     return render_template('debt_comparison_form.html', form=form, message=error)