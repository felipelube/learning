from typing import List


def items_average(lyst: List[int]):
    n = len(lyst)
    if n == 0:
        return 0
    return sum(lyst) / n


assert(items_average([10, 20, 30, 40]) == 25.0)
assert("{0:.4g}".format(items_average([30, 60, 40])) == "43.33")
assert(items_average([]) == 0)
