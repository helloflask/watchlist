from flask import Blueprint, render_template, request, redirect, url_for, flash
from flask_login import login_user, login_required, logout_user
from sqlalchemy import select

from watchlist.models import User
from watchlist.extensions import db

auth_bp = Blueprint('auth', __name__)


@auth_bp.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        if not username or not password:
            flash('Invalid input.')
            return redirect(url_for('auth.login'))

        user = db.session.execute(select(User).filter_by(username=username)).scalar()

        if user is not None and user.validate_password(password):
            login_user(user)
            flash('Login success.')
            return redirect(url_for('main.index'))

        flash('Invalid username or password.')
        return redirect(url_for('auth.login'))

    return render_template('login.html')


@auth_bp.route('/logout')
@login_required
def logout():
    logout_user()
    flash('Goodbye.')
    return redirect(url_for('main.index'))
