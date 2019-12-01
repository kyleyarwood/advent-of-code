AUNT_SUES_VALUES = {'children': 3, 'cats': 7, 'samoyeds': 2, 'pomeranians': 3, 'akitas': 0, 'vizslas': 0, 'goldfish': 5, 'trees': 3, 'cars': 2, 'perfumes': 1}


def compare_sue_value(aunt_sue_value, sue_dictionary, aunt_sues_values, comparison = 0):
    if aunt_sue_value not in sue_dictionary:
        return False
    elif comparison == 0:
        return sue_dictionary[aunt_sue_value] != aunt_sues_values[aunt_sue_value]
    elif comparison == -1:
        return sue_dictionary[aunt_sue_value] >= aunt_sues_values[aunt_sue_value]
    elif comparison == 1:
        return sue_dictionary[aunt_sue_value] <= aunt_sues_values[aunt_sue_value]

def get_actual_aunt_sue_number(sue_dictionaries):
    global AUNT_SUES_VALUES

    for i in range(len(sue_dictionaries)):
        for aunt_sue_value in AUNT_SUES_VALUES:
            if compare_sue_value(aunt_sue_value, sue_dictionaries[i], AUNT_SUES_VALUES):
                break
        else:
            return i + 1

def get_the_REAL_aunt_sue_number(sue_dictionaries):
    global AUNT_SUES_VALUES

    for i in range(len(sue_dictionaries)):
        for aunt_sue_value in AUNT_SUES_VALUES:
            if aunt_sue_value in ('cats', 'trees'):
                if compare_sue_value(aunt_sue_value, sue_dictionaries[i], AUNT_SUES_VALUES, 1):
                    break
            elif aunt_sue_value in ('pomeranians', 'goldfish'):
                if compare_sue_value(aunt_sue_value, sue_dictionaries[i], AUNT_SUES_VALUES, -1):
                    break
            elif compare_sue_value(aunt_sue_value, sue_dictionaries[i], AUNT_SUES_VALUES):
                break
        else:
            return i + 1

def get_sue_dictionaries(aunt_sues):
    sue_dictionaries = []
    
    for aunt_sue in aunt_sues:
        sue_info = aunt_sue.replace(',', '').split(' ')
        sue_dictionary = {}
        
        for i in range(2, len(sue_info), 2):
            sue_dictionary[sue_info[i][:-1]] = int(sue_info[i+1])
        
        sue_dictionaries.append(sue_dictionary)

    return sue_dictionaries

def get_aunt_sues(filename):
    with open(filename, 'r') as f:
        return f.readlines()

def main():
    aunt_sues = get_aunt_sues("day16input.txt")
    sue_dictionaries = get_sue_dictionaries(aunt_sues)
    result = get_actual_aunt_sue_number(sue_dictionaries)
    #part 1
    print(result)

    result = get_the_REAL_aunt_sue_number(sue_dictionaries)
    #part 2
    print(result)

if __name__ == "__main__":
    main()
