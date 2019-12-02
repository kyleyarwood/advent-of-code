

def run_program_and_get_zeroth_position(program, noun, verb):
    i = 0

    program = list(map(int, program))
    #print(a)
    program[1] = noun
    program[2] = verb
    while program[i] != 99:
        if program[i] == 1:
            program[program[i+3]] = program[program[i+1]] + program[program[i+2]]
        elif program[i] == 2:
            program[program[i+3]] = program[program[i+1]] * program[program[i+2]]
        i += 4

    return program[0]

def get_file_lines(filename):
    with open(filename, 'r') as f:
        return f.read()

def find_noun_and_verb_for_output(program, output):
    for noun in range(100):
        for verb in range(100):
            new_program = [p for p in program]
            if run_program_and_get_zeroth_position(new_program, noun, verb) == output:
                return 100*noun + verb

def main():
    file_lines = get_file_lines("day2input.txt")
    program = file_lines.split(',')

    result = run_program_and_get_zeroth_position([p for p in program], 12, 2)
    #part 1
    print(result)

    result = find_noun_and_verb_for_output(program, 19690720)
    #part 2
    print(result)

if __name__ == "__main__":
    main()
