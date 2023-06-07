# Debt Comparison

To compare debts in order to identify the fastest repayment method

- Install the requirements
```bash
pip install -r requirements.txt
```

- Run the app.py file to start the site locally
```bash
python -m flask run
```

This calculator was developed solely by me as part of a larger group project to create a financial advice website.

The calculator is designed to compare 3 methods of debt repayment called the snowball, stack and avalanche approaches.
- A **snowball** approach is to pay off the smallest debt first, this is popular because it is often the easiest approach giving a high level of achievement because the smallest debts are cleared first and seemlingly faster.
- A **stack** approach is to pay off the debt with the highest level of interest first. This is a popular approach because it can be the cheaper option.
- An **avalanche** approach is to pay off the largest debt first, this can be a faster approach but is harder to commit to.
In all 3 approaches the __key to success__ is to commit a set amount of money to a baseline repayment and when one debt is repaid in full, instead of taking back that extra cash to keep the same amount of money going towards the debt and increase the repayments on the next debt.

Repayment approaches can seem complicated and confusing, this app uses simple maths to help calculate those approaches and make an **informed choice** about debt repayment.

Limitations:
- This app uses basic GCSE maths, it does not calculate compound interest or give the user an option to __top-up__ repayments, and 3 debts must be entered for the calculation to run.
- This app does not handle for negative interest rates.

This is the results page generated:
![Image - Results page from debt comparison app](./application/static/images/debtcomparison.jpg)