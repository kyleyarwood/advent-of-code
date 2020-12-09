from file_lines import get_file_lines



def get_bathroom_code(lines, start=5):
	code = []
	fns = {'U': lambda x: x-3, 'D': lambda x: x+3, 'L': lambda x: x-1, 'R': lambda x: x+1}
	for line in lines:
		for instr in line:
			new_start = fns[instr](start)
			if 1 <= new_start <= 9:
				print(new_start)
				start = new_start
			else:
				print('nothing')
		print()
		code.append(start)
	return ''.join(map(str, code))



def main():
	lines = get_file_lines('day2.in')
	result = get_bathroom_code(lines)
	print(result)

if __name__ == "__main__":
	main()
