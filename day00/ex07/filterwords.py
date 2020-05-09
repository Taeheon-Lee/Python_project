import sys
import string

if len(sys.argv) != 3:
    print("ERROR")
elif sys.argv[1].isdigit():
    print("ERROR")
else:
    lst = list(sys.argv[1].split())
    result = []
    for s in lst:
        if len(s) > int(sys.argv[2]):
            result.append(s)
    for i in range(len(result)):
        result[i] = result[i].translate(str.maketrans("", "", string.punctuation))
        #Third prameter of maketrans is for setting char to ignore
    print(result)
