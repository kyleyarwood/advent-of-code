from file_lines import get_file_lines
#from collections import defaultdict

def create_graph(file_lines):
    graph = {}
    for file_line in file_lines:
        contains, contained = file_line[:-1].split(' contain ')
        final_contained = []
        for bag_type in contained.split(', '):
            space_split = bag_type.split()
            if space_split[0]=='no':
                print(contains[:-1])
                graph[contains[:-1]] = []
                continue
            num_bags = int(space_split[0])
            bag = ' '.join(space_split[1:])
            if num_bags != 1:
                bag = bag[:-1]
            final_contained.append((num_bags, bag))
        graph[contains[:-1]] = final_contained
    return graph

def dfs(graph_keys, graph, d, start=None):
    if start is None:
        for key in graph_keys:
            if key in d:
                continue
            dfs(graph_keys, graph, d, key)
    else:
        for neighbour_num, neighbour_bag in graph[start]:
            if neighbour_bag not in d:
                dfs(graph_keys, graph, d, neighbour_bag)
            if d[neighbour_bag]:
                d[start] = True
                break
        else:
            d[start] = False

def how_many_in_gold(graph, start='shiny gold bag', dp={}):
    if start not in dp:
        dp[start] = 0
        for neighbour_num, neighbour_bag in graph[start]:
            if neighbour_bag not in dp:
                how_many_in_gold(graph, neighbour_bag, dp)
            dp[start] += neighbour_num * (dp[neighbour_bag]+1)
        
    return dp[start]
    

def how_many_contain_gold(graph):
    d = {'shiny gold bag': True}
    dfs(list(graph.keys()), graph, d)
    return sum(d.values()) - 1

def main():
    file_lines = get_file_lines("day7.in")
    graph = create_graph(file_lines)
    #print(graph)
    result = how_many_contain_gold(graph)
    print(result)

    #part 2
    result = how_many_in_gold(graph)
    print(result)

if __name__ == "__main__":
    main()
