from collections import defaultdict

with open('day8.in', 'r') as f:
	lines = [x.strip() for x in f.readlines()]

trees = []
for line in lines:
	new_row = []
	for c in line:
		new_row.append(int(c))
	trees.append(new_row)


def get_viewing_distance(val, last_occurrence):
	res = -1
	for i in range(val, len(last_occurrence)):
		res = max(res, last_occurrence[i])
	return res

scenic_scores = defaultdict(lambda: 1)
visibility = [[False for x in row] for row in trees]
for i,row in enumerate(trees):
	mx = -1
	last_occurrence = [-1 for i in range(10)]
	for j,x in enumerate(row):
		vd = get_viewing_distance(x, last_occurrence)
		if vd == -1:
			scenic_scores[(i,j)] *= j
		else:
			scenic_scores[(i,j)] *= (j - vd)
		last_occurrence[x] = j
		if x > mx:
			visibility[i][j] = True
			mx = x
	last_occurrence = [-1 for i in range(10)]
	mx = -1
	for j,x in enumerate(reversed(row)):
		vd = get_viewing_distance(x, last_occurrence)
		if vd == -1:
			scenic_scores[(i,len(row)-1-j)] *= j
		else:
			scenic_scores[(i,len(row)-1-j)] *= (j - vd)
		last_occurrence[x] = j
		if x > mx:
			visibility[i][-j-1] = True
			mx = x

for j in range(len(trees[0])):
	last_occurrence = [-1 for i in range(10)]
	mx = -1
	for i in range(len(trees)):
		x = trees[i][j]
		vd = get_viewing_distance(x, last_occurrence)
		if vd == -1:
			scenic_scores[(i,j)] *= i
		else:
			scenic_scores[(i,j)] *= (i - vd)
		last_occurrence[x] = i
		if x > mx:
			visibility[i][j] = True
			mx = x
	last_occurrence = [-1 for i in range(10)]
	mx = -1
	for i in range(len(trees)-1,-1,-1):
		x = trees[i][j]
		vd = get_viewing_distance(x, last_occurrence)
		if vd == -1:
			scenic_scores[(i,j)] *= (len(trees)-1-i)
		else:
			scenic_scores[(i,j)] *= (len(trees)-1-i - vd)
		last_occurrence[x] = len(trees)-1-i
		if x > mx:
			visibility[i][j] = True
			mx = x

x = sum(sum(row) for row in visibility)
print(f"PART 1: {x}")

print(f"PART 2: {max(scenic_scores.values())}")
