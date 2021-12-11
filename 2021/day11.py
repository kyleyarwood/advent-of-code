with open('day11.in', 'r') as f:
    grid = [list(map(int, x.strip())) for x in f.readlines()]

#print('\n'.join(map(str, grid)))

def in_bounds(grid, i, j):
    return 0 <= i < len(grid) and 0 <= j < len(grid[i])

def simulate_step(grid):
    critical_val = 9
    tens = []
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            grid[i][j] += 1
            if grid[i][j] > critical_val:
                tens.append((i,j))
    while tens:
        new_tens = []
        for x,y in tens:
            for i in range(x-1, x+2):
                for j in range(y-1, y+2):
                    if i==x and j==y or not in_bounds(grid, i, j) or grid[i][j] > critical_val:
                        continue
                    grid[i][j] += 1
                    if grid[i][j] > critical_val:
                        new_tens.append((i,j))
        tens = new_tens
    res = 0
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if grid[i][j] > critical_val:
                res += 1
                grid[i][j] = 0
    return res
    
res = 0
steps = 100
for i in range(steps):
    x = simulate_step(grid)
    #print(i+1, x)
    res += x
print(f"Part 1: {res}")

while True:
    steps += 1
    x = simulate_step(grid)
    if x == len(grid)*len(grid[0]):
        break
print(f"Part 2: {steps}")

