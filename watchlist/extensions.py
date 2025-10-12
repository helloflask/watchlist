from flask_login import LoginManager
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase


class Base(DeclarativeBase):
  pass


db = SQLAlchemy(model_class=Base)
login_manager = LoginManager()


@login_manager.user_loader
def load_user(user_id):
    from watchlist.models import User
    user = db.session.get(User, int(user_id))
    return user


login_manager.login_view = 'login'
# login_manager.login_message = 'Your custom message'
