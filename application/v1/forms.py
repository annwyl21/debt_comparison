from wtforms import IntegerField, SubmitField, BooleanField, SelectField, StringField
from flask_wtf import FlaskForm

class ComparisonForm(FlaskForm):
    debt1_amount = IntegerField('Debt Amount')
    debt1_repayment = IntegerField('Minimum Repayment')
    debt1_interest = IntegerField('Debt Interest Rate (APR)')
    
    debt2_amount = IntegerField('Debt Amount')
    debt2_repayment = IntegerField('Minimum Repayment')
    debt2_interest = IntegerField('Debt Interest Rate (APR)')
    
    debt3_amount = IntegerField('Debt Amount')
    debt3_repayment = IntegerField('Minimum Repayment')
    debt3_interest = IntegerField('Debt Interest Rate (APR)')
    
    submit = SubmitField('Submit')
