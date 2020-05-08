import sys

if len(sys.argv) < 3 or len(sys.argv) > 3 or \
    sys.argv[1].isdigit() == False or sys.argv[2].isdigit() == False:
    if len(sys.argv) < 3:
        pass
    elif len(sys.argv) > 3:
        print("InputError: too many arguments\n")
    elif sys.argv[1].isdigit() == False or sys.argv[2].isdigit() == False:
        print("InputError: only numbers\n")
    print("Usage: python operations.py <number1> <number2>")
    print("""Example:
    python operations.py 10 3""")
else:
    s = int(sys.argv[1]) + int(sys.argv[2])
    d = abs(int(sys.argv[1]) - int(sys.argv[2]))
    p = int(sys.argv[1]) * int(sys.argv[2])
    if sys.argv[2] == '0':
        q = "ERROR (div by zero)"
    else:
        q = int(sys.argv[1]) / int(sys.argv[2])
    if sys.argv[2] == '0':
        r = "ERROR (modulo by zero)"
    else:
        r = int(sys.argv[1]) % int(sys.argv[2])

    print("sum:        ", s)
    print("Difference: ", d)
    print("Product:    ", p)
    print("Quotient:   ", q)
    print("Remainder:  ", r)
