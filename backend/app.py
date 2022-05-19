from flask import Flask
from pymongo import MongoClient


client = MongoClient('localhost', 27017)
db = client.campProject


app = Flask(__name__)


@app.route('/')
def home()


return 123


if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)
