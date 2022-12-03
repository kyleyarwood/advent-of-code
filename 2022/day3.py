with open('day3.in', 'r') as f:
	rucksacks = [x.strip() for x in f.readlines()]
rucksacks.pop()
res = 0
for rucksack in rucksacks:
	n = len(rucksack)
	first,second = rucksack[:n//2],rucksack[n//2:]
	common = list(set(first).intersection(set(second)))[0]
	res += 26*common.isupper() + (ord(common.lower()) - ord('a') + 1)

print(f"PART 1: {res}")

res = 0
for i in range(0, len(rucksacks), 3):
	common = list(set(rucksacks[i]).intersection(set(rucksacks[i+1])).intersection(set(rucksacks[i+2])))[0]
	res += 26*common.isupper() + ord(common.lower()) - ord('a') + 1

print(f"PART 2: {res}")
