from flask import render_template
from app import app, db


@app.errorhandler(404)
def not_found_error(error):
    """
    The 404 error page will show the 404.html page instead of the standard page.
    """
    return render_template('404.html'), 404


@app.errorhandler(500)
def internal_error(error):
    """
    The 500 error page will show the 404.html page instead of the standard page.
    """
    db.session.rollback()
    return render_template('500.html'), 500

