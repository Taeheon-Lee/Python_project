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
    for i in range(3 - percent_digit):
        print(" ", end="")
    print(f"{int(percent)}%]", end="")
    num_mark = int(round((percent / 5), 0))
    print("[", end="")
    for j in range(num_mark):
        print("=", end="")
    if not (num_mark == 20):
        print(">", end="")
        num_mark += 1
    for k in range(20 - num_mark):
        print(" ", end="")
    print("] %d/%d | elapsed time %.2fs" % (elem, size, round((end_time - start_time), 2)))

listy = range(3333)
ret = 0
for elem in listy:
    ft_progress(listy, elem)
    ret += elem
    time.sleep(0.005)
print()
print(ret)
