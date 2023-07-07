from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, TextAreaField
from wtforms.validators import InputRequired, Length


class UserForm(FlaskForm):
    username = StringField("Username", validators=[InputRequired()])
    password = PasswordField("Password", validators=[InputRequired()])


class TweetForm(FlaskForm):
    text = TextAreaField("Tweet Text", validators=[InputRequired(), Length(max=150)], render_kw={'maxlength': '150', 'placeholder': 'Enter your tweet (150 characters max)'})

    def validate_text(self, field):
        if field.data is not None and len(field.data) > 150:
            raise ValidationError('Exceeded maximum character limit.')