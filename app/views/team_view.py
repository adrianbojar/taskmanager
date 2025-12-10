from flask import Blueprint, request, redirect, render_template
from app.services.team_service import TeamService

team_bp = Blueprint("teams", __name__)
service = TeamService()

# CREATE
@team_bp.route("/teams/new", methods=["GET", "POST"])
def new_team():
    if request.method == "POST":
        name = request.form.get("name")
        description = request.form.get("description")
        service.create_team(name, description)
        return redirect("/teams")
    return render_template("teams/new.html")

# READ (list all teams)
@team_bp.route("/teams")
def view_teams():
    teams = service.get_all_teams()
    return render_template("teams/view.html", teams=teams)

# READ (single team detail)
@team_bp.route("/teams/<int:team_id>")
def view_team(team_id):
    team = service.get_team(team_id)
    return render_template("teams/detail.html", team=team)

# UPDATE
@team_bp.route("/teams/<int:team_id>/edit", methods=["GET", "POST"])
def edit_team(team_id):
    team = service.get_team(team_id)
    if request.method == "POST":
        name = request.form.get("name")
