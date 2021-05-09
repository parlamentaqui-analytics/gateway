import os
import requests
from flask import Blueprint, jsonify
from dotenv import load_dotenv

load_dotenv()

ETL_TWITTER_HOST = os.getenv('ETL_TWITTER_HOST')
ETL_TWITTER_PORT = os.getenv('ETL_TWITTER_PORT')

base_url = f"{ETL_TWITTER_HOST}:{ETL_TWITTER_PORT}"

twitter = Blueprint('twitter', __name__, url_prefix='/twitter')

@twitter.route('/')
def index():
    return "twitter"

@twitter.route('/tweets')
def tweets():
    r = requests.get(f'http://{base_url}/api/tweets')
    return jsonify(r.json())
