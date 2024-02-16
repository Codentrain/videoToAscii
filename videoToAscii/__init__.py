import img_converter
import cam_access


def build_img():
    img = cam_access.capture()
    img_gray = img_converter.img_to_grey_scale(img)
    resize = img_converter.scale_img(img_gray, w, h)
    return img_converter.img_to_text(resize)