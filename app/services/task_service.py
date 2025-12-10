from app.models import task_repository

class TaskService:
    def get_all_tasks(self):
        return task_repository.get_all_tasks()

    def get_task(self, task_id):
        return task_repository.get_task_by_id(task_id)

    def create_task(self, title, description, status, creator_id, assignee_id):
        task_data = {
            "title": title,
            "description": description,
            "status": status,
            "creator_id": creator_id,
            "assignee_id": assignee_id
        }
        return task_repository.create_task(task_data)

    def update_task(self, task_id, title, description, status, creator_id, assignee_id):
        new_data = {
            "title": title,
            "description": description,
            "status": status,
            "creator_id": creator_id,
            "assignee_id": assignee_id
        }
        return task_repository.update_task(task_id, new_data)

    def delete_task(self, task_id):
        return task_repository.delete_task(task_id)
