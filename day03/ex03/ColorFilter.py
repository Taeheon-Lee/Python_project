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
        row = img.shape[0]
        for i in range(0, row):
            for j in range(0, row):
                img[i][j][0], img[i][j][1] = 0, 0
        ImageProcessor.display(img)

    @staticmethod
    def to_green(img):
        row = img.shape[0]
        for i in range(0, row):
            for j in range(0, row):
                img[i][j][0], img[i][j][2] = 0, 0
        ImageProcessor.display(img)

    @staticmethod
    def to_red(img):
        row = img.shape[0]
        for i in range(0, row):
            for j in range(0, row):
                img[i][j][1], img[i][j][2] = 0, 0
        ImageProcessor.display(img)

    @staticmethod
    def round(num):
        if num < 0.2:
            return 0.0
        elif 0.2 <= num < 0.4:
            return 0.2
        elif 0.4 <= num < 0.6:
            return 0.4
        elif 0.6 <= num < 0.8:
            return 0.6
        elif 0.8 <= num <= 1.0:
            return 0.8

    @staticmethod
    def celluloid(img):
        row = img.shape[0]
        for i in range(0, row):
            for j in range(0, row):
                boundary = (0.2126 * img[i][j][0] + 0.7152 * img[i][j][1] + 0.0722 * img[i][j][2])
                boundary = round(boundary)
                img[i][j][0] = (boundary - 0.7152 * img[i][j][1] - 0.0722 * img[i][j][2]) / 0.2126
                img[i][j][1] = (boundary - 0.2126 * img[i][j][0] - 0.0722 * img[i][j][2]) / 0.7152
                img[i][j][2] = (boundary - 0.2126 * img[i][j][0] - 0.7152 * img[i][j][1]) / 0.0722
        ImageProcessor.display(img)
