from file_lines import get_file_lines

lines = get_file_lines('day8.in')

def gcd(a,b):
	return a if b==0 else gcd(b, a%b)

rows,cols = 6,50
screen = [[0 for i in range(cols)] for j in range(rows)]

for line in lines:
	instr = line.split()
	if instr[0]=='rect':
		wide,tall = map(int, instr[1].split('x'))
		for i in range(tall):
			for j in range(wide):
				screen[i][j] = 1
	elif instr[1]=='row':
		row = int(instr[2][2:])
		by = int(instr[4])%cols
		screen[row] = screen[row][-by:] + screen[row][:-by]
	else:
		col = int(instr[2][2:])
		by = int(instr[4])%rows
		for i in range(by):
			tmp = screen[rows-1][col]
			for j in range(rows-1, 0, -1):
				screen[j][col] = screen[j-1][col]
			screen[0][col] = tmp
#print(screen)

result = sum(sum(row) for row in screen)
print(result)

for i in range(0,cols,5):
	for j in range(rows):
		for k in range(5):
			print(screen[j][i+k], end=' ')
		print()
	print()
