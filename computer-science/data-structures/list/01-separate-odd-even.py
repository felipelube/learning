from typing import Dict, List


def separate_odd_even(lyst: List[int]) -> Dict[str, List[int]]:
    return {
        'even': [n for n in lyst if n % 2 == 0],
        'odds': [n for n in lyst if n % 2 != 0]
    }
