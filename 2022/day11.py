import operator
import inspect

with open('day11.in', 'r') as f:
	lines = [x.strip() for x in f.readlines()]

def make_operation(op1, op, op2):
	return lambda x: op(x if op1 == 'old' else int(op1), x if op2 == 'old' else int(op2))

def make_test(divisor):
	return lambda x: x%divisor == 0

class Monkey:
	def __init__(self, items, operation, divisor, true_monkey, false_monkey):
		self.items = items
		self.operation = operation
		self.divisor = divisor
		self.inspected_count = 0
		self.true_monkey = true_monkey
		self.false_monkey = false_monkey

monkeys = []
monkeys2 = []

for i in range(0, len(lines), 7):
	_, worry_levels = lines[i+1].split(': ')
	items = [int(x) for x in worry_levels.split(', ')]
	op1,op,op2 = lines[i+2].split()[-3:]
	op = operator.add if op == '+' else operator.mul
	operation = make_operation(op1, op, op2)
	divisor = int(lines[i+3].split()[-1])
	true_monkey = int(lines[i+4].split()[-1])
	false_monkey = int(lines[i+5].split()[-1])
	monkey = Monkey(items, operation, divisor, true_monkey, false_monkey)
	monkey2 = Monkey(items[::], operation, divisor, true_monkey, false_monkey)
	monkeys.append(monkey)
	monkeys2.append(monkey2)

def product(A):
	res = 1
	for x in A:
		res *= x
	return res


rounds = 20
for k in range(rounds):
	for i,monkey in enumerate(monkeys):
		for item in monkey.items:
			after_op = monkey.operation(item)
			new_worry_level = after_op//3
			if new_worry_level%monkey.divisor == 0:
				monkeys[monkey.true_monkey].items.append(new_worry_level)
			else:
				monkeys[monkey.false_monkey].items.append(new_worry_level)
			monkey.inspected_count += 1
		monkey.items = []

inspected_counts = [m.inspected_count for m in monkeys]
inspected_counts.sort()
res = inspected_counts[-1]*inspected_counts[-2]
print(f"PART 1: {res}")

rounds = 10000
BIG_MOD = product([m.divisor for m in monkeys])

for k in range(rounds):
    for i,monkey in enumerate(monkeys2):
        for item in monkey.items:
            after_op = monkey.operation(item)
            new_worry_level = after_op%BIG_MOD
            if new_worry_level%monkey.divisor == 0:
                monkeys2[monkey.true_monkey].items.append(new_worry_level)
            else:
                monkeys2[monkey.false_monkey].items.append(new_worry_level)
            monkey.inspected_count += 1
        monkey.items = []

inspected_counts = [m.inspected_count for m in monkeys2]
inspected_counts.sort()
res = inspected_counts[-1]*inspected_counts[-2]
print(f"PART 2: {res}")
