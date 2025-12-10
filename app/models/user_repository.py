from app.entities.models import User
from db.database import SessionLocal


def create_user(user_data):
    db = SessionLocal()
    user = User(**user_data)
    db.add(user)
    db.commit()
    db.refresh(user)
    return user

def get_user_by_id(user_id):
    db = SessionLocal()
    return db.query(User).filter(User.id == user_id).first()

def get_all_users():
    db = SessionLocal()
    return db.query(User).all()

def update_user(user_id, new_data):
    db = SessionLocal()
    user = db.query(User).filter(User.id == user_id).first()
    for key, value in new_data.items():
        setattr(user, key, value)
    db.commit()
    return user

def delete_user(user_id):
    db = SessionLocal()
    user = db.query(User).filter(User.id == user_id).first()
    db.delete(user)
    db.commit()
