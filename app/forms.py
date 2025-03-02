from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, FloatField
from wtforms.validators import DataRequired

class ExpenseForm(FlaskForm):
    item = StringField('Item', validators=[DataRequired()], render_kw={"placeholder": "Enter item name"})
    amount = FloatField('Amount', validators=[DataRequired()],render_kw={"placeholder": "Enter Amount name"})
    submit = SubmitField('Submit')
