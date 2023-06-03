from flask_wtf import FlaskForm
from wtforms import Stringfield, Floatfield

class AddSanckForm(FlaskForm):
    """Form for adding snacks"""

    name = StringField("Snack Name")
    price = FloatField("Price in USD")
