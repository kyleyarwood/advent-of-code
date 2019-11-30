
def add_distance_and_location(distances_map, locations, trip_distance):
    from_dest = min(trip_distance[0], trip_distance[2])
    to_dest = max(trip_distance[0], trip_distance[2])
    
    if from_dest not in locations:
        locations.add(from_dest)

    if to_dest not in locations:
        locations.add(to_dest)

    distances_map[(from_dest, to_dest)] = int(trip_distance[4])

def get_distances_map(trip_distances):
    distances_map = {}
    locations = set()

    for trip_distance in trip_distances:
        add_distance_and_location(distances_map, locations, trip_distance.replace('\n', '').split(' '))

    return distances_map, locations


def get_trip_distances(filename):
    with open(filename, 'r') as f:
        return f.readlines()

def get_extreme_path(distances_map, locations_remaining, shortest = True, current_location = None):
    if locations_remaining == set():
        return 0

    extreme_path = None

    for location in list(locations_remaining):
        locations_remaining.remove(location)
        if current_location is None:
            if extreme_path is None:
                extreme_path = get_extreme_path(distances_map, locations_remaining, shortest, location)
            else:
                if shortest:
                    extreme_path = min(extreme_path, get_extreme_path(distances_map, locations_remaining, shortest, location))
                else:
                    extreme_path = max(extreme_path, get_extreme_path(distances_map, locations_remaining, shortest, location))
        else:
            if extreme_path is None:
                distance = distances_map[(min(location, current_location), max(location, current_location))]
                extreme_path = get_extreme_path(distances_map, locations_remaining, shortest, location) + distance
            else:
                distance = distances_map[(min(location, current_location), max(location, current_location))]
                new_path = get_extreme_path(distances_map, locations_remaining, shortest, location) + distance
                if shortest:
                    extreme_path = min(extreme_path, new_path)
                else:
                    extreme_path = max(extreme_path, new_path)
        locations_remaining.add(location)

    return extreme_path


def main():
    trip_distances = get_trip_distances("day9input.txt")
    distances_map, locations = get_distances_map(trip_distances)

    result = get_extreme_path(distances_map, locations)
    #part 1
    print(result)

    result = get_extreme_path(distances_map, locations, shortest = False)
    #part 2
    print(result)

if __name__ == "__main__":
    main()
