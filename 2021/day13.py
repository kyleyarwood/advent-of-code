with open('day13.in', 'r') as f:
    data = [x.strip() for x in f.readlines()]

coords, folds = [], []
x_size = y_size = -1
is_coords = True
for line in data:
    if not line:
        is_coords = False
        continue
    if is_coords:
        x,y = map(int, line.split(','))
        x_size, y_size = max(x_size, x), max(y_size, y)
        coords.append((x, y))
    else:
        folds.append(line.split('='))

grid = [[False for j in range(x_size+1)] for i in range(y_size+1)]

for x,y in coords:
    grid[y][x] = True

def print_grid(grid):
    print('\n'.join(''.join('#' if x else '-' for x in row) for row in grid))

printed_res = False
for axis,value in folds:
    edge = int(value)
    if axis[-1] == 'y':
        new_grid = [[False for j in range(len(grid[0]))] for i in range(max(edge, len(grid)-1-edge))] 
        for i,row in enumerate(grid):
            if i==edge:
                continue
            for j,val in enumerate(row):
                new_grid[-abs(i-edge)][j] = new_grid[-abs(i-edge)][j] or val
    else:
        new_grid = [[False for j in range(max(edge, len(grid[0])-1-edge))] for i in range(len(grid))]
        for i,row in enumerate(grid):
            for j,val in enumerate(row):
                if j==edge:
                    continue
                new_grid[i][-abs(j-edge)] = new_grid[i][-abs(j-edge)] or val
    grid = new_grid
    if not printed_res:
        print(sum(sum(row) for row in grid))
        printed_res = True
            
print_grid(grid)
