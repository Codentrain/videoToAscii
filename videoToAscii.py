import time
import os

import cam_acces
import img_converter


def build_img():
    img = cam_acces.capture()
    img_gray = img_converter.img_to_grey_scale(img)
    resize = img_converter.scale_img(img_gray, 192, 64)
    return img_converter.img_to_text(resize)


while True:
    print(build_img())
    time.sleep(1 / 60)
