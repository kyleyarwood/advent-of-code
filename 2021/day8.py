from itertools import permutations

file = 'day8.in'
with open(file, 'r') as f:
    data = [x.strip() for x in f.readlines()]

res = 0
for x in data:
    inp,outp = x.split(' | ')
    for y in outp.split():
        if len(y) in (2, 3, 4, 7):
            res += 1
print(res)

result = 0
digits = [
        [0,1,2,4,5,6],
        [2,5],
        [0,2,3,4,6],
        [0,2,3,5,6],
        [1,2,3,5],
        [0,1,3,5,6],
        [0,1,3,4,5,6],
        [0,2,5],
        [0,1,2,3,4,5,6],
        [0,1,2,3,5,6]
    ]
for j,x in enumerate(data):
    for perm in permutations(list('abcdefg')):
        res = []
        inp,outp = x.split(' | ')
        digs = digits[:]
        fail = False
        #check that perm works
        for y in inp.split():
            b = [i for i,e in enumerate(perm) if e in y]
            new_digs = []
            for i,digit in enumerate(digs):
                if b!=digit:
                    new_digs.append(digit)
            if len(digs) == len(new_digs):
                fail = True
                break
            digs = new_digs

        #perm failed, try next one
        if fail:
            continue

        #perm worked, create 4 digit output
        for y in outp.split():
            b = [i for i,e in enumerate(perm) if e in y]
            for i,digit in enumerate(digits):
                if b==digit:
                    res.append(i)
                    break
        result += int(''.join(map(str, res)))
        break
print(result)
