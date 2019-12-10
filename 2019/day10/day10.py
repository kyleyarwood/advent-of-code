from fractions import Fraction
def get_file_lines(filename):
    with open(filename, 'r') as f:
        return f.readlines()

def get_asteroids(file_lines):
    asteroids = set()
    for x in range(len(file_lines)):
        for y in range(len(file_lines[x])):
            if file_lines[x][y] == '#':
                asteroids.add((x, y))
    return asteroids

def get_line_of_sight(asteroid1, asteroid2):
    if asteroid1[1] - asteroid2[1] == 0:
        return ("n/a", asteroid1[0] > asteroid2[0])
    return (Fraction(asteroid1[0] - asteroid2[0], asteroid1[1] - asteroid2[1]), asteroid1[0] > asteroid2[0])

def add_to_dict(d, key, value):
    if key not in d:
        d[key] = []
    d[key].append(value)

def get_all_lines_of_sight(my_asteroid, asteroids):
    lines_of_sight = {}
    for asteroid in asteroids:
        if asteroid[1] - asteroid2[1] == 0:
            lines_of_sight[("n/a", asteroid1[0] > asteroid2[0])] = asteroid
            continue
        add_to_dict(lines_of_sight, (Fraction(my_asteroid[0] - asteroid[0], my_asteroid[1] - asteroid[1]), my_asteroid[0] > asteroid[0]), asteroid)
    return lines_of_sight
        

def get_num_in_line_of_sight(my_asteroid, asteroids):
    lines_of_sight = set()
    for asteroid in asteroids:
        if asteroid == my_asteroid:
            continue
        line_of_sight = get_line_of_sight(my_asteroid, asteroid)
        if line_of_sight not in lines_of_sight:
            lines_of_sight.add(line_of_sight)
    return len(lines_of_sight) + 1

def get_where_200th_destroyed(asteroid, asteroids):
    lines_of_sight = get_all_lines_of_sight(asteroid, asteroids)

def get_result(asteroids):
    result = 0
    asteroid_coords = (0, 0)
    for asteroid in asteroids:
        num = get_num_in_line_of_sight(asteroid, asteroids)
        if num > result:
            asteroid_coords = asteroid
        result = max(result, num)
    return asteroid_coords, result

def part2(asteroid, asteroids):
    return get_where_200th_destroyed(asteroids)

def main():
    file_lines = get_file_lines("test.in")
    asteroids = get_asteroids(file_lines)
    asteroid_coords, result = get_result(asteroids)
    #part 1
    print(result)

    result = part2(asteroid_coords, asteroids)
    #part 2
    print(result)

if __name__ == "__main__":
    main()
