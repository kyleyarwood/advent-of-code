def is_red(json_doc, i):
    return json_doc[i] == ':' and i + 5 < len(json_doc) and json_doc[i:i+6] == ":\"red\""

def is_number(json_doc, i):
    return json_doc[i].isnumeric() or json_doc[i] == '-' and json_doc[i+1].isnumeric()

def sum_object(json_doc, i):
    summation = 0
    found_red = False

    while i < len(json_doc) and json_doc[i] != '}':
        if json_doc[i] == '{':
            object_sum, i = sum_object(json_doc, i + 1)
            summation += object_sum
        elif is_red(json_doc, i):
            i += 5
            found_red = True
        elif is_number(json_doc, i):
            number, i = get_number(json_doc, i)
            summation += number
        elif json_doc[i] == '[':
            array_sum, i = sum_array(json_doc, i + 1)
            summation += array_sum
        i += 1
    
    return 0 if found_red else summation, i

def sum_array(json_doc, i):
    summation = 0

    while i < len(json_doc) and json_doc[i] != ']':
        if json_doc[i] == '{':
            object_sum, i = sum_object(json_doc, i + 1)
            summation += object_sum
        elif is_number(json_doc, i):
            number, i = get_number(json_doc, i)
            summation += number
        i += 1

    return summation, i

def get_number(json_doc, i):
    j = i + 1
    while json_doc[j].isnumeric():
        j += 1
    number = int(json_doc[i:j])
    return number, j - 1

def sum_all_non_red_numbers(json_doc):
    summation = 0
    i = 0

    while i < len(json_doc):
        if json_doc[i] == '{':
            object_sum, i = sum_object(json_doc, i + 1)
            summation += object_sum
        elif is_number(json_doc, i):
            number, i = get_number(json_doc, i)
            summation += number
        i += 1

    return summation

def sum_all_numbers(json_doc):
    summation = 0
    i = 0

    while i < len(json_doc):
        if is_number(json_doc, i):
            number, i = get_number(json_doc, i)
            summation += number
        i += 1

    return summation

def get_json_doc(filename):
    with open(filename, 'r') as f:
        return f.read().replace('\n', '')

def main():
    json_doc = get_json_doc("day12input.txt")
    result = sum_all_numbers(json_doc)
    #part 1
    print(result)

    result = sum_all_non_red_numbers(json_doc)
    #part 2
    print(result)

if __name__ == "__main__":
    main()
