"""This module contains the forms for the index page."""
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField


class VerbForm(FlaskForm):
    """Form for searching and filtering verbs."""
    verb = StringField("Search and Filter By:")
    submit = SubmitField("Search")
