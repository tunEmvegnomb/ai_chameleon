from flask import Flask, jsonify, request, render_template, redirect, url_for
from pymongo import MongoClient
from werkzeug.utils import secure_filename
from datetime import datetime, timedelta
import os
from flask_cors import CORS
import model


app = Flask(__name__)
cors = CORS(app, resources={r"*": {"origins": "*"}})
# CORS(app)


client = MongoClient('localhost', 27017)
db = client.chameleon

recent_selfie_id = None

@app.route('/')
def home():
    return render_template('main.html')

# recent_selfie_id = str(db.selfie.find_one()['_id'])


@app.route('/result')
def result_page():

    return render_template('result.html')


@app.route('/loadimage', methods=['GET'])
def load_image():
    # -- 로직과 의사코드를 주석으로 달아보세요 --
    global recent_selfie_id
    print(f'최근 아이디 값은 : {recent_selfie_id}')
    gif_selfie_id = db.gif.find_one(
        {'selfie_id': recent_selfie_id})['selfie_id']
    print(f'이것은 셀피 아이디 값입니다 {gif_selfie_id}')
    if gif_selfie_id == recent_selfie_id:
        find_gif = db.gif.find_one()['name_gif']

        return jsonify({'find_gif': find_gif}, recent_selfie_id)

    # print(gif_selfie_id)
# load_image(recent_selfie_id)
# 1. 셀피 데이터를 먼저 print로 확인함
# 2. 셀피 데이터베이스에서 recent_selfie_id값을 정의해야함
# 3. 셀피 데이터베이스를 활용하여 이미지 gif를 가지고 와야함
# pass


#   --- 셀피 업로드하기 ---
@app.route('/saveselfie', methods=['POST'])
def save_selfie():
    # print('업로드로 들어오긴 합니까?')
    # print(request)
    # print(f'헤더에 오리진 들어옴? {request.headers}')
    # -- Request --
    file_receive = request.files['file_give']
    print(f'받아온 파일은 {request.files}')

    # -- API Progress --
    extension = file_receive.filename.split('.')[-1]
    print(f'extension {extension}')

    time_now = datetime.now()
    timestamp = f"{time_now.strftime('%Y%m%d_%H%M%S')}"
    filename = f'{timestamp}.{extension}'
    print(f'filename : {filename}')

    save_to = f'static/image/selfie/{filename}'
    file_receive.save(save_to)

    doc_selfie = {
        'name_selfie': filename
    }

    db.selfie.insert_one(doc_selfie)
    model.make_gif(filename)

    global recent_selfie_id
    recent_selfie_id = str(db.selfie.find_one({'name_selfie': filename})['_id'])
    print(f'최근 아이디 값은 : {recent_selfie_id}')

    # # -- Response --
    return jsonify({'save_to': save_to, 'recent_selfie_id': recent_selfie_id, 'filename': filename})
    # return redirect(url_for('save_gif')), recent_selfie_id, filename


@app.route('/savegif', methods=['POST'])
def save_gif():
    # --- Request ---
    data = request.form
    print(f'리퀘스트 폼 {data}')
    filename = request.form['filename']
    print(f'savegif : filename : {filename}')
    recent_selfie_id = request.form['recent_selfie_id']
    print(f'savegif : recent_id : {recent_selfie_id}')
    # --- Progress ---
    global current_time
    current_time = model.make_gif(filename)
    print(f'모델작동 {current_time}')

    gif_doc = {
        'selfie_id': recent_selfie_id,
        'name_gif': current_time
    }
    db.gif.insert_one(gif_doc)
    print('gif 데이터베이스 삽입')
    # --- Response ---

    return jsonify({'msg': 'gif를 저장했습니다!', 'current_time': current_time})


@app.route('/loadgif', methods=['GET'])
def result_gif():
    print(current_time, "1")

    return jsonify({'current_time': current_time})


if __name__ == '__main__':
    app.run('127.0.0.1', port=5000, debug=True)
