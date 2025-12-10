from flask import Blueprint, request, redirect, render_template
from app.services.comment_service import CommentService

comment_bp = Blueprint("comments", __name__)
service = CommentService()

# CREATE
@comment_bp.route("/comments/new", methods=["GET", "POST"])
def new_comment():
    if request.method == "POST":
        content = request.form.get("content")
        author_id = int(request.form.get("author_id"))
        task_id = int(request.form.get("task_id"))
        service.create_comment(content, author_id, task_id)
        return redirect("/comments")
    return render_template("comments/new.html")

# READ (list all comments)
@comment_bp.route("/comments")
def view_comments():
    comments = service.get_all_comments()
    return render_template("comments/view.html", comments=comments)

# READ (single comment detail)
@comment_bp.route("/comments/<int:comment_id>")
def view_comment(comment_id):
    comment = service.get_comment(comment_id)
    return render_template("comments/detail.html", comment=comment)

# UPDATE
@comment_bp.route("/comments/<int:comment_id>/edit", methods=["GET", "POST"])
def edit_comment(comment_id):
    comment = service.get_comment(comment_id)
    if request.method == "POST":
        content = request.form.get("content")
        author_id = int(request.form.get("author_id"))
        task_id = int(request.form.get("task_id"))
        service.update_comment(comment_id, content, author_id, task_id)
        return redirect("/comments")
    return render_template("comments/edit.html", comment=comment)

# DELETE
@comment_bp.route("/comments/<int:comment_id>/delete", methods=["POST"])
def delete_comment(comment_id):
    service.delete_comment(comment_id)
    return redirect("/comments")
