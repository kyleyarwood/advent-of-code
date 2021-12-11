with open('day19.in', 'r') as f:
	lines = [x.strip() for x in f.readlines()]

deck = [i for i in range(10007)]
for i,line in enumerate(lines):
	print(i, line)
	instrs = line.split()
	if line == 'deal into new stack':
		deck = deck[::-1]
	elif instrs[0] == 'cut':
		N = int(instrs[1])
		N = (len(deck) + N)%len(deck)
		deck = deck[N:] + deck[:N]
	else:
		inc = int(instrs[-1])
		new_deck = [-1 for _ in range(10007)]
		i = 0
		while i < len(deck):
			new_deck[(i*inc)%len(deck)] = deck[i]
			i += 1
		deck = new_deck

for i,e in enumerate(deck):
	if e==2019:
		print(i)
		break

def undo_for_index(i):
	num_cards = 119315717514047
	for line in reversed(lines):
		instrs = line.split()
		if line == 'deal into new stack':
			i = num_cards - 1 - i
		elif instrs[0] == 'cut':
			N = int(instrs[1])
			#i = (i-N)%num_cards
			i = (i+N)%num_cards
		else:
			inc = int(instrs[-1])
			#i = (inc*i)%num_cards
			i = (pow(inc, -1, num_cards)*i)%num_cards
	return i, (pow(i, -1, num_cards)*2020)%num_cards

def part2():
	i = (2020, 0)
	j = 0
	s = set()
	while i not in s and j < 2:
		i = i[0]
		s.add(i)
		i = undo_for_index(i)
		j += 1
	print(i, j)

part2()
