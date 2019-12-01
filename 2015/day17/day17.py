
def get_containers(filename):
    with open(filename, 'r') as f:
        return f.readlines()

def get_num_ways_to_fill_n_litres(containers, num_containers_used, litres_to_fill, containers_used_so_far = 0):
    count = 0
    
    if litres_to_fill == 0:
        if containers_used_so_far not in num_containers_used:
            num_containers_used[containers_used_so_far] = 0
        num_containers_used[containers_used_so_far] += 1
        return 1
    elif not containers:
        return 0

    count += get_num_ways_to_fill_n_litres(containers[1:], num_containers_used, litres_to_fill, containers_used_so_far)

    if containers[0] <= litres_to_fill:
        count += get_num_ways_to_fill_n_litres(containers[1:], num_containers_used, litres_to_fill - containers[0], containers_used_so_far + 1)

    return count

def get_num_ways_with_min_containers(num_containers_used):
    return num_containers_used[min(num_containers_used)]

def main():
    filename = "day17input.txt"
    containers = get_containers(filename)
    containers = list(map(int, containers))
    LITRES_TO_FILL = 150

    num_containers_used = {}
    result = get_num_ways_to_fill_n_litres(containers, num_containers_used, LITRES_TO_FILL)
    #part 1
    print(result)

    result = get_num_ways_with_min_containers(num_containers_used)
    #part 2
    print(result)

if __name__ == "__main__":
    main()
