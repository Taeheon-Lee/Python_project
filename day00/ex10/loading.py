import sys
import time

start_time = time.perf_counter()

def ft_progress(my_list, elem):
    size = len(my_list)
    end_time = time.perf_counter()
    if (elem == 0):
        print("ETA: Calculated", end=" ")
    else:
        sys.stdout.write("\033[F")
        eta = round(((size * (end_time - start_time)) / elem), 2)
        print(f"ETA: {eta}s", end=" ")
    elem += 1
    percent = round(((elem / size) * 100), 0)
    if (percent < 10):
        print(f"[  {int(percent)}%]", end="")
    elif (percent < 100):
        print(f"[ {int(percent)}%]", end="")
    else:
        print(f"[{int(percent)}%]", end="")
    cnt_mark = int(round((percent / 5), 0))
    print("[", end="")
    for j in range(cnt_mark):
        print("=", end="")
    if not (cnt_mark == 20):
        print(">", end="")
    for k in range(20 - cnt_mark):
        print(" ", end="")
    print(f"] {elem}/{size} | elapsed time {round((end_time - start_time), 2)}s")

listy = range(3333)
ret = 0
for elem in listy:
    ft_progress(listy, elem)
    ret += elem
    time.sleep(0.005)
print()
print(ret)
