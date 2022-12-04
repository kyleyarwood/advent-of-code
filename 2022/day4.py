with open('day4.in', 'r') as f:
	lines = [x.strip() for x in f.readlines()]

part1 = 0
part2 = 0

for line in lines:
	e1,e2 = line.split(',')
	x,y = map(int, e1.split('-'))
	a,b = map(int, e2.split('-'))
	if x <= a <= b <= y or a <= x <= y <= b:
		part1 += 1
	if a <= y <= b or x <= b <= y:
		part2 += 1

print(f"PART 1: {part1}")
print(f"PART 2: {part2}")
