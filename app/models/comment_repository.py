from app.entities.models import Comment
from db.database import SessionLocal

def create_comment(comment_data):
    db = SessionLocal()
    comment = Comment(**comment_data)
    db.add(comment)
    db.commit()
    db.refresh(comment)
    return comment

def get_comment_by_id(comment_id):
    db = SessionLocal()
    return db.query(Comment).filter(Comment.id == comment_id).first()

def get_all_comments():
    db = SessionLocal()
    return db.query(Comment).all()

def update_comment(comment_id, new_data):
    db = SessionLocal()
    comment = db.query(Comment).filter(Comment.id == comment_id).first()
    for key, value in new_data.items():
        setattr(comment, key, value)
    db.commit()
    return comment

def delete_comment(comment_id):
    db = SessionLocal()
    comment = db.query(Comment).filter(Comment.id == comment_id).first()
    db.delete(comment)
    db.commit()
