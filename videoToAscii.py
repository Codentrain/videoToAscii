import time
import argparse

from videoToAscii import build_img

parser = argparse.ArgumentParser(description="read camera stream and display the result in the terminal")
parser.add_argument("--height", type=int, default=64)
parser.add_argument("--width", type=int, default=192)
parser.add_argument("--rate", type=int, default=60)
args = parser.parse_args()

h = args.height
w = args.width
r = args.rate


while True:
    print(build_img())
    time.sleep(1 / r)
