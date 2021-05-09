import os
import requests
from flask import Blueprint
from dotenv import load_dotenv

load_dotenv()

ETL_TSE_HOST = os.getenv('ETL_TSE_HOST')
ETL_TSE_PORT = os.getenv('ETL_TSE_PORT')

base_url = f"{ETL_TSE_HOST}:{ETL_TSE_PORT}"

tse = Blueprint('tse', __name__, url_prefix='/tse')

@tse.route('/')
def index():
    return "tse"

@tse.route('/deputies')
def deputies():
    r = requests.get(f'http://{base_url}/api/deputies')
    return r.json()