from flask import render_template, redirect, url_for
from app.forms import ExpenseForm
from app import app, db
from app.models import Expense
from datetime import datetime

@app.route("/", methods=['GET', 'POST'])
@app.route("/home", methods=['GET', 'POST'])

def index():
    form = ExpenseForm()
    if form.validate_on_submit():
        new_expense = Expense(
                    item = form.item.data,
                      amount = form.amount.data, date = datetime.utcnow())
        db.session.add(new_expense)
        db.session.commit()
        
        return redirect(url_for('index'))
    expenses = Expense.query.order_by(Expense.date.desc()).all()

    total_amount = sum(expenses.amount for expenses  in expenses)
    return render_template('index.html', form=form, expenses=expenses, total_amount=total_amount)
    