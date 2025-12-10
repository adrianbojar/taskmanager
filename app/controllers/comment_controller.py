from flask import Blueprint, request, redirect, render_template
from app.services.comment_service import CommentService

comment_bp = Blueprint("comments", __name__)
service = CommentService()

@comment_bp.route("/comments")
def view_comments():
    comments = service.get_all_comments()
    return render_template("comments/view.html", comments=comments)

@comment_bp.route("/comments/new", methods=["GET", "POST"])
def new_comment():
    if request.method == "POST":
        content = request.form.get("content")
        author_id = int(request.form.get("author_id"))
        task_id = int(request.form.get("task_id"))

        service.create_comment(content, author_id, task_id)
        return redirect("/comments")

    return render_template("comments/new.html")

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

@comment_bp.route("/comments/<int:comment_id>/delete", methods=["POST"])
def delete_comment(comment_id):
    service.delete_comment(comment_id)
    return redirect("/comments")

print()