from flask import Blueprint, request, redirect, render_template
from app.services.task_service import TaskService

task_bp = Blueprint("tasks", __name__)
service = TaskService()

# CREATE
@task_bp.route("/tasks/new", methods=["GET", "POST"])
def new_task():
    if request.method == "POST":
        title = request.form.get("title")
        description = request.form.get("description")
        project_id = int(request.form.get("project_id"))
        assignee_id = int(request.form.get("assignee_id"))

        service.create_task(title, description, project_id, assignee_id)
        return redirect("/tasks")
    return render_template("tasks/new.html")

# READ (list all tasks)
@task_bp.route("/tasks")
def view_tasks():
    tasks = service.get_all_tasks()
    return render_template("tasks/view.html", tasks=tasks)

# READ (single task detail)
@task_bp.route("/tasks/<int:task_id>")
def view_task(task_id):
    task = service.get_task(task_id)
    return render_template("tasks/detail.html", task=task)

# UPDATE
@task_bp.route("/tasks/<int:task_id>/edit", methods=["GET", "POST"])
def edit_task(task_id):
    task = service.get_task(task_id)
    if request.method == "POST":
        title = request.form.get("title")
        description = request.form.get("description")
        project_id = int(request.form.get("project_id"))
        assignee_id = int(request.form.get("assignee_id"))

        service.update_task(task_id, title, description, project_id, assignee_id)
        return redirect("/tasks")
    return render_template("tasks/edit.html", task=task)

# DELETE
@task_bp.route("/tasks/<int:task_id>/delete", methods=["POST"])
def delete_task(task_id):
    service.delete_task(task_id)
    return redirect("/tasks")
