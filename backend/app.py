from flask import Flask, jsonify, request, render_template
from pymongo import MongoClient
from datetime import datetime
from flask_cors import CORS
import model
import emotion_sq


app = Flask(__name__)
cors = CORS(app, resources={r"*": {"origins": "*"}})


client = MongoClient('localhost', 27017)
db = client.chameleon

recent_selfie_id = None
filename = ""


@app.route('/')
def home():
    return render_template('main.html')


@app.route('/result')
def result_page():

    return render_template('result.html')


@app.route('/loadimage', methods=['GET'])
def load_image():
    global recent_selfie_id
    gif_selfie_id = db.gif.find_one(
        {'selfie_id': recent_selfie_id})['selfie_id']
    if gif_selfie_id == recent_selfie_id:
        find_gif = db.gif.find_one()['name_gif']

        return jsonify({'find_gif': find_gif}, recent_selfie_id)


#   --- 셀피 업로드하기 ---
@app.route('/saveselfie', methods=['POST'])
def save_selfie():

    file_receive = request.files['file_give']
    extension = file_receive.filename.split('.')[-1]

    time_now = datetime.now()
    timestamp = f"{time_now.strftime('%Y%m%d_%H%M%S')}"

    global filename
    filename = f'{timestamp}.{extension}'

    save_to = f'static/image/selfie/{filename}'
    file_receive.save(save_to)

    doc_selfie = {
        'name_selfie': filename
    }

    db.selfie.insert_one(doc_selfie)
    model.make_gif(filename)

    global recent_selfie_id
    recent_selfie_id = str(db.selfie.find_one(
        {'name_selfie': filename})['_id'])

    return jsonify({'save_to': save_to, 'recent_selfie_id': recent_selfie_id, 'filename': filename})

# --- gif로 변환 ---
@app.route('/savegif', methods=['POST'])
def save_gif():
    data = request.form
    filename = request.form['filename']
    recent_selfie_id = request.form['recent_selfie_id']
    
    global current_time
    current_time = model.make_gif(filename)

    gif_doc = {
        'selfie_id': recent_selfie_id,
        'name_gif': current_time
    }
    db.gif.insert_one(gif_doc)
    
    return jsonify({'msg': 'gif를 저장했습니다!', 'current_time': current_time})


@app.route('/loadgif', methods=['GET'])
def result_gif():
    return jsonify({'current_time': current_time})


# -- 감정 인식 함수 호출 --
@app.route('/emotion', methods=['GET'])
def load_emotion():
    global filename
    file = db.selfie.find_one({'name_selfie': filename})
    result = emotion_sq.find_emotion(filename)

    # -- 리스트 형식의 감정을 담음 --
    emotion = ['Angry', 'Disgust', 'Fear',
               'Happy', 'Sad', 'Surprise', 'Neutral']

    # -- result는 0~6 사이의 정수이므로 emotion list의 result를 대입해 감정을 빼낸다
    music_index = emotion[result]
    return jsonify({'music_index': music_index})


if __name__ == '__main__':
    app.run('127.0.0.1', port=5000, debug=True)
