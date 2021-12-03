with open('day3.in', 'r') as f:
	lines = [x.strip() for x in f.readlines()]
bits = len(lines[0])
def get_counts(strings):
	counts = [0 for i in range(bits)]
	for word in strings:
		for i,c in enumerate(word):
			if c=='1':
				counts[i] += 1
	return counts
counts = get_counts(lines)

gamma = ['1' if counts[i] > len(lines)//2 else '0' for i in range(bits)]
gamma = int(''.join(gamma), 2)
result = gamma*(2**bits-1-gamma)
print(result)

#part 2
def get_o2_co2(strings):
	i = 0
	o2 = strings[:]
	co2 = strings[:]
	while i < bits:
		o2counts = get_counts(o2)
		co2counts = get_counts(co2)
		o2mostcommon = '1' if o2counts[i] >= (len(o2)+1)//2 else '0'
		co2leastcommon = '0' if co2counts[i] >= (len(co2)+1)//2 else '1'
		if len(o2)>1:
			o2 = [x for x in o2 if x[i] == o2mostcommon]
		if len(co2)>1:
			co2 = [x for x in co2 if x[i] == co2leastcommon]
		i += 1
	return map(lambda x: int(x[0], 2), (o2, co2))

o2,co2 = get_o2_co2(lines)
print(o2*co2)
