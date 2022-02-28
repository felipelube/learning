def sum_of(n: int):
    s = 0
    for i in range(n+1):
        s += i
    return s


assert(sum_of(3) == 6)
assert(sum_of(5) == 15)
