from flask import Flask
from news.news import news
from twitter.twitter import twitter
from camara.camara import camara
from tse.tse import tse

app = Flask(__name__)
app.register_blueprint(news)
app.register_blueprint(twitter)
app.register_blueprint(camara)
app.register_blueprint(tse)

@app.route('/')
def index():
    return "Parlamentaqui Gateway!!!"

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')