from dijkstar import Graph, find_path

with open('day15.in', 'r') as f:
    data = [list(map(int, x.strip())) for x in f.readlines()]

def dijkstra(d):
    g = Graph()
    for i in range(len(d)):
        for j in range(len(d[i])):
            dirs = ((i-1, j), (i+1, j), (i, j-1), (i, j+1))
            for x,y in dirs:
                if 0 <= x < len(d) and 0 <= y < len(d[i]):
                    g.add_edge((i,j),(x,y),d[x][y])
    return find_path(g, (0, 0), (len(d)-1, len(d[0])-1)).total_cost


def print_grid(grid):
    print('\n'.join(''.join(map(str, row)) for row in grid))

def get_five_by_five(d):
    result = []
    for i in range(len(d)*5):
        new_row = []
        for j in range(len(d[i%len(d)])*5):
            x = i%len(d)
            y = j%len(d[x])
            a = d[x][y] + i//len(d) + j//len(d)
            res = a%10 + a//10
            new_row.append(res)
        result.append(new_row)
    return result

result = dijkstra(data)
print(f"Part 1: {result}")


new_data = get_five_by_five(data)
result = dijkstra(new_data)
print(f"Part 2: {result}")
