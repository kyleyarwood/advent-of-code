def trees_with_slope(inp, right_factor, down_factor=1):
	right = 0
	trees = 0
	for line in inp[::down_factor]:
		print(line)
		if line[right]=='#':
			trees += 1
		right = (right + right_factor)%len(line)
	return trees

def get_input(filename):
	with open(filename, 'r') as f:
		return list(map(lambda line: line.strip(), f.readlines()))

def main():
	inp = get_input('day3.in')
	RIGHT = 3
	result = trees_with_slope(inp, RIGHT)
	print(result)

	#part 2
	prod = 1
	for right,down in [(1,1),(3,1),(5,1),(7,1),(1,2)]:
		prod *= trees_with_slope(inp, right, down)
	print(prod)

if __name__ == "__main__":
	main()
