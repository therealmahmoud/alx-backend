#!/usr/bin/env python3
"""Flask app."""
from flask_babel import Babel
from flask import Flask, render_template, request, g
from typing import Union, Dict
import pytz


class Config:
    """ Flask babel config."""
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app = Flask(__name__)
app.config.from_object(Config)
babel = Babel(app)
users = {
    1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
    2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
    3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
    4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
}


def get_user() -> Union[Dict, None]:
    """ Gets user based on id."""
    user_id = users.keys()
    if user_id in users:
        return user_id
    return None


@app.before_request
def before_request() -> None:
    """ Getting user before any request."""
    user = get_user()
    g.user = user


@babel.localeselector
def get_locale() -> str:
    """Retrieves the locale for a web page."""
    locale = request.args.get('locale', '')
    if locale in app.config["LANGUAGES"]:
        return locale
    return request.accept_languages.best_match([Config.LANGUAGES])


@babel.timezoneselector
def get_timezone() -> str:
    """Retrieves the TimeZone."""
    timezone = request.args.get('timezone', '').strip()
    if not timezone and g.user:
        timezone = g.user['timezone']
    try:
        return pytz.timezone(timezone).zone
    except pytz.exceptions.UnknownTimeZoneError:
        return Config.BABEL_DEFAULT_TIMEZONE


@app.route('/')
def index() -> str:
    """ Home route"""
    return render_template('5-index.html')


if __name__ == "__main__":
    app.run(debug=True)
