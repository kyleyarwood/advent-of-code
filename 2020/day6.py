from file_lines import get_file_lines

def get_num_yes_for_groups(lines):
    result = 0
    qs = set()
    first_of_group = True
    for line in lines:
        if line=='':
            result += len(qs)
            qs = set()
            continue
        for c in line:
            if c not in qs:
                qs.add(c)
    result += len(qs)
    return result

def all_yes_for_groups(lines):
    result = 0
    qs = set()
    first_of_group = True
    for line in lines:
        if line=='':
            print(qs)
            result += len(qs)
            qs = set()
            first_of_group = True
            continue
        if first_of_group:
            first_of_group = False
            qs = set(list(line))
            continue
        new_qs = set(list(line))
        qs = qs.intersection(new_qs)
    print(qs)
    result += len(qs)
    return result

def main():
    lines = [line.strip() for line in get_file_lines("day6.in")]
    result = get_num_yes_for_groups(lines)
    print(result)
    result = all_yes_for_groups(lines)
    print(result)

if __name__ == "__main__":
    main()
