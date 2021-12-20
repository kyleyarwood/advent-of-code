with open('day20.in', 'r') as f:
    data = [x.strip() for x in f.readlines()]

mapping = data[0]
grid = []
for line in data[2:]:
    grid.append([int(x=='#') for x in line])
n = 3

def get_pixel_value(grid, i, j, out_of_bounds):
    binary = []
    for x in range(i-1, i+2):
        for y in range(j-1, j+2):
            if 0 <= x < len(grid) and 0 <= y < len(grid[x]):
                binary.append(grid[x][y])
            else:
                binary.append(out_of_bounds)
    return 1 if mapping[int('0' + ''.join(map(str, binary)), 2)] == '#' else 0

def get_how_many_lit(grid, iterations=2):
    grid = [row[::] for row in grid]
    out_of_bounds = 0
    for i in range(iterations):
        new_grid = []
        for i in range(-1, len(grid)+1):
            new_row = []
            for j in range(-1, len(grid[0])+1):
                new_row.append(get_pixel_value(grid, i, j, out_of_bounds))
            new_grid.append(new_row)
        out_of_bounds = get_pixel_value(grid, -2, -2, out_of_bounds)
        grid = new_grid
    return sum(sum(row) for row in grid)

result = get_how_many_lit(grid)
print(f"Part 1: {result}")

result = get_how_many_lit(grid, iterations=50)
print(f"Part 2: {result}")
