
def get_run(string, j):
    k = j
    while k < len(string) and string[k] == string[j]:
        k += 1
    return k - j

def increasing(number):
    string = str(number)
    for j in range(len(string) - 1):
        if string[j] > string[j+1]:
            return False
    else:
        return True

def has_run_of_two(number):
    string = str(number)
    
    j = 0
    while j < len(string):
        run = get_run(string, j)
        if run >= 2:
            return True
        else:
            j += run

    return False

def has_run_of_only_two(number):
    string = str(number)

    j = 0
    while j < len(string):
        run = get_run(string, j)
        if run == 2:
            return True
        else:
            j += run

    return False


def valid_passwords_count(lo, hi):
    count = 0
    for i in range(lo, hi + 1):
        if increasing(i) and has_run_of_two(i):
            count += 1
    return count

def new_valid_passwords_count(lo, hi):
    count = 0
    for i in range(lo, hi + 1):
        if increasing(i) and has_run_of_only_two(i):
            count += 1
    return count

def main():
    lo = 256310
    hi = 732736

    result = valid_passwords_count(lo, hi)
    #part 1
    print(result)

    result = new_valid_passwords_count(lo, hi)
    #part 2
    print(result)


if __name__ == "__main__":
    main()
