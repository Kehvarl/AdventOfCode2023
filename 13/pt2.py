from collections import defaultdict
from pprint import pprint

with open("input.txt") as f:
    content = f.readlines()
    # content = [x.strip() for x in f.readlines()]

patterns = []
pattern = []

for r in content:
    if r == "\n":
        patterns.append(pattern)
        pattern = []
    else:
        pattern.append(r.strip())
patterns.append(pattern)


def reflections(content):
    h_kept = set()
    for row in range(len(content) - 1):
        smudges = 0
        for r in range(len(content)):
            if (row - r) >= 0 and (row + 1 + r) < len(content):
                for c in range(0, len(content[0])):
                    if content[row-r][c] != content[row+1+r][c]:
                        smudges += 1
        if smudges == 1:
            h_kept.add(row)

    v_kept = set()
    for col in range(len(content[0]) - 1):
        smudges = 0
        for c in range(len(content[0])):
            if (col - c) >= 0 and (col + 1 + c) < len(content[0]):
                for row in range(len(content)):
                    if content[row][col - c] != content[row][col + c + 1]:
                        smudges += 1
        if smudges == 1:
            v_kept.add(col)

    return h_kept, v_kept

v = 0
h = 0
for p in patterns:
    hr, vr = reflections(p)
    print(hr, vr)
    for r1 in hr:
        h += (r1+1)*100
    for r2 in vr:
        v += r2 + 1

print(v, h, v+h)
