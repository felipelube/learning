from typing import List


def second_largest(lyst: List[int]):
    if len(lyst) == 0:
        return None

    largest = lyst[0]
    second_largest = None
    for n in lyst[1:]:
        if n > largest:
            largest, second_largest = n, largest
        elif n != largest:
            if second_largest is None:
                second_largest = n
            elif n > second_largest:
                second_largest = n

    return second_largest


assert second_largest([10, 5, 8, 20]) == 10
assert second_largest([20, 10, 20, 8, 12]) == 12
assert second_largest([10, 10, 10]) == None
