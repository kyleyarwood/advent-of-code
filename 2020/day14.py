from file_lines import get_file_lines
from collections import defaultdict

lines = get_file_lines('day14.in')

mem = {}
new_mem = {}
mask = {}
NUM_BITS = 36

def int_to_list_of_bits(x):
    return [True if y=='1' else False for y in bin(x)[2:].zfill(NUM_BITS)]

def list_of_bits_to_int(a):
    return int(''.join(str(int(x)) for x in a), 2)

def list_of_bits_to_str(a):
    return ''.join('1' if x else '0' for x in a)

def str_to_list_of_bits(s):
    return [True if c=='1' else False for c in s.zfill(NUM_BITS)]

def get_all_possible_indexes(index, i=0):
    if i==len(index):
        return [index]
    if index[i] is None:
        return (get_all_possible_indexes(index[:i] + [True] + index[i+1:], i+1) +
                get_all_possible_indexes(index[:i] + [False] + index[i+1:], i+1))
    return get_all_possible_indexes(index, i+1)

def masked_memory_values(index, mask):
    index = int_to_list_of_bits(index)
    for i in range(len(index)):
        if i in mask:
            if mask[i]:
                index[i] = mask[i]
        else:
            index[i] = None
    indexes = get_all_possible_indexes(index)
    return indexes

for line in lines:
    var, val = line.split(' = ')
    if var=='mask':
        mask = {i: bool(int(x)) for i,x in enumerate(val) if x != 'X'}
    else:
        index = int(var.split('[')[1][:-1])
        orig_val = int(val)
        val = int_to_list_of_bits(int(val))
        for i in range(len(val)):
            if i in mask:
                val[i] = mask[i]
        mem[index] = list_of_bits_to_int(val)
        for i in masked_memory_values(index, mask):
            new_mem[list_of_bits_to_int(i)] = orig_val

result = sum(mem.values())
print(result)

result = sum(new_mem.values())
print(result)
