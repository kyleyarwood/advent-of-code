from file_lines import get_file_lines
from collections import defaultdict


lines = get_file_lines('day10.in')

curr_chips = defaultdict(list)
outputs = defaultdict(list)
comps = {}

for line in lines:
	words = line.split()
	if words[0] == 'value':
		curr_chips['b'+words[5]].append(int(words[1]))
	else:
		bot = 'b'+words[1]
		lo = ('b' if words[5]=='bot' else 'o')+words[6]
		hi = ('b' if words[-2]=='bot' else 'o')+words[-1]
		comps[bot] = (lo, hi)

while curr_chips:
	for bot in list(curr_chips.keys()):
		if len(curr_chips[bot])==2:
			lo,hi = sorted(curr_chips[bot])
			if lo==17 and hi==61:
				print(bot)
			if comps[bot][0][0]=='o':
				outputs[comps[bot][0]].append(lo)
			else:
				curr_chips[comps[bot][0]].append(lo)
			if comps[bot][1][0]=='o':
				outputs[comps[bot][1]].append(hi)
			else:
				curr_chips[comps[bot][1]].append(hi)
			del curr_chips[bot]

result = 1
for i in map(str, range(3)):
	result *= outputs['o'+i][0]
print(result)


