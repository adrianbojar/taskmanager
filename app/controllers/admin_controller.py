from flask import Blueprint, render_template, redirect, request, url_for, flash
from flask_login import login_required, current_user

from app.extensions import db
from app.models.user import User
from app.models.note import Note
from app.utils import admin_required


admin_bp = Blueprint("admin", __name__)

# dozwolone role
ALLOWED_ROLES = {"user", "admin"}

# dozwolone kategorie (bez DOM)
ALLOWED_CATEGORIES = {"Praca", "Studia"}

# limit długości notatki
MAX_NOTE_LEN = 500


def _get_role(value: str) -> str:
    # sprawdzenie czy rola jest poprawna
    value = (value or "").strip()
    return value if value in ALLOWED_ROLES else "user"


def _get_category(value: str) -> str:
    # sprawdzenie czy kategoria jest poprawna
    value = (value or "").strip()
    return value if value in ALLOWED_CATEGORIES else "Praca"


def _admins_count() -> int:
    # policz ilu jest adminów
    return User.query.filter_by(role="admin").count()


@admin_bp.route("/admin")
@login_required
@admin_required
def panel():
    # panel admina: użytkownicy i wszystkie notatki
    users = User.query.order_by(User.id.desc()).all()
    notes = Note.query.order_by(Note.id.desc()).all()

    return render_template(
        "admin.html",
        users=users,
        notes=notes,
        categories=["Praca", "Studia"],
    )


@admin_bp.route("/admin/change-role", methods=["POST"])
@login_required
@admin_required
def change_role():
    # zmiana roli użytkownika
    user_id = request.form.get("user_id", type=int)
    new_role = _get_role(request.form.get("role"))

    target = User.query.get(user_id)
    if not target:
        flash("Nie znaleziono użytkownika.", "error")
        return redirect(url_for("admin.panel"))

    if target.id == current_user.id:
        flash("Nie możesz zmieniać swojej roli.", "error")
        return redirect(url_for("admin.panel"))

    if target.role == "admin" and new_role != "admin":
        if _admins_count() <= 1:
            flash("Nie możesz odebrać roli ostatniemu adminowi.", "error")
            return redirect(url_for("admin.panel"))

    target.role = new_role
    db.session.commit()

    flash("Zmieniono rolę użytkownika.", "success")
    return redirect(url_for("admin.panel"))


@admin_bp.route("/admin/delete-user", methods=["POST"])
@login_required
@admin_required
def delete_user():
    # usuwanie użytkownika
    user_id = request.form.get("user_id", type=int)

    target = User.query.get(user_id)
    if not target:
        flash("Nie znaleziono użytkownika.", "error")
        return redirect(url_for("admin.panel"))

    if target.id == current_user.id:
        flash("Nie możesz usunąć siebie.", "error")
        return redirect(url_for("admin.panel"))

    if target.role == "admin" and _admins_count() <= 1:
        flash("Nie możesz usunąć ostatniego admina.", "error")
        return redirect(url_for("admin.panel"))

    db.session.delete(target)
    db.session.commit()

    flash("Usunięto użytkownika.", "success")
    return redirect(url_for("admin.panel"))


@admin_bp.route("/admin/notes/send", methods=["POST"])
@login_required
@admin_required
def send_note_to_user():
    # admin wysyła notatkę do użytkownika
    user_id = request.form.get("user_id", type=int)
    content = (request.form.get("content") or "").strip()
    category = _get_category(request.form.get("category"))

    target = User.query.get(user_id)
    if not target:
        flash("Nie znaleziono użytkownika.", "error")
        return redirect(url_for("admin.panel"))

    if not content:
        flash("Treść notatki nie może być pusta.", "error")
        return redirect(url_for("admin.panel"))

    if len(content) > MAX_NOTE_LEN:
        flash("Notatka jest za długa.", "error")
        return redirect(url_for("admin.panel"))

    note = Note(
        content=content,
        category=category,
        is_done=False,
        user_id=target.id,
        author_id=current_user.id,
    )

    db.session.add(note)
    db.session.commit()

    flash(f"Wysłano notatkę do {target.email}.", "success")
    return redirect(url_for("admin.panel"))


@admin_bp.route("/admin/notes/<int:note_id>/toggle", methods=["POST"])
@login_required
@admin_required
def toggle_note(note_id: int):
    # admin zmienia status wykonania notatki
    note = Note.query.get_or_404(note_id)
    note.is_done = not note.is_done
    db.session.commit()
    return redirect(url_for("admin.panel"))


@admin_bp.route("/admin/notes/<int:note_id>/delete", methods=["POST"])
@login_required
@admin_required
def delete_note(note_id: int):
    # admin usuwa notatkę
    note = Note.query.get_or_404(note_id)
    db.session.delete(note)
    db.session.commit()
    flash("Usunięto notatkę.", "success")
    return redirect(url_for("admin.panel"))


@admin_bp.route("/admin/notes/<int:note_id>/edit", methods=["GET", "POST"])
@login_required
@admin_required
def edit_note(note_id: int):
    # admin edytuje notatkę
    note = Note.query.get_or_404(note_id)

    if request.method == "POST":
        content = (request.form.get("content") or "").strip()
        category = _get_category(request.form.get("category"))
        is_done = request.form.get("is_done") == "on"

        if not content:
            flash("Treść nie może być pusta.", "error")
            return redirect(url_for("admin.edit_note", note_id=note.id))

        if len(content) > MAX_NOTE_LEN:
            flash("Notatka jest za długa.", "error")
            return redirect(url_for("admin.edit_note", note_id=note.id))

        note.content = content
        note.category = category
        note.is_done = is_done
        db.session.commit()

        flash("Zapisano zmiany.", "success")
        return redirect(url_for("admin.panel"))

    return render_template(
        "admin_edit_note.html",
        note=note,
        categories=["Praca", "Studia"],
    )