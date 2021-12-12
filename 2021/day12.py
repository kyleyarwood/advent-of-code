from collections import defaultdict

with open('day12.in', 'r') as f:
    data = [x.strip() for x in f.readlines()]

def create_graph(data):
    graph = defaultdict(list)
    for line in data:
        x,y = line.split('-')
        graph[x].append(y)
        graph[y].append(x)
    return graph
            
def get_num_paths(graph, times_visited, threshold = 2, start='start', end='end', have_visited_threshold = False):
    if start == end:
        return 1
    result = 0
    times_visited[start] += 1
    for neighbour in graph[start]:
        if neighbour == 'start':
            continue
        if neighbour == neighbour.upper() or times_visited[neighbour] == 0 or (times_visited[neighbour] < threshold and not have_visited_threshold):
            result += get_num_paths(graph, 
                    times_visited, 
                    threshold, 
                    neighbour, 
                    end, 
                    have_visited_threshold or (times_visited[neighbour] > 0 and neighbour == neighbour.lower()))
    times_visited[start] -= 1
    return result

graph = create_graph(data)
visited = set()

times_visited = defaultdict(int)
result = get_num_paths(graph, times_visited, threshold=1)
print(f"Part 1: {result}")

times_visited = defaultdict(int)
result = get_num_paths(graph, times_visited, threshold=2)
print(f"Part 2: {result}")