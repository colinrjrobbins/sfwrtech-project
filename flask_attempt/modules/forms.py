from flask_wtf import FlaskForm
from wtforms import StringField, DecimalField, Label, SubmitField

class MovieSearch(FlaskForm):
    movieName = StringField('movieName')
    genre = StringField('genre')
    year = DecimalField('year')

class SignIn(FlaskForm):
    email = StringField('email')

class SearchResult(FlaskForm):
    movie_name = Label('movie_name')
    description = Label('description')
    submit = SubmitField('submit')