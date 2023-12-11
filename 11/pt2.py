from collections import defaultdict
from pprint import pprint

with open("test.txt") as f:
    content = f.readlines()
    #content = [int(x) for x in f.readlines()]


duplicate_rows = set()
duplicate_cols = set()
for i, v1 in enumerate(content):
    if all(c == '.' for c in v1.strip()):
        duplicate_rows.add(i)

for col in range(len(content[0])):
    empty = True
    for row in range(len(content)):
        if content[row][col] != '.':
            empty = False
            break
    if empty:
        duplicate_cols.add(col)

x = 0
y = 0
galaxies = set()
for row in range(len(content)):
    if row in duplicate_rows:
        y += 999999
    x = 0
    for col in range(len(content[0].strip())):
        if col in duplicate_cols:
            x += 999999
        if content[row][col] == "#":
            galaxies.add((x, y))
        x += 1
    y += 1

#print(duplicate_cols)
#print(duplicate_rows)
#print(galaxies)


def taxicab(a, b):
    dx = max(a[0], b[0]) - min(a[0], b[0])
    dy = max(a[1], b[1]) - min(a[1], b[1])
    return dx + dy


pairs = set()
distances = []
for g1 in galaxies:
    for g2 in galaxies:
        if g1 == g2:
            continue
        if (g1, g2) in pairs or (g2, g1) in pairs:
            continue
        pairs.add((g1, g2))
        distances.append(taxicab(g1, g2))

#print(pairs)
#print(len(distances))
#print(distances)
print(sum(distances))



