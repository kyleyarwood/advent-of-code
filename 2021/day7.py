file = 'day7.in'
with open(file, 'r') as f:
	data = list(map(int, f.read().strip().split(',')))

for i,fn in enumerate([lambda x,y: abs(x-y), lambda x,y: (abs(x-y)*(abs(x-y)+1))//2]):
	x = 0
	res = float('inf')
	while x < max(data):
		res = min(res, sum(map(lambda y: fn(x,y), data)))
		x += 1
	print(f"Part {i+1}: {res}")
