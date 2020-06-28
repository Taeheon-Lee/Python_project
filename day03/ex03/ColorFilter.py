from ImageProcessor import ImageProcessor
import numpy as np

class ColorFilter():
    @staticmethod
    def invert(img):
        row = img.shape[0]
        for i in range(0, row):
            img[i] = 1 - img[i]
        ImageProcessor.display(img)

    @staticmethod
    def to_blue(img):
        pass

    @staticmethod
    def to_green(img):
        pass

    @staticmethod
    def to_red(img):
        pass

    @staticmethod
    def celluloid(img):
        pass
