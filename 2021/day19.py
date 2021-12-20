with open('day19.in', 'r') as f:
    data = [x.strip() for x in f.readlines()]

scanners = []
scanner = []
for line in data:
    if len(line) <= 1 or line[0]=='-':
        if scanner:
            scanners.append(scanner)
        scanner = []
    else:
        scanner.append(list(map(int, line.split(','))))

print(scanners)
    
def get_scanner_set(scanner, x_adj=0, y_adj=0, z_adj=0, rotation=0):
    s = [(x+x_adj, y+y_adj, z+z_adj) for x,y,z in scanner]
    if rotation==1:
        s = [() for x,y,z in scanner]


        '''
        (x,y) => 
        -x-x-
        x-S--
        -x---
        '''

        '''

        '''
    
THRESHOLD = 12
#center everything around the 1st scanner

