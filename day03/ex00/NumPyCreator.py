import numpy as np

class NumPyCreator:
    @staticmethod
    def from_list(my_list):
        arr = np.array(my_list)
        return (arr)

    @staticmethod
    def from_tuple(my_tuple):
        my_list = list(my_tuple)
        arr = np.array(my_list)
        return (arr)

    @staticmethod
    def from_iterable(my_range):
        my_list = list(my_range)
        arr = np.array(my_list)
        return (arr)

    @staticmethod
    def from_shape(shape, value=0):
        if not isinstance(shape, tuple):
            raise TypeError("Shape should be tuple")
        if not len(shape) == 2:
            raise ValueError("Elements of shape should be 2")
        arr = np.full(shape, value)
        return (arr)

    @staticmethod
    def random(shape):
        if not isinstance(shape, tuple):
            raise TypeError("Shape should be tuple")
        if not len(shape) == 2:
            raise ValueError("Elements of shape should be 2")
        arr = np.random.rand(shape[0], shape[1])
        return (arr)

    @staticmethod
    def identity(n):
        arr = np.eye(n)
        return (arr)
