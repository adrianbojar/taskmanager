# SQLAlchemy engine and session setup
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
from app.entities.models import Base
import os

# Ścieżka do pliku bazy danych SQLite
DB_PATH = os.path.join(os.path.dirname(__file__), "..", "db/task_manager.db")

# URI połączenia SQLite
DATABASE_URL = f"sqlite:///{DB_PATH}"

# Tworzenie silnika bazy danych
engine = create_engine(
    DATABASE_URL,
    connect_args={"check_same_thread": False},  # wymagane dla SQLite w aplikacjach wielowątkowych
    echo=False  # ustaw True, jeśli chcesz logować SQL w konsoli
)

# Fabryka sesji
SessionLocal = scoped_session(
    sessionmaker(autocommit=False, autoflush=False, bind=engine)
)

def init_db():
    """
    Tworzy wszystkie tabele w bazie, jeśli jeszcze nie istnieją.
    """
    Base.metadata.create_all(bind=engine)
