from flask import Blueprint, render_template, request, url_for, redirect, flash
from flask_login import login_required, current_user
from sqlalchemy import select

from watchlist.models import User, Movie
from watchlist.extensions import db

main_bp = Blueprint('main', __name__)


@main_bp.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        if not current_user.is_authenticated:
            return redirect(url_for('main.index'))

        title = request.form['title']
        year = request.form['year']

        if not title or not year or len(year) != 4 or len(title) > 60:
            flash('Invalid input.')
            return redirect(url_for('main.index'))

        movie = Movie(title=title, year=year)
        db.session.add(movie)
        db.session.commit()
        flash('Item created.')
        return redirect(url_for('main.index'))

    movies = db.session.execute(select(Movie)).scalars().all()
    return render_template('index.html', movies=movies)


@main_bp.route('/movie/edit/<int:movie_id>', methods=['GET', 'POST'])
@login_required
def edit(movie_id):
    movie = db.get_or_404(Movie, movie_id)

    if request.method == 'POST':
        title = request.form['title']
        year = request.form['year']

        if not title or not year or len(year) != 4 or len(title) > 60:
            flash('Invalid input.')
            return redirect(url_for('main.edit', movie_id=movie_id))

        movie.title = title
        movie.year = year
        db.session.commit()
        flash('Item updated.')
        return redirect(url_for('main.index'))

    return render_template('edit.html', movie=movie)


@main_bp.route('/movie/delete/<int:movie_id>', methods=['POST'])
@login_required
def delete(movie_id):
    movie = db.get_or_404(Movie, movie_id)
    db.session.delete(movie)
    db.session.commit()
    flash('Item deleted.')
    return redirect(url_for('main.index'))


@main_bp.route('/settings', methods=['GET', 'POST'])
@login_required
def settings():
    if request.method == 'POST':
        name = request.form['name']

        if not name or len(name) > 20:
            flash('Invalid input.')
            return redirect(url_for('main.settings'))

        user = db.session.get(User, current_user.id)
        user.name = name
        db.session.commit()
        flash('Settings updated.')
        return redirect(url_for('main.index'))

    return render_template('settings.html')
