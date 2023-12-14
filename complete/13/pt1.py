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
    h_reflections = set()
    for row, line in enumerate(content):
        if row < len(content)-1 and line == content[row + 1]:
            h_reflections.add(row)

    v_reflections = set()
    for col in range(0, len(content[0]) - 1):
        reflect = True
        for row in range(len(content)):
            if content[row][col] != content[row][col + 1]:
                reflect = False
                break
        if reflect:
            v_reflections.add(col)

    h_kept = set()
    for r in h_reflections:
        d = 0
        good = True
        while good and r - d >= 0 and r + d < (len(content) - 1):
            if content[r - d] != content[r + d + 1]:
                good = False
            d += 1
        if good:
            h_kept.add(r)

    v_kept = set()
    for c in v_reflections:
        d = 0
        good = True
        while good and c - d >= 0 and c + d < (len(content[0]) - 1):
            for row in range(len(content)):
                if content[row][c - d] != content[row][c + d + 1]:
                    good = False
            d += 1
        if good:
            v_kept.add(c)

    print(h_reflections, h_kept, v_reflections, v_kept)
    return h_kept, v_kept

v = 0
h = 0
for p in patterns:
    #print(reflections(p))
    hr, vr = reflections(p)
    if len(hr) == len(vr) == 0:
        pprint(p)
        print()
    for r1 in hr:
        h += (r1+1)*100
    for r2 in vr:
        v += r2 + 1

print(v, h, v+h)
