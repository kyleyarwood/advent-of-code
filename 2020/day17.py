from collections import defaultdict
from file_lines import get_file_lines

lines = get_file_lines('day17.in')

grid = defaultdict(int)
four_d_grid = defaultdict(int)

plane=plane1=plane2=0
for i,line in enumerate(lines):
    for j,c in enumerate(line):
        if c=='#':
            grid[(i,j,plane)] = 1
            four_d_grid[(i,j,plane1,plane2)] = 1

def active_neighbours(grid, x, y, z, w=None):
    result = 0
    #print(w)
    for i in range(x-1,x+2):
        for j in range(y-1,y+2):
            for k in range(z-1,z+2):
                if w is None:
                    if (i!=x or j!=y or k!=z) and grid[(i,j,k)] == 1:
                        result += 1
                    continue
                for m in range(w-1,w+2):
                    if (i!=x or j!=y or k!=z or m!=w) and grid[(i,j,k,m)] == 1:
                        #print('hello')
                        result += 1
    return result

def simulate_cycle(grid, four_d=False):
    min_ds = []
    max_ds = []
    for i in range(3+four_d):
        min_ds.append(min(grid.keys(), key=lambda x: x[i])[i])
        max_ds.append(max(grid.keys(), key=lambda x: x[i])[i])
    new_grid = defaultdict(int)
    for x in range(min_ds[0]-1, max_ds[0]+2):
        for y in range(min_ds[1]-1, max_ds[1]+2):
            for z in range(min_ds[2]-1, max_ds[2]+2):
                if four_d:
                    for w in range(min_ds[3]-1, max_ds[3]+2):
                        num_active_neighbours = active_neighbours(grid,x,y,z,w)
                        if grid[(x,y,z,w)] == 1 and num_active_neighbours in (2,3):
                            new_grid[(x,y,z,w)] = 1
                        elif grid[(x,y,z,w)] == 0 and num_active_neighbours == 3:
                            new_grid[(x,y,z,w)] = 1
                    continue
                num_active_neighbours = active_neighbours(grid,x,y,z)
                if grid[(x,y,z)]==1 and num_active_neighbours not in (2,3):
                    new_grid[(x,y,z)] = 0
                elif grid[(x,y,z)]==1:
                    new_grid[(x,y,z)] = 1
                elif num_active_neighbours == 3:
                    new_grid[(x,y,z)] = 1
                else:
                    new_grid[(x,y,z)] = 0
    return new_grid

def total_active_cells(grid):
    return sum(grid.values())
    
for i in range(6):
    grid = simulate_cycle(grid)
    four_d_grid = simulate_cycle(four_d_grid, True)

print(total_active_cells(grid))
print(total_active_cells(four_d_grid))
