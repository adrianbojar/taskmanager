from config.database import init_db, SessionLocal
from flask import Flask
from app.controllers.user_controller import user_bp
from config.database import init_db
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

app = Flask(
    __name__,
    template_folder=os.path.join("app", "views")
)

# rejestracja kontrolerów
app.register_blueprint(user_bp)

def main():
    # Inicjalizacja bazy danych
    init_db()

    # Test: otwórz sesję
    db = SessionLocal()
    print("Połączono z bazą SQLite!")
    db.close()

@app.route("/")
def index():
    return "<h1>Task Manager działa!</h1><a href='/users'>Przejdź do użytkowników</a>"

if __name__ == "__main__":
    init_db()
    app.run(debug=True)
