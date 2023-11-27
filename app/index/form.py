from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField


class VerbForm(FlaskForm):
    verb = StringField("Search and Filter By:")
    submit = SubmitField("Search")
