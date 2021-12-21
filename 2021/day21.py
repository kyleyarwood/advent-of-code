with open('day21.in', 'r') as f:
    data = [int(x.strip()[-1]) for x in f.readlines()]

def part1(data):
    player1 = player2 = 0
    is_player1 = True
    x = 0
    p1, p2 = map(lambda x: x-1, data)
    while player1 < 1000 and player2 < 1000:
        y = 3*x + 6
        x += 3
        if is_player1:
            p1 = (p1 + y)%10
            player1 += p1+1
        else:
            p2 = (p2 + y)%10
            player2 += p2+1
        is_player1 = not is_player1
    if player1 < 1000:
        return player1*x
    return player2*x


result = part1(data)
print(result)

THRESHOLD = 21

def part2(memo, p1, p2, player1=0, player2=0):
    if player2 >= THRESHOLD:
        return (0, 1)
    if (p1, p2, player1, player2) not in memo:
        ress = []
        for i in range(1, 4):
            for j in range(1, 4):
                for k in range(1,4):
                    new_p1 = (p1+i+j+k)%10
                    ress.append(part2(memo, p2, new_p1, player2, player1 + new_p1+1))
        x = sum(e[0] for e in ress)
        y = sum(e[1] for e in ress)
        memo[(p1, p2, player1, player2)] = (y-x, y)
    return memo[(p1, p2, player1, player2)]



memo = {}
result = part2(memo, data[0]-1, data[1]-1)
most_wins = max(result[0], result[1]-result[0])
print(most_wins)