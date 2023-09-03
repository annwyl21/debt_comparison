from wtforms import IntegerField, SubmitField, StringField
from flask_wtf import FlaskForm

class DebtEntryForm(FlaskForm):
    identifier = StringField('Debt Identifier')
    amount = IntegerField('Debt Amount Outstanding')
    min_repayment = IntegerField('Minimum Repayment')
    interest_rate = IntegerField('Debt Interest Rate (APR)')
    
    submit = SubmitField('Submit')

# Each debt is entered, the data is saved in the program only (no database or local storage)
