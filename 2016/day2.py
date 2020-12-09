from file_lines import get_file_lines



def get_bathroom_code(lines, start=5):
	g = [[1,2,3],[4,5,6],[7,8,9]]
	row, col = 1, 1
	code = []
	for line in lines:
		for instr in line:
			if instr == 'U':
				row = max(0, row-1)
			elif instr == 'D':
				row = min(2, row+1)
			elif instr == 'L':
				col = max(0, col-1)
			else:
				col = min(2, col+1)
		code.append(g[row][col])
	return ''.join(map(str, code))



def main():
	lines = get_file_lines('day2.in')
	result = get_bathroom_code(lines)
	print(result)

if __name__ == "__main__":
	main()
