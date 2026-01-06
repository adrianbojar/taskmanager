from functools import wraps
from flask import redirect, url_for, flash
from flask_login import current_user

def admin_required(view_func):
    @wraps(view_func)
    def wrapper(*args, **kwargs):
        if not current_user.is_authenticated or current_user.role != "admin":
            flash("Brak uprawnień (tylko admin).", "error")
            return redirect(url_for("main.index"))
        return view_func(*args, **kwargs)
    return wrapper