from collections import Counter

def is_valid_password(pw):
    return pw['lo'] <= pw['pass'].count(pw['char']) <= pw['hi']

def xor(a, b):
    return (a or b) and not (a and b)

def new_is_valid_password(pw):
    first = pw['pass'][pw['lo']-1] == pw['char']
    second = pw['pass'][pw['hi']-1] == pw['char']
    return xor(first, second)

def get_input(filename):
    with open(filename, 'r') as f:
        return f.readlines()

def parse_line(line):
    line = line.split()
    lo,hi = map(int, line[0].split('-'))
    char = line[1][:-1]
    pw = line[2]
    return {'lo': lo, 'hi': hi, 'char': char, 'pass': pw}

def main():
    inp = get_input("day2.in")
    inp = [parse_line(line) for line in inp]
    result = sum(is_valid_password(pw) for pw in inp)
    print(result)

    #part 2
    result = sum(new_is_valid_password(pw) for pw in inp)
    print(result)

if __name__ == "__main__":
    main()
