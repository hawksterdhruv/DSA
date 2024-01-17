"""
Utility funtions for Algorithms
Author : Dhruv Shah
"""
import time


def timer_random(func: callable, args, /, times: int = 100):
    """
    Measures time taken by a function to run times

    Args:
        func (callable): _description_
        args (_type_): _description_
        times (int, optional): _description_. Defaults to 100.
    """
    st_time = time.time()
    for _ in range(times):
        func(*args)
    en_time = time.time()
    print(f"{func.__name__} : {en_time-st_time}")
