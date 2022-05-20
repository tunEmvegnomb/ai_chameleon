from flask import Flask, request
from pymongo import MongoClient


client = MongoClient('localhost', 27017)
db = client.chameleon


app = Flask(__name__)


@app.route('/')
def home():
    return 123

# --- gif 이미지를 결과페이지에 출력하는 API ---


# recent_selfie_id = str(db.selfie.find_one()['_id'])


@app.route('/loadimage', methods=['GET'])
def load_image():
    # -- 로직과 의사코드를 주석으로 달아보세요 --
    global recent_selfie_id
    print(f'이것은 리센트 아이디 값입니다 {recent_selfie_id}')
    gif_selfie_id = db.gif.find_one(
        {'selfie_id': recent_selfie_id})['selfie_id']
    print(f'이것은 셀피 아이디 값입니다 {gif_selfie_id}')
    if gif_selfie_id == recent_selfie_id:
        find_gif = db.gif.find_one()['name_gif']

        return find_gif

    # print(gif_selfie_id)
# load_image(recent_selfie_id)
# 1. 셀피 데이터를 먼저 print로 확인함
# 2. 셀피 데이터베이스에서 recent_selfie_id값을 정의해야함
# 3. 셀피 데이터베이스를 활용하여 이미지 gif를 가지고 와야함
# pass


#   --- 셀피 업로드하기 ---
@app.route('/saveselfie', methods=['POST'])
def save_selfie():
    # -- Request --
    # file_receive = request.form
    print(request.files)



    # -- API Progress --

    # -- Response --

    return 'hello'


if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)
