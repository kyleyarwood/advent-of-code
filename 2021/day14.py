from collections import defaultdict, Counter

with open('day14.in') as f:
    data = [x.strip() for x in f.readlines()]

start = data[0]

prod_rules = {}
for line in data[2:]:
    x,y = line.split(' -> ')
    prod_rules[x] = y

def after_n_steps(s, prod_rules, n):
    #dp is (2 character string, n) -> Counter
    dp = defaultdict(int)
    for x in prod_rules:
        dp[(x, 0)] = Counter(x)
    for i in range(1, n+1):
        for x in prod_rules:
            dp[(x, i)] = dp[(x[0] + prod_rules[x], i-1)] + dp[(prod_rules[x] + x[1], i-1)]
            dp[(x, i)][prod_rules[x]] -= 1
    result = Counter([])
    for i in range(len(s)-1):
        result += dp[(s[i:i+2], n)]
        if i != 0:
            result[s[i]] -= 1
    return result

for i,n in enumerate((10, 40)):
    counter = after_n_steps(start, prod_rules, n=n)
    res = max(counter.values()) - min(counter.values())
    print(f"Part {i+1}: {res}")