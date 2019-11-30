SIXTEEN_BIT_MAX = 65536

def is_int(string):
    try:
        retval = int(string)
        return True
    except:
        return False

def assign_instruction(map_of_values, instruction):
    if instruction[1] == "->":
        map_of_values[instruction[2]] = ("ASSIGN", int(instruction[0]) if is_int(instruction[0]) else instruction[0])
    elif instruction[0] == "NOT":
        map_of_values[instruction[3]] = (
                "NOT", 
                int(instruction[1]) if is_int(instruction[1]) else instruction[1])
    elif instruction[1] == "AND":
        map_of_values[instruction[4]] = (
                "AND", 
                int(instruction[0]) if is_int(instruction[0]) else instruction[0], 
                int(instruction[2]) if is_int(instruction[2]) else instruction[2])
    elif instruction[1] == "OR":
        map_of_values[instruction[4]] = (
                "OR", 
                int(instruction[0]) if is_int(instruction[0]) else instruction[0], 
                int(instruction[2]) if is_int(instruction[2]) else instruction[2])
    elif instruction[1] == "LSHIFT":
        map_of_values[instruction[4]] = (
                "LSHIFT", 
                int(instruction[0]) if is_int(instruction[0]) else instruction[0], 
                int(instruction[2]))
    elif instruction[1] == "RSHIFT":
        map_of_values[instruction[4]] = (
                "RSHIFT", 
                int(instruction[0]) if is_int(instruction[0]) else instruction[0], 
                int(instruction[2]))


def assign_instructions(instructions):
    map_of_values = {}

    for instruction in instructions:
        assign_instruction(map_of_values, instruction.replace('\n', '').split(' '))

    return map_of_values

def evaluate_key(map_of_values, key):
    if type(key) is int:
        return key

    key_tuple = map_of_values[key]
    global SIXTEEN_BIT_MAX

    if key_tuple[0] == "ASSIGN":
        return evaluate_key(map_of_values, key_tuple[1])
    elif key_tuple[0] == "AND":
        map_of_values[key] = ("ASSIGN", evaluate_key(map_of_values, key_tuple[1]) & evaluate_key(map_of_values, key_tuple[2]))
    elif key_tuple[0] == "OR":
        map_of_values[key] = ("ASSIGN", evaluate_key(map_of_values, key_tuple[1]) | evaluate_key(map_of_values, key_tuple[2]))
    elif key_tuple[0] == "NOT":
        map_of_values[key] = ("ASSIGN", SIXTEEN_BIT_MAX - 1 - (evaluate_key(map_of_values, key_tuple[1])))
    elif key_tuple[0] == "LSHIFT":
        map_of_values[key] = ("ASSIGN", evaluate_key(map_of_values, key_tuple[1])*(2**key_tuple[2])%SIXTEEN_BIT_MAX)
    elif key_tuple[0] == "RSHIFT":
        map_of_values[key] = ("ASSIGN", evaluate_key(map_of_values, key_tuple[1]) >> key_tuple[2])
    
    return map_of_values[key][1]


def get_instructions(filename):
    with open(filename, 'r') as f:
        return f.readlines()

def main():
    instructions = get_instructions("day7input.txt")
    
    map_of_values = assign_instructions(instructions)
    #print(map_of_values)
    result = evaluate_key(map_of_values, "a")
    #part 1
    print(result)

    new_map_of_values = assign_instructions(instructions)
    new_map_of_values['b'] = ("ASSIGN", result)
    result = evaluate_key(new_map_of_values, "a")
    #part 2
    print(result)


if __name__ == "__main__":
    main()
