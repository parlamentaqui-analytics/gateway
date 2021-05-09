import os
from flask import Flask
from news.news import news
from twitter.twitter import twitter
from camara.camara import camara
from tse.tse import tse
from flask_cors import CORS 

app = Flask(__name__)
cors = CORS(app)
app.register_blueprint(news)
app.register_blueprint(twitter)
app.register_blueprint(camara)
app.register_blueprint(tse)

PORT = os.getenv('PORT')

@app.route('/')
def index():
    return "Parlamentaqui Gateway!!!"

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=PORT)
