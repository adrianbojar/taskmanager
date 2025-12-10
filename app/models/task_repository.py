from app.entities.models import Task
from db.database import SessionLocal

def create_task(task_data):
    db = SessionLocal()
    task = Task(**task_data)
    db.add(task)
    db.commit()
    db.refresh(task)
    return task

def get_task_by_id(task_id):
    db = SessionLocal()
    return db.query(Task).filter(Task.id == task_id).first()

def get_all_tasks():
    db = SessionLocal()
    return db.query(Task).all()

def update_task(task_id, new_data):
    db = SessionLocal()
    task = db.query(Task).filter(Task.id == task_id).first()
    for key, value in new_data.items():
        setattr(task, key, value)
    db.commit()
    return task

def delete_task(task_id):
    db = SessionLocal()
    task = db.query(Task).filter(Task.id == task_id).first()
    db.delete(task)
    db.commit()
