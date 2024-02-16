from cv2 import cvtColor, resize, COLOR_BGR2GRAY, INTER_AREA

grey_scale_char = ' .:-=+*#%@'
# greyScalChar = '@%#*+=-:. '
# greyScalChar = "$@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/\|()1{}[]?-_+~<>i!lI;:,\"^`'. "


def img_to_grey_scale(img):
    return cvtColor(img, COLOR_BGR2GRAY)


def scale_img(img, width, height):
    return resize(img, dsize=(width, height), interpolation=INTER_AREA)


def grey_to_char(grey_val):
    return grey_scale_char[int((grey_val * 7) / 255)]


def img_to_text(img):

    matrix = img.tolist()
    text_img = ""

    for i in range(len(matrix)):
        for j in range(len(matrix[0]) - 1, 0, -1):
            text_img += grey_to_char(matrix[i][j])
        text_img += "\n"

    return text_img
