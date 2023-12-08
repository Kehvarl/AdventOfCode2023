from collections import defaultdict
from pprint import pprint
from math import gcd

with open("input.txt") as f:
    content = f.readlines()
    #content = [int(x) for x in f.readlines()]

instructions = content[0].strip()

tree = {}
alist = []
for v1 in content[2:]:
    node, branches = v1.strip().split(" = ")
    if node[2] == 'A':
        alist.append(node)
    left, right = branches.replace("(", "").replace(")", "").split(", ")
    tree[node] = {"L":left, "R":right}

instruction_index = 0
outputs = []
for current in alist:
    instruction_index = 0
    while current[2] != "Z":
        i = instructions[instruction_index % len(instructions)]
        instruction_index += 1
        current = tree[current][i]
    outputs.append(instruction_index)

lcm = 1
for c in outputs:
    lcm = lcm * c // gcd(lcm, c)
print(lcm)
