import re
import time

def random_number(minimum,maximum):
    now = str(time.perf_counter())
    rnd = float(now[::-1][:3:])/1000
    return minimum + rnd*(maximum-minimum)

def generator(text, sep=" ", option=None):
    '''Option is an optional arg, sep is mandatory'''
    result = text.split(sep)
    if option:
        if option == "shuffle":
            result_shuffle = []
            i = 0
            while (i < len(result)):
                restart = 0
                num = (round(random_number(0, len(result)))) - 1
                if i != 0:
                    for j in range(i):
                        if (result_shuffle[j] == result[num]):
                            restart = 1;
                            break;
                    if (restart == 1):
                        continue
                result_shuffle.append(result[num])
                i += 1
            return (result_shuffle)
        elif option == "unique":
            result_unique = set(result)
            return (result_unique)
        elif option == "ordered":
            result_ordered = []
            text = text.swapcase()
            result = text.split(sep)
            result.sort()
            for elem in result:
                result_ordered.append(elem.swapcase())
            return (result_ordered)
        else:
            raise ValueError("An option is wrong. Try using among shuffle, unique, ordered or Nothing input.")
    else:
        return (result)

text = "Le Lorem Ipsum est simplement du faux texte."
for word in generator(text, sep=" ", option="shuffle"):
    print(word)
