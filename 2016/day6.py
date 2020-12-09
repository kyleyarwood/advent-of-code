from file_lines import get_file_lines
from collections import Counter

lines = get_file_lines('day6.in')

#part 1
cs = [Counter(line[i] for line in lines) for i in range(len(lines[0]))]
result = ''.join(max(c.keys(), key=lambda x: c[x]) for c in cs)
print(result)

result = ''.join(min(c.keys(), key=lambda x: c[x]) for c in cs)
print(result)
