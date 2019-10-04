from flask_wtf import FlaskForm
from wtforms import SelectField, SubmitField, StringField
from wtforms.validators import DataRequired, Length, EqualTo, ValidationError


class formularioLogin(FlaskForm):
    email = StringField('email')
    submit = SubmitField("Send Email")
