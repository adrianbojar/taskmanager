from flask import Blueprint, request, redirect, render_template
from app.services.project_service import ProjectService

project_bp = Blueprint("projects", __name__)
service = ProjectService()

@project_bp.route("/projects")
def view_projects():
    projects = service.get_all_projects()
    return render_template("projects/view.html", projects=projects)

@project_bp.route("/projects/new", methods=["GET", "POST"])
def new_project():
    if request.method == "POST":
        name = request.form.get("name")
        description = request.form.get("description")
        owner_id = int(request.form.get("owner_id"))

        service.create_project(name, description, owner_id)
        return redirect("/projects")

    return render_template("projects/new.html")

@project_bp.route("/projects/<int:project_id>/edit", methods=["GET", "POST"])
def edit_project(project_id):
    project = service.get_project(project_id)

    if request.method == "POST":
        name = request.form.get("name")
        description = request.form.get("description")
        owner_id = int(request.form.get("owner_id"))

        service.update_project(project_id, name, description, owner_id)
        return redirect("/projects")

    return render_template("projects/edit.html", project=project)

@project_bp.route("/projects/<int:project_id>/delete", methods=["POST"])
def delete_project(project_id):
    service.delete_project(project_id)
    return redirect("/projects")
