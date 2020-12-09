from file_lines import get_file_lines

lines = get_file_lines('day3.in')

def is_valid_triangle(a,b,c):
    return a+b>c and a+c>b and b+c>a

grid = [list(map(int, line.split())) for line in lines]

num_valid_triangles = sum(is_valid_triangle(a,b,c) for a,b,c in grid)
print(num_valid_triangles)    

new_num_valid_triangles = 0
for i in range(0, len(grid), 3):
    for j in range(len(grid[i])):
        new_num_valid_triangles += is_valid_triangle(
            grid[i][j], grid[i+1][j], grid[i+2][j])
print(new_num_valid_triangles)
