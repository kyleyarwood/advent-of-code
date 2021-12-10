with open('day10.in', 'r') as f:
    data = [x.strip() for x in f.readlines()]

corrupt = 0
incomplete = []
corrupt_scores = {')': 3, ']': 57, '}': 1197, '>': 25137}
incomplete_scores = {')': 1, ']': 2, '}': 3, '>': 4}
closing = {'(': ')', '{': '}', '[': ']', '<': '>'}
incomplete_lines = []
for line in data:
    stack = []
    for c in line:
        if c in closing.keys():
            stack.append(c)
        elif c == closing[stack[-1]]:
            stack.pop()
        else:
            corrupt += corrupt_scores[c]
            break
    else:
        to_add = 0
        while stack:
            to_add *= 5
            to_add += incomplete_scores[closing[stack.pop()]]
        incomplete.append(to_add)
print(f'Part 1: {corrupt}')
print(f'Part 2: {sorted(incomplete)[len(incomplete)//2]}')
