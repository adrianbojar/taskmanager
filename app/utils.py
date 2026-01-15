from functools import wraps
from flask import redirect, url_for, flash
from flask_login import current_user

def admin_required(view_func):
    # dekorator zabezpieczający widoki tylko dla admina
    @wraps(view_func)
    def wrapper(*args, **kwargs):
        if not current_user.is_authenticated:
            flash("Musisz się zalogować.", "error")
            return redirect(url_for("auth.login"))
        if not current_user.is_admin:
            flash("Brak uprawnień (tylko admin).", "error")
            return redirect(url_for("main.dashboard"))
        return view_func(*args, **kwargs)
    return wrapper