with open('day12.in', 'r') as f:
	lines = [x.strip() for x in f.readlines()]

grid = []

x=y=-1
a=b=-1

lowest = set()
for i,line in enumerate(lines):
	row = []
	for j,c in enumerate(line):
		if c == 'S':
			x,y=i,j
			row.append(0)
			lowest.add((i,j))
		elif c == 'E':
			a,b=i,j
			row.append(25)
		else:
			row.append(ord(c)-ord('a'))
			if row[-1] == 0:
				lowest.add((i,j))
	grid.append(row)

def bfs(sx=x,sy=y):
	def get_nbrs(p,q):
		nbrs = []
		for r,s in ((p-1,q),(p+1,q),(p,q-1),(p,q+1)):
			if 0<=r<len(grid) and 0<=s<len(grid[r]) and grid[r][s]<=grid[p][q]+1:
				nbrs.append((r,s))
		return nbrs

	frontier = [(sx,sy)]
	count = 0
	visited = set(frontier)
	while (a,b) not in visited:
		if not frontier:
			return float('inf')
		new_frontier = []
		for i,j in frontier:
			for r,s in get_nbrs(i,j):
				if (r,s) in visited:
					continue
				new_frontier.append((r,s))
				visited.add((r,s))
		frontier = new_frontier
		count += 1
	return count


res = bfs()
print(f"PART 1: {res}")

for i,j in lowest:
	res = min(res, bfs(i,j))
print(f"PART 2: {res}")
