from collections import defaultdict

from flask import Blueprint, render_template
from flask_login import login_required, current_user

from app.models.note import Note

main_bp = Blueprint("main", __name__)


@main_bp.route("/")
def index():
    return render_template("index.html")


@main_bp.route("/dashboard")
@login_required
def dashboard():
    # sort: niewykonane na górze, potem najnowsze zmiany
    notes = (
        Note.query
        .filter_by(user_id=current_user.id)
        .order_by(Note.is_done.asc(), Note.updated_at.desc())
        .all()
    )

    grouped_notes = defaultdict(list)
    for n in notes:
        grouped_notes[n.category].append(n)

    # zawsze pokaż 3 kolumny
    for cat in ["Praca", "Dom", "Studia"]:
        grouped_notes.setdefault(cat, [])

    return render_template(
        "dashboard.html",
        user=current_user,
        grouped_notes=grouped_notes
    )