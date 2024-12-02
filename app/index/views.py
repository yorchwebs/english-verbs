from flask import Response, Blueprint, render_template, request
from utils.pydantic_validator import VerbFormModel
from app.index.form import VerbForm
from app.index.models import Verb
from typing import List
from math import ceil

index_bp = Blueprint(
    "index_bp", __name__, template_folder="templates", static_folder="static"
)


@index_bp.route("/", methods=["GET", "POST"])
def index() -> Response:
    """Handle index page and form submission."""
    form = VerbForm()
    per_page = 20  # Número de elementos por página
    page = request.args.get("page", 1, type=int)

    if form.validate_on_submit():
        page = 1
        # Insertar verbo y obtener verbos coincidentes
        verb: VerbFormModel = form.verb.data
        query = Verb.select()
        if verb:
            query: List[Verb] = query.select().where(
                (Verb.SIMPLE_FORM.contains(verb))
                | (Verb.THIRD_PERSON.contains(verb))
                | (Verb.SIMPLE_PAST.contains(verb))
                | (Verb.PAST_PARTICIPLE.contains(verb))
                | (Verb.GERUND.contains(verb))
                | (Verb.MEANING.contains(verb))
            )
    else:
        # Obtener todos los verbos si se envía el formulario sin un verbo específico
        query = Verb.select()

    # Obtener total de resultados y configurar la paginación
    total_verbs = query.count()
    total_pages = ceil(total_verbs / per_page)
    verbs = query.paginate(page, per_page)

    return render_template(
        "index.html",
        form=form,
        verbs=verbs,
        page=page,
        total_pages=total_pages,
        per_page=per_page,
    )