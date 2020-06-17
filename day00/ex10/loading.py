import sys
import time

start_time = time.perf_counter()

def ft_progress(my_list, elem):
    size = len(my_list)
    end_time = time.perf_counter()
    if (elem == 0):
        print("ETA: Calculated [", end="")
    else:
        sys.stdout.write('\x1b[1A')
        sys.stdout.write('\x1b[2K')
        eta = round(((size * (end_time - start_time)) / elem), 2)
        print("ETA: %.2fs [" % (eta), end="")
    elem += 1
    percent = int(((elem / size) * 100))
    percent_digit = len(str(percent))
    i = 0
    while i < (3 - percent_digit):
        print(" ", end="")
        i += 1
    print(f"{int(percent)}%]", end="")
    num_mark = int(round((percent / 5), 0))
    print("[", end="")
    i = 0
    while i < num_mark:
        print("=", end="")
        i += 1
    if not (num_mark == 20):
        print(">", end="")
        num_mark += 1
    i = 0
    while i < (20 - num_mark):
        print(" ", end="")
        i += 1
    print("] %d/%d | elapsed time %.2fs" % (elem, size, round((end_time - start_time), 2)))

listy = range(3333)
ret = 0
for elem in listy:
    ft_progress(listy, elem)
    ret += elem
    time.sleep(0.005)
print()
print(ret)
