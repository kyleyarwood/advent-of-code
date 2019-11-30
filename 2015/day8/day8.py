from collections import Counter

def get_diff(char_string):
    diff = 2
    char_string = char_string[1:-1]

    i = 0

    while i < len(char_string):
        if char_string[i] == '\\':
            if char_string[i+1] == '\\' or char_string[i+1] == '\"':
                diff += 1
                i += 1
            else:
                diff += 3
                i += 3
        i += 1

    return diff

def get_total_diff(char_strings):
    total_diff = 0
    
    for char_string in char_strings:
        total_diff += get_diff(char_string)

    return total_diff

def get_char_strings(filename):
    with open(filename, 'r') as f:
        return f.readlines()

def get_encoding_diff(char_string):
    c = Counter(char_string)
    return c['\"'] + c['\\'] + 2

def get_total_encoding_diff(char_strings):
    total_encoding_diff = 0
    
    for char_string in char_strings:
        total_encoding_diff += get_encoding_diff(char_string)

    return total_encoding_diff

def main():
    char_strings = get_char_strings("day8input.txt")
    
    result = get_total_diff(char_strings)
    #part 1
    print(result)

    result = get_total_encoding_diff(char_strings)
    #part 2
    print(result)


if __name__ == "__main__":
    main()
