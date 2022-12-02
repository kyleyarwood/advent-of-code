with open('day1.in', 'r') as f:
	lines = [x.strip() for x in f.readlines()]

elf_meals = [[]]
for line in lines:
	if line == '':
		elf_meals.append([])
	else:
		elf_meals[-1].append(int(line))

most_calories_elf,most_calories=-1,-1
for elf,meals in enumerate(elf_meals):
	calories = sum(meals)
	if calories > most_calories:
		most_calories_elf,most_calories=elf,calories

print(f"PART 1: {most_calories}")

total_calories = [sum(elf_meal) for elf_meal in elf_meals]

result = sum(sorted(total_calories)[-3:])
print(f"PART 2: {result}")
