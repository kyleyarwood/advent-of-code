def product_of_sum_to(a, n):
    seen = set()
    for e in a:
        if n-e in seen:
            return e*(n-e)
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

if __name__ == "__main__":
    main()
