from typing import List


def find_only_odd(lyst: List[int]):
    res = 0
    for item in lyst:
        res = item ^ res
    return res


assert find_only_odd([10, 30, 30, 10, 30, 30, 20]) == 20
assert find_only_odd([10, 10, 10, 10, 10, 20, 20]) == 10
assert find_only_odd([10, 10, 20, 30, 30, 20, 40]) == 40
assert find_only_odd([10]) == 10
assert find_only_odd([1, 1, 0, 1, 0, 1, 1]) == 1
