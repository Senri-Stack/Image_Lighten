import cv2

import os
import configparser

class Image:
    def __init__(self):
        self.path_dir = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__), 'file'))

    def make_save_path(self):
        self.save_dir = os.path.join(self.path_dir, 'save_img')
        if not os.path.exists(self.save_dir):
            os.mkdir(self.save_dir)

    def en_decode(self):
        self.img = cv2.imread('file/img/input.jpg')
        result, encimg = cv2.imencode("img2.jpg", self.img, [int(cv2.IMWRITE_JPEG_QUALITY), 25])
        cv2.imwrite("file/save_img/output.jpg", self.img)

if __name__ == "__main__":
    app = Image()
    app.make_save_path()
    app.en_decode()