from collections import defaultdict, Counter

with open('day6.in', 'r') as f:
	vals = list(map(int, f.read().strip().split(',')))

for part,days in enumerate([80, 256]):
	c = Counter(vals)

	for i in range(days):
		new_c = defaultdict(int)
		for j in range(1,9):
			new_c[j-1] += c[j]
		new_c[6] += c[0]
		new_c[8] += c[0]
		c = new_c

	result = sum(c.values())
	print(f"Part {part+1}: {result}")
