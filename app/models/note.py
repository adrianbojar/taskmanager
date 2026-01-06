from datetime import datetime
from app.extensions import db

class Note(db.Model):
    __tablename__ = "notes"

    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.String(500), nullable=False)

    # NOWE
    category = db.Column(db.String(20), nullable=False, default="Dom")   # Praca/Dom/Studia
    is_done = db.Column(db.Boolean, nullable=False, default=False)

    created_at = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, nullable=False, default=datetime.utcnow, onupdate=datetime.utcnow)

    user_id = db.Column(db.Integer, db.ForeignKey("users.id"), nullable=False)
    owner = db.relationship("User", back_populates="notes")

    def __repr__(self) -> str:
        return f"<Note {self.id}>"
