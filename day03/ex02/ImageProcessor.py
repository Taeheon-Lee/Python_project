import numpy as np
import matplotlib.pyplot as plt
import matplotlib.image as img

class ImageProcessor:
    @staticmethod
    def load(input):
        my_img = img.imread(input)
        my_shape = my_img.shape
        pix = np.array(my_img)
        print("Loading image of dimensions", my_shape[0], "x", my_shape[1])
        return (pix)

    @staticmethod
    def display(arr):
        plt.imshow(arr)
        plt.show()
