from file_lines import get_file_lines

lines = get_file_lines('day7.in')

def is_valid_ip(ip):
    l4 = []
    has_abba = False
    is_square = False
    for c in ip:
        if c in ('[', ']'):
            if c=='[':
                is_square=True
            else:
                is_square=False
            l4 = []
            continue
        l4.append(c)
        if len(l4) > 4:
            l4.pop(0)
        if len(l4)==4 and l4[0]!=l4[1] and l4[0]==l4[3] and l4[1]==l4[2]:
            if is_square:
                return False
            has_abba = True
    return has_abba

def supports_ssl(ip):
    l3 = []
    patterns = set()
    is_square = False
    for c in ip:
        #print(look_for)
        if c in ('[', ']'):
            if c=='[':
                is_square = True
            else:
                is_square = False
            l3 = []
            continue
        l3.append(c)
        if len(l3) > 3:
            l3.pop(0)
        if len(l3)==3 and l3[0]!=l3[1] and l3[0]==l3[2]:
            bab = ''.join((l3[1], l3[0], l3[1]))
            if (bab, not is_square) in patterns:
                return True
        joined = ''.join(l3)
        if joined not in patterns:
            patterns.add((joined, is_square))
    return False

result = sum(is_valid_ip(ip) for ip in lines)
print(result)

#part 2
result = sum(supports_ssl(ip) for ip in lines)
print(result)
