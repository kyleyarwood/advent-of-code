from collections import defaultdict

with open('day22.in', 'r') as f:
    data = [x.strip() for x in f.readlines()]

on = []

def overlap(x,a):
    return (max(x[0], a[0]), min(x[1], a[1]))

def overlap(x,y,z,a,b,c):
    xs = overlap(x,a)
    ys = overlap(y,b)
    zs = overlap(z,c)
    return xs,ys,zs

d = {}
for line in data:
    switch,ranges = line.split()
    x,y,z = ranges.split(',')
    xs,xe = map(int, x.split('=')[-1].split('..'))
    ys,ye = map(int, y.split('=')[-1].split('..'))
    zs,ze = map(int, z.split('=')[-1].split('..'))
    for x in range(max(xs,-50), min(xe,50)+1):
        for y in range(max(ys,-50), min(ye,50)+1):
            for z in range(max(zs,-50), min(ze,50)+1):
                d[(x,y,z)] = int(switch == 'on')
result = sum(d.values())
print(result)
'''
overlaps = []
for a,b,c in on:
    xs,ys,zs = overlap(x,y,z,a,b,c)
    if 
    overlaps.append((1-2*int(switch=='off'),xs,ys,zs))
on.append((int(switch=='on'), (xs,xe),(ys,ye),(zs,ze)))
'''


