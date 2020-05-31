class Vector:
    def __init__(self, my_list, my_size, my_range):
        if my_list:
            if isinstance(my_list, list):
                for elem in my_list:
                    if not isinstance(elem, float):
                        raise ValueError("Values of list should be float")
                    self.my_list = my_list
                    self.length = len(my_list)
            else:
                raise TypeError("Put list on the first param")
        if my_size:
            if not isinstance(my_size, int):
                raise TypeError("A size should be integer")
            if not self.my_list:
                self.my_list = []
                for elem in range(my_size):
                    self.my_list[elem] = elem
                self.length = len(my_list)
            else:
                copy = []
                for elem in range(my_size):
                    copy[elem] = elem
                if (self.my_list != copy):
                    raise ValueError("My_list is not matched with my_size")
        if my_range:
            if not isinstance(my_range, tuple):
                raise TypeError("A range should be tuple")
            if not len(my_range) == 2:
                raise ValueError("A length of range should be two")
            for elem in my_range:
                if not isinstance(elem, int):
                    raise ValueError("Values of range should be integer")
            if not self.my_list:
                i = 0
                self.my_list = []
                for elem in range(my_range[0], my_range[1]):
                    self.my_list[i] == elem
                    i += 1
                self.length = len(my_list)
            else:
                i = 0
                copy = []
                for elem in range(my_range[0], my_range[1]):
                    copy[i] == elem
                    i += 1
                if (self.my_list != copy):
                    raise ValueError("My_list is not matched with my_range")
        else:
            raise ValueError("Nothing initialized")

    def __add__(self, scalars_or_vectors):
        if isinstance(scalars_or_vectors, Vector):
            if self.length == scalars_or_vectors.length:
                for elem in range(self.length):
                    self.my_list[elem] += scalars_or_vectors.my_list[elem]
            else:
                raise ValueError("Size of vectors are different respectively")
        elif isinstance(scalars_or_vectors, int) or isinstance(scalars_or_vectors, float):
            for elem in range(self.length):
                self.my_list[elem] += scalars_or_vectors
        else:
            raise TypeError("An input is not scalars or vectors")

    def __radd__(self, scalars_or_vectors):
        if isinstance(scalars_or_vectors, Vector):
            if self.length == scalars_or_vectors.length:
                for elem in range(self.length):
                    self.my_list[elem] += scalars_or_vectors.my_list[elem]
            else:
                raise ValueError("Size of vectors are different respectively")
        elif isinstance(scalars_or_vectors, int) or isinstance(scalars_or_vectors, float):
            for elem in range(self.length):
                self.my_list[elem] += scalars_or_vectors
        else:
            raise TypeError("An input is not scalars or vectors")

    def __sub__(self, scalars_or_vectors):
        if isinstance(scalars_or_vectors, Vector):
            if self.length == scalars_or_vectors.length:
                for elem in range(self.length):
                    self.my_list[elem] -= scalars_or_vectors.my_list[elem]
            else:
                raise ValueError("Size of vectors are different respectively")
        elif isinstance(scalars_or_vectors, int) or isinstance(scalars_or_vectors, float):
            for elem in range(self.length):
                self.my_list[elem] -= scalars_or_vectors
        else:
            raise TypeError("An input is not scalars or vectors")

    def __rsub__(self, scalars_or_vectors):
        if isinstance(scalars_or_vectors, Vector):
            if self.length == scalars_or_vectors.length:
                for elem in range(self.length):
                    self.my_list[elem] -= scalars_or_vectors.my_list[elem]
            else:
                raise ValueError("Size of vectors are different respectively")
        elif isinstance(scalars_or_vectors, int) or isinstance(scalars_or_vectors, float):
            for elem in range(self.length):
                self.my_list[elem] -= scalars_or_vectors
        else:
            raise TypeError("An input is not scalars or vectors")

    def __truediv__(self, scalars):
        if isinstance(scalars, int):
            if scalars != 0:
                for elem in range(self.length):
                    self.my_list[elem] /= scalars
            else:
                raise ValueError("Can not divided by 0")
        else:
            raise TypeError("An input should be only scalars")

    def __rtruediv__(self, scalars):
        if isinstance(scalars, int):
            if scalars != 0:
                for elem in range(self.length):
                    self.my_list[elem] /= scalars
            else:
                raise ValueError("Can not divided by 0")
        else:
            raise TypeError("An input should be only scalars")

    def __mul__(self, scalars_or_vectors):
        if isinstance(scalars_or_vectors, Vector):
            if self.length == scalars_or_vectors.length:
                for elem in range(self.length):
                    self.my_list[elem] *= scalars_or_vectors.my_list[elem]
            else:
                raise ValueError("Size of vectors are different respectively")
        elif isinstance(scalars_or_vectors, int) or isinstance(scalars_or_vectors, float):
            for elem in range(self.length):
                self.my_list[elem] *= scalars_or_vectors
        else:
            raise TypeError("An input is not scalars or vectors")

    def __rmul__(self, scalars_or_vectors):
        if isinstance(scalars_or_vectors, Vector):
            if self.length == scalars_or_vectors.length:
                for elem in range(self.length):
                    self.my_list[elem] *= scalars_or_vectors.my_list[elem]
            else:
                raise ValueError("Size of vectors are different respectively")
        elif isinstance(scalars_or_vectors, int) or isinstance(scalars_or_vectors, float):
            for elem in range(self.length):
                self.my_list[elem] *= scalars_or_vectors
        else:
            raise TypeError("An input is not scalars or vectors")

    def __str__(self):
        pass

    def __repr__(self):
        pass
