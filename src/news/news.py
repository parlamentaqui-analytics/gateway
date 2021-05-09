import os
import requests
from flask import Blueprint
from dotenv import load_dotenv

load_dotenv()

ETL_NEWS_HOST = os.getenv('ETL_NEWS_HOST')
ETL_NEWS_PORT = os.getenv('ETL_NEWS_PORT')

base_url = f"{ETL_NEWS_HOST}:{ETL_NEWS_PORT}"

news = Blueprint('news', __name__, url_prefix='/news')

@news.route('/')
def index():
    return "news"

@news.route('/deputies')
def deputies():
    r = requests.get(f'http://{base_url}/api/deputies')
    return r.json()