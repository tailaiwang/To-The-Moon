
from flask.helpers import url_for

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
from flask import jsonify


def newEncoder(o):
    if type(o) == ObjectId:
        return str(o)
    return o.__str__


@app.route("/api")
def index():
    script_dir = os.path.dirname(__file__)
    full_path = os.path.join(script_dir, 'jobs/webScraper/scrapeResults.json')
    with open(full_path) as f:
        data = json.load(f)
        return jsonify(data)


@app.route("/api/tickers", methods=["GET"])  # return unique tickers
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


@app.route("/api/live", methods=["GET"])  # return live DB
def live():
    headers = {'Authorization': os.environ.get('DATABASE_ACCESS_KEY')}
    r = requests.get(os.environ.get('DATABASE_REST_API'), headers=headers)
    return r.text


def runAutomaticWebScrape():
    print("---------------------------")
    print("Running automatic webscrape")
    print("---------------------------")
    webScrapeToJSONAndPush()


# add automatic task
schedular.add_job(id='webScrapeAuto', func=runAutomaticWebScrape,
                  trigger='interval', seconds=86400)


def runManualWebScrape():
    print("---------------------------")
    print("Running manual webscrape")
    print("---------------------------")
    webScrapeToJSONAndPush()


@app.route('/api/scrape')
def manualScrape():
    schedular.add_job(func=runManualWebScrape,
                      trigger='date', id='webScrapeManual')
    return "Added manual scraping to job...results will be updated in approx 30 minutes"


@app.route("/api/ratings")
def getAllRatings():
    ratings = []

    headers = {'Authorization': os.environ.get('DATABASE_ACCESS_KEY')}
    r = requests.get(os.environ.get('DATABASE_REST_API'), headers=headers)
    data = r.json()

    for stock in data:
        ratings.append(
            {
                "ticker": stock["ticker"],
                "rating": stock["rating"]
            }
        )
    return jsonify(ratings)


@app.route("/api/ratings/<stockTicker>")
def getRatingDetail(stockTicker):
    headers = {'Authorization': os.environ.get('DATABASE_ACCESS_KEY')}
    r = requests.get(os.environ.get('DATABASE_REST_API'), headers=headers)
    data = r.json()
    if list(filter(lambda stock: stock["ticker"] == stockTicker, data)):
        return jsonify(list(filter(lambda stock: stock["ticker"] == stockTicker, data))[0])
    return "Stock not found", 400
