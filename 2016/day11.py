from file_lines import get_file_lines

lines = get_file_lines('day11.in')

floor_contents = []
for line in lines:
	csv = line.replace(', ', ' and ').replace(' and ', ',').replace('.', '').split(',')
	new_floor = []
	for v in csv:
		material, type = v.split()[-2:]
		if type == 'generator':
			new_floor.append((material, True))
		elif type == 'microchip':
			new_floor.append((material.split('-')[0], False))
	floor_contents.append(new_floor)

def deep_copy(floor_contents):
	return [[x for x in floor] for floor in floor_contents]

def get_neighbours(floor_contents):
	neighbours = []
	for i,floor in enumerate(floor_contents):
		for j,content in enumerate(floor):
			if not content[1]:
				if i > 0 and any(c == (content[0], True) for c in floor_contents[i-1]) or all(not c[1] for c in floor_contents[i-1]):
					new_neighbour = deep_copy(floor_contents)
					new_neighbour[i].pop(j)
					new_neighbour[i-1].append(content)
					neighbours.append(new_neighbour)
				if i < len(floor_contents)-1 and any(c== (content[0], True) for c in floor_contents[i+1]) or all(not c[1] for c in floor_contents[i+1]):
					new_neighbour = deep_copy(floor_contents)
					new_neighbour[i].pop(j)
					new_neighbour[i+1].append(content)
					neighbours.append(new_neighbour)
			else:
				#TODO: figure out generator case
				continue
	return neighbours

def is_goal(floor_contents):
	return not any(floor_contents[:-1])

def floor_contents_tuple(floor_contents):
	return tuple(tuple(sorted(floor)) for floor in floor_contents)

def shortest_path(floor_contents):
	floor_tuple = floor_contents_tuple(floor_contents)
	frontier = [floor_contents]
	visited = set([floor_tuple])
	path_length = 1
	while frontier:
		new_frontier = []
		for node in frontier:
			neighbours = get_neighbours(node)
			for neighbour in neighbours:
				if is_goal(neighbour):
					return path_length
				neighbour_tuple = floor_contents_tuple(neighbour)
				if neighbour_tuple in visited:
					continue
				visited.add(neighbour_tuple)
				new_frontier.append(neighbour)
		frontier = new_frontier
		path_length += 1
	return -1



