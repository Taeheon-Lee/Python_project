import sys

if len(sys.argv) > 1:

    array = sys.argv[1:]
    array = array[len(array)::-1]

    for i in range(len(array)):
        array[i] = array[i].swapcase()
        array[i] = array[i][len(array[i])::-1]

# using enumerate
# for idx, item in enumerate(array):
#     array[idx] = item.swapcase()
#     array[idx] = array[idx][len(item)::-1]

    print(*array)
