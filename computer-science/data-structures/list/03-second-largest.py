from typing import List


def second_largest(lyst: List[int]):
    if len(lyst) == 0:
        return None

    largest = None
    second_largest = None
    for n in lyst:
        if largest is None:
            largest = n
        elif n > largest:
            second_largest, largest = largest, n
        elif second_largest is not None and n < largest and n > second_largest:
            second_largest = n
        elif second_largest is None and n < largest:
            second_largest = n

    return second_largest


assert second_largest([10, 5, 8, 20]) == 10
assert second_largest([20, 10, 20, 8, 12]) == 12
assert second_largest([10, 10, 10]) == None
