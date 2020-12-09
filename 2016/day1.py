from file_lines import get_file_lines

def R(dx,dy):
	if dx==0:
		return dy,0
	else:
		return 0,-dx

def L(dx, dy):
	if dx==0:
		return -dy,0
	else:
		return 0,dx

def get_length_of_path(line):
	x, y, dx, dy = 0, 0, 0, 1
	visited = set((0, 0))
	part_2_location = None
	mvmts = line.split(', ')
	fns = {'L': L, 'R': R}
	print(mvmts)
	for mvmt in mvmts:
		d, amt = mvmt[0], int(mvmt[1:])
		dx, dy = fns[d](dx, dy)
		for i in range(amt):
			x += dx
			y += dy
			if part_2_location is None and (x,y) in visited:
				part_2_location = (x,y)
			elif (x,y) not in visited:
				visited.add((x,y))
	return abs(x) + abs(y), abs(part_2_location[0]) + abs(part_2_location[1])

def main():
	line = get_file_lines('day1.in')[0]
	result = get_length_of_path(line)
	print(result)

	#part 2

if __name__ == "__main__":
	main()
