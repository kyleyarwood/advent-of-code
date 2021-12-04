with open('day4.in', 'r') as f:
	lines = [x.strip() for x in f.readlines()]

def has_board_won(board):
	if any(all(x[1] for x in row) for row in board) or any(all(board[i][j][1] for i in range(len(board))) for j in range(len(board[0]))):
		return True
	#for i in range(5):
	#	if not board[i][i][1]:
	#		break
	#else:
	#	return True
	#for i in range(5):
	#	if not board[i][-i-1][1]:
	#		break
	#else:
	#	return True
	return False

numbers_called = [int(x) for x in lines[0].split(',')]

def create_board(lines):
	board = []
	for line in lines:
		new_row = [[int(x), False] for x in line.split()]
		board.append(new_row)
	return board

def fill_number(board, number):
	for i in range(len(board)):
		for j in range(len(board[i])):
			if board[i][j][0] == number and not board[i][j][1]:
				board[i][j][1] = True
				return True
	return False

def score_of_board(board, num):
	result = 0
	for row in board:
		for val in row:
			if not val[1]:
				result += val[0]
	return result*num

boards = []
part_2_boards = []
for i in range(2, len(lines), 6):
	boards.append(create_board(lines[i:i+5]))
	part_2_boards.append(create_board(lines[i:i+5]))


res = -1
num = -1
for number in numbers_called:
	for i,board in enumerate(boards):
		x = fill_number(board, number)
		if x and has_board_won(board):
			res = i
			num = number
			break
	else:
		continue
	break

result = score_of_board(boards[res], num)
print(result)

#part 2
res = num = -1
solved_boards = set()
for number in numbers_called:
	for i,board in enumerate(part_2_boards):
		x = fill_number(board, number)
		if x and has_board_won(board):
			solved_boards.add(i)
			if len(solved_boards) == len(part_2_boards):
				res = i
				num = number
				break
	else:
		continue
	break

result = score_of_board(part_2_boards[res], num)
print(result)
print(all(has_board_won(board) for board in part_2_boards))
