def in_bounds(light_configurations, row, col):
    return 0 <= row < len(light_configurations) and 0 <= col < len(light_configurations[row])

def get_num_neighbours_on(light_configurations, row, col):
    num_neighbours_on = 0

    for i in range(row - 1, row + 2):
        for j in range(col - 1, col + 2):
            if i == row and j == col:
                continue
            elif in_bounds(light_configurations, i, j) and light_configurations[i][j] in (1, -1):
                num_neighbours_on += 1

    return num_neighbours_on

def try_to_turn_on(light_configurations, row, col):
    num_neighbours_on = get_num_neighbours_on(light_configurations, row, col)

    if num_neighbours_on == 3:
        light_configurations[row][col] = 2

def try_to_turn_off(light_configurations, row, col):
    num_neighbours_on = get_num_neighbours_on(light_configurations, row, col)

    if num_neighbours_on < 2 or num_neighbours_on > 3:
        light_configurations[row][col] = -1

def clean_up(light_configurations):
    for row in range(len(light_configurations)):
        for col in range(len(light_configurations[row])):
            if light_configurations[row][col] == 2:
                light_configurations[row][col] -= 1
            elif light_configurations[row][col] == -1:
                light_configurations[row][col] += 1

def not_in_corner(light_configurations, row, col):
    return not ((row == 0 or row == len(light_configurations) - 1) and (col == 0 or col == len(light_configurations[row]) - 1))

def light_configuration_step(light_configurations, four_corners):
    for row in range(len(light_configurations)):
        for col in range(len(light_configurations[row])):
            if light_configurations[row][col] == 1 and (not four_corners or not_in_corner(light_configurations, row, col)):
                try_to_turn_off(light_configurations, row, col)
            elif light_configurations[row][col] == 0:
                try_to_turn_on(light_configurations, row, col)

    clean_up(light_configurations)

def light_configuration_steps(light_configurations, steps, four_corners = False):
    if steps == 0:
        return

    light_configuration_step(light_configurations, four_corners)

    light_configuration_steps(light_configurations, steps - 1, four_corners)
    
def get_num_on_lights(light_configurations):
    return sum([sum(row) for row in light_configurations])

def get_light_configurations(filename):
    with open(filename, 'r') as f:
        return f.readlines()

def main():
    light_configurations = get_light_configurations("day18input.txt")
    light_configurations = [[1 if light == "#" else 0 for light in row.replace('\n', '')] for row in light_configurations]
    light_configurations_part2 = [[light for light in row] for row in light_configurations]
    light_configuration_steps(light_configurations, 100)
    result = get_num_on_lights(light_configurations)
    #part 1
    print(result)

    light_configuration_steps(light_configurations_part2, 100, True)
    result = get_num_on_lights(light_configurations_part2)
    #part 2
    print(result)


if __name__ == "__main__":
    main()
