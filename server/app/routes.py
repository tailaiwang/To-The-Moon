
from flask.helpers import url_for
from . import app, schedular
from flask import request
from werkzeug.urls import url_parse
from datetime import datetime
import json
import os
from flask import jsonify
from .jobs.webScraper import webScrapeToJSON

@app.route("/")
def index():
  script_dir = os.path.dirname(__file__)
  full_path = os.path.join(script_dir, 'jobs/webScraper/scrapeResults.json')
  with open(full_path) as f:
    data = json.load(f)
    return jsonify(data)

def runManualWebScrape():
  print("---------------------------")
  print("Running manual webscrape")
  print("---------------------------")
  webScrapeToJSON()


@app.route('/scrape')
def manualScrape():
  schedular.add_job(func = runManualWebScrape, trigger = 'date', id = 'webScrapeManual')
  return "Added manual scraping to job...results will be updated in approx 5 minutes"
