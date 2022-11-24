# initial default file AKA index file

from flask import Flask

app = Flask(__name__)

from application import routes