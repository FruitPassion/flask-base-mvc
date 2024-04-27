from flask import Blueprint, render_template

auth = Blueprint("auth", __name__)


@auth.route("/")
def index():
    """
    This is the index page for the auth blueprint.
    """
    return render_template("auth/index.html")
