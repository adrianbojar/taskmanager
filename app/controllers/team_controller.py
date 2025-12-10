from flask import Blueprint, request, redirect, render_template
from app.services.team_service import TeamService

team_bp = Blueprint("teams", __name__)
service = TeamService()

@team_bp.route("/teams")
def view_teams():
    teams = service.get_all_teams()
    return render_template("teams/view.html", teams=teams)

@team_bp.route("/teams/new", methods=["GET", "POST"])
def new_team():
    if request.method == "POST":
        name = request.form.get("name")
        description = request.form.get("description")

        service.create_team(name, description)
        return redirect("/teams")

    return render_template("teams/new.html")

@team_bp.route("/teams/<int:team_id>/edit", methods=["GET", "POST"])
def edit_team(team_id):
    team = service.get_team(team_id)

    if request.method == "POST":
        name = request.form.get("name")
        description = request.form.get("description")

        service.update_team(team_id, name, description)
        return redirect("/teams")

    return render_template("teams/edit.html", team=team)

@team_bp.route("/teams/<int:team_id>/delete", methods=["POST"])
def delete_team(team_id):
    service.delete_team(team_id)
    return redirect("/teams")
