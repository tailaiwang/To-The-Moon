
from flask.helpers import url_for
from . import app
from flask import request
from werkzeug.urls import url_parse
from datetime import datetime

@app.route("/")
def index():
  return "hi"