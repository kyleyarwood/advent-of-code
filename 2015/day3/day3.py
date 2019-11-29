
def add_location(houses_visited, location):
    if location not in houses_visited:
        houses_visited.add(location)


def get_num_houses_with_robo(directions):
    santa_positions = [[0, 0], [0, 0]]
    houses_visited = set([(0, 0)])

    for i in range(len(directions)):
        if directions[i] == ">":
            santa_positions[i%2][0] += 1
        elif directions[i] == "<":
            santa_positions[i%2][0] -= 1
        elif directions[i] == "^":
            santa_positions[i%2][1] += 1
        elif directions[i] == "v":
            santa_positions[i%2][1] -= 1
        add_location(houses_visited, (santa_positions[i%2][0], santa_positions[i%2][1]))

    return len(houses_visited)


def get_num_houses(directions):
    x = 0
    y = 0
    houses_visited = set([(x, y)])

    for direction in directions:
        if direction == ">":
            x += 1
        elif direction == "<":
            x -= 1
        elif direction == "^":
            y += 1
        elif direction == "v":
            y -= 1
        
        add_location(houses_visited, (x, y))

    return len(houses_visited)

def read_file(filename):
    with open(filename, 'r') as f:
        return f.read()

def main():
    directions = read_file("day3input.txt")

    result = get_num_houses(directions)
    #part 1
    print(result)

    result = get_num_houses_with_robo(directions)
    #part 2
    print(result)

if __name__ == "__main__":
    main()
