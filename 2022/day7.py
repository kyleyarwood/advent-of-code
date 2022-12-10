with open('day7.in', 'r') as f:
	lines = [x.strip() for x in f.readlines()]

class Directory:
	def __init__(self, name='/', parent=None):
		self.parent = parent
		self.name = name
		self.file_sizes = 0
		self.children = {}

	def __str__(self):
		return f'{self.name},{self.file_sizes}\n' + '\n-\n'.join(str(x) for x in self.children.values())


def sum_subtree_sums_at_most_k(root, k=100_000):
	#result, actual_subtree_sum
	if not root:
		return 0,0
	res = sums = 0
	for child in root.children.values():
		a,b = sum_subtree_sums_at_most_k(child, k)
		res += a
		sums += b
	if sums + root.file_sizes <= k:
		res += sums + root.file_sizes
	sums += root.file_sizes
	return res, sums

def fill_subtree_sums(root, subtree_sums):
	sums = 0
	for child in root.children.values():
		b = fill_subtree_sums(child,subtree_sums)
		sums += b
	sums += root.file_sizes
	subtree_sums[root.name] = sums
	return sums

root_dir = Directory()
pwd = root_dir
i = 0
while i < len(lines):
	#print(pwd.name, pwd.file_sizes)
	if lines[i][:4] == '$ cd':
		d = lines[i].split()[-1]
		if d == '/':
			pwd = root_dir
		elif d == '..':
			pwd = pwd.parent
		else:
			if d not in pwd.children:
				pwd.children[d] = Directory(d, pwd)
			pwd = pwd.children[d]
	elif lines[i][:4] == '$ ls':
		i += 1
		dir_size = 0
		while i < len(lines) and lines[i][0] != '$':
			if lines[i][:3] != 'dir':
				size,file = lines[i].split()
				dir_size += int(size)
			i += 1
		pwd.file_sizes = dir_size
		i -= 1
	i += 1

part1 = sum_subtree_sums_at_most_k(root_dir)
print(f"PART 1: {part1}")

subtree_sums = {}
fill_subtree_sums(root_dir, subtree_sums)

TOTAL_DISK_SPACE = 70_000_000
TOTAL_USED_SPACE = subtree_sums['/']
SPACE_REQUIRED = 30_000_000
min_space = TOTAL_USED_SPACE - (TOTAL_DISK_SPACE - SPACE_REQUIRED)
print(min_space)
for val in subtree_sums.values():
	if val >= min_space:
		print(f"PART 2: {val}")
		break
