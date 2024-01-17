""" Implementation of Biary Search """

import logging

from typing import Any

logger = logging.getLogger(__name__)


def binary_search(target: list[Any], key: Any) -> (int | None, bool):
    """
    Returns (index of key, True) in target if the element is found
    or the (index of element immediately greater than key, False) if key is not found in target

    Args:
        target (list[Any]): _description_
        key (Any): _description_

    Returns:
        (int | None, bool): _description_
    """
    n = len(target)
    if n == 0:
        return 0, False
    low = 0
    high = n - 1
    while low <= high:
        mid = (high + low) // 2
        if key == target[mid]:
            return mid, True
        elif key > target[mid]:
            low = mid + 1
        else:
            high = mid - 1
        logger.debug(
            "mid = %s, low = %s, high = %s, List[mid] = %s", mid, low, high, target[mid]
        )
    return low, False


if __name__ == "__main__":
    key = 51
    input_array = list(range(0, 98, 2))
    logger.info("Input-Target : %s", input_array)
    logger.info("Input-Key : %s", key)
    logger.info("Output : %s", binary_search(input_array, key))
