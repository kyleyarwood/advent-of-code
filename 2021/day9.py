from collections import defaultdict

with open('day9.in', 'r') as f:
    data = [x.strip() for x in f.readlines()]
grid = []
for row in data:
    grid.append(list(map(int, list(row))))

def is_low_point(val, i, j):
    ds = [(i, j-1), (i, j+1), (i+1, j), (i-1, j)]
    for x,y in ds:
        if 0 <= x < len(grid) and 0 <= y < len(grid[x]):
            if grid[x][y] <= val:
                return False
    return True
res = 0
for i, row in enumerate(grid):
    for j, val in enumerate(row):
        if is_low_point(val, i, j):
            res += 1+val
print(res)

visited = {}

def dfs(grid):
    def helper(i, j):
        if grid[i][j] == 9:
            return None
        if (i, j) not in visited:
            if is_low_point(grid[i][j], i, j):
                visited[(i, j)] = (i, j)
            m, a, b = grid[i][j], i, j
            for x,y in ((i-1, j), (i+1, j), (i, j-1), (i, j+1)):
                if 0 <= x < len(grid) and 0 <= y < len(grid[x]) and grid[x][y] < m:
                    m = grid[x][y]
                    a,b = x,y
            lowpoint = helper(a,b)
            visited[(i, j)] = lowpoint
        return visited[(i,j)]

    for i,row in enumerate(grid):
        for j,val in enumerate(row):
            helper(i, j)

dfs(grid)

def prod(a):
    res = 1
    for x in a:
        res *= x
    return res

basins = defaultdict(list)
for x,y in visited.keys():
    basins[visited[(x,y)]].append((x,y))
res = prod(sorted([len(basins[x]) for x in basins])[-3:])
print(res)
