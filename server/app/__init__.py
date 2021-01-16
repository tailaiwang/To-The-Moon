from flask import Flask
from config import Config
import os
from flask_apscheduler import APScheduler
from .jobs.webScraper import webScrapeToJSONAndPush
import time
from google.cloud import language_v1


app = Flask(__name__)
app.config.from_object(Config)

schedular = APScheduler()
schedular.init_app(app)
schedular.start()

client = language_v1.LanguageServiceClient()

def runAutomaticWebScrape():
  print("---------------------------")
  print("Running automatic webscrape")
  print("---------------------------")
  webScrapeToJSONAndPush()

schedular.add_job(id = 'webScrapeAuto', func = runAutomaticWebScrape, trigger = 'interval', seconds = 900)








from . import routes