from flask import Blueprint, redirect, request, url_for, flash, render_template
from flask_login import login_required, current_user

from app.extensions import db
from app.models.note import Note

notes_bp = Blueprint("notes", __name__)

ALLOWED_CATEGORIES = {"Praca", "Dom", "Studia"}
MAX_LEN = 500


def _get_category(value: str) -> str:
    value = (value or "").strip()
    return value if value in ALLOWED_CATEGORIES else "Dom"


@notes_bp.route("/notes/add", methods=["POST"])
@login_required
def add_note():
    content = (request.form.get("content") or "").strip()
    category = _get_category(request.form.get("category"))

    if not content:
        flash("Treść notatki nie może być pusta.", "error")
        return redirect(url_for("main.dashboard"))

    if len(content) > MAX_LEN:
        flash(f"Notatka jest za długa (max {MAX_LEN} znaków).", "error")
        return redirect(url_for("main.dashboard"))

    note = Note(content=content, category=category, user_id=current_user.id)
    db.session.add(note)
    db.session.commit()

    flash("Dodano notatkę.", "success")
    return redirect(url_for("main.dashboard"))


@notes_bp.route("/notes/<int:note_id>/delete", methods=["POST"])
@login_required
def delete_note(note_id: int):
    note = Note.query.get_or_404(note_id)

    if note.user_id != current_user.id:
        flash("Nie masz uprawnień do usunięcia tej notatki.", "error")
        return redirect(url_for("main.dashboard"))

    db.session.delete(note)
    db.session.commit()

    flash("Usunięto notatkę.", "success")
    return redirect(url_for("main.dashboard"))


@notes_bp.route("/notes/<int:note_id>/toggle", methods=["POST"])
@login_required
def toggle_done(note_id: int):
    note = Note.query.get_or_404(note_id)

    if note.user_id != current_user.id:
        flash("Nie masz uprawnień do tej operacji.", "error")
        return redirect(url_for("main.dashboard"))

    note.is_done = not note.is_done
    db.session.commit()
    return redirect(url_for("main.dashboard"))


@notes_bp.route("/notes/<int:note_id>/edit", methods=["GET", "POST"])
@login_required
def edit_note(note_id: int):
    note = Note.query.get_or_404(note_id)

    if note.user_id != current_user.id:
        flash("Nie masz uprawnień do edycji tej notatki.", "error")
        return redirect(url_for("main.dashboard"))

    if request.method == "POST":
        content = (request.form.get("content") or "").strip()
        category = _get_category(request.form.get("category"))
        is_done = request.form.get("is_done") == "on"

        if not content:
            flash("Treść notatki nie może być pusta.", "error")
            return redirect(url_for("notes.edit_note", note_id=note.id))

        if len(content) > MAX_LEN:
            flash(f"Notatka jest za długa (max {MAX_LEN} znaków).", "error")
            return redirect(url_for("notes.edit_note", note_id=note.id))

        note.content = content
        note.category = category
        note.is_done = is_done
        db.session.commit()

        flash("Zapisano zmiany.", "success")
        return redirect(url_for("main.dashboard"))

    return render_template("edit_note.html", note=note, categories=sorted(ALLOWED_CATEGORIES))