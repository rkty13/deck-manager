from flask import Flask

app = Flask(__name__)

app.config.from_pyfile("dev_config.cfg")

from . import models
from . import controllers
from . import views