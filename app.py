# -*- coding: utf-8 -*-
from flask import Flask
app = Flask(__name__)


@app.route('/')
def hello():
    return 'Welcome to My Watchlist!'
