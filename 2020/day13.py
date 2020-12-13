from file_lines import get_file_lines
from math import ceil
from itertools import permutations

lines = get_file_lines('day13.in')

result,m = None,None

earliest = int(lines[0])
inp = lines[1]
c = 0

for x in inp.split(','):
    if x=='x':
        continue
    y = int(x)
    c = max(c,y)
    #print(y, ceil(earliest/y)*y)
    if m is None:
        result,m = y,ceil(earliest/y)*y
    else:
        new_result,new_m = y,ceil(earliest/y)*y
        if new_m < m:
            result,m = new_result,new_m

print(result*(m-earliest))

k = {int(y): i for i,y in enumerate(inp.split(',')) if y!='x'}

def inv(x, m):
    for i in range(m):
        if (x*i)%m == 1:
            return i
    return None

def lin_cong(tup, a_2, m_2):
    a,b = tup
    a = a%m_2
    b = b%m_2
    #print(tup, a_2, m_2)
    new_mod = (inv(a, m_2)*(a_2-b))%m_2
    #print(m_2, new_mod)
    return (m_2, new_mod)

result = None

for x in k:
    t = (1,0)
    for y in k:
        soln = lin_cong(t, k[x]-k[y], y)
        t = (t[0]*soln[0], t[0]*soln[1] + t[1])
    if (result is None or (result is not None and result[1] > t[1])) and t[1] >= earliest:
        result = t
print(result)
