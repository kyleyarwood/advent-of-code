with open('day9.in', 'r') as f:
	lines = [x.strip() for x in f.readlines()]

Hx=Hy=Tx=Ty=0
s = set([(Tx,Ty)])

map = {
	'R': (1,0),
	'L': (-1,0),
	'U': (0,1),
	'D': (0,-1),
}

for instruction in lines:
	d,steps = instruction.split()
	dx,dy = map[d]
	for i in range(int(steps)):
		Hx += dx
		Hy += dy
		if abs(Hx-Tx) > 1 or abs(Hy-Ty) > 1:
			Tx,Ty = Hx-dx,Hy-dy
		s.add((Tx,Ty))

part1 = len(s)
print(f"PART 1: {part1}")

knots = [[0,0] for x in range(10)]
s = set([tuple(knots[-1])])
for instruction in lines:
	d,steps = instruction.split()
	dx,dy = map[d]
	for _ in range(int(steps)):
		knots[0][0] += dx
		knots[0][1] += dy
		for j in range(1, len(knots)):
			if abs(knots[j-1][0] - knots[j][0]) > 1 or abs(knots[j-1][1] - knots[j][1]) > 1:
				if knots[j-1][0]==knots[j][0]:
					knots[j][1] += 1 if knots[j-1][1] > knots[j][1] else -1
				elif knots[j-1][1]==knots[j][1]:
					knots[j][0] += 1 if knots[j-1][0] > knots[j][0] else -1
				else:
					drx = 1 if knots[j-1][0] > knots[j][0] else -1
					dry = 1 if knots[j-1][1] > knots[j][1] else -1
					knots[j][0] += drx
					knots[j][1] += dry
		s.add(tuple(knots[-1]))

mxx = max(x for x,y in s)
mnx = min(x for x,y in s)
mxy = max(y for x,y in s)
mny = min(y for x,y in s)

for y in range(mxy, mny-1, -1):
	for x in range(mnx, mxx+1):
		print('#' if (x,y) in s else '.', end='')
	print()

part2 = len(s)
print(f"PART 2: {part2}")
