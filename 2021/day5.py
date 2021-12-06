with open('day5.in', 'r') as f:
    lines = [x.strip() for x in f.readlines()]

result = 0
#print(len(lines))
'''
for i,l1 in enumerate(lines):
    s1,e1 = l1.split(' -> ')
    ax,ay = map(int, s1.split(','))
    bx,by = map(int, e1.split(','))
    for l2 in lines[i+1:]:
        s2,e2 = l2.split(' -> ')
        cx,cy = map(int, s2.split(','))
        dx,dy = map(int, e2.split(','))
        if cx==dx and ax==bx:
            if ax != cx:
                continue
            ay,by = sorted([ay,by])
            cy,dy = sorted([cy,dy])
            result += max(0, min(by,dy)-max(ay,cy)+1)
        elif cx==dx:
            ax,bx = sorted([ax,bx])
            if not (ax <= cx <= bx):
                continue
            cy,dy = sorted([cy,dy])
            if cy <= ay <= dy:
                result += 1
        elif ay==by:
            if ay != cy:
                continue
            ax,bx = sorted([ax,bx])
            cx,dx = sorted([cx,dx])
            result += max(0, min(bx,dx)-max(ax,cx)+1)
        else:
            ay,by = sorted([ay,by])
            if not (ay <= cy <= by):
                continue
            cx,dx = sorted([cx,dx])
            if cx <= ax <= dx:
                result += 1
'''
n = 1000
mx = my = 0
grid = [[0 for i in range(n)] for j in range(n)]
for i,line in enumerate(lines):
    s,e = line.split(' -> ')
    ax,ay = map(int, s.split(','))
    bx,by = map(int, e.split(','))
    if ax!=bx and ay!=by:
        continue
    ax,bx = sorted([ax,bx])
    ay,by = sorted([ay,by])
    mx,my = max(mx,bx),max(my,by)
    for i in range(ax,bx+1):
        for j in range(ay,by+1):
            grid[i][j] += 1
result = sum(grid[i][j] > 1 for i in range(n) for j in range(n))
print(result, mx,my)

grid = [[0 for i in range(n)] for j in range(n)]
for i,line in enumerate(lines):
    s,e = line.split(' -> ')
    ax,ay = map(int, s.split(','))
    bx,by = map(int, e.split(','))
    #if ax==bx or ay==by:
    #    continue
    if ax!=bx and ay!=by:
        if ax <= bx:
            if ay <= by:
                for i in range(ax,bx+1):
                    grid[i][ay+i-ax] += 1
            else:
                for i in range(ax,bx+1):
                    grid[i][ay-i+ax] += 1
        elif ay >= by:
            for i in range(bx,ax+1):
                grid[i][by+i-bx] += 1
        else:
            for i in range(bx,ax+1):
                grid[i][by-i+bx] += 1
        #for i in range(min(ax,bx), max(ax,bx)+1):
        #    grid[i][min(ay,by)+i-min(ax,bx)] += 1
        continue
    ax,bx = sorted([ax,bx])
    ay,by = sorted([ay,by])
    mx,my = max(mx,bx),max(my,by)
    for i in range(ax,bx+1):
        for j in range(ay,by+1):
            grid[i][j] += 1

print('\n'.join(map(str, grid)))
result = sum(grid[i][j] > 1 for i in range(n) for j in range(n))
print(result, mx,my)
