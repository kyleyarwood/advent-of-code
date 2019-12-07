def get_orbits_map(orbits_map, orbited_planets, planets, direct_orbits):
    for direct_orbit in direct_orbits:
        orbited, orbiting = direct_orbit.replace('\n', '').split(')')
        if orbiting not in orbited_planets:
            orbited_planets.add(orbited)
        
        if orbiting not in planets:
            planets.add(orbiting)
        if orbited not in planets:
            planets.add(orbited)

        if orbiting not in orbits_map:
            orbits_map[orbiting] = [orbited]
        else:
            orbits_map[orbiting].append(orbited)

def get_direct_orbits(filename):
    with open(filename, 'r') as f:
        return f.readlines()

def get_num_orbits(orbits_map, checksums, planet):
    if planet not in checksums:
        if planet not in orbits_map:
            checksums[planet] = 0
            return 0
        num_orbits = 0
        
        for orbited_planet in orbits_map[planet]:
            num_orbits += get_num_orbits(orbits_map, checksums, orbited_planet) + 1
    
        checksums[planet] = num_orbits

    return checksums[planet]

def get_orbit_checksum(orbits_map, orbited_planets, planets):
    checksums = {}
    
    for planet in planets.difference(orbited_planets):
        get_num_orbits(orbits_map, checksums, planet)   

    return sum(checksums.values())

def get_neighbours(neighbours, direct_orbits):
    for direct_orbit in direct_orbits:
        orbited, orbiting = direct_orbit.replace('\n', '').split(')')
        if orbited not in neighbours:
            neighbours[orbited] = []
        if orbiting not in neighbours:
            neighbours[orbiting] = []
        neighbours[orbited].append(orbiting)
        neighbours[orbiting].append(orbited)

def get_shortest_path_length(neighbours, start, dest, visited, length_so_far = 0):
    if start == dest:
        return length_so_far - 2

    visited.add(start)
    shortest_path_length = None

    for neighbour in neighbours[start]:
        if neighbour in visited:
            continue
        
        path_length = get_shortest_path_length(neighbours, neighbour, dest, visited, length_so_far + 1)

        if shortest_path_length is None:
            shortest_path_length = path_length
        elif path_length is not None:
            shortest_path_length = min(shortest_path_length, path_length)

    visited.remove(start)
    return shortest_path_length

def main():
    direct_orbits = get_direct_orbits("day6input.txt")
    orbited_planets = set()
    planets = set()
    orbits_map = {}
    get_orbits_map(orbits_map, orbited_planets, planets, direct_orbits)
    
    result = get_orbit_checksum(orbits_map, orbited_planets, planets)
    #part 1
    print(result)
    
    neighbours = {}
    get_neighbours(neighbours, direct_orbits)
    visited = set()
    result = get_shortest_path_length(neighbours, "YOU", "SAN", visited)
    #part 2
    print(result)


if __name__ == "__main__":
    main()
