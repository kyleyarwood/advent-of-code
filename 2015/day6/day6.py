def get_number_before_character_and_string_after(instruction, character):
    i = instruction.find(character)
    num = int(instruction[:i])
    return num, instruction[i:]

def get_coordinates(instruction):
    x_lo, instruction = get_number_before_character_and_string_after(instruction, ',')
    y_lo, instruction = get_number_before_character_and_string_after(instruction[1:], ' ')
    i = instruction[1:].find(' ')
    x_hi, instruction = get_number_before_character_and_string_after(instruction[i+1:], ',')
    y_hi = int(instruction[1:])
    return x_lo, y_lo, x_hi, y_hi


def toggle(light_setup, instruction, new_rules):
    x_lo, y_lo, x_hi, y_hi = get_coordinates(instruction[7:])
    
    if new_rules:
        for x in range(x_lo, x_hi + 1):
            for y in range(y_lo, y_hi + 1):
                light_setup[x][y] += 2
    else:
        for x in range(x_lo, x_hi + 1):
            for y in range(y_lo, y_hi + 1):
                light_setup[x][y] = 1 - light_setup[x][y]

def turn_on(light_setup, instruction, new_rules):
    x_lo, y_lo, x_hi, y_hi = get_coordinates(instruction[8:])

    if new_rules:
        for x in range(x_lo, x_hi + 1):
            for y in range(y_lo, y_hi + 1):
                light_setup[x][y] += 1
    else:
        for x in range(x_lo, x_hi + 1):
            for y in range(y_lo, y_hi + 1):
                light_setup[x][y] = 1

def turn_off(light_setup, instruction, new_rules):
    x_lo, y_lo, x_hi, y_hi = get_coordinates(instruction[9:])

    if new_rules:
        for x in range(x_lo, x_hi + 1):
            for y in range(y_lo, y_hi + 1):
                light_setup[x][y] = max(0, light_setup[x][y] - 1)
    else:
        for x in range(x_lo, x_hi + 1):
            for y in range(y_lo, y_hi + 1):
                light_setup[x][y] = 0

def execute_instructions(instructions, new_rules = False):
    light_setup = [[0 for i in range(1000)] for j in range(1000)]
    
    for instruction in instructions:
        if instruction[:7] == "turn on":
            turn_on(light_setup, instruction, new_rules)
        elif instruction[:8] == "turn off":
            turn_off(light_setup, instruction, new_rules)
        elif instruction[:6] == "toggle":
            toggle(light_setup, instruction, new_rules)

    return light_setup

def count_lights_on(light_setup):
    count = 0

    for row in light_setup:
        for light in row:
            count += light

    return count

def read_instructions(filename):
    with open(filename, 'r') as f:
        return f.readlines()

def main():
    instructions = read_instructions("day6input.txt")
    light_setup = execute_instructions(instructions)
    
    result = count_lights_on(light_setup)
    #part 1
    print(result)

    light_setup = execute_instructions(instructions, True)

    result = count_lights_on(light_setup)
    #part 2
    print(result)


if __name__ == "__main__":
    main()
