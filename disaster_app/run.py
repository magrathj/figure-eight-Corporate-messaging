from disaster_app import app

import json
import plotly
import pandas as pd

import nltk
print("hey")

from nltk.stem import WordNetLemmatizer
from nltk.tokenize import word_tokenize

from flask import Flask
from flask import render_template, request, jsonify
from plotly.graph_objs import Bar
from sklearn.externals import joblib
from sqlalchemy import create_engine
from sqlalchemy.engine import reflection



@app.route('/')
@app.route('/index', methods=['POST', 'GET'])
def index():
    return "Hello, World!"
