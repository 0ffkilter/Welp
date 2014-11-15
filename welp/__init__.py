from flask import Flask

welp = Flask(__name__)
welp.config.from_object('welp.config.Config')
from welp import views
