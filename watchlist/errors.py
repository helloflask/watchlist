from flask import render_template


def register_errors(app):

    @app.errorhandler(400)
    def bad_request(error):
        return render_template('errors/400.html'), 400


    @app.errorhandler(404)
    def page_not_found(error):
        return render_template('errors/404.html'), 404


    @app.errorhandler(500)
    def internal_server_error(error):
        return render_template('errors/500.html'), 500
