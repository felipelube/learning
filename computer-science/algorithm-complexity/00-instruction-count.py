# LAMBERT, Kenneth. Fundamentals of Python: Data Structures. Cengage learning, 2019. p. 55

def calc_iterations(problemSize: int) -> int:
    iteractions = 0
    while problemSize > 0:
        problemSize = problemSize // 2
        iteractions += 1
    return iteractions


if __name__ == '__main__':
    problemSize = int(input("Type the problem size: "))

    print("\nIncrease by deduplicating the problem size")
    last_v = 0
    v = 0
    for i in range(100):
        last_v, v = v, calc_iterations(problemSize * 10 ** i)
        print("{} increased by {} from {}".format(v, v-last_v, last_v))

    print("\nIncrease by doubling the problem size")
    last_v = 0
    v = 0
    for o in range(100):
        last_v, v = v, calc_iterations(problemSize * 2 ** o)
        print("{} increased by {} from {}".format(v, v-last_v, last_v))
