
from flask.helpers import url_for
from google.cloud import language_v1
from . import app, schedular, client
from flask import request
from werkzeug.urls import url_parse
from datetime import datetime
import json
import os
from flask import jsonify
from .jobs.webScraper import webScrapeToJSONAndPush




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
  webScrapeToJSONAndPush()


@app.route('/scrape')
def manualScrape():
  schedular.add_job(func = runManualWebScrape, trigger = 'date', id = 'webScrapeManual')
  return "Added manual scraping to job...results will be updated in approx 5 minutes"



def getSentiment(text):

  document = language_v1.Document(content=text, type_=language_v1.Document.Type.PLAIN_TEXT)

  # Detects the sentiment of the text
  sentiment = client.analyze_sentiment(request={'document': document}).document_sentiment
  return("Sentiment: {}, {}".format(sentiment.score, sentiment.magnitude))



@app.route("/ratings")


@app.route("/ratings/<stockTicker>")



