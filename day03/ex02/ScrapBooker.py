from ImageProcessor import ImageProcessor
import numpy as np


class ScrapBooker:

    @staticmethod
    def crop(array, dimensions=(1, 1), position=(0, 0)):
        start_x = position[0]
        start_y = position[1]
        end_x = start_x + dimensions[0]
        end_y = start_y + dimensions[1]
        if (end_x <= array.shape[0] and end_y <= array.shape[1]):
            return (array[start_x:end_x, start_y:end_y]) # refer to numpy indexing
        raise ValueError("dimensions are larger than the current image size.")

    @staticmethod
    def thin(array, n, axis):
        return np.delete(array, slice(n - 1, None, n), axis - 1)

    @staticmethod
    def juxtapose(array, n, axis):
        return np.concatenate([array] * n, axis=axis)

    @staticmethod
    def mosaic(array, dimensions):
        return np.tile(array, (dimensions[0], dimensions[1], 1))
