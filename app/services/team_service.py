from app.models import team_repository

class TeamService:
    def get_all_teams(self):
        return team_repository.get_all_teams()

    def get_team(self, team_id):
        return team_repository.get_team_by_id(team_id)

    def create_team(self, name, description):
        team_data = {"name": name, "description": description}
        return team_repository.create_team(team_data)

    def update_team(self, team_id, name, description):
        new_data = {"name": name, "description": description}
        return team_repository.update_team(team_id, new_data)

    def delete_team(self, team_id):
        return team_repository.delete_team(team_id)
