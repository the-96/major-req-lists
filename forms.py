from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField
from wtforms.validators import DataRequired, Length, Email, EqualTo
from wtforms import StringField

class SearchForm(FlaskForm):
  search = StringField('search', [DataRequired()])
  submit = SubmitField('Search',
                       render_kw={'class': 'btn btn-success btn-block'})

class RegistrationForm(FlaskForm):
    username = StringField('Username',
                           validators = [DataRequired(), Length(min=2,max=15)])
    email = StringField('Email',
                        validators = [DataRequired(), Email()])
    password = PasswordField('Password',
                             validators = [DataRequired()])
    password2 = PasswordField('Confirm password',
                              validators = [DataRequired(), EqualTo('password')])
    submit = SubmitField('Sign up')


class LoginForm(FlaskForm):
    email = StringField('Email',
                        validators = [DataRequired(), Email()])
    password = PasswordField('Password',
                             validators = [DataRequired()])
    remember = BooleanField('Remember me')
    submit = SubmitField('Sign in')










