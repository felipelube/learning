from typing import Any, List


def get_reverse(lyst: List[Any]):
    if len(lyst) <= 1:
        return lyst

    reverse = []
    i = len(lyst) - 1
    while i >= 0:
        reverse.append(lyst[i])
        i -= 1

    return reverse


assert get_reverse([10, 20, 30, 40]) == [40, 30, 20, 10]
assert get_reverse(["geeks", "ide", "courses"]) == ["courses", "ide", "geeks"]
