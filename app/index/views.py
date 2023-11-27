from flask import Blueprint, render_template, request

from app.index.models import Verb

from app.index.form import VerbForm

from app.index.pydantic_validator import VerbFormModel

index_bp = Blueprint(
    "index_bp", __name__, template_folder="templates", static_folder="static"
)


@index_bp.route("/", methods=["GET", "POST"])
def index():
    form: VerbForm = VerbForm()

    if request.method == "POST" and form.validate_on_submit():
        insert_verb = VerbFormModel(verb=form.verb.data)
        if insert_verb.verb:
            verbs = Verb.select().where(
                (Verb.simple_form.contains(insert_verb.verb))
                | (Verb.third_person.contains(insert_verb.verb))
                | (Verb.simple_past.contains(insert_verb.verb))
                | (Verb.past_participle.contains(insert_verb.verb))
                | (Verb.gerund.contains(insert_verb.verb))
                | (Verb.meaning.contains(insert_verb.verb))
            )
        else:
            verbs = Verb.select(
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

    all_verbs = Verb.select(
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
