from file_lines import get_file_lines


def get_seat_id(line):
	lo, hi = 0, 127
	for c in line[:7]:
		if c=='F':
			hi = (lo + hi)//2
		else:
			lo = (lo + hi)//2 + 1
	row = lo
	lo, hi = 0, 7
	for c in line[7:]:
		if c=='L':
			hi = (lo + hi)//2
		else:
			lo = (lo + hi)//2 + 1
	col = lo
	return row*8 + col


def highest_seat_id(inp):
	d = {line: get_seat_id(line) for line in inp}
	result = sorted([(line, d[line]) for line in d.keys()], key=lambda x: x[1], reverse=True)
	#print(result)
	return max(d.values())

def get_my_seat_id(inp):
	s = set([get_seat_id(line) for line in inp])
	for i in s:
		if i+1 not in s and i+2 in s:
			return i+1
	return -1

def main():
	inp = [line.strip() for line in get_file_lines('day5.in')]
	result = highest_seat_id(inp)
	print(result)
	#print(get_seat_id("FFFBBBFRRR"))
	#print(get_seat_id("BBFFBBFRLL"))
	
	#part 2
	result = get_my_seat_id(inp)
	print(result)

if __name__ == "__main__":
	main()
