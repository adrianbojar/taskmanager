from flask import Blueprint, request, redirect, render_template
from app.services.project_service import ProjectService

project_bp = Blueprint("projects", __name__)
service = ProjectService()

# CREATE
@project_bp.route("/projects/new", methods=["GET", "POST"])
def new_project():
    if request.method == "POST":
        name = request.form.get("name")
        description = request.form.get("description")
        team_id = int(request.form.get("team_id"))

        service.create_project(name, description, team_id)
        return redirect("/projects")
    return render_template("projects/new.html")

# READ (list all projects)
@project_bp.route("/projects")
def view_projects():
    projects = service.get_all_projects()
    return render_template("projects/view.html", projects=projects)

# READ (single project detail)
@project_bp.route("/projects/<int:project_id>")
def view_project(project_id):
    project = service.get_project(project_id)
    return render_template("projects/detail.html", project=project)

# UPDATE
@project_bp.route("/projects/<int:project_id>/edit", methods=["GET", "POST"])
def edit_project(project_id):
    project = service.get_project(project_id)
    if request.method == "POST":
        name = request.form.get("name")
        description = request.form.get("description")
        team_id = int(request.form.get("team_id"))

        service.update_project(project_id, name, description, team_id)
        return redirect("/projects")
    return render_template("projects/edit.html", project=project)

# DELETE
@project_bp.route("/projects/<int:project_id>/delete", methods=["POST"])
def delete_project(project_id):
    service.delete_project(project_id)
    return redirect("/projects")
