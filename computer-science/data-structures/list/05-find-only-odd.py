from collections import Counter
from typing import List


def find_only_odd(lyst: List[int]):
    c = Counter(lyst)
    return [item[0] for item in c.items() if item[1] % 2 != 0][0]


assert find_only_odd([10, 30, 30, 10, 30, 30, 20]) == 20
assert find_only_odd([10, 10, 10, 10, 10, 20, 20]) == 10
assert find_only_odd([10, 10, 20, 30, 30, 20, 40]) == 40
assert find_only_odd([10]) == 10
