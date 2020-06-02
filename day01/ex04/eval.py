class Evaluator:
    @staticmethod
    def zip_evaluate(coefs, words):
        if not isinstance(words, list):
            raise TypeError("Words should be list.")
        for elem in words:
            if not isinstance(elem, str):
                raise ValueError("Elements of list should be string")
        if not isinstance(coefs, list):
            raise TypeError("Words should be list.")
        for elem in coefs:
            if not isinstance(elem, float):
                raise ValueError("Elements of list should be float")
        if not len(words) == len(coefs):
            print(-1)
        else:
            count = 0
            for x, y in zip(coefs, words):
                count += x * len(y)
            print(count)

    @staticmethod
    def enumerate_evaluate(coefs, words):
        if not isinstance(words, list):
            raise TypeError("Words should be list.")
        for elem in words:
            if not isinstance(elem, str):
                raise ValueError("Elements of list should be string")
        if not isinstance(coefs, list):
            raise TypeError("Words should be list.")
        for elem in coefs:
            if not isinstance(elem, float):
                raise ValueError("Elements of list should be float")
        if not len(words) == len(coefs):
            print(-1)
        else:
            count = 0
            for x, y in enumerate(words):
                count += coefs[x] * len(y)
            print(count)
