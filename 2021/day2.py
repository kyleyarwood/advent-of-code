with open('day2.in', 'r') as f:
    lines = f.readlines()

#part 1
result = 0
hor1 = depth1 = hor2 = depth2 = aim = 0

for x in lines:
    a,b = x.split()
    b = int(b)
    if a=='forward':
        hor1 += b
        hor2 += b
        depth2 += aim*b
    elif a=='down':
        depth1 += b
        aim += b
    else:
        depth1 -= b
        aim -= b
print(f"Part 1: {hor1*depth1}")
print(f"Part 2: {hor2*depth2}")
