
def get_reindeer_speeds(filename):
    with open(filename, 'r') as f:
        return f.readlines()

def get_reindeer_info(reindeer_speed):
    return reindeer_speed.replace('\n', '').split(' ')

def get_distance_in_n_seconds(reindeer_speed, n):
    reindeer_info = get_reindeer_info(reindeer_speed)

    seconds_per_go_period = int(reindeer_info[6])
    seconds_per_go_and_rest_period = seconds_per_go_period + int(reindeer_info[13])
    
    km_per_second = int(reindeer_info[3])
    km_per_go_period = km_per_second * seconds_per_go_period

    distance = km_per_go_period*(n//seconds_per_go_and_rest_period)

    seconds_left_over = n%seconds_per_go_and_rest_period

    distance += (km_per_second)*min(seconds_left_over, seconds_per_go_period)

    return distance

def get_maximum_distance_in_n_seconds(reindeer_speeds, n):
    return max([get_distance_in_n_seconds(reindeer_speed, n) for reindeer_speed in reindeer_speeds])

def set_distances(reindeer_distances, reindeer_speed_go_rests, i):
    for reindeer in reindeer_speed_go_rests.keys():
        seconds_into_go_period = i%(reindeer_speed_go_rests[reindeer][1] + reindeer_speed_go_rests[reindeer][2])
        if 0 < seconds_into_go_period <= reindeer_speed_go_rests[reindeer][1]:
            reindeer_distances[reindeer] += reindeer_speed_go_rests[reindeer][0]

def grant_points(reindeer_distances, reindeer_points):
    max_distance = max(reindeer_distances.values())
    for reindeer in reindeer_distances.keys():
        if reindeer_distances[reindeer] == max_distance:
            reindeer_points[reindeer] += 1

def get_most_points(reindeer_speeds, n):
    reindeer_infos = [get_reindeer_info(reindeer_speed) for reindeer_speed in reindeer_speeds]
    reindeer_distances = {reindeer_info[0] : 0 for reindeer_info in reindeer_infos}
    reindeer_speed_go_rests = {reindeer_info[0] : (int(reindeer_info[3]), int(reindeer_info[6]), int(reindeer_info[13]))
            for reindeer_info in reindeer_infos}
    reindeer_points = {reindeer_info[0] : 0 for reindeer_info in reindeer_infos}

    for i in range(1, n + 1):
        set_distances(reindeer_distances, reindeer_speed_go_rests, i)
        grant_points(reindeer_distances, reindeer_points)

    return max(reindeer_points.values())

def main():
    reindeer_speeds = get_reindeer_speeds("day14input.txt")
    result = get_maximum_distance_in_n_seconds(reindeer_speeds, 2503)
    #part 1
    print(result)

    result = get_most_points(reindeer_speeds, 2503)
    #part 1
    print(result)

if __name__ == "__main__":
    main()
