import torch
import torchvision
from torchvision import models
import torchvision.transforms as T
import numpy as np
from PIL import Image
import matplotlib.pyplot as plt

from sklearn.utils import shuffle


IMG_SIZE = 480

color = [
    (0, 0, 0),       # 0=background*
    (124, 92, 168),     # 1=aeroplane
    (84, 216, 192),     # 2=bicycle*
    (236, 242, 163),   # 3=bird
    (0, 0, 128),     # 4=boat
    (84, 216, 192),   # 5=bottle
    (69, 66, 193),   # 6=bus*
    (248, 110, 127),  # 7=car*
    (255, 255, 255),  # 8=cat*
    (221, 209, 238),     # 9=chair*
    (236, 242, 163),    # 10=cow
    (14, 26, 99),   # 11=dining table*
    (188, 245, 101),    # 12=dog*
    (34, 252, 250),   # 13=horse
    (56, 141, 250),  # 14=motorbike*
    (249, 134, 202),  # 15=person*
    (199, 176, 255),      # 16=potted plant*
    (212, 80, 183),    # 17=sheep
    (212, 80, 95),     # 18=sofa*
    (250, 235, 215),   # 19=train
    (0, 64, 128)     # 20=tv/monitor*
]

pallete = []
for i in range(4):
    color = shuffle(color)
    pallete.append(color)
# for i in pallete:
#   print(i)

deeplab = models.segmentation.deeplabv3_resnet101(pretrained=True).eval()

img = Image.open('frontend/static/img/03.jpg')
plt.figure(figsize=(4, 4))
plt.imshow(img)
print(img)

trf = T.Compose([  # 앞의 일을 순서대로 진행시켜
    T.Resize(480),  # 이미지를 작게 리사이즈(가로사이즈를 맞춰서)
    T.ToTensor(),  # 이미지를 0~1의 값을 갖는 텐서로 바꿈 why? 그래야 컴퓨터가 이해하니까
    T.Normalize(  # 일반화 why? 그래야 컴퓨터가 데이터를 잘 이해해서? 값이 비슷비슷해야 이해를 잘한다고 알고 있음. 아님말고
        mean=[0.485, 0.456, 0.406],  # 평균
        std=[0.229, 0.224, 0.225]  # 표준편차
    )
])

input_img = trf(img).unsqueeze(0)  # 4 차원텐서로 만들어줌 deeplab 모델 돌리기 위해

out = deeplab(input_img)['out']  # deeplab모델 한번 돌리기


# argmax = 21개중에 가장 큰 값만 뽑아냄 dim=0 채널 방향으로  argmax 한다는 얘기
out = torch.argmax(out.squeeze(), dim=0)
out = out.detach().cpu().numpy()  # 텐서를 떼어낸 다음에 numpy 어레이로 바꿔줌
print(out.shape)
print(np.unique(out))


def seg_map(img, color):  # 이미지로 되돌리는 과정
    # img.shqpe의 0번 인덱스는 세로값, img.shape 1번 인덱스는 가로값, 3은 색상이예요. dtype 은 이미지랑 똑같이 만들기 위해 지정했다
    rgb = np.zeros((img.shape[0], img.shape[1], 3), dtype=np.uint8)
    for c in range(21):
        idx = img == c

        rgb[idx] = color[c]
    return rgb


img_list = []

for i in pallete:

    img_out = seg_map(out, i)

    img_list.append(img_out)

    fig, ax = plt.subplots(nrows=1, ncols=2, figsize=(16, 16))
    ax[1].imshow(img_out)
    plt.show()
