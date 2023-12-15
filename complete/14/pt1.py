from collections import defaultdict
from pprint import pprint

with open("input.txt") as f:
    #content = f.readlines()
    content = [x.strip() for x in f.readlines()]

grid = {}
w = len(content[0])
h = len(content)
for y, v1 in enumerate(content):
    for x, v2 in enumerate(v1):
        grid[(x, y)] = v2

for y in range(h):
    for x in range(w):
        if grid[(x, y)] == 'O':
            grid[(x, y)] = "."
            pos = (x, y)
            for d in range(1, y+1):
                iy = y-d
                if iy >= 0 and grid[(x, iy)] == ".":
                    pos = (x, iy)
                else:
                    break
            grid[pos] = 'O'


ans = 0
for y in range(h):
    line = ""
    for x in range(w):
        line += grid[(x, y)]
        if grid[(x, y)] == 'O':
            ans += h-y
    print(line)

print(ans)
