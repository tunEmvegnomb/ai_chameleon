import os
import imageio
import torch
import torchvision
import datetime
from torchvision import models
import torchvision.transforms as T
import numpy as np
from PIL import Image
import matplotlib.pyplot as plt

from sklearn.utils import shuffle

from datetime import date, datetime, timedelta


def make_gif(filename):
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

    deeplab = models.segmentation.deeplabv3_resnet101(pretrained=True).eval()

    img = Image.open(f'static/image/selfie/{filename}').convert('RGB')

    trf = T.Compose([
        T.Resize(480),
        T.ToTensor(),
        T.Normalize(
            mean=[0.485, 0.456, 0.406],
            std=[0.229, 0.224, 0.225]
        )
    ])
    print(trf(img).shape)

    input_img = trf(img).unsqueeze(0)

    out = deeplab(input_img)['out']  # deeplab모델 한번 돌리기

    out = torch.argmax(out.squeeze(), dim=0)
    out = out.detach().cpu().numpy()

    def seg_map(img, color):  # 이미지로 되돌리는 과정

        rgb = np.zeros((img.shape[0], img.shape[1], 3), dtype=np.uint8)
        for c in range(21):
            idx = img == c

            rgb[idx] = color[c]
        return rgb

    # 이미지 출력 저장
    img_list = []
    current_time = datetime.now().strftime('%Y%m%d%H%M%S')
    n = 1

    for i in pallete:
        img_out = seg_map(out, i)
        img_list.append(img_out)
    imageio.mimsave(
        f"static/image/gif/{current_time}.gif", img_list, fps=3)

    return current_time
