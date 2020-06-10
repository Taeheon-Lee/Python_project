import time
from random import randint
import logging
import functools

def log(func):
    @functools.wraps(func)
    def wrapper(*args, **kargs):
        start_time = time.perf_counter()
        value = func(*args, **kargs)
        end_time = time.perf_counter()
        run_time = end_time - start_time
        if run_time < 1.0:
            run_time *= 1000
            logger.info(f"{func.__name__.title().replace('_', ' ')}\t[ exec-time =  {run_time:.3f} ms ]")
        else:
            logger.info(f"{func.__name__.title().replace('_', ' ')}\t[ exec-time =  {run_time:.3f} s ]")
        return (value)
    return wrapper

class CoffeeMachine():

    water_level = 100

    @log
    def start_machine(self):
        if self.water_level > 20:
            return True
        else:
            print("Please add water")
            return False

    @log
    def boil_water(self):
        return "boiling..."

    @log
    def make_coffee(self):
        if self.start_machine():
            for _ in range(20):
                time.sleep(0.1)
                self.water_level -= 1
            print(self.boil_water())
            print("Coffee is ready!")

    @log
    def add_water(self, water_level):
        time.sleep(randint(1, 5))
        self.water_level += water_level
        print("Blub blub blub...")

if __name__ == "__main__":
    logger = logging.getLogger("cmaxime")
    logger.setLevel(logging.DEBUG)
    formatter = logging.Formatter('(%(name)s)Running: %(message)s')
    file_handler = logging.FileHandler('machine.log')
    file_handler.setLevel(logging.DEBUG)
    file_handler.setFormatter(formatter)
    logger.addHandler(file_handler)

    machine = CoffeeMachine()
    for i in range(0, 5):
        machine.make_coffee()
    machine.make_coffee()
    machine.add_water(70)
