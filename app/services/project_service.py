from app.models import project_repository

class ProjectService:
    def get_all_projects(self):
        return project_repository.get_all_projects()

    def get_project(self, project_id):
        return project_repository.get_project_by_id(project_id)

    def create_project(self, name, description, owner_id):
        project_data = {"name": name, "description": description, "owner_id": owner_id}
        return project_repository.create_project(project_data)

    def update_project(self, project_id, name, description, owner_id):
        new_data = {"name": name, "description": description, "owner_id": owner_id}
        return project_repository.update_project(project_id, new_data)

    def delete_project(self, project_id):
        return project_repository.delete_project(project_id)
