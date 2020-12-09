from file_lines import get_file_lines
from collections import Counter

lines = get_file_lines('day4.in')

def shift_cipher(s, shift):
    result = []
    for c in s:
        if c=='-':
            result.append(' ')
            continue
        val = ord(c) - ord('a')
        val = (val + shift)%26
        result.append(chr(ord('a') + val))
    return ''.join(result)

result = 0
for line in lines:
    parts = line.split('-')
    name = ''.join(parts[:-1])
    line_without_id_sum = '-'.join(parts[:-1])
    sector_id, checksum = parts[-1].split('[')
    sector_id, checksum = int(sector_id), checksum[:-1]
    msg = shift_cipher(line_without_id_sum, sector_id)
    if 'pole' in msg and 'north' in msg:
        print(msg, sector_id)
    c = Counter(name)
    sorted_c_keys = sorted(c.keys(), key=lambda x: (-c[x], x))
    if ''.join(sorted_c_keys[:5])==checksum:
        result += sector_id
print(result)
