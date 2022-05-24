# 0. 사용할 패키지 불러오기
from keras.models import load_model
from keras.utils import np_utils
from keras.datasets import mnist
from keras.models import Sequential
from keras.layers import Dense, Activation
import numpy as np
from numpy import argmax

# 0. 하드로 이미지 세팅
# np.array로 만들어주기
from PIL import Image

img = Image.open("backend/static/image/base/smile.jpeg")
imgArray = np.array(img)
print(imgArray.shape)


# # 1. 실무에 사용할 데이터 준비하기
# (x_train, y_train), (x_test, y_test) = mnist.load_data()
# x_test = x_test.reshape(10000, 784).astype('float32') / 255.0
# y_test = np_utils.to_categorical(y_test)
# xhat_idx = np.random.choice(x_test.shape[0], 5)
# xhat = x_test[xhat_idx]

# # 2. 모델 불러오기
# model = load_model('mnist_mlp_model.h5')

# # 3. 모델 사용하기
# yhat = model.predict_classes(xhat)

# for i in range(5):
#     print('True : ' +
#           str(argmax(y_test[xhat_idx[i]])) + ', Predict : ' + str(yhat[i]))


# test_imgs, test_labels = test_gen.__getitem__(100)
# print(test_imgs.shape)

# y_pred = model.predict(test_imgs)

# classes = dict((v, k) for k, v in test_gen.class_indices.items())
# fig, axes = plt.subplots(2,8, figsize=(20,12))

# for img, test_label, pred_label, ax in zip(test_imgs, test_labels, y_pred, axes.flatten()):
#   test_label = classes[np.argmax(test_label)]
#   pred_label = classes[np.argmax(pred_label)]

# #   # 만약 라벨 값이 0.5 이상이면 1로 만들어주는 쓰레시홀드 만들기
# #   test_label = 'cat' if pred_label > 0.5 else 'dog'

#   ax.set_title('GT:%s\nPR:%s' % (test_label, pred_label))
#   ax.imshow(img)

#   # print(test_label)
