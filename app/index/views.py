"""This module contains the views for the index page."""
from flask import request
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
    """Render the index page and handle form submission."""
    form: VerbForm = VerbForm()
    if request.method == "POST" and form.validate_on_submit():
        # If the form is submitted and valid,
        # insert the verb and retrieve matching verbs
        insert_verb: VerbFormModel = VerbFormModel(verb=form.verb.data)
        if insert_verb.verb:
            verbs: List[str] = Verb.select().where(
                (Verb.simple_form.contains(insert_verb.verb))
                | (Verb.third_person.contains(insert_verb.verb))
                | (Verb.simple_past.contains(insert_verb.verb))
                | (Verb.past_participle.contains(insert_verb.verb))
                | (Verb.gerund.contains(insert_verb.verb))
                | (Verb.meaning.contains(insert_verb.verb))
            )
        else:
            # If the form is submitted but the verb field is empty,
            # retrieve all verbs
            verbs: List[str] = Verb.select(
                Verb.num_id,
                Verb.verb_type,
                Verb.simple_form,
                Verb.third_person,
                Verb.simple_past,
                Verb.past_participle,
                Verb.gerund,
                Verb.meaning,
            )
        return render_template("index.html", form=form, verbs=verbs)
    # If the request method is GET, retrieve all verbs and render the
    # index page
    all_verbs: List[str] = Verb.select(
        Verb.num_id,
        Verb.verb_type,
        Verb.simple_form,
        Verb.third_person,
        Verb.simple_past,
        Verb.past_participle,
        Verb.gerund,
        Verb.meaning,
    )
    return render_template("index.html", form=form, verbs=all_verbs)
