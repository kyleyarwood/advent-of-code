from file_lines import get_file_lines

seat_map = [list(s) for s in get_file_lines('day11.in')]
original_seat_map = [[x for x in row] for row in seat_map]

def num_adjacent(seat_map, i, j):
    result = 0
    for x in range(max(0, i-1), min(len(seat_map), i+2)):
        for y in range(max(0, j-1), min(len(seat_map[i]),j+2)):
            if x == i and y == j:
                continue
            result += seat_map[x][y]=='#'
    return result

def simulate_round(seat_map):
    new_seat_map = []
    any_changes = False
    for i,row in enumerate(seat_map):
        new_row = []
        for j,cell in enumerate(row):
            if cell == 'L' and num_adjacent(seat_map, i, j)==0:
                any_changes = True
                new_row.append('#')
            elif cell == '#' and num_adjacent(seat_map, i, j)>=4:
                any_changes = True
                new_row.append('L')
            else:
                new_row.append(cell)
        new_seat_map.append(new_row)
    return new_seat_map, any_changes

def num_can_see(seat_map, i, j):
    directions = [(1,0),(1,-1),(0,-1),(-1,-1),(-1,0),(-1,1),(0,1),(1,1)]
    result = 0
    for dx,dy in directions:
        x,y = i+dx,j+dy
        while 0 <= x < len(seat_map) and 0 <= y < len(seat_map[x]):
            if seat_map[x][y] == '#':
                result += 1
                break
            elif seat_map[x][y] == 'L':
                break
            x += dx
            y += dy
    return result

def simulate_new_round(seat_map):
    new_seat_map = []
    any_changes = False
    for i,row in enumerate(seat_map):
        new_row = []
        for j,cell in enumerate(row):
            if cell=='#' and num_can_see(seat_map, i, j)>=5:
                any_changes = True
                new_row.append('L')
            elif cell=='L' and num_can_see(seat_map, i, j)==0:
                any_changes = True
                new_row.append('#')
            else:
                new_row.append(cell)
        new_seat_map.append(new_row)
    return new_seat_map, any_changes


def num_occupied(seat_map):
    return sum(sum(x=='#' for x in row) for row in seat_map)

any_changes = True
while any_changes:
    seat_map, any_changes = simulate_round(seat_map)

result = num_occupied(seat_map)
print(result)

def print_seat_map(seat_map):
    print('\n'.join(''.join(row) for row in seat_map))
    print()

any_changes = True
seat_map = [[x for x in row] for row in original_seat_map]
while any_changes:
    seat_map, any_changes = simulate_new_round(seat_map)


result = num_occupied(seat_map)
print(result)
