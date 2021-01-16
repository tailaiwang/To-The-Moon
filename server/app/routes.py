
from flask.helpers import url_for
from google.cloud import language_v1
from . import app, schedular, client
from flask import request
from werkzeug.urls import url_parse
from datetime import datetime
import requests
import json
import os
import re
from flask import jsonify
from .jobs.webScraper import webScrapeToJSONAndPush


@app.route("/")
def index():
  script_dir = os.path.dirname(__file__)
  full_path = os.path.join(script_dir, 'jobs/webScraper/scrapeResults.json')
  with open(full_path) as f:
    data = json.load(f)
    return jsonify(data)


@app.route("/tickers/") # return unique tickers
def titles():
  script_dir = os.path.dirname(__file__)
  full_path = os.path.join(script_dir, 'jobs/webScraper/scrapeResults.json')
  with open(full_path) as f:
    data = json.load(f)
    tickerSet = set()
    for line in data:
      tickerSet.add(line['stockTicker'])

    retval = []
    for item in tickerSet:
      retval.append(item)

    return jsonify(retval)

@app.route("/live", methods=["GET"]) # return live DB
def live():
  headers = { 'Authorization': os.environ.get('DATABASE_ACCESS_KEY')}
  r = requests.get(os.environ.get('DATABASE_REST_API'), headers=headers)
  return r.text


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
  return sentiment.score

# Calculates the average rating per stock ticker based on WSB
def calcRating(title, description, score, comments, flairs, awards, count):
  rating = 0
  titleSenti = getSentiment(title)
  descSenti = getSentiment(description)
  commentsSenti = getSentiment(comments)
  totalSenti = 3 * titleSenti + 2 * descSenti + commentsSenti

  # find the number of rocket ships inside the comments, title, desc
  # rocketShipCount = 0.10 * len(re.findall(ru'🚀', title + description + comments))
  # finds the number of YOLOs, each YOLO is +5
  yoloCount = flairs.count("YOLO")

  rating = (totalSenti * (score + awards) + rocketShipCount + yoloCount ) / count
  return rating

@app.route("/ratings")
def getAllRatings():
  ratings= []
  #replace with API call later
  script_dir = os.path.dirname(__file__)
  full_path = os.path.join(script_dir, 'jobs/webScraper/poggedResults.json')
  with open(full_path) as f:
    data = json.load(f)
    for stock in data:
      ratings.append(
        {
          "ticker": stock["ticker"],
        }
      )
  return ratings.__str__()
    

@app.route("/ratings/<stockTicker>")
def getRatingDetail(stockTicker):
  #replace with API call later
  script_dir = os.path.dirname(__file__)
  full_path = os.path.join(script_dir, 'jobs/webScraper/poggedResults.json')
  with open(full_path) as f:
    data = json.load(f)
    if filter(lambda stock : stock["ticker"] == stockTicker, data):
      return list(filter(lambda stock : stock["ticker"] == stockTicker, data))[0].__str__()
  return "Stock not found", 400


