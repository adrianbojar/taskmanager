import os
from flask import Flask
from config import Config
from app.extensions import db, login_manager

def create_app():
    base_dir = os.path.dirname(os.path.abspath(__file__))  # .../my_flask_mvc_app/app
    templates_dir = os.path.join(base_dir, "views", "templates")
    static_dir = os.path.join(base_dir, "views", "static")

    app = Flask(
        __name__,
        template_folder=templates_dir,
        static_folder=static_dir,
        static_url_path="/static",
    )
    app.config.from_object(Config)

    db.init_app(app)
    login_manager.init_app(app)

    # user_loader
    from app.models.user import User
    @login_manager.user_loader
    def load_user(user_id: str):
        return db.session.get(User, int(user_id))

    # blueprinty
    from app.controllers.main_controller import main_bp
    from app.controllers.auth_controller import auth_bp
    from app.controllers.notes_controller import notes_bp
    from app.controllers.admin_controller import admin_bp

    app.register_blueprint(main_bp)
    app.register_blueprint(auth_bp)
    app.register_blueprint(notes_bp)
    app.register_blueprint(admin_bp)

    with app.app_context():
        db.create_all()

        # admin autoutworzenie (jeśli już masz, nic nie popsuje)
        from werkzeug.security import generate_password_hash
        admin_email = "admin@local"
        admin = User.query.filter_by(email=admin_email).first()
        if not admin:
            admin = User(email=admin_email, password_hash=generate_password_hash("admin123"), role="admin")
            db.session.add(admin)
            db.session.commit()

    return app