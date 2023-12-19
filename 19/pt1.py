from collections import defaultdict, deque
from pprint import pprint

with open("input.txt") as f:
    content = f.read()
    #content = [x.strip() for x in f.readlines()]

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


accepted = []
for part in parts:
    current = 'in'
    working = True
    while working:
        work = workflows[current]
        for rule in work:
            next_workflow = current
            if rule[0] == 'True':
                next_workflow = rule[1]
            else:
                q = rule[0][0]
                op = rule[0][1]
                val = int(rule[0][2:])
                if op == '>':
                    if part[q] > val:
                        next_workflow = rule[1]
                elif op == '<':
                    if part[q] < val:
                        next_workflow = rule[1]
                else:
                    print(op, " Not in rules")

            if next_workflow == 'A':
                accepted.append(part)
                working = False
                break
            elif next_workflow == 'R':
                working = False
                break
            elif next_workflow != current:
                current = next_workflow
                break

print(accepted)
print(len(accepted))

total = 0
for a in accepted:
    for key in a:
        total += a[key]
print(total)


