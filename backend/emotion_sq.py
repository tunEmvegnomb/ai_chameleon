# 0. 사용할 패키지 불러오기
from aiohttp import parse_content_disposition
import tensorflow as tf
from keras.models import load_model
from keras.utils import np_utils
from keras.datasets import mnist
from keras.models import Sequential
from keras.layers import Dense, Activation
import numpy as np
from numpy import argmax
from PIL import Image
import os
os.environ["CUDA_VISIBLE_DEVICES"] = "-1"
# 0. 하드로 이미지 세팅
# np.array로 만들어주기


def find_emotion(filename):
    image = Image.open(f'static/image/selfie/{filename}').convert("L")
    print(type(image))
    newsize = (48, 48)
    image = image.resize(newsize)
    img = np.asarray(image)
    img = img.astype(np.float32)/255.
    img = np.reshape(img, (-1, 48, 48))

    print(img.shape)

    model = load_model('emotion_sq.h5')

    # # 3. 모델 사용하기
    yhat = model.predict(img)

    print(np.argmax(yhat))
    e_result = np.argmax(yhat)
    return e_result
