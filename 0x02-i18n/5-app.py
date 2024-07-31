#!/usr/bin/env python3
"""Flask app."""
from flask_babel import Babel
from flask import Flask, render_template, request, g
from typing import Union, Dict


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
    user_id = users.keys()
    if user_id in users:
        return user_id
    return None


@app.before_request
def before_request() -> None:
    user = get_user()
    g.user = user


@babel.localeselector
def get_locale():
    """ Returns the locale of the web page."""
    queries = request.query_string.decode('utf-8').split('&')
    query_table = dict(map(
        lambda x: (x if '=' in x else '{}='.format(x)).split('='),
        queries,
    ))
    if 'locale' in query_table:
        if query_table['locale'] in app.config["LANGUAGES"]:
            return query_table['locale']
    return request.accept_languages.best_match([Config.LANGUAGES])


@app.route('/')
def index() -> str:
    """ Home route"""
    return render_template('3-index.html')


if __name__ == "__main__":
    app.run(debug=True)
