from file_lines import get_file_lines

def get_result(lines):
    accumulator = 0
    lines_ran = set()
    i = 0
    while i not in lines_ran and i < len(lines):
        s = lines[i].split()
        lines_ran.add(i)
        if s[0] == 'acc':
            accumulator += int(s[1])
            i += 1
        elif s[0] == 'jmp':
            i += int(s[1])
        else:
            i += 1
    return accumulator
        
def does_terminate(lines):
    lines_ran = set()
    i = 0
    while i not in lines_ran and i < len(lines):
        s = lines[i].split()
        lines_ran.add(i)
        if s[0] == 'acc' or s[0]=='nop':
            i += 1
        else:
            i += int(s[1])
    return i == len(lines)

def get_terminating_program(lines):
    for i, line in enumerate(lines):
        s = line.split()
        if s[0] == 'nop':
            k = lines[:i] + [' '.join(['jmp', s[1]])] + lines[i+1:]
            if does_terminate(k):
                return k
        elif s[0] == 'jmp':
            k = lines[:i] + [' '.join(['nop', s[1]])] + lines[i+1:]
            if does_terminate(k):
                return k
    return -1

def get_resultb(lines):
    terminating_program = get_terminating_program(lines)
    result = get_result(terminating_program)
    return result

def main():
    lines = get_file_lines('day8.in')
    result = get_result(lines)
    print(result)
    result = get_resultb(lines)
    print(result)

if __name__ == "__main__":
    main()
