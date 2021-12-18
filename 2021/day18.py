import json
from copy import deepcopy

class Tree:
    def __init__(self, val=None, left=None, right=None):
        self.is_list = False
        self.left = None
        self.right = None
        self.val = None
        if left is not None:
            self.is_list = True
            self.left = left
            self.right = right
        elif isinstance(val, list):
            self.is_list = True
            self.left = Tree(val[0])
            self.right = Tree(val[1])
        else:
            self.val = val

    def __str__(self):
        if not self.is_list:
            return str(self.val)
        left = str(self.left)
        right = str(self.right)
        return f"{left} {right}"

with open('day18.in', 'r') as f:
    data = [x.strip() for x in f.readlines()]

trees = [Tree(json.loads(line)) for line in data]

def get_first_depth_four_path(tree, path, depth=0):
    if depth==4 and tree.is_list:
        return ''.join(path)
    if not tree.is_list:
        return None
    path.append('L')
    left = get_first_depth_four_path(tree.left, path, depth+1)
    if left is not None:
        return left
    path[-1] = 'R'
    right = get_first_depth_four_path(tree.right, path, depth+1)
    path.pop()
    return right

def get_in_order(tree):
    if not tree.is_list:
        return [tree]
    return get_in_order(tree.left) + get_in_order(tree.right)

def get_first_large_regular_number(tree, threshold=10):
    if not tree.is_list:
        if tree.val >= threshold:
            return tree
        return None
    left = get_first_large_regular_number(tree.left, threshold)
    if left is not None:
        return left
    return get_first_large_regular_number(tree.right, threshold)

def condense_tree(tree):
    while True:
        path=[]
        first_depth_four_path = get_first_depth_four_path(tree, path)
        if first_depth_four_path is not None:
            node = tree
            for x in first_depth_four_path:
                if x=='L': node = node.left
                else: node = node.right
            in_order = get_in_order(tree)
            i = 0
            while in_order[i] != node.left:
                i += 1
            if i > 0:
                in_order[i-1].val += node.left.val
            if i+2 < len(in_order):
                in_order[i+2].val += node.right.val
            node.is_list = False
            node.left = node.right = None
            node.val = 0
        else:
            first_large_regular_number = get_first_large_regular_number(tree)
            if first_large_regular_number is None:
                break
            left = first_large_regular_number.val//2
            right = (first_large_regular_number.val+1)//2
            first_large_regular_number.val = None
            first_large_regular_number.is_list = True
            first_large_regular_number.left = Tree(val=left)
            first_large_regular_number.right = Tree(val=right)
    


def get_magnitude(tree):
    if tree.is_list:
        return 3*get_magnitude(tree.left) + 2*get_magnitude(tree.right)
    return tree.val

def add_tree(t1, t2):
    t = Tree(left=t1, right=t2)
    condense_tree(t)
    return t

def add_trees(trees):
    result = trees[0]
    for tree in trees[1:]:
        result = add_tree(result, tree)
    return result

result = add_trees(trees)
magnitude = get_magnitude(result)
print(f"Part 1: {magnitude}")

trees = [Tree(json.loads(line)) for line in data]
result = 0
for i,t1 in enumerate(trees):
    for j,t2 in enumerate(trees):
        if i==j:
            continue
        result = max(result, get_magnitude(add_tree(deepcopy(t1),deepcopy(t2))))
print(f"Part 2: {result}")
