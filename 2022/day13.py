import json
from copy import deepcopy

with open('day13.in', 'r') as f:
	lines = [x.strip() for x in f.readlines()]

part1 = 0
pairs = []

for i in range(0, len(lines), 3):
	l1 = json.loads(lines[i])
	l2 = json.loads(lines[i+1])
	pairs.append((l1, l2))

def cmp(A, B):
	P,Q = map(deepcopy, [A,B])
	stack = [[P, Q, 0]]
	while stack:
		P,Q,i = stack[-1]
		if i>=len(Q) and i>=len(P):
			stack.pop()
			stack[-1][-1] += 1
			continue
		elif i>=len(P):
			return True
		elif i>=len(Q):
			return False
		if isinstance(P[i], list) and isinstance(Q[i], list):
			stack.append([P[i],Q[i],0])
			continue
		elif isinstance(P[i], list):
			Q[i] = [Q[i]]
			continue
		elif isinstance(Q[i], list):
			P[i] = [P[i]]
			continue
		if P[i] < Q[i]:
			return True
		elif P[i] > Q[i]:
			return False
		stack[-1][-1] += 1

def sort(pairs):
	#O(n^2) should be fine
	packets = []
	pairs.append([[[2]], [[6]]])
	for x,y in pairs:
		packets.append(x)
		packets.append(y)
	for i in range(len(packets)):
		mx = i
		for j in range(i+1, len(packets)):
			if cmp(packets[j], packets[mx]):
				mx = j
		packets[i], packets[mx] = packets[mx], packets[i]
	return packets	

k=0
for A,B in pairs:
	k += 1
	if cmp(A, B):
		part1 += k

print(f"PART 1: {part1}")

part2 = []

res = sort(pairs)
for i,x in enumerate(res):
	if x == [[2]] or x == [[6]]:
		part2.append(i)

print(f"PART 2: {part2}, {(part2[0]+1)*(part2[1]+1)}")
