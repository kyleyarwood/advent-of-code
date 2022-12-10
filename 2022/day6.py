with open('day6.in', 'r') as f:
	data = f.read().strip()

length = 4

res = -1
for i in range(len(data)-length+1):
	if len(set(data[i:i+length])) == length:
		res = i+length
		break
print(f"PART 1: {res}")

length = 14

res = -1
for i in range(len(data)-length+1):
    if len(set(data[i:i+length])) == length:
        res = i+length
        break
print(f"PART 1: {res}")

