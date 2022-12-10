with open('day10.in', 'r') as f:
	lines = [x.strip() for x in f.readlines()]

res = cycles = 0
X = 1
for line in lines:
	if cycles > 220:
		break
	if line == 'noop':
		cycles += 1
		if (cycles - 20)%40 == 0:
			print(cycles, X)
			res += X*cycles
		continue
	_,val = line.split()
	val = int(val)
	if (cycles + 1 - 20)%40 == 0:
		res += X*(cycles + 1)
		print(cycles+1,X)
	elif (cycles + 2 - 20)%40 == 0:
		print(cycles+2,X)
		res += X*(cycles + 2)
	X += val
	cycles += 2
print(f"PART 1: {res}")

X = 1
cycle = 0
for line in lines:
	x = cycle%40
	if x==0:
		print()
	if X-1 <= x <= X+1:
		print('#', end='')
	else:
		print('.', end='')
	if line == 'noop':
		cycle += 1
		continue
	_,val = line.split()
	val = int(val)
	cycle += 1
	x = cycle%40
	if x==0:
		print()
	if X-1 <= x <= X+1:
		print('#', end='')
	else:
		print('.', end='')
	X += val
	cycle += 1

