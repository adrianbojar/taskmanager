from flask_login import UserMixin
from app.extensions import db

class User(db.Model, UserMixin):
    # tabela użytkowników
    __tablename__ = "users"
    # podstawowe dane użytkownika
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password_hash = db.Column(db.String(255), nullable=False)
    role = db.Column(db.String(20), nullable=False, default="user")
    # notatki, które użytkownik widzi na swoim koncie
    notes = db.relationship(
        "Note",
        back_populates="owner",
        cascade="all, delete-orphan",
        foreign_keys="Note.user_id",
    )
    # sprawdzenie czy użytkownik jest adminem
    @property
    def is_admin(self) -> bool:
        return self.role == "admin"
    def __repr__(self) -> str:
        return f"<User {self.email}>"