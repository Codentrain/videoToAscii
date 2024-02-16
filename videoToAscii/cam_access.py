from cv2 import VideoCapture

cam_port = 0
cam = VideoCapture(cam_port)


def capture():
    # reading the input using the camera
    result, image = cam.read()

    return image
