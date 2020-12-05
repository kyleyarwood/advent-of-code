from collections import defaultdict
PROBLEM_INPUT = 34000000

def get_lowest_house_with_at_least_n_presents(n):
    houses = [[i, 0] for i in range(1, n//10 + 1)]
    for i in range(1, n//10 + 1):
        for j in range(i, n//10, i):
            houses[j - 1][1] += i*10
    return list(filter(lambda x: x[1] >= n, houses))[0][0]

def part2(n):
    houses = defaultdict(int)

    i = 1
    upper_bound = -1
    while True:
        for j in range(1, 51):
            houses[i*j] += i*11
            if houses[i*j] >= n:
                upper_bound = i*j
                break
        else:
            i += 1
            continue
        i += 1
        break
    
    while i < upper_bound//11 + 1:
        for j in range(1, 51):
            if j >= upper_bound//11 + 1:
                break
            houses[i*j] += i*11
        i += 1

    return min(list(filter(lambda x: houses[x] >= n, houses.keys())))

def main():
    global PROBLEM_INPUT
    #result = get_lowest_house_with_at_least_n_presents(PROBLEM_INPUT)
    #part 1
    #print(result)

    result = part2(PROBLEM_INPUT)
    #part 2
    print(result)


if __name__ == "__main__":
    main()
