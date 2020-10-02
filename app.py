import flask
from flask import request, jsonify
from flask import render_template
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity


app = flask.Flask(__name__)


@app.route('/', methods=['GET'])
def home():
    
        return "Home Page"
