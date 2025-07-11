from math import ceil

from flask import Blueprint, redirect, render_template, request

from app.db.database import DatabaseSingleton
from app.index.form import VerbForm

index_bp = Blueprint("index_bp", __name__, template_folder="templates")


@index_bp.route("/", methods=["GET", "POST"])
def index():
    form = VerbForm()
    conn = DatabaseSingleton().get_conn()

    per_page = 20
    page = request.args.get("page", 1, type=int)
    offset = (page - 1) * per_page

    if form.validate_on_submit():
        # Si se envió el formulario por POST, redirige a una URL con parámetro 'verb'
        search_term = form.verb.data.upper()
        return redirect(f"/?verb={search_term}")
    else:
        search_term = request.args.get("verb", "").upper()

    # --- Consulta de Verbos ---
    verb_query = "SELECT * FROM Verbs"
    count_query = "SELECT COUNT(*) FROM Verbs"
    verb_params = []
    count_params = []

    if search_term:
        where_clause = """
        WHERE SIMPLE_FORM LIKE ?
        OR THIRD_PERSON LIKE ?
        OR SIMPLE_PAST LIKE ?
        OR PAST_PARTICIPLE LIKE ?
        OR GERUND LIKE ?
        OR MEANING LIKE ?
        """
        verb_query += f" {where_clause}"
        count_query += f" {where_clause}"
        verb_params = count_params = [f"%{search_term}%"] * 6

    verb_query += " LIMIT ? OFFSET ?"
    verb_params.extend([per_page, offset])

    # Obtener verbos
    verb_cursor = conn.execute(verb_query, tuple(verb_params))
    verb_rows = verb_cursor.fetchall()
    verb_columns = [
        col[1] for col in conn.execute("PRAGMA table_info('Verbs');").fetchall()
    ]

    # Obtener todos los audios de AudioVerbs
    audio_cursor = conn.execute("SELECT * FROM AudioVerbs")
    audio_rows = audio_cursor.fetchall()
    audio_columns = [
        col[1] for col in conn.execute("PRAGMA table_info('AudioVerbs');").fetchall()
    ]

    # Construir audio_dict usando el campo ID de forma segura
    audio_dict = {}
    for row in audio_rows:
        audio_data = dict(zip(audio_columns, row))
        audio_id = audio_data.get("ID")
        if audio_id is not None:
            audio_dict[audio_id] = audio_data

    # Unir verbos con sus audios según ID
    verbs = []
    for row in verb_rows:
        verb = dict(zip(verb_columns, row))
        audio = audio_dict.get(verb.get("ID"), {})  # Accede por ID, no por índice

        verb["audio_simple"] = audio.get("SIMPLE_FORM", "")
        verb["audio_third"] = audio.get("THIRD_PERSON", "")
        verb["audio_past"] = audio.get("SIMPLE_PAST", "")
        verb["audio_part"] = audio.get("PAST_PARTICIPLE", "")
        verb["audio_gerund"] = audio.get("GERUND", "")

        verbs.append(verb)

    # Total de páginas
    count_cursor = conn.execute(count_query, tuple(count_params))
    total_rows = count_cursor.fetchone()[0]
    total_pages = ceil(total_rows / per_page)

    return render_template(
        "index.html",
        form=form,
        verbs=verbs,
        page=page,
        total_pages=total_pages,
        per_page=per_page,
        search_term=search_term,
    )
