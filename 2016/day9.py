from file_lines import get_file_lines

lines = get_file_lines('day9.in')

inp = ''.join(lines)

def part_2(s, start, end):
    result = 0
    while start < end:
        if s[start] != '(':
            result += 1
            start += 1
        else:
            first_num = []
            start += 1
            while inp[start] != 'x':
                first_num.append(inp[start])
                start += 1
            start += 1
            second_num = []
            while inp[start] != ')':
                second_num.append(inp[start])
                start += 1
            first_num = int(''.join(first_num))
            second_num = int(''.join(second_num))
            start += 1
            result += second_num*part_2(s, start, start + first_num)
            start += first_num
    return result

i = 0
result = len(inp)
while i < len(inp):
    if inp[i] == '(':
        first_num = []
        subtracting_count = 1
        i += 1
        while inp[i] != 'x':
            first_num.append(inp[i])
            subtracting_count += 1
            i += 1
        i += 1
        subtracting_count += 1
        second_num = []
        while inp[i] != ')':
            second_num.append(inp[i])
            subtracting_count += 1
            i += 1
        subtracting_count += 1
        first_num = int(''.join(first_num))
        second_num = int(''.join(second_num))
        i += first_num
        result -= subtracting_count
        result += (second_num-1)*first_num
    i += 1
print(result)

result = part_2(inp, 0, len(inp))
print(result)
