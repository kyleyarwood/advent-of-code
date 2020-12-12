from file_lines import get_file_lines

lines = get_file_lines('day12.in')

dx,dy = 1,0
x,y=0,0

def manhattan(x,y):
	return abs(x) + abs(y)

def R(dx,dy):
	return dy,-dx

def R_by_deg(dx, dy, deg):
	deg = deg%360
	n_turns = deg//90
	for i in range(n_turns):
		dx,dy=R(dx,dy)
	return dx,dy

def L_by_deg(dx,dy,deg):
	deg = deg%360
	deg = 360 - deg
	return R_by_deg(dx,dy,deg)

for cmd in lines:
	action, amount = cmd[0], int(cmd[1:])
	if action=='N':
		y += amount
	elif action=='S':
		y -= amount
	elif action=='E':
		x += amount
	elif action=='W':
		x -= amount
	elif action=='F':
		x += dx*amount
		y += dy*amount
	elif action=='R':
		dx,dy=R_by_deg(dx,dy,amount)
	else:
		dx,dy=L_by_deg(dx,dy,amount)

result = manhattan(x,y)
print(result)

x,y=0,0
wrx,wry=10,1

for cmd in lines:
	action, amount = cmd[0], int(cmd[1:])
	if action=='N':
		wry += amount
	elif action=='S':
		wry -= amount
	elif action=='E':
		wrx += amount
	elif action=='W':
		wrx -= amount
	elif action=='F':
		x += wrx*amount
		y += wry*amount
	elif action=='L':
		wrx,wry = L_by_deg(wrx,wry,amount)
	else:
		wrx,wry = R_by_deg(wrx,wry,amount)

result = manhattan(x,y)
print(result)
