def get_file_lines(filename):
	with open(filename, 'r') as f:
		return [line.strip() for line in f.readlines()]
