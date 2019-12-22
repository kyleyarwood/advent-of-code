PROBLEM_INPUT = 34000000

def get_lowest_house_with_at_least_n_presents(n):
    houses = [[i, 0] for i in range(1, n//10 + 1)]
    for i in range(1, n//10 + 1):
        for j in range(i, n//10, i):
            houses[j - 1][1] += i*10
    return list(filter(lambda x: x[1] >= n, houses))[0][0]


def main():
    global PROBLEM_INPUT
    result = get_lowest_house_with_at_least_n_presents(PROBLEM_INPUT)
    #part 1
    print(result)


if __name__ == "__main__":
    main()
