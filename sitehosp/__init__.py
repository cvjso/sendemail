import os
from flask import Flask

app = Flask(__name__)
app.config['SECRET_KEY'] = '5928e1d7adda985bfcbb3df2a0a3549c'

from sitehosp.controllers import default
