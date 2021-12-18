from math import sqrt, ceil

with open('day17.in', 'r') as f:
    data = f.read().strip()

xs, ys = data.split(', ')
xs = xs[13:]

x_lo,x_hi = map(int, (xs.split('=')[1]).split('..'))
y_lo,y_hi = map(int, (ys.split('=')[1]).split('..'))

x_iters = {}
for x in range(ceil(sqrt(x_lo)), x_hi+1):
    iters = 0
    x_posn = 0
    dx = x
    min_iter = max_iter = -1
    while x_posn <= x_hi:
        if x_posn >= x_lo:
            max_iter = iters
            if min_iter == -1:
                min_iter = iters
        iters += 1
        x_posn += dx
        dx -= 1
        if dx==-1:
            break
    if x_lo <= x_posn <= x_hi:
        max_iter = float('inf')
    if min_iter != -1:
        x_iters[x] = (min_iter, max_iter)

y_iters = {}
for y in range(y_lo, -y_lo):
    iters = 0
    y_posn = 0
    dy = y
    min_iter = max_iter = -1
    if dy > 0:
        iters = abs(y)*2 + 1
        dy = -dy - 1
    while y_posn >= y_lo:
        if y_posn <= y_hi:
            max_iter = iters
            if min_iter == -1:
                min_iter = iters
        iters += 1
        y_posn += dy
        dy -= 1
    if min_iter != -1:
        y_iters[y] = (min_iter, max_iter)

res = max(e for e in y_iters.keys() if y_iters[e][0] != -1)
res = (res*(res+1))//2
print(f"Part 1: {res}")

res = 0
for y in y_iters:
    ys, ye = y_iters[y]
    for x in x_iters:
        xs, xe = x_iters[x]
        s = max(xs, ys)
        e = min(xe, ye)
        res += (s <= e)
print(f"Part 2: {res}")