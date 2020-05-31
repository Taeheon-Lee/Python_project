class Vector:
    def __init__(self, input):
        if isinstance(input, list):
            for elem in input:
                if not isinstance(elem, float):
                    raise ValueError("Values of list should be float")
                self.values = input
                self.size = len(self.values)
        elif isinstance(input, int):
                self.values = []
                for elem in range(input):
                    self.values.append(float(elem))
                self.size = len(self.values)
        elif isinstance(input, tuple) and len(input) == 2:
            for elem in input:
                if not isinstance(elem, int):
                    raise ValueError("Values of range should be integer")
                self.values = []
                for elem in range(input[0], input[1]):
                    self.values.append(float(elem))
                self.size = len(self.values)
        else:
            raise ValueError("Type of input is wrong. Input should be list or integer or tuple")

    def __add__(self, scalars_or_vectors):
        if isinstance(scalars_or_vectors, Vector):
            if self.size == scalars_or_vectors.size:
                for elem in range(self.size):
                    self.values[elem] += scalars_or_vectors.values[elem]
            else:
                raise ValueError("Size of vectors are different respectively")
        elif isinstance(scalars_or_vectors, int) or isinstance(scalars_or_vectors, float):
            for elem in range(self.size):
                self.values[elem] += scalars_or_vectors
        else:
            raise TypeError("An input is not scalars or vectors")

    def __radd__(self, scalars_or_vectors):
        if isinstance(scalars_or_vectors, Vector):
            if self.size == scalars_or_vectors.size:
                for elem in range(self.size):
                    self.values[elem] += scalars_or_vectors.values[elem]
            else:
                raise ValueError("Size of vectors are different respectively")
        elif isinstance(scalars_or_vectors, int) or isinstance(scalars_or_vectors, float):
            for elem in range(self.size):
                self.values[elem] += scalars_or_vectors
        else:
            raise TypeError("An input is not scalars or vectors")

    def __sub__(self, scalars_or_vectors):
        if isinstance(scalars_or_vectors, Vector):
            if self.size == scalars_or_vectors.size:
                for elem in range(self.size):
                    self.values[elem] -= scalars_or_vectors.values[elem]
            else:
                raise ValueError("Size of vectors are different respectively")
        elif isinstance(scalars_or_vectors, int) or isinstance(scalars_or_vectors, float):
            for elem in range(self.size):
                self.values[elem] -= scalars_or_vectors
        else:
            raise TypeError("An input is not scalars or vectors")

    def __rsub__(self, scalars_or_vectors):
        if isinstance(scalars_or_vectors, Vector):
            if self.size == scalars_or_vectors.size:
                for elem in range(self.size):
                    self.values[elem] -= scalars_or_vectors.values[elem]
            else:
                raise ValueError("Size of vectors are different respectively")
        elif isinstance(scalars_or_vectors, int) or isinstance(scalars_or_vectors, float):
            for elem in range(self.size):
                self.values[elem] -= scalars_or_vectors
        else:
            raise TypeError("An input is not scalars or vectors")

    def __truediv__(self, scalars):
        if isinstance(scalars, int):
            if scalars != 0:
                for elem in range(self.size):
                    self.values[elem] /= scalars
            else:
                raise ValueError("Can not divided by 0")
        else:
            raise TypeError("An input should be only scalars")

    def __rtruediv__(self, scalars):
        if isinstance(scalars, int):
            if scalars != 0:
                for elem in range(self.size):
                    self.values[elem] = scalars / self.values[elem]
            else:
                raise ValueError("Can not divided by 0")
        else:
            raise TypeError("An input should be only scalars")

    def __mul__(self, scalars_or_vectors):
        if isinstance(scalars_or_vectors, Vector):
            if self.size == scalars_or_vectors.size:
                for elem in range(self.size):
                    self.values[elem] *= scalars_or_vectors.values[elem]
            else:
                raise ValueError("Size of vectors are different respectively")
        elif isinstance(scalars_or_vectors, int) or isinstance(scalars_or_vectors, float):
            for elem in range(self.size):
                self.values[elem] *= scalars_or_vectors
        else:
            raise TypeError("An input is not scalars or vectors")

    def __rmul__(self, scalars_or_vectors):
        if isinstance(scalars_or_vectors, Vector):
            if self.size == scalars_or_vectors.size:
                for elem in range(self.size):
                    self.values[elem] *= scalars_or_vectors.values[elem]
            else:
                raise ValueError("Size of vectors are different respectively")
        elif isinstance(scalars_or_vectors, int) or isinstance(scalars_or_vectors, float):
            for elem in range(self.size):
                self.values[elem] *= scalars_or_vectors
        else:
            raise TypeError("An input is not scalars or vectors")
