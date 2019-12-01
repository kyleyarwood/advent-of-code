def insert_into_people(people, person):
    if person not in people:
        people.add(person)

def get_happiness_map_and_people(seating_happinesses):
    happiness_map = {}
    people = set()
    seating_happinesses = [seating_happiness.replace('\n', '').split(' ') for seating_happiness in seating_happinesses]

    for seating_happiness in seating_happinesses:
        person_tuple = (seating_happiness[0], seating_happiness[-1][:-1])
        if seating_happiness[2] == "gain":
            happiness_map[person_tuple] = int(seating_happiness[3])
        else:
            happiness_map[person_tuple] = 0 - int(seating_happiness[3])
        insert_into_people(people, seating_happiness[0])

    return happiness_map, people

def get_optimal_happiness(happiness_map, people_remaining, current_person = None, original_person = None):
    if people_remaining == set():
        return happiness_map[(current_person, original_person)] + happiness_map[(original_person, current_person)]
    optimal_happiness = None

    for person in people_remaining:
        people_remaining.remove(person)
        if current_person is None:
            optimal_happiness = get_optimal_happiness(happiness_map, people_remaining, person, person)
            people_remaining.add(person)
            return optimal_happiness
        if optimal_happiness is None:
            optimal_happiness = get_optimal_happiness(happiness_map, people_remaining, person, original_person) + happiness_map[(current_person, person)] + happiness_map[(person, current_person)]
        else:
            optimal_happiness = max(optimal_happiness, get_optimal_happiness(happiness_map, people_remaining, person, original_person) + happiness_map[(current_person, person)] + happiness_map[(person, current_person)])
        people_remaining.add(person)

    return optimal_happiness

def get_seating_happinesses(filename):
    with open(filename, 'r') as f:
        return f.readlines()

def add_me(happiness_map, people):
    me = "Kyle"

    for person in people:
        happiness_map[(me, person)] = 0
        happiness_map[(person, me)] = 0

    people.add(me)

def main():
    seating_happinesses = get_seating_happinesses("day13input.txt")
    happiness_map, people = get_happiness_map_and_people(seating_happinesses)
    result = get_optimal_happiness(happiness_map, people)
    #part 1
    print(result)

    add_me(happiness_map, people)

    result = get_optimal_happiness(happiness_map, people)
    #part 2
    print(result)

if __name__ == "__main__":
    main()
