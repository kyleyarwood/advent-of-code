from file_lines import get_file_lines

lines = get_file_lines('day18.in')

def is_int(x):
	try:
		x = int(x)
		return True
	except:
		return False

def evaluate(expr, i=0):
	results = [[0, lambda x,y: x+y]]
	while i < len(expr):
		if is_int(expr[i]):
			results[-1][0] = results[-1][1](results[-1][0], int(expr[i]))
			print(results)
		elif expr[i] == '(':
			results.append([0, lambda x,y: x+y])
		elif expr[i] == ')':
			result = results.pop()
			results[-1][0] = results[-1][1](results[-1][0], result[0])
			print(results)
		elif expr[i] == '+':
			results[-1][1] = lambda x,y: x+y
		else:
			results[-1][1] = lambda x,y: x*y
		i += 1
	return results[0][0]

class ExpressionNode:
	def __init__(self):
		self.left = None
		self.right = None
		self.is_val = True
		self.val = 0
		self.operator = None

def addition_precedence_evaluate(expr):
	

lines = list(map(lambda line: line.replace('(', '( ').replace(')', ' )').split(), lines))
result = sum(evaluate(line) for line in lines)
print(result)
