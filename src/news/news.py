import os
import requests
import json
from flask import Blueprint, jsonify
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
    return jsonify(r.json())

#Pega as duas mais recentes noticias em formato json
@news.route('/latestNews')
def latest_news():
    r = requests.get(f'http://{base_url}/api/news')
    return jsonify(r.json())

@news.route('/latestNews/<id>')
def latest_news_by_id(id):
    r = requests.get(f'http://{base_url}/api/get_news_by_id/{id}')
    return jsonify(r.json())
