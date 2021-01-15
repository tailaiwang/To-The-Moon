from flask import Flask
from config import Config
import os

app = Flask(__name__)
app.config.from_object(Config)



from . import routes