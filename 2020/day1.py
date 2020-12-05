from collections import defaultdict

def product_of_sum_to(a, n):
    seen = set()
    for e in a:
        if n-e in seen:
            return e*(n-e)
        seen.add(e)
    return -1

def product_of_three_sum_to(a, n):
    seen = set()
    pair_sums = defaultdict(int)
    for e in a:
        if n-e in pair_sums:
            a,b = pair_sums[n-e]
            return a*b*e
        for num in seen:
            pair_sum = e + num
            pair_sums[pair_sum] = (e, num)
        seen.add(e)
    return -1

def get_input(filename):
    with open(filename, 'r') as f:
        return list(map(int, f.readlines()))

def main():
    inp = get_input("day1.in")
    N = 2020
    result = product_of_sum_to(inp, N)
    print(result)

    #part 2
    result = product_of_three_sum_to(inp, N)
    print(result)

if __name__ == "__main__":
    main()
