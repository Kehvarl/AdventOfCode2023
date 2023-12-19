from collections import defaultdict, deque
from copy import deepcopy
from pprint import pprint

with open("input.txt") as f:
    content = f.read()
    # content = [x.strip() for x in f.readlines()]

c_workflows, c_parts = content.split("\n\n")
c_workflows = [x.strip() for x in c_workflows.split('\n')]
c_parts = [x.strip() for x in c_parts.split('\n')]
workflows = {}
for w in c_workflows:
    name, rules = w.split('{')
    workflows[name] = []
    for r in rules[:-1].split(','):
        if ':' in r:
            op, output = r.split(':')
        else:
            op = 'True'
            output = r
        workflows[name].append((op, output))

parts = []
for p in c_parts:
    part = {}
    stats = p[1:-1].split(',')
    for s in stats:
        val, qty = s.split('=')
        part[val] = int(qty)
    parts.append(part)


def combinations(rng):
    r = 1
    for i in rng.values():
        r *= i[1] - i[0] + 1
    return r


def solve(part, workflow):
    accepted = 0
    # print(rng, flow)
    for rule in workflows[workflow]:
        if rule[0] == 'True':
            if rule[1] == "A":
                accepted += combinations(part)
            elif rule[1] != "R":
                accepted += solve(part, rule[1])
        else:
            q = rule[0][0]
            op = rule[0][1]
            val = int(rule[0][2:])
            if op == '>':
                new_rng = deepcopy(part)
                if new_rng[q][1] > val:
                    new_rng[q][0] = max(new_rng[q][0], val+1)
                    if rule[1] == "A":
                        accepted += combinations(new_rng)
                    elif rule[1] != "R":
                        accepted += solve(new_rng, rule[1])
                    part[q][1] = min(part[q][1], val)
            elif op == '<':
                new_rng = deepcopy(part)
                if new_rng[q][0] < val:
                    new_rng[q][1] = min(new_rng[q][1], val-1)
                    if rule[1] == "A":
                        accepted += combinations(new_rng)
                    elif rule[1] != "R":
                        accepted += solve(new_rng, rule[1])
                    part[q][0] = max(part[q][0], val)

    return accepted


print(solve({"x":[1, 4000], "m":[1, 4000], "a":[1, 4000], "s":[1, 4000]}, "in"))