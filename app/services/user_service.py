from app.entities.models import User
from config.database import SessionLocal
from werkzeug.security import generate_password_hash


class UserService:

    def __init__(self):
        self.db = SessionLocal

    def get_all_users(self):
        session = self.db()
        users = session.query(User).all()
        session.close()
        return users

    def get_user(self, user_id):
        session = self.db()
        user = session.query(User).filter(User.id == user_id).first()
        session.close()
        return user

    def create_user(self, name, email, password, role):
        session = self.db()
        user = User(
            name=name,
            email=email,
            password_hash=generate_password_hash(password),
            role=role
        )
        session.add(user)
        session.commit()
        session.close()
        return user

    def update_user(self, user_id, name, email, password, role):
        session = self.db()
        user = session.query(User).filter(User.id == user_id).first()

        if user:
            user.name = name
            user.email = email
            if password:
                user.password_hash = generate_password_hash(password)
            user.role = role
            session.commit()

        session.close()
        return user

    def delete_user(self, user_id):
        session = self.db()
        user = session.query(User).filter(User.id == user_id).first()

        if user:
            session.delete(user)
            session.commit()

        session.close()