from flask_wtf import FlaskForm
from wtforms import StringField, FloatField, BooleanField, RadioField, SelectField
from wtforms.validators import InputRequired, Optional, Email

states = ["AK", "AL", "AR", "AS", "AZ", "CA", "CO", "CT", "DC", "DE", "FL", "GA", "GU", "HI", "IA", "ID", "IL", "IN", "KS", "KY", "LA", "MA", "MD", "ME", "MI", "MN", "MO", "MP",
          "MS", "MT", "NC", "ND", "NE", "NH", "NJ", "NM", "NV", "NY", "OH", "OK", "OR", "PA", "PR", "RI", "SC", "SD", "TN", "TX", "UM", "UT", "VA", "VI", "VT", "WA", "WI", "WV", "WY"]


class AddSnackForm(FlaskForm):
    """Form for adding snacks"""
    email = StringField("Email", validators=[Optional(), Email()])
    name = StringField("Snack Name", validators=[
                       InputRequired("Snack Name can't be blank")])
    price = FloatField("Price in USD")
    quantity = FloatField("How many")
    is_healthy = BooleanField("This is a healthy snack")
    # catageory = RadioField("Catageory", choices=
    #                        [('ic','Ice Cream'),('chips','Potato Chips'),('candy','Candy/Sweets')])
    catageory = SelectField("Catageory", choices=[(
        'ic', 'Ice Cream'), ('chips', 'Potato Chips'), ('candy', 'Candy/Sweets')])


class EmployeeForm(FlaskForm):
    """Form for adding new employee"""

    name = StringField("Employee Name", validators=[
                       InputRequired(message="Name cannot be blank")])
    state = SelectField("State", choices=[(st, st) for st in states])
    dept_code = SelectField("Department Code")
