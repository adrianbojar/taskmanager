from app.models import comment_repository

class CommentService:
    def get_all_comments(self):
        return comment_repository.get_all_comments()

    def get_comment(self, comment_id):
        return comment_repository.get_comment_by_id(comment_id)

    def create_comment(self, content, author_id, task_id):
        comment_data = {"content": content, "author_id": author_id, "task_id": task_id}
        return comment_repository.create_comment(comment_data)

    def update_comment(self, comment_id, content, author_id, task_id):
        new_data = {"content": content, "author_id": author_id, "task_id": task_id}
        return comment_repository.update_comment(comment_id, new_data)

    def delete_comment(self, comment_id):
        return comment_repository.delete_comment(comment_id)
