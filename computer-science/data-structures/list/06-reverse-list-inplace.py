from typing import Any, List


def reverse(lyst: List[Any]):
    s = 0
    e = len(lyst)-1

    while s < e:
        lyst[s], lyst[e] = lyst[e], lyst[s]
        s += 1
        e -= 1


list_1 = [10, 20, 30, 40]
list_2 = ["geeks", "ide", "courses"]

reverse(list_1)
reverse(list_2)

assert list_1 == [40, 30, 20, 10]
assert list_2 == ["courses", "ide", "geeks"]
