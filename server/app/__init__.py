from flask import Flask
from config import Config
import os
from flask_apscheduler import APScheduler

import time
from google.cloud import language_v1


app = Flask(__name__)
app.config.from_object(Config)

schedular = APScheduler()
schedular.init_app(app)
schedular.start()

client = language_v1.LanguageServiceClient()










from . import routes
from .jobs.webScraper import webScrapeToJSONAndPush