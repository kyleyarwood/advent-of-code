def add_to_map(my_map, dupes, file_line, l = 0):
    x = 0
    y = 0
    total_steps = 0
    for f in file_line:
        for i in range(int(f[1:])):
            total_steps += 1
            if f[0] == 'R':
                x += 1
            elif f[0] == 'D':
                y -= 1
            elif f[0] == 'L':
                x -= 1
            else:
                y += 1
            if (x, y) not in my_map:
                if l != 1:
                    my_map[(x, y)] = total_steps
            elif (x,y) not in dupes and l != 0:
                dupes[(x, y)] = my_map[(x, y)] + total_steps
    


def method(file_lines):
    file_line = file_lines[0]
    file_line = file_line.split(',')
    my_map = {}
    dupes = {}
    add_to_map(my_map, dupes, file_line)
    file_line = file_lines[1].split(',')
    add_to_map(my_map, dupes, file_line, 1)
    print(min(dupes.values()))


def get_file_lines(filename):
    with open(filename, 'r') as f:
        return f.readlines()


def main():
    file_lines = get_file_lines("day3input.txt")
    result = method(file_lines)
    print(result)



if __name__ == "__main__":
    main()
