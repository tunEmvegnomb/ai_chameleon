from flask import Flask
from pymongo import MongoClient


client = MongoClient('localhost', 27017)
db = client.campProject


app = Flask(__name__)


@app.route('/')
def home()


return 123


# --- gif 이미지를 결과페이지에 출력하는 API ---
@app.route('/loadimage', methods=['GET'])
def load_image():
    # -- 로직과 의사코드를 주석으로 달아보세요 --
    pass


if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)
