from flask import Blueprint, request, redirect, render_template
from app.services.user_service import UserService

user_bp = Blueprint("user", __name__)
service = UserService()


@user_bp.route("/users")
def view_users():
    users = service.get_all_users()
    return render_template("users/view.html", users=users)


@user_bp.route("/users/new", methods=["GET", "POST"])
def new_user():
    if request.method == "POST":
        name = request.form.get("name")
        email = request.form.get("email")
        password = request.form.get("password")
        role = request.form.get("role", "member")

        service.create_user(name, email, password, role)
        return redirect("/users")

    return render_template("users/new.html")


@user_bp.route("/users/<int:user_id>/edit", methods=["GET", "POST"])
def edit_user(user_id):
    user = service.get_user(user_id)

    if request.method == "POST":
        name = request.form.get("name")
        email = request.form.get("email")
        password = request.form.get("password")
        role = request.form.get("role")

        service.update_user(user_id, name, email, password, role)
        return redirect("/users")

    return render_template("users/edit.html", user=user)


@user_bp.route("/users/<int:user_id>/delete", methods=["POST"])
def delete_user(user_id):
    service.delete_user(user_id)
    return redirect("/users")