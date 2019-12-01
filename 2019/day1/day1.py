
def get_file_lines(filename):
    with open(filename, 'r') as f:
        return f.readlines()

def total_fuel_with_fuel_for_fuel(modules):
    total_fuel = 0

    for module in modules:
        result = max(module//3 - 2, 0)
        total_fuel += result
        while result > 0:
            result = max(result//3 - 2, 0)
            total_fuel += result

    return total_fuel


def total_fuel(modules):
    total_fuel = 0

    for module in modules:
        total_fuel += module//3 - 2

    return total_fuel


def main():
    modules = get_file_lines("day1input.txt")
    modules = [int(module) for module in modules]

    result = total_fuel(modules)
    #part 1
    print(result)

    result = total_fuel_with_fuel_for_fuel(modules)
    #part 2
    print(result)

if __name__ == "__main__":
    main()
