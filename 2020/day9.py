from file_lines import get_file_lines


def get_result(lines):
    result = 0
    lines = [int(line) for line in lines]
    last_25 = set()
    i = 0
    preamble = 25
    while i < preamble:
        last_25.add(lines[i])
        i += 1
    while i < len(lines):
        for k in last_25:
            for j in last_25:
                if k!=j and k+j==lines[i]:
                    break
            else:
                continue
            break
        else:
            return lines[i]
        last_25.remove(lines[i-preamble])
        last_25.add(lines[i])
        i += 1
    return result

def get_resultb(lines, n):    
    result = 0
    last_n = []
    lines = [int(line) for line in lines]
    for i,e in enumerate(lines):
        print(last_n)
        for j in range(len(last_n)):
            last_n[j] += e
            if last_n[j] == n:
                #print(e)
                my_list = lines[j:i+1]
                print(last_n[j])
                print(sum(my_list))
                return max(my_list) + min(my_list)
        last_n.append(e)
    return result

def main():
    lines = get_file_lines('day9.in')
    result = get_result(lines)
    print(result)

    #part 2
    result = get_resultb(lines, result)
    print(result)


if __name__ == "__main__":
    main()
