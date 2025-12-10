from flask import Blueprint, request, redirect, render_template
from app.services.user_service import UserService

user_bp = Blueprint("users", __name__)
service = UserService()

# CREATE
@user_bp.route("/users/new", methods=["GET", "POST"])
def new_user():
    if request.method == "POST":
        username = request.form.get("username")
        email = request.form.get("email")
        service.create_user(username, email)
        return redirect("/users")
    return render_template("users/new.html")

# READ (list all users)
@user_bp.route("/users")
def view_users():
    users = service.get_all_users()
    return render_template("users/view.html", users=users)

# READ (single user detail)
@user_bp.route("/users/<int:user_id>")
def view_user(user_id):
    user = service.get_user(user_id)
    return render_template("users/detail.html", user=user)

# UPDATE
@user_bp.route("/users/<int:user_id>/edit", methods=["GET", "POST"])
def edit_user(user_id):
    user = service.get_user(user_id)
    if request.method == "POST":
        username = request.form.get("username")
        email = request.form.get("email")
        service.update_user(user_id, username, email)
        return redirect("/users")
    return render_template("users/edit.html", user=user)

# DELETE
@user_bp.route("/users/<int:user_id>/delete", methods=["POST"])
def delete_user(user_id):
    service.delete_user(user_id)
    return redirect("/users")
