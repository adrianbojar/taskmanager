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
    # pobranie wszystkich notatek użytkownika
    notes = Note.query.filter_by(user_id=current_user.id).all()

    return render_template(
        "dashboard.html",
        user=current_user,
        notes=notes
    )