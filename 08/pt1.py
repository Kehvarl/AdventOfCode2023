from collections import defaultdict
from pprint import pprint

with open("input.txt") as f:
    content = f.readlines()
    #content = [int(x) for x in f.readlines()]

instructions = content[0].strip()

tree = {}
for v1 in content[2:]:
    node, branches = v1.strip().split(" = ")
    left, right = branches.replace("(", "").replace(")", "").split(", ")
    tree[node] = {"L":left, "R":right}


def find(find_tree, result):
    for node in find_tree:
        if result == find_tree[node][0]:
            return (node, "R")
        elif result == find_tree[node][1]:
            return (node, "L")
    return (None, "")


current = "AAA"
target = "ZZZ"
steps = []
instruction_index = 0
while current != target:
    #print(current, tree[current], instructions[instruction_index], tree[current][instructions[instruction_index]])
    current = tree[current][instructions[instruction_index]]
    steps.append(current)
    instruction_index += 1
    if instruction_index >= len(instructions):
        instruction_index = 0

print(steps, len(steps))