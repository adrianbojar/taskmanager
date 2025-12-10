from app.entities.models import Project
from db.database import SessionLocal

def create_project(project_data):
    db = SessionLocal()
    project = Project(**project_data)
    db.add(project)
    db.commit()
    db.refresh(project)
    return project

def get_project_by_id(project_id):
    db = SessionLocal()
    return db.query(Project).filter(Project.id == project_id).first()

def get_all_projects():
    db = SessionLocal()
    return db.query(Project).all()

def update_project(project_id, new_data):
    db = SessionLocal()
    project = db.query(Project).filter(Project.id == project_id).first()
    for key, value in new_data.items():
        setattr(project, key, value)
    db.commit()
    return project

def delete_project(project_id):
    db = SessionLocal()
    project = db.query(Project).filter(Project.id == project_id).first()
    db.delete(project)
    db.commit()
