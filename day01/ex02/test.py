from vector import Vector

try:
    print("----------Case: a = Vector([1, 2, 3, 4])-----------")
    a = Vector([5, 10, 15, 20])
except ValueError as error:
    print("ValueError: ", error, "\n")
    print("----------Case: a = Vector([1.0, 2.0, 3.0, 4.0])----------")
    a = Vector([5.0, 10.0, 15.0, 20.0])
    print("a =",a.__dict__, "\n")
    print("----------Case: a = Vector(5)----------")
    a = Vector(5)
    print("a =",a.__dict__, "\n")
    print("----------Case: a = Vector((1, 6))----------")
    a = Vector((1, 6))
    print("a =", a.__dict__, "\n")
    print("----------set a = Vector([5.0, 10.0, 15.0, 20.0]), b = Vector([25.0, 30.0, 35.0])----------")
    a = Vector([5.0, 10.0, 15.0, 20.0])
    b = Vector([25.0, 30.0, 35.0])
    print("a =", a.__dict__, "\nb =", b.__dict__, "\n")
    try:
        print("----------Case: a + b----------")
        a + b
    except ValueError as error:
        print("ValueError: ", error), "\n"
        print("----------set a = Vector([5.0, 10.0, 15.0, 20.0]), b = Vector([25.0, 30.0, 35.0, 40])----------")
        b = Vector([25.0, 30.0, 35.0, 40.0])
        print("a =", a.__dict__, "\nb =", b.__dict__, "\n")
        print("----------Case: a + b----------")
        a + b
        print("a =", a.__dict__, "\n")
        print("----------Case: a + 5----------")
        a + 5
        print("a =", a.__dict__, "\n")
        print("----------Case: 5 + a----------")
        5 + a
        print("a =", a.__dict__, "\n")
        print("a =", a.__dict__, "\nb =", b.__dict__, "\n")
        print("----------Case: a - b----------")
        a - b
        print("a =", a.__dict__, "\n")
        print("----------Case: a - 5----------")
        a - 5
        print("a =", a.__dict__, "\n")
        print("----------Case: 5 - a----------")
        5 - a
        print("a =", a.__dict__, "\n")
        print("a =", a.__dict__, "\nb =", b.__dict__, "\n")
        print("----------Case: a * b----------")
        a * b
        print("a =", a.__dict__, "\n")
        print("----------Case: a * 2----------")
        a * 2
        print("a =", a.__dict__, "\n")
        print("----------Case: 2 * a----------")
        2 * a
        print("a =", a.__dict__, "\n")
        print("a =", a.__dict__, "\nb =", b.__dict__, "\n")
        print("----------Case: a / 100----------")
        a / 100
        print("a =", a.__dict__, "\n")
        print("----------Case: 1000 / a----------")
        1000 / a
        print("a =", a.__dict__, "\n")
        try:
            print("----------Case: a / b----------")
            a / b
        except TypeError as error:
            print("TypeError: ", error)
