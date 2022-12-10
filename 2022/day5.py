with open('day5.in', 'r') as f:
	lines = [x for x in f.readlines()]

stacks = []
for i,line in enumerate(lines):
	j = k = 0
	if line[1] == '1':
		break
	while j < len(line):
		if i==0:
			stacks.append([])
		if line[j] == '[':
			stacks[k].append(line[j+1])
		k += 1
		j += 4

for k in range(len(stacks)):
	stacks[k] = stacks[k][::-1]
part_2_stacks = [stack[::] for stack in stacks]

for line in lines[i+2:]:
	amt,which = line.split(' from ')
	amt = int(amt.split()[-1])
	frm,t = map(int, which.split(' to '))
	for k in range(amt):
		stacks[t-1].append(stacks[frm-1].pop())

print(f"PART 1: {''.join(stack[-1] for stack in stacks)}")

for line in lines[i+2:]:
	amt,which = line.split(' from ')
	amt = int(amt.split()[-1])
	frm,t = map(int, which.split(' to '))
	stack = []
	for k in range(amt):
		stack.append(part_2_stacks[frm-1].pop())
	while stack:
		part_2_stacks[t-1].append(stack.pop())

print(f"PART 2: {''.join(stack[-1] for stack in part_2_stacks)}")
