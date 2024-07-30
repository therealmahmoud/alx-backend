#!/usr/bin/env python3
"""Flask app."""
from flask import Flask, render_template
from flask_babel import Babel


app = Flask(__name__)
app.config['BABLE_DEFAULT_LOCALE'] = "en", "UTC"
Babel = Babel(app)


@app.route('/')
def index() -> str:
    """ Home route"""
    return render_template('0-index.html')


class Config:
    LANGUAGES = ["en", "fr"]


if __name__ == "__main__":
    app.run(debug=True)
