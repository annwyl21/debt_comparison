from wtforms import IntegerField, SubmitField
from flask_wtf import FlaskForm

class RepaymentForm(FlaskForm):
    repayment_commitment = IntegerField('Repayment Commitment')
    submit = SubmitField('Submit')

