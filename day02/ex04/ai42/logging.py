import time
import logging
import functools

def log(func):
    @functools.wraps(func)
    def wrapper(*args, **kargs):
        start_time = time.perf_counter()
        value = func(*args, **kargs)
        end_time = time.perf_counter()
        run_time = end_time - start_time
        f = open('log.txt', 'a+')
        if run_time < 1.0:
            run_time *= 1000
            f.write(f"{func.__name__.title().replace('_', ' ')}\t[ exec-time =  {run_time:.3f} ms ]")
        else:
            f.write(f"{func.__name__.title().replace('_', ' ')}\t[ exec-time =  {run_time:.3f} s ]")
        f.close()
        return (value)
    return wrapper
