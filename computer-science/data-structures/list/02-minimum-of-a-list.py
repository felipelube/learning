from typing import List


def list_minimums(lyst: List[int], x: int):
    return [n for n in lyst if n < x]


assert list_minimums([8, 100, 20, 40, 3, 7], 10) == [8, 3, 7]
assert list_minimums([100, 20, 40, 60, 80, 200], 60) == [20, 40]
assert list_minimums([], 10) == []
