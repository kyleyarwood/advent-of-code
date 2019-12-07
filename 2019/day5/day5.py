

def run_program_and_print_error_codes(program):
    i = 0

    program = list(map(int, program))
    while program[i] != 99:
        opcode = str(program[i])
        if opcode[-1] in ('1', '2', '7', '8'):
            operand1 = program[i+1] if len(opcode) >= 3 and opcode[-3] == '1' else program[program[i+1]]
            operand2 = program[i+2] if len(opcode) >= 4 and opcode[-4] == '1' else program[program[i+2]]
            result_index = i+3 if len(opcode) >= 5 and opcode[-5] == '1' else program[i+3]
            if opcode[-1] == '1':
                program[result_index] = operand1 + operand2
            elif opcode[-1] == '2':
                program[result_index] = operand1 * operand2
            else:
                if opcode[-1] == '7' and operand1 < operand2 or opcode[-1] == '8' and operand1 == operand2:
                    program[result_index] = 1
                else:
                    program[result_index] = 0
            i += 4
        elif opcode[-1] == '3':
            value_to_store = int(input('operand 3\n'))
            result_index = i+1 if len(opcode) >= 3 and opcode[-3] == '1' else program[i+1]
            program[result_index] = value_to_store
            i += 2
        elif opcode[-1] == '4':
            index_to_print = i+1 if len(opcode) >= 3 and opcode[-3] == '1' else program[i+1]
            print(program[index_to_print])
            i += 2
        elif opcode[-1] in ('5', '6'):
            first_param = program[i+1] if len(opcode) >= 3 and opcode[-3] == '1' else program[program[i+1]]
            second_param = program[i+2] if len(opcode) >= 4 and opcode[-4] == '1' else program[program[i+2]]
            if opcode[-1] == '5' and first_param != 0 or opcode[-1] == '6' and first_param == 0:
                i = second_param
            else:
                i += 3


def get_file_lines(filename):
    with open(filename, 'r') as f:
        return f.read()

def main():
    file_lines = get_file_lines("day5input.txt")
    program = file_lines.split(',')

    result = run_program_and_print_error_codes([p for p in program])
    #part 1
    print(result)

if __name__ == "__main__":
    main()
