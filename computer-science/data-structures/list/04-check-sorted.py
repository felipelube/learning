from typing import List


def check_sorted(lyst: List[int]):
    if len(lyst) <= 1:
        return True

    for i, item in enumerate(lyst):
        if i+1 < len(lyst) and lyst[i+1] < item:
            break
    else:
        return True
    return False


assert check_sorted([10, 20, 30]) == True
assert check_sorted([10, 20, 20, 30]) == True
assert check_sorted([10, 5, 2]) == False
assert check_sorted([10]) == True
assert check_sorted([]) == True
assert check_sorted([10, 5, 30]) == False
assert check_sorted([30, 20, 10]) == False
