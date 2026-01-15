from datetime import datetime
from app.extensions import db


class Note(db.Model):
    # tabela notatek
    __tablename__ = "notes"

    # podstawowe dane notatki
    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.String(500), nullable=False)

    # kategoria i status wykonania
    category = db.Column(db.String(20), nullable=False, default="Praca")
    is_done = db.Column(db.Boolean, nullable=False, default=False)

    # daty utworzenia i edycji
    created_at = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, nullable=False, default=datetime.utcnow, onupdate=datetime.utcnow)

    # odbiorca notatki (kto ją widzi)
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"), nullable=False)
    owner = db.relationship("User", back_populates="notes", foreign_keys=[user_id])

    # autor notatki (kto ją napisał)
    author_id = db.Column(db.Integer, db.ForeignKey("users.id"), nullable=False)
    author = db.relationship("User", foreign_keys=[author_id])

    def __repr__(self) -> str:
        return f"<Note {self.id}>"