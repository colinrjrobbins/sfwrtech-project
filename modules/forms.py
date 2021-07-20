from flask_wtf import FlaskForm
from wtforms import StringField, DecimalField

class MovieSearch(FlaskForm):
    movieName = StringField('movieName')
    genre = StringField('genre')
    year = DecimalField('year')

class SignIn(FlaskForm):
    email = StringField('email')