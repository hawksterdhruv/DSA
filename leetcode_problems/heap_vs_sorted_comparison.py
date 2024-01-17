"""
comparison between python heap sort and regular sorting.
"""
import heapq
import random

from commons.utils import timer_random


def heap_sort(array: list):
    """
    Heap sorts an array

    Args:
        array (list): _description_
    """
    op = []
    for a in array:
        heapq.heappush(op, a)


def regular_sort(array: list):
    """
    Default python sorting for an array

    Args:
        array (list): _description_
    """
    _ = sorted(array)


input_array = [random.random() for a in range(10000)]


timer_random(heap_sort, (input_array,), times=2000)
timer_random(regular_sort, (input_array,), times=2000)
