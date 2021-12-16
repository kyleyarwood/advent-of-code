from functools import reduce
from operator import mul

res = []
d = {x: bin(int(x, 16))[2:].zfill(4) for x in 
        list(map(str, range(10))) + ['A', 'B', 'C', 'D', 'E', 'F']}

with open('day16.in', 'r') as f:
    for c in f.read().strip():
        res.append(d[c])
data = ''.join(res)

def get_version_type_id(data, i=0):
    if len(data)-i < 6:
        return None, None
    return int(data[i:i+3], 2), int(data[i+3:i+6], 2)

def get_literal_value(data, i=0):
    is_last_group = False
    res = []
    while i < len(data):
        if data[i] == '0':
            is_last_group = True
        res.append(data[i+1:i+5])
        i += 5
        if is_last_group:
            break
    return int(''.join(res), 2), i

def get_length_of_contained_subpackets(data, i=0):
    return int(data[i:i+15], 2)

def get_num_immediately_contained_subpackets(data, i=0):
    return int(data[i:i+11], 2)

def sum_of_version_numbers(data, i=0, part_2=False):
    fns = {0: sum, 1: lambda x: reduce(mul, x, 1), 2: min, 3: max, 5: (lambda x: x[0]>x[1]), 6: (lambda x: x[0]<x[1]), 7: (lambda x: x[0]==x[1])}
    if i>=len(data)-6:
        return 0, i+6
    version, type_id = get_version_type_id(data, i)
    i += 6
    if type_id == 4:
        retval, i = get_literal_value(data, i)
        return retval if part_2 else version, i
    if not part_2:
        type_id = 0

    length_type_id = data[i]
    i += 1
    if not part_2 or type_id == 1:
        res = version
    res = [] if part_2 else [version]
    if length_type_id == '0':
        length_of_contained_subpackets = get_length_of_contained_subpackets(data, i)
        i += 15
        j = i
        while i - j < length_of_contained_subpackets:
            retval, i = sum_of_version_numbers(data, i, part_2)
            res.append(retval)
        return fns[type_id](res), i
    elif length_type_id == '1':
        num_immediately_contained_subpackets = get_num_immediately_contained_subpackets(data, i)
        i += 11
        for j in range(num_immediately_contained_subpackets):
            retval, i = sum_of_version_numbers(data, i, part_2)
            res.append(retval)
        return fns[type_id](res), i

    
result = sum_of_version_numbers(data)[0]
print(result)

result = sum_of_version_numbers(data, i=0, part_2=True)[0]
print(result)