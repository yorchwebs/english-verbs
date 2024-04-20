"""This module contains the views for the index page."""
from flask import Response
from flask import Blueprint
from flask import render_template

from typing import List

from app.index.models import Verb

from app.index.form import VerbForm

from app.index.utils.pydantic_validator import VerbFormModel

index_bp = Blueprint(
    "index_bp", __name__, template_folder="templates", static_folder="static"
)


@index_bp.route("/", methods=["GET", "POST"])
def index() -> Response:
    """Handle index page and form submission."""
    form: VerbForm = VerbForm()
    if form.validate_on_submit():
        # Insert verb and retrieve matching verbs
        verb: VerbFormModel = form.verb.data
        if verb:
            matching_verbs: List[Verb] = Verb.select().where(
                (Verb.simple_form.contains(verb))
                | (Verb.third_person.contains(verb))
                | (Verb.simple_past.contains(verb))
                | (Verb.past_participle.contains(verb))
                | (Verb.gerund.contains(verb))
                | (Verb.meaning.contains(verb))
            )
        else:
            # Retrieve all verbs if form is submitted but verb field is empty
            matching_verbs = Verb.select()
        return render_template("index.html", form=form, verbs=matching_verbs)
    # Retrieve all verbs if request method is GET
    verbs = Verb.select()
    return render_template("index.html", form=form, verbs=verbs)

