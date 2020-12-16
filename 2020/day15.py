from file_lines import get_file_lines

inp = list(map(int, get_file_lines('day15.in')[0].split(',')))

def nth_number(inp, n=2020):
	ages = {}
	for i,e in enumerate(inp[:-1]):
		ages[e] = i
	i = len(inp)
	last_num = inp[-1]
	while i < n:
		if last_num in ages:
			new_num = i-1-ages[last_num]
			ages[last_num] = i-1
			last_num = new_num
		else:
			ages[last_num] = i-1
			last_num = 0
		i += 1
	return last_num

result = nth_number(inp)
print(result)

result = nth_number(inp, 30000000)
print(result)
