import sys

if len(sys.argv) > 1:

    if len(sys.argv) > 2:
        print("ERROR")
        sys.exit()

    if sys.argv[1].isdigit() == False:
        print("ERROR")
        sys.exit()

    num = int(sys.argv[1])
    if (num == 0):
        print("I'm Zero.")
    elif (num % 2 == 0):
        print("I'm Even.")
    elif (num % 2 != 0):
        print("I'm Odd.")
