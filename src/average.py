from typing import List


def find_average(numbers: List[int]) -> float:
    # raise NotImplementedError
    numbers_sum = sum(numbers)
    divisor = len(numbers)
    return numbers_sum / divisor
