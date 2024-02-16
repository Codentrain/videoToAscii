import time
import argparse

import cam_acces
import img_converter

parser = argparse.ArgumentParser(description="read camera stream and display the result in the terminal")
parser.add_argument("--height", type=int, default=64)
parser.add_argument("--width", type=int, default=192)
parser.add_argument("--rate", type=int, default=60)
args = parser.parse_args()

h = args.height
w = args.width
r = args.rate


def build_img():
    img = cam_acces.capture()
    img_gray = img_converter.img_to_grey_scale(img)
    resize = img_converter.scale_img(img_gray, w, h)
    return img_converter.img_to_text(resize)


while True:
    print(build_img())
    time.sleep(1 / r)
