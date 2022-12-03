with open('day2.in', 'r') as f:
    lines = [x.strip() for x in f.readlines()]

opp_strats = ['A', 'B', 'C']
my_strats = ['X', 'Y', 'Z']

res = 0
for line in lines:
    if not line:
        continue
    opp,my = line.split()
    opp_i = opp_strats.index(opp)
    my_i = my_strats.index(my)
    if opp_i == my_i:
        res += 3
    elif (my_i - opp_i)%3 == 1:
        res += 6
    res += my_i + 1

print(f"PART 1: {res}")

res = 0
for line in lines:
    if not line:
        continue
    opp,my = line.split()
    opp_i = opp_strats.index(opp)
    if my == 'X':
        my_i = (opp_i - 1)%3
    elif my == 'Y':
        res += 3
        my_i = opp_i
    else:
        res += 6
        my_i = (opp_i + 1)%3
    res += my_i + 1

print(f"PART 2: {res}")
