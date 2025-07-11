"""This module contains the forms for the index page."""

from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import Optional


class VerbForm(FlaskForm):
    """Form for searching and filtering verbs."""

    verb = StringField("Search or filter by:", validators=[Optional()])
    submit = SubmitField("Search")
