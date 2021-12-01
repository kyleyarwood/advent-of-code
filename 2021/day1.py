with open('day1.in', 'r') as f:
	data = list(map(int, f.readlines()))

#part 1
result = sum(data[i+1] > data[i] for i in range(len(data)-1))
print(result)


#part 2
result = sum(data[i+3] > data[i] for i in range(len(data)-3))
print(result)
