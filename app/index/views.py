from math import ceil

from flask import Blueprint, render_template, request

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

    search_term = (
        form.verb.data.upper()
        if form.validate_on_submit()
        else request.args.get("verb", "").upper()
    )

    # Base queries
    base_query = "SELECT * FROM Verbs"
    count_query = "SELECT COUNT(*) FROM Verbs"
    params = []
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
        base_query += f" {where_clause}"
        count_query += f" {where_clause}"
        params = count_params = [f"%{search_term}%"] * 6

    base_query += " LIMIT ? OFFSET ?"
    params.extend([per_page, offset])

    result_cursor = conn.execute(base_query, tuple(params))
    rows = result_cursor.fetchall()

    col_cursor = conn.execute("PRAGMA table_info('Verbs');")
    columns = [col[1] for col in col_cursor.fetchall()]

    verbs = [dict(zip(columns, row)) for row in rows]

    # Añadir columna de audio manualmente (ejemplo con naming convention)
    for verb in verbs:
        simple_form = verb["SIMPLE_FORM"].lower()
        verb["audio_url"] = (
            f"https://res.cloudinary.com/yorchwebs/video/upload/verbs/{simple_form}.mp3"
        )

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
