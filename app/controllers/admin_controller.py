from flask import Blueprint, render_template, redirect, url_for, flash, request
from flask_login import login_required, current_user

from app.extensions import db
from app.models.user import User
from app.utils import admin_required

admin_bp = Blueprint("admin", __name__, url_prefix="/admin")


@admin_bp.route("/")
@login_required
@admin_required
def panel():
    users = User.query.order_by(User.id.asc()).all()
    return render_template("admin.html", users=users)


@admin_bp.route("/role", methods=["POST"])
@login_required
@admin_required
def change_role():
    user_id = int(request.form.get("user_id", "0"))
    new_role = request.form.get("role", "user")

    if new_role not in ("user", "admin"):
        flash("Nieprawidłowa rola.", "error")
        return redirect(url_for("admin.panel"))

    user = User.query.get_or_404(user_id)

    if user.id == current_user.id:
        flash("Nie możesz zmienić roli samemu sobie.", "error")
        return redirect(url_for("admin.panel"))

    user.role = new_role
    db.session.commit()

    flash("Zmieniono rolę.", "success")
    return redirect(url_for("admin.panel"))


@admin_bp.route("/delete", methods=["POST"])
@login_required
@admin_required
def delete_user():
    user_id = int(request.form.get("user_id", "0"))
    user = User.query.get_or_404(user_id)

    if user.id == current_user.id:
        flash("Nie możesz usunąć samego siebie.", "error")
        return redirect(url_for("admin.panel"))

    db.session.delete(user)
    db.session.commit()

    flash("Usunięto użytkownika.", "success")
    return redirect(url_for("admin.panel"))